# Byttepakker — generert

*Generert 18.10.2026 kl. 07:13 UTC av `scripts/bytter.py` fra `fpl-data`. **Rør ikke fila for hånd.** Horisont GW8–12. Bytter vurderes i GW8 og GW9. Maks minuspoeng per runde: 0.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–6 summerer til sesongtotalene for 333 spillere, 19 felt; 334 spillere på lag som har spilt i GW7 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 18.10.2026 06:34 UTC, 0.6 t gammelt ved kjøring
- ✅ Bytteregler i API-et stemmer med 05 og skriptet: maks 3 per klubb, maks 5 frikjøp, halve prisstigningen ved salg, tropp på 15
- ✅ Bank regnet fra 6 overganger stemmer med historikken i alle 7 runder
- ✅ Frikjøp til GW8: 1. Kostnaden i hver runde stemmer med historikken

**Frikjøp, runde for runde:** GW1: første runde → 1 · GW2: 1 frikjøp, 0 brukt → 2 · GW3: 2 frikjøp, 0 brukt → 3 · GW4: 3 frikjøp, 2 brukt → 2 · GW5: 2 frikjøp, 0 brukt → 3 · GW6: 3 frikjøp, 1 brukt → 3 · GW7: 3 frikjøp, 3 brukt → 1

## Troppen inn i GW8

Bank **£0.3m**, frikjøp **1**. Salgspris etter regelen i `05`.

| Spiller | Lag | Pos | Nå | Kjøpt | Salgspris | Sum GW8–12 | Robust | P(spiller) GW8 | Eid |
|---|---|---|---|---|---|---|---|---|---|
| Verbruggen | BHA | GKP | £4.6m | £4.5m | £4.5m | 13.22 | 12.82 | 0.91 | 22.4 % |
| Kinsky | TOT | GKP | £4.5m | £4.5m | £4.5m | 13.14 | 13.15 | 0.91 | 15.5 % |
| Calafiori | ARS | DEF | £6.0m | £5.5m | £5.7m | 19.93 | 18.81 | 0.91 | 53.3 % |
| Thomas (COV) | COV | DEF | £4.0m | £4.0m | £4.0m | 17.25 | 16.50 | 0.91 | 9.2 % |
| Davis | IPS | DEF | £4.0m | £4.0m | £4.0m | 16.51 | 15.24 | 0.91 | 7.5 % |
| Diop | IPS | DEF | £3.9m | £4.0m | £3.9m | 14.72 | 14.61 | 0.91 | 11.1 % |
| Egan | HUL | DEF | £4.1m | £4.1m | £4.1m | 13.09 | 12.81 | 0.91 | 7.2 % |
| Saka | ARS | MID | £9.6m | £9.6m | £9.6m | 28.04 | 25.35 | 0.91 | 17.0 % |
| B.Fernandes | MUN | MID | £11.8m | £12.0m | £11.8m | 26.44 | 20.81 | 0.91 | 30.7 % |
| Mbeumo | MUN | MID | £7.8m | £8.0m | £7.8m | 24.77 | 20.47 | 0.91 | 19.5 % |
| Groß | BHA | MID | £6.1m | £6.1m | £6.1m | 19.85 | 17.88 | 0.91 | 44.2 % |
| Slater | HUL | MID | £4.5m | £4.5m | £4.5m | 12.31 | 11.65 | 0.91 | 5.0 % |
| Haaland | MCI | FWD | £15.7m | £15.5m | £15.6m | 28.00 | 26.24 | 0.91 | 76.5 % |
| Barry | EVE | FWD | £5.7m | £5.7m | £5.7m | 21.91 | 19.41 | 0.91 | 8.7 % |
| João Pedro | CHE | FWD | £7.8m | £7.5m | £7.6m | 21.71 | 19.66 | 0.91 | 72.4 % |

## Spar — ingen bytter

Lagets forventede poeng: **288.70** over horisonten (robust 261.22). Per runde: GW8 58.58, GW9 57.59, GW10 59.40, GW11 57.27, GW12 55.87.

GW8: elleveren 49.11 + kapteinsledd 6.60 (Saka, vise Haaland) + innbytterledd 2.88. Benk: Kinsky, Diop, Egan, Slater.

## Beste planer (16758 lovlige av 49411 vurderte)

Endring = forventede poeng mot å spare, over hele horisonten, etter minuspoeng.

