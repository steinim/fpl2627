#!/usr/bin/env python3
"""Genererer kampprogramdelen av context/04-kampprogram-og-endringslogg.md.

Alt denne fila skriver er AVLEDET fra speilet i github.com/steinim/fpl-data:
kampdatoer, UK-klokkeslett, kamppar og hvilke av mine spillere som er i spill.
Ingenting her skal vedlikeholdes for hånd. Endringsloggen og
verifiseringsnotatene i 04 ligger utenfor markørene og røres ikke.

Kun stdlib — ingen pip install i CI.

Bruk:
    python3 scripts/gen_kampprogram.py                 # skriv 04 på plass
    python3 scripts/gen_kampprogram.py --check         # exit 1 ved strukturavvik, skriv ingenting
    python3 scripts/gen_kampprogram.py --stdout        # skriv blokka til stdout
    python3 scripts/gen_kampprogram.py --init          # legg inn markørene hvis de mangler
    python3 scripts/gen_kampprogram.py --runder 6      # antall runder framover (standard 5)
"""

from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import io
import json
import pathlib
import sys
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

MIRROR = "https://raw.githubusercontent.com/steinim/fpl-data/main/data"
UK = ZoneInfo("Europe/London")
START = "<!-- GENERERT:KAMPPROGRAM:START -->"
SLUTT = "<!-- GENERERT:KAMPPROGRAM:SLUTT -->"
MAALFIL = pathlib.Path("context/04-kampprogram-og-endringslogg.md")

DAG = {0: "man", 1: "tir", 2: "ons", 3: "tor", 4: "fre", 5: "lør", 6: "søn"}


# --------------------------------------------------------------------------- henting


