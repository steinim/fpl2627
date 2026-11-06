# Byttepakker — generert

*Generert 06.11.2026 kl. 17:21 UTC av `scripts/bytter.py` fra `fpl-data`. **Rør ikke fila for hånd.** Horisont GW10–14. Bytter vurderes i GW10 og GW11. Maks minuspoeng per runde: 0.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–9 summerer til sesongtotalene for alle 670 spillere, 19 felt
- ✅ Speilet hentet 06.11.2026 08:29 UTC, 8.9 t gammelt ved kjøring
- ✅ Bytteregler i API-et stemmer med 05 og skriptet: maks 3 per klubb, maks 5 frikjøp, halve prisstigningen ved salg, tropp på 15
- ✅ Bank regnet fra 8 overganger stemmer med historikken i alle 9 runder
- ✅ Frikjøp til GW10: 1. Kostnaden i hver runde stemmer med historikken

**Frikjøp, runde for runde:** GW1: første runde → 1 · GW2: 1 frikjøp, 0 brukt → 2 · GW3: 2 frikjøp, 0 brukt → 3 · GW4: 3 frikjøp, 2 brukt → 2 · GW5: 2 frikjøp, 0 brukt → 3 · GW6: 3 frikjøp, 1 brukt → 3 · GW7: 3 frikjøp, 3 brukt → 1 · GW8: 1 frikjøp, 0 brukt → 2 · GW9: 2 frikjøp, 2 brukt → 1

## Troppen inn i GW10

Bank **£4.7m**, frikjøp **1**. Salgspris etter regelen i `05`.

| Spiller | Lag | Pos | Nå | Kjøpt | Salgspris | Sum GW10–14 | Robust | P(spiller) GW10 | Eid |
|---|---|---|---|---|---|---|---|---|---|
| Verbruggen | BHA | GKP | £4.6m | £4.5m | £4.5m | 14.68 | 14.37 | 0.93 | 23.3 % |
| Kinsky | TOT | GKP | £4.4m | £4.5m | £4.4m | 13.93 | 13.94 | 0.93 | 15.5 % |
| Calafiori | ARS | DEF | £5.9m | £5.5m | £5.7m | 17.36 | 16.52 | 0.93 | 48.2 % |
| Thomas (COV) | COV | DEF | £4.0m | £4.0m | £4.0m | 14.91 | 14.32 | 0.47 | 7.9 % |
| Davis | IPS | DEF | £4.0m | £4.0m | £4.0m | 14.65 | 13.63 | 0.93 | 6.8 % |
| Diop | IPS | DEF | £3.9m | £4.0m | £3.9m | 14.46 | 14.35 | 0.93 | 10.1 % |
| Egan | HUL | DEF | £4.1m | £4.1m | £4.1m | 13.32 | 13.12 | 0.93 | 6.9 % |
| Mbeumo | MUN | MID | £7.9m | £8.0m | £7.9m | 24.49 | 21.10 | 0.93 | 20.1 % |
| Tavernier | BOU | MID | £6.6m | £6.4m | £6.5m | 22.54 | 20.36 | 0.93 | 28.8 % |
| B.Fernandes | MUN | MID | £11.7m | £12.0m | £11.7m | 21.16 | 17.05 | 0.74 | 21.2 % |
| Groß | BHA | MID | £6.2m | £6.1m | £6.1m | 18.39 | 16.76 | 0.93 | 47.0 % |
| Slater | HUL | MID | £4.5m | £4.5m | £4.5m | 11.61 | 11.13 | 0.93 | 4.4 % |
| Haaland | MCI | FWD | £15.8m | £15.5m | £15.6m | 27.12 | 25.68 | 0.93 | 79.1 % |
| Barry | EVE | FWD | £5.6m | £5.7m | £5.6m | 25.16 | 23.13 | 0.93 | 8.0 % |
| Evanilson | BOU | FWD | £6.4m | £6.3m | £6.3m | 21.25 | 18.91 | 0.93 | 19.7 % |

## Spar — ingen bytter

Lagets forventede poeng: **271.07** over horisonten (robust 249.10). Per runde: GW10 55.37, GW11 54.72, GW12 52.75, GW13 54.32, GW14 53.91.

GW10: elleveren 46.94 + kapteinsledd 6.04 (Barry, vise Haaland) + innbytterledd 2.39. Benk: Kinsky, Egan, Slater, Thomas (COV).

## Beste planer (41910 lovlige av 50651 vurderte)

Endring = forventede poeng mot å spare, over hele horisonten, etter minuspoeng.

