# Byttepakker — generert

*Generert 31.10.2026 kl. 18:33 UTC av `scripts/bytter.py` fra `fpl-data`. **Rør ikke fila for hånd.** Horisont GW10–14. Bytter vurderes i GW10 og GW11. Maks minuspoeng per runde: 0.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–8 summerer til sesongtotalene for 188 spillere, 19 felt; 481 spillere på lag som har spilt i GW9 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 31.10.2026 17:16 UTC, 1.3 t gammelt ved kjøring
- ✅ Bytteregler i API-et stemmer med 05 og skriptet: maks 3 per klubb, maks 5 frikjøp, halve prisstigningen ved salg, tropp på 15
- ✅ Bank regnet fra 8 overganger stemmer med historikken i alle 9 runder
- ✅ Frikjøp til GW10: 1. Kostnaden i hver runde stemmer med historikken

**Frikjøp, runde for runde:** GW1: første runde → 1 · GW2: 1 frikjøp, 0 brukt → 2 · GW3: 2 frikjøp, 0 brukt → 3 · GW4: 3 frikjøp, 2 brukt → 2 · GW5: 2 frikjøp, 0 brukt → 3 · GW6: 3 frikjøp, 1 brukt → 3 · GW7: 3 frikjøp, 3 brukt → 1 · GW8: 1 frikjøp, 0 brukt → 2 · GW9: 2 frikjøp, 2 brukt → 1

## Troppen inn i GW10

Bank **£4.7m**, frikjøp **1**. Salgspris etter regelen i `05`.

| Spiller | Lag | Pos | Nå | Kjøpt | Salgspris | Sum GW10–14 | Robust | P(spiller) GW10 | Eid |
|---|---|---|---|---|---|---|---|---|---|
| Kinsky | TOT | GKP | £4.4m | £4.5m | £4.4m | 13.88 | 13.89 | 0.91 | 15.3 % |
| Verbruggen | BHA | GKP | £4.6m | £4.5m | £4.5m | 13.34 | 13.00 | 0.91 | 22.5 % |
| Calafiori | ARS | DEF | £5.9m | £5.5m | £5.7m | 15.81 | 15.04 | 0.68 | 48.1 % |
| Davis | IPS | DEF | £4.0m | £4.0m | £4.0m | 14.85 | 13.78 | 0.91 | 7.1 % |
| Thomas (COV) | COV | DEF | £4.0m | £4.0m | £4.0m | 14.60 | 14.05 | 0.46 | 8.5 % |
| Diop | IPS | DEF | £3.9m | £4.0m | £3.9m | 14.17 | 14.05 | 0.91 | 10.3 % |
| Egan | HUL | DEF | £4.1m | £4.1m | £4.1m | 13.62 | 13.38 | 0.91 | 7.3 % |
| Mbeumo | MUN | MID | £7.9m | £8.0m | £7.9m | 24.69 | 21.14 | 0.91 | 21.1 % |
| Tavernier | BOU | MID | £6.5m | £6.4m | £6.4m | 23.22 | 20.92 | 0.91 | 25.6 % |
| B.Fernandes | MUN | MID | £11.7m | £12.0m | £11.7m | 19.85 | 15.68 | 0.67 | 22.4 % |
| Groß | BHA | MID | £6.2m | £6.1m | £6.1m | 19.17 | 17.46 | 0.91 | 46.7 % |
| Slater | HUL | MID | £4.5m | £4.5m | £4.5m | 11.51 | 10.99 | 0.91 | 4.5 % |
| Haaland | MCI | FWD | £15.8m | £15.5m | £15.6m | 27.53 | 26.03 | 0.91 | 78.9 % |
| Barry | EVE | FWD | £5.6m | £5.7m | £5.6m | 22.32 | 19.91 | 0.91 | 7.4 % |
| Evanilson | BOU | FWD | £6.3m | £6.3m | £6.3m | 20.67 | 18.13 | 0.91 | 14.8 % |

## Spar — ingen bytter

Lagets forventede poeng: **269.13** over horisonten (robust 245.67). Per runde: GW10 53.89, GW11 54.56, GW12 52.54, GW13 54.17, GW14 53.98.

GW10: elleveren 44.29 + kapteinsledd 6.13 (Haaland, vise Mbeumo) + innbytterledd 3.47. Benk: Verbruggen, Egan, Slater, Thomas (COV).

## Beste planer (40780 lovlige av 48982 vurderte)

Endring = forventede poeng mot å spare, over hele horisonten, etter minuspoeng.

