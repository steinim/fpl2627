# Forventede poeng — generert

*Generert 26.11.2026 kl. 22:59 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–11 (data_checked). Horisont: GW12–16. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–11 summerer til sesongtotalene for alle 674 spillere, 19 felt
- ✅ Speilet hentet 26.11.2026 22:34 UTC, 0.4 t gammelt ved kjøring
- ✅ Lagstyrke-prior fra context/lagstyrke-prior.csv (ρ = 0.5); opprykksprior brukt for COV, HUL, IPS

## Modell og estimerte parametre

Formelen står i toppen av `scripts/forventning.py`.

- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel 0.7, start- og spillesannsynlighet kalibrert per runde fram (fast starter: P(start) 0.92 i første runde etter grunnlaget, 0.82 i den 7.), krymping av spillerrater mot posisjon og startpris 3 kamper, krymping av DC-treffrate mot posisjonssnitt 4 kamper, CS-faktor 1.046, målfaktor GKP 1.0, DEF 0.799, MID 0.987, FWD 1.001; assistfaktor GKP 1.376, DEF 1.202, MID 1.349, FWD 2.09.
- **Estimert fra sesongens data ved hver kjøring:**
  - Liga-xG per lag og kamp μ = 1.495. Bane: hjemme ×1.094, borte ×0.906.
  - Lagstyrke krympet mot forrige sesong (dempet med ρ = 0.5) med k = 15 kamper (angrep) og 30 (forsvar).
  - Bonus: k = 38.0 kamper for spillerens eget avvik. Koeffisienter per posisjon (konstant, så felt i rekkefølge):
    - GKP (n = 220): konstant -0.308; cs +0.983, redninger +0.104
    - DEF (n = 881): konstant -0.057; mal +1.186, assist +0.522, cs +0.517, dc +0.099
    - MID (n = 963): konstant +0.008; mal +1.458, assist +0.546, dc +0.047
    - FWD (n = 205): konstant +0.026; mal +1.621, assist +0.176, dc -0.026
  - Gule kort krympes med k = 7.3 kamper mot posisjonssnitt. Strafferedninger per keeper-90: 0.009.

**Begrensninger:**

- Snittet ligger 4–6 % under fasit i tilbaketesten. Avviket sitter hos spillere med lav startandel (under 0,2: 16 % under); faste startere treffer innenfor 1 %. Start- og spillesannsynligheten er kalibrert uten historisk skadestatus, så FPL-status kommer i tillegg — for en flagget spiller telles en del av skaderisikoen to ganger.
- Straffer ligger i xG slik de har falt. Straffeskytterrolle vises i kolonnen «Str», men modelleres ikke separat. Bommet straffe (−2) er ikke med.
- Tilgjengelighet utover neste runde bygger på FPL-status og -nyhet. Returdatoen i nyheten tolkes som første dag spilleren er tilgjengelig. Tolkningen står i flagget.
- Spillere uten telte kamper i grunnlaget (nysignert, skadet hele perioden) får ingen forventning. De må vurderes for hånd.
- I dobbelrunder er minuttfordelingen tilnærmet. En spiller som har byttet klubb i grunnlaget, får rater som blander to roller. Begge deler flagges.
- Modellen forklarer om lag 20 % av variansen i poeng for én runde og 30–40 % over fem. Over fem runder bommer den i snitt med 5,1–5,8 poeng per spiller.

### Lagstyrke (1,00 = snitt)

| Lag | Angrep A | Forsvar D (lavere er bedre) |
|---|---|---|
| MCI | 1.20 | 0.89 |
| BHA | 1.19 | 0.96 |
| BOU | 1.16 | 0.97 |
| MUN | 1.14 | 1.08 |
| LIV | 1.12 | 0.91 |
| ARS | 1.10 | 0.72 |
| BRE | 1.09 | 0.99 |
| CHE | 1.05 | 1.03 |
| NFO | 1.03 | 0.97 |
| CRY | 1.03 | 1.14 |
| LEE | 0.99 | 0.94 |
| AVL | 0.96 | 1.04 |
| NEW | 0.96 | 1.05 |
| SUN | 0.94 | 1.01 |
| FUL | 0.90 | 0.99 |
| IPS | 0.88 | 1.15 |
| EVE | 0.88 | 1.03 |
| TOT | 0.85 | 0.93 |
| COV | 0.81 | 1.07 |
| HUL | 0.78 | 1.07 |

## Troppen (picks GW11)

