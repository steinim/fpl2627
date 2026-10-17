#!/usr/bin/env python3
"""Forventede FPL-poeng per spiller og kamp, bygget ledd for ledd fra poengreglene.

Erstatter håndmodellen «forventet per runde» fra GW7-økten 17.10.2026. Den hadde seks
kjente feil (se feilloggen i context/03). Alt her er AVLEDET fra rå API-JSON i speilet
github.com/steinim/fpl-data. Ingen tall vedlikeholdes for hånd, med ett unntak:
context/fravaer.csv, der årsaken til hvert fravær føres (minimumskrav 11 i 03).

Kun stdlib — ingen pip install i CI.

Bruk (fra reporoten):
    python3 scripts/forventning.py                      # skriv analyse/forventning.md og .csv
    python3 scripts/forventning.py --stdout             # markdown til stdout, skriv ingenting
    python3 scripts/forventning.py --check              # bare kontrollene, exit 1 ved feil
    python3 scripts/forventning.py --runder 6           # horisont i runder (standard 5)
    python3 scripts/forventning.py --fra-runde 8        # første runde i horisonten
    python3 scripts/forventning.py --spillere 426,165   # ta med disse i markdown i tillegg
    python3 scripts/forventning.py --uten-fikstur       # alle motstandere og baner = snitt
    python3 scripts/forventning.py --tilbaketest        # modellen mot faktiske poeng, GW4 og utover
    python3 scripts/forventning.py --kilde DIR          # les speilets data/-struktur fra en mappe

MODELLEN
========
Én kamp for spiller i (lag T, posisjon p) mot motstander O på bane v (H/B), med
tilgjengelighet a. Grunnlaget er alle ferdige runder med data_checked = true.

Minutter (rate og tilgjengelighet skilles — minimumskrav 11):
  Hver runde i grunnlaget er start, innbytter eller fravær. Et fravær uten årsak i
  context/fravaer.csv telles som ikke-start og flagges UAVKLART. Fravær med årsak
  skade, karantene, landslag, personlig eller ikke_registrert telles ikke med.
  Kamp i er vektet AVTAK^(runder siden kampen), så en endret rolle slår raskt igjennom.
    startandel s   = vektede starter / vektede telte kamper
    innbytterandel = vektede innbytterkamper / vektede ikke-starter
    P(start) = a·s     P(innbytter) = a·(1−s)·innbytterandel
    E[min]   = P(start)·min per start + P(innbytter)·min per innbytterkamp
    P(≥60)   = P(start)·andel starter med ≥60 min + P(innbytter)·tilsvarende

Lagstyrke (xG-basert, multiplikativ, tilpasset motstanderne lagene har møtt):
    forventet xG for lag T mot O på bane v = μ · A_T · D_O · bane_v
  A og D tilpasses iterativt og krympes mot forrige sesongs styrke (context/lagstyrke-prior.csv,
  dempet med LAG_RHO) med vekt LAG_KA/LAG_KD kamper. Opprykkslag får snittet for forrige
  sesongs opprykkslag. Alle tre konstantene er valgt ved kryssvalidering, se konstantene.

Spillerrater per 90 er motstandsjusterte: xG/90 = Σ xG / Σ (min/90 · D_motstander · bane),
og krympes mot det som er typisk for posisjonen og startprisen med vekt SPILLER_K kamper.
(Forrige sesongs rate per spiller ble testet som prior og ga ingen gevinst — se SPILLER_K.)
Robust variant: samme, uten spillerens kamp med høyest xG + xA (minimumskrav 2).

Poeng per ledd — verdiene leses fra API-ets game_config og kontrolleres mot context/05:
    oppmøte    2·P(≥60) + 1·(P(spiller) − P(≥60))
    mål        xG/90 · målfaktor[p] · D_O · bane · E[min]/90 · målpoeng[p]
    assist     xA/90 · assistfaktor[p] · D_O · bane · E[min]/90 · 3
    clean sh.  P(≥60) · exp(−CS-faktor · λ · min ved ≥60/90) · CS-poeng[p],
               λ = μ · D_T · A_O · bane (lagets forventede baklengs per 90)
               (mål-, assist- og CS-faktor: kalibrert mot to hele sesonger, se konstantene)
    baklengs   −1 · E[⌊G/2⌋], G ~ Poisson(λ · min/90), keeper og forsvarer
    redninger  E[⌊S/3⌋], S ~ Poisson(redninger/90 · A_O · bane · min/90), keeper
    strafferedning  ligasnitt per keeper-90 · E[min]/90 · 5
    DC         2 · (P(start)·treffrate i starter + P(innbytter)·treffrate som innbytter);
               treffrate = andel kamper med DC ≥ terskel, talt runde for runde (krav 12),
               krympet mot posisjonssnittet med vekt DC_K kamper
    bonus      lineær modell per posisjon tilpasset alle kamper ≥60 min denne sesongen
               (bonus ~ mål, assist, CS, redninger, DC-treff), satt inn med forventede
               verdier, pluss spillerens eget avvik krympet med empirisk Bayes
    kort       −1·gule/90 (krympet mot posisjonssnitt) − 3·røde/90 − 2·selvmål/90 (ligasnitt)

VALIDERING (python3 scripts/historikk.py tilbaketest), forventet mot faktisk poeng for alle
spillere med minst én start, målrunde GW4–38. r = korrelasjon, MAE = snittlig absolutt feil.
I parentes: poeng per kamp hittil, og den gamle håndmodellen fra GW7-økten.
  2025/26, én runde fram    r 0,433 (0,345 / 0,353)   MAE 1,77 (1,93 / 1,88)
  2025/26, fem runder fram  r 0,550 (0,486 / 0,502)   MAE 5,90 (6,46 / 6,18)
  2024/25, én runde fram    r 0,468 (0,392 / 0,401)   MAE 1,61 (1,74 / 1,64)
  2024/25, fem runder fram  r 0,621 (0,562 / 0,579)   MAE 5,21 (5,71 / 5,38)
2025/26 er delvis i utvalget: lagstyrke, SPILLER_K og kalibreringen er valgt der. 2024/25 er
utenfor utvalget (kjør med --sesong 2024-25 --faktorer-fra 2025-26), med ett unntak: AVTAK ble
valgt ved å se på begge sesongene. Fiksturjusteringen løfter r med 0,010–0,012 på én runde.
Den robuste varianten (uten beste kamp) treffer like godt som hovedtallet (r 0,434 mot 0,433 og
0,468 mot 0,468). Den er en følsomhetssjekk, ikke et bedre estimat.
Modellen er best på alle mål i begge sesonger, men FPL-poeng er støyete: den forklarer om lag
20 % av variansen i én runde og 30–40 % over fem. Forskjeller under 2–3 poeng over fem runder
er innenfor usikkerheten.

Kjente begrensninger: se BEGRENSNINGER under. Lista skrives ut i hver rapport.
"""

from __future__ import annotations

import argparse
import collections
import csv
import dataclasses
import datetime as dt
import io
import json
import math
import pathlib
import re
import sys
import urllib.error
import urllib.request

MIRROR = "https://raw.githubusercontent.com/steinim/fpl-data/main/data"
REPO_RAW = "https://raw.githubusercontent.com/steinim/fpl2627/main"
FRAVAER_FIL = pathlib.Path("context/fravaer.csv")
PRIOR_FIL = pathlib.Path("context/lagstyrke-prior.csv")
UT_MD = pathlib.Path("analyse/forventning.md")
UT_CSV = pathlib.Path("analyse/forventning.csv")

# Lagstyrke: krympes mot forrige sesongs styrke, dempet med RHO, med vekt k (i kamper).
# Valgt ved kryssvalidering på 2025/26 (prior fra 2024/25), sjekkpunkt GW1–33, spådd lag-xG
# fem runder fram: MSE 0,528 mot 0,542 uten prior og 0,632 uten krymping. Kontrollert på en
# uavhengig sesong (2024/25, prior fra 2023/24): 0,592 mot 0,626 og 0,690.
# Reproduser med `python3 scripts/historikk.py kryssvalider`.
LAG_KA = 15.0
LAG_KD = 30.0
LAG_RHO = 0.5

# Kalibrering mot FPL-poeng, 2024/25 og 2025/26 samlet (`python3 scripts/historikk.py kalibrer`).
# FPL gir assist for returer, vunne straffer og avbøyde pasninger som Opta-xA ikke teller:
# spisser får 2,1 FPL-assist per xA, midtbane 1,35, forsvarere 1,20. Forsvarere scorer 20 %
# sjeldnere enn xG tilsier. Keeperens assistfaktor er snittet for alle posisjoner.
MAL_FAKTOR = {"GKP": 1.0, "DEF": 0.799, "MID": 0.987, "FWD": 1.001}
ASSIST_FAKTOR = {"GKP": 1.376, "DEF": 1.202, "MID": 1.349, "FWD": 2.090}
# Poisson på spådd λ gir 5–7 % for mange clean sheets (0,268 mot 0,250 per lagkamp i 2025/26,
# 0,244 mot 0,232 i 2024/25). Faktoren 1,046 er vektet snitt av 1,056 og 1,036. Mekanismen:
# sjansene i en kamp gir P(0 mål) = Π(1 − p) < e^(−Σp). Faktoren på λ gjelder bare clean
# sheet-sannsynligheten; forventet antall baklengs er kalibrert uten (0,453 spådd mot 0,455
# faktisk per lagkamp, 2025/26).
CS_FAKTOR = 1.046

# Spillerens xG/90 og xA/90 krympes mot det som er typisk for hans posisjon og startpris
# (minstekvadrat på alle spillere med minst 180 minutter i grunnlaget), med vekt k i kamper à 90 min.
# Startprisen er FPLs vurdering før sesongen og inneholder ingen informasjon fra sesongen selv.
# Valgt ved tilbaketest på 2025/26 (med AVTAK 0,7): GW4–10, én runde fram, r 0,382 → 0,393 → 0,394
# for k = 0, 3, 6; fem runder fram 0,515 → 0,521 → 0,518. Hele sesongen: 0,430 → 0,433.
# Effekten er størst tidlig i sesongen.
SPILLER_K = 3.0
# Testet og forkastet 17.10.2026: forrige sesongs xG/90 og xA/90 for samme spiller som prior
# (koblet på FPLs stabile «code»), krympet mot prisprioren. Ingen gevinst i noen kombinasjon av
# vekter: r endret seg under 0,005 i både 2024/25 og 2025/26. Startprisen fanger historikken.

# Vekt på eldre kamper i start- og innbytterandelen: AVTAK^(antall runder siden kampen).
# Tilbaketest (r mellom forventet og faktisk poeng, fem runder fram): 2025/26 0,523 uten avtak,
# 0,550 med 0,7; 2024/25 0,597 og 0,621. 0,7 ligger nær optimum i begge sesonger og på både
# én og fem runder, så verdien er ikke tilpasset én sesong. Reproduser med historikk.py.
AVTAK = 0.7

# DC-treffraten (andel kamper over terskelen) krympes mot posisjonssnittet med vekt DC_K kamper.
# Tilbaketest 2025/26, forsvarere, DC-poeng fem runder fram: r 0,496 (rå) → 0,512 (k = 4), og
# forventede poeng totalt 0,539 → 0,542. Optimum k = 4; 2 og 8 er nesten like gode. Bare 2025/26
# har DC-poeng, så verdien er valgt i utvalget.
DC_K = 4.0

