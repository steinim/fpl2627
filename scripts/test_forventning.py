#!/usr/bin/env python3
"""Tester for scripts/forventning.py. Kjør fra reporoten:

    python3 -m unittest discover -s scripts -p "test_*.py" -v

Tre lag:
  1. Poengreglene i skriptet mot tabellen i context/05 (nivå 0).
  2. Enhetstester per ledd på syntetiske data der svaret er kjent.
  3. Regresjonstester mot ekte rundedata i speilet (GW1–6, låste runder). Hoppes over uten
     nettilgang. Tilfellene er feilene fra 17.10.2026: João Pedro GW5, Thomas og Egan DC,
     Fernandes GW2.
"""

from __future__ import annotations

import datetime as dt
import json
import math
import pathlib
import re
import sys
import tempfile
import unittest
import urllib.error

HER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HER))
import forventning as fv  # noqa: E402

REGLER = HER.parent / "context" / "05-spillets-regler.md"


# --------------------------------------------------------------------------- 1. regler mot 05


def poengtabell() -> dict[str, list[str]]:
    tekst = REGLER.read_text(encoding="utf-8")
    seksjon = tekst.split("## 5. Poeng", 1)[1].split("\n## ", 1)[0]
    rader = {}
    for linje in seksjon.splitlines():
        if not linje.startswith("|") or "---" in linje or "Hendelse" in linje:
            continue
        celler = [c.strip() for c in linje.strip().strip("|").split("|")]
        rader[celler[0]] = celler[1:]
    return rader


def tall(celle: str) -> int:
    c = celle.replace("**", "").replace("−", "-").strip()
    return 0 if c in ("—", "-", "") else int(c)


class TestReglerMot05(unittest.TestCase):
    def setUp(self):
        self.t = poengtabell()
        self.pos = ["GKP", "DEF", "MID", "FWD"]

    def rad(self, start: str) -> list[int]:
        treff = [k for k in self.t if k == start] or [k for k in self.t if k.startswith(start)]
        self.assertEqual(len(treff), 1, f"fant ikke én rad som starter med «{start}» i 05")
        return [tall(c) for c in self.t[treff[0]]]

    def test_oppmote(self):
        self.assertEqual(self.rad("Spilt inntil 60 min"), [fv.POENG["short_play"]] * 4)
        self.assertEqual(self.rad("Spilt 60 min eller mer"), [fv.POENG["long_play"]] * 4)
        self.assertEqual(fv.MIN_LANG, 60)

    def test_per_posisjon(self):
        for start, nokkel in (("Mål", "goals_scored"), ("Clean sheet", "clean_sheets"),
                              ("Defensive contribution", "defensive_contribution")):
            self.assertEqual(self.rad(start), [fv.POENG[nokkel][p] for p in self.pos], start)
        self.assertEqual(self.rad("Per **2** baklengsmål"), [fv.POENG["goals_conceded"][p] for p in self.pos])

    def test_flate(self):
        self.assertEqual(self.rad("Målgivende"), [fv.POENG["assists"]] * 4)
        self.assertEqual(self.rad("Bommet straffe"), [fv.POENG["penalties_missed"]] * 4)
        self.assertEqual(self.rad("Gult kort"), [fv.POENG["yellow_cards"]] * 4)
        self.assertEqual(self.rad("Rødt kort"), [fv.POENG["red_cards"]] * 4)
        self.assertEqual(self.rad("Selvmål"), [fv.POENG["own_goals"]] * 4)
        self.assertEqual(self.rad("Strafferedning")[0], fv.POENG["penalties_saved"])
        self.assertEqual(self.rad("Per **3** redninger")[0], fv.POENG["saves"])

    def test_terskler(self):
        tekst = REGLER.read_text(encoding="utf-8")
        self.assertIn(f"Per **{fv.REDNINGER_PER_POENG}** redninger", tekst)
        self.assertIn(f"Per **{fv.BAKLENGS_PER_POENG}** baklengsmål", tekst)
        self.assertRegex(tekst, rf"forsvarere trenger \*\*{fv.DC_TERSKEL['DEF']}\*\*")
        self.assertRegex(tekst, rf"Midtbanespillere \*\*og spisser\*\* trenger \*\*{fv.DC_TERSKEL['MID']}\*\*")
        self.assertEqual(fv.DC_TERSKEL["MID"], fv.DC_TERSKEL["FWD"])

    def test_bonusfelt_folger_bps(self):
        # 05: clean sheet gir BPS bare til keeper og forsvarer.
        self.assertIn("Clean sheet, keeper eller forsvarer", REGLER.read_text(encoding="utf-8"))
        self.assertNotIn("cs", fv.BONUS_FELT["MID"])
        self.assertNotIn("cs", fv.BONUS_FELT["FWD"])


