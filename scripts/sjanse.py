#!/usr/bin/env python3
"""Kalibrering av FPL-flagget «d» (tvilsom, 25/50/75 %) mot hvem som faktisk spilte.

Leser historikken til fpl-data (players.csv er speilet fire ganger i døgnet) fra en lokal klon,
tar siste versjon før hver deadline, og sammenligner flaggede spillere med hvor ofte de samme
spillerne spiller når de ikke er flagget. Kjøres for hånd, ikke i CI. Kun stdlib.

Bruk (fra reporoten):
    git clone --filter=blob:none https://github.com/steinim/fpl-data /tmp/fpl-data
    python3 scripts/sjanse.py /tmp/fpl-data

Mål: a = (antall som spilte, minutter > 0) / (sum av spillernes egen spilleandel i runder der de
sto som «a» før deadline). a = 1 betyr at flagget ikke koster noe utover vanlig rotasjon.
Bare spillere som spiller i minst halvparten av de uflaggede rundene (minst to slike runder).
k = runder etter flagget (0 = runden flagget gjelder). Observasjonene overlapper: samme spiller
kan telle i flere påfølgende snapshot. Tabellene er beskrivende, ikke en tilpasset modell.

forventning.py bruker i dag FPL-sjansen for k = 0 og 100 % for k ≥ 1.
"""

from __future__ import annotations

import collections
import csv
import datetime as dt
import io
import pathlib
import subprocess
import sys


def git(repo: pathlib.Path, *a: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, check=True).stdout


def tid(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 1
    repo = pathlib.Path(argv[0])
    data = repo / "data"
    events = list(csv.DictReader(open(data / "events.csv", encoding="utf-8")))
    deadline = {int(e["id"]): tid(e["deadline_time"]) for e in events}
    ferdig = [int(e["id"]) for e in events if e["finished"] == "True" and e["data_checked"] == "True"]
    siste = max(ferdig)
    live = {n: {r["id"]: int(r["minutes"]) for r in csv.DictReader(open(data / f"live/gw{n}.csv", encoding="utf-8"))}
            for n in range(1, siste + 1)}
    commits = sorted((tid(t), h) for h, t in (l.split() for l in
                     git(repo, "log", "--format=%H %cI", "--", "data/players.csv").splitlines()))
    snap: dict[int, list[dict]] = {}
    for n in range(1, siste + 1):
        for_ = [h for t, h in commits if t < deadline[n]]
        if for_:
            snap[n] = list(csv.DictReader(io.StringIO(git(repo, "show", f"{for_[-1]}:data/players.csv"))))
    if not snap:
        print("ingen snapshot før noen deadline", file=sys.stderr)
        return 1

    base: dict[str, list[int]] = collections.defaultdict(lambda: [0, 0])
    for n, rader in snap.items():
        for r in rader:
            if r["status"] == "a":
                base[r["id"]][1] += 1
                base[r["id"]][0] += live[n].get(r["id"], 0) > 0

    def andel(i: str) -> float | None:
        x, y = base[i]
        return x / y if y >= 2 else None

    etter_sjanse = collections.defaultdict(lambda: [0, 0.0, 0])
    etter_borte = collections.defaultdict(lambda: [0, 0.0, 0])
    for n, rader in snap.items():
        for r in rader:
            b = andel(r["id"])
            if r["status"] != "d" or not b or b < 0.5:
                continue
            borte = 0
            while n - 1 - borte >= 1 and live[n - 1 - borte].get(r["id"], 0) == 0:
                borte += 1
            g = "0" if borte == 0 else ("1" if borte == 1 else "2+")
            for k in range(5):
                if n + k > siste:
                    break
                spilte = live[n + k].get(r["id"], 0) > 0
                for tab, nokkel in ((etter_sjanse, (r["chance_next"], k)), (etter_borte, (g, k))):
                    t = tab[nokkel]
                    t[0] += spilte
                    t[1] += b
                    t[2] += 1

    print(f"Snapshot før GW{min(snap)}–GW{max(snap)}, utfall til GW{siste}.\n")
    for tittel, tab, kol in (("Etter FPL-sjanse", etter_sjanse, "Sjanse"),
                             ("Etter runder på rad uten minutter før flagget", etter_borte, "Borte")):
        print(f"### {tittel}\n\n| {kol} | k | n | a |\n|---|---|---|---|")
        for (g, k) in sorted(tab):
            s, e, n = tab[(g, k)]
            print(f"| {g} | {k} | {n} | {s / e:.2f} |")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
