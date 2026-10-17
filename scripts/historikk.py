#!/usr/bin/env python3
"""Tidligere sesonger: lagstyrke-prior, kryssvalidering og tilbaketest for forventning.py.

Kjøres for hånd, ikke i CI. Henter ferdige sesonger fra vaastav/Fantasy-Premier-League
på GitHub — et tredjepartsspeil av det offisielle FPL-API-et. Bare avsluttede sesonger
brukes, så tallene endrer seg ikke. Kun stdlib.

Bruk (fra reporoten):
    python3 scripts/historikk.py prior                 # skriv context/lagstyrke-prior.csv
    python3 scripts/historikk.py kryssvalider          # velg k og ρ for lagstyrken på nytt
    python3 scripts/historikk.py kalibrer              # mål/xG, assist/xA og CS-faktor på nytt
    python3 scripts/historikk.py tilbaketest           # hele forventningsmodellen på 2025/26
    python3 scripts/historikk.py tilbaketest --sesong 2024-25 --faktorer-fra 2025-26
                                                       # utenfor utvalget: ingen parameter valgt på 2024/25

prior:        context/lagstyrke-prior.csv: rå lagstyrke for forrige hele sesong (A, D uten
              krymping) per kortnavn, og raden OPPRYKK = snittet for lagene som rykket opp den
              sesongen. forventning.py demper verdiene med LAG_RHO og krymper mot dem.
kryssvalider: for hver sesong i VALIDERING tilpasses lagstyrken på GW1..g og spår lag-xG i
              GW g+1..g+5, g = 1..33. Rutenett over ρ, kA og kD. Skriver MSE-tabellen.
tilbaketest:  bygger en speilkopi (samme filformat som fpl-data) av en hel sesong og kjører
              forventning.tilbaketest() med prior fra sesongen før. Tilgjengelighet = 100 %.
"""

from __future__ import annotations

import argparse
import collections
import csv
import io
import itertools
import json
import math
import pathlib
import sys
import tempfile
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import forventning as fv  # noqa: E402

VAASTAV = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data"
POSISJON = {"GK": 1, "GKP": 1, "DEF": 2, "MID": 3, "FWD": 4}
# Sesongene som brukes. Endres når 2026/27 er ferdig spilt.
SISTE = "2025-26"
FORRIGE = "2024-25"
FORFORRIGE = "2023-24"
VALIDERING = [("2025-26", "2024-25", "2023-24"), ("2024-25", "2023-24", "2022-23")]


