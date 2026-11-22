# Byttepakker — generert

*Generert 22.11.2026 kl. 20:43 UTC av `scripts/bytter.py` fra `fpl-data`. **Rør ikke fila for hånd.** Horisont GW12–16. Bytter vurderes i GW12 og GW13. Maks minuspoeng per runde: 0.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–10 summerer til sesongtotalene for 54 spillere, 19 felt; 620 spillere på lag som har spilt i GW11 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 22.11.2026 20:28 UTC, 0.3 t gammelt ved kjøring
- ✅ Bytteregler i API-et stemmer med 05 og skriptet: maks 3 per klubb, maks 5 frikjøp, halve prisstigningen ved salg, tropp på 15
- ✅ Bank regnet fra 10 overganger stemmer med historikken i alle 11 runder
- ✅ Frikjøp til GW12: 1. Kostnaden i hver runde stemmer med historikken

**Frikjøp, runde for runde:** GW1: første runde → 1 · GW2: 1 frikjøp, 0 brukt → 2 · GW3: 2 frikjøp, 0 brukt → 3 · GW4: 3 frikjøp, 2 brukt → 2 · GW5: 2 frikjøp, 0 brukt → 3 · GW6: 3 frikjøp, 1 brukt → 3 · GW7: 3 frikjøp, 3 brukt → 1 · GW8: 1 frikjøp, 0 brukt → 2 · GW9: 2 frikjøp, 2 brukt → 1 · GW10: 1 frikjøp, 0 brukt → 2 · GW11: 2 frikjøp, 2 brukt → 1

## Chips

Brukt i settet: Triple Captain GW5. Igjen: **Wildcard, Free Hit, Bench Boost**. Frist: GW19-deadline 2027-01-01T18:30:00Z (UTC), 8 runder fra og med GW12, én chip per runde (`05`).

## Troppen inn i GW12

Bank **£2.5m**, frikjøp **1**. Salgspris etter regelen i `05`.

| Spiller | Lag | Pos | Nå | Kjøpt | Salgspris | Sum GW12–16 | Robust | P(spiller) GW12 | Eid |
|---|---|---|---|---|---|---|---|---|---|
| Verbruggen | BHA | GKP | £4.7m | £4.5m | £4.6m | 14.20 | 13.91 | 0.91 | 24.5 % |
| Kinsky | TOT | GKP | £4.4m | £4.5m | £4.4m | 13.33 | 13.33 | 0.91 | 16.0 % |
| Van Hecke | TOT | DEF | £5.2m | £5.1m | £5.1m | 18.02 | 16.44 | 0.91 | 18.7 % |
| Calafiori | ARS | DEF | £5.9m | £5.5m | £5.7m | 16.93 | 16.14 | 0.91 | 48.5 % |
| Thomas (COV) | COV | DEF | £4.0m | £4.0m | £4.0m | 15.71 | 15.08 | 0.91 | 6.8 % |
| Diop | IPS | DEF | £3.9m | £4.0m | £3.9m | 13.42 | 13.31 | 0.91 | 9.5 % |
| Davis | IPS | DEF | £4.0m | £4.0m | £4.0m | 12.92 | 12.01 | 0.68 | 6.2 % |
| E.Le Fée | SUN | MID | £5.7m | £5.7m | £5.7m | 23.32 | 21.20 | 0.91 | 3.1 % |
| Mbeumo | MUN | MID | £7.8m | £8.0m | £7.8m | 22.92 | 20.03 | 0.91 | 17.8 % |
| B.Fernandes | MUN | MID | £11.6m | £12.0m | £11.6m | 22.76 | 19.27 | 0.79 | 20.0 % |
| Tavernier | BOU | MID | £6.7m | £6.4m | £6.5m | 22.04 | 20.21 | 0.91 | 33.1 % |
| Groß | BHA | MID | £6.3m | £6.1m | £6.2m | 20.79 | 18.61 | 0.91 | 49.4 % |
| Haaland | MCI | FWD | £15.8m | £15.5m | £15.6m | 26.78 | 25.38 | 0.91 | 78.3 % |
| Barry | EVE | FWD | £5.7m | £5.7m | £5.7m | 24.30 | 22.58 | 0.91 | 11.5 % |
| Evanilson | BOU | FWD | £6.6m | £6.3m | £6.4m | 20.86 | 18.96 | 0.91 | 26.7 % |

