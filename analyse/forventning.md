# Forventede poeng — generert

*Generert 08.11.2026 kl. 08:57 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–9 (data_checked). Horisont: GW11–15. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–9 summerer til sesongtotalene for 340 spillere, 19 felt; 331 spillere på lag som har spilt i GW10 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 08.11.2026 07:57 UTC, 1.0 t gammelt ved kjøring
- ✅ Lagstyrke-prior fra context/lagstyrke-prior.csv (ρ = 0.5); opprykksprior brukt for COV, HUL, IPS

## Modell og estimerte parametre

Formelen står i toppen av `scripts/forventning.py`.

- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel 0.7, start- og spillesannsynlighet kalibrert per runde fram (fast starter: P(start) 0.92 i første runde etter grunnlaget, 0.82 i den 7.), krymping av spillerrater mot posisjon og startpris 3 kamper, krymping av DC-treffrate mot posisjonssnitt 4 kamper, CS-faktor 1.046, målfaktor GKP 1.0, DEF 0.799, MID 0.987, FWD 1.001; assistfaktor GKP 1.376, DEF 1.202, MID 1.349, FWD 2.09.
- **Estimert fra sesongens data ved hver kjøring:**
  - Liga-xG per lag og kamp μ = 1.457. Bane: hjemme ×1.068, borte ×0.932.
  - Lagstyrke krympet mot forrige sesong (dempet med ρ = 0.5) med k = 15 kamper (angrep) og 30 (forsvar).
  - Bonus: k = 38.0 kamper for spillerens eget avvik. Koeffisienter per posisjon (konstant, så felt i rekkefølge):
    - GKP (n = 180): konstant -0.238; cs +0.990, redninger +0.083
    - DEF (n = 724): konstant -0.049; mal +1.215, assist +0.428, cs +0.550, dc +0.089
    - MID (n = 789): konstant +0.007; mal +1.428, assist +0.533, dc +0.082
    - FWD (n = 169): konstant +0.017; mal +1.667, assist +0.304, dc -0.017
  - Gule kort krympes med k = 7.3 kamper mot posisjonssnitt. Strafferedninger per keeper-90: 0.011.

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
| MCI | 1.21 | 0.92 |
| BHA | 1.18 | 0.98 |
| ARS | 1.15 | 0.72 |
| BOU | 1.13 | 0.97 |
| MUN | 1.12 | 1.02 |
| BRE | 1.12 | 1.02 |
| CHE | 1.11 | 0.99 |
| LIV | 1.05 | 0.90 |
| NFO | 1.02 | 0.96 |
| CRY | 0.97 | 1.12 |
| FUL | 0.96 | 1.01 |
| NEW | 0.95 | 1.10 |
| SUN | 0.95 | 1.03 |
| LEE | 0.94 | 0.97 |
| AVL | 0.93 | 1.03 |
| EVE | 0.92 | 1.03 |
| IPS | 0.90 | 1.13 |
| TOT | 0.85 | 0.93 |
| COV | 0.80 | 1.06 |
| HUL | 0.79 | 1.07 |

## Troppen (picks GW10)

