# Byttepakker — generert

*Generert 03.11.2026 kl. 20:30 UTC av `scripts/bytter.py` fra `fpl-data`. **Rør ikke fila for hånd.** Horisont GW10–14. Bytter vurderes i GW10 og GW11. Maks minuspoeng per runde: 0.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–9 summerer til sesongtotalene for alle 670 spillere, 19 felt
- ✅ Speilet hentet 03.11.2026 20:16 UTC, 0.2 t gammelt ved kjøring
- ✅ Bytteregler i API-et stemmer med 05 og skriptet: maks 3 per klubb, maks 5 frikjøp, halve prisstigningen ved salg, tropp på 15
- ✅ Bank regnet fra 8 overganger stemmer med historikken i alle 9 runder
- ✅ Frikjøp til GW10: 1. Kostnaden i hver runde stemmer med historikken

**Frikjøp, runde for runde:** GW1: første runde → 1 · GW2: 1 frikjøp, 0 brukt → 2 · GW3: 2 frikjøp, 0 brukt → 3 · GW4: 3 frikjøp, 2 brukt → 2 · GW5: 2 frikjøp, 0 brukt → 3 · GW6: 3 frikjøp, 1 brukt → 3 · GW7: 3 frikjøp, 3 brukt → 1 · GW8: 1 frikjøp, 0 brukt → 2 · GW9: 2 frikjøp, 2 brukt → 1

## Troppen inn i GW10

Bank **£4.7m**, frikjøp **1**. Salgspris etter regelen i `05`.

| Spiller | Lag | Pos | Nå | Kjøpt | Salgspris | Sum GW10–14 | Robust | P(spiller) GW10 | Eid |
|---|---|---|---|---|---|---|---|---|---|
| Verbruggen | BHA | GKP | £4.6m | £4.5m | £4.5m | 14.68 | 14.37 | 0.93 | 23.1 % |
| Kinsky | TOT | GKP | £4.4m | £4.5m | £4.4m | 13.93 | 13.94 | 0.93 | 15.4 % |
| Calafiori | ARS | DEF | £5.9m | £5.5m | £5.7m | 17.36 | 16.52 | 0.93 | 47.9 % |
| Davis | IPS | DEF | £4.0m | £4.0m | £4.0m | 14.65 | 13.63 | 0.93 | 6.9 % |
| Diop | IPS | DEF | £3.9m | £4.0m | £3.9m | 14.46 | 14.35 | 0.93 | 10.2 % |
| Egan | HUL | DEF | £4.1m | £4.1m | £4.1m | 13.32 | 13.12 | 0.93 | 7.0 % |
| Thomas (COV) | COV | DEF | £4.0m | £4.0m | £4.0m | 11.53 | 11.08 | 0.33 | 8.2 % |
| Mbeumo | MUN | MID | £7.9m | £8.0m | £7.9m | 24.49 | 21.10 | 0.93 | 20.4 % |
| Tavernier | BOU | MID | £6.6m | £6.4m | £6.5m | 22.54 | 20.36 | 0.93 | 27.6 % |
| B.Fernandes | MUN | MID | £11.7m | £12.0m | £11.7m | 21.16 | 17.05 | 0.74 | 21.6 % |
| Groß | BHA | MID | £6.2m | £6.1m | £6.1m | 18.39 | 16.76 | 0.93 | 46.9 % |
| Slater | HUL | MID | £4.5m | £4.5m | £4.5m | 11.61 | 11.13 | 0.93 | 4.4 % |
| Haaland | MCI | FWD | £15.8m | £15.5m | £15.6m | 27.12 | 25.68 | 0.93 | 79.0 % |
| Barry | EVE | FWD | £5.6m | £5.7m | £5.6m | 25.16 | 23.13 | 0.93 | 7.6 % |
| Evanilson | BOU | FWD | £6.4m | £6.3m | £6.3m | 21.25 | 18.91 | 0.93 | 18.0 % |

## Spar — ingen bytter

Lagets forventede poeng: **269.08** over horisonten (robust 247.23). Per runde: GW10 55.33, GW11 54.02, GW12 52.41, GW13 53.73, GW14 53.59.

GW10: elleveren 46.94 + kapteinsledd 6.04 (Barry, vise Haaland) + innbytterledd 2.35. Benk: Kinsky, Egan, Slater, Thomas (COV).

## Beste planer (41838 lovlige av 50741 vurderte)

Endring = forventede poeng mot å spare, over hele horisonten, etter minuspoeng.

