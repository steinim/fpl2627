# Forventede poeng — generert

*Generert 17.10.2026 kl. 11:23 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–6 (data_checked). Horisont: GW8–12. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–6 summerer til sesongtotalene for alle 667 spillere, 19 felt
- ✅ Speilet hentet 17.10.2026 06:09 UTC, 5.2 t gammelt ved kjøring
- ✅ Lagstyrke-prior fra context/lagstyrke-prior.csv (ρ = 0.5); opprykksprior brukt for COV, HUL, IPS

## Modell og estimerte parametre

Formelen står i toppen av `scripts/forventning.py`.

- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel 0.7, krymping av spillerrater mot posisjon og startpris 3 kamper, krymping av DC-treffrate mot posisjonssnitt 4 kamper, CS-faktor 1.046, målfaktor GKP 1.0, DEF 0.799, MID 0.987, FWD 1.001; assistfaktor GKP 1.376, DEF 1.202, MID 1.349, FWD 2.09.
- **Estimert fra sesongens data ved hver kjøring:**
  - Liga-xG per lag og kamp μ = 1.533. Bane: hjemme ×1.059, borte ×0.941.
  - Lagstyrke krympet mot forrige sesong (dempet med ρ = 0.5) med k = 15 kamper (angrep) og 30 (forsvar).
  - Bonus: k = 38.0 kamper for spillerens eget avvik. Koeffisienter per posisjon (konstant, så felt i rekkefølge):
    - GKP (n = 120): konstant -0.204; cs +0.956, redninger +0.068
    - DEF (n = 488): konstant -0.048; mal +1.165, assist +0.375, cs +0.545, dc +0.095
    - MID (n = 523): konstant +0.004; mal +1.399, assist +0.539, dc +0.129
    - FWD (n = 114): konstant -0.021; mal +1.387, assist +0.385, dc +0.021
  - Gule kort krympes med k = 10.9 kamper mot posisjonssnitt. Strafferedninger per keeper-90: 0.017.

**Begrensninger:**

- Snittet ligger 1–4 % over fasit i tilbaketesten, fordi historisk skadestatus ikke finnes og alle settes som tilgjengelige. I bruk dekker FPL-status kjente skader, ikke uvarslet rotasjon.
- Straffer ligger i xG slik de har falt. Straffeskytterrolle vises i kolonnen «Str», men modelleres ikke separat. Bommet straffe (−2) er ikke med.
- Tilgjengelighet utover neste runde bygger på FPL-status og -nyhet. Returdatoen i nyheten tolkes som første dag spilleren er tilgjengelig. Tolkningen står i flagget.
- Spillere uten telte kamper i grunnlaget (nysignert, skadet hele perioden) får ingen forventning. De må vurderes for hånd.
- I dobbelrunder er minuttfordelingen tilnærmet. En spiller som har byttet klubb i grunnlaget, får rater som blander to roller. Begge deler flagges.
- Modellen forklarer om lag 20 % av variansen i poeng for én runde og 30–40 % over fem. Forskjeller under 2–3 poeng over fem runder er innenfor usikkerheten.

### Lagstyrke (1,00 = snitt)

| Lag | Angrep A | Forsvar D (lavere er bedre) |
|---|---|---|
| BHA | 1.21 | 0.99 |
| MCI | 1.21 | 0.93 |
| BRE | 1.15 | 1.02 |
| ARS | 1.14 | 0.73 |
| MUN | 1.12 | 0.97 |
| CHE | 1.08 | 1.00 |
| LIV | 1.02 | 0.93 |
| BOU | 1.02 | 1.00 |
| CRY | 1.02 | 1.07 |
| NFO | 1.01 | 1.02 |
| NEW | 0.99 | 1.08 |
| FUL | 0.97 | 1.01 |
| LEE | 0.96 | 0.98 |
| SUN | 0.95 | 0.98 |
| EVE | 0.93 | 1.03 |
| AVL | 0.92 | 1.00 |
| IPS | 0.91 | 1.09 |
| COV | 0.83 | 1.06 |
| HUL | 0.83 | 1.08 |
| TOT | 0.82 | 0.96 |

## Troppen (picks GW6)