Bytter gjort etter GW10-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW11 | GW12 | GW13 | GW14 | GW15 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Verbruggen ★ | BHA | GKP | 4.6 | 3.17 | 3.05 | 2.70 | 2.74 | 2.97 | **14.63** | 14.33 | 0.02 | 0.00 | 1.00 |  |  | — |
| Kinsky ★ | TOT | GKP | 4.4 | 3.01 | 2.70 | 2.82 | 2.56 | 2.83 | **13.93** | 13.93 | 0.00 | 0.00 | 1.00 |  |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 3.46 | 3.25 | 3.11 | 3.45 | 3.36 | **16.63** | 15.81 | 0.29 | 0.23 | 0.78 | 0/8 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 2.92 | 3.18 | 3.04 | 2.62 | 3.08 | **14.85** | 13.82 | 0.25 | 0.20 | 1.00 | 0/9 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 1.79 | 3.19 | 3.60 | 2.83 | 3.41 | **14.82** | 14.24 | 0.13 | 0.09 | 1.00 | 5/8 |  | GW11: FPL-sjanse 50 % |
| Diop ★ | IPS | DEF | 3.9 | 2.97 | 3.05 | 3.00 | 2.64 | 2.90 | **14.57** | 14.45 | 0.03 | 0.02 | 1.00 | 5/9 |  | — |
| Egan ★ | HUL | DEF | 4.1 | 2.74 | 2.77 | 2.88 | 2.42 | 3.11 | **13.91** | 13.71 | 0.05 | 0.03 | 1.00 | 5/9 |  | — |
| Mbeumo ★ | MUN | MID | 7.9 | 4.33 | 5.00 | 4.73 | 5.08 | 4.67 | **23.81** | 20.53 | 0.61 | 0.44 | 1.00 | 0/9 | 2 | — |
| Tavernier ★ | BOU | MID | 6.7 | 4.54 | 4.21 | 4.37 | 4.69 | 3.37 | **21.17** | 19.18 | 0.61 | 0.50 | 1.00 | 0/9 | 3 | — |
| B.Fernandes ★ | MUN | MID | 11.6 | 3.67 | 4.34 | 4.18 | 4.54 | 4.20 | **20.93** | 16.87 | 0.57 | 0.29 | 0.78 | 0/8 | 1 | én kamp (GW2) står for 55% av xGI | første straffeskytter (penalties_order 1) |
| Groß ★ | BHA | MID | 6.3 | 3.77 | 3.99 | 3.34 | 3.32 | 3.71 | **18.13** | 16.54 | 0.42 | 0.35 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Slater ★ | HUL | MID | 4.5 | 2.42 | 2.39 | 2.37 | 2.20 | 2.35 | **11.73** | 11.22 | 0.13 | 0.09 | 1.00 | 0/9 |  | — |
| Haaland ★ | MCI | FWD | 15.8 | 6.13 | 4.39 | 5.73 | 5.33 | 5.70 | **27.27** | 25.81 | 0.83 | 0.75 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 4.88 | 4.83 | 4.74 | 5.05 | 4.47 | **23.98** | 22.07 | 0.80 | 0.69 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson ★ | BOU | FWD | 6.5 | 4.28 | 3.97 | 4.16 | 4.37 | 3.18 | **19.96** | 17.83 | 0.55 | 0.42 | 1.00 | 0/9 |  | — |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW11 | GW12 | GW13 | GW14 | GW15 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | 5.0 | 3.13 | 3.47 | 2.98 | 3.25 | 2.98 | **15.81** | 15.80 | 0.00 | 0.00 | 1.00 |  |  | — |
| Raya | ARS | GKP | 6.2 | 3.18 | 2.99 | 2.86 | 3.18 | 2.96 | **15.16** | 15.15 | 0.00 | 0.00 | 1.00 |  |  | — |
| Suzuki | AVL | GKP | 5.0 | 3.16 | 2.99 | 3.00 | 2.90 | 2.90 | **14.94** | 14.92 | 0.00 | 0.00 | 0.98 |  |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Lammens | MUN | GKP | 4.8 | 2.96 | 2.96 | 2.93 | 3.18 | 2.85 | **14.88** | 14.82 | 0.00 | 0.00 | 1.00 |  |  | — |
| Tzolakis | HUL | GKP | 4.7 | 2.97 | 2.94 | 2.95 | 2.78 | 3.04 | **14.69** | 14.69 | 0.00 | 0.00 | 1.00 |  |  | — |
| Verbruggen ★ | BHA | GKP | 4.6 | 3.17 | 3.05 | 2.70 | 2.74 | 2.97 | **14.63** | 14.33 | 0.02 | 0.00 | 1.00 |  |  | — |
| Horníček | NEW | GKP | 5.0 | 2.89 | 2.77 | 2.80 | 2.89 | 2.80 | **14.15** | 14.15 | 0.00 | 0.00 | 1.00 |  |  | — |
| Donnarumma | MCI | GKP | 5.5 | 3.07 | 2.66 | 2.97 | 2.61 | 2.72 | **14.03** | 14.03 | 0.00 | 0.00 | 1.00 |  |  | — |

### DEF

