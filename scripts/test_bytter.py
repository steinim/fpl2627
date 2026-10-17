#!/usr/bin/env python3
"""Tester for scripts/bytter.py. Kjør fra reporoten:

    python3 -m unittest discover -s scripts -p "test_*.py" -v

  1. Regler: salgspris mot eksempelet i context/05, frikjøp runde for runde, reglene i API-et.
  2. Lagpoeng: elleveren, kapteinsleddet og innbytterne mot en uttømmende opptelling av alle
     utfall etter regelen i 05.
  3. Planer: bank, klubbgrense, minuspoeng, og at søket finner et salg i én runde som
     finansierer et kjøp i den neste.
  4. Troppstilstand fra speilfiler: bankkjede, overganger og bytter oppgitt for hånd.
  5. Ekte data (hoppes over uten nett): bankkjeden og frikjøpene for laget i speilet.
"""

from __future__ import annotations

import itertools
import json
import pathlib
import re
import sys
import tempfile
import unittest
import urllib.error

HER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HER))
import bytter as by  # noqa: E402
import forventning as fv  # noqa: E402

REGLER = HER.parent / "context" / "05-spillets-regler.md"


# --------------------------------------------------------------------------- 1. regler


class TestRegler(unittest.TestCase):
    def test_salgspris_eksempelet_i_05(self):
        tekst = REGLER.read_text(encoding="utf-8")
        m = re.search(r"kjøpt £(\d+),(\d)m, steget til £(\d+),(\d)m, salgspris \*\*£(\d+),(\d)m\*\*", tekst)
        self.assertIsNotNone(m, "fant ikke regelsidens eksempel i 05")
        kjopt, naa, salg = (int(m.group(i)) * 10 + int(m.group(i + 1)) for i in (1, 3, 5))
        self.assertEqual(by.salgspris(kjopt, naa), salg)

    def test_salgspris_ellers(self):
        self.assertEqual(by.salgspris(67, 68), 67)    # +0,1 gir ingenting
        self.assertEqual(by.salgspris(55, 59), 57)    # halve stigningen
        self.assertEqual(by.salgspris(120, 118), 118)  # fall: hele fallet
        self.assertEqual(by.salgspris(40, 40), 40)

    def test_maks_frikjop_og_minuspoeng_i_05(self):
        tekst = REGLER.read_text(encoding="utf-8")
        self.assertIn(f"**Maks {by.MAKS_FRIKJOP} lagret**", tekst)
        self.assertIn(f"**−{by.HIT} poeng**", tekst)
        self.assertIn(f"| Maks per klubb | {by.MAKS_PER_KLUBB} |", tekst)

    def historikk(self, bytter: list[int], kostnad: list[int] | None = None, chips=()) -> dict:
        kostnad = kostnad or [0] * len(bytter)
        return {"current": [{"event": i + 1, "event_transfers": b, "event_transfers_cost": c, "bank": 0}
                            for i, (b, c) in enumerate(zip(bytter, kostnad))],
                "chips": [{"event": e, "name": n} for e, n in chips]}

    def test_frikjop_som_laget_i_speilet(self):
        # GW1–6 slik history.json viser dem 17.10.2026, tre bytter i GW7.
        h = self.historikk([0, 0, 0, 2, 0, 1], chips=[(5, "3xc")])
        ft, forklaring, feil = by.frikjop(h, {7: 3}, 7)
        self.assertEqual((ft, feil), (3, []))
        ft, _, feil = by.frikjop(h, {7: 3}, 8)
        self.assertEqual((ft, feil), (1, []))

    def test_frikjop_tak_og_minuspoeng(self):
        ft, _, feil = by.frikjop(self.historikk([0] * 9), {}, 10)
        self.assertEqual((ft, feil), (5, []))
        # 3 bytter med 1 frikjøp = 2 hits = −8 i historikken: stemmer.
        ft, _, feil = by.frikjop(self.historikk([0, 3], [0, 8]), {}, 3)
        self.assertEqual((ft, feil), (1, []))

    def test_frikjop_avvik_mot_kostnad_er_feil(self):
        _, _, feil = by.frikjop(self.historikk([0, 3], [0, 4]), {}, 3)
        self.assertTrue(feil)

    def test_frikjop_etter_wildcard_er_feil(self):
        _, _, feil = by.frikjop(self.historikk([0, 0, 5], chips=[(3, "wildcard")]), {}, 4)
        self.assertTrue(any("wildcard" in x for x in feil))

    def test_frikjop_ukjent_runde(self):
        ft, _, feil = by.frikjop(self.historikk([0, 0]), {}, 4)
        self.assertIsNone(ft)
        self.assertTrue(feil)

    def test_regler_i_api(self):
        regler = {"squad_team_limit": 3, "max_extra_free_transfers": 4, "transfers_sell_on_fee": 0.5,
                  "element_sell_at_purchase_price": False, "squad_squadsize": 15}
        self.assertEqual(by.kontroller_regler(regler)[0], [])
        self.assertTrue(by.kontroller_regler({**regler, "squad_team_limit": 4})[0])
        self.assertTrue(by.kontroller_regler({})[0])