def hent(sti: str) -> str:
    req = urllib.request.Request(f"{VAASTAV}/{sti}", headers={"User-Agent": "fpl2627-historikk"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8")


def les_csv(sti: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(hent(sti))))


def forrige_navn(navn: str) -> str:
    """«2025-26» -> «2024-25»."""
    aar = int(navn[:4]) - 1
    return f"{aar}-{str(aar + 1)[2:]}"


def heltall(r: dict, felt: str) -> int:
    """Kolonner som ikke fantes i eldre sesonger (defensive_contribution før 2025/26) leses som 0.
    Det stemmer med fasit: DC ga ikke poeng før 2025/26."""
    v = r.get(felt)
    return int(v) if v not in (None, "") else 0


class Sesong:
    def __init__(self, navn: str, med_kamper: bool = True):
        self.navn = navn
        self.lag = {int(t["id"]): t for t in les_csv(f"{navn}/teams.csv")}
        self.kortnavn = {tid: t["short_name"] for tid, t in self.lag.items()}
        if not med_kamper:
            return
        # «AM» (assistant manager i 2024/25) er ikke en spiller og holdes utenfor.
        self.rader = [r for r in les_csv(f"{navn}/gws/merged_gw.csv") if r["position"] in POSISJON]
        self.kamper = {int(f["id"]): f for f in les_csv(f"{navn}/fixtures.csv")}
        self.lag_xg: dict[tuple[int, int], float] = collections.defaultdict(float)
        for r in self.rader:
            f = self.kamper[int(r["fixture"])]
            lag = int(f["team_h"] if r["was_home"] == "True" else f["team_a"])
            self.lag_xg[(int(r["fixture"]), lag)] += float(r["expected_goals"])

    def ferdige(self) -> list[int]:
        return sorted(k for k, f in self.kamper.items() if f["finished"] == "True" and f["event"])

    def lagrader(self, kamper: list[int]) -> list[fv.Lagrad]:
        ut = []
        for k in kamper:
            f = self.kamper[k]
            h, b = int(f["team_h"]), int(f["team_a"])
            ut.append(fv.Lagrad(h, int(f["event"]), [(b, "H")], self.lag_xg[(k, h)], self.lag_xg[(k, b)], True))
            ut.append(fv.Lagrad(b, int(f["event"]), [(h, "B")], self.lag_xg[(k, b)], self.lag_xg[(k, h)], True))
        return ut


def prior_for_sesong(s: Sesong, rho: float) -> dict[int, tuple[float, float]]:
    """Lagstyrke-prior for sesong s, bygget på sesongen før (og opprykkssnittet fra den)."""
    forrige = forrige_navn(s.navn)
    tabell = prior_tabell(Sesong(forrige), set(Sesong(forrige_navn(forrige), med_kamper=False).kortnavn.values()))
    return prior_per_lagid(tabell, s.kortnavn, rho)


def raa_styrke(s: Sesong) -> dict[str, tuple[float, float]]:
    st = fv.tilpass_lagstyrke(s.lagrader(s.ferdige()), kA=0.0, kD=0.0)
    return {s.kortnavn[t]: (st.A[t], st.D[t]) for t in st.A}


def prior_tabell(sesong: Sesong, forrige_lag: set[str]) -> dict[str, tuple[float, float]]:
    """Rå styrke per kortnavn + OPPRYKK (snitt for lagene som ikke var med sesongen før)."""
    styrke = raa_styrke(sesong)
    opp = [k for k in styrke if k not in forrige_lag]
    if not opp:
        raise ValueError(f"fant ingen opprykkslag i {sesong.navn}")
    styrke["OPPRYKK"] = (sum(styrke[k][0] for k in opp) / len(opp), sum(styrke[k][1] for k in opp) / len(opp))
    return styrke


def prior_per_lagid(tabell: dict[str, tuple[float, float]], kortnavn: dict[int, str], rho: float) -> dict[int, tuple[float, float]]:
    return {tid: (1 + rho * (tabell.get(k, tabell["OPPRYKK"])[0] - 1),
                  1 + rho * (tabell.get(k, tabell["OPPRYKK"])[1] - 1)) for tid, k in kortnavn.items()}


# --------------------------------------------------------------------------- prior


def kommando_prior(ut: pathlib.Path) -> int:
    s = Sesong(SISTE)
    forrige = set(Sesong(FORRIGE, med_kamper=False).kortnavn.values())
    tabell = prior_tabell(s, forrige)
    opp = sorted(k for k in tabell if k != "OPPRYKK" and k not in forrige)
    ut.parent.mkdir(parents=True, exist_ok=True)
    with ut.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["lag", "A", "D", "grunnlag"])
        for k in sorted(tabell, key=lambda x: (x == "OPPRYKK", x)):
            a, d = tabell[k]
            grunn = (f"snitt for opprykkslagene {', '.join(opp)} i {SISTE}" if k == "OPPRYKK"
                     else f"{SISTE}, {len(s.ferdige())} kamper, rå xG-styrke uten krymping")
            w.writerow([k, f"{a:.4f}", f"{d:.4f}", grunn])
    print(f"{ut} skrevet: {len(tabell) - 1} lag + OPPRYKK ({', '.join(opp)})")
    return 0


# --------------------------------------------------------------------------- kryssvalidering