def hent(sti: str) -> str:
    url = f"{MIRROR}/{sti}"
    req = urllib.request.Request(url, headers={"User-Agent": "fpl2627-gen"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def hent_csv(sti: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(hent(sti))))


def hent_csv_valgfri(sti: str) -> list[dict] | None:
    try:
        return hent_csv(sti)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def hent_json(sti: str):
    return json.loads(hent(sti))


# --------------------------------------------------------------------------- hjelpere


def uk(kickoff: str) -> dt.datetime:
    """UTC-streng fra APIet -> tidssonebevisst UK-tid. BST/GMT håndteres av zoneinfo."""
    return dt.datetime.fromisoformat(kickoff.replace("Z", "+00:00")).astimezone(UK)


def datostreng(d: dt.datetime) -> str:
    return f"{DAG[d.weekday()]} {d.day}.{d.month}."


# --------------------------------------------------------------------------- kontroller


def strukturkontroll(fixtures: list[dict], fixtures_json) -> tuple[list[str], dict]:
    """Returnerer (avvik, fakta). Tom avviksliste = programmet har normal form."""
    avvik: list[str] = []
    per_runde: dict[int, list[dict]] = collections.defaultdict(list)
    uten_runde = 0
    uten_kickoff = 0

    for f in fixtures:
        if not (f.get("event") or "").strip():
            uten_runde += 1
            continue
        if not (f.get("kickoff_time") or "").strip():
            uten_kickoff += 1
            continue
        per_runde[int(f["event"])].append(f)

    if uten_runde:
        avvik.append(f"{uten_runde} kamp(er) uten rundenummer — utsatt eller ikke omberammet")
    if uten_kickoff:
        avvik.append(f"{uten_kickoff} kamp(er) uten klokkeslett")

    alle_lag = {f["home"] for f in fixtures} | {f["away"] for f in fixtures}

    for runde in sorted(per_runde):
        rader = per_runde[runde]
        lag = [r["home"] for r in rader] + [r["away"] for r in rader]
        teller = collections.Counter(lag)

        dobbel = sorted(t for t, n in teller.items() if n > 1)
        if dobbel:
            avvik.append(f"GW{runde}: DOBBELRUNDE — {', '.join(dobbel)} har to kamper")

        blanke = sorted(alle_lag - set(lag))
        if blanke:
            avvik.append(f"GW{runde}: BLANKRUNDE — uten kamp: {', '.join(blanke)}")

        if len(rader) != 10:
            avvik.append(f"GW{runde}: {len(rader)} kamper, ikke 10")

    prov = [f for f in fixtures_json if f.get("provisional_start_time")]
    if prov:
        avvik.append(f"{len(prov)} kamp(er) med provisional_start_time=true — klokkeslett ikke endelig")

    # Speilet mot seg selv: csv og json skal være samme datasett.
    jm = {f["id"]: f for f in fixtures_json}
    for r in fixtures:
        j = jm.get(int(r["id"]))
        if j is None:
            avvik.append(f"kamp {r['id']} finnes i csv, ikke i json")
            continue
        if (j.get("kickoff_time") or "") != r["kickoff_time"]:
            avvik.append(f"kamp {r['id']}: kickoff avviker mellom csv og json")

    fakta = {
        "kamper": len(fixtures),
        "runder": len(per_runde),
        "lag": len(alle_lag),
        "provisional": len(prov),
        "per_runde": per_runde,
    }
    return avvik, fakta


# --------------------------------------------------------------------------- tropp


def finn_tropp(events: list[dict]) -> tuple[int | None, dict[str, str], list[str]]:
    """Nyeste tilgjengelige picks-fil. Returnerer (runde, {navn: lag}, merknader).

    Picks for en runde finnes først etter at deadline er passert, så vi går bakover
    fra siste påbegynte runde. Rapporten MÅ oppgi hvilken runde snapshotet er fra —
    en tropp fra GW5 er ikke troppen i GW8.
    """
    merknader: list[str] = []
    paabegynt = [int(e["id"]) for e in events if e.get("finished") == "True" or e.get("is_current") == "True"]
    start = max(paabegynt) if paabegynt else 1

    for runde in range(start, 0, -1):
        rader = hent_csv_valgfri(f"entry/picks/gw{runde}.csv")
        if rader:
            return runde, {r["web_name"]: r["team"] for r in rader}, merknader

    merknader.append("fant ingen picks-fil i speilet — spillerkolonnen er tom")
    return None, {}, merknader


# --------------------------------------------------------------------------- utskrift


def rundetabell(runde: int, rader: list[dict], tropp: dict[str, str]) -> list[str]:
    rader = sorted(rader, key=lambda r: (r["kickoff_time"], r["home"]))
    ut = [
        "",
        f"### GW{runde}",
        "",
        "| Dato | UK-tid | Kamp | Troppen |",
        "|---|---|---|---|",
    ]
    i_spill = 0
    interne: list[str] = []

    for r in rader:
        t = uk(r["kickoff_time"])
        mine = sorted(n for n, lag in tropp.items() if lag in (r["home"], r["away"]))
        i_spill += len(mine)
        if tropp and r["home"] in tropp.values() and r["away"] in tropp.values():
            interne.append(f"{r['home']}–{r['away']} ({len(mine)})")
        ut.append(
            f"| {datostreng(t)} | {t:%H:%M} | {r['home']} – {r['away']} "
            f"| {', '.join(mine) if mine else '—'} |"
        )

    soner = {uk(r["kickoff_time"]).tzname() for r in rader}
    ut.append("")
    ut.append(f"{i_spill} spillere i spill. Interne oppgjør: {', '.join(interne) if interne else 'ingen'}.")
    if len(soner) > 1:
        ut.append("")
        ut.append(
            "⚠️ **Klokka stilles inne i denne runden** — "
            f"kampene ligger i både {' og '.join(sorted(soner))}. Kolonnen er ferdig omregnet til UK-tid."
        )
    return ut


def bygg_blokk(antall_runder: int) -> tuple[str, list[str]]:
    fixtures = hent_csv("fixtures.csv")
    fixtures_json = hent_json("fixtures.json")
    events = hent_csv("events.csv")

    avvik, fakta = strukturkontroll(fixtures, fixtures_json)
    tropp_runde, tropp, merknader = finn_tropp(events)
    avvik.extend(merknader)

    # Troppens lagnavn skal finnes i kampprogrammet. Treffer ikke, har speilet
    # endret navneformat, og spillerkolonnen blir stille feil.
    alle_lag = {f["home"] for f in fixtures} | {f["away"] for f in fixtures}
    ukjente = sorted({lag for lag in tropp.values() if lag not in alle_lag})
    if ukjente:
        avvik.append(f"lagnavn i picks finnes ikke i fixtures: {', '.join(ukjente)}")

    neste = [int(e["id"]) for e in events if e.get("is_next") == "True"]
    naa = [int(e["id"]) for e in events if e.get("is_current") == "True"]
    fra = neste[0] if neste else (naa[0] if naa else 1)
    vindu = [r for r in range(fra, fra + antall_runder) if r in fakta["per_runde"]]

    deadlines = {int(e["id"]): e["deadline_time"] for e in events}
    generert = dt.datetime.now(dt.timezone.utc)

    L: list[str] = [START, ""]
    L.append("## Kampprogram — generert fra speilet")
    L.append("")
    L.append(
        f"*Generert {generert:%d.%m.%Y kl. %H:%M} UTC av `scripts/gen_kampprogram.py` "
        f"fra `fpl-data`. **Rør ikke denne blokka for hånd** — endringer blir overskrevet "
        f"ved neste kjøring. Endringsloggen og verifiseringsnotatene ligger under markøren.*"
    )
    L.append("")

    if avvik:
        L.append("### ⚠️ Strukturavvik")
        L.append("")
        for a in avvik:
            L.append(f"- {a}")
        L.append("")
        L.append(
            "Avvik over er funnet maskinelt i speilet. En blank- eller dobbelrunde her er "
            "**ikke** bekreftet av Premier League før det står i en nivå 1-kilde — slå det opp."
        )
        L.append("")
    else:
        L.append(
            f"**Strukturkontroll: ingen avvik.** {fakta['kamper']} kamper, {fakta['runder']} runder, "
            f"{fakta['lag']} lag, alle runder med nøyaktig 10 kamper og 20 unike lag. "
            f"Ingen blankrunde, ingen dobbelrunde, 0 kamper med foreløpig klokkeslett. "
            f"csv og json i speilet er identiske."
        )
        L.append("")

    if tropp_runde:
        L.append(
            f"**Spillerkolonnen bygger på `entry/picks/gw{tropp_runde}.csv`** "
            f"({len(tropp)} spillere) — nyeste tilgjengelige øyeblikksbilde. "
            f"Bytter gjort etter GW{tropp_runde}-deadline vises ikke."
        )
        L.append("")

    for runde in vindu:
        L.extend(rundetabell(runde, fakta["per_runde"][runde], tropp))

    L.append("")
    L.append("### Deadlines")
    L.append("")
    L.append("| Runde | Deadline (UTC) | Deadline (UK) |")
    L.append("|---|---|---|")
    for runde in vindu:
        d = deadlines.get(runde)
        if d:
            t = uk(d)
            L.append(f"| GW{runde} | `{d}` | {datostreng(t)} {t:%H:%M} |")

    L.append("")
    L.append("### Rundestruktur, alle 38")
    L.append("")
    L.append("Antall ulike avsparkstidspunkt per runde. Står alle ti kampene på samme slott, "
             "er kringkastervalget for den runden ikke kunngjort ennå.")
    L.append("")
    L.append("| Runde | Kamper | Ulike slott | Datoer |")
    L.append("|---|---|---|---|")
    for runde in sorted(fakta["per_runde"]):
        rader = fakta["per_runde"][runde]
        tider = {f"{uk(r['kickoff_time']):%Y-%m-%d %H:%M}" for r in rader}
        datoer = sorted({uk(r["kickoff_time"]).date() for r in rader})
        d = f"{datoer[0]:%d.%m.}" if len(datoer) == 1 else f"{datoer[0]:%d.%m.}–{datoer[-1]:%d.%m.}"
        flagg = " — **ikke kunngjort**" if len(tider) == 1 else ""
        L.append(f"| GW{runde} | {len(rader)} | {len(tider)}{flagg} | {d} |")

    L.append("")
    L.append(SLUTT)
    return "\n".join(L), avvik


# --------------------------------------------------------------------------- skriving


def uten_tidsstempel(tekst: str) -> str:
    return "\n".join(l for l in tekst.splitlines() if not l.startswith("*Generert "))


def skriv(blokk: str, init: bool) -> bool:
    """Bytter ut blokka mellom markørene. Returnerer True hvis fila ble endret."""
    if not MAALFIL.exists():
        sys.exit(f"finner ikke {MAALFIL} — kjør fra reporoten")

    tekst = MAALFIL.read_text(encoding="utf-8")

    if START not in tekst or SLUTT not in tekst:
        if not init:
            sys.exit(
                f"markørene mangler i {MAALFIL}.\n"
                f"Legg inn disse to linjene der kampprogrammet skal stå, så tar skriptet resten:\n"
                f"  {START}\n  {SLUTT}\n"
                f"Eller kjør med --init for å legge dem til på slutten av fila."
            )
        tekst = tekst.rstrip() + "\n\n" + START + "\n" + SLUTT + "\n"

    foer, _, rest = tekst.partition(START)
    gammel, _, etter = rest.partition(SLUTT)
    ny = foer + blokk + etter

    # Tidsstempelet endres hver kjøring. Uten denne sammenligningen ville CI
    # committe hver gang selv når ingen kamp har flyttet seg.
    if uten_tidsstempel(START + gammel + SLUTT) == uten_tidsstempel(blokk):
        return False
    MAALFIL.write_text(ny, encoding="utf-8")
    return True


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true", help="exit 1 ved strukturavvik, skriv ingenting")
    p.add_argument("--stdout", action="store_true", help="skriv blokka til stdout")
    p.add_argument("--init", action="store_true", help="legg til markørene hvis de mangler")
    p.add_argument("--runder", type=int, default=5, help="antall runder framover (standard 5)")
    a = p.parse_args()

    blokk, avvik = bygg_blokk(a.runder)

    if a.check:
        for x in avvik:
            print(f"AVVIK: {x}", file=sys.stderr)
        print(f"{len(avvik)} avvik", file=sys.stderr)
        return 1 if avvik else 0

    if a.stdout:
        print(blokk)
        return 0

    endret = skriv(blokk, a.init)
    print("04 oppdatert" if endret else "04 uendret")
    for x in avvik:
        print(f"AVVIK: {x}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
