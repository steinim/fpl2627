#!/usr/bin/env python3
"""Byttepakker: hvilke bytter i de to neste rundene gir flest forventede poeng over horisonten,
regnet med salgspris, bank, klubbgrense, frikjøp og minuspoeng.

Bygger på scripts/forventning.py (forventede poeng og sannsynlighet for å spille, per spiller og
runde) og speilets lagdata: entry/picks/gw{n}.json (tropp og bank), entry/transfers.json
(innkjøpspriser) og entry/history.json (bytter, kostnad og chips per runde). Kun stdlib.

Bruk (fra reporoten):
    python3 scripts/bytter.py                          # skriv analyse/bytter.md
    python3 scripts/bytter.py --stdout                 # til stdout, skriv ingenting
    python3 scripts/bytter.py --runder 6               # horisont (standard 5)
    python3 scripts/bytter.py --maks-hits 1            # tillat ett bytte utover frikjøpene per runde
    python3 scripts/bytter.py --vis-ut 426,1           # beste planer som selger disse
    python3 scripts/bytter.py --ekstra-bytter "Gibbs-White>Groß,N.Williams>Thomas@COV"
                                                       # bytter gjort etter siste speiling
                                                       # (navn, navn@LAG eller element-id)
    python3 scripts/bytter.py --frikjop 1 --bank 0.3   # overstyr beregnet frikjøp og bank
    python3 scripts/bytter.py --kilde DIR              # les speilets data/-struktur fra en mappe

LAGETS POENG I EN RUNDE
=======================
  - De elleve beste på forventning: 1 keeper, minst 3 forsvarere, minst 1 spiss (05, seksjon 1).
    Med troppen 2/5/5/3 gir det automatisk minst 2 midtbanespillere.
  - Kapteinsledd: kapteinens forventning + P(kapteinen spiller ikke) × visekapteinens (05:
    bindet går til visekapteinen når kapteinen spiller null minutter). Kapteinen er den av de tre
    beste som gir størst ledd; visekapteinen den beste av de andre.
  - Innbytterledd: sannsynligheten for at hver benkespiller kommer inn, regnet over alle
    kombinasjoner av fravær per posisjon og hvilke benkespillere som spilte, etter regelen i 05:
    keeper bare for keeper; hver utespiller som ikke spilte, byttes mot den høyest prioriterte
    innbytteren som spilte og ikke bryter formasjonen (minst 3 forsvarere og 1 spiss). Benken
    sorteres på forventning. Fravær antas uavhengige. Kombinasjoner under 1e−7 hoppes over.
    Kort fra benken (05: teller som å ha spilt) er ikke med.
  Spillernes forventning og P(spiller) kommer fra forventning.py og inkluderer tilgjengelighet
  (FPL-status og context/fravaer.csv). Benkerekkefølgen antas å følge forventningen.

PLANER
======
Bytter i første runde i horisonten (A) og/eller i andre (B). Verdi = sum av lagets poeng over
horisonten − 4 per bytte utover frikjøpene (05, seksjon 2). Et bytte gjelder fra runden det tas.
  Frikjøp:      FT(B) = min(5, FT(A) − bytter(A) + 1), aldri under 1.
  Bank:         ≥ 0 etter byttene i hver runde.
  Salgspris:    innkjøpspris + halve stigningen rundet ned til £0,1m; ved fall det lavere
                beløpet (05, seksjon 2).
  Innkjøpspris: siste kjøp i entry/transfers.json; spillere fra første tropp har startprisen
                (prisene endres ikke før sesongstart, 05).
  Klubbgrense:  maks 3 per klubb etter hver runde.
  Reglene kontrolleres mot API-ets game_config.rules ved hver kjøring. Bankkjeden (overganger
  mot bank i historikken) og frikjøpskjeden (bytter og kostnad mot historikken) kontrolleres
  runde for runde. Avvik stopper kjøringen.

SØK
===
Kandidater per posisjon: de 25 beste på forventning over horisonten, og de 10 beste per million
blant dem med minst halvparten av posisjonens beste forventning. Alle enkeltbytter vurderes i A
og i B. Kombinasjoner beskjæres med en rangering som ser bort fra bank og klubbgrense, slik at et
salg i A som finansierer et kjøp i B blir funnet selv om salget alene taper poeng:
  - én i A + én i B: alle enkeltbytter i A × utvalget for B
  - to i B etter å ha spart i A (når frikjøpene eller --maks-hits tillater det)
  - to i A, to i A + én i B, én i A + to i B (bare når frikjøpene eller --maks-hits tillater det)
Utvalget for B: de 80 beste, de 2 beste for hver spiller i troppen, og de 3 beste for hver
spiller blant bytter som frigjør minst £1,0m. Søket er ikke uttømmende for kombinasjoner.
Prisendringer før byttet og bytter i tredje runde eller senere er ikke modellert. Heller ikke de
operative reglene i context/01 (template i premiumslottene, differensialer, ett bytte per runde);
eierandelen står i rapporten så de kan sjekkes.

USIKKERHET
==========
I tilbaketesten avviker realiserte poeng over fem runder i snitt 5,1–5,8 poeng per spiller fra
forventningen (MAE), og r er 0,56–0,63. En planforskjell på noen få poeng er en svak preferanse,
ikke en dom. Robust endring (uten hver spillers beste xGI-kamp) viser om en plan hviler på én
enkeltkamp.
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import datetime as dt
import functools
import itertools
import math
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import forventning as fv  # noqa: E402

UT_MD = pathlib.Path("analyse/bytter.md")

# Regler (05). Kontrolleres mot API-ets game_config.rules i kontroller_regler.
HIT = 4
TROPP_FORM = {"GKP": 2, "DEF": 5, "MID": 5, "FWD": 3}
MAKS_PER_KLUBB = 3
MAKS_FRIKJOP = 5
SALGSANDEL = 0.5

# Søk.
K_XP = 25
K_VERDI = 10
TOPP_B = 80
TOPP_PER_SPILLER = 2
TOPP_FRIGJOR = 3
FRIGJOR_MIN = 10            # tideler av £m
TOPP_PAR = 30
TOPP_PAR_B = 200


# --------------------------------------------------------------------------- regler


def salgspris(innkjop: int, naa: int) -> int:
    """Salgspris i tideler av £m (05, seksjon 2)."""
    return innkjop + (naa - innkjop) // 2 if naa > innkjop else naa


def kontroller_regler(regler: dict) -> tuple[list[str], list[str]]:
    if not regler:
        return ["game_config.rules mangler i bootstrap — bytteregler kan ikke kontrolleres"], []
    forventet = {
        "squad_team_limit": MAKS_PER_KLUBB,
        "max_extra_free_transfers": MAKS_FRIKJOP - 1,
        "transfers_sell_on_fee": SALGSANDEL,
        "element_sell_at_purchase_price": False,
        "squad_squadsize": sum(TROPP_FORM.values()),
    }
    avvik = [f"{k}: API {regler.get(k)!r}, skriptet {v!r}" for k, v in forventet.items() if regler.get(k) != v]
    if avvik:
        return ["bytteregler i API-et avviker fra 05 og skriptet: " + "; ".join(avvik)], []
    return [], ["Bytteregler i API-et stemmer med 05 og skriptet: maks 3 per klubb, maks 5 frikjøp, "
                "halve prisstigningen ved salg, tropp på 15"]


def frikjop(historikk: dict, kjente_bytter: dict[int, int], til_runde: int,
            maks: int = MAKS_FRIKJOP) -> tuple[int | None, list[str], list[str]]:
    """Frikjøp tilgjengelig i til_runde, regnet runde for runde fra lagets første runde.

    historikk = entry/history.json. kjente_bytter = antall bytter per runde for runder som ikke
    står i historikken ennå. Returnerer (frikjøp, forklaring, feil). Kostnaden i historikken
    kontrolleres mot frikjøpene: avvik betyr at beregningen er feil, og stopper kjøringen."""
    rader = {h["event"]: h for h in historikk.get("current", [])}
    chips = {c["event"]: c["name"] for c in historikk.get("chips", [])}
    forklaring: list[str] = []
    feil: list[str] = []
    if not rader:
        return None, forklaring, ["historikken er tom — bruk --frikjop"]
    ft: int | None = None
    for e in range(min(rader), til_runde):
        if e in rader:
            brukt, kostnad = rader[e]["event_transfers"], rader[e]["event_transfers_cost"]
        elif e in kjente_bytter:
            brukt, kostnad = kjente_bytter[e], None
        else:
            return None, forklaring, [f"antall bytter i GW{e} er ukjent — bruk --frikjop eller --ekstra-bytter"]
        chip = chips.get(e)
        if ft is None:
            neste = 1
            forklaring.append(f"GW{e}: første runde → 1")
        elif chip in ("wildcard", "freehit"):
            neste = min(maks, ft + 1)
            forklaring.append(f"GW{e}: {chip}, sparte overlever (05); +1 etter chipen ikke verifisert → {neste}")
            feil.append(f"frikjøp etter {chip} i GW{e} er ikke verifisert mot 05 — kontroller i appen og bruk --frikjop")
        else:
            hits = max(0, brukt - ft)
            if kostnad is not None and kostnad != HIT * hits:
                feil.append(f"GW{e}: {brukt} bytter med {ft} frikjøp gir {HIT * hits} i kostnad, historikken sier "
                            f"{kostnad} — frikjøpsberegningen stemmer ikke")
            neste = min(maks, max(0, ft - brukt) + 1)
            forklaring.append(f"GW{e}: {ft} frikjøp, {brukt} brukt" + (f", {hits} hit" if hits else "") + f" → {neste}")
        ft = neste
    return ft, forklaring, feil


# --------------------------------------------------------------------------- tropp


@dataclasses.dataclass
class Spiller:
    eid: int
    navn: str
    pos: str
    lag: int
    pris: int                  # nåpris, tideler av £m
    xp: list[float]            # forventede poeng per runde i horisonten
    xr: list[float]            # robust variant
    p: list[float]             # P(spiller) per runde
    eierandel: float = 0.0     # eierandel i prosent (selected_by_percent)


@dataclasses.dataclass
class Tilstand:
    tropp: list[int]
    innkjop: dict[int, int]
    bank: int
    frikjop: int
    runde: int                 # første runde i horisonten (A)
    ok: list[str]
    advarsler: list[str]
    feil: list[str]
    forklaring_ft: list[str]


def finn_spiller(tekst: str, data: fv.Data) -> int:
    """«426», «Groß» eller «Thomas@COV» → element-id. Tvetydige eller ukjente navn er feil."""
    tekst = tekst.strip()
    if tekst.isdigit():
        if int(tekst) not in data.elementer:
            raise ValueError(f"ukjent element-id {tekst}")
        return int(tekst)
    navn, _, lag = tekst.partition("@")
    treff = [e for e, x in data.elementer.items() if x["web_name"] == navn
             and (not lag or data.lag[x["team"]]["short_name"] == lag)]
    if len(treff) == 1:
        return treff[0]
    if not treff:
        raise ValueError(f"fant ingen spiller «{tekst}»")
    alt = ", ".join(f"{data.elementer[e]['web_name']}@{data.lag[data.elementer[e]['team']]['short_name']} ({e})"
                    for e in treff)
    raise ValueError(f"«{tekst}» er tvetydig: {alt}")


def les_ekstra(tekst: str, data: fv.Data) -> list[tuple[int, int]]:
    ut = []
    for del_ in [d for d in tekst.split(",") if d.strip()]:
        if ">" not in del_:
            raise ValueError(f"«{del_}» mangler «>» (format: Ut>Inn)")
        a, b = del_.split(">", 1)
        ut.append((finn_spiller(a, data), finn_spiller(b, data)))
    return ut


def bygg_tilstand(kilde: fv.Kilde, data: fv.Data, runde_a: int, ekstra: list[tuple[int, int]],
                  ekstra_runde: int | None, frikjop_overstyr: int | None,
                  bank_overstyr: int | None) -> Tilstand:
    ok: list[str] = []
    adv: list[str] = []
    feil: list[str] = []
    if data.tropp_runde is None:
        raise ValueError("fant ingen picks-fil i speilet")
    if runde_a <= data.tropp_runde:
        raise ValueError(f"horisonten starter i GW{runde_a}, men troppen er fra GW{data.tropp_runde}")
    r_ekstra = ekstra_runde if ekstra_runde is not None else data.tropp_runde + 1
    if ekstra and not data.tropp_runde < r_ekstra <= runde_a:
        raise ValueError(f"ekstra bytter i GW{r_ekstra} må ligge etter GW{data.tropp_runde} og senest i GW{runde_a}")
    picks = kilde.json(f"entry/picks/gw{data.tropp_runde}.json")
    historikk = kilde.json("entry/history.json")
    overganger = sorted(kilde.json("entry/transfers.json", paakrevd=False) or [], key=lambda t: t["time"])
    el = data.elementer
    startpris = {e: x["now_cost"] - (x.get("cost_change_start") or 0) for e, x in el.items()}

    regel_feil, regel_ok = kontroller_regler(data.regler)
    feil += regel_feil
    ok += regel_ok

    # Bankkjeden: overgangene skal gjenskape banken i historikken, runde for runde.
    hist_bank = {h["event"]: h["bank"] for h in historikk.get("current", [])}
    bank = 0
    avvik = []
    for e in sorted(hist_bank):
        bank += sum(t["element_out_cost"] - t["element_in_cost"] for t in overganger if t["event"] == e)
        if bank != hist_bank[e]:
            avvik.append(f"GW{e}: kjeden gir £{bank / 10:.1f}m, historikken £{hist_bank[e] / 10:.1f}m")
    if avvik:
        feil.append("banken regnet fra overgangene stemmer ikke med historikken: " + "; ".join(avvik))
    elif hist_bank:
        ok.append(f"Bank regnet fra {len(overganger)} overganger stemmer med historikken i alle {len(hist_bank)} runder")

    # Tropp og bank etter siste picks, deretter overganger speilet kjenner for senere runder.
    tropp = [p["element"] for p in picks["picks"]]
    bank = picks["entry_history"]["bank"]
    innkjop: dict[int, int] = {}
    for t in overganger:
        innkjop[t["element_in"]] = t["element_in_cost"]
    senere = [t for t in overganger if t["event"] > data.tropp_runde]
    for t in senere:
        if t["element_out"] not in tropp or t["element_in"] in tropp:
            feil.append(f"overgangen {t['element_out']} → {t['element_in']} i GW{t['event']} passer ikke troppen")
            continue
        tropp[tropp.index(t["element_out"])] = t["element_in"]
        bank += t["element_out_cost"] - t["element_in_cost"]
    kjente_bytter = collections.Counter(t["event"] for t in senere)
    if senere:
        ok.append(f"{len(senere)} overgang(er) etter GW{data.tropp_runde} lagt på troppen fra speilet")

    # Bytter gjort etter siste speiling, oppgitt for hånd.
    if ekstra:
        for ut, inn in ekstra:
            if ut not in tropp:
                raise ValueError(f"{el[ut]['web_name']} er ikke i troppen")
            if inn in tropp:
                raise ValueError(f"{el[inn]['web_name']} er allerede i troppen")
            if el[ut]["element_type"] != el[inn]["element_type"]:
                raise ValueError(f"{el[ut]['web_name']} og {el[inn]['web_name']} har ulik posisjon")
            bank += salgspris(innkjop.get(ut, startpris[ut]), el[ut]["now_cost"]) - el[inn]["now_cost"]
            tropp[tropp.index(ut)] = inn
            innkjop[inn] = el[inn]["now_cost"]
            kjente_bytter[r_ekstra] += 1
        adv.append(f"{len(ekstra)} bytte(r) i GW{r_ekstra} oppgitt for hånd, ikke i speilet ennå: "
                   + ", ".join(f"{el[u]['web_name']} → {el[i]['web_name']}" for u, i in ekstra)
                   + ". Salgs- og innkjøpspris regnet med dagens priser — kontroller banken mot appen.")
    for e in tropp:
        innkjop.setdefault(e, startpris[e])

    form = collections.Counter(fv.POS[el[e]["element_type"]] for e in tropp)
    if dict(form) != TROPP_FORM:
        feil.append(f"troppen har formen {dict(form)}, ikke {TROPP_FORM}")
    if max(collections.Counter(el[e]["team"] for e in tropp).values()) > MAKS_PER_KLUBB:
        feil.append("troppen har mer enn tre spillere fra én klubb")
    if bank < 0:
        feil.append(f"banken blir £{bank / 10:.1f}m — byttene er ikke lovlige med dagens priser")

    ft, forklaring, ft_feil = frikjop(historikk, dict(kjente_bytter), runde_a)
    allerede = kjente_bytter.get(runde_a, 0)
    if frikjop_overstyr is not None:
        adv.append(f"frikjøp overstyrt til {frikjop_overstyr} (beregnet: {ft if ft is not None else 'ukjent'})")
        ft = frikjop_overstyr
    else:
        feil.extend(ft_feil)
        if ft is not None:
            ft = max(0, ft - allerede)
            ok.append(f"Frikjøp til GW{runde_a}: {ft}"
                      + (f", etter {allerede} bytte(r) allerede gjort i GW{runde_a}" if allerede else "")
                      + ". Kostnaden i hver runde stemmer med historikken")
    if ft is None:
        feil.append("frikjøp kunne ikke beregnes")
        ft = 0
    if bank_overstyr is not None:
        adv.append(f"bank overstyrt til £{bank_overstyr / 10:.1f}m (beregnet: £{bank / 10:.1f}m)")
        bank = bank_overstyr
    return Tilstand(tropp, innkjop, bank, ft, runde_a, ok, adv, feil, forklaring)


# --------------------------------------------------------------------------- lagpoeng

MIN_FORM = {"DEF": 3, "MID": 2, "FWD": 1}       # 05: minst 3 forsvarere og 1 spiss; 2 midtbane følger av troppen
MAKS_FORM = {"DEF": 5, "MID": 5, "FWD": 3}
ORDEN = ("DEF", "MID", "FWD")


def antall_fordeling(sannsynligheter: list[float]) -> list[float]:
    """Fordelingen av antall inntrufne hendelser, hver med sin sannsynlighet (Poisson-binomisk)."""
    f = [1.0]
    for q in sannsynligheter:
        ny = [0.0] * (len(f) + 1)
        for k, v in enumerate(f):
            ny[k] += v * (1 - q)
            ny[k + 1] += v * q
        f = ny
    return f


@functools.lru_cache(maxsize=None)
def innbyttere(spill: tuple[tuple[str, tuple[float, ...]], ...], benk: tuple[tuple[str, float], ...],
               terskel: float = 1e-7) -> tuple[float, ...]:
    """P(benkespiller j spiller og kommer inn) for utespillerbenken, i prioritert rekkefølge.

    spill = ((posisjon, P(spiller) for hver startende utespiller i posisjonen), …);
    benk = ((posisjon, P(spiller)), …).
    Antall fravær per posisjon er uavhengige Poisson-binomiske fordelinger. For hver kombinasjon
    av fravær og hvilke benkespillere som spilte, følges regelen i 05: hver utespiller som ikke
    spilte byttes mot den høyest prioriterte innbytteren som spilte og ikke bryter formasjonen.
    Kombinasjoner med sannsynlighet under terskel hoppes over."""
    spill_d = dict(spill)
    fordeling = {pos: antall_fordeling([1 - x for x in spill_d.get(pos, ())]) for pos in ORDEN}
    start = {pos: len(spill_d.get(pos, ())) for pos in ORDEN}
    ut = [0.0] * len(benk)
    utfall = []
    for maske in range(1 << len(benk)):
        pm = 1.0
        for j, (_, pb) in enumerate(benk):
            pm *= pb if maske >> j & 1 else 1 - pb
        if pm > terskel:
            utfall.append((maske, pm))
    for d, pd in enumerate(fordeling["DEF"]):
        if pd < terskel:
            continue
        for mi, pmi in enumerate(fordeling["MID"]):
            if pd * pmi < terskel:
                continue
            for f, pf in enumerate(fordeling["FWD"]):
                pa = pd * pmi * pf
                if pa < terskel or d + mi + f == 0:
                    continue
                fravaer = ["DEF"] * d + ["MID"] * mi + ["FWD"] * f
                for maske, pm in utfall:
                    antall = dict(start)
                    ledig = [j for j in range(len(benk)) if maske >> j & 1]
                    for pos in fravaer:
                        for j in ledig:
                            bpos = benk[j][0]
                            if bpos != pos and (antall[pos] - 1 < MIN_FORM[pos] or antall[bpos] + 1 > MAKS_FORM[bpos]):
                                continue
                            antall[pos] -= 1
                            antall[bpos] += 1
                            ut[j] += pa * pm
                            ledig.remove(j)
                            break
    return tuple(ut)


class Evaluator:
    """Lagets forventede poeng per runde for en tropp, med hurtigbuffer."""

    def __init__(self, spillere: dict[int, Spiller]):
        self.s = spillere
        self.buffer: dict[tuple, float] = {}

    def runde(self, tropp: tuple[int, ...], g: int, robust: bool = False) -> float:
        nokkel = (frozenset(tropp), g, robust)
        v = self.buffer.get(nokkel)
        if v is None:
            v = self.buffer[nokkel] = self.detaljer(tropp, g, robust)["sum"]
        return v

    def detaljer(self, tropp: tuple[int, ...], g: int, robust: bool = False) -> dict:
        S = self.s
        verdi = {e: (S[e].xr[g] if robust else S[e].xp[g]) for e in tropp}
        p = {e: S[e].p[g] for e in tropp}
        etter = collections.defaultdict(list)
        for e in tropp:
            etter[S[e].pos].append(e)
        for pos in etter:
            etter[pos].sort(key=lambda e: -verdi[e])
        gk, gk_benk = etter["GKP"][0], etter["GKP"][1]
        resten = sorted(etter["DEF"][3:] + etter["MID"] + etter["FWD"][1:], key=lambda e: -verdi[e])
        ellever = etter["DEF"][:3] + etter["FWD"][:1] + resten[:6]
        benk = resten[6:]
        alle = [gk] + ellever
        sum_xi = sum(verdi[e] for e in alle)

        rang = sorted(alle, key=lambda e: -verdi[e])
        kap, vise, kaptein = rang[0], rang[1], -math.inf
        for c in rang[:3]:
            v = next(x for x in rang if x != c)
            t = verdi[c] + (1 - p[c]) * verdi[v]
            if t > kaptein:
                kap, vise, kaptein = c, v, t

        innbytte = (1 - p[gk]) * verdi[gk_benk]
        brukt = innbyttere(
            tuple((pos, tuple(sorted(round(p[e], 6) for e in ellever if S[e].pos == pos))) for pos in ORDEN),
            tuple((S[b].pos, round(p[b], 6)) for b in benk))
        for b, pb in zip(benk, brukt):
            if p[b] > 1e-12:
                innbytte += verdi[b] / p[b] * pb
        return {"sum": sum_xi + kaptein + innbytte, "ellever": alle, "benk": [gk_benk] + benk,
                "kaptein": kap, "vise": vise, "xi": sum_xi, "kapteinsledd": kaptein, "innbytte": innbytte}


# --------------------------------------------------------------------------- planer


@dataclasses.dataclass(frozen=True)
class Bytte:
    ut: int
    inn: int


def kolliderer(x: tuple[Bytte, ...], y: tuple[Bytte, ...]) -> bool:
    brukt = {b.ut for b in x} | {b.inn for b in x}
    return any(b.ut in brukt or b.inn in brukt for b in y)


@dataclasses.dataclass
class Plan:
    a: tuple[Bytte, ...]
    b: tuple[Bytte, ...]
    verdi: float
    hits: int
    bank_a: int
    bank_b: int
    tropp_a: tuple[int, ...]
    tropp_b: tuple[int, ...]
    robust: float | None = None
    per_runde: list[float] = dataclasses.field(default_factory=list)


class Planlegger:
    def __init__(self, tilstand: Tilstand, spillere: dict[int, Spiller], kandidater: dict[str, list[int]],
                 n_runder: int, maks_hits: int):
        self.t = tilstand
        self.s = spillere
        self.kand = kandidater
        self.n = n_runder
        self.maks_hits = maks_hits
        self.ev = Evaluator(spillere)
        self.tropp0 = tuple(tilstand.tropp)
        self.antall_vurdert = 0

    def selg(self, e: int, innkjop: dict[int, int]) -> int:
        return salgspris(innkjop.get(e, self.s[e].pris), self.s[e].pris)

    def bruk(self, tropp: tuple[int, ...], bank: int, bytter: tuple[Bytte, ...], innkjop: dict[int, int],
             fritt: bool = False) -> tuple[tuple[int, ...], int, dict[int, int]] | None:
        """Utfører byttene. None hvis ulovlige. fritt=True ser bort fra bank og klubbgrense."""
        t = list(tropp)
        nye = dict(innkjop)
        for b in bytter:
            if b.ut not in t or b.inn in t or self.s[b.ut].pos != self.s[b.inn].pos:
                return None
            bank += self.selg(b.ut, nye) - self.s[b.inn].pris
            t[t.index(b.ut)] = b.inn
            nye[b.inn] = self.s[b.inn].pris
        if not fritt:
            if bank < 0:
                return None
            if max(collections.Counter(self.s[e].lag for e in t).values()) > MAKS_PER_KLUBB:
                return None
        return tuple(t), bank, nye

    def frikjop_b(self, n_a: int) -> int:
        return max(1, min(MAKS_FRIKJOP, max(0, self.t.frikjop - n_a) + 1))

    def vurder(self, a: tuple[Bytte, ...], b: tuple[Bytte, ...], fritt: bool = False) -> Plan | None:
        self.antall_vurdert += 1
        hits_a = max(0, len(a) - self.t.frikjop)
        hits_b = max(0, len(b) - self.frikjop_b(len(a)))
        if hits_a > self.maks_hits or hits_b > self.maks_hits:
            return None
        if b and self.n < 2:
            return None
        r = self.bruk(self.tropp0, self.t.bank, a, self.t.innkjop, fritt)
        if r is None:
            return None
        tropp_a, bank_a, innkjop_a = r
        r = self.bruk(tropp_a, bank_a, b, innkjop_a, fritt)
        if r is None:
            return None
        tropp_b, bank_b, _ = r
        verdi = self.ev.runde(tropp_a, 0) + sum(self.ev.runde(tropp_b, g) for g in range(1, self.n))
        return Plan(a, b, verdi - HIT * (hits_a + hits_b), hits_a + hits_b, bank_a, bank_b, tropp_a, tropp_b)

    def enkeltbytter(self) -> list[Bytte]:
        return [Bytte(e, k) for e in self.tropp0 for k in self.kand[self.s[e].pos] if k not in self.tropp0]

    def utvalg(self, rang: list[Bytte]) -> list[Bytte]:
        """De beste etter en rangering uten bank og klubbgrense, pluss de beste per solgt spiller
        og de beste per solgt spiller blant bytter som frigjør penger."""
        valgt = list(rang[:TOPP_B])
        sett = set(valgt)
        per: collections.Counter = collections.Counter()
        frigjor: collections.Counter = collections.Counter()
        for s in rang:
            ta = False
            if per[s.ut] < TOPP_PER_SPILLER:
                per[s.ut] += 1
                ta = True
            if (self.selg(s.ut, self.t.innkjop) - self.s[s.inn].pris >= FRIGJOR_MIN
                    and frigjor[s.ut] < TOPP_FRIGJOR):
                frigjor[s.ut] += 1
                ta = True
            if ta and s not in sett:
                valgt.append(s)
                sett.add(s)
        return valgt

    def sok(self) -> tuple[Plan, list[Plan], dict]:
        spar = self.vurder((), ())
        assert spar is not None
        planer: dict[tuple, Plan] = {}

        def legg(a: tuple[Bytte, ...], b: tuple[Bytte, ...]) -> Plan | None:
            nokkel = (frozenset(a), frozenset(b))
            if nokkel in planer:
                return planer[nokkel]
            p = self.vurder(a, b)
            if p:
                planer[nokkel] = p
            return p

        def fri(a: tuple[Bytte, ...], b: tuple[Bytte, ...]) -> float:
            p = self.vurder(a, b, fritt=True)
            return p.verdi if p else -math.inf

        to_runder = self.n > 1
        to_i_a = self.t.frikjop >= 2 or self.maks_hits >= 1
        to_i_b_spart = self.frikjop_b(0) >= 2 or self.maks_hits >= 1
        to_i_b_etter_en = self.frikjop_b(1) >= 2 or self.maks_hits >= 1

        enkle = self.enkeltbytter()
        for s in enkle:
            legg((s,), ())
            if to_runder:
                legg((), (s,))
        fri_a = {s: fri((s,), ()) for s in enkle}
        topp_a = self.utvalg(sorted(enkle, key=lambda s: -fri_a[s]))
        topp_b: list[Bytte] = []
        if to_runder:
            fri_b = {s: fri((), (s,)) for s in enkle}
            topp_b = self.utvalg(sorted(enkle, key=lambda s: -fri_b[s]))
            for s1 in enkle:
                for s2 in topp_b:
                    if not kolliderer((s1,), (s2,)):
                        legg((s1,), (s2,))

        par_b: list[tuple[float, tuple[Bytte, ...]]] = []
        if to_runder and to_i_b_spart:
            for s1, s2 in itertools.combinations(topp_b, 2):
                if kolliderer((s1,), (s2,)):
                    continue
                legg((), (s1, s2))
                par_b.append((fri((), (s1, s2)), (s1, s2)))

        par_a: list[Plan] = []
        if to_i_a:
            for s1, s2 in itertools.combinations(topp_a, 2):
                if kolliderer((s1,), (s2,)):
                    continue
                p = legg((s1, s2), ())
                if p:
                    par_a.append(p)
            if to_runder:
                for p in sorted(par_a, key=lambda p: -p.verdi)[:TOPP_PAR]:
                    for s in topp_b:
                        if not kolliderer(p.a, (s,)):
                            legg(p.a, (s,))

        if to_runder and to_i_b_etter_en:
            beste_a = sorted((planer[(frozenset((s,)), frozenset())] for s in enkle
                              if (frozenset((s,)), frozenset()) in planer), key=lambda p: -p.verdi)[:TOPP_PAR]
            beste_par_b = [b for _, b in sorted(par_b, key=lambda x: -x[0])[:TOPP_PAR_B]]
            for pa in beste_a:
                for b in beste_par_b:
                    if not kolliderer(pa.a, b):
                        legg(pa.a, b)

        # Planer som ender i samme tropp i begge runder (f.eks. A → X, B → Y og A → Y, B → X i samme
        # runde) er samme plan. Behold én.
        unike: dict[tuple, Plan] = {}
        for p in sorted(planer.values(), key=lambda p: (-p.verdi, beskriv(p, self.s, 0))):
            unike.setdefault((frozenset(p.tropp_a), frozenset(p.tropp_b)), p)
        omfang = {"enkeltbytter": len(enkle), "utvalg_a": len(topp_a), "utvalg_b": len(topp_b),
                  "lovlige": len(unike), "vurdert": self.antall_vurdert,
                  "kandidater": {pos: len(v) for pos, v in self.kand.items()}}
        return spar, list(unike.values()), omfang

    def fullfor(self, p: Plan) -> Plan:
        """Robust verdi og poeng per runde, bare for planer som vises."""
        if p.robust is None:
            tropper = [p.tropp_a] + [p.tropp_b] * (self.n - 1)
            p.robust = sum(self.ev.runde(t, g, robust=True) for g, t in enumerate(tropper)) - HIT * p.hits
            p.per_runde = [self.ev.runde(t, g) for g, t in enumerate(tropper)]
        return p


def kandidater(spillere: dict[int, Spiller], tropp: list[int]) -> dict[str, list[int]]:
    ut: dict[str, list[int]] = {}
    for pos in fv.POSISJONER:
        alle = sorted((s for s in spillere.values() if s.pos == pos and s.eid not in tropp and sum(s.xp) > 0),
                      key=lambda s: (-sum(s.xp), s.eid))
        valgt = [s.eid for s in alle[:K_XP]]
        if alle:
            terskel = 0.5 * sum(alle[0].xp)
            for s in sorted((s for s in alle if sum(s.xp) >= terskel), key=lambda s: (-sum(s.xp) / s.pris, s.eid))[:K_VERDI]:
                if s.eid not in valgt:
                    valgt.append(s.eid)
        ut[pos] = valgt
    return ut


# --------------------------------------------------------------------------- utskrift


def kr(tideler: int) -> str:
    return f"£{tideler / 10:.1f}m"


def beskriv(p: Plan, S: dict[int, Spiller], ra: int) -> str:
    deler = []
    if p.a:
        deler.append(f"GW{ra}: " + ", ".join(f"{S[b.ut].navn} → {S[b.inn].navn}" for b in p.a))
    if p.b:
        deler.append(f"GW{ra + 1}: " + ", ".join(f"{S[b.ut].navn} → {S[b.inn].navn}" for b in p.b))
    return " · ".join(deler) if deler else "spar"


def klubbtekst(tropp: tuple[int, ...], S: dict[int, Spiller], data: fv.Data) -> str:
    c = collections.Counter(data.lag[S[e].lag]["short_name"] for e in tropp)
    return " · ".join(f"{k} {v}" for k, v in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))


def gkdef(tropp: tuple[int, ...], S: dict[int, Spiller]) -> int:
    return sum(S[e].pris for e in tropp if S[e].pos in ("GKP", "DEF"))


def markdown(t: Tilstand, pl: Planlegger, spar: Plan, planer: list[Plan], omfang: dict, runder: list[int],
             data: fv.Data, vis_ut: list[int], topp: int, naa: dt.datetime, fv_kontroller: tuple,
             flagg: dict[int, str]) -> str:
    S = pl.s
    ra = runder[0]
    spenn = f"GW{runder[0]}–{runder[-1]}"
    L = ["# Byttepakker — generert", "",
         f"*Generert {naa:%d.%m.%Y kl. %H:%M} UTC av `scripts/bytter.py` fra `fpl-data`. **Rør ikke fila for hånd.** "
         f"Horisont {spenn}. Bytter vurderes i GW{ra}" + (f" og GW{ra + 1}" if len(runder) > 1 else "")
         + f". Maks minuspoeng per runde: {pl.maks_hits * HIT}.*", ""]
    fv_feil, fv_adv, fv_ok = fv_kontroller
    L += ["## Kontroller", ""]
    L += [f"- ❌ {x}" for x in fv_feil + t.feil]
    L += [f"- ✅ {x}" for x in fv_ok + t.ok]
    L += [f"- ⚠️ {x}" for x in fv_adv + t.advarsler]
    L += ["", "**Frikjøp, runde for runde:** " + " · ".join(t.forklaring_ft), ""]

    L += [f"## Troppen inn i GW{ra}", "", f"Bank **{kr(t.bank)}**, frikjøp **{t.frikjop}**. Salgspris etter regelen i `05`.", "",
          f"| Spiller | Lag | Pos | Nå | Kjøpt | Salgspris | Sum {spenn} | Robust | P(spiller) GW{ra} | Eid |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for e in sorted(t.tropp, key=lambda e: (fv.POSISJONER.index(S[e].pos), -sum(S[e].xp))):
        s = S[e]
        L.append(f"| {s.navn} | {data.lag[s.lag]['short_name']} | {s.pos} | {kr(s.pris)} | {kr(t.innkjop[e])} "
                 f"| {kr(salgspris(t.innkjop[e], s.pris))} | {sum(s.xp):.2f} | {sum(s.xr):.2f} | {s.p[0]:.2f} "
                 f"| {s.eierandel:.1f} % |")
    L.append("")

    d0 = pl.ev.detaljer(pl.tropp0, 0)
    L += ["## Spar — ingen bytter", "",
          f"Lagets forventede poeng: **{spar.verdi:.2f}** over horisonten (robust {spar.robust:.2f}). Per runde: "
          + ", ".join(f"GW{r} {v:.2f}" for r, v in zip(runder, spar.per_runde)) + ".", "",
          f"GW{ra}: elleveren {d0['xi']:.2f} + kapteinsledd {d0['kapteinsledd']:.2f} ({S[d0['kaptein']].navn}, "
          f"vise {S[d0['vise']].navn}) + innbytterledd {d0['innbytte']:.2f}. Benk: "
          + ", ".join(S[e].navn for e in d0["benk"]) + ".", ""]

    hode = (f"| Plan | Minus | Endring {spenn} | Robust endring | Endring GW{ra} | Bank etter GW{ra} "
            f"| Bank etter GW{ra + 1} | Klubber med 3 |")
    skille = "|---|---|---|---|---|---|---|---|"

    viste: list[Plan] = []

    def rad(p: Plan, prefiks: str = "") -> str:
        pl.fullfor(p)
        viste.append(p)
        tre = sorted(k for k, v in collections.Counter(data.lag[S[e].lag]["short_name"] for e in p.tropp_b).items() if v >= 3)
        return (f"| {prefiks}{beskriv(p, S, ra)} | {-HIT * p.hits if p.hits else 0} | **{p.verdi - spar.verdi:+.2f}** "
                f"| {p.robust - spar.robust:+.2f} | {p.per_runde[0] - spar.per_runde[0]:+.2f} | {kr(p.bank_a)} "
                f"| {kr(p.bank_b)} | {', '.join(tre) or '—'} |")

    vist = planer[:topp]
    L += [f"## Beste planer ({omfang['lovlige']} lovlige av {omfang['vurdert']} vurderte)", "",
          "Endring = forventede poeng mot å spare, over hele horisonten, etter minuspoeng.", "", hode, skille]
    L += [rad(p) for p in vist]
    L.append("")

    L += ["## Beste plan som selger hver spiller", "",
          "Svarer på «bør X selges?»: den beste lovlige planen der spilleren går ut, mot å spare.", "", hode, skille]
    beste_ut: dict[int, Plan] = {}
    for p in planer:
        for b in p.a + p.b:
            beste_ut.setdefault(b.ut, p)
    for e in sorted(t.tropp, key=lambda e: (fv.POSISJONER.index(S[e].pos), -sum(S[e].xp))):
        if e in beste_ut:
            L.append(rad(beste_ut[e], f"**{S[e].navn} ut:** "))
        else:
            L.append(f"| **{S[e].navn} ut:** ingen lovlig plan | | | | | | | |")
    L.append("")

    def antidrift(p: Plan) -> list[str]:
        pl.fullfor(p)
        return [f"- Klubber etter: {klubbtekst(p.tropp_b, S, data)}",
                f"- Keeper- og forsvarsbudsjett (nåpris): {kr(gkdef(pl.tropp0, S))} → {kr(gkdef(p.tropp_b, S))}. "
                "Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.",
                f"- Bank: {kr(t.bank)} → {kr(p.bank_a)} etter GW{ra}"
                + (f" → {kr(p.bank_b)} etter GW{ra + 1}" if len(runder) > 1 else ""),
                "- Endring per runde: " + ", ".join(f"GW{r} {v1 - v0:+.2f}"
                                                   for r, v0, v1 in zip(runder, spar.per_runde, p.per_runde))]

    for e in vis_ut:
        if e not in S:
            continue
        L += [f"## {S[e].navn} ut", ""]
        if e not in beste_ut:
            L += ["Ingen lovlig plan selger spilleren.", ""]
            continue
        p = beste_ut[e]
        L += [f"**{beskriv(p, S, ra)}** — {p.verdi - spar.verdi:+.2f} mot å spare "
              f"(robust {p.robust - spar.robust:+.2f}).", ""] + antidrift(p) + [""]
        alt = [q for q in planer if any(b.ut == e for b in q.a + q.b)][:5]
        L += ["De fem beste planene som selger ham:", "", hode, skille] + [rad(q) for q in alt] + [""]
        uten = next((q for q in planer if all(b.ut != e for b in q.a + q.b)), None)
        if uten:
            L += [f"Beste plan som beholder ham: **{beskriv(uten, S, ra)}**, {uten.verdi - spar.verdi:+.2f} mot å spare.", ""]

    L += ["## Anti-drift for de tre beste planene", ""]
    for p in vist[:3]:
        L += [f"**{beskriv(p, S, ra)}**", ""] + antidrift(p) + [""]

    inn = list(dict.fromkeys(b.inn for p in viste for b in p.a + p.b))
    L += ["## Spillere inn i planene over", "",
          "Flaggene kommer fra `forventning.py`. Én kamp som bærer xGI-en, slår ut i robust endring.", "",
          f"| Spiller | Lag | Pos | Pris | Eid | Sum {spenn} | Robust | P(spiller) GW{ra} | Flagg |",
          "|---|---|---|---|---|---|---|---|---|"]
    for e in sorted(inn, key=lambda e: (fv.POSISJONER.index(S[e].pos), -sum(S[e].xp))):
        s = S[e]
        L.append(f"| {s.navn} | {data.lag[s.lag]['short_name']} | {s.pos} | {kr(s.pris)} | {s.eierandel:.1f} % "
                 f"| {sum(s.xp):.2f} | {sum(s.xr):.2f} | {s.p[0]:.2f} | {flagg.get(e, '') or '—'} |")
    L.append("")

    L += ["## Søkets omfang og forutsetninger", "",
          "- Kandidater per posisjon: " + ", ".join(f"{k} {v}" for k, v in omfang["kandidater"].items())
          + f" ({K_XP} beste på forventning, {K_VERDI} beste per million).",
          f"- {omfang['enkeltbytter']} enkeltbytter vurdert i hver runde. Utvalg for kombinasjoner: "
          f"{omfang['utvalg_a']} i GW{ra}, {omfang['utvalg_b']} i GW{ra + 1}. Søket er ikke uttømmende for kombinasjoner.",
          "- Priser er dagens. Prisendringer før byttet er ikke modellert.",
          "- De operative reglene i `01` (template i premiumslottene, differensialer bare mellom £4,0m og £5,5m "
          "og maks tre samtidig, ett bytte per runde) er ikke modellert. Eierandelen står i tabellene; sjekk "
          "reglene for spillerne som kommer inn.",
          "- Bytter i tredje runde og senere er ikke med. En plan som sparer, har verdi utover horisonten "
          "som tabellen ikke viser.",
          "- I tilbaketesten avviker realiserte poeng over fem runder i snitt 5–6 poeng per spiller fra "
          "forventningen. En planforskjell på noen få poeng er en svak preferanse, ikke en dom.", ""]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- main


def lag_spillere(m: fv.Modell, data: fv.Data, runder: list[int], fravaer: dict, tropp: list[int]) -> dict[int, Spiller]:
    spillere: dict[int, Spiller] = {}
    navn = collections.Counter(x["web_name"] for x in data.elementer.values())
    for e, x in data.elementer.items():
        if x["status"] == "u" and e not in tropp:
            continue
        pr = fv.projiser(m, e, runder, fravaer.get(e, {}))
        vist = x["web_name"] + (f" ({data.lag[x['team']]['short_name']})" if navn[x["web_name"]] > 1 else "")
        spillere[e] = Spiller(e, vist, fv.POS[x["element_type"]], x["team"], x["now_cost"],
                              [pr["runder"][r] for r in runder], [pr["robust"][r] for r in runder],
                              [pr["spiller"][r] for r in runder], float(x.get("selected_by_percent") or 0))
    return spillere


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--stdout", action="store_true", help="markdown til stdout, skriv ingenting")
    ap.add_argument("--runder", type=int, default=5, help="antall runder i horisonten (standard 5)")
    ap.add_argument("--fra-runde", type=int, help="første runde i horisonten (standard: neste deadline)")
    ap.add_argument("--maks-hits", type=int, default=0, help="bytter utover frikjøpene tillatt per runde")
    ap.add_argument("--vis-ut", default="", help="spillere (navn, navn@LAG eller id): beste planer som selger dem")
    ap.add_argument("--ekstra-bytter", default="", help="«Ut>Inn,Ut>Inn»: bytter gjort etter siste speiling")
    ap.add_argument("--ekstra-runde", type=int, help="runden de ekstra byttene ble gjort i (standard: runden etter siste picks)")
    ap.add_argument("--frikjop", type=int, help="overstyr beregnede frikjøp")
    ap.add_argument("--bank", type=float, help="overstyr beregnet bank, i £m (f.eks. 0.3)")
    ap.add_argument("--topp", type=int, default=15, help="antall planer i hovedtabellen")
    ap.add_argument("--kilde", type=pathlib.Path, help="mappe med speilets data/-struktur")
    ap.add_argument("--fravaer", type=pathlib.Path, default=fv.FRAVAER_FIL)
    ap.add_argument("--prior", type=pathlib.Path, default=fv.PRIOR_FIL)
    ap.add_argument("--ut-md", type=pathlib.Path, default=UT_MD)
    a = ap.parse_args(argv)

    naa = dt.datetime.now(dt.timezone.utc)
    kilde = fv.Kilde(a.kilde)
    data = fv.last_data(kilde)
    if not data.grunnlag:
        print("FEIL: ingen ferdige, låste runder i speilet", file=sys.stderr)
        return 1
    fr_tekst, _ = fv.hent_repofil(a.fravaer)
    fravaer, fr_feil = fv.les_fravaer(fr_tekst, data.elementer)
    pr_tekst, _ = fv.hent_repofil(a.prior)
    prior, _, pr_feil = fv.les_prior(pr_tekst, data.lag)
    fv_feil, fv_adv, fv_ok = fv.kontroller(data, fr_feil + (pr_feil if pr_tekst else []), naa)
    if fr_tekst is None:
        fv_adv.append(f"fant ikke fraværsfila ({a.fravaer}) — alle fravær står som uavklart")
    if pr_tekst is None:
        fv_adv.append(f"fant ikke lagstyrke-prior ({a.prior}) — lagstyrke krympes mot 1,0")
    try:
        runder = fv.horisont(data, a.fra_runde, a.runder, naa)
        ekstra = les_ekstra(a.ekstra_bytter, data)
        vis_ut = [finn_spiller(x, data) for x in a.vis_ut.split(",") if x.strip()]
        tilstand = bygg_tilstand(kilde, data, runder[0], ekstra, a.ekstra_runde, a.frikjop,
                                 None if a.bank is None else round(a.bank * 10))
    except (ValueError, FileNotFoundError) as e:
        print(f"FEIL: {e}", file=sys.stderr)
        return 1
    if fv_feil or tilstand.feil:
        for x in fv_feil + tilstand.feil:
            print(f"FEIL: {x}", file=sys.stderr)
        return 1

    start = time.time()
    m = fv.bygg_modell(data, fravaer, prior=prior)
    spillere = lag_spillere(m, data, runder, fravaer, tilstand.tropp)
    pl = Planlegger(tilstand, spillere, kandidater(spillere, tilstand.tropp), len(runder), a.maks_hits)
    spar, planer, omfang = pl.sok()
    pl.fullfor(spar)
    flagg = {}
    for e in spillere:
        merk = fv.projiser(m, e, runder, fravaer.get(e, {}))["merknader"]
        flagg[e] = " · ".join(m.profiler[e].flagg + merk)
    md = markdown(tilstand, pl, spar, planer, omfang, runder, data, vis_ut, a.topp, naa, (fv_feil, fv_adv, fv_ok), flagg)
    print(f"{omfang['vurdert']} planer vurdert, {omfang['lovlige']} lovlige, {time.time() - start:.1f} s", file=sys.stderr)
    if a.stdout:
        print(md)
        return 0
    gammel = a.ut_md.read_text(encoding="utf-8") if a.ut_md.exists() else ""
    if fv.uten_tidsstempel(gammel) == fv.uten_tidsstempel(md):
        print(f"{a.ut_md} uendret")
        return 0
    a.ut_md.parent.mkdir(parents=True, exist_ok=True)
    a.ut_md.write_text(md, encoding="utf-8")
    print(f"{a.ut_md} oppdatert")
    return 0


if __name__ == "__main__":
    sys.exit(main())