| Plan | Minus | Endring GW10–14 | Robust endring | Endring GW10 | Bank etter GW10 | Bank etter GW11 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| GW10: Slater → Gibbs-White · GW11: Egan → Silva | 0 | **+11.98** | +11.00 | +1.73 | £1.4m | £0.4m | BOU |
| GW10: Slater → Gibbs-White · GW11: Diop → Silva | 0 | **+11.80** | +10.64 | +1.73 | £1.4m | £0.2m | BOU |
| GW10: Slater → Gibbs-White · GW11: Davis → Silva | 0 | **+11.75** | +10.94 | +1.73 | £1.4m | £0.3m | BOU |
| GW10: Egan → Silva · GW11: Slater → Gibbs-White | 0 | **+11.67** | +10.91 | +1.43 | £3.7m | £0.4m | BOU |
| GW10: Slater → Gibbs-White · GW11: Egan → Van Hecke | 0 | **+11.47** | +10.09 | +1.73 | £1.4m | £0.5m | — |
| GW10: Diop → Silva · GW11: Slater → Gibbs-White | 0 | **+11.32** | +10.33 | +1.25 | £3.5m | £0.2m | BOU |
| GW10: Slater → Gibbs-White · GW11: Diop → Van Hecke | 0 | **+11.29** | +9.73 | +1.73 | £1.4m | £0.3m | — |
| GW10: Slater → Gibbs-White · GW11: Davis → Van Hecke | 0 | **+11.24** | +10.03 | +1.73 | £1.4m | £0.4m | — |
| GW10: Davis → Silva · GW11: Slater → Gibbs-White | 0 | **+11.19** | +10.74 | +1.17 | £3.6m | £0.3m | BOU |
| GW10: Slater → Gibbs-White · GW11: Egan → Murillo | 0 | **+11.15** | +10.86 | +1.73 | £1.4m | £0.0m | — |
| GW10: Slater → Gibbs-White · GW11: Egan → De Cuyper | 0 | **+10.94** | +8.90 | +1.73 | £1.4m | £0.1m | BHA |
| GW10: Egan → Van Hecke · GW11: Slater → Gibbs-White | 0 | **+10.82** | +9.60 | +1.09 | £3.8m | £0.5m | — |
| GW10: Slater → Gibbs-White · GW11: Davis → De Cuyper | 0 | **+10.72** | +8.84 | +1.73 | £1.4m | £0.0m | BHA |
| GW10: Slater → Gibbs-White · GW11: Egan → Muharemović | 0 | **+10.64** | +10.19 | +1.73 | £1.4m | £0.4m | — |
| GW10: Slater → Gibbs-White · GW11: Egan → Vuskovic | 0 | **+10.49** | +10.12 | +1.73 | £1.4m | £0.3m | BHA |

## Beste plan som selger hver spiller

Svarer på «bør X selges?»: den beste lovlige planen der spilleren går ut, mot å spare.

| Plan | Minus | Endring GW10–14 | Robust endring | Endring GW10 | Bank etter GW10 | Bank etter GW11 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| **Verbruggen ut:** GW10: Slater → Gibbs-White · GW11: Verbruggen → Trafford | 0 | **+9.15** | +9.08 | +1.73 | £1.4m | £0.9m | — |
| **Kinsky ut:** GW10: Slater → Gibbs-White · GW11: Kinsky → Trafford | 0 | **+9.24** | +9.12 | +1.73 | £1.4m | £0.8m | — |
| **Calafiori ut:** GW10: Slater → Gibbs-White · GW11: Calafiori → Silva | 0 | **+10.29** | +9.59 | +1.73 | £1.4m | £2.0m | BOU |
| **Thomas (COV) ut:** GW10: Slater → Gibbs-White · GW11: Thomas (COV) → Silva | 0 | **+10.36** | +9.54 | +1.73 | £1.4m | £0.3m | BOU |
| **Davis ut:** GW10: Slater → Gibbs-White · GW11: Davis → Silva | 0 | **+11.75** | +10.94 | +1.73 | £1.4m | £0.3m | BOU |
| **Diop ut:** GW10: Slater → Gibbs-White · GW11: Diop → Silva | 0 | **+11.80** | +10.64 | +1.73 | £1.4m | £0.2m | BOU |
| **Egan ut:** GW10: Slater → Gibbs-White · GW11: Egan → Silva | 0 | **+11.98** | +11.00 | +1.73 | £1.4m | £0.4m | BOU |
| **Mbeumo ut:** GW10: Egan → Gabriel · GW11: Mbeumo → Gibbs-White | 0 | **+6.75** | +8.56 | +2.48 | £0.8m | £0.9m | — |
| **Tavernier ut:** GW10: Slater → Gibbs-White · GW11: Tavernier → E.Le Fée | 0 | **+7.61** | +7.29 | +1.73 | £1.4m | £2.2m | — |
| **B.Fernandes ut:** GW10: Egan → Gabriel · GW11: B.Fernandes → Gibbs-White | 0 | **+7.66** | +10.02 | +2.48 | £0.8m | £4.7m | — |
| **Groß ut:** GW10: Slater → Gibbs-White · GW11: Groß → E.Le Fée | 0 | **+10.42** | +9.47 | +1.73 | £1.4m | £1.8m | — |
| **Slater ut:** GW10: Slater → Gibbs-White · GW11: Egan → Silva | 0 | **+11.98** | +11.00 | +1.73 | £1.4m | £0.4m | BOU |
| **Haaland ut:** GW10: Slater → Gibbs-White · GW11: Haaland → Isak | 0 | **+1.54** | +1.55 | +1.73 | £1.4m | £7.8m | — |
| **Barry ut:** GW10: Slater → E.Le Fée · GW11: Barry → Thiago | 0 | **+4.00** | +2.62 | +1.66 | £3.5m | £1.3m | — |
| **Evanilson ut:** GW10: Slater → E.Le Fée · GW11: Evanilson → Isak | 0 | **+7.10** | +6.39 | +1.66 | £3.5m | £0.6m | — |