Bytter gjort etter GW11-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Verbruggen ★ | BHA | GKP | 4.7 | 3.08 | 2.60 | 2.64 | 2.99 | 2.96 | **14.28** | 14.01 | 0.02 | 0.00 | 1.00 |  |  | — |
| Kinsky ★ | TOT | GKP | 4.4 | 2.77 | 2.99 | 2.68 | 2.82 | 2.39 | **13.65** | 13.65 | 0.00 | 0.00 | 1.00 |  |  | — |
| Van Hecke ★ | TOT | DEF | 5.2 | 3.62 | 4.13 | 3.40 | 3.78 | 2.95 | **17.88** | 16.42 | 0.23 | 0.14 | 1.00 | 4/11 |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 3.47 | 3.15 | 3.47 | 3.40 | 3.50 | **17.00** | 16.22 | 0.24 | 0.20 | 0.90 | 0/10 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 3.28 | 3.97 | 2.96 | 3.62 | 2.79 | **16.62** | 16.27 | 0.16 | 0.13 | 1.00 | 6/9 |  | — |
| Diop ★ | IPS | DEF | 3.9 | 2.93 | 2.77 | 2.33 | 2.76 | 1.94 | **12.73** | 12.61 | 0.03 | 0.02 | 1.00 | 5/11 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 2.37 | 2.87 | 2.34 | 2.97 | 1.97 | **12.52** | 11.64 | 0.22 | 0.17 | 1.00 | 0/11 |  | GW12: FPL-sjanse 75 % |
| B.Fernandes ★ | MUN | MID | 11.6 | 5.29 | 4.73 | 5.45 | 4.83 | 3.56 | **23.86** | 20.51 | 0.67 | 0.46 | 0.90 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Tavernier ★ | BOU | MID | 6.8 | 4.59 | 4.86 | 5.21 | 3.61 | 5.03 | **23.30** | 21.59 | 0.64 | 0.56 | 1.00 | 1/11 | 3 | — |
| E.Le Fée ★ | SUN | MID | 5.7 | 4.90 | 4.13 | 4.42 | 4.65 | 5.04 | **23.13** | 21.10 | 0.55 | 0.46 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| Groß ★ | BHA | MID | 6.3 | 4.83 | 3.94 | 3.90 | 4.51 | 4.73 | **21.92** | 19.82 | 0.53 | 0.43 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 4.80 | 4.30 | 4.89 | 4.34 | 3.30 | **21.63** | 18.97 | 0.58 | 0.43 | 1.00 | 0/11 | 2 | — |
| Haaland ★ | MCI | FWD | 15.8 | 4.47 | 5.85 | 5.20 | 6.00 | 6.11 | **27.64** | 26.42 | 0.83 | 0.76 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 5.07 | 4.76 | 5.12 | 4.37 | 4.34 | **23.66** | 22.01 | 0.77 | 0.68 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson ★ | BOU | FWD | 6.6 | 4.40 | 4.74 | 4.98 | 3.45 | 4.82 | **22.38** | 20.68 | 0.64 | 0.55 | 1.00 | 0/11 |  | — |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | 5.1 | 3.64 | 3.10 | 3.39 | 3.01 | 3.27 | **16.42** | 16.41 | 0.00 | 0.00 | 1.00 |  |  | — |
| Tzolakis | HUL | GKP | 4.7 | 3.37 | 3.33 | 3.21 | 3.32 | 3.13 | **16.36** | 16.36 | 0.00 | 0.00 | 1.00 |  |  | — |
| Lammens | MUN | GKP | 4.8 | 3.06 | 2.94 | 3.17 | 2.81 | 2.74 | **14.72** | 14.67 | 0.00 | 0.00 | 1.00 |  |  | — |
| A.Becker | LIV | GKP | 5.5 | 2.97 | 3.05 | 2.65 | 2.87 | 3.02 | **14.56** | 14.54 | 0.00 | 0.00 | 1.00 |  |  | — |
| Suzuki | AVL | GKP | 5.1 | 3.08 | 3.11 | 2.88 | 2.84 | 2.64 | **14.55** | 14.54 | 0.00 | 0.00 | 0.99 |  |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Horníček | NEW | GKP | 5.0 | 2.91 | 2.92 | 3.01 | 2.86 | 2.72 | **14.42** | 14.42 | 0.00 | 0.00 | 1.00 |  |  | — |
| Donnarumma | MCI | GKP | 5.4 | 2.75 | 2.99 | 2.63 | 2.81 | 3.13 | **14.31** | 14.31 | 0.00 | 0.00 | 1.00 |  |  | — |
| Verbruggen ★ | BHA | GKP | 4.7 | 3.08 | 2.60 | 2.64 | 2.99 | 2.96 | **14.28** | 14.01 | 0.02 | 0.00 | 1.00 |  |  | — |