| Plan | Minus | Endring GW8–12 | Robust endring | Endring GW8 | Bank etter GW8 | Bank etter GW9 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| GW8: Groß → E.Le Fée · GW9: Egan → Bogle | 0 | **+4.92** | +2.65 | +0.83 | £0.7m | £0.1m | — |
| GW8: Groß → E.Le Fée · GW9: Slater → Rudoni | 0 | **+4.77** | +2.97 | +0.83 | £0.7m | £0.3m | — |
| GW8: Groß → E.Le Fée · GW9: Slater → Gomez (BHA) | 0 | **+4.41** | +2.90 | +0.83 | £0.7m | £0.2m | — |
| GW9: Slater → E.Le Fée, João Pedro → Gonzalo | 0 | **+4.32** | +2.93 | +0.00 | £0.3m | £0.6m | — |
| GW8: Groß → Rudoni · GW9: Slater → E.Le Fée | 0 | **+4.19** | +2.70 | +0.26 | £1.5m | £0.3m | — |
| GW8: Groß → E.Le Fée · GW9: Kinsky → Trafford | 0 | **+4.14** | +3.05 | +0.83 | £0.7m | £0.2m | — |
| GW8: Groß → E.Le Fée · GW9: Verbruggen → Trafford | 0 | **+4.14** | +3.09 | +0.83 | £0.7m | £0.2m | — |
| GW8: João Pedro → Gonzalo · GW9: Slater → E.Le Fée | 0 | **+4.09** | +2.81 | -0.22 | £1.8m | £0.6m | — |
| GW9: Egan → Bogle, Groß → E.Le Fée | 0 | **+4.08** | +2.12 | +0.00 | £0.3m | £0.1m | — |
| GW9: Slater → E.Le Fée, Groß → Rudoni | 0 | **+3.93** | +2.45 | +0.00 | £0.3m | £0.3m | — |
| GW8: Groß → E.Le Fée · GW9: Egan → Justin | 0 | **+3.87** | +2.80 | +0.83 | £0.7m | £0.3m | — |
| GW8: Groß → E.Le Fée · GW9: Egan → Mitchell | 0 | **+3.66** | +1.74 | +0.83 | £0.7m | £0.3m | — |
| GW9: Slater → E.Le Fée, Groß → Gomez (BHA) | 0 | **+3.58** | +2.38 | +0.00 | £0.3m | £0.2m | — |
| GW8: Groß → E.Le Fée · GW9: Slater → Timber | 0 | **+3.40** | +2.29 | +0.83 | £0.7m | £0.2m | — |
| GW9: Kinsky → Trafford, Groß → E.Le Fée | 0 | **+3.30** | +2.53 | +0.00 | £0.3m | £0.2m | — |

## Beste plan som selger hver spiller

Svarer på «bør X selges?»: den beste lovlige planen der spilleren går ut, mot å spare.

| Plan | Minus | Endring GW8–12 | Robust endring | Endring GW8 | Bank etter GW8 | Bank etter GW9 | Klubber med 3 |
|---|---|---|---|---|---|---|---|
| **Verbruggen ut:** GW8: Groß → E.Le Fée · GW9: Verbruggen → Trafford | 0 | **+4.14** | +3.09 | +0.83 | £0.7m | £0.2m | — |
| **Kinsky ut:** GW8: Groß → E.Le Fée · GW9: Kinsky → Trafford | 0 | **+4.14** | +3.05 | +0.83 | £0.7m | £0.2m | — |
| **Calafiori ut:** GW9: Slater → E.Le Fée, Calafiori → Bogle | 0 | **+3.22** | +0.98 | +0.00 | £0.3m | £0.1m | — |
| **Thomas (COV) ut:** GW9: Thomas (COV) → Silva, João Pedro → Gonzalo | 0 | **+1.21** | +0.82 | +0.00 | £0.3m | £0.8m | — |
| **Davis ut:** GW8: Groß → E.Le Fée · GW9: Davis → Bogle | 0 | **+3.29** | +1.59 | +0.83 | £0.7m | £0.0m | — |
| **Diop ut:** GW8: Groß → E.Le Fée · GW9: Diop → Justin | 0 | **+3.28** | +2.14 | +0.83 | £0.7m | £0.1m | — |
| **Egan ut:** GW8: Groß → E.Le Fée · GW9: Egan → Bogle | 0 | **+4.92** | +2.65 | +0.83 | £0.7m | £0.1m | — |
| **Saka ut:** GW9: Slater → E.Le Fée, Saka → Gibbs-White | 0 | **-0.12** | -1.13 | +0.00 | £0.3m | £0.7m | — |
| **B.Fernandes ut:** GW9: Slater → E.Le Fée, B.Fernandes → Gibbs-White | 0 | **+1.51** | +3.34 | +0.00 | £0.3m | £2.9m | — |
| **Mbeumo ut:** GW9: Slater → E.Le Fée, Mbeumo → Ødegaard | 0 | **+2.18** | +1.48 | +0.00 | £0.3m | £0.1m | ARS |
| **Groß ut:** GW8: Groß → E.Le Fée · GW9: Egan → Bogle | 0 | **+4.92** | +2.65 | +0.83 | £0.7m | £0.1m | — |
| **Slater ut:** GW8: Groß → E.Le Fée · GW9: Slater → Rudoni | 0 | **+4.77** | +2.97 | +0.83 | £0.7m | £0.3m | — |
| **Haaland ut:** GW9: Slater → Gibbs-White, Haaland → Gonzalo | 0 | **-2.16** | -2.71 | +0.00 | £0.3m | £6.3m | — |
| **Barry ut:** GW8: Groß → E.Le Fée · GW9: Barry → Gonzalo | 0 | **+0.90** | +0.56 | +0.83 | £0.7m | £0.3m | — |
| **João Pedro ut:** GW9: Slater → E.Le Fée, João Pedro → Gonzalo | 0 | **+4.32** | +2.93 | +0.00 | £0.3m | £0.6m | — |