# --------------------------------------------------------------------------- 2. matematikk


class TestMatematikk(unittest.TestCase):
    def brute(self, lam: float, k: int) -> float:
        p, tot = math.exp(-lam), 0.0
        for n in range(200):
            if n > 0:
                p *= lam / n
            tot += p * (n // k)
        return tot

    def test_poisson_floor(self):
        for lam in (0.0, 0.05, 0.78, 1.43, 3.0, 7.5):
            for k in (2, 3):
                self.assertAlmostEqual(fv.poisson_floor_forventning(lam, k), self.brute(lam, k), places=9)
        self.assertAlmostEqual(fv.poisson_floor_forventning(0.78, 2), 0.193, places=3)

    def test_eb_k(self):
        like = [[1.0, 1.2, 0.8, 1.1], [1.0, 0.9, 1.1, 1.0], [1.05, 0.95, 1.0, 1.0]]
        self.assertEqual(fv.eb_k(like)[0], 38.0)  # ingen forskjell mellom grupper -> maks krymping
        ulike = [[0.5, 0.52, 0.48], [1.0, 1.02, 0.98], [1.5, 1.52, 1.48], [2.0, 2.0, 2.02]]
        self.assertEqual(fv.eb_k(ulike)[0], 1.0)  # stor forskjell, lite støy -> min krymping

    def test_ols_eksakt(self):
        x = [[1.0, a, b] for a in range(5) for b in range(4)]
        y = [0.3 + 1.5 * r[1] - 0.25 * r[2] for r in x]
        for fasit, est in zip([0.3, 1.5, -0.25], fv.ols(x, y)):
            self.assertAlmostEqual(fasit, est, places=6)

    def test_korrelasjon(self):
        self.assertAlmostEqual(fv.pearson([1, 2, 3, 4], [2, 4, 6, 8]), 1.0)
        self.assertAlmostEqual(fv.spearman([1, 2, 3, 4], [1, 4, 9, 16]), 1.0)


# --------------------------------------------------------------------------- 2b. fravær, prior og tilgjengelighet


ELEMENTER = {165: {"id": 165, "web_name": "João Pedro"}, 426: {"id": 426, "web_name": "B.Fernandes"}}


class TestFravaerOgPrior(unittest.TestCase):
    def test_gyldig_rad(self):
        tekst = "id,navn,runder,aarsak,sjanse,kilde,notat\n165,João Pedro,5-6,skade,,kilde,\n"
        f, feil = fv.les_fravaer(tekst, ELEMENTER)
        self.assertEqual(feil, [])
        self.assertEqual(sorted(f[165]), [5, 6])
        self.assertEqual(f[165][5].aarsak, "skade")

    def test_feil_navn_stopper(self):
        tekst = "id,navn,runder,aarsak,sjanse,kilde,notat\n165,Joao,5,skade,,,\n"
        _, feil = fv.les_fravaer(tekst, ELEMENTER)
        self.assertEqual(len(feil), 1)
        self.assertIn("heter", feil[0])

    def test_ukjent_aarsak_og_id(self):
        tekst = "id,navn,runder,aarsak,sjanse,kilde,notat\n165,João Pedro,5,forkjølet,,,\n999,X,5,skade,,,\n"
        _, feil = fv.les_fravaer(tekst, ELEMENTER)
        self.assertEqual(len(feil), 2)

    def test_prior(self):
        lag = {1: {"short_name": "ARS"}, 2: {"short_name": "COV"}}
        tekst = "lag,A,D,grunnlag\nARS,1.2,0.6,x\nOPPRYKK,0.8,1.2,y\n"
        pr, opp, feil = fv.les_prior(tekst, lag, rho=0.5)
        self.assertEqual(feil, [])
        self.assertEqual(opp, ["COV"])
        self.assertAlmostEqual(pr[1][0], 1.1)
        self.assertAlmostEqual(pr[1][1], 0.8)
        self.assertAlmostEqual(pr[2][1], 1.1)
        self.assertTrue(fv.les_prior("lag,A,D\nARS,1,1\n", lag)[2], "manglende OPPRYKK skal gi feil")


def profil(**k) -> fv.Profil:
    base = dict(eid=1, navn="X", lag=1, pos="MID", pris=5.0, status="a", sjanse_neste=None, nyhet="", straffe=None)
    base.update(k)
    return fv.Profil(**base)


class TestTilgjengelighet(unittest.TestCase):
    def test_retur_dato(self):
        self.assertEqual(fv.retur_dato("Hamstring injury - Expected back 24 Oct", 2026), dt.date(2026, 10, 24))
        self.assertEqual(fv.retur_dato("Suspended until 7 Jan", 2026), dt.date(2027, 1, 7))
        self.assertIsNone(fv.retur_dato("Knee injury - Unknown return date", 2026))

    def test_regler(self):
        okt = lambda d: dt.date(2026, 10, d)  # noqa: E731
        skadet = profil(status="i", sjanse_neste=0, nyhet="Ankle injury - Expected back 24 Oct")
        self.assertEqual(fv.tilgjengelighet(skadet, 8, okt(23), 8, {}, 2026)[0], 0.0)
        self.assertEqual(fv.tilgjengelighet(skadet, 8, okt(24), 8, {}, 2026)[0], 1.0)
        ukjent = profil(status="i", sjanse_neste=0, nyhet="Back injury - Unknown return date")
        self.assertEqual(fv.tilgjengelighet(ukjent, 9, okt(31), 8, {}, 2026)[0], 0.0)
        tvil = profil(status="d", sjanse_neste=75, nyhet="Knock - 75% chance of playing")
        self.assertEqual(fv.tilgjengelighet(tvil, 8, okt(24), 8, {}, 2026)[0], 0.75)
        self.assertEqual(fv.tilgjengelighet(tvil, 9, okt(31), 8, {}, 2026)[0], 1.0)
        self.assertEqual(fv.tilgjengelighet(profil(status="u"), 8, okt(24), 8, {}, 2026)[0], 0.0)
        overstyr = {8: fv.Fravaer("karantene", None, "")}
        self.assertEqual(fv.tilgjengelighet(profil(), 8, okt(24), 8, overstyr, 2026)[0], 0.0)


# --------------------------------------------------------------------------- 2c. hele kjeden på en syntetisk liga


def lag_speil(mappe: pathlib.Path, runder: dict[int, list[tuple[int, int]]], spillere: dict[int, dict],
              statistikk: dict[tuple[int, int], dict], fremtid: dict[int, list[tuple[int, int]]]) -> None:
    """Skriver en minimal speilkopi. runder: {runde: [(hjemme, borte), ...]}.
    statistikk: {(runde, spiller): stats-dict}; manglende felt fylles med 0."""
    lag = sorted({t for kamper in list(runder.values()) + list(fremtid.values()) for k in kamper for t in k})
    kamper, fid = [], 0
    kamp_id: dict[tuple[int, int], list[int]] = {}
    for n, liste in sorted(list(runder.items()) + list(fremtid.items())):
        for h, b in liste:
            fid += 1
            ferdig = n in runder
            kamper.append({"id": fid, "event": n, "team_h": h, "team_a": b, "finished": ferdig,
                           "kickoff_time": f"2026-08-{10 + n:02d}T14:00:00Z", "stats": []})
            for t in (h, b):
                kamp_id.setdefault((n, t), []).append(fid)
    events = [{"id": n, "finished": n in runder, "data_checked": n in runder, "is_next": n == min(fremtid),
               "is_current": n == max(runder), "deadline_time": f"2026-08-{10 + n:02d}T12:00:00Z"}
              for n in sorted(list(runder) + list(fremtid))]
    felt = fv.SUMMEFELT_HEL + fv.SUMMEFELT_DESIMAL
    totaler = {eid: {f: 0.0 for f in felt} for eid in spillere}
    (mappe / "live").mkdir(parents=True)
    for n in runder:
        el = []
        for eid, sp in spillere.items():
            s = {f: 0 for f in fv.SUMMEFELT_HEL}
            s.update({f: "0.00" for f in fv.SUMMEFELT_DESIMAL})
            s.update(statistikk.get((n, eid), {}))
            for f in felt:
                totaler[eid][f] += float(s[f])
            el.append({"id": eid, "stats": s,
                       "explain": [{"fixture": k, "stats": []} for k in kamp_id.get((n, sp["team"]), [])]})
        (mappe / "live" / f"gw{n}.json").write_text(json.dumps({"elements": el}), encoding="utf-8")
    elementer = []
    for eid, sp in spillere.items():
        e = {"id": eid, "web_name": sp["navn"], "team": sp["team"], "element_type": sp["type"], "now_cost": 50,
             "status": "a", "chance_of_playing_next_round": None, "news": "", "penalties_order": None}
        for f in felt:
            v = totaler[eid][f]
            e[f] = f"{v:.2f}" if f in fv.SUMMEFELT_DESIMAL else int(v)
        elementer.append(e)
    bootstrap = {"elements": elementer, "events": events,
                 "teams": [{"id": t, "name": f"Lag{t}", "short_name": f"L{t}"} for t in lag],
                 "game_config": {"scoring": fv.POENG}}
    (mappe / "bootstrap-static.json").write_text(json.dumps(bootstrap), encoding="utf-8")
    (mappe / "fixtures.json").write_text(json.dumps(kamper), encoding="utf-8")


def st(minutter: int, start: int = 1, **k) -> dict:
    d = {"minutes": minutter, "starts": start}
    for nokkel, verdi in k.items():
        d[nokkel] = f"{verdi:.2f}" if nokkel in fv.SUMMEFELT_DESIMAL else verdi
    return d


class TestKjede(unittest.TestCase):
    """Fire lag, tre spilte runder, to runder framover. Spiller 1 (MID, lag 1) er skadet i GW2."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        mappe = pathlib.Path(cls.tmp.name)
        runder = {1: [(1, 2), (3, 4)], 2: [(1, 3), (2, 4)], 3: [(4, 1), (3, 2)]}
        fremtid = {4: [(2, 1), (4, 3)], 5: [(1, 4), (2, 3), (1, 3)]}  # GW5: lag 1 har to kamper
        spillere = {
            1: {"navn": "Skadet", "team": 1, "type": 3},
            2: {"navn": "Stopper", "team": 2, "type": 2},
            3: {"navn": "Innbytter", "team": 3, "type": 4},
            4: {"navn": "Keeper", "team": 4, "type": 1},
            5: {"navn": "Kortspiller", "team": 1, "type": 3},
        }
        statistikk = {}
        for n in runder:
            statistikk[(n, 2)] = st(90, defensive_contribution=[10, 9, 12][n - 1], expected_goals=0.1,
                                    expected_goals_conceded=1.0)
            statistikk[(n, 3)] = st(20, start=0, expected_goals=0.2)
            statistikk[(n, 4)] = st(90, saves=[3, 5, 1][n - 1], expected_goals_conceded=1.2)
            statistikk[(n, 5)] = st(45, expected_goals=0.05)
        statistikk[(1, 1)] = st(90, expected_goals=0.5, expected_assists=0.2, goals_scored=1)
        statistikk[(3, 1)] = st(80, expected_goals=0.3, expected_assists=0.1)
        # GW2: 0 minutter for spiller 1
        cls.mappe = mappe
        lag_speil(mappe, runder, spillere, statistikk, fremtid)
        cls.data = fv.last_data(fv.Kilde(mappe))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def modell(self, fravaer=None) -> fv.Modell:
        return fv.bygg_modell(self.data, fravaer or {})

    def test_kontroller_gaar_gjennom(self):
        feil, _, ok = fv.kontroller(self.data, [], dt.datetime(2026, 8, 13, tzinfo=dt.timezone.utc))
        self.assertEqual(feil, [])
        self.assertTrue(any("summerer" in x for x in ok))

    def test_kontroller_fanger_feil_poengregel(self):
        self.data.poengregler["assists"] = 4
        try:
            feil, _, _ = fv.kontroller(self.data, [], dt.datetime(2026, 8, 13, tzinfo=dt.timezone.utc))
            self.assertTrue(any("assists" in x for x in feil))
        finally:
            self.data.poengregler["assists"] = 3

    def test_uavklart_fravaer_flagges_og_telles(self):
        p = self.modell().profiler[1]
        self.assertEqual(p.fravaer_uavklart, [2])
        self.assertEqual((p.starter, p.telte), (2, 3))
        self.assertTrue(any("UAVKLART" in f for f in p.flagg))

    def test_skade_holdes_utenfor(self):
        p = self.modell({1: {2: fv.Fravaer("skade", None, "test")}}).profiler[1]
        self.assertEqual(p.fravaer_utelatt, [2])
        self.assertEqual((p.starter, p.telte, p.startandel), (2, 2, 1.0))
        self.assertEqual(p.fravaer_uavklart, [])

    def test_rotasjon_telles(self):
        p = self.modell({1: {2: fv.Fravaer("rotasjon", None, "test")}}).profiler[1]
        self.assertEqual((p.starter, p.telte), (2, 3))
        self.assertEqual(p.fravaer_uavklart, [])

    def test_dc_fra_rundetall(self):
        p = self.modell().profiler[2]  # DEF med DC 10, 9, 12 -> 2 av 3 over terskel 10
        self.assertEqual(p.dc_grunnlag, "2/3")
        # Eneste forsvarer i ligaen: posisjonssnittet er hans egen rate, så krympingen endrer ingenting.
        self.assertAlmostEqual(p.dc_start, 2 / 3)

    def test_dc_krymping(self):
        a = profil(pos="DEF")
        a.dc_treff_s, a.dc_n_s = 4, 6
        b = profil(eid=2, pos="DEF")
        b.dc_treff_s, b.dc_n_s = 0, 6
        fv.krymp_dc({1: a, 2: b}, 4.0)
        self.assertAlmostEqual(a.dc_start, (4 + 4 * 4 / 12) / 10)
        self.assertAlmostEqual(b.dc_start, (0 + 4 * 4 / 12) / 10)
        fv.krymp_dc({1: a, 2: b}, 0.0)
        self.assertAlmostEqual(a.dc_start, 4 / 6)

    def test_ingen_cs_uten_60_min(self):
        m = self.modell()
        p = m.profiler[5]  # starter hver kamp, men går av etter 45 min
        k = fv.forvent_kamp(p, m.styrke, m.liga, 2, "H", 1.0)
        self.assertEqual(k["cs"], 0.0)
        self.assertAlmostEqual(k["oppmote"], 1.0)

    def test_komponentene_summerer(self):
        m = self.modell()
        for eid, p in m.profiler.items():
            k = fv.forvent_kamp(p, m.styrke, m.liga, 2, "B", 0.8)
            self.assertAlmostEqual(k["total"], sum(k[c] for c in fv.KOMPONENTER), places=9)

    def test_tilgjengelighet_null_gir_null(self):
        m = self.modell()
        for p in m.profiler.values():
            self.assertEqual(fv.forvent_kamp(p, m.styrke, m.liga, 2, "H", 0.0)["total"], 0.0)

    def test_avtak_vekter_nylige_kamper(self):
        # Spiller 1: start GW1, fravær GW2 (uavklart = ikke-start), start GW3.
        p = self.modell().profiler[1]
        a = fv.AVTAK
        self.assertAlmostEqual(p.startandel, (a ** 2 + 1) / (a ** 2 + a + 1))
        # Samme fravær ført som rotasjon gir samme tall; som skade utelates det.
        q = self.modell({1: {2: fv.Fravaer("skade", None, "")}}).profiler[1]
        self.assertAlmostEqual(q.startandel, 1.0)

    def test_innbytter(self):
        p = self.modell().profiler[3]
        self.assertEqual((p.starter, p.innbytter, p.startandel, p.innbytterandel), (0, 3, 0.0, 1.0))
        self.assertAlmostEqual(p.min_innbytter, 20.0)

    def test_dobbelrunde_i_horisonten(self):
        m = self.modell()
        pr = fv.projiser(m, 5, [4, 5], {})
        enkel = fv.projiser(m, 5, [4], {})["runder"][4]
        self.assertGreater(pr["runder"][5], 1.5 * enkel)
        self.assertTrue(any("dobbelrunde" in x for x in pr["merknader"]))

    def test_sannsynlighet_for_aa_spille(self):
        m = self.modell()
        # Grunnlaget er GW1–3, så GW4 er h = 0 og GW5 er h = 1.
        # Spiller 2 startet alle tre: s = u = 1. Lag 2 har én kamp i både GW4 og GW5.
        pr = fv.projiser(m, 2, [4, 5], {})
        for n, h in ((4, 0), (5, 1)):
            ps = sum(fv.START_KAL[h])
            self.assertAlmostEqual(pr["spiller"][n], max(ps, sum(fv.SPILL_KAL[h])))
            self.assertLess(pr["spiller"][n], 1.0)
        # Spiller 1: lag 1 har to kamper i GW5, så P(spiller) = 1 − (1 − p)².
        p = m.profiler[1]
        pr1 = fv.projiser(m, 1, [4, 5], {})
        self.assertAlmostEqual(pr1["spiller"][4], sum(fv.minutt_sannsynlighet(p, 0)))
        self.assertAlmostEqual(pr1["spiller"][5], 1 - (1 - sum(fv.minutt_sannsynlighet(p, 1))) ** 2)
        skadet = fv.projiser(m, 1, [4], {4: fv.Fravaer("skade", None, "")})
        self.assertEqual(skadet["spiller"][4], 0.0)

    def test_h_regnes_fra_siste_runde_i_grunnlaget(self):
        m = self.modell()
        p = m.profiler[2]
        alene = fv.projiser(m, 2, [5], {})["runder"][5]
        mot, bane = 3, "H"  # GW5: (2, 3), lag 2 hjemme
        self.assertAlmostEqual(alene, fv.forvent_kamp(p, m.styrke, m.liga, mot, bane, 1.0, h=1)["total"])
        self.assertNotAlmostEqual(alene, fv.forvent_kamp(p, m.styrke, m.liga, mot, bane, 1.0, h=0)["total"])


    def test_krymping_mot_pris(self):
        uten = fv.bygg_modell(self.data, {}, spiller_k=0.0).profiler[1]
        med = fv.bygg_modell(self.data, {}, spiller_k=3.0).profiler[1]
        lav, hoy = sorted([uten.xg90, med.xg90_prior])
        self.assertTrue(lav - 1e-12 <= med.xg90 <= hoy + 1e-12, "krympet rate skal ligge mellom rå rate og prior")
        self.assertNotEqual(uten.xg90, med.xg90)

    def test_keeper_redninger(self):
        m = self.modell()
        p = m.profiler[4]
        self.assertGreater(p.redn90, 0)
        k = fv.forvent_kamp(p, m.styrke, m.liga, 1, "H", 1.0)
        self.assertGreater(k["redninger"], 0)
        self.assertEqual(k["dc"], 0.0)


class TestMinuttkalibrering(unittest.TestCase):
    def fast(self, **k) -> fv.Profil:
        p = profil(**k)
        p.telte, p.starter, p.innbytter, p.startandel, p.innbytterandel = 10, 10, 0, 1.0, 0.0
        return p

    def test_raa_andeler_uten_h(self):
        p = profil()
        p.telte, p.starter, p.innbytter, p.startandel, p.innbytterandel = 4, 2, 1, 0.6, 0.5
        ps, pi = fv.minutt_sannsynlighet(p, None)
        self.assertAlmostEqual(ps, 0.6)
        self.assertAlmostEqual(pi, 0.4 * 0.5)

    def test_fast_starter_under_en_og_synkende(self):
        p = self.fast()
        start = [fv.minutt_sannsynlighet(p, h)[0] for h in range(7)]
        self.assertTrue(all(a > b for a, b in zip(start, start[1:])), start)
        self.assertTrue(0.85 < start[0] < 0.95, start[0])
        self.assertTrue(0.75 < start[6] < 0.85, start[6])

    def test_reserve_over_null_og_stigende(self):
        p = profil()
        p.telte, p.starter, p.innbytter, p.startandel, p.innbytterandel = 10, 0, 0, 0.0, 0.0
        start = [fv.minutt_sannsynlighet(p, h)[0] for h in range(7)]
        self.assertTrue(all(a < b for a, b in zip(start, start[1:])), start)
        self.assertGreater(start[0], 0.0)

    def test_spiller_minst_like_ofte_som_start(self):
        for s in (0.0, 0.3, 0.7, 1.0):
            for ib in (0.0, 0.5, 1.0):
                p = profil()
                p.telte, p.starter, p.innbytter = 10, round(10 * s), round(10 * (1 - s) * ib)
                p.startandel, p.innbytterandel = s, ib
                for h in range(9):
                    ps, pi = fv.minutt_sannsynlighet(p, h)
                    self.assertGreaterEqual(pi, 0.0)
                    self.assertLessEqual(ps + pi, 1.0)
                    self.assertGreaterEqual(ps, 0.0)

    def test_h_utover_tabellen_bruker_siste(self):
        p = self.fast()
        siste = max(fv.START_KAL)
        self.assertEqual(fv.minutt_sannsynlighet(p, siste + 5), fv.minutt_sannsynlighet(p, siste))

    def test_ingen_telte_kamper_gir_null(self):
        p = profil()
        self.assertEqual(fv.minutt_sannsynlighet(p, 0), (0.0, 0.0))

    def test_konstantene_passer_forklaringsvariablene(self):
        n = len(fv.minuttledd(0.5, 0.5))
        self.assertEqual(sorted(fv.START_KAL), list(range(len(fv.START_KAL))))
        self.assertEqual(sorted(fv.SPILL_KAL), sorted(fv.START_KAL))
        for c in list(fv.START_KAL.values()) + list(fv.SPILL_KAL.values()):
            self.assertEqual(len(c), n)


# --------------------------------------------------------------------------- 3. ekte data


def ekte() -> fv.Data | None:
    try:
        return fv.last_data(fv.Kilde(), til_runde=7)
    except (urllib.error.URLError, OSError):
        return None


class TestEkteData(unittest.TestCase):
    """Rundedata GW1–6 2026/27 fra speilet. Låste runder endrer seg ikke."""

    @classmethod
    def setUpClass(cls):
        cls.data = ekte()
        if cls.data is None:
            raise unittest.SkipTest("ingen nettilgang til speilet")
        cls.fravaer = {165: {5: fv.Fravaer("skade", None, "roundtable.io 16.9.2026")}}
        cls.m = fv.bygg_modell(cls.data, cls.fravaer)
        cls.m_uten = fv.bygg_modell(cls.data, {})

    def finn(self, navn: str, lag: str) -> int:
        treff = [e for e, x in self.data.elementer.items()
                 if x["web_name"] == navn and self.data.lag[x["team"]]["short_name"] == lag]
        self.assertEqual(len(treff), 1, f"{navn} ({lag})")
        return treff[0]

    def test_fernandes_en_kamp(self):
        p = self.m.profiler[426]
        self.assertAlmostEqual(p.xgi90_raa, 0.673, places=3)
        self.assertAlmostEqual(p.xgi90_uten_beste, 0.308, places=3)
        self.assertEqual(p.beste_runde, 2)
        self.assertAlmostEqual(p.andel_beste, 2.50 / 4.04, places=2)
        self.assertTrue(any("GW2" in f and "xGI" in f for f in p.flagg))

    def test_joao_pedro_skade_gw5(self):
        p = self.m.profiler[165]
        self.assertEqual(p.fravaer_utelatt, [5])
        self.assertEqual((p.starter, p.telte, p.startandel), (5, 5, 1.0))
        q = self.m_uten.profiler[165]
        self.assertEqual(q.fravaer_uavklart, [5])
        a = fv.AVTAK  # starter GW1–4 og GW6, ikke-start GW5; vekt a^(6 − runde)
        start = sum(a ** (6 - n) for n in (1, 2, 3, 4, 6))
        self.assertAlmostEqual(q.startandel, start / (start + a))

    def test_thomas_dc_fra_rundetall(self):
        p = self.m.profiler[self.finn("Thomas", "COV")]
        self.assertEqual(p.dc_grunnlag, "4/6")  # 10, 9, 12, 8, 13, 22
        self.assertTrue(0.0 < p.dc_start < 4 / 6, "krympet rate skal ligge under råraten 4/6")

    def test_egan_dc_fra_rundetall(self):
        p = self.m.profiler[self.finn("Egan", "HUL")]
        self.assertEqual(p.dc_grunnlag, "3/6")  # 21, 13, 7, 14, 4, 6

    def test_lagkart_loser_alle(self):
        self.assertEqual(self.m.uloste_lag, [])

    def test_poengregler_i_api(self):
        feil, _, _ = fv.kontroller(self.data, [], dt.datetime.now(dt.timezone.utc))
        self.assertFalse([x for x in feil if "poengreglene" in x])


if __name__ == "__main__":
    unittest.main()