## Anti-drift for de tre beste planene

**GW10: Slater → Gibbs-White · GW11: Egan → Silva**

- Klubber etter: BOU 3 · BHA 2 · IPS 2 · MUN 2 · ARS 1 · COV 1 · EVE 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £31.9m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £1.4m etter GW10 → £0.4m etter GW11
- Endring per runde: GW10 +1.73, GW11 +2.01, GW12 +2.23, GW13 +2.29, GW14 +3.71

**GW10: Slater → Gibbs-White · GW11: Diop → Silva**

- Klubber etter: BOU 3 · BHA 2 · MUN 2 · ARS 1 · COV 1 · EVE 1 · HUL 1 · IPS 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £32.1m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £1.4m etter GW10 → £0.2m etter GW11
- Endring per runde: GW10 +1.73, GW11 +1.97, GW12 +2.19, GW13 +2.26, GW14 +3.64

**GW10: Slater → Gibbs-White · GW11: Davis → Silva**

- Klubber etter: BOU 3 · BHA 2 · MUN 2 · ARS 1 · COV 1 · EVE 1 · HUL 1 · IPS 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £32.0m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £1.4m etter GW10 → £0.3m etter GW11
- Endring per runde: GW10 +1.73, GW11 +1.99, GW12 +2.12, GW13 +2.24, GW14 +3.66

## Spillere inn i planene over

Flaggene kommer fra `forventning.py`. Én kamp som bærer xGI-en, slår ut i robust endring.

| Spiller | Lag | Pos | Pris | Eid | Sum GW10–14 | Robust | P(spiller) GW10 | Flagg |
|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | £5.0m | 6.3 % | 16.40 | 16.39 | 0.93 | — |
| Gabriel | ARS | DEF | £8.0m | 25.0 % | 21.15 | 20.32 | 0.93 | — |
| Silva | BOU | DEF | £5.1m | 3.0 % | 19.51 | 18.13 | 0.93 | — |
| Van Hecke | TOT | DEF | £5.0m | 12.1 % | 18.66 | 16.82 | 0.93 | — |
| Murillo | NFO | DEF | £5.5m | 2.0 % | 18.30 | 17.80 | 0.93 | — |
| De Cuyper | BHA | DEF | £5.4m | 45.7 % | 18.26 | 15.10 | 0.93 | én kamp (GW1) står for 53% av xGI |
| Muharemović | LEE | DEF | £5.1m | 6.1 % | 18.15 | 17.44 | 0.93 | — |
| Vuskovic | BHA | DEF | £5.2m | 7.6 % | 17.61 | 16.98 | 0.93 | — |
| Gibbs-White | NFO | MID | £7.8m | 10.1 % | 23.71 | 22.71 | 0.93 | første straffeskytter (penalties_order 1) |
| E.Le Fée | SUN | MID | £5.7m | 2.7 % | 22.13 | 19.81 | 0.93 | — |
| Thiago | BRE | FWD | £7.8m | 9.1 % | 21.39 | 20.25 | 0.93 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | £9.2m | 22.7 % | 20.80 | 19.77 | 0.83 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |

## Søkets omfang og forutsetninger

- Kandidater per posisjon: GKP 25, DEF 25, MID 25, FWD 25 (25 beste på forventning, 10 beste per million).
- 375 enkeltbytter vurdert i hver runde. Utvalg for kombinasjoner: 111 i GW10, 111 i GW11. Søket er ikke uttømmende for kombinasjoner.
- Priser er dagens. Prisendringer før byttet er ikke modellert.
- De operative reglene i `01` (template i premiumslottene, differensialer bare mellom £4,0m og £5,5m og maks tre samtidig, ett bytte per runde) er ikke modellert. Eierandelen står i tabellene; sjekk reglene for spillerne som kommer inn.
- Bytter i tredje runde og senere er ikke med. En plan som sparer, har verdi utover horisonten som tabellen ikke viser.
- I tilbaketesten avviker realiserte poeng over fem runder i snitt 5–6 poeng per spiller fra forventningen. En planforskjell på noen få poeng er en svak preferanse, ikke en dom.