| Plan | Minus | Endring GW10–14 | Robust endring | Endring GW10 | Bank etter GW10 | Bank etter GW11 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| GW10: Egan → Silva · GW11: Slater → Gibbs-White | 0 | **+10.77** | +9.51 | +1.42 | £3.8m | £0.4m | BOU |
| GW10: Diop → Silva · GW11: Slater → Gibbs-White | 0 | **+10.58** | +9.32 | +1.34 | £3.6m | £0.2m | BOU |
| GW10: Slater → Gibbs-White · GW11: Egan → Silva | 0 | **+10.52** | +9.58 | +1.17 | £1.3m | £0.4m | BOU |
| GW10: Slater → Gibbs-White · GW11: Diop → Silva | 0 | **+10.41** | +9.48 | +1.17 | £1.3m | £0.2m | BOU |
| GW10: Slater → Gibbs-White · GW11: Davis → Silva | 0 | **+10.09** | +9.62 | +1.17 | £1.3m | £0.3m | BOU |
| GW10: Davis → Silva · GW11: Slater → Gibbs-White | 0 | **+10.07** | +9.48 | +1.15 | £3.7m | £0.3m | BOU |
| GW10: Egan → Gabriel · GW11: Calafiori → Silva | 0 | **+9.94** | +8.79 | +2.46 | £0.8m | £1.5m | BOU |
| GW10: Diop → Gabriel · GW11: Calafiori → Silva | 0 | **+9.67** | +8.57 | +2.38 | £0.6m | £1.3m | BOU |
| GW10: Thomas (COV) → Silva · GW11: Slater → Gibbs-White | 0 | **+9.67** | +8.66 | +1.70 | £3.7m | £0.3m | BOU |
| GW10: Egan → Gabriel · GW11: Slater → Rudoni | 0 | **+9.58** | +8.53 | +2.46 | £0.8m | £0.4m | — |
| GW10: Egan → Silva · GW11: Slater → Ødegaard | 0 | **+9.51** | +6.88 | +1.42 | £3.8m | £1.6m | BOU |
| GW10: Diop → Gabriel · GW11: Slater → Rudoni | 0 | **+9.41** | +8.34 | +2.38 | £0.6m | £0.2m | — |
| GW10: Slater → Ødegaard · GW11: Egan → Silva | 0 | **+9.38** | +6.88 | +1.29 | £2.5m | £1.6m | BOU |
| GW11: Slater → Gibbs-White, Egan → Silva | 0 | **+9.35** | +8.36 | +0.00 | £4.7m | £0.4m | BOU |
| GW10: Diop → Silva · GW11: Slater → Ødegaard | 0 | **+9.34** | +6.69 | +1.34 | £3.6m | £1.4m | BOU |

## Beste plan som selger hver spiller

Svarer på «bør X selges?»: den beste lovlige planen der spilleren går ut, mot å spare.

| Plan | Minus | Endring GW10–14 | Robust endring | Endring GW10 | Bank etter GW10 | Bank etter GW11 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| **Kinsky ut:** GW10: Egan → Gabriel · GW11: Kinsky → Trafford | 0 | **+9.12** | +8.54 | +2.46 | £0.8m | £0.2m | — |
| **Verbruggen ut:** GW10: Egan → Gabriel · GW11: Verbruggen → Trafford | 0 | **+9.18** | +8.62 | +2.46 | £0.8m | £0.3m | — |
| **Calafiori ut:** GW10: Egan → Gabriel · GW11: Calafiori → Silva | 0 | **+9.94** | +8.79 | +2.46 | £0.8m | £1.5m | BOU |
| **Davis ut:** GW10: Slater → Gibbs-White · GW11: Davis → Silva | 0 | **+10.09** | +9.62 | +1.17 | £1.3m | £0.3m | BOU |
| **Thomas (COV) ut:** GW10: Thomas (COV) → Silva · GW11: Slater → Gibbs-White | 0 | **+9.67** | +8.66 | +1.70 | £3.7m | £0.3m | BOU |
| **Diop ut:** GW10: Diop → Silva · GW11: Slater → Gibbs-White | 0 | **+10.58** | +9.32 | +1.34 | £3.6m | £0.2m | BOU |
| **Egan ut:** GW10: Egan → Silva · GW11: Slater → Gibbs-White | 0 | **+10.77** | +9.51 | +1.42 | £3.8m | £0.4m | BOU |
| **Mbeumo ut:** GW10: Egan → Gabriel · GW11: Mbeumo → Gibbs-White | 0 | **+4.60** | +6.96 | +2.46 | £0.8m | £0.8m | — |
| **Tavernier ut:** GW10: Egan → Gabriel · GW11: Tavernier → Ødegaard | 0 | **+5.43** | +4.65 | +2.46 | £0.8m | £0.5m | ARS |
| **B.Fernandes ut:** GW10: Egan → Gabriel · GW11: B.Fernandes → Gibbs-White | 0 | **+7.12** | +9.69 | +2.46 | £0.8m | £4.6m | — |
| **Groß ut:** GW10: Egan → Gabriel · GW11: Groß → Ødegaard | 0 | **+8.81** | +7.52 | +2.46 | £0.8m | £0.2m | ARS |
| **Slater ut:** GW10: Egan → Silva · GW11: Slater → Gibbs-White | 0 | **+10.77** | +9.51 | +1.42 | £3.8m | £0.4m | BOU |
| **Haaland ut:** GW10: Egan → Gabriel · GW11: Haaland → Thiago | 0 | **-0.17** | -1.17 | +2.46 | £0.8m | £8.6m | — |
| **Barry ut:** GW10: Egan → Silva · GW11: Barry → Thiago | 0 | **+5.20** | +4.90 | +1.42 | £3.8m | £1.6m | BOU |
| **Evanilson ut:** GW10: Egan → Silva · GW11: Evanilson → Thiago | 0 | **+6.22** | +6.07 | +1.42 | £3.8m | £2.3m | — |