## Spar — ingen bytter

Lagets forventede poeng: **283.41** over horisonten (robust 260.35). Per runde: GW12 56.30, GW13 57.33, GW14 57.60, GW15 56.59, GW16 55.58.

GW12: elleveren 46.38 + kapteinsledd 6.02 (B.Fernandes, vise Barry) + innbytterledd 3.91. Benk: Kinsky, Evanilson, Diop, Davis.

## Beste planer (35926 lovlige av 49956 vurderte)

Endring = forventede poeng mot å spare, over hele horisonten, etter minuspoeng.

| Plan | Minus | Endring GW12–16 | Robust endring | Endring GW12 | Bank etter GW12 | Bank etter GW13 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| GW12: Davis → Muharemović · GW13: Diop → Silva | 0 | **+7.13** | +6.65 | +1.22 | £1.4m | £0.2m | BOU |
| GW12: Diop → Muharemović · GW13: Davis → Silva | 0 | **+7.05** | +6.56 | +1.15 | £1.3m | £0.2m | BOU |
| GW12: Davis → De Cuyper · GW13: Diop → Konsa | 0 | **+6.83** | +5.03 | +1.33 | £1.0m | £0.0m | BHA |
| GW12: Davis → Vuskovic · GW13: Diop → Silva | 0 | **+6.78** | +6.32 | +0.91 | £1.2m | £0.0m | BHA, BOU |
| GW12: Diop → De Cuyper · GW13: Davis → Konsa | 0 | **+6.76** | +4.94 | +1.25 | £0.9m | £0.0m | BHA |
| GW12: Davis → De Cuyper · GW13: Calafiori → Murillo | 0 | **+6.75** | +5.03 | +1.33 | £1.0m | £1.2m | BHA |
| GW12: Diop → De Cuyper · GW13: Calafiori → Murillo | 0 | **+6.70** | +4.79 | +1.25 | £0.9m | £1.1m | BHA |
| GW12: Davis → Bogle · GW13: Diop → Murillo | 0 | **+6.70** | +6.13 | +1.10 | £1.7m | £0.1m | — |
| GW12: Diop → Vuskovic · GW13: Davis → Silva | 0 | **+6.70** | +6.23 | +0.84 | £1.1m | £0.0m | BHA, BOU |
| GW12: Davis → De Cuyper · GW13: Calafiori → Silva | 0 | **+6.68** | +4.36 | +1.33 | £1.0m | £1.6m | BHA, BOU |
| GW12: Davis → Silva · GW13: Diop → Muharemović | 0 | **+6.65** | +6.09 | +0.75 | £1.4m | £0.2m | BOU |
| GW12: Diop → De Cuyper · GW13: Calafiori → Silva | 0 | **+6.63** | +4.11 | +1.25 | £0.9m | £1.5m | BHA, BOU |
| GW12: Davis → De Cuyper · GW13: Diop → Bogle | 0 | **+6.63** | +4.21 | +1.33 | £1.0m | £0.1m | BHA |
| GW12: Diop → Bogle · GW13: Davis → Murillo | 0 | **+6.63** | +6.03 | +1.02 | £1.6m | £0.1m | — |
| GW12: Davis → Bogle · GW13: Diop → Silva | 0 | **+6.63** | +5.45 | +1.10 | £1.7m | £0.5m | BOU |

## Wildcard i GW12

Beste tropp innenfor £99.7m (bank + salgspriser), funnet med lokalsøk på elleveren og kapteinen, deretter regnet med innbytterledd som planene over.

| | Forventet GW12–16 | Robust | Mot å spare | Mot beste plan |
|---|---|---|---|---|
| Wildcard | **293.39** | 272.12 | +9.98 | **+2.85** |
| Beste plan | 290.54 | 267.00 | +7.13 | — |
| Spar | 283.41 | 260.35 | — | — |

Per runde mot beste plan: GW12 +0.76, GW13 -0.27, GW14 -0.43, GW15 +0.32, GW16 +2.47.

Ut (7): Verbruggen, Thomas (COV), Calafiori, B.Fernandes, Kinsky, Diop, Davis. Inn (7): Trafford £5.1m, Wilson (COV) £4.4m, Gabriel £8.1m, De Cuyper £5.5m, Silva £5.1m, Justin £4.5m, Gibbs-White £7.8m.