Bytter gjort etter GW6-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Verbruggen ★ | BHA | GKP | 4.6 | 2.97 | 2.80 | 3.00 | 3.28 | 3.20 | **15.25** | 14.78 | 0.03 | 0.00 | 1.00 |  |  | — |
| Kinsky ★ | TOT | GKP | 4.5 | 2.84 | 3.07 | 2.99 | 3.25 | 3.01 | **15.16** | 15.16 | 0.00 | 0.00 | 1.00 |  |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 4.93 | 4.20 | 5.23 | 4.45 | 4.24 | **23.04** | 21.74 | 0.34 | 0.28 | 1.00 | 0/6 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 3.78 | 3.87 | 3.73 | 3.73 | 3.97 | **19.07** | 17.60 | 0.35 | 0.28 | 1.00 | 0/6 |  | — |
| Diop ★ | IPS | DEF | 4.0 | 3.30 | 3.46 | 3.27 | 3.45 | 3.51 | **16.99** | 16.86 | 0.04 | 0.03 | 1.00 | 3/6 |  | — |
| N.Williams ★ | NFO | DEF | 5.0 | 3.68 | 3.10 | 3.27 | 3.34 | 3.59 | **16.99** | 16.27 | 0.25 | 0.20 | 1.00 | 1/6 |  | — |
| Egan ★ | HUL | DEF | 4.1 | 3.01 | 3.55 | 2.64 | 2.88 | 2.99 | **15.07** | 14.75 | 0.04 | 0.01 | 1.00 | 3/6 |  | — |
| B.Fernandes ★ | MUN | MID | 11.8 | 6.37 | 5.85 | 6.42 | 5.57 | 6.43 | **30.64** | 24.07 | 0.67 | 0.31 | 1.00 | 0/6 | 1 | én kamp (GW2) står for 62% av xGI | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 5.96 | 5.48 | 6.01 | 5.23 | 6.01 | **28.69** | 23.68 | 0.70 | 0.45 | 1.00 | 0/6 | 2 | — |
| Ødegaard ★ | ARS | MID | 6.8 | 5.22 | 4.58 | 5.41 | 4.96 | 4.85 | **25.02** | 21.36 | 0.65 | 0.40 | 1.00 | 0/6 | 3 | — |
| Gibbs-White ★ | NFO | MID | 8.0 | 4.01 | 5.09 | 5.16 | 5.05 | 5.44 | **24.76** | 23.29 | 0.59 | 0.49 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) | FPL-sjansen gjelder GW7; brukt for GW8 | GW8: FPL-sjanse 75 % |
| Slater ★ | HUL | MID | 4.5 | 2.89 | 3.03 | 2.56 | 2.85 | 2.83 | **14.16** | 13.39 | 0.14 | 0.08 | 1.00 | 0/6 |  | — |
| Haaland ★ | MCI | FWD | 15.7 | 6.50 | 7.01 | 6.56 | 7.12 | 5.23 | **32.42** | 30.37 | 0.91 | 0.78 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 4.16 | 5.28 | 5.66 | 5.12 | 5.17 | **25.39** | 22.47 | 0.82 | 0.64 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| João Pedro ★ | CHE | FWD | 7.8 | 5.11 | 5.14 | 4.80 | 5.17 | 4.91 | **25.12** | 22.73 | 0.64 | 0.47 | 1.00 | 0/5 |  | — |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | 5.0 | 3.57 | 3.51 | 3.84 | 3.47 | 3.83 | **18.21** | 18.19 | 0.00 | 0.00 | 1.00 |  |  | — |
| Raya | ARS | GKP | 6.1 | 3.80 | 3.48 | 3.98 | 3.53 | 3.42 | **18.20** | 18.18 | 0.00 | 0.00 | 1.00 |  |  | — |
| Martinez | CHE | GKP | 5.0 | 3.80 | 3.52 | 3.55 | 3.64 | 3.51 | **18.02** | 18.00 | 0.00 | 0.00 | 1.00 |  |  | — |
| Kelleher | BRE | GKP | 5.0 | 3.53 | 3.46 | 3.28 | 3.53 | 3.31 | **17.11** | 17.09 | 0.00 | 0.00 | 1.00 |  |  | — |
| Donnarumma | MCI | GKP | 5.5 | 3.48 | 3.33 | 3.39 | 3.55 | 3.29 | **17.03** | 17.03 | 0.00 | 0.00 | 1.00 |  |  | — |
| Lammens | MUN | GKP | 4.9 | 3.37 | 3.20 | 3.50 | 3.25 | 3.25 | **16.57** | 16.58 | 0.00 | 0.00 | 1.00 |  |  | — |
| Suzuki | AVL | GKP | 5.0 | 3.22 | 3.39 | 3.20 | 3.41 | 3.34 | **16.55** | 16.53 | 0.00 | 0.00 | 0.94 |  |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Leno | FUL | GKP | 4.5 | 3.39 | 3.27 | 3.32 | 3.02 | 3.28 | **16.27** | 16.28 | 0.00 | 0.00 | 1.00 |  |  | — |