# --------------------------------------------------------------------------- 2. lagpoeng


def spiller(eid: int, pos: str, xp: float, p: float = 1.0, lag: int | None = None, pris: int = 50,
            runder: int = 1) -> by.Spiller:
    return by.Spiller(eid, f"S{eid}", pos, lag if lag is not None else eid, pris, [xp] * runder, [xp] * runder,
                      [p] * runder)


def tropp(xp: dict[int, tuple[str, float, float]], **k) -> dict[int, by.Spiller]:
    return {e: spiller(e, pos, x, p, **k) for e, (pos, x, p) in xp.items()}


STANDARD = {
    1: ("GKP", 4.0, 1.0), 2: ("GKP", 3.0, 1.0),
    3: ("DEF", 5.0, 1.0), 4: ("DEF", 4.0, 1.0), 5: ("DEF", 3.0, 1.0), 6: ("DEF", 2.0, 1.0), 7: ("DEF", 1.0, 1.0),
    8: ("MID", 9.0, 1.0), 9: ("MID", 6.0, 1.0), 10: ("MID", 5.5, 1.0), 11: ("MID", 2.5, 1.0), 12: ("MID", 1.5, 1.0),
    13: ("FWD", 8.0, 1.0), 14: ("FWD", 3.5, 1.0), 15: ("FWD", 0.5, 1.0),
}


def simuler_innbytte(spill: dict[str, list[float]], benk: list[tuple[str, float]]) -> list[float]:
    """Uttømmende opptelling: hver starter og benkespiller spiller eller ikke, uavhengig.
    Regelen i 05: utespillere som ikke spilte, tas i rekkefølge forsvar, midtbane, angrep, og byttes
    mot den høyest prioriterte innbytteren som spilte og ikke bryter formasjonen."""
    startere = [(pos, q) for pos in by.ORDEN for q in spill.get(pos, [])]
    antall0 = {pos: len(spill.get(pos, [])) for pos in by.ORDEN}
    ut = [0.0] * len(benk)
    for s_utfall in itertools.product([0, 1], repeat=len(startere)):
        ps = 1.0
        for (pos, q), spilte in zip(startere, s_utfall):
            ps *= q if spilte else 1 - q
        for b_utfall in itertools.product([0, 1], repeat=len(benk)):
            pb = 1.0
            for (_, q), spilte in zip(benk, b_utfall):
                pb *= q if spilte else 1 - q
            antall = dict(antall0)
            ledig = [j for j in range(len(benk)) if b_utfall[j]]
            for (pos, _), spilte in zip(startere, s_utfall):
                if spilte:
                    continue
                for j in ledig:
                    bpos = benk[j][0]
                    if bpos != pos and (antall[pos] - 1 < by.MIN_FORM[pos] or antall[bpos] + 1 > by.MAKS_FORM[bpos]):
                        continue
                    antall[pos] -= 1
                    antall[bpos] += 1
                    ut[j] += ps * pb
                    ledig.remove(j)
                    break
    return ut