- Klubber etter: BOU 3 · BHA 2 · LEE 2 · ARS 1 · COV 1 · EVE 1 · MCI 1 · MUN 1 · NFO 1 · SUN 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £32.1m → £37.9m
- Bank etter: £0.2m
- Wildcardet beholder frikjøpene (`05`), planene bruker dem. Gevinsten over beste plan er det chipen kjøper i denne horisonten; det samme wildcardet senere kan være verdt mer eller mindre. Søket er ikke garantert optimalt.

## Beste plan som selger hver spiller

Svarer på «bør X selges?»: den beste lovlige planen der spilleren går ut, mot å spare.

| Plan | Minus | Endring GW12–16 | Robust endring | Endring GW12 | Bank etter GW12 | Bank etter GW13 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| **Verbruggen ut:** GW12: Davis → De Cuyper · GW13: Verbruggen → Trafford | 0 | **+6.45** | +4.63 | +1.33 | £1.0m | £0.5m | — |
| **Kinsky ut:** GW12: Davis → De Cuyper · GW13: Kinsky → Trafford | 0 | **+6.52** | +4.67 | +1.33 | £1.0m | £0.3m | BHA |
| **Van Hecke ut:** GW12: Davis → De Cuyper · GW13: Van Hecke → Murillo | 0 | **+5.91** | +4.79 | +1.33 | £1.0m | £0.6m | BHA |
| **Calafiori ut:** GW12: Davis → De Cuyper · GW13: Calafiori → Murillo | 0 | **+6.75** | +5.03 | +1.33 | £1.0m | £1.2m | BHA |
| **Thomas (COV) ut:** GW12: Davis → De Cuyper · GW13: Thomas (COV) → Konsa | 0 | **+6.07** | +4.28 | +1.33 | £1.0m | £0.1m | BHA |
| **Diop ut:** GW12: Davis → Muharemović · GW13: Diop → Silva | 0 | **+7.13** | +6.65 | +1.22 | £1.4m | £0.2m | BOU |
| **Davis ut:** GW12: Davis → Muharemović · GW13: Diop → Silva | 0 | **+7.13** | +6.65 | +1.22 | £1.4m | £0.2m | BOU |
| **E.Le Fée ut:** GW12: Calafiori → De Cuyper · GW13: E.Le Fée → Gibbs-White | 0 | **+1.89** | +0.89 | +0.99 | £2.7m | £0.6m | BHA |
| **Mbeumo ut:** GW12: Davis → De Cuyper · GW13: Mbeumo → Gibbs-White | 0 | **+5.08** | +4.56 | +1.33 | £1.0m | £1.0m | BHA |
| **B.Fernandes ut:** GW12: Davis → De Cuyper · GW13: B.Fernandes → Gibbs-White | 0 | **+3.57** | +4.01 | +1.33 | £1.0m | £4.8m | BHA |
| **Tavernier ut:** GW12: Davis → Silva · GW13: Tavernier → Gibbs-White | 0 | **+4.97** | +5.10 | +0.75 | £1.4m | £0.1m | — |
| **Groß ut:** GW12: Davis → De Cuyper · GW13: Groß → Ødegaard | 0 | **+5.03** | +3.02 | +1.33 | £1.0m | £0.5m | — |
| **Haaland ut:** GW12: Davis → De Cuyper · GW13: Haaland → Isak | 0 | **-1.98** | -4.85 | +1.33 | £1.0m | £7.3m | BHA |
| **Barry ut:** GW12: Diop → Bogle · GW13: Barry → N.Jackson | 0 | **+0.09** | -1.08 | +1.02 | £1.6m | £0.1m | — |
| **Evanilson ut:** GW12: Davis → De Cuyper · GW13: Evanilson → N.Jackson | 0 | **+4.19** | +2.22 | +1.33 | £1.0m | £0.2m | BHA |

## Anti-drift for de tre beste planene

**GW12: Davis → Muharemović · GW13: Diop → Silva**

- Klubber etter: BOU 3 · BHA 2 · MUN 2 · TOT 2 · ARS 1 · COV 1 · EVE 1 · LEE 1 · MCI 1 · SUN 1
- Keeper- og forsvarsbudsjett (nåpris): £32.1m → £34.4m. Flytter det mer enn £1,0m, er det en strukturendring (CLAUDE.md).
- Bank: £2.5m → £1.4m etter GW12 → £0.2m etter GW13
- Endring per runde: GW12 +1.22, GW13 +0.47, GW14 +2.60, GW15 +0.07, GW16 +2.77