| Spiller | Lag | Pos | Pris | GW11 | GW12 | GW13 | GW14 | GW15 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel | ARS | DEF | 8.1 | 4.25 | 3.94 | 3.73 | 4.12 | 3.96 | **20.00** | 19.21 | 0.19 | 0.14 | 1.00 | 4/9 |  | — |
| Van Hecke | TOT | DEF | 5.0 | 4.28 | 3.58 | 3.88 | 3.21 | 3.83 | **18.78** | 16.93 | 0.26 | 0.15 | 1.00 | 3/9 |  | — |
| Silva | BOU | DEF | 5.1 | 3.94 | 3.66 | 3.54 | 4.32 | 2.99 | **18.45** | 17.19 | 0.18 | 0.11 | 1.00 | 6/9 |  | — |
| De Cuyper | BHA | DEF | 5.4 | 4.03 | 4.07 | 3.09 | 3.23 | 3.88 | **18.31** | 15.21 | 0.39 | 0.20 | 1.00 | 0/9 |  | én kamp (GW1) står for 53% av xGI |
| Murillo | NFO | DEF | 5.5 | 3.38 | 3.74 | 4.01 | 3.51 | 3.54 | **18.18** | 17.68 | 0.19 | 0.17 | 1.00 | 6/9 |  | — |
| Vuskovic | BHA | DEF | 5.2 | 3.91 | 3.85 | 3.03 | 3.17 | 3.71 | **17.67** | 17.05 | 0.16 | 0.12 | 1.00 | 4/9 |  | — |
| Muharemović | LEE | DEF | 5.1 | 3.20 | 4.11 | 2.89 | 3.82 | 3.08 | **17.09** | 16.42 | 0.10 | 0.06 | 1.00 | 6/9 |  | — |
| Hill | BOU | DEF | 5.6 | 3.57 | 3.33 | 3.18 | 3.92 | 2.75 | **16.75** | 15.81 | 0.11 | 0.03 | 1.00 | 5/9 |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 3.46 | 3.25 | 3.11 | 3.45 | 3.36 | **16.63** | 15.81 | 0.29 | 0.23 | 0.78 | 0/8 |  | — |
| Konsa | ARS | DEF | 4.8 | 3.63 | 3.29 | 3.07 | 3.40 | 3.17 | **16.56** | 15.88 | 0.09 | 0.04 | 0.96 | 3/7 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Virgil | LIV | DEF | 6.4 | 3.32 | 3.32 | 3.52 | 2.87 | 3.43 | **16.46** | 16.05 | 0.06 | 0.04 | 1.00 | 5/9 |  | — |
| N.Williams | NFO | DEF | 4.9 | 3.01 | 3.38 | 3.66 | 3.16 | 3.20 | **16.40** | 15.77 | 0.24 | 0.20 | 1.00 | 2/9 |  | — |
| Jacquet | LIV | DEF | 5.1 | 3.30 | 3.31 | 3.50 | 2.86 | 3.41 | **16.38** | 15.91 | 0.06 | 0.04 | 1.00 | 4/9 |  | — |
| Bogle | LEE | DEF | 4.8 | 3.00 | 4.02 | 2.66 | 3.76 | 2.85 | **16.30** | 14.63 | 0.28 | 0.18 | 1.00 | 0/9 |  | — |
| Richards | CRY | DEF | 4.9 | 3.50 | 3.75 | 2.75 | 3.05 | 2.95 | **15.99** | 15.93 | 0.03 | 0.02 | 1.00 | 7/9 |  | — |

### MID