class TestLagpoeng(unittest.TestCase):
    def test_elleveren_folger_formasjonen(self):
        ev = by.Evaluator(tropp(STANDARD))
        d = ev.detaljer(tuple(STANDARD), 0)
        ellever = set(d["ellever"])
        # Keeper 1; forsvar 3, 4, 5 (minst tre); spiss 13 (minst én); deretter de seks beste av resten:
        # 8 (9,0), 9 (6,0), 10 (5,5), 14 (3,5), 11 (2,5), 6 (2,0).
        self.assertEqual(ellever, {1, 3, 4, 5, 13, 8, 9, 10, 14, 11, 6})
        self.assertEqual(d["benk"], [2, 12, 7, 15])
        self.assertAlmostEqual(d["xi"], 4 + 5 + 4 + 3 + 8 + 9 + 6 + 5.5 + 3.5 + 2.5 + 2)

    def test_minst_tre_forsvarere_selv_om_de_er_svake(self):
        svak = {**STANDARD, 3: ("DEF", 0.3, 1.0), 4: ("DEF", 0.2, 1.0), 5: ("DEF", 0.1, 1.0),
                6: ("DEF", 0.05, 1.0), 7: ("DEF", 0.01, 1.0)}
        d = by.Evaluator(tropp(svak)).detaljer(tuple(svak), 0)
        self.assertEqual(sum(1 for e in d["ellever"] if svak[e][0] == "DEF"), 3)

    def test_kapteinsledd(self):
        xp = {**STANDARD, 8: ("MID", 9.0, 0.5)}
        d = by.Evaluator(tropp(xp)).detaljer(tuple(xp), 0)
        # Kaptein 8: 9 + 0,5·8 = 13. Kaptein 13: 8 + 0·9 = 8. Det beste leddet velges.
        self.assertEqual(d["kaptein"], 8)
        self.assertAlmostEqual(d["kapteinsledd"], 9.0 + 0.5 * 8.0)

    def test_ingen_innbytte_naar_alle_spiller(self):
        d = by.Evaluator(tropp(STANDARD)).detaljer(tuple(STANDARD), 0)
        self.assertAlmostEqual(d["innbytte"], 0.0)
        self.assertAlmostEqual(d["sum"], d["xi"] + d["kapteinsledd"])

    def test_keeper_bare_for_keeper(self):
        xp = {**STANDARD, 1: ("GKP", 4.0, 0.6), 2: ("GKP", 3.0, 0.5)}
        d = by.Evaluator(tropp(xp)).detaljer(tuple(xp), 0)
        self.assertAlmostEqual(d["innbytte"], 0.4 * 3.0)

    def test_innbyttere_mot_uttommende_opptelling(self):
        tilfeller = [
            ({"DEF": [0.9, 0.8, 0.95], "MID": [0.9, 0.7, 0.9, 0.85], "FWD": [0.9, 0.6, 0.8]},
             [("MID", 0.9), ("DEF", 0.8), ("FWD", 0.7)]),
            ({"DEF": [0.9, 0.8, 0.95, 0.5], "MID": [0.9, 0.7, 0.9], "FWD": [0.6, 0.8, 0.9]},
             [("DEF", 0.9), ("MID", 0.8), ("MID", 0.95)]),
            ({"DEF": [0.7, 0.7, 0.7, 0.7, 0.7], "MID": [0.5, 0.6, 0.9], "FWD": [0.8, 0.8]},
             [("MID", 0.5), ("MID", 0.9), ("FWD", 0.4)]),
            ({"DEF": [0.91] * 3, "MID": [0.91] * 4, "FWD": [0.91] * 3}, [("DEF", 0.91), ("DEF", 0.91), ("MID", 0.91)]),
        ]
        for spill, benk in tilfeller:
            fasit = simuler_innbytte(spill, benk)
            svar = by.innbyttere(tuple((pos, tuple(v)) for pos, v in spill.items()), tuple(benk), terskel=0.0)
            for a, b in zip(svar, fasit):
                self.assertAlmostEqual(a, b, places=12, msg=f"{spill} {benk}")

    def test_innbyttere_med_standard_terskel_er_naer_fasit(self):
        spill = {"DEF": [0.9, 0.8, 0.95], "MID": [0.9, 0.7, 0.9, 0.85], "FWD": [0.9, 0.6, 0.8]}
        benk = [("MID", 0.9), ("DEF", 0.8), ("FWD", 0.7)]
        fasit = simuler_innbytte(spill, benk)
        svar = by.innbyttere(tuple((pos, tuple(v)) for pos, v in spill.items()), tuple(benk))
        for a, b in zip(svar, fasit):
            self.assertAlmostEqual(a, b, places=5)

    def test_tre_forsvarere_laaser_forsvaret(self):
        # Tre forsvarere i elleveren og bare midtbane på benken: en forsvarer som ikke spiller,
        # kan ikke erstattes.
        svar = by.innbyttere((("DEF", (0.0, 1.0, 1.0)), ("MID", (1.0,) * 4), ("FWD", (1.0,) * 3)),
                             (("MID", 1.0), ("MID", 1.0), ("MID", 1.0)), terskel=0.0)
        self.assertEqual(svar, (0.0, 0.0, 0.0))
        svar = by.innbyttere((("DEF", (0.0, 1.0, 1.0, 1.0)), ("MID", (1.0,) * 3), ("FWD", (1.0,) * 3)),
                             (("MID", 1.0), ("MID", 1.0), ("DEF", 1.0)), terskel=0.0)
        self.assertEqual(svar, (1.0, 0.0, 0.0))