def mse(s: Sesong, prior: dict[int, tuple[float, float]], kA: float, kD: float, sjekk: range) -> float:
    alle = s.ferdige()
    se, n = 0.0, 0
    for g in sjekk:
        hist = [k for k in alle if int(s.kamper[k]["event"]) <= g]
        st = fv.tilpass_lagstyrke(s.lagrader(hist), kA=kA, kD=kD, prior=prior)
        for k in alle:
            if not g < int(s.kamper[k]["event"]) <= g + 5:
                continue
            f = s.kamper[k]
            h, b = int(f["team_h"]), int(f["team_a"])
            ph = st.mu * st.A[h] * st.D[b] * st.bane_angrep["H"]
            pb = st.mu * st.A[b] * st.D[h] * st.bane_angrep["B"]
            se += (ph - s.lag_xg[(k, h)]) ** 2 + (pb - s.lag_xg[(k, b)]) ** 2
            n += 2
    return se / n


def kommando_kryssvalider() -> int:
    rutenett = list(itertools.product([0.0, 0.25, 0.5, 0.75, 1.0], [4, 8, 15, 30], [8, 15, 30, 60]))
    for sesong, forrige, forforrige in VALIDERING:
        s = Sesong(sesong)
        tabell = prior_tabell(Sesong(forrige), set(Sesong(forforrige, med_kamper=False).kortnavn.values()))
        res: dict[tuple[float, int, int], float] = {}
        for rho, kA, kD in rutenett:
            res[(rho, kA, kD)] = mse(s, prior_per_lagid(tabell, s.kortnavn, rho), kA, kD, range(1, 34))
        beste = min(res, key=res.get)
        valgt = (fv.LAG_RHO, fv.LAG_KA, fv.LAG_KD)
        print(f"## {sesong} (prior fra {forrige})")
        print(f"beste (ρ, kA, kD) = {beste}: MSE {res[beste]:.4f}")
        print(f"valgt i forventning.py {valgt}: MSE {res.get(valgt, float('nan')):.4f}")
        print(f"uten prior, k = (8, 20): MSE {mse(s, {}, 8, 20, range(1, 34)):.4f}")
        print(f"uten krymping: MSE {mse(s, {}, 0, 0, range(1, 34)):.4f}")
        print()
    return 0


# --------------------------------------------------------------------------- kalibrering


def cs_faktor(s: Sesong, prior: dict[int, tuple[float, float]]) -> tuple[float, int, int]:
    """Faktor f slik at Σ exp(−f·λ) over alle lagkamper = antall clean sheets, der λ er
    lagstyrkemodellens spådde baklengs (tilpasset på rundene før kampen)."""
    alle = s.ferdige()
    lam, cs = [], 0
    for g in range(1, 38):
        st = fv.tilpass_lagstyrke(s.lagrader([k for k in alle if int(s.kamper[k]["event"]) <= g]),
                                  kA=fv.LAG_KA, kD=fv.LAG_KD, prior=prior)
        for k in alle:
            if int(s.kamper[k]["event"]) != g + 1:
                continue
            f = s.kamper[k]
            h, b = int(f["team_h"]), int(f["team_a"])
            lam.append(st.lam90(h, b, "H"))
            lam.append(st.lam90(b, h, "B"))
            cs += (int(f["team_a_score"]) == 0) + (int(f["team_h_score"]) == 0)
    lo, hi = 0.5, 2.5
    for _ in range(60):
        mid = (lo + hi) / 2
        if sum(math.exp(-mid * x) for x in lam) > cs:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2, len(lam), cs