| Plan | Minus | Endring GW10–14 | Robust endring | Endring GW10 | Bank etter GW10 | Bank etter GW11 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| GW10: Thomas (COV) → Silva · GW11: Slater → Gibbs-White | 0 | **+11.15** | +10.18 | +1.58 | £3.7m | £0.3m | BOU |
| GW10: Slater → Gibbs-White · GW11: Thomas (COV) → Silva | 0 | **+11.00** | +9.88 | +1.43 | £1.3m | £0.3m | BOU |
| GW10: Slater → Gibbs-White · GW11: Egan → Silva | 0 | **+10.90** | +9.73 | +1.43 | £1.3m | £0.4m | BOU |
| GW10: Egan → Silva · GW11: Slater → Gibbs-White | 0 | **+10.90** | +9.87 | +1.43 | £3.8m | £0.4m | BOU |
| GW10: Slater → E.Le Fée · GW11: Thomas (COV) → Silva | 0 | **+10.72** | +8.20 | +1.66 | £3.5m | £2.5m | BOU |
| GW10: Thomas (COV) → Silva · GW11: Slater → E.Le Fée | 0 | **+10.64** | +8.66 | +1.58 | £3.7m | £2.5m | BOU |
| GW10: Slater → E.Le Fée · GW11: Egan → Silva | 0 | **+10.63** | +8.07 | +1.66 | £3.5m | £2.6m | BOU |
| GW10: Slater → Gibbs-White · GW11: Thomas (COV) → Van Hecke | 0 | **+10.49** | +8.97 | +1.43 | £1.3m | £0.3m | — |
| GW10: Slater → Gibbs-White · GW11: Diop → Silva | 0 | **+10.43** | +8.96 | +1.43 | £1.3m | £0.2m | BOU |
| GW10: Egan → Gabriel · GW11: Groß → E.Le Fée | 0 | **+10.40** | +9.40 | +2.48 | £0.8m | £1.2m | — |
| GW10: Egan → Silva · GW11: Slater → E.Le Fée | 0 | **+10.40** | +8.37 | +1.43 | £3.8m | £2.6m | BOU |
| GW10: Slater → Gibbs-White · GW11: Egan → Van Hecke | 0 | **+10.39** | +8.82 | +1.43 | £1.3m | £0.4m | — |
| GW10: Slater → Gibbs-White · GW11: Davis → Silva | 0 | **+10.33** | +9.56 | +1.43 | £1.3m | £0.3m | BOU |
| GW10: Thomas (COV) → Gabriel · GW11: Groß → E.Le Fée | 0 | **+10.32** | +9.44 | +2.64 | £0.7m | £1.1m | — |
| GW10: Thomas (COV) → Van Hecke · GW11: Slater → Gibbs-White | 0 | **+10.30** | +8.87 | +1.24 | £3.7m | £0.3m | — |

## Beste plan som selger hver spiller

Svarer på «bør X selges?»: den beste lovlige planen der spilleren går ut, mot å spare.

| Plan | Minus | Endring GW10–14 | Robust endring | Endring GW10 | Bank etter GW10 | Bank etter GW11 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| **Verbruggen ut:** GW10: Egan → Gabriel · GW11: Verbruggen → Trafford | 0 | **+8.56** | +8.27 | +2.48 | £0.8m | £0.3m | — |
| **Kinsky ut:** GW10: Egan → Gabriel · GW11: Kinsky → Trafford | 0 | **+8.65** | +8.30 | +2.48 | £0.8m | £0.2m | — |
| **Calafiori ut:** GW10: Egan → Gabriel · GW11: Calafiori → Silva | 0 | **+9.69** | +8.78 | +2.48 | £0.8m | £1.5m | BOU |
| **Davis ut:** GW10: Slater → Gibbs-White · GW11: Davis → Silva | 0 | **+10.33** | +9.56 | +1.43 | £1.3m | £0.3m | BOU |
| **Diop ut:** GW10: Slater → Gibbs-White · GW11: Diop → Silva | 0 | **+10.43** | +8.96 | +1.43 | £1.3m | £0.2m | BOU |
| **Egan ut:** GW10: Slater → Gibbs-White · GW11: Egan → Silva | 0 | **+10.90** | +9.73 | +1.43 | £1.3m | £0.4m | BOU |
| **Thomas (COV) ut:** GW10: Thomas (COV) → Silva · GW11: Slater → Gibbs-White | 0 | **+11.15** | +10.18 | +1.58 | £3.7m | £0.3m | BOU |
| **Mbeumo ut:** GW10: Egan → Gabriel · GW11: Mbeumo → Gibbs-White | 0 | **+6.02** | +7.53 | +2.48 | £0.8m | £0.8m | — |
| **Tavernier ut:** GW10: Egan → Gabriel · GW11: Tavernier → E.Le Fée | 0 | **+7.01** | +6.48 | +2.48 | £0.8m | £1.6m | — |
| **B.Fernandes ut:** GW10: Egan → Gabriel · GW11: B.Fernandes → Gibbs-White | 0 | **+6.84** | +8.93 | +2.48 | £0.8m | £4.6m | — |
| **Groß ut:** GW10: Egan → Gabriel · GW11: Groß → E.Le Fée | 0 | **+10.40** | +9.40 | +2.48 | £0.8m | £1.2m | — |
| **Slater ut:** GW10: Thomas (COV) → Silva · GW11: Slater → Gibbs-White | 0 | **+11.15** | +10.18 | +1.58 | £3.7m | £0.3m | BOU |
| **Haaland ut:** GW10: Egan → Gabriel · GW11: Haaland → Isak | 0 | **+0.88** | +0.49 | +2.48 | £0.8m | £7.2m | — |
| **Barry ut:** GW10: Slater → E.Le Fée · GW11: Barry → Thiago | 0 | **+3.88** | +2.45 | +1.66 | £3.5m | £1.3m | — |
| **Evanilson ut:** GW10: Slater → E.Le Fée · GW11: Evanilson → Isak | 0 | **+6.95** | +6.20 | +1.66 | £3.5m | £0.6m | — |