# --------------------------------------------------------------------------- 3. planer


def tilstand(tropp_ids: list[int], bank: int, frikjop: int, innkjop: dict[int, int] | None = None) -> by.Tilstand:
    return by.Tilstand(list(tropp_ids), innkjop or {}, bank, frikjop, 8, [], [], [], [])


class TestPlaner(unittest.TestCase):
    def oppsett(self, n_runder: int = 5, bank: int = 0, frikjop: int = 1, maks_hits: int = 0,
                ekstra: dict[int, by.Spiller] | None = None, kand: dict[str, list[int]] | None = None):
        S = {e: spiller(e, pos, x, p, pris=50, runder=n_runder) for e, (pos, x, p) in STANDARD.items()}
        for e in S:
            S[e].lag = e  # hver sin klubb
        S.update(ekstra or {})
        t = tilstand(list(STANDARD), bank, frikjop, {e: S[e].pris for e in STANDARD})
        kand = kand or {pos: [e for e, s in S.items() if s.pos == pos and e not in STANDARD] for pos in fv.POSISJONER}
        return by.Planlegger(t, S, kand, n_runder, maks_hits)

    def test_salg_som_finansierer_kjop_neste_runde(self):
        # Z (midtbane, £10,0m, 12 per runde) er for dyr for ett salg: Y (£9,0m) er den dyreste i
        # troppen og banken er tom. Riktig plan: S12 (benk, £5,0m) → C (£1,0m) i A frigjør £4,0m,
        # og Y → Z i B. Det koster ingenting i A, fordi S12 sitter på benken og alle spiller.
        ekstra = {20: spiller(20, "MID", 12.0, pris=100, runder=5),     # Z
                  21: spiller(21, "MID", 0.1, pris=10, runder=5)}       # C
        for e in ekstra:
            ekstra[e].lag = e
        pl = self.oppsett(ekstra=ekstra)
        pl.s[10].pris, pl.t.innkjop[10] = 90, 90     # Y: 5,5 per runde
        spar, planer, _ = pl.sok()
        beste = planer[0]
        self.assertEqual({(b.ut, b.inn) for b in beste.a}, {(12, 21)})
        self.assertEqual({(b.ut, b.inn) for b in beste.b}, {(10, 20)})
        self.assertEqual((beste.bank_a, beste.bank_b), (40, 30))
        # Fire runder med Z: 12 − 5,5 i elleveren, og Z tar kapteinsbindet fra S8 (12 − 9).
        self.assertAlmostEqual(beste.verdi - spar.verdi, 4 * ((12.0 - 5.5) + (12.0 - 9.0)))
        # Y → Z alene er ikke lovlig: banken holder ikke.
        self.assertIsNone(pl.vurder((), (by.Bytte(10, 20),)))

    def test_klubbgrense(self):
        ekstra = {20: spiller(20, "MID", 20.0, pris=10, runder=5), 22: spiller(22, "DEF", 2.0, pris=10, runder=5)}
        ekstra[20].lag, ekstra[22].lag = 99, 22
        pl = self.oppsett(ekstra=ekstra)
        for e in (3, 4, 5):
            pl.s[e].lag = 99           # tre fra klubb 99 allerede
        self.assertIsNone(pl.vurder((by.Bytte(12, 20),), ()))
        # Selges en av dem først, er kjøpet lovlig i neste runde.
        self.assertIsNotNone(pl.vurder((by.Bytte(3, 22),), (by.Bytte(12, 20),)))

    def test_minuspoeng_og_frikjop(self):
        ekstra = {20: spiller(20, "MID", 3.0, pris=10, runder=5), 21: spiller(21, "FWD", 2.0, pris=10, runder=5)}
        for e in ekstra:
            ekstra[e].lag = e
        pl = self.oppsett(ekstra=ekstra, maks_hits=1)
        to = (by.Bytte(12, 20), by.Bytte(15, 21))
        p = pl.vurder(to, ())
        self.assertEqual(p.hits, 1)
        self.assertAlmostEqual(p.verdi, pl.ev.runde(p.tropp_a, 0) + sum(pl.ev.runde(p.tropp_b, g) for g in range(1, 5)) - 4)
        # Spart i A gir to frikjøp i B: ingen minuspoeng.
        self.assertEqual(pl.vurder((), to).hits, 0)
        # Uten tillatte hits er to bytter i A ulovlig.
        pl.maks_hits = 0
        self.assertIsNone(pl.vurder(to, ()))

    def test_frikjop_neste_runde(self):
        pl = self.oppsett(frikjop=1)
        self.assertEqual([pl.frikjop_b(n) for n in (0, 1, 2)], [2, 1, 1])
        pl = self.oppsett(frikjop=5)
        self.assertEqual(pl.frikjop_b(0), 5)