def faktorer(sesonger: list[str]) -> tuple[dict[str, float], dict[str, float], float, list[str]]:
    """Mål/xG og assist/xA per posisjon og CS-faktoren, samlet over sesongene. Returnerer også
    linjer til utskrift."""
    mal, xg, ass, xa = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    fs, linjer = [], []
    for navn in sesonger:
        s = Sesong(navn)
        for r in s.rader:
            pos = fv.POS[POSISJON[r["position"]]]
            mal[pos] += int(r["goals_scored"])
            xg[pos] += float(r["expected_goals"])
            ass[pos] += int(r["assists"])
            xa[pos] += float(r["expected_assists"])
        f, n, cs = cs_faktor(s, prior_for_sesong(s, fv.LAG_RHO))
        fs.append((f, n))
        linjer.append(f"{navn}: CS-faktor {f:.3f} ({cs} clean sheets på {n} lagkamper)")
    alle_ass, alle_xa = sum(ass.values()), sum(xa.values())
    malf = {p: (mal[p] / xg[p] if p != "GKP" and xg[p] else 1.0) for p in fv.POSISJONER}
    assf = {p: (ass[p] / xa[p] if p != "GKP" else alle_ass / alle_xa) for p in fv.POSISJONER}
    for p in fv.POSISJONER:
        linjer.append(f"  {p}: mål/xG {malf[p]:.3f} (n {mal[p]}), assist/xA {assf[p]:.3f} "
                      f"(n {ass[p] if p != 'GKP' else alle_ass})")
    csf = sum(x * n for x, n in fs) / sum(n for _, n in fs)
    linjer.append(f"CS-faktor, vektet snitt: {csf:.3f}")
    return malf, assf, csf, linjer


def kommando_kalibrer(sesonger: list[str]) -> int:
    print(f"Kalibrering på {', '.join(sesonger)}:")
    for linje in faktorer(sesonger)[3]:
        print(linje)
    return 0


# --------------------------------------------------------------------------- tilbaketest


def skriv_speil(s: Sesong, mappe: pathlib.Path) -> None:
    """Skriver sesongen i fpl-data-format: bootstrap-static.json, fixtures.json, live/gwN.json."""
    per_runde: dict[int, dict[int, list[dict]]] = collections.defaultdict(lambda: collections.defaultdict(list))
    siste: dict[int, dict] = {}
    forste: dict[int, dict] = {}
    for r in s.rader:
        n, eid = int(r["GW"]), int(r["element"])
        per_runde[n][eid].append(r)
        if eid not in siste or int(siste[eid]["GW"]) <= n:
            siste[eid] = r
        if eid not in forste or int(forste[eid]["GW"]) > n:
            forste[eid] = r
    elementer = []
    for eid, r in siste.items():
        f = s.kamper[int(r["fixture"])]
        lag = int(f["team_h"] if r["was_home"] == "True" else f["team_a"])
        elementer.append({
            "id": eid, "web_name": r["name"], "team": lag, "element_type": POSISJON[r["position"]],
            "now_cost": int(r["value"]), "cost_change_start": int(r["value"]) - int(forste[eid]["value"]),
            "status": "a", "chance_of_playing_next_round": None,
            "news": "", "penalties_order": None,
        })
    runder = sorted(per_runde)
    events = []
    for n in runder:
        avspark = min(f["kickoff_time"] for f in s.kamper.values() if f["event"] and int(f["event"]) == n)
        events.append({"id": n, "finished": True, "data_checked": True, "is_next": False,
                       "is_current": n == runder[-1], "deadline_time": avspark})
    kamper = []
    side: dict[int, dict[str, list[dict]]] = collections.defaultdict(lambda: {"h": [], "a": []})
    for r in s.rader:
        side[int(r["fixture"])]["h" if r["was_home"] == "True" else "a"].append(
            {"element": int(r["element"]), "value": heltall(r, "bps")})
    for k, f in s.kamper.items():
        kamper.append({
            "id": k, "event": int(f["event"]) if f["event"] else None, "team_h": int(f["team_h"]),
            "team_a": int(f["team_a"]), "kickoff_time": f["kickoff_time"], "finished": f["finished"] == "True",
            "stats": [{"identifier": "bps", "h": side[k]["h"], "a": side[k]["a"]}],
        })
    lag = [{"id": tid, "name": t["name"], "short_name": t["short_name"]} for tid, t in s.lag.items()]
    bootstrap = {"elements": elementer, "teams": lag, "events": events,
                 "game_config": {"scoring": fv.POENG}}
    (mappe / "live").mkdir(parents=True, exist_ok=True)
    (mappe / "bootstrap-static.json").write_text(json.dumps(bootstrap), encoding="utf-8")
    (mappe / "fixtures.json").write_text(json.dumps(kamper), encoding="utf-8")
    hel = ["minutes", "goals_scored", "assists", "clean_sheets", "goals_conceded", "own_goals",
           "penalties_saved", "penalties_missed", "yellow_cards", "red_cards", "saves", "bonus", "bps",
           "starts", "defensive_contribution", "total_points"]
    des = ["expected_goals", "expected_assists", "expected_goals_conceded"]
    for n in runder:
        el = []
        for eid, rader in per_runde[n].items():
            stats = {f: sum(heltall(r, f) for r in rader) for f in hel}
            stats.update({f: f"{sum(float(r[f]) for r in rader):.2f}" for f in des})
            el.append({"id": eid, "stats": stats, "explain": [{"fixture": int(r["fixture"]), "stats": []} for r in rader]})
        (mappe / "live" / f"gw{n}.json").write_text(json.dumps({"elements": el}), encoding="utf-8")