### DEF

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel | ARS | DEF | 8.1 | 4.03 | 3.67 | 4.02 | 3.90 | 3.98 | **19.60** | 18.87 | 0.16 | 0.12 | 1.00 | 5/11 |  | — |
| De Cuyper | BHA | DEF | 5.5 | 4.42 | 3.14 | 3.31 | 4.27 | 4.39 | **19.53** | 16.83 | 0.43 | 0.29 | 1.00 | 0/11 |  | — |
| Silva | BOU | DEF | 5.1 | 3.85 | 3.70 | 4.49 | 3.06 | 4.29 | **19.39** | 18.27 | 0.17 | 0.11 | 1.00 | 8/11 |  | — |
| Murillo | NFO | DEF | 5.5 | 3.97 | 3.94 | 3.50 | 3.42 | 4.01 | **18.85** | 18.39 | 0.18 | 0.16 | 1.00 | 7/11 |  | — |
| Hill | BOU | DEF | 5.7 | 3.73 | 3.54 | 4.31 | 3.00 | 4.12 | **18.68** | 17.86 | 0.12 | 0.06 | 1.00 | 7/11 |  | én kamp (GW2) står for 54% av xGI |
| Muharemović | LEE | DEF | 5.1 | 4.29 | 2.92 | 3.98 | 2.94 | 3.76 | **17.90** | 17.27 | 0.08 | 0.05 | 1.00 | 7/11 |  | — |
| Van Hecke ★ | TOT | DEF | 5.2 | 3.62 | 4.13 | 3.40 | 3.78 | 2.95 | **17.88** | 16.42 | 0.23 | 0.14 | 1.00 | 4/11 |  | — |
| Virgil | LIV | DEF | 6.4 | 3.53 | 3.76 | 3.03 | 3.48 | 3.71 | **17.51** | 17.19 | 0.09 | 0.07 | 1.00 | 6/11 |  | — |
| Justin | LEE | DEF | 4.5 | 4.23 | 2.78 | 3.94 | 2.82 | 3.69 | **17.45** | 16.78 | 0.16 | 0.12 | 1.00 | 4/11 |  | — |
| Jacquet | LIV | DEF | 5.1 | 3.49 | 3.70 | 2.99 | 3.44 | 3.66 | **17.30** | 16.92 | 0.08 | 0.06 | 1.00 | 5/11 |  | — |
| Konsa | ARS | DEF | 4.9 | 3.70 | 3.29 | 3.57 | 3.34 | 3.34 | **17.24** | 16.62 | 0.08 | 0.04 | 0.98 | 4/9 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Bogle | LEE | DEF | 4.8 | 4.21 | 2.63 | 3.96 | 2.68 | 3.65 | **17.12** | 15.62 | 0.28 | 0.20 | 1.00 | 0/11 |  | — |
| Vuskovic | BHA | DEF | 5.3 | 3.82 | 2.80 | 2.97 | 3.72 | 3.75 | **17.06** | 16.47 | 0.14 | 0.10 | 1.00 | 4/11 |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 3.47 | 3.15 | 3.47 | 3.40 | 3.50 | **17.00** | 16.22 | 0.24 | 0.20 | 0.90 | 0/10 |  | — |
| N.Williams | NFO | DEF | 4.8 | 3.57 | 3.55 | 3.12 | 3.04 | 3.64 | **16.92** | 16.31 | 0.20 | 0.17 | 1.00 | 2/11 |  | — |