### DEF

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calafiori ★ | ARS | DEF | 5.9 | 4.93 | 4.20 | 5.23 | 4.45 | 4.24 | **23.04** | 21.74 | 0.34 | 0.28 | 1.00 | 0/6 |  | — |
| Silva | BOU | DEF | 5.0 | 3.83 | 4.57 | 4.42 | 4.51 | 4.19 | **21.52** | 19.64 | 0.27 | 0.16 | 1.00 | 4/6 |  | én kamp (GW4) står for 50% av xGI |
| Gabriel | ARS | DEF | 7.9 | 4.44 | 3.83 | 4.72 | 4.00 | 3.81 | **20.81** | 20.10 | 0.12 | 0.08 | 1.00 | 2/6 |  | — |
| De Cuyper | BHA | DEF | 5.2 | 3.85 | 3.49 | 4.21 | 4.55 | 4.62 | **20.72** | 15.98 | 0.45 | 0.17 | 1.00 | 0/6 |  | én kamp (GW1) står for 68% av xGI |
| Mukiele | SUN | DEF | 5.4 | 4.14 | 4.16 | 3.92 | 3.90 | 4.46 | **20.59** | 18.33 | 0.23 | 0.10 | 0.94 | 3/5 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv | én kamp (GW4) står for 64% av xGI |
| Khalaili | CRY | DEF | 5.0 | 4.12 | 4.00 | 3.86 | 4.08 | 4.50 | **20.56** | 18.64 | 0.32 | 0.23 | 0.94 | 2/5 |  | — |
| Bogle | LEE | DEF | 4.7 | 3.85 | 3.71 | 4.53 | 3.58 | 4.61 | **20.28** | 17.80 | 0.32 | 0.16 | 1.00 | 0/6 |  | én kamp (GW3) står for 57% av xGI |
| Thomas | COV | DEF | 4.0 | 4.11 | 4.14 | 3.87 | 4.04 | 3.77 | **19.92** | 19.04 | 0.14 | 0.08 | 1.00 | 4/6 |  | — |
| Murillo | NFO | DEF | 5.5 | 4.23 | 3.65 | 3.82 | 3.90 | 4.13 | **19.72** | 19.23 | 0.18 | 0.16 | 1.00 | 5/6 |  | — |
| Muharemović | LEE | DEF | 5.0 | 3.69 | 3.54 | 4.33 | 3.42 | 4.35 | **19.33** | 18.25 | 0.09 | 0.03 | 1.00 | 4/6 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 3.78 | 3.87 | 3.73 | 3.73 | 3.97 | **19.07** | 17.60 | 0.35 | 0.28 | 1.00 | 0/6 |  | — |
| Hill | BOU | DEF | 5.5 | 3.35 | 4.01 | 3.87 | 3.93 | 3.69 | **18.84** | 17.35 | 0.13 | 0.01 | 1.00 | 4/6 |  | — |
| Vuskovic | BHA | DEF | 5.1 | 3.53 | 3.17 | 3.70 | 4.11 | 4.06 | **18.57** | 18.00 | 0.14 | 0.11 | 1.00 | 3/6 |  | — |
| Mitchell | CRY | DEF | 4.5 | 3.67 | 3.65 | 3.47 | 3.69 | 4.07 | **18.55** | 16.60 | 0.19 | 0.08 | 1.00 | 1/6 |  | én kamp (GW3) står for 64% av xGI |
| Justin | LEE | DEF | 4.5 | 3.49 | 3.34 | 4.13 | 3.22 | 4.17 | **18.36** | 18.12 | 0.14 | 0.11 | 1.00 | 2/6 |  | — |