## Anti-drift for de tre beste planene

**GW10: Egan → Silva · GW11: Slater → Gibbs-White**

- Klubber etter: BOU 3 · BHA 2 · IPS 2 · MUN 2 · ARS 1 · COV 1 · EVE 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £31.8m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £3.8m etter GW10 → £0.4m etter GW11
- Endring per runde: GW10 +1.42, GW11 +1.85, GW12 +2.14, GW13 +2.00, GW14 +3.36

**GW10: Diop → Silva · GW11: Slater → Gibbs-White**

- Klubber etter: BOU 3 · BHA 2 · MUN 2 · ARS 1 · COV 1 · EVE 1 · HUL 1 · IPS 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £32.0m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £3.6m etter GW10 → £0.2m etter GW11
- Endring per runde: GW10 +1.34, GW11 +1.80, GW12 +2.09, GW13 +2.01, GW14 +3.34

**GW10: Slater → Gibbs-White · GW11: Egan → Silva**

- Klubber etter: BOU 3 · BHA 2 · IPS 2 · MUN 2 · ARS 1 · COV 1 · EVE 1 · MCI 1 · NFO 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £30.9m → £31.8m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £4.7m → £1.3m etter GW10 → £0.4m etter GW11
- Endring per runde: GW10 +1.17, GW11 +1.85, GW12 +2.14, GW13 +2.00, GW14 +3.36

## Spillere inn i planene over

Flaggene kommer fra `forventning.py`. Én kamp som bærer xGI-en, slår ut i robust endring.

| Spiller | Lag | Pos | Pris | Eid | Sum GW10–14 | Robust | P(spiller) GW10 | Flagg |
|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | £5.0m | 6.3 % | 16.44 | 16.43 | 0.91 | — |
| Gabriel | ARS | DEF | £8.0m | 23.9 % | 21.41 | 20.57 | 0.91 | — |
| Silva | BOU | DEF | £5.0m | 2.0 % | 19.50 | 18.04 | 0.91 | — |
| Ødegaard | ARS | MID | £6.7m | 16.8 % | 21.25 | 18.65 | 0.91 | — |
| Gibbs-White | NFO | MID | £7.9m | 11.3 % | 19.93 | 19.03 | 0.74 | UAVKLART FRAVÆR GW7 — telt som ikke-start; før årsaken i context/fravaer.csv · første straffeskytter (penalties_order 1) |
| Rudoni | COV | MID | £4.9m | 0.7 % | 18.04 | 16.52 | 0.91 | første straffeskytter (penalties_order 1) |
| Thiago | BRE | FWD | £7.8m | 9.2 % | 21.45 | 20.34 | 0.91 | første straffeskytter (penalties_order 1) |

## Søkets omfang og forutsetninger

- Kandidater per posisjon: GKP 25, DEF 26, MID 25, FWD 25 (25 beste på forventning, 10 beste per million).
- 380 enkeltbytter vurdert i hver runde. Utvalg for kombinasjoner: 107 i GW10, 107 i GW11. Søket er ikke uttømmende for kombinasjoner.
- Priser er dagens. Prisendringer før byttet er ikke modellert.
- De operative reglene i `01` (template i premiumslottene, differensialer bare mellom £4,0m og £5,5m og maks tre samtidig, ett bytte per runde) er ikke modellert. Eierandelen står i tabellene; sjekk reglene for spillerne som kommer inn.
- Bytter i tredje runde og senere er ikke med. En plan som sparer, har verdi utover horisonten som tabellen ikke viser.
- I tilbaketesten avviker realiserte poeng over fem runder i snitt 5–6 poeng per spiller fra forventningen. En planforskjell på noen få poeng er en svak preferanse, ikke en dom.