# --------------------------------------------------------------------------- 4. tilstand fra speilfiler


def element(eid: int, pos: int, lag: int, pris: int, endring: int = 0, navn: str | None = None) -> dict:
    return {"id": eid, "web_name": navn or f"S{eid}", "element_type": pos, "team": lag, "now_cost": pris,
            "cost_change_start": endring, "status": "a"}


class TestTilstand(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        mappe = pathlib.Path(self.tmp.name)
        (mappe / "entry" / "picks").mkdir(parents=True)
        typer = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4]
        el = {e: element(e, typer[e - 1], e, 50) for e in range(1, 16)}
        el[8]["now_cost"], el[8]["cost_change_start"] = 78, 3       # startpris 75, nå 78
        el[20] = element(20, 3, 20, 60)
        el[21] = element(21, 3, 21, 80, navn="Dobbel")
        el[22] = element(22, 3, 22, 40, navn="Dobbel")
        el[30] = element(30, 3, 30, 52)                             # kjøpt GW2 til 50, nå 52
        self.data = fv.Data(elementer=el, lag={t: {"id": t, "short_name": f"L{t}"} for t in range(1, 31)},
                            events=[], poengregler={}, kamper={}, live={}, grunnlag=[1, 2, 3], utelatte_runder=[],
                            snapshot=None, tropp_runde=3, tropp=list(range(1, 16)),
                            regler={"squad_team_limit": 3, "max_extra_free_transfers": 4, "transfers_sell_on_fee": 0.5,
                                    "element_sell_at_purchase_price": False, "squad_squadsize": 15})
        overganger = [{"element_in": 30, "element_in_cost": 50, "element_out": 9, "element_out_cost": 50,
                       "event": 2, "time": "2026-08-28T10:00:00Z"}]
        historikk = {"current": [{"event": 1, "event_transfers": 0, "event_transfers_cost": 0, "bank": 0},
                                 {"event": 2, "event_transfers": 1, "event_transfers_cost": 0, "bank": 0},
                                 {"event": 3, "event_transfers": 0, "event_transfers_cost": 0, "bank": 0}],
                     "chips": []}
        tropp_ids = [e for e in range(1, 16) if e != 9] + [30]
        picks = {"picks": [{"element": e} for e in tropp_ids], "entry_history": {"bank": 0}}
        (mappe / "entry" / "transfers.json").write_text(json.dumps(overganger))
        (mappe / "entry" / "history.json").write_text(json.dumps(historikk))
        (mappe / "entry" / "picks" / "gw3.json").write_text(json.dumps(picks))
        self.historikk = historikk
        self.mappe = mappe
        self.kilde = fv.Kilde(mappe)

    def tearDown(self):
        self.tmp.cleanup()

    def test_tropp_bank_og_frikjop(self):
        t = by.bygg_tilstand(self.kilde, self.data, 4, [], None, None, None)
        self.assertEqual(t.feil, [])
        self.assertEqual(t.bank, 0)
        self.assertEqual(t.frikjop, 2)              # GW2: 1 frikjøp brukt → 1; GW3: 0 brukt → 2
        self.assertEqual(t.innkjop[30], 50)         # siste kjøp
        self.assertEqual(t.innkjop[8], 75)          # startpris
        self.assertTrue(any("stemmer med historikken" in x for x in t.ok))

    def test_bytter_oppgitt_for_haand(self):
        # S8 (kjøpt 75, nå 78: salgspris 76) → S20 (60): bank 0 + 76 − 60 = 16.
        t = by.bygg_tilstand(self.kilde, self.data, 5, [(8, 20)], 4, None, None)
        self.assertEqual(t.feil, [])
        self.assertEqual(t.bank, 16)
        self.assertIn(20, t.tropp)
        self.assertNotIn(8, t.tropp)
        self.assertEqual(t.frikjop, 2)              # GW4: 2 frikjøp, 1 brukt → 2 til GW5

    def test_bank_under_null_er_feil(self):
        # Keeper ut for midtbane er ulovlig posisjon:
        with self.assertRaises(ValueError):
            by.bygg_tilstand(self.kilde, self.data, 5, [(1, 21)], 4, None, None)
        # Midtbane S10 (50) → S21 (80): bank −30.
        t = by.bygg_tilstand(self.kilde, self.data, 5, [(10, 21)], 4, None, None)
        self.assertTrue(any("banken blir" in x for x in t.feil))

    def test_bankkjede_som_ikke_stemmer_er_feil(self):
        self.historikk["current"][1]["bank"] = 5
        (self.mappe / "entry" / "history.json").write_text(json.dumps(self.historikk))
        t = by.bygg_tilstand(self.kilde, self.data, 4, [], None, None, None)
        self.assertTrue(any("bankkjede" in x or "banken regnet" in x for x in t.feil))

    def test_horisont_for_troppen_er_feil(self):
        with self.assertRaises(ValueError):
            by.bygg_tilstand(self.kilde, self.data, 3, [], None, None, None)

    def test_tvetydig_navn(self):
        with self.assertRaises(ValueError):
            by.finn_spiller("Dobbel", self.data)
        self.assertEqual(by.finn_spiller("Dobbel@L22", self.data), 22)
        self.assertEqual(by.finn_spiller("30", self.data), 30)


# --------------------------------------------------------------------------- 5. ekte data


class TestEkteData(unittest.TestCase):
    """Laget i speilet. Historikken for låste runder endrer seg ikke."""

    @classmethod
    def setUpClass(cls):
        try:
            k = fv.Kilde()
            cls.historikk = k.json("entry/history.json")
            cls.overganger = k.json("entry/transfers.json")
        except (urllib.error.URLError, OSError):
            raise unittest.SkipTest("ingen nettilgang til speilet")

    def test_bankkjeden_stemmer(self):
        bank = 0
        for h in sorted(self.historikk["current"], key=lambda h: h["event"]):
            bank += sum(t["element_out_cost"] - t["element_in_cost"] for t in self.overganger if t["event"] == h["event"])
            self.assertEqual(bank, h["bank"], f"GW{h['event']}")

    def test_frikjop_gw8(self):
        # Tre bytter i GW7 (01). Når GW7 er i historikken, brukes den i stedet.
        ft, _, feil = by.frikjop(self.historikk, {7: 3}, 8)
        self.assertEqual(feil, [])
        self.assertEqual(ft, 1)


if __name__ == "__main__":
    unittest.main()