## Anti-drift for de tre beste planene

**GW8: Groß → E.Le Fée · GW9: Egan → Bogle**

- Klubber etter: ARS 2 · IPS 2 · MUN 2 · BHA 1 · CHE 1 · COV 1 · EVE 1 · HUL 1 · LEE 1 · MCI 1 · SUN 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £31.1m → £31.7m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £0.3m → £0.7m etter GW8 → £0.1m etter GW9
- Endring per runde: GW8 +0.83, GW9 +0.85, GW10 +1.53, GW11 +0.46, GW12 +1.25

**GW8: Groß → E.Le Fée · GW9: Slater → Rudoni**

- Klubber etter: ARS 2 · COV 2 · IPS 2 · MUN 2 · BHA 1 · CHE 1 · EVE 1 · HUL 1 · MCI 1 · SUN 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £31.1m → £31.1m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £0.3m → £0.7m etter GW8 → £0.3m etter GW9
- Endring per runde: GW8 +0.83, GW9 +1.25, GW10 +1.05, GW11 +0.93, GW12 +0.70

**GW8: Groß → E.Le Fée · GW9: Slater → Gomez (BHA)**

- Klubber etter: ARS 2 · BHA 2 · IPS 2 · MUN 2 · CHE 1 · COV 1 · EVE 1 · HUL 1 · MCI 1 · SUN 1 · TOT 1
- Keeper- og forsvarsbudsjett (nåpris): £31.1m → £31.1m. Topplagsandelen regnes ikke — `01` har erklært den utløpt som styringstall.
- Bank: £0.3m → £0.7m etter GW8 → £0.2m etter GW9
- Endring per runde: GW8 +0.83, GW9 +0.96, GW10 +1.04, GW11 +0.74, GW12 +0.84

## Spillere inn i planene over

Flaggene kommer fra `forventning.py`. Én kamp som bærer xGI-en, slår ut i robust endring.

| Spiller | Lag | Pos | Pris | Eid | Sum GW8–12 | Robust | P(spiller) GW8 | Flagg |
|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | £5.0m | 5.7 % | 15.76 | 15.75 | 0.91 | — |
| Silva | BOU | DEF | £5.0m | 0.6 % | 18.60 | 16.99 | 0.91 | én kamp (GW4) står for 50% av xGI |
| Bogle | LEE | DEF | £4.7m | 9.7 % | 17.53 | 15.40 | 0.91 | én kamp (GW3) står for 57% av xGI |
| Mitchell | CRY | DEF | £4.5m | 5.8 % | 16.06 | 14.39 | 0.91 | én kamp (GW3) står for 64% av xGI |
| Justin | LEE | DEF | £4.5m | 2.0 % | 15.88 | 15.68 | 0.91 | — |
| E.Le Fée | SUN | MID | £5.7m | 3.0 % | 22.18 | 19.03 | 0.91 | — |
| Ødegaard | ARS | MID | £6.8m | 19.0 % | 21.62 | 18.49 | 0.91 | — |
| Gibbs-White | NFO | MID | £8.0m | 12.1 % | 21.35 | 20.09 | 0.68 | første straffeskytter (penalties_order 1) · GW8: FPL-sjanse 75 % |
| Rudoni | COV | MID | £4.9m | 0.2 % | 18.98 | 17.32 | 0.91 | første straffeskytter (penalties_order 1) |
| Gomez (BHA) | BHA | MID | £5.0m | 3.6 % | 17.73 | 16.75 | 0.91 | — |
| Timber | CRY | MID | £5.0m | 0.1 % | 15.89 | 15.72 | 0.91 | — |
| Gonzalo | FUL | FWD | £6.1m | 7.1 % | 21.10 | 19.48 | 0.91 | første straffeskytter (penalties_order 1) |

## Søkets omfang og forutsetninger

- Kandidater per posisjon: GKP 25, DEF 26, MID 26, FWD 25 (25 beste på forventning, 10 beste per million).
- 385 enkeltbytter vurdert i hver runde. Utvalg for kombinasjoner: 108 i GW8, 107 i GW9. Søket er ikke uttømmende for kombinasjoner.
- Priser er dagens. Prisendringer før byttet er ikke modellert.
- De operative reglene i `01` (template i premiumslottene, differensialer bare mellom £4,0m og £5,5m og maks tre samtidig, ett bytte per runde) er ikke modellert. Eierandelen står i tabellene; sjekk reglene for spillerne som kommer inn.
- Bytter i tredje runde og senere er ikke med. En plan som sparer, har verdi utover horisonten som tabellen ikke viser.
- I tilbaketesten avviker realiserte poeng over fem runder i snitt 5–6 poeng per spiller fra forventningen. En planforskjell på noen få poeng er en svak preferanse, ikke en dom.