### MID

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Saka | ARS | MID | 9.6 | 6.83 | 5.85 | 7.09 | 6.44 | 6.29 | **32.50** | 29.37 | 0.83 | 0.69 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| B.Fernandes ★ | MUN | MID | 11.8 | 6.37 | 5.85 | 6.42 | 5.57 | 6.43 | **30.64** | 24.07 | 0.67 | 0.31 | 1.00 | 0/6 | 1 | én kamp (GW2) står for 62% av xGI | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 5.96 | 5.48 | 6.01 | 5.23 | 6.01 | **28.69** | 23.68 | 0.70 | 0.45 | 1.00 | 0/6 | 2 | — |
| E.Le Fée | SUN | MID | 5.7 | 5.20 | 5.10 | 5.24 | 4.91 | 5.21 | **25.67** | 22.00 | 0.64 | 0.47 | 1.00 | 0/6 | 2 | — |
| Rogers | CHE | MID | 7.9 | 5.20 | 5.11 | 4.84 | 5.19 | 4.91 | **25.25** | 23.59 | 0.55 | 0.43 | 1.00 | 1/6 |  | — |
| Ødegaard ★ | ARS | MID | 6.8 | 5.22 | 4.58 | 5.41 | 4.96 | 4.85 | **25.02** | 21.36 | 0.65 | 0.40 | 1.00 | 0/6 | 3 | — |
| Gibbs-White ★ | NFO | MID | 8.0 | 4.01 | 5.09 | 5.16 | 5.05 | 5.44 | **24.76** | 23.29 | 0.59 | 0.49 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) | FPL-sjansen gjelder GW7; brukt for GW8 | GW8: FPL-sjanse 75 % |
| Groß | BHA | MID | 6.1 | 4.27 | 4.22 | 4.81 | 4.70 | 4.99 | **22.98** | 20.68 | 0.51 | 0.41 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Palmer | CHE | MID | 9.7 | 4.71 | 4.62 | 4.38 | 4.69 | 4.44 | **22.84** | 21.51 | 0.37 | 0.28 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Rudoni | COV | MID | 4.9 | 4.62 | 4.56 | 4.38 | 4.73 | 4.27 | **22.56** | 20.57 | 0.68 | 0.53 | 0.94 | 1/5 | 1 | første straffeskytter (penalties_order 1) |
| Enciso | IPS | MID | 5.5 | 4.47 | 4.37 | 4.43 | 4.13 | 4.48 | **21.88** | 20.75 | 0.55 | 0.47 | 1.00 | 0/6 |  | — |
| Cunha | MUN | MID | 7.9 | 4.50 | 4.22 | 4.54 | 4.10 | 4.50 | **21.87** | 21.44 | 0.32 | 0.28 | 1.00 | 1/6 |  | — |
| Stach | LEE | MID | 6.0 | 4.22 | 4.22 | 4.46 | 4.21 | 4.60 | **21.70** | 20.83 | 0.24 | 0.18 | 1.00 | 3/6 |  | — |
| Tavernier | BOU | MID | 6.1 | 4.06 | 4.42 | 4.38 | 4.49 | 4.19 | **21.56** | 18.95 | 0.48 | 0.35 | 1.00 | 0/6 | 3 | — |
| Cherki | MCI | MID | 7.9 | 4.21 | 4.42 | 4.21 | 4.53 | 3.53 | **20.91** | 19.82 | 0.69 | 0.61 | 0.94 | 0/5 |  | — |

### FWD

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.7 | 6.50 | 7.01 | 6.56 | 7.12 | 5.23 | **32.42** | 30.37 | 0.91 | 0.78 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 4.16 | 5.28 | 5.66 | 5.12 | 5.17 | **25.39** | 22.47 | 0.82 | 0.64 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| João Pedro ★ | CHE | FWD | 7.8 | 5.11 | 5.14 | 4.80 | 5.17 | 4.91 | **25.12** | 22.73 | 0.64 | 0.47 | 1.00 | 0/5 |  | — |
| Gonzalo | FUL | FWD | 6.1 | 4.86 | 4.70 | 5.30 | 4.48 | 5.06 | **24.41** | 22.53 | 0.63 | 0.54 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Thiago | BRE | FWD | 7.8 | 4.87 | 5.07 | 4.60 | 5.11 | 4.54 | **24.19** | 22.37 | 0.59 | 0.48 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Calvert-Lewin | LEE | FWD | 6.0 | 4.19 | 4.24 | 4.46 | 4.25 | 4.73 | **21.88** | 20.66 | 0.54 | 0.46 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Havertz | ARS | FWD | 7.5 | 4.31 | 3.80 | 4.44 | 4.13 | 4.06 | **20.75** | 19.53 | 0.40 | 0.31 | 1.00 | 0/6 |  | — |
| Delap | NFO | FWD | 5.5 | 4.21 | 4.05 | 4.09 | 3.99 | 4.30 | **20.65** | 18.28 | 0.60 | 0.40 | 0.91 | 0/4 | 3 | — |
| Wissa | NEW | FWD | 6.2 | 4.14 | 4.34 | 4.01 | 3.58 | 3.96 | **20.03** | 18.24 | 0.45 | 0.33 | 1.00 | 0/6 | 2 | — |
| Evanilson | BOU | FWD | 6.1 | 3.77 | 4.05 | 4.03 | 4.14 | 3.86 | **19.85** | 18.77 | 0.37 | 0.30 | 1.00 | 0/6 |  | — |

## Uavklart fravær i troppen og valgte spillere

Ingen.