**GW12: Diop → Muharemović · GW13: Davis → Silva**

- Klubber etter: BOU 3 · BHA 2 · MUN 2 · TOT 2 · ARS 1 · COV 1 · EVE 1 · LEE 1 · MCI 1 · SUN 1
- Keeper- og forsvarsbudsjett (nåpris): £32.1m → £34.4m. Flytter det mer enn £1,0m, er det en strukturendring (CLAUDE.md).
- Bank: £2.5m → £1.3m etter GW12 → £0.2m etter GW13
- Endring per runde: GW12 +1.15, GW13 +0.47, GW14 +2.60, GW15 +0.07, GW16 +2.77

**GW12: Davis → De Cuyper · GW13: Diop → Konsa**

- Klubber etter: BHA 3 · ARS 2 · BOU 2 · MUN 2 · TOT 2 · COV 1 · EVE 1 · MCI 1 · SUN 1
- Keeper- og forsvarsbudsjett (nåpris): £32.1m → £34.6m. Flytter det mer enn £1,0m, er det en strukturendring (CLAUDE.md).
- Bank: £2.5m → £1.0m etter GW12 → £0.0m etter GW13
- Endring per runde: GW12 +1.33, GW13 +0.40, GW14 +1.49, GW15 +1.10, GW16 +2.51

## Spillere inn i planene over

Flaggene kommer fra `forventning.py`. Én kamp som bærer xGI-en, slår ut i robust endring.

| Spiller | Lag | Pos | Pris | Eid | Sum GW12–16 | Robust | P(spiller) GW12 | Flagg |
|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | £5.1m | 7.2 % | 16.42 | 16.41 | 0.91 | — |
| De Cuyper | BHA | DEF | £5.5m | 49.9 % | 19.36 | 16.53 | 0.91 | — |
| Murillo | NFO | DEF | £5.5m | 1.9 % | 19.27 | 18.79 | 0.91 | — |
| Silva | BOU | DEF | £5.1m | 4.0 % | 18.86 | 17.67 | 0.91 | — |
| Muharemović | LEE | DEF | £5.1m | 7.0 % | 17.98 | 17.33 | 0.91 | — |
| Vuskovic | BHA | DEF | £5.3m | 11.5 % | 17.71 | 17.12 | 0.91 | — |
| Konsa | ARS | DEF | £4.9m | 25.5 % | 17.12 | 16.49 | 0.88 | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Bogle | LEE | DEF | £4.8m | 11.6 % | 17.05 | 15.46 | 0.91 | — |
| Gibbs-White | NFO | MID | £7.8m | 8.8 % | 22.79 | 21.82 | 0.91 | første straffeskytter (penalties_order 1) |
| Ødegaard | ARS | MID | £6.7m | 16.7 % | 20.60 | 18.45 | 0.91 | — |
| Isak | LIV | FWD | £9.3m | 26.6 % | 20.72 | 19.72 | 0.84 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |
| N.Jackson | AVL | FWD | £7.2m | 36.1 % | 20.07 | 18.22 | 0.91 | — |

## Søkets omfang og forutsetninger

- Kandidater per posisjon: GKP 25, DEF 25, MID 25, FWD 25 (25 beste på forventning, 10 beste per million).
- 375 enkeltbytter vurdert i hver runde. Utvalg for kombinasjoner: 109 i GW12, 110 i GW13. Søket er ikke uttømmende for kombinasjoner.
- Priser er dagens. Prisendringer før byttet er ikke modellert.
- De operative reglene i `arkiv/01` (template i premiumslottene, differensialer bare mellom £4,0m og £5,5m og maks tre samtidig, ett bytte per runde) er ikke modellert. Eierandelen står i tabellene; sjekk reglene for spillerne som kommer inn.
- Bytter i tredje runde og senere er ikke med. En plan som sparer, har verdi utover horisonten som tabellen ikke viser.
- I tilbaketesten avviker realiserte poeng over fem runder i snitt 5–6 poeng per spiller fra forventningen. En planforskjell på noen få poeng er en svak preferanse, ikke en dom.