| Spiller | Lag | Pos | Pris | GW11 | GW12 | GW13 | GW14 | GW15 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mbeumo ★ | MUN | MID | 7.9 | 4.33 | 5.00 | 4.73 | 5.08 | 4.67 | **23.81** | 20.53 | 0.61 | 0.44 | 1.00 | 0/9 | 2 | — |
| Gibbs-White | NFO | MID | 7.8 | 4.51 | 4.89 | 4.72 | 4.70 | 4.44 | **23.27** | 22.29 | 0.60 | 0.54 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| E.Le Fée | SUN | MID | 5.7 | 4.45 | 4.53 | 3.97 | 4.37 | 4.36 | **21.68** | 19.42 | 0.56 | 0.45 | 1.00 | 1/9 | 2 | — |
| Tavernier ★ | BOU | MID | 6.7 | 4.54 | 4.21 | 4.37 | 4.69 | 3.37 | **21.17** | 19.18 | 0.61 | 0.50 | 1.00 | 0/9 | 3 | — |
| B.Fernandes ★ | MUN | MID | 11.6 | 3.67 | 4.34 | 4.18 | 4.54 | 4.20 | **20.93** | 16.87 | 0.57 | 0.29 | 0.78 | 0/8 | 1 | én kamp (GW2) står for 55% av xGI | første straffeskytter (penalties_order 1) |
| Rogers | CHE | MID | 8.2 | 4.33 | 3.87 | 4.52 | 3.93 | 3.58 | **20.23** | 19.10 | 0.48 | 0.39 | 1.00 | 1/9 |  | — |
| Ødegaard | ARS | MID | 6.7 | 4.29 | 4.09 | 3.93 | 3.82 | 4.06 | **20.18** | 17.81 | 0.53 | 0.37 | 1.00 | 0/9 | 3 | — |
| Palmer | CHE | MID | 9.8 | 4.24 | 3.79 | 4.44 | 3.85 | 3.50 | **19.82** | 18.41 | 0.41 | 0.33 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Rayan | BOU | MID | 6.3 | 3.95 | 3.69 | 3.79 | 4.05 | 3.06 | **18.54** | 17.08 | 0.36 | 0.28 | 1.00 | 1/9 |  | — |
| Enciso | IPS | MID | 5.5 | 3.56 | 3.93 | 3.66 | 3.41 | 3.90 | **18.47** | 17.75 | 0.49 | 0.44 | 1.00 | 0/9 |  | — |
| Rudoni | COV | MID | 4.9 | 4.09 | 3.45 | 3.93 | 3.35 | 3.63 | **18.46** | 16.97 | 0.49 | 0.39 | 0.98 | 1/8 | 1 | første straffeskytter (penalties_order 1) |
| Iwobi | FUL | MID | 5.4 | 3.56 | 3.87 | 3.57 | 3.64 | 3.81 | **18.45** | 17.15 | 0.51 | 0.41 | 1.00 | 0/9 | 3 | — |
| Groß ★ | BHA | MID | 6.3 | 3.77 | 3.99 | 3.34 | 3.32 | 3.71 | **18.13** | 16.54 | 0.42 | 0.35 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Rice | ARS | MID | 7.5 | 3.71 | 3.55 | 3.42 | 3.37 | 3.50 | **17.55** | 17.05 | 0.29 | 0.26 | 1.00 | 1/9 |  | — |
| McAtee | NFO | MID | 5.5 | 3.44 | 3.60 | 3.54 | 3.46 | 3.35 | **17.39** | 16.81 | 0.27 | 0.23 | 1.00 | 4/9 |  | — |

### FWD

| Spiller | Lag | Pos | Pris | GW11 | GW12 | GW13 | GW14 | GW15 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.8 | 6.13 | 4.39 | 5.73 | 5.33 | 5.70 | **27.27** | 25.81 | 0.83 | 0.75 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 4.88 | 4.83 | 4.74 | 5.05 | 4.47 | **23.98** | 22.07 | 0.80 | 0.69 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Thiago | BRE | FWD | 7.8 | 4.82 | 4.28 | 3.69 | 4.24 | 4.08 | **21.11** | 19.98 | 0.60 | 0.53 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | 9.2 | 4.39 | 3.97 | 4.26 | 3.78 | 4.01 | **20.41** | 19.40 | 0.63 | 0.56 | 0.89 | 0/8 | 2 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Evanilson ★ | BOU | FWD | 6.5 | 4.28 | 3.97 | 4.16 | 4.37 | 3.18 | **19.96** | 17.83 | 0.55 | 0.42 | 1.00 | 0/9 |  | — |
| Gonzalo | FUL | FWD | 5.9 | 3.84 | 4.21 | 3.74 | 3.90 | 4.17 | **19.86** | 18.69 | 0.56 | 0.49 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Calvert-Lewin | LEE | FWD | 6.0 | 3.70 | 4.10 | 3.42 | 4.15 | 3.31 | **18.69** | 17.75 | 0.47 | 0.41 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| N.Jackson | AVL | FWD | 7.1 | 3.79 | 3.63 | 3.65 | 3.80 | 3.36 | **18.23** | 17.37 | 0.43 | 0.38 | 1.00 | 0/8 | 3 | — |
| Delap | NFO | FWD | 5.3 | 3.49 | 3.72 | 3.52 | 3.55 | 3.33 | **17.61** | 15.99 | 0.49 | 0.37 | 0.97 | 0/7 | 3 | — |
| Havertz | ARS | FWD | 7.4 | 3.41 | 3.30 | 3.22 | 3.07 | 3.34 | **16.34** | 15.60 | 0.43 | 0.37 | 0.78 | 0/8 |  | — |

## Uavklart fravær i troppen og valgte spillere

Ingen.