### MID

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B.Fernandes ★ | MUN | MID | 11.6 | 5.29 | 4.73 | 5.45 | 4.83 | 3.56 | **23.86** | 20.51 | 0.67 | 0.46 | 0.90 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Gibbs-White | NFO | MID | 7.8 | 5.16 | 4.64 | 4.70 | 4.27 | 4.84 | **23.61** | 22.63 | 0.54 | 0.48 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Tavernier ★ | BOU | MID | 6.8 | 4.59 | 4.86 | 5.21 | 3.61 | 5.03 | **23.30** | 21.59 | 0.64 | 0.56 | 1.00 | 1/11 | 3 | — |
| E.Le Fée ★ | SUN | MID | 5.7 | 4.90 | 4.13 | 4.42 | 4.65 | 5.04 | **23.13** | 21.10 | 0.55 | 0.46 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| Groß ★ | BHA | MID | 6.3 | 4.83 | 3.94 | 3.90 | 4.51 | 4.73 | **21.92** | 19.82 | 0.53 | 0.43 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 4.80 | 4.30 | 4.89 | 4.34 | 3.30 | **21.63** | 18.97 | 0.58 | 0.43 | 1.00 | 0/11 | 2 | — |
| Ødegaard | ARS | MID | 6.7 | 4.33 | 4.01 | 3.89 | 4.25 | 4.47 | **20.94** | 18.90 | 0.52 | 0.40 | 1.00 | 0/11 | 3 | — |
| Rogers | CHE | MID | 8.3 | 3.89 | 4.68 | 3.99 | 3.45 | 4.23 | **20.26** | 19.23 | 0.44 | 0.37 | 1.00 | 1/11 |  | — |
| Wirtz | LIV | MID | 7.4 | 3.97 | 4.23 | 3.72 | 3.92 | 3.89 | **19.73** | 18.23 | 0.46 | 0.35 | 1.00 | 0/11 | 4 | — |
| Rayan | BOU | MID | 6.3 | 3.87 | 4.04 | 4.31 | 3.14 | 4.16 | **19.52** | 18.29 | 0.38 | 0.32 | 1.00 | 1/11 |  | — |
| Barcola | LIV | MID | 8.1 | 3.92 | 4.17 | 3.61 | 3.80 | 3.75 | **19.24** | 17.36 | 0.50 | 0.36 | 0.98 | 0/8 |  | — |
| Palmer | CHE | MID | 9.8 | 3.70 | 4.43 | 3.79 | 3.28 | 4.01 | **19.22** | 17.94 | 0.36 | 0.29 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| McAtee | NFO | MID | 5.5 | 4.07 | 3.78 | 3.75 | 3.51 | 3.83 | **18.94** | 18.45 | 0.30 | 0.28 | 1.00 | 5/11 |  | — |
| Gomez | BHA | MID | 5.1 | 4.07 | 3.43 | 3.40 | 3.82 | 3.95 | **18.67** | 17.03 | 0.33 | 0.26 | 1.00 | 2/11 |  | — |
| Rudoni | COV | MID | 5.0 | 3.61 | 4.28 | 3.57 | 3.84 | 3.26 | **18.56** | 17.31 | 0.47 | 0.39 | 0.99 | 1/10 | 1 | første straffeskytter (penalties_order 1) |

### FWD

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.8 | 4.47 | 5.85 | 5.20 | 6.00 | 6.11 | **27.64** | 26.42 | 0.83 | 0.76 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 5.07 | 4.76 | 5.12 | 4.37 | 4.34 | **23.66** | 22.01 | 0.77 | 0.68 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | 9.4 | 4.61 | 4.94 | 4.32 | 4.51 | 4.40 | **22.79** | 21.62 | 0.71 | 0.62 | 0.95 | 0/10 | 2 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Evanilson ★ | BOU | FWD | 6.6 | 4.40 | 4.74 | 4.98 | 3.45 | 4.82 | **22.38** | 20.68 | 0.64 | 0.55 | 1.00 | 0/11 |  | — |
| Calvert-Lewin | LEE | FWD | 6.0 | 4.92 | 3.78 | 4.92 | 3.69 | 4.33 | **21.64** | 19.88 | 0.57 | 0.48 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| N.Jackson | AVL | FWD | 7.3 | 4.19 | 4.30 | 4.49 | 3.76 | 3.63 | **20.37** | 18.65 | 0.53 | 0.43 | 1.00 | 0/10 | 3 | — |
| Delap | NFO | FWD | 5.3 | 4.06 | 3.59 | 3.66 | 3.29 | 3.68 | **18.28** | 16.76 | 0.44 | 0.35 | 0.99 | 0/9 | 3 | — |
| Havertz | ARS | FWD | 7.4 | 3.49 | 3.26 | 3.11 | 3.46 | 3.64 | **16.95** | 16.21 | 0.40 | 0.35 | 0.90 | 0/10 |  | — |
| Gonzalo | FUL | FWD | 5.8 | 3.39 | 3.03 | 3.23 | 3.51 | 3.09 | **16.26** | 15.44 | 0.52 | 0.45 | 0.69 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| McBurnie | HUL | FWD | 5.5 | 3.50 | 3.46 | 3.07 | 3.25 | 2.85 | **16.13** | 14.72 | 0.34 | 0.25 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |

## Uavklart fravær i troppen og valgte spillere

Ingen.