def kommando_tilbaketest(sesong: str, fra: int, faktorer_fra: list[str] | None) -> int:
    """Tilbaketest på én hel sesong. Med faktorer_fra kalibreres mål-, assist- og CS-faktorene
    på andre sesonger enn den som testes, slik at testen er utenfor utvalget."""
    s = Sesong(sesong)
    prior = prior_for_sesong(s, fv.LAG_RHO)
    original = (dict(fv.MAL_FAKTOR), dict(fv.ASSIST_FAKTOR), fv.CS_FAKTOR)
    if faktorer_fra:
        malf, assf, csf, linjer = faktorer(faktorer_fra)
        fv.MAL_FAKTOR.update(malf)
        fv.ASSIST_FAKTOR.update(assf)
        fv.CS_FAKTOR = csf
    try:
        with tempfile.TemporaryDirectory() as tmp:
            mappe = pathlib.Path(tmp)
            skriv_speil(s, mappe)
            kilde = fv.Kilde(mappe)
            kal = f"kalibrert på {', '.join(faktorer_fra)}" if faktorer_fra else "faktorer fra forventning.py"
            print(f"# Tilbaketest {sesong} (prior fra {forrige_navn(sesong)}, {kal}), målrunder fra GW{fra}\n")
            for h in (1, 5):
                for linje in fv.tilbaketest(kilde, {}, prior=prior, fra_runde=fra, horisont=h):
                    print(linje)
            print("\n# Samme, uten fiksturjustering\n")
            for h in (1, 5):
                for linje in fv.tilbaketest(kilde, {}, noytral=True, prior=prior, fra_runde=fra, horisont=h):
                    print(linje)
    finally:
        fv.MAL_FAKTOR.clear()
        fv.MAL_FAKTOR.update(original[0])
        fv.ASSIST_FAKTOR.clear()
        fv.ASSIST_FAKTOR.update(original[1])
        fv.CS_FAKTOR = original[2]
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="kommando", required=True)
    p = sub.add_parser("prior")
    p.add_argument("--ut", type=pathlib.Path, default=fv.PRIOR_FIL)
    sub.add_parser("kryssvalider")
    k = sub.add_parser("kalibrer")
    k.add_argument("--sesonger", default=",".join(v[0] for v in VALIDERING))
    t = sub.add_parser("tilbaketest")
    t.add_argument("--sesong", default=SISTE)
    t.add_argument("--fra-runde", type=int, default=4)
    t.add_argument("--faktorer-fra", default="", help="kalibrer på disse sesongene (kommaseparert)")
    a = ap.parse_args()
    if a.kommando == "prior":
        return kommando_prior(a.ut)
    if a.kommando == "kryssvalider":
        return kommando_kryssvalider()
    if a.kommando == "kalibrer":
        return kommando_kalibrer([x for x in a.sesonger.split(",") if x])
    return kommando_tilbaketest(a.sesong, a.fra_runde, [x for x in a.faktorer_fra.split(",") if x] or None)


if __name__ == "__main__":
    sys.exit(main())
