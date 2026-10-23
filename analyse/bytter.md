# Byttepakker — generert

*Generert 23.10.2026 kl. 23:10 UTC av `scripts/bytter.py` fra `fpl-data`. **Rør ikke fila for hånd.** Horisont GW9–13. Bytter vurderes i GW9 og GW10. Maks minuspoeng per runde: 0.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–7 summerer til sesongtotalene for 602 spillere, 19 felt; 66 spillere på lag som har spilt i GW8 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 23.10.2026 22:37 UTC, 0.5 t gammelt ved kjøring
- ✅ Bytteregler i API-et stemmer med 05 og skriptet: maks 3 per klubb, maks 5 frikjøp, halve prisstigningen ved salg, tropp på 15
- ✅ Bank regnet fra 6 overganger stemmer med historikken i alle 8 runder
- ✅ Frikjøp til GW9: 2. Kostnaden i hver runde stemmer med historikken

**Frikjøp, runde for runde:** GW1: første runde → 1 · GW2: 1 frikjøp, 0 brukt → 2 · GW3: 2 frikjøp, 0 brukt → 3 · GW4: 3 frikjøp, 2 brukt → 2 · GW5: 2 frikjøp, 0 brukt → 3 · GW6: 3 frikjøp, 1 brukt → 3 · GW7: 3 frikjøp, 3 brukt → 1 · GW8: 1 frikjøp, 0 brukt → 2

## Troppen inn i GW9

Bank **£0.3m**, frikjøp **2**. Salgspris etter regelen i `05`.

| Spiller | Lag | Pos | Nå | Kjøpt | Salgspris | Sum GW9–13 | Robust | P(spiller) GW9 | Eid |
|---|---|---|---|---|---|---|---|---|---|
| Kinsky | TOT | GKP | £4.5m | £4.5m | £4.5m | 13.25 | 13.25 | 0.91 | 14.6 % |
| Verbruggen | BHA | GKP | £4.6m | £4.5m | £4.5m | 12.95 | 12.60 | 0.91 | 22.6 % |
| Calafiori | ARS | DEF | £6.0m | £5.5m | £5.7m | 19.19 | 18.22 | 0.91 | 54.8 % |
| Thomas (COV) | COV | DEF | £4.0m | £4.0m | £4.0m | 18.07 | 17.36 | 0.91 | 9.8 % |
| Davis | IPS | DEF | £4.0m | £4.0m | £4.0m | 15.62 | 14.44 | 0.91 | 7.4 % |
| Diop | IPS | DEF | £3.9m | £4.0m | £3.9m | 14.98 | 14.86 | 0.91 | 10.9 % |
| Egan | HUL | DEF | £4.1m | £4.1m | £4.1m | 13.87 | 13.60 | 0.91 | 7.2 % |
| Mbeumo | MUN | MID | £7.9m | £8.0m | £7.9m | 24.62 | 20.94 | 0.91 | 21.8 % |
| B.Fernandes | MUN | MID | £11.8m | £12.0m | £11.8m | 24.30 | 19.21 | 0.91 | 26.2 % |
| Groß | BHA | MID | £6.2m | £6.1m | £6.1m | 18.91 | 17.12 | 0.91 | 46.3 % |
| Slater | HUL | MID | £4.5m | £4.5m | £4.5m | 11.95 | 11.34 | 0.91 | 4.8 % |
| Saka | ARS | MID | £9.6m | £9.6m | £9.6m | 0.00 | 0.00 | 0.00 | 10.3 % |
| Haaland | MCI | FWD | £15.7m | £15.5m | £15.6m | 28.96 | 27.46 | 0.91 | 77.5 % |
| Barry | EVE | FWD | £5.7m | £5.7m | £5.7m | 22.06 | 19.55 | 0.91 | 7.8 % |
| João Pedro | CHE | FWD | £7.9m | £7.5m | £7.7m | 21.78 | 19.78 | 0.91 | 73.8 % |

## Spar — ingen bytter

Lagets forventede poeng: **269.89** over horisonten (robust 247.25). Per runde: GW9 55.24, GW10 55.01, GW11 53.68, GW12 52.29, GW13 53.66.

GW9: elleveren 45.59 + kapteinsledd 6.88 (Haaland, vise Mbeumo) + innbytterledd 2.77. Benk: Verbruggen, Diop, Slater, Saka.

## Beste planer (22961 lovlige av 57493 vurderte)

Endring = forventede poeng mot å spare, over hele horisonten, etter minuspoeng.