## Anti-drift for de tre beste planene

**GW10: Thomas (COV) → Silva · GW11: Slater → Gibbs-White**

- Klubber etter: BOU 3 · BHA 2 · IPS 2 · MUN 2 · ARS 1 · EVE 1 · HUL 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £31.9m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £3.7m etter GW10 → £0.3m etter GW11
- Endring per runde: GW10 +1.58, GW11 +1.88, GW12 +2.19, GW13 +2.01, GW14 +3.49

**GW10: Slater → Gibbs-White · GW11: Thomas (COV) → Silva**

- Klubber etter: BOU 3 · BHA 2 · IPS 2 · MUN 2 · ARS 1 · EVE 1 · HUL 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £31.9m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £1.3m etter GW10 → £0.3m etter GW11
- Endring per runde: GW10 +1.43, GW11 +1.88, GW12 +2.19, GW13 +2.01, GW14 +3.49

**GW10: Slater → Gibbs-White · GW11: Egan → Silva**

- Klubber etter: BOU 3 · BHA 2 · IPS 2 · MUN 2 · ARS 1 · COV 1 · EVE 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £31.8m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £1.3m etter GW10 → £0.4m etter GW11
- Endring per runde: GW10 +1.43, GW11 +1.87, GW12 +2.13, GW13 +2.01, GW14 +3.46

## Spillere inn i planene over

Flaggene kommer fra `forventning.py`. Én kamp som bærer xGI-en, slår ut i robust endring.

| Spiller | Lag | Pos | Pris | Eid | Sum GW10–14 | Robust | P(spiller) GW10 | Flagg |
|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | £5.0m | 6.3 % | 16.40 | 16.39 | 0.93 | — |
| Gabriel | ARS | DEF | £8.0m | 24.5 % | 21.15 | 20.32 | 0.93 | — |
| Silva | BOU | DEF | £5.0m | 2.5 % | 19.51 | 18.13 | 0.93 | — |
| Van Hecke | TOT | DEF | £5.0m | 11.2 % | 18.66 | 16.82 | 0.93 | — |
| E.Le Fée | SUN | MID | £5.7m | 2.7 % | 22.13 | 19.81 | 0.93 | — |
| Gibbs-White | NFO | MID | £7.9m | 10.7 % | 20.58 | 19.71 | 0.79 | UAVKLART FRAVÆR GW7 — telt som ikke-start; før årsaken i context/fravaer.csv · første straffeskytter (penalties_order 1) |
| Thiago | BRE | FWD | £7.8m | 9.2 % | 21.39 | 20.25 | 0.93 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | £9.2m | 21.7 % | 20.80 | 19.77 | 0.83 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |

## Søkets omfang og forutsetninger

- Kandidater per posisjon: GKP 25, DEF 25, MID 25, FWD 25 (25 beste på forventning, 10 beste per million).
- 375 enkeltbytter vurdert i hver runde. Utvalg for kombinasjoner: 111 i GW10, 111 i GW11. Søket er ikke uttømmende for kombinasjoner.
- Priser er dagens. Prisendringer før byttet er ikke modellert.
- De operative reglene i `01` (template i premiumslottene, differensialer bare mellom £4,0m og £5,5m og maks tre samtidig, ett bytte per runde) er ikke modellert. Eierandelen står i tabellene; sjekk reglene for spillerne som kommer inn.
- Bytter i tredje runde og senere er ikke med. En plan som sparer, har verdi utover horisonten som tabellen ikke viser.
- I tilbaketesten avviker realiserte poeng over fem runder i snitt 5–6 poeng per spiller fra forventningen. En planforskjell på noen få poeng er en svak preferanse, ikke en dom.