POS = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
POSISJONER = ("GKP", "DEF", "MID", "FWD")

# Poengregler. Kontrolleres mot API-ets game_config.scoring ved hver kjøring (kjøringen
# stopper ved avvik) og mot tabellen i context/05 i testene.
POENG = {
    "long_play": 2,
    "short_play": 1,
    "assists": 3,
    "saves": 1,
    "penalties_saved": 5,
    "penalties_missed": -2,
    "yellow_cards": -1,
    "red_cards": -3,
    "own_goals": -2,
    "goals_scored": {"GKP": 10, "DEF": 6, "MID": 5, "FWD": 4},
    "clean_sheets": {"GKP": 4, "DEF": 4, "MID": 1, "FWD": 0},
    "goals_conceded": {"GKP": -1, "DEF": -1, "MID": 0, "FWD": 0},
    "defensive_contribution": {"GKP": 0, "DEF": 2, "MID": 2, "FWD": 2},
}
# Tersklene står ikke i API-et. Kilde: context/05, kontrollert i testene.
MIN_LANG = 60
REDNINGER_PER_POENG = 3
BAKLENGS_PER_POENG = 2
DC_TERSKEL = {"GKP": None, "DEF": 10, "MID": 12, "FWD": 12}

AARSAK_UTELATES = {"skade", "karantene", "landslag", "personlig", "ikke_registrert"}
AARSAK_TELLES = {"rotasjon", "benket"}
AARSAKER = AARSAK_UTELATES | AARSAK_TELLES

BEGRENSNINGER = [
    "Snittet ligger 1–4 % over fasit i tilbaketesten, fordi historisk skadestatus ikke finnes og alle "
    "settes som tilgjengelige. I bruk dekker FPL-status kjente skader, ikke uvarslet rotasjon.",
    "Straffer ligger i xG slik de har falt. Straffeskytterrolle vises i kolonnen «Str», men modelleres "
    "ikke separat. Bommet straffe (−2) er ikke med.",
    "Tilgjengelighet utover neste runde bygger på FPL-status og -nyhet. Returdatoen i nyheten tolkes som "
    "første dag spilleren er tilgjengelig. Tolkningen står i flagget.",
    "Spillere uten telte kamper i grunnlaget (nysignert, skadet hele perioden) får ingen forventning. "
    "De må vurderes for hånd.",
    "I dobbelrunder er minuttfordelingen tilnærmet. En spiller som har byttet klubb i grunnlaget, får "
    "rater som blander to roller. Begge deler flagges.",
    "Modellen forklarer om lag 20 % av variansen i poeng for én runde og 30–40 % over fem. Forskjeller "
    "under 2–3 poeng over fem runder er innenfor usikkerheten.",
]

SUMMEFELT_HEL = [
    "minutes", "goals_scored", "assists", "clean_sheets", "goals_conceded", "own_goals",
    "penalties_saved", "penalties_missed", "yellow_cards", "red_cards", "saves", "bonus",
    "bps", "starts", "defensive_contribution", "total_points",
]
SUMMEFELT_DESIMAL = ["expected_goals", "expected_assists", "expected_goals_conceded"]
KOMPONENTER = [
    "oppmote", "mal", "assist", "cs", "baklengs", "redninger", "strafferedning", "dc",
    "bonus", "kort",
]
MND = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
RETUR_RE = re.compile(r"(?:Expected back|Suspended until)\s+(\d{1,2})\s+([A-Z][a-z]{2})")


# --------------------------------------------------------------------------- henting