| Plan | Minus | Endring GW9–13 | Robust endring | Endring GW9 | Bank etter GW9 | Bank etter GW10 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → Silva | 0 | **+17.89** | +13.24 | +2.75 | £2.5m | £1.6m | — |
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Diop → Silva | 0 | **+17.67** | +12.92 | +2.75 | £2.5m | £1.4m | — |
| GW9: Saka → Tavernier, Egan → Silva · GW10: Slater → E.Le Fée | 0 | **+17.67** | +13.13 | +2.53 | £2.8m | £1.6m | — |
| GW9: Saka → E.Le Fée, Egan → Silva · GW10: Slater → Tavernier | 0 | **+17.56** | +12.97 | +2.41 | £3.3m | £1.6m | — |
| GW9: Saka → Tavernier, Diop → Silva · GW10: Slater → E.Le Fée | 0 | **+17.49** | +12.85 | +2.56 | £2.6m | £1.4m | — |
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → De Cuyper | 0 | **+17.43** | +11.37 | +2.75 | £2.5m | £1.3m | BHA |
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Davis → Silva | 0 | **+17.40** | +13.07 | +2.75 | £2.5m | £1.5m | — |
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → Vuskovic | 0 | **+17.40** | +13.37 | +2.75 | £2.5m | £1.5m | BHA |
| GW9: Saka → Tavernier, Egan → Silva · GW10: Slater → Ødegaard | 0 | **+17.38** | +12.74 | +2.53 | £2.8m | £0.5m | — |
| GW9: Saka → E.Le Fée, Diop → Silva · GW10: Slater → Tavernier | 0 | **+17.37** | +12.69 | +2.44 | £3.1m | £1.4m | — |
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Diop → De Cuyper | 0 | **+17.22** | +11.00 | +2.75 | £2.5m | £1.1m | BHA |
| GW9: Saka → Tavernier, Diop → Silva · GW10: Slater → Ødegaard | 0 | **+17.19** | +12.46 | +2.56 | £2.6m | £0.3m | — |
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → Murillo | 0 | **+17.19** | +13.28 | +2.75 | £2.5m | £1.1m | — |
| GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Diop → Vuskovic | 0 | **+17.18** | +13.04 | +2.75 | £2.5m | £1.3m | BHA |
| GW9: Saka → Tavernier, Davis → Silva · GW10: Slater → E.Le Fée | 0 | **+17.18** | +13.02 | +2.52 | £2.7m | £1.5m | — |

## Beste plan som selger hver spiller

Svarer på «bør X selges?»: den beste lovlige planen der spilleren går ut, mot å spare.

| Plan | Minus | Endring GW9–13 | Robust endring | Endring GW9 | Bank etter GW9 | Bank etter GW10 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| **Kinsky ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Kinsky → Raya | 0 | **+16.79** | +13.05 | +2.75 | £2.5m | £0.9m | — |
| **Verbruggen ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Verbruggen → Raya | 0 | **+16.79** | +13.08 | +2.75 | £2.5m | £0.9m | — |
| **Calafiori ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Calafiori → Gabriel | 0 | **+14.73** | +10.99 | +2.75 | £2.5m | £0.3m | — |
| **Thomas (COV) ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Thomas (COV) → Silva | 0 | **+15.60** | +11.06 | +2.75 | £2.5m | £1.5m | — |
| **Davis ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Davis → Silva | 0 | **+17.40** | +13.07 | +2.75 | £2.5m | £1.5m | — |
| **Diop ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Diop → Silva | 0 | **+17.67** | +12.92 | +2.75 | £2.5m | £1.4m | — |
| **Egan ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → Silva | 0 | **+17.89** | +13.24 | +2.75 | £2.5m | £1.6m | — |
| **Mbeumo ut:** GW9: Saka → Rogers, Slater → Tavernier · GW10: Mbeumo → E.Le Fée | 0 | **+11.85** | +10.08 | +2.77 | £0.2m | £2.4m | — |
| **B.Fernandes ut:** GW9: Saka → Rogers, Slater → Tavernier · GW10: B.Fernandes → E.Le Fée | 0 | **+12.18** | +11.67 | +2.77 | £0.2m | £6.3m | — |
| **Groß ut:** GW9: Saka → Rogers, Slater → Tavernier · GW10: Groß → E.Le Fée | 0 | **+16.16** | +13.06 | +2.77 | £0.2m | £0.6m | — |
| **Slater ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → Silva | 0 | **+17.89** | +13.24 | +2.75 | £2.5m | £1.6m | — |
| **Saka ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → Silva | 0 | **+17.89** | +13.24 | +2.75 | £2.5m | £1.6m | — |
| **Haaland ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Haaland → Isak | 0 | **+5.97** | +1.43 | +2.75 | £2.5m | £9.1m | — |
| **Barry ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Barry → Gonzalo | 0 | **+14.25** | +11.24 | +2.75 | £2.5m | £2.1m | — |
| **João Pedro ut:** GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: João Pedro → Isak | 0 | **+14.72** | +11.30 | +2.75 | £2.5m | £1.2m | — |