class Kilde:
    """Leser speilets data/-struktur over HTTP, eller fra en lokal mappe (tester, offline)."""

    def __init__(self, mappe: pathlib.Path | None = None, base: str = MIRROR):
        self.mappe = mappe
        self.base = base

    def tekst(self, sti: str) -> str | None:
        if self.mappe is not None:
            p = self.mappe / sti
            return p.read_text(encoding="utf-8") if p.exists() else None
        req = urllib.request.Request(f"{self.base}/{sti}", headers={"User-Agent": "fpl2627-forventning"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise

    def json(self, sti: str, paakrevd: bool = True):
        t = self.tekst(sti)
        if t is None:
            if paakrevd:
                raise FileNotFoundError(f"{sti} finnes ikke i kilden")
            return None
        return json.loads(t)


@dataclasses.dataclass
class Data:
    elementer: dict[int, dict]
    lag: dict[int, dict]
    events: list[dict]
    poengregler: dict
    kamper: dict[int, dict]
    live: dict[int, dict[int, dict]]
    grunnlag: list[int]
    utelatte_runder: list[int]
    snapshot: dict | None
    tropp_runde: int | None
    tropp: list[int]


def last_data(kilde: Kilde, til_runde: int | None = None) -> Data:
    """Laster bootstrap, kamper og live-filer for alle ferdige, låste runder.

    til_runde begrenser grunnlaget til runder < til_runde (brukes i tilbaketesten).
    """
    b = kilde.json("bootstrap-static.json")
    kamper = {f["id"]: f for f in kilde.json("fixtures.json")}
    snapshot = kilde.json("snapshot.json", paakrevd=False)
    events = b["events"]

    grunnlag, utelatte = [], []
    for e in events:
        if not e.get("finished"):
            continue
        if til_runde is not None and e["id"] >= til_runde:
            continue
        (grunnlag if e.get("data_checked") else utelatte).append(e["id"])

    live = {}
    for n in grunnlag:
        live[n] = {x["id"]: x for x in kilde.json(f"live/gw{n}.json")["elements"]}

    tropp_runde, tropp = None, []
    paabegynt = [e["id"] for e in events if e.get("finished") or e.get("is_current")]
    for n in range(max(paabegynt) if paabegynt else 0, 0, -1):
        p = kilde.json(f"entry/picks/gw{n}.json", paakrevd=False)
        if p and p.get("picks"):
            tropp_runde, tropp = n, [x["element"] for x in p["picks"]]
            break

    return Data(
        elementer={e["id"]: e for e in b["elements"]},
        lag={t["id"]: t for t in b["teams"]},
        events=events,
        poengregler=b.get("game_config", {}).get("scoring", {}),
        kamper=kamper,
        live=live,
        grunnlag=sorted(grunnlag),
        utelatte_runder=sorted(utelatte),
        snapshot=snapshot,
        tropp_runde=tropp_runde,
        tropp=tropp,
    )


# --------------------------------------------------------------------------- fraværsfila


@dataclasses.dataclass
class Fravaer:
    aarsak: str
    sjanse: int | None
    kilde: str


def les_runder(tekst: str) -> list[int]:
    ut: list[int] = []
    for del_ in re.split(r"[;\s]+", tekst.strip()):
        if not del_:
            continue
        if "-" in del_:
            a, b = del_.split("-", 1)
            ut.extend(range(int(a), int(b) + 1))
        else:
            ut.append(int(del_))
    return ut


def les_fravaer(tekst: str | None, elementer: dict[int, dict]) -> tuple[dict[int, dict[int, Fravaer]], list[str]]:
    """Returnerer ({element: {runde: Fravaer}}, feil). Ukjent årsak, ukjent id eller feil navn
    er feil som stopper kjøringen: en rad som treffer feil spiller er verre enn ingen rad."""
    ut: dict[int, dict[int, Fravaer]] = collections.defaultdict(dict)
    feil: list[str] = []
    if not tekst:
        return ut, feil
    for nr, r in enumerate(csv.DictReader(io.StringIO(tekst)), start=2):
        try:
            eid = int(r["id"])
        except (KeyError, TypeError, ValueError):
            feil.append(f"fravaer.csv linje {nr}: mangler gyldig id")
            continue
        el = elementer.get(eid)
        if el is None:
            feil.append(f"fravaer.csv linje {nr}: id {eid} finnes ikke i FPL")
            continue
        navn = (r.get("navn") or "").strip()
        if navn != el["web_name"]:
            feil.append(f"fravaer.csv linje {nr}: id {eid} heter «{el['web_name']}» i FPL, ikke «{navn}»")
            continue
        aarsak = (r.get("aarsak") or "").strip()
        if aarsak not in AARSAKER:
            feil.append(f"fravaer.csv linje {nr}: ukjent årsak «{aarsak}» (lovlige: {', '.join(sorted(AARSAKER))})")
            continue
        sjanse_t = (r.get("sjanse") or "").strip()
        try:
            sjanse = int(sjanse_t) if sjanse_t else None
        except ValueError:
            feil.append(f"fravaer.csv linje {nr}: sjanse «{sjanse_t}» er ikke et heltall")
            continue
        if sjanse is not None and not 0 <= sjanse <= 100:
            feil.append(f"fravaer.csv linje {nr}: sjanse {sjanse} utenfor 0–100")
            continue
        try:
            runder = les_runder(r.get("runder") or "")
        except ValueError:
            feil.append(f"fravaer.csv linje {nr}: kan ikke lese runder «{r.get('runder')}»")
            continue
        if not runder:
            feil.append(f"fravaer.csv linje {nr}: ingen runder oppgitt")
            continue
        for n in runder:
            ut[eid][n] = Fravaer(aarsak, sjanse, (r.get("kilde") or "").strip())
    return ut, feil


def hent_repofil(sti: pathlib.Path) -> tuple[str | None, str]:
    """Lokal fil hvis den finnes (kjøring fra reporoten), ellers main-grenen på GitHub."""
    if sti.exists():
        return sti.read_text(encoding="utf-8"), str(sti)
    try:
        t = Kilde(base=REPO_RAW).tekst(str(sti))
    except (urllib.error.URLError, OSError):
        t = None
    return t, (f"{REPO_RAW}/{sti}" if t is not None else "ikke funnet")


def les_prior(tekst: str | None, lag: dict[int, dict], rho: float = LAG_RHO) -> tuple[dict[int, tuple[float, float]], list[str], list[str]]:
    """Leser forrige sesongs rå lagstyrke (kortnavn → A, D) og demper den med rho.

    Lag som ikke finnes i fila (opprykkslag) får raden OPPRYKK. Returnerer
    (prior per lag-id, lag som fikk opprykksprior, feil)."""
    feil: list[str] = []
    if not tekst:
        return {}, [], ["lagstyrke-prior mangler — alle lag krympes mot 1,0"]
    rader = {}
    for r in csv.DictReader(io.StringIO(tekst)):
        try:
            rader[r["lag"].strip()] = (float(r["A"]), float(r["D"]))
        except (KeyError, ValueError):
            feil.append(f"lagstyrke-prior: ugyldig rad {r}")
    if "OPPRYKK" not in rader:
        feil.append("lagstyrke-prior mangler raden OPPRYKK")
        return {}, [], feil
    prior, opprykk = {}, []
    for tid, t in lag.items():
        a, d = rader.get(t["short_name"], rader["OPPRYKK"])
        if t["short_name"] not in rader:
            opprykk.append(t["short_name"])
        prior[tid] = (1 + rho * (a - 1), 1 + rho * (d - 1))
    return prior, sorted(opprykk), feil


# --------------------------------------------------------------------------- matematikk


def poisson_floor_forventning(lam: float, k: int) -> float:
    """E[⌊X/k⌋] for X ~ Poisson(lam). Summerer til halen er under 1e-12."""
    if lam <= 0:
        return 0.0
    p = math.exp(-lam)
    total, n, kum = 0.0, 0, p
    nmax = int(lam + 12 * math.sqrt(lam) + 30)
    while n < nmax:
        n += 1
        p *= lam / n
        kum += p
        total += p * (n // k)
        if kum > 1 - 1e-12 and n > lam:
            break
    return total


def eb_k(grupper: list[list[float]], kmin: float = 1.0, kmax: float = 38.0) -> tuple[float, dict]:
    """Krympingskonstant k = σ²(innen) / σ²(sann mellom), estimert med momentmetoden.

    k uttrykkes i antall observasjoner: et estimat med n observasjoner krympes som
    (n·snitt + k·prior) / (n + k). Er variansen mellom grupper ikke større enn støyen
    tilsier, blir k = kmax (sterk krymping).
    """
    g = [x for x in grupper if len(x) >= 1]
    innen_sum, innen_df = 0.0, 0
    for x in g:
        if len(x) >= 2:
            m = sum(x) / len(x)
            innen_sum += sum((v - m) ** 2 for v in x)
            innen_df += len(x) - 1
    if innen_df == 0 or len(g) < 3:
        return kmax, {"grunn": "for få observasjoner"}
    s2_innen = innen_sum / innen_df
    snitt = [sum(x) / len(x) for x in g]
    m_alle = sum(snitt) / len(snitt)
    s2_mellom = sum((s - m_alle) ** 2 for s in snitt) / (len(snitt) - 1)
    n_snitt = sum(len(x) for x in g) / len(g)
    sann = s2_mellom - s2_innen / n_snitt
    if sann <= 0:
        return kmax, {"s2_innen": s2_innen, "s2_mellom": s2_mellom, "sann": sann}
    k = min(kmax, max(kmin, s2_innen / sann))
    return k, {"s2_innen": s2_innen, "s2_mellom": s2_mellom, "sann": sann}


def ols(x: list[list[float]], y: list[float]) -> list[float]:
    """Minste kvadraters løsning via normallikningene, Gauss-eliminasjon med pivotering."""
    p = len(x[0])
    a = [[0.0] * (p + 1) for _ in range(p)]
    for rad, yi in zip(x, y):
        for i in range(p):
            for j in range(p):
                a[i][j] += rad[i] * rad[j]
            a[i][p] += rad[i] * yi
    for i in range(p):
        a[i][i] += 1e-9  # numerisk stabilitet; påvirker ikke resultatet målbart
    for kol in range(p):
        piv = max(range(kol, p), key=lambda r: abs(a[r][kol]))
        if abs(a[piv][kol]) < 1e-12:
            raise ValueError("singulær matrise i bonusmodellen")
        a[kol], a[piv] = a[piv], a[kol]
        for r in range(p):
            if r != kol:
                f = a[r][kol] / a[kol][kol]
                for c in range(kol, p + 1):
                    a[r][c] -= f * a[kol][c]
    return [a[i][p] / a[i][i] for i in range(p)]


def pearson(a: list[float], b: list[float]) -> float:
    n = len(a)
    if n < 3:
        return float("nan")
    ma, mb = sum(a) / n, sum(b) / n
    sa = math.sqrt(sum((v - ma) ** 2 for v in a))
    sb = math.sqrt(sum((v - mb) ** 2 for v in b))
    if sa == 0 or sb == 0:
        return float("nan")
    return sum((u - ma) * (v - mb) for u, v in zip(a, b)) / (sa * sb)


def rangering(v: list[float]) -> list[float]:
    orden = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v)
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and v[orden[j + 1]] == v[orden[i]]:
            j += 1
        for t in range(i, j + 1):
            r[orden[t]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(a: list[float], b: list[float]) -> float:
    return pearson(rangering(a), rangering(b))


# --------------------------------------------------------------------------- lag per runde


def kamper_i_runde(data: Data, n: int) -> list[dict]:
    return [f for f in data.kamper.values() if f.get("event") == n]


def lagkart(data: Data) -> tuple[dict[tuple[int, int], int | None], list[str]]:
    """{(runde, element): lag} for alle spiller-runder med minutter.

    Laget bestemmes av kampen spilleren står oppført med i explain. Står spillerens
    nåværende lag i kampen, er det laget. Ellers (spilleren har byttet klubb) slås han
    opp i kampens statistikklister. Uløste rader rapporteres.
    """
    kart: dict[tuple[int, int], int | None] = {}
    uloste: list[str] = []
    for n, rader in data.live.items():
        for eid, x in rader.items():
            if x["stats"]["minutes"] <= 0:
                continue
            fids = [e["fixture"] for e in x.get("explain", [])]
            el = data.elementer.get(eid)
            lag = None
            for fid in fids:
                f = data.kamper.get(fid)
                if f is None:
                    continue
                if el and el["team"] in (f["team_h"], f["team_a"]):
                    lag = el["team"]
                    break
                for s in f.get("stats", []):
                    if any(o["element"] == eid for o in s["h"]):
                        lag = f["team_h"]
                    elif any(o["element"] == eid for o in s["a"]):
                        lag = f["team_a"]
                    if lag is not None:
                        break
                if lag is not None:
                    break
            kart[(n, eid)] = lag
            if lag is None:
                navn = el["web_name"] if el else str(eid)
                uloste.append(f"GW{n} {navn}")
    return kart, uloste


@dataclasses.dataclass
class Lagrad:
    lag: int
    runde: int
    motstandere: list[tuple[int, str]]
    xgf: float
    xga: float
    enkel: bool


def lagrader(data: Data, kart: dict[tuple[int, int], int | None]) -> list[Lagrad]:
    """Lagets xG for og mot per runde. I enkeltrunder er xG mot = motstanderens xG.
    Har noen av lagene to kamper i runden, brukes Σ xGC for lagets spillere / 11."""
    ut: list[Lagrad] = []
    for n in data.grunnlag:
        kamper = [f for f in kamper_i_runde(data, n) if f.get("finished")]
        per_lag: dict[int, list[tuple[int, str]]] = collections.defaultdict(list)
        for f in kamper:
            per_lag[f["team_h"]].append((f["team_a"], "H"))
            per_lag[f["team_a"]].append((f["team_h"], "B"))
        xgf: dict[int, float] = collections.defaultdict(float)
        xgc: dict[int, float] = collections.defaultdict(float)
        for eid, x in data.live[n].items():
            lag = kart.get((n, eid))
            if lag is None:
                continue
            xgf[lag] += float(x["stats"]["expected_goals"])
            xgc[lag] += float(x["stats"]["expected_goals_conceded"])
        for lag, mot in per_lag.items():
            enkel = len(mot) == 1 and len(per_lag[mot[0][0]]) == 1
            xga = xgf[mot[0][0]] if enkel else xgc[lag] / 11
            ut.append(Lagrad(lag, n, mot, xgf[lag], xga, enkel))
    return ut


# --------------------------------------------------------------------------- lagstyrke


@dataclasses.dataclass
class Lagstyrke:
    mu: float
    bane_angrep: dict[str, float]
    bane_forsvar: dict[str, float]
    A: dict[int, float]
    D: dict[int, float]
    kA: float
    kD: float
    noytral: bool = False

    def angrep(self, motstander: int, bane: str) -> float:
        """Multiplikator på en spillers xG/xA mot denne motstanderen på denne banen."""
        if self.noytral:
            return 1.0
        return self.D.get(motstander, 1.0) * self.bane_angrep[bane]

    def press(self, motstander: int, bane: str) -> float:
        """Multiplikator på skudd mot eget mål (redninger) mot denne motstanderen."""
        if self.noytral:
            return 1.0
        return self.A.get(motstander, 1.0) * self.bane_forsvar[bane]

    def lam90(self, lag: int, motstander: int, bane: str) -> float:
        """Lagets forventede baklengs per 90 i denne kampen."""
        if self.noytral:
            return self.mu * self.D.get(lag, 1.0)
        return self.mu * self.D.get(lag, 1.0) * self.A.get(motstander, 1.0) * self.bane_forsvar[bane]


def tilpass_lagstyrke(rader: list[Lagrad], noytral: bool = False,
                      kA: float | None = None, kD: float | None = None,
                      prior: dict[int, tuple[float, float]] | None = None) -> Lagstyrke:
    """Tilpasser μ, banefaktorer og lagstyrke A (angrep) og D (forsvar).

    A og D krympes mot prior (standard 1,0) med vekt k: (n·rå + k·prior) / (n + k).
    kA/kD = None betyr at k estimeres fra dataene (empirisk Bayes) — brukes bare som
    diagnostikk; i produksjon settes k og prior fra kryssvalideringen (se LAG_KA/LAG_KD).
    """
    if not rader:
        raise ValueError("ingen lagkamper i grunnlaget — kan ikke tilpasse lagstyrke")
    kamper = sum(len(r.motstandere) for r in rader)
    mu = sum(r.xgf for r in rader) / kamper
    if mu <= 0:
        raise ValueError("samlet xG i grunnlaget er 0 — kan ikke tilpasse lagstyrke")
    hjemme = [r.xgf for r in rader if r.enkel and r.motstandere[0][1] == "H"]
    borte = [r.xgf for r in rader if r.enkel and r.motstandere[0][1] == "B"]
    h = (sum(hjemme) / len(hjemme)) / mu if hjemme else 1.0
    b = (sum(borte) / len(borte)) / mu if borte else 1.0
    bane_angrep = {"H": h, "B": b}
    bane_forsvar = {"H": b, "B": h}  # hjemme møter du et lag som spiller borte
    lag = sorted({r.lag for r in rader})
    A = {t: 1.0 for t in lag}
    D = {t: 1.0 for t in lag}
    for _ in range(200):
        nyA, nyD = {}, {}
        for t in lag:
            rt = [r for r in rader if r.lag == t]
            nevA = sum(mu * sum(D[o] * bane_angrep[v] for o, v in r.motstandere) for r in rt)
            nevD = sum(mu * sum(A[o] * bane_forsvar[v] for o, v in r.motstandere) for r in rt)
            nyA[t] = sum(r.xgf for r in rt) / nevA if nevA > 0 else 1.0
            nyD[t] = sum(r.xga for r in rt) / nevD if nevD > 0 else 1.0
        mA = sum(nyA.values()) / len(nyA)
        mD = sum(nyD.values()) / len(nyD)
        nyA = {t: v / mA for t, v in nyA.items()}
        nyD = {t: v / mD for t, v in nyD.items()}
        endring = max(max(abs(nyA[t] - A[t]) for t in lag), max(abs(nyD[t] - D[t]) for t in lag))
        A, D = nyA, nyD
        if endring < 1e-10:
            break

    if kA is None or kD is None:
        # Empirisk Bayes (bare diagnostikk): k fra kamp-for-kamp-forholdstall.
        gA, gD = collections.defaultdict(list), collections.defaultdict(list)
        for r in rader:
            if not r.enkel:
                continue
            o, v = r.motstandere[0]
            if D[o] > 0:
                gA[r.lag].append(r.xgf / (mu * D[o] * bane_angrep[v]))
            if A[o] > 0:
                gD[r.lag].append(r.xga / (mu * A[o] * bane_forsvar[v]))
        if kA is None:
            kA, _ = eb_k(list(gA.values()))
        if kD is None:
            kD, _ = eb_k(list(gD.values()))
    n = collections.Counter()
    for r in rader:
        n[r.lag] += len(r.motstandere)
    pr = prior or {}
    A = {t: (n[t] * A[t] + kA * pr.get(t, (1.0, 1.0))[0]) / (n[t] + kA) for t in lag}
    D = {t: (n[t] * D[t] + kD * pr.get(t, (1.0, 1.0))[1]) / (n[t] + kD) for t in lag}
    return Lagstyrke(mu, bane_angrep, bane_forsvar, A, D, kA, kD, noytral)


# --------------------------------------------------------------------------- spillerrunder


@dataclasses.dataclass
class Spillerrunde:
    runde: int
    kamper: int            # lagets kamper i runden (2 = dobbelrunde)
    minutter: int
    starter: int
    mal: int
    assist: int
    xg: float
    xa: float
    dc: int
    redninger: int
    bonus: int
    gule: int
    rode: int
    selvmal: int
    straffe_redd: int
    cs: int
    poeng: int
    motstandere: list[tuple[int, str]]
    lag: int = 0


def spillerrunder(data: Data, eid: int, kart: dict[tuple[int, int], int | None]) -> list[Spillerrunde]:
    """Én rad per runde i grunnlaget der spilleren finnes i live-data og laget hans spilte."""
    el = data.elementer[eid]
    ut: list[Spillerrunde] = []
    for n in data.grunnlag:
        x = data.live[n].get(eid)
        if x is None:
            continue  # ikke registrert i FPL ennå
        s = x["stats"]
        fids = [e["fixture"] for e in x.get("explain", []) if e["fixture"] in data.kamper]
        lag = kart.get((n, eid)) or el["team"]
        if not fids:
            fids = [f["id"] for f in kamper_i_runde(data, n) if lag in (f["team_h"], f["team_a"])]
        mot = []
        for fid in fids:
            f = data.kamper[fid]
            if f["team_h"] == lag:
                mot.append((f["team_a"], "H"))
            elif f["team_a"] == lag:
                mot.append((f["team_h"], "B"))
        if not mot:
            continue  # laget hadde ikke kamp (blank runde), eller laget er ukjent
        ut.append(Spillerrunde(
            runde=n, kamper=len(mot), minutter=s["minutes"], starter=s.get("starts", 0),
            mal=s["goals_scored"], assist=s["assists"],
            xg=float(s["expected_goals"]), xa=float(s["expected_assists"]),
            dc=s["defensive_contribution"], redninger=s["saves"], bonus=s["bonus"],
            gule=s["yellow_cards"], rode=s["red_cards"], selvmal=s["own_goals"],
            straffe_redd=s["penalties_saved"], cs=s["clean_sheets"], poeng=s["total_points"],
            motstandere=mot, lag=lag,
        ))
    return ut


# --------------------------------------------------------------------------- ligarater og bonus


@dataclasses.dataclass
class Ligarater:
    rode90: dict[str, float]
    selvmal90: dict[str, float]
    straffe_redd90: float
    gule90: dict[str, float]
    gule_k: float
    bonus_beta: dict[str, list[float]]
    bonus_felt: dict[str, list[str]]
    bonus_kort: dict[str, float]
    bonus_k: float
    bonus_n: dict[str, int]


# Feltene følger BPS-tabellen i context/05: clean sheet gir BPS bare til keeper og forsvarer,
# så CS er ikke med for midtbane og spiss.
BONUS_FELT = {
    "GKP": ["cs", "redninger"],
    "DEF": ["mal", "assist", "cs", "dc"],
    "MID": ["mal", "assist", "dc"],
    "FWD": ["mal", "assist", "dc"],
}


def dc_treff(dc: int, pos: str) -> int:
    t = DC_TERSKEL[pos]
    return 1 if t is not None and dc >= t else 0


def bonus_rad(r: Spillerrunde, pos: str) -> list[float]:
    verdier = {"mal": r.mal, "assist": r.assist, "cs": r.cs, "redninger": r.redninger,
               "dc": dc_treff(r.dc, pos)}
    return [1.0] + [float(verdier[f]) for f in BONUS_FELT[pos]]


def tilpass_ligarater(data: Data, alle: dict[int, list[Spillerrunde]]) -> tuple[Ligarater, dict[int, float]]:
    """Ligasnitt for sjeldne hendelser, gule kort med krymping, og bonusmodellen.

    Returnerer også hver spillers krympede bonusavvik (spillerens bonus utover det
    modellen forklarer med mål, assist, CS, redninger og DC-treff)."""
    minutter = collections.Counter()
    rode = collections.Counter()
    selvmal = collections.Counter()
    gule = collections.Counter()
    straffe_redd, keepermin = 0, 0
    gule_grupper: dict[str, list[list[float]]] = collections.defaultdict(list)
    x_pos: dict[str, list[list[float]]] = collections.defaultdict(list)
    y_pos: dict[str, list[float]] = collections.defaultdict(list)
    eier: dict[str, list[int]] = collections.defaultdict(list)
    kort_sum: dict[str, float] = collections.defaultdict(float)
    kort_n = collections.Counter()

    for eid, rader in alle.items():
        pos = POS[data.elementer[eid]["element_type"]]
        g_obs = []
        for r in rader:
            if r.minutter <= 0:
                continue
            minutter[pos] += r.minutter
            rode[pos] += r.rode
            selvmal[pos] += r.selvmal
            gule[pos] += r.gule
            if pos == "GKP":
                straffe_redd += r.straffe_redd
                keepermin += r.minutter
            if r.kamper == 1 and r.minutter >= MIN_LANG:
                g_obs.append(float(r.gule))
                x_pos[pos].append(bonus_rad(r, pos))
                y_pos[pos].append(float(r.bonus))
                eier[pos].append(eid)
            elif r.kamper == 1:
                kort_sum[pos] += r.bonus
                kort_n[pos] += 1
        if g_obs:
            gule_grupper[pos].append(g_obs)

    beta: dict[str, list[float]] = {}
    resid: dict[int, list[float]] = collections.defaultdict(list)
    for pos in POSISJONER:
        felt = BONUS_FELT[pos]
        xs, ys = x_pos[pos], y_pos[pos]
        if len(ys) < len(felt) + 5:
            beta[pos] = [sum(ys) / len(ys) if ys else 0.0] + [0.0] * len(felt)
        else:
            # Et felt uten variasjon (f.eks. ingen spiss over DC-terskelen) kan ikke estimeres
            # og settes til 0 i stedet for å gjøre matrisen singulær.
            aktive = [j for j in range(1, len(felt) + 1) if len({rad[j] for rad in xs}) > 1]
            br = ols([[rad[0]] + [rad[j] for j in aktive] for rad in xs], ys)
            beta[pos] = [br[0]] + [0.0] * len(felt)
            for i, j in enumerate(aktive):
                beta[pos][j] = br[i + 1]
        for rad, yi, eid in zip(xs, ys, eier[pos]):
            resid[eid].append(yi - sum(b * v for b, v in zip(beta[pos], rad)))
    bonus_k, _ = eb_k(list(resid.values()))
    avvik = {eid: (sum(v) / len(v)) * len(v) / (len(v) + bonus_k) for eid, v in resid.items()}

    alle_g = [g for grupper in gule_grupper.values() for g in grupper]
    gule_k, _ = eb_k(alle_g)

    def per90(teller: collections.Counter, pos: str) -> float:
        return teller[pos] / minutter[pos] * 90 if minutter[pos] else 0.0

    return Ligarater(
        rode90={p: per90(rode, p) for p in POSISJONER},
        selvmal90={p: per90(selvmal, p) for p in POSISJONER},
        straffe_redd90=straffe_redd / keepermin * 90 if keepermin else 0.0,
        gule90={p: per90(gule, p) for p in POSISJONER},
        gule_k=gule_k,
        bonus_beta=beta,
        bonus_felt=dict(BONUS_FELT),
        bonus_kort={p: (kort_sum[p] / kort_n[p] if kort_n[p] else 0.0) for p in POSISJONER},
        bonus_k=bonus_k,
        bonus_n={p: len(y_pos[p]) for p in POSISJONER},
    ), avvik


# --------------------------------------------------------------------------- spillerprofil


@dataclasses.dataclass
class Profil:
    eid: int
    navn: str
    lag: int
    pos: str
    pris: float
    status: str
    sjanse_neste: int | None
    nyhet: str
    straffe: int | None
    telte: int = 0
    starter: int = 0
    innbytter: int = 0
    startandel: float = 0.0
    innbytterandel: float = 0.0
    start_siste3: float | None = None
    min_start: float = 0.0
    min_innbytter: float = 0.0
    p60_start: float = 0.0
    p60_innbytter: float = 0.0
    min60: float = 90.0
    minutter: int = 0
    xg90: float = 0.0
    xa90: float = 0.0
    xg90_robust: float = 0.0
    xa90_robust: float = 0.0
    nevner: float = 0.0
    nevner_robust: float = 0.0
    xg90_prior: float = 0.0
    xa90_prior: float = 0.0
    startpris: float = 0.0
    xgi90_raa: float = 0.0
    xgi90_uten_beste: float = 0.0
    andel_beste: float = 0.0
    beste_runde: int | None = None
    redn90: float = 0.0
    dc_start: float = 0.0
    dc_innbytter: float = 0.0
    dc_treff_s: int = 0
    dc_n_s: int = 0
    dc_treff_i: int = 0
    dc_n_i: int = 0
    dc_grunnlag: str = ""
    gule90: float = 0.0
    bonus_avvik: float = 0.0
    poeng_sesong: int = 0
    poeng_uten_beste: int = 0
    fravaer_uavklart: list[int] = dataclasses.field(default_factory=list)
    fravaer_utelatt: list[int] = dataclasses.field(default_factory=list)
    flagg: list[str] = dataclasses.field(default_factory=list)


def bygg_profil(data: Data, eid: int, rader: list[Spillerrunde], styrke: Lagstyrke,
                fravaer: dict[int, Fravaer], liga: Ligarater, bonus_avvik: dict[int, float]) -> Profil:
    el = data.elementer[eid]
    pos = POS[el["element_type"]]
    p = Profil(
        eid=eid, navn=el["web_name"], lag=el["team"], pos=pos, pris=el["now_cost"] / 10,
        status=el["status"], sjanse_neste=el.get("chance_of_playing_next_round"),
        nyhet=el.get("news") or "", straffe=el.get("penalties_order"),
    )
    p.startpris = (el["now_cost"] - (el.get("cost_change_start") or 0)) / 10

    # --- minutter og rolle (minimumskrav 11)
    telte_seq: list[int] = []  # 1 = start, 0 = ikke start, i kronologisk rekkefølge
    telte_runde: list[tuple[int, int, int]] = []  # (runde, start, innbytter) per telt kamp
    min_start, min_innb, starter_60, innb_60 = [], [], 0, 0
    for r in rader:
        if r.kamper > 1 and r.minutter > 0:
            # Dobbelrunde: live-data summerer begge kampene. Starter telles eksakt, minutter
            # per start og DC-treff kan ikke fordeles og holdes utenfor de ratene.
            p.flagg.append(f"DGW i grunnlaget (GW{r.runde}): minuttfordeling tilnærmet")
            st = min(r.starter, r.kamper)
            p.telte += r.kamper
            p.starter += st
            telte_seq.extend([1] * st + [0] * (r.kamper - st))
            telte_runde.extend([(r.runde, 1, 0)] * st + [(r.runde, 0, 1)] * (r.kamper - st))
            if st == r.kamper:
                # Startet alle kampene: minuttene fordeles likt. Ellers er fordelingen ukjent.
                for _ in range(st):
                    min_start.append(r.minutter / r.kamper)
                    starter_60 += r.minutter / r.kamper >= MIN_LANG
            continue
        if r.minutter > 0 and r.starter >= 1:
            p.telte += 1
            p.starter += 1
            telte_seq.append(1)
            telte_runde.append((r.runde, 1, 0))
            min_start.append(r.minutter)
            starter_60 += r.minutter >= MIN_LANG
        elif r.minutter > 0:
            p.telte += 1
            p.innbytter += 1
            telte_seq.append(0)
            telte_runde.append((r.runde, 0, 1))
            min_innb.append(r.minutter)
            innb_60 += r.minutter >= MIN_LANG
        else:
            f = fravaer.get(r.runde)
            if f is not None and f.aarsak in AARSAK_UTELATES:
                p.fravaer_utelatt.append(r.runde)
                continue
            p.telte += r.kamper
            telte_seq.extend([0] * r.kamper)
            telte_runde.extend([(r.runde, 0, 0)] * r.kamper)
            if f is None:
                p.fravaer_uavklart.append(r.runde)
    # Start- og innbytterandel med vekt AVTAK^(alder i runder): nyere kamper teller mer.
    siste = max((n for n, _, _ in telte_runde), default=0)
    w = [(AVTAK ** (siste - n), st, ib) for n, st, ib in telte_runde]
    w_alle = sum(v for v, _, _ in w)
    w_start = sum(v for v, st, _ in w if st)
    w_ikke = w_alle - w_start
    p.startandel = w_start / w_alle if w_alle > 0 else 0.0
    p.innbytterandel = sum(v for v, _, ib in w if ib) / w_ikke if w_ikke > 1e-12 else 0.0
    if len(telte_seq) >= 3:
        p.start_siste3 = sum(telte_seq[-3:]) / 3
    p.min_start = sum(min_start) / len(min_start) if min_start else 0.0
    p.min_innbytter = sum(min_innb) / len(min_innb) if min_innb else 0.0
    p.p60_start = starter_60 / len(min_start) if min_start else 0.0
    p.p60_innbytter = innb_60 / len(min_innb) if min_innb else 0.0
    lange = [m for m in min_start if m >= MIN_LANG]
    p.min60 = sum(lange) / len(lange) if lange else 90.0
    if p.fravaer_uavklart:
        p.flagg.append(
            "UAVKLART FRAVÆR GW" + ", GW".join(map(str, p.fravaer_uavklart))
            + " — telt som ikke-start; før årsaken i context/fravaer.csv"
        )
    if p.telte == 0:
        p.flagg.append("ingen telte kamper i grunnlaget — ingen forventning")
    uvektet = p.starter / p.telte if p.telte else 0.0
    if p.start_siste3 is not None and abs(p.start_siste3 - uvektet) >= 0.34:
        p.flagg.append(f"rollen endret? start siste 3: {p.start_siste3:.0%} mot {uvektet:.0%} totalt")

    # --- rater per 90, motstandsjustert, med og uten beste kamp
    spilt = [r for r in rader if r.minutter > 0]
    p.minutter = sum(r.minutter for r in spilt)
    p.poeng_sesong = sum(r.poeng for r in rader)
    if spilt:
        beste = max(spilt, key=lambda r: (r.xg + r.xa, -r.runde))
        p.beste_runde = beste.runde
        p.poeng_uten_beste = p.poeng_sesong - max(r.poeng for r in rader)

        def rater(utvalg: list[Spillerrunde]) -> tuple[float, float, float]:
            nevner = sum(r.minutter / 90 * sum(styrke.angrep(o, v) for o, v in r.motstandere) / len(r.motstandere)
                         for r in utvalg)
            if nevner <= 0:
                return 0.0, 0.0, 0.0
            xg = sum(r.xg for r in utvalg) / nevner
            xa = sum(r.xa for r in utvalg) / nevner
            return xg, xa, nevner

        p.xg90, p.xa90, p.nevner = rater(spilt)
        if len(spilt) >= 3:
            uten = [r for r in spilt if r is not beste]
            p.xg90_robust, p.xa90_robust, p.nevner_robust = rater(uten)
        else:
            p.xg90_robust, p.xa90_robust, p.nevner_robust = p.xg90, p.xa90, p.nevner
        xgi = sum(r.xg + r.xa for r in spilt)
        p.xgi90_raa = xgi / p.minutter * 90
        rest_min = p.minutter - beste.minutter
        p.xgi90_uten_beste = (xgi - beste.xg - beste.xa) / rest_min * 90 if rest_min > 0 else 0.0
        p.andel_beste = (beste.xg + beste.xa) / xgi if xgi > 0 else 0.0
        if pos == "GKP":
            nevner = sum(r.minutter / 90 * sum(styrke.press(o, v) for o, v in r.motstandere) / len(r.motstandere)
                         for r in spilt)
            p.redn90 = sum(r.redninger for r in spilt) / nevner if nevner > 0 else 0.0
        # gule kort: krympet mot posisjonssnitt (empirisk Bayes, k i kamper à 90 min)
        k = liga.gule_k
        p.gule90 = (sum(r.gule for r in spilt) + k * liga.gule90[pos]) / (p.minutter / 90 + k)
    else:
        p.gule90 = liga.gule90[pos]
    if p.minutter and p.minutter < 270:
        p.flagg.append(f"få minutter ({p.minutter}) — ratene er usikre")
    if p.andel_beste >= 0.5 and len(spilt) >= 3 and p.xgi90_raa * p.minutter / 90 >= 1.0:
        p.flagg.append(f"én kamp (GW{p.beste_runde}) står for {p.andel_beste:.0%} av xGI")

    # --- DC-treff fra rundetallene (minimumskrav 12)
    terskel = DC_TERSKEL[pos]
    if terskel is not None:
        st = [r for r in rader if r.kamper == 1 and r.minutter > 0 and r.starter >= 1]
        ib = [r for r in rader if r.kamper == 1 and r.minutter > 0 and r.starter == 0]
        st_treff = sum(r.dc >= terskel for r in st)
        ib_treff = sum(r.dc >= terskel for r in ib)
        p.dc_treff_s, p.dc_n_s, p.dc_treff_i, p.dc_n_i = st_treff, len(st), ib_treff, len(ib)
        # Råraten; krympes mot posisjonssnittet i krymp_dc når alle profiler er bygget.
        p.dc_start = st_treff / len(st) if st else 0.0
        p.dc_innbytter = ib_treff / len(ib) if ib else 0.0
        p.dc_grunnlag = f"{st_treff}/{len(st)}"

    andre = sorted({r.runde for r in rader if r.lag and r.lag != p.lag and r.minutter > 0})
    if andre:
        p.flagg.append("spilte for en annen klubb i GW" + ", GW".join(map(str, andre))
                       + " — ratene blander to roller")
    p.bonus_avvik = bonus_avvik.get(eid, 0.0)
    if p.straffe == 1:
        p.flagg.append("første straffeskytter (penalties_order 1)")
    return p


# --------------------------------------------------------------------------- tilgjengelighet


def retur_dato(nyhet: str, sesong_aar: int) -> dt.date | None:
    """«Expected back 24 Oct» / «Suspended until 25 Oct» -> dato. Måned fra juli og
    utover hører til sesongens første år, januar–juni til det andre."""
    m = RETUR_RE.search(nyhet or "")
    if not m:
        return None
    mnd = MND.get(m.group(2))
    if mnd is None:
        return None
    aar = sesong_aar if mnd >= 7 else sesong_aar + 1
    try:
        return dt.date(aar, mnd, int(m.group(1)))
    except ValueError:
        return None


def tilgjengelighet(p: Profil, runde: int, kampdato: dt.date, sjanse_runde: int | None,
                    overstyr: dict[int, Fravaer], sesong_aar: int) -> tuple[float, str]:
    """Sannsynlighet for at spilleren er tilgjengelig i denne kampen, med begrunnelse."""
    f = overstyr.get(runde)
    if f is not None:
        sj = f.sjanse if f.sjanse is not None else (0 if f.aarsak in AARSAK_UTELATES else 100)
        return sj / 100, f"fravaer.csv: {f.aarsak}"
    if p.status == "u":
        return 0.0, "ikke tilgjengelig i FPL (u)"
    # En returdato i FPL-nyheten er mer presis enn prosentsjansen, og brukes alene når den finnes.
    ret = retur_dato(p.nyhet, sesong_aar)
    if ret is not None:
        if kampdato < ret:
            return 0.0, f"ute til {ret:%d.%m.} ifølge FPL-nyhet"
        return 1.0, f"tilgjengelig f.o.m. {ret:%d.%m.} (tolket fra FPL-nyhet)"
    if runde == sjanse_runde and p.sjanse_neste is not None:
        return p.sjanse_neste / 100, f"FPL-sjanse {p.sjanse_neste} %"
    if p.status in ("i", "s", "n"):
        return 0.0, f"status {p.status} uten returdato"
    return 1.0, ""


# --------------------------------------------------------------------------- forventning per kamp


def forvent_kamp(p: Profil, styrke: Lagstyrke, liga: Ligarater, motstander: int, bane: str,
                 a: float, robust: bool = False) -> dict[str, float]:
    pos = p.pos
    p_start = a * p.startandel
    p_innb = a * (1 - p.startandel) * p.innbytterandel
    e_min = p_start * p.min_start + p_innb * p.min_innbytter
    p60 = p_start * p.p60_start + p_innb * p.p60_innbytter
    p_kort = p_start + p_innb - p60

    xg90 = p.xg90_robust if robust else p.xg90
    xa90 = p.xa90_robust if robust else p.xa90
    ang = styrke.angrep(motstander, bane)
    lam90 = styrke.lam90(p.lag, motstander, bane)

    k: dict[str, float] = {}
    k["oppmote"] = POENG["long_play"] * p60 + POENG["short_play"] * p_kort
    k["mal"] = xg90 * MAL_FAKTOR[pos] * ang * e_min / 90 * POENG["goals_scored"][pos]
    k["assist"] = xa90 * ASSIST_FAKTOR[pos] * ang * e_min / 90 * POENG["assists"]
    p_cs60 = math.exp(-CS_FAKTOR * lam90 * p.min60 / 90)
    k["cs"] = p60 * p_cs60 * POENG["clean_sheets"][pos]
    gc = POENG["goals_conceded"][pos]
    k["baklengs"] = gc * (
        p_start * poisson_floor_forventning(lam90 * p.min_start / 90, BAKLENGS_PER_POENG)
        + p_innb * poisson_floor_forventning(lam90 * p.min_innbytter / 90, BAKLENGS_PER_POENG)
    ) if gc else 0.0
    if pos == "GKP":
        r90 = p.redn90 * styrke.press(motstander, bane)
        k["redninger"] = POENG["saves"] * (
            p_start * poisson_floor_forventning(r90 * p.min_start / 90, REDNINGER_PER_POENG)
            + p_innb * poisson_floor_forventning(r90 * p.min_innbytter / 90, REDNINGER_PER_POENG)
        )
        k["strafferedning"] = liga.straffe_redd90 * e_min / 90 * POENG["penalties_saved"]
    else:
        k["redninger"] = 0.0
        k["strafferedning"] = 0.0
    k["dc"] = POENG["defensive_contribution"][pos] * (p_start * p.dc_start + p_innb * p.dc_innbytter)

    # Bonus: lineær modell satt inn med forventede verdier gitt ≥60 min.
    forventet60 = {
        "mal": xg90 * MAL_FAKTOR[pos] * ang * p.min60 / 90,
        "assist": xa90 * ASSIST_FAKTOR[pos] * ang * p.min60 / 90,
        "cs": p_cs60,
        "redninger": p.redn90 * styrke.press(motstander, bane) * p.min60 / 90 if pos == "GKP" else 0.0,
        "dc": p.dc_start,
    }
    beta = liga.bonus_beta[pos]
    b60 = beta[0] + sum(b * forventet60[f] for b, f in zip(beta[1:], liga.bonus_felt[pos])) + p.bonus_avvik
    k["bonus"] = p60 * max(0.0, b60) + p_kort * liga.bonus_kort[pos]
    k["kort"] = (POENG["yellow_cards"] * p.gule90 + POENG["red_cards"] * liga.rode90[pos]
                 + POENG["own_goals"] * liga.selvmal90[pos]) * e_min / 90
    k["total"] = sum(k[c] for c in KOMPONENTER)
    k["e_min"] = e_min
    return k


# --------------------------------------------------------------------------- hele modellen


@dataclasses.dataclass
class Modell:
    data: Data
    styrke: Lagstyrke
    liga: Ligarater
    profiler: dict[int, Profil]
    rader: dict[int, list[Spillerrunde]]
    uloste_lag: list[str]
    lagrader: list[Lagrad]


def bygg_modell(data: Data, fravaer: dict[int, dict[int, Fravaer]], noytral: bool = False,
                prior: dict[int, tuple[float, float]] | None = None, spiller_k: float | None = None) -> Modell:
    if spiller_k is None:
        spiller_k = SPILLER_K
    kart, uloste = lagkart(data)
    lr = lagrader(data, kart)
    styrke = tilpass_lagstyrke(lr, noytral=noytral, kA=LAG_KA, kD=LAG_KD, prior=prior)
    alle = {eid: spillerrunder(data, eid, kart) for eid in data.elementer}
    liga, avvik = tilpass_ligarater(data, alle)
    profiler = {
        eid: bygg_profil(data, eid, alle[eid], styrke, fravaer.get(eid, {}), liga, avvik)
        for eid in data.elementer
    }
    krymp_mot_pris(profiler, spiller_k)
    krymp_dc(profiler, DC_K)
    return Modell(data, styrke, liga, profiler, alle, uloste, lr)


def krymp_dc(profiler: dict[int, Profil], k: float) -> None:
    """DC-treffrate i starter og som innbytter krympes mot posisjonens samlede treffrate."""
    for pos in POSISJONER:
        if DC_TERSKEL[pos] is None:
            continue
        utvalg = [p for p in profiler.values() if p.pos == pos]
        ns = sum(p.dc_n_s for p in utvalg)
        ni = sum(p.dc_n_i for p in utvalg)
        snitt_s = sum(p.dc_treff_s for p in utvalg) / ns if ns else 0.0
        snitt_i = sum(p.dc_treff_i for p in utvalg) / ni if ni else 0.0
        for p in utvalg:
            p.dc_start = (p.dc_treff_s + k * snitt_s) / (p.dc_n_s + k) if p.dc_n_s + k > 0 else 0.0
            p.dc_innbytter = (p.dc_treff_i + k * snitt_i) / (p.dc_n_i + k) if p.dc_n_i + k > 0 else 0.0


def pris_prior(profiler: dict[int, Profil], felt: str) -> dict[str, tuple[float, float]]:
    """Vektet minstekvadrat felt ~ a + b·startpris per posisjon, spillere med ≥180 min, vekt = minutter."""
    ut = {}
    for pos in POSISJONER:
        utvalg = [p for p in profiler.values() if p.pos == pos and p.minutter >= 180]
        w = [p.minutter for p in utvalg]
        if len(utvalg) < 10 or sum(w) == 0:
            snitt = sum(getattr(p, felt) * p.minutter for p in utvalg) / sum(w) if utvalg and sum(w) else 0.0
            ut[pos] = (snitt, 0.0)
            continue
        x = [p.startpris for p in utvalg]
        y = [getattr(p, felt) for p in utvalg]
        mx = sum(wi * xi for wi, xi in zip(w, x)) / sum(w)
        my = sum(wi * yi for wi, yi in zip(w, y)) / sum(w)
        sxx = sum(wi * (xi - mx) ** 2 for wi, xi in zip(w, x))
        b = sum(wi * (xi - mx) * (yi - my) for wi, xi, yi in zip(w, x, y)) / sxx if sxx > 0 else 0.0
        ut[pos] = (my - b * mx, b)
    return ut


def krymp_mot_pris(profiler: dict[int, Profil], k: float) -> None:
    """Krymper xG/90 og xA/90 (og den robuste varianten) mot posisjon- og prisprioren."""
    pg = pris_prior(profiler, "xg90")
    pa = pris_prior(profiler, "xa90")
    for p in profiler.values():
        p.xg90_prior = max(0.0, pg[p.pos][0] + pg[p.pos][1] * p.startpris)
        p.xa90_prior = max(0.0, pa[p.pos][0] + pa[p.pos][1] * p.startpris)
        if k <= 0:
            continue
        p.xg90 = (p.nevner * p.xg90 + k * p.xg90_prior) / (p.nevner + k)
        p.xa90 = (p.nevner * p.xa90 + k * p.xa90_prior) / (p.nevner + k)
        p.xg90_robust = (p.nevner_robust * p.xg90_robust + k * p.xg90_prior) / (p.nevner_robust + k)
        p.xa90_robust = (p.nevner_robust * p.xa90_robust + k * p.xa90_prior) / (p.nevner_robust + k)


def sesong_aar(data: Data) -> int:
    return dt.datetime.fromisoformat(data.events[0]["deadline_time"].replace("Z", "+00:00")).year


def horisont(data: Data, fra: int | None, antall: int, naa: dt.datetime) -> list[int]:
    if fra is None:
        fremtid = [e["id"] for e in data.events
                   if dt.datetime.fromisoformat(e["deadline_time"].replace("Z", "+00:00")) > naa]
        if not fremtid:
            raise ValueError("ingen runder med deadline i framtiden")
        fra = min(fremtid)
    ider = {e["id"] for e in data.events}
    return [n for n in range(fra, fra + antall) if n in ider]


def projiser(m: Modell, eid: int, runder: list[int], fravaer: dict[int, Fravaer]) -> dict:
    """Forventede poeng per runde (sum over lagets kamper i runden) og per komponent."""
    p = m.profiler[eid]
    sjanse_runde = next((e["id"] for e in m.data.events if e.get("is_next")), None)
    aar = sesong_aar(m.data)
    ut = {"runder": {}, "robust": {}, "komp": collections.Counter(), "merknader": []}
    if sjanse_runde is not None and runder and sjanse_runde < runder[0]:
        # Speilet ble hentet før forrige deadline: FPL-sjansen gjelder en runde som er låst.
        # Den er likevel det ferskeste vi har, og brukes for første runde i horisonten.
        if p.sjanse_neste is not None and p.sjanse_neste < 100:
            ut["merknader"].append(f"FPL-sjansen gjelder GW{sjanse_runde}; brukt for GW{runder[0]}")
        sjanse_runde = runder[0]
    for n in runder:
        kamper = [f for f in kamper_i_runde(m.data, n) if p.lag in (f["team_h"], f["team_a"])]
        tot, tot_r = 0.0, 0.0
        for f in kamper:
            mot, bane = (f["team_a"], "H") if f["team_h"] == p.lag else (f["team_h"], "B")
            dato = (dt.datetime.fromisoformat(f["kickoff_time"].replace("Z", "+00:00")).date()
                    if f.get("kickoff_time") else dt.date.max)
            a, grunn = tilgjengelighet(p, n, dato, sjanse_runde, fravaer, aar)
            if grunn and a < 1:
                ut["merknader"].append(f"GW{n}: {grunn}")
            elif grunn and "tolket" in grunn:
                ut["merknader"].append(f"GW{n}: {grunn}")
            k = forvent_kamp(p, m.styrke, m.liga, mot, bane, a)
            kr = forvent_kamp(p, m.styrke, m.liga, mot, bane, a, robust=True)
            tot += k["total"]
            tot_r += kr["total"]
            for c in KOMPONENTER:
                ut["komp"][c] += k[c]
        if len(kamper) == 0:
            ut["merknader"].append(f"GW{n}: ingen kamp (blank runde)")
        elif len(kamper) > 1:
            ut["merknader"].append(f"GW{n}: {len(kamper)} kamper (dobbelrunde)")
        ut["runder"][n] = tot
        ut["robust"][n] = tot_r
    ut["merknader"] = list(dict.fromkeys(ut["merknader"]))
    return ut


# --------------------------------------------------------------------------- kontroller


def kontroller(data: Data, fravaer_feil: list[str], naa: dt.datetime) -> tuple[list[str], list[str], list[str]]:
    """Returnerer (feil, advarsler, ok-linjer). Feil stopper kjøringen."""
    feil = list(fravaer_feil)
    adv: list[str] = []
    ok: list[str] = []

    # 1. poengreglene i API-et mot konstantene her
    avvik = []
    for nokkel, verdi in POENG.items():
        api = data.poengregler.get(nokkel)
        if api != verdi:
            avvik.append(f"{nokkel}: API {api} ≠ skript {verdi}")
    if avvik:
        feil.append("poengreglene i API-et avviker fra skriptet: " + "; ".join(avvik))
    else:
        ok.append(f"Poengregler: alle {len(POENG)} kategorier i API-ets game_config stemmer med skriptet")

    # 2. live-filene summert mot sesongtotalene i bootstrap
    ferdige = [e["id"] for e in data.events if e.get("finished")]
    if data.utelatte_runder:
        adv.append("ferdige runder uten data_checked er holdt utenfor grunnlaget: GW"
                   + ", GW".join(map(str, data.utelatte_runder)))
    if sorted(ferdige) == data.grunnlag:
        avvik_n = collections.Counter()
        eksempler: list[str] = []
        for eid, el in data.elementer.items():
            for felt in SUMMEFELT_HEL + SUMMEFELT_DESIMAL:
                s = sum(float(data.live[n][eid]["stats"][felt]) for n in data.grunnlag if eid in data.live[n])
                tol = 0.06 if felt in SUMMEFELT_DESIMAL else 1e-9
                if abs(float(el[felt]) - s) > tol:
                    avvik_n[felt] += 1
                    if len(eksempler) < 5:
                        eksempler.append(f"{el['web_name']} {felt}: sesong {el[felt]}, runder {s:g}")
        if avvik_n:
            feil.append(f"rundedata summerer ikke til sesongtotalene ({dict(avvik_n)}): " + "; ".join(eksempler))
        else:
            ok.append(f"Rundedata GW{data.grunnlag[0]}–{data.grunnlag[-1]} summerer til sesongtotalene for "
                      f"alle {len(data.elementer)} spillere, {len(SUMMEFELT_HEL) + len(SUMMEFELT_DESIMAL)} felt")
    else:
        adv.append("summekontrollen er hoppet over fordi grunnlaget ikke er alle ferdige runder")

    # 3. speilets alder
    if data.snapshot and data.snapshot.get("fetched_at"):
        hentet = dt.datetime.fromisoformat(data.snapshot["fetched_at"])
        alder = (naa - hentet).total_seconds() / 3600
        linje = f"Speilet hentet {hentet:%d.%m.%Y %H:%M} UTC, {alder:.1f} t gammelt ved kjøring"
        (adv if alder > 26 else ok).append(linje + (" — eldre enn 26 t" if alder > 26 else ""))
    else:
        adv.append("snapshot.json mangler — speilets alder er ukjent")

    # 4. blank- og dobbelrunder, utsatte kamper
    per = collections.Counter()
    for f in data.kamper.values():
        if f.get("event"):
            per[(f["event"], f["team_h"])] += 1
            per[(f["event"], f["team_a"])] += 1
    dobbel = sorted({n for (n, _), c in per.items() if c > 1})
    if dobbel:
        adv.append("dobbelrunder i programmet: GW" + ", GW".join(map(str, dobbel)))
    alle_lag = set(data.lag)
    blank = sorted({n for n in {k[0] for k in per} if {t for (r, t) in per if r == n} != alle_lag})
    if blank:
        adv.append("blankrunder i programmet (minst ett lag uten kamp): GW" + ", GW".join(map(str, blank)))
    utsatt = [f for f in data.kamper.values() if not f.get("event")]
    if utsatt:
        adv.append(f"{len(utsatt)} kamp(er) uten runde (utsatt) — ikke med i horisonten")
    return feil, adv, ok


# --------------------------------------------------------------------------- tilbaketest


def gammel_modell(p: Profil, rader: list[Spillerrunde]) -> float:
    """Håndmodellen fra GW7-økten, gjenskapt fra utfallene (maks avvik 0,005 på ni spillere).
    Brukes bare som sammenligning i tilbaketesten."""
    spilt = [r for r in rader if r.minutter > 0]
    m = sum(r.minutter for r in spilt)
    if m == 0 or not rader:
        return 0.0
    f = 90 / m
    xg = sum(r.xg for r in spilt) * f
    xa = sum(r.xa for r in spilt) * f
    # on-pitch xGC er ikke i Spillerrunde; tilbaketesten fyller inn via attributt
    xgc = getattr(p, "_xgc90", 0.0)
    dc = sum(r.dc for r in spilt) * f
    pos = p.pos
    base = (2 + xg * POENG["goals_scored"][pos] + xa * 3 + math.exp(-xgc) * POENG["clean_sheets"][pos]
            - (xgc / 2 if pos in ("DEF", "GKP") else 0))
    t = DC_TERSKEL[pos]
    dcledd = 2 * min(1.0, (dc / t) ** 3) if t else 0.0
    return (base + dcledd) * m / (90 * len(rader))


def tilbaketest(kilde: Kilde, fravaer: dict[int, dict[int, Fravaer]], noytral: bool = False,
                prior: dict[int, tuple[float, float]] | None = None, fra_runde: int = 4,
                horisont: int = 1, spiller_k: float | None = None, til_runde: int | None = None) -> list[str]:
    full = last_data(kilde)
    L = [f"## Tilbaketest, {horisont} runde{'r' if horisont > 1 else ''} fram", "",
         "Modellen bygges på rundene før målrunden og spår "
         + ("målrunden" if horisont == 1 else f"summen for målrunden og de {horisont - 1} neste")
         + " for alle spillere med minst én start i grunnlaget. Tilgjengelighet settes til 100 % for alle "
         "(historisk status finnes ikke i speilet), så skadde spillere trekker snittet av faktiske poeng ned "
         "for alle metodene likt. «PPG» = poeng per telte kamp i grunnlaget × antall kamper. "
         "«Gammel» = håndmodellen fra GW7-økten × antall kamper.", "",
         "| Målrunde | Spillere | Snitt faktisk | Snitt ny | Snitt gammel | MAE ny | MAE PPG | MAE gammel "
         "| r ny | r PPG | r gammel | ρ ny | ρ PPG | ρ gammel |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    samlet = collections.defaultdict(list)
    per_pos = collections.defaultdict(lambda: collections.defaultdict(list))
    for maal in full.grunnlag:
        if maal < fra_runde or (til_runde is not None and maal > til_runde):
            continue
        d = last_data(kilde, til_runde=maal)
        m = bygg_modell(d, fravaer, noytral=noytral, prior=prior, spiller_k=spiller_k)
        maalrunder = [n for n in range(maal, maal + horisont) if n in full.grunnlag]
        if len(maalrunder) < horisont:
            continue
        faktisk_runder = {n: {x["id"]: x for x in kilde.json(f"live/gw{n}.json")["elements"]} for n in maalrunder}
        kamper = [f for f in full.kamper.values() if f.get("event") in maalrunder]
        xgc90 = {}
        for eid in d.elementer:
            mins = sum(d.live[n][eid]["stats"]["minutes"] for n in d.grunnlag if eid in d.live[n])
            xgc = sum(float(d.live[n][eid]["stats"]["expected_goals_conceded"]) for n in d.grunnlag if eid in d.live[n])
            xgc90[eid] = xgc / mins * 90 if mins else 0.0
        ny, rob, ppg, gml, fak = [], [], [], [], []
        for eid, p in m.profiler.items():
            if p.starter == 0 or eid not in faktisk_runder[maal]:
                continue
            lag = p.lag
            mine = [f for f in kamper if lag in (f["team_h"], f["team_a"])]
            if not mine:
                continue
            x, xr = 0.0, 0.0
            for f in mine:
                mot, bane = (f["team_a"], "H") if f["team_h"] == lag else (f["team_h"], "B")
                x += forvent_kamp(p, m.styrke, m.liga, mot, bane, 1.0)["total"]
                xr += forvent_kamp(p, m.styrke, m.liga, mot, bane, 1.0, robust=True)["total"]
            p._xgc90 = xgc90[eid]  # type: ignore[attr-defined]
            ny.append(x)
            rob.append(xr)
            ppg.append(len(mine) * (sum(r.poeng for r in m.rader[eid]) / p.telte if p.telte else 0.0))
            gml.append(len(mine) * gammel_modell(p, m.rader[eid]))
            fak.append(float(sum(faktisk_runder[n][eid]["stats"]["total_points"]
                                 for n in maalrunder if eid in faktisk_runder[n])))
            per_pos[p.pos]["ny"].append(x)
            per_pos[p.pos]["fak"].append(fak[-1])
        for navn, v in (("ny", ny), ("rob", rob), ("ppg", ppg), ("gml", gml), ("fak", fak)):
            samlet[navn].extend(v)

        def mae(a: list[float]) -> float:
            return sum(abs(u - v) for u, v in zip(a, fak)) / len(fak)

        L.append(f"| GW{maal} | {len(fak)} | {sum(fak)/len(fak):.2f} | {sum(ny)/len(ny):.2f} | {sum(gml)/len(gml):.2f} "
                 f"| {mae(ny):.2f} | {mae(ppg):.2f} | {mae(gml):.2f} "
                 f"| {pearson(ny, fak):.3f} | {pearson(ppg, fak):.3f} | {pearson(gml, fak):.3f} "
                 f"| {spearman(ny, fak):.3f} | {spearman(ppg, fak):.3f} | {spearman(gml, fak):.3f} |")
    if samlet["fak"]:
        f = samlet["fak"]

        def mae2(a: list[float]) -> float:
            return sum(abs(u - v) for u, v in zip(a, f)) / len(f)

        L.append(f"| **Samlet** | {len(f)} | {sum(f)/len(f):.2f} | {sum(samlet['ny'])/len(f):.2f} "
                 f"| {sum(samlet['gml'])/len(f):.2f} | {mae2(samlet['ny']):.2f} | {mae2(samlet['ppg']):.2f} "
                 f"| {mae2(samlet['gml']):.2f} | {pearson(samlet['ny'], f):.3f} | {pearson(samlet['ppg'], f):.3f} "
                 f"| {pearson(samlet['gml'], f):.3f} | {spearman(samlet['ny'], f):.3f} "
                 f"| {spearman(samlet['ppg'], f):.3f} | {spearman(samlet['gml'], f):.3f} |")
        L += ["", f"Robust variant (uten spillerens beste xGI-kamp), samlet: snitt {sum(samlet['rob'])/len(f):.2f}, "
              f"MAE {mae2(samlet['rob']):.2f}, r {pearson(samlet['rob'], f):.3f}, ρ {spearman(samlet['rob'], f):.3f}."]
        L += ["", "**Kalibrering per posisjon, ny modell (samlet):**", "",
              "| Posisjon | Spillere | Snitt forventet | Snitt faktisk |", "|---|---|---|---|"]
        for pos in POSISJONER:
            v = per_pos[pos]
            if v["fak"]:
                L.append(f"| {pos} | {len(v['fak'])} | {sum(v['ny'])/len(v['ny']):.2f} | {sum(v['fak'])/len(v['fak']):.2f} |")
    L.append("")
    return L


# --------------------------------------------------------------------------- utskrift


def kort_lag(data: Data, lag: int) -> str:
    return data.lag[lag]["short_name"] if lag in data.lag else str(lag)


def rad_for(m: Modell, eid: int, runder: list[int], fravaer: dict[int, dict[int, Fravaer]]) -> dict:
    p = m.profiler[eid]
    pr = projiser(m, eid, runder, fravaer.get(eid, {}))
    sum_x = sum(pr["runder"].values())
    sum_r = sum(pr["robust"].values())
    rad = {
        "id": eid, "navn": p.navn, "lag": kort_lag(m.data, p.lag), "pos": p.pos, "pris": f"{p.pris:.1f}",
        "status": p.status, "sjanse_neste": "" if p.sjanse_neste is None else p.sjanse_neste,
        "straffe": "" if p.straffe is None else p.straffe,
    }
    for n in runder:
        rad[f"xp_gw{n}"] = round(pr["runder"][n], 2)
    rad.update({
        "xp_sum": round(sum_x, 2), "xp_sum_robust": round(sum_r, 2),
        "xp_per_mill": round(sum_x / p.pris, 3) if p.pris else 0,
    })
    for c in KOMPONENTER:
        rad[f"k_{c}"] = round(pr["komp"][c], 2)
    rad.update({
        "xgi90_raa": round(p.xgi90_raa, 2), "xgi90_uten_beste": round(p.xgi90_uten_beste, 2),
        "andel_beste_kamp": round(p.andel_beste, 2), "xg90_just": round(p.xg90, 3), "xa90_just": round(p.xa90, 3),
        "xg90_prior": round(p.xg90_prior, 3), "xa90_prior": round(p.xa90_prior, 3),
        "redn90_just": round(p.redn90, 2), "minutter": p.minutter, "telte_kamper": p.telte, "starter": p.starter,
        "innbytter": p.innbytter, "startandel": round(p.startandel, 2),
        "start_siste3": "" if p.start_siste3 is None else round(p.start_siste3, 2),
        "min_per_start": round(p.min_start, 1), "p60_start": round(p.p60_start, 2),
        "dc_treff_start": p.dc_grunnlag, "bonus_avvik": round(p.bonus_avvik, 3),
        "poeng_sesong": p.poeng_sesong, "poeng_uten_beste": p.poeng_uten_beste,
        "fravaer_uavklart": " ".join(f"GW{n}" for n in p.fravaer_uavklart),
        "fravaer_utelatt": " ".join(f"GW{n}" for n in p.fravaer_utelatt),
        "flagg": " | ".join(p.flagg + pr["merknader"]),
    })
    return rad


def fmt(v) -> str:
    return f"{v:.2f}" if isinstance(v, float) else str(v)


def markdown(m: Modell, runder: list[int], rader: dict[int, dict], feil: list[str], adv: list[str],
             ok: list[str], ekstra: list[int], fravaer_kilde: str, tilbake: list[str] | None,
             naa: dt.datetime) -> str:
    d = m.data
    s = m.styrke
    L = ["# Forventede poeng — generert", "",
         f"*Generert {naa:%d.%m.%Y kl. %H:%M} UTC av `scripts/forventning.py` fra `fpl-data`. "
         f"**Rør ikke fila for hånd.** Grunnlag: GW{d.grunnlag[0]}–{d.grunnlag[-1]} (data_checked). "
         f"Horisont: GW{runder[0]}–{runder[-1]}"
         + (" — **fiksturnøytral**" if s.noytral else "") + f". Fraværsfil: {fravaer_kilde}.*", ""]
    L += ["## Kontroller", ""]
    for x in feil:
        L.append(f"- ❌ {x}")
    for x in ok:
        L.append(f"- ✅ {x}")
    for x in adv:
        L.append(f"- ⚠️ {x}")
    if m.uloste_lag:
        L.append(f"- ⚠️ {len(m.uloste_lag)} spiller-runder uten løst lag: {', '.join(m.uloste_lag[:10])}")
    L.append("")

    L += ["## Modell og estimerte parametre", "",
          "Formelen står i toppen av `scripts/forventning.py`.", "",
          f"- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel "
          f"{AVTAK}, krymping av spillerrater mot posisjon og startpris {SPILLER_K:g} kamper, krymping av "
          f"DC-treffrate mot posisjonssnitt {DC_K:g} kamper, CS-faktor {CS_FAKTOR}, målfaktor "
          + ", ".join(f"{p} {MAL_FAKTOR[p]}" for p in POSISJONER) + "; assistfaktor "
          + ", ".join(f"{p} {ASSIST_FAKTOR[p]}" for p in POSISJONER) + ".",
          "- **Estimert fra sesongens data ved hver kjøring:**",
          f"  - Liga-xG per lag og kamp μ = {s.mu:.3f}. Bane: hjemme ×{s.bane_angrep['H']:.3f}, borte ×{s.bane_angrep['B']:.3f}.",
          f"  - Lagstyrke krympet mot forrige sesong (dempet med ρ = {LAG_RHO}) med k = {s.kA:.0f} kamper "
          f"(angrep) og {s.kD:.0f} (forsvar).",
          f"  - Bonus: k = {m.liga.bonus_k:.1f} kamper for spillerens eget avvik. Koeffisienter per posisjon "
          "(konstant, så felt i rekkefølge):"]
    for pos in POSISJONER:
        felt = ", ".join(f"{f} {b:+.3f}" for f, b in zip(m.liga.bonus_felt[pos], m.liga.bonus_beta[pos][1:]))
        L.append(f"    - {pos} (n = {m.liga.bonus_n[pos]}): konstant {m.liga.bonus_beta[pos][0]:+.3f}; {felt}")
        negative = [f for f, b in zip(m.liga.bonus_felt[pos], m.liga.bonus_beta[pos][1:])
                    if f in ("mal", "assist", "cs", "redninger") and b < 0]
        if negative:
            L.append(f"    - ⚠️ {pos}: negativ koeffisient for {', '.join(negative)} — bonusmodellen er ikke troverdig her")
    L.append(f"  - Gule kort krympes med k = {m.liga.gule_k:.1f} kamper mot posisjonssnitt. "
             f"Strafferedninger per keeper-90: {m.liga.straffe_redd90:.3f}.")
    L += ["", "**Begrensninger:**", ""] + [f"- {b}" for b in BEGRENSNINGER] + [""]

    lagrangering = sorted(s.A, key=lambda t: -s.A[t])
    L += ["### Lagstyrke (1,00 = snitt)", "", "| Lag | Angrep A | Forsvar D (lavere er bedre) |", "|---|---|---|"]
    for t in lagrangering:
        L.append(f"| {kort_lag(d, t)} | {s.A[t]:.2f} | {s.D[t]:.2f} |")
    L.append("")

    kol = " | ".join(f"GW{n}" for n in runder)
    hode = f"| Spiller | Lag | Pos | Pris | {kol} | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |"
    skille = "|" + "---|" * (len(runder) + 12)

    i_tropp = set(d.tropp)

    def tabellrad(eid: int) -> str:
        r = rader[eid]
        gw = " | ".join(fmt(r[f"xp_gw{n}"]) for n in runder)
        navn = f"{r['navn']} ★" if eid in i_tropp else r["navn"]
        return (f"| {navn} | {r['lag']} | {r['pos']} | {r['pris']} | {gw} | **{fmt(r['xp_sum'])}** "
                f"| {fmt(r['xp_sum_robust'])} | {fmt(r['xgi90_raa'])} | {fmt(r['xgi90_uten_beste'])} "
                f"| {fmt(r['startandel'])} | {r['dc_treff_start']} | {r['straffe']} | {r['flagg'] or '—'} |")

    if d.tropp:
        L += [f"## Troppen (picks GW{d.tropp_runde})", "",
              f"Bytter gjort etter GW{d.tropp_runde}-deadline vises ikke.", "", hode, skille]
        for eid in sorted(d.tropp, key=lambda e: (POSISJONER.index(rader[e]["pos"]), -rader[e]["xp_sum"])):
            L.append(tabellrad(eid))
        L.append("")
    if ekstra:
        L += ["## Valgte spillere", "", hode, skille]
        for eid in ekstra:
            if eid in rader:
                L.append(tabellrad(eid))
        L.append("")

    L += ["## Beste per posisjon (sum over horisonten)", "",
          "Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er "
          "samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk "
          "begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.", ""]
    for pos, antall in (("GKP", 8), ("DEF", 15), ("MID", 15), ("FWD", 10)):
        kandidater = [e for e, r in rader.items() if r["pos"] == pos and r["status"] != "u" and r["minutter"] >= 180]
        kandidater.sort(key=lambda e: -rader[e]["xp_sum"])
        L += [f"### {pos}", "", hode, skille]
        for eid in kandidater[:antall]:
            L.append(tabellrad(eid))
        L.append("")

    uavklart = [(rader[e]["navn"], rader[e]["lag"], rader[e]["fravaer_uavklart"])
                for e in (list(d.tropp) + ekstra) if e in rader and rader[e]["fravaer_uavklart"]]
    L += ["## Uavklart fravær i troppen og valgte spillere", ""]
    if uavklart:
        L += ["Telles som ikke-start til årsaken er ført i `context/fravaer.csv`. Slå opp årsaken — ikke gjett.", "",
              "| Spiller | Lag | Runder |", "|---|---|---|"]
        L += [f"| {n} | {l} | {r} |" for n, l, r in uavklart]
    else:
        L.append("Ingen.")
    L.append("")
    if tilbake:
        L += tilbake
    return "\n".join(L) + "\n"


def csv_tekst(rader: dict[int, dict]) -> str:
    alle = sorted(rader.values(), key=lambda r: (-r["xp_sum"], r["id"]))
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(alle[0].keys()), lineterminator="\n")
    w.writeheader()
    w.writerows(alle)
    return buf.getvalue()


def uten_tidsstempel(tekst: str) -> str:
    return "\n".join(l for l in tekst.splitlines() if not l.startswith("*Generert ") and "t gammelt ved kjøring" not in l)


# --------------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--stdout", action="store_true", help="markdown til stdout, skriv ingenting")
    ap.add_argument("--check", action="store_true", help="bare kontrollene, exit 1 ved feil")
    ap.add_argument("--runder", type=int, default=5, help="antall runder i horisonten (standard 5)")
    ap.add_argument("--fra-runde", type=int, help="første runde i horisonten")
    ap.add_argument("--spillere", default="", help="kommaseparerte element-id-er å vise i tillegg")
    ap.add_argument("--uten-fikstur", action="store_true", help="alle motstandere og baner = snitt")
    ap.add_argument("--tilbaketest", action="store_true", help="kjør tilbaketest og ta den med i rapporten")
    ap.add_argument("--kilde", type=pathlib.Path, help="mappe med speilets data/-struktur")
    ap.add_argument("--fravaer", type=pathlib.Path, default=FRAVAER_FIL, help="fraværsfil (csv)")
    ap.add_argument("--prior", type=pathlib.Path, default=PRIOR_FIL, help="forrige sesongs lagstyrke (csv)")
    ap.add_argument("--ut-md", type=pathlib.Path, default=UT_MD)
    ap.add_argument("--ut-csv", type=pathlib.Path, default=UT_CSV)
    a = ap.parse_args(argv)

    naa = dt.datetime.now(dt.timezone.utc)
    kilde = Kilde(a.kilde)
    data = last_data(kilde)
    if not data.grunnlag:
        print("ingen ferdige, låste runder i speilet — ingenting å bygge på", file=sys.stderr)
        return 1
    fr_tekst, fr_kilde = hent_repofil(a.fravaer)
    fravaer, fr_feil = les_fravaer(fr_tekst, data.elementer)
    pr_tekst, pr_kilde = hent_repofil(a.prior)
    prior, opprykk, pr_feil = les_prior(pr_tekst, data.lag)
    feil, adv, ok = kontroller(data, fr_feil + (pr_feil if pr_tekst else []), naa)
    if fr_tekst is None:
        adv.append(f"fant ikke fraværsfila ({a.fravaer}) — alle fravær står som uavklart")
    if pr_tekst is None:
        adv.append(f"fant ikke lagstyrke-prior ({a.prior}) — lagstyrke krympes mot 1,0")
    else:
        ok.append(f"Lagstyrke-prior fra {pr_kilde} (ρ = {LAG_RHO}); opprykksprior brukt for "
                  + (", ".join(opprykk) if opprykk else "ingen"))

    if a.check or feil:
        for x in feil:
            print(f"FEIL: {x}", file=sys.stderr)
        for x in adv:
            print(f"ADVARSEL: {x}", file=sys.stderr)
        for x in ok:
            print(f"OK: {x}", file=sys.stderr)
        if feil:
            return 1
        if a.check:
            return 0

    m = bygg_modell(data, fravaer, noytral=a.uten_fikstur, prior=prior)
    try:
        runder = horisont(data, a.fra_runde, a.runder, naa)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1
    ekstra = [int(x) for x in a.spillere.split(",") if x.strip()]
    rader = {eid: rad_for(m, eid, runder, fravaer) for eid in data.elementer}
    tilbake = tilbaketest(kilde, fravaer, noytral=a.uten_fikstur, prior=prior) if a.tilbaketest else None
    md = markdown(m, runder, rader, feil, adv, ok, ekstra, fr_kilde, tilbake, naa)

    if a.stdout:
        print(md)
        return 0
    ny_csv = csv_tekst(rader)
    gammel_md = a.ut_md.read_text(encoding="utf-8") if a.ut_md.exists() else ""
    gammel_csv = a.ut_csv.read_text(encoding="utf-8") if a.ut_csv.exists() else ""
    # Tidsstempel og speilets alder endres hver kjøring. Uten denne sammenligningen ville
    # CI committe hver gang selv når ingen tall har endret seg.
    if uten_tidsstempel(gammel_md) == uten_tidsstempel(md) and gammel_csv == ny_csv:
        print(f"{a.ut_md} og {a.ut_csv} uendret")
        return 0
    a.ut_md.parent.mkdir(parents=True, exist_ok=True)
    a.ut_csv.parent.mkdir(parents=True, exist_ok=True)
    a.ut_md.write_text(md, encoding="utf-8")
    a.ut_csv.write_text(ny_csv, encoding="utf-8")
    print(f"{a.ut_md} og {a.ut_csv} oppdatert")
    return 0


if __name__ == "__main__":
    sys.exit(main())