## Anti-drift for de tre beste planene

**GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Egan → Silva**

- Klubber etter: BHA 2 · BOU 2 · IPS 2 · MUN 2 · ARS 1 · CHE 1 · COV 1 · EVE 1 · MCI 1 · SUN 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £31.1m → £32.0m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £0.3m → £2.5m etter GW9 → £1.6m etter GW10
- Endring per runde: GW9 +2.75, GW10 +4.33, GW11 +4.02, GW12 +3.42, GW13 +3.38

**GW9: Saka → E.Le Fée, Slater → Tavernier · GW10: Diop → Silva**

- Klubber etter: BHA 2 · BOU 2 · MUN 2 · ARS 1 · CHE 1 · COV 1 · EVE 1 · HUL 1 · IPS 1 · MCI 1 · SUN 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £31.1m → £32.2m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £0.3m → £2.5m etter GW9 → £1.4m etter GW10
- Endring per runde: GW9 +2.75, GW10 +4.27, GW11 +3.96, GW12 +3.33, GW13 +3.38

**GW9: Saka → Tavernier, Egan → Silva · GW10: Slater → E.Le Fée**

- Klubber etter: BHA 2 · BOU 2 · IPS 2 · MUN 2 · ARS 1 · CHE 1 · COV 1 · EVE 1 · MCI 1 · SUN 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £31.1m → £32.0m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £0.3m → £2.8m etter GW9 → £1.6m etter GW10
- Endring per runde: GW9 +2.53, GW10 +4.33, GW11 +4.02, GW12 +3.42, GW13 +3.38

## Spillere inn i planene over

Flaggene kommer fra `forventning.py`. Én kamp som bærer xGI-en, slår ut i robust endring.

| Spiller | Lag | Pos | Pris | Eid | Sum GW9–13 | Robust | P(spiller) GW9 | Flagg |
|---|---|---|---|---|---|---|---|---|
| Raya | ARS | GKP | £6.1m | 45.4 % | 15.74 | 15.72 | 0.91 | — |
| Gabriel | ARS | DEF | £7.9m | 21.1 % | 18.91 | 18.15 | 0.91 | — |
| Silva | BOU | DEF | £5.0m | 0.7 % | 18.88 | 17.36 | 0.91 | — |
| Murillo | NFO | DEF | £5.5m | 2.2 % | 17.35 | 16.78 | 0.91 | — |
| Vuskovic | BHA | DEF | £5.1m | 6.2 % | 17.26 | 16.55 | 0.91 | — |
| De Cuyper | BHA | DEF | £5.3m | 42.2 % | 17.18 | 13.54 | 0.91 | én kamp (GW1) står for 65% av xGI |
| Tavernier | BOU | MID | £6.2m | 13.5 % | 21.52 | 18.95 | 0.91 | — |
| E.Le Fée | SUN | MID | £5.7m | 2.9 % | 21.30 | 18.48 | 0.91 | — |
| Rogers | CHE | MID | £8.0m | 49.7 % | 21.23 | 19.85 | 0.91 | — |
| Ødegaard | ARS | MID | £6.8m | 18.4 % | 20.45 | 17.61 | 0.91 | — |
| Gonzalo | FUL | FWD | £6.1m | 6.5 % | 20.99 | 19.62 | 0.91 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | £9.0m | 13.9 % | 18.63 | 17.67 | 0.73 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |

## Søkets omfang og forutsetninger

- Kandidater per posisjon: GKP 25, DEF 26, MID 26, FWD 25 (25 beste på forventning, 10 beste per million).
- 385 enkeltbytter vurdert i hver runde. Utvalg for kombinasjoner: 105 i GW9, 109 i GW10. Søket er ikke uttømmende for kombinasjoner.
- Priser er dagens. Prisendringer før byttet er ikke modellert.
- De operative reglene i `01` (template i premiumslottene, differensialer bare mellom £4,0m og £5,5m og maks tre samtidig, ett bytte per runde) er ikke modellert. Eierandelen står i tabellene; sjekk reglene for spillerne som kommer inn.
- Bytter i tredje runde og senere er ikke med. En plan som sparer, har verdi utover horisonten som tabellen ikke viser.
- I tilbaketesten avviker realiserte poeng over fem runder i snitt 5–6 poeng per spiller fra forventningen. En planforskjell på noen få poeng er en svak preferanse, ikke en dom.

