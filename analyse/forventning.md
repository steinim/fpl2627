# Forventede poeng — generert

*Generert 17.10.2026 kl. 22:20 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–6 (data_checked). Horisont: GW8–12. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–6 summerer til sesongtotalene for 333 spillere, 19 felt; 334 spillere på lag som har spilt i GW7 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 17.10.2026 21:43 UTC, 0.6 t gammelt ved kjøring
- ✅ Lagstyrke-prior fra context/lagstyrke-prior.csv (ρ = 0.5); opprykksprior brukt for COV, HUL, IPS

## Modell og estimerte parametre

Formelen står i toppen av `scripts/forventning.py`.

- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel 0.7, start- og spillesannsynlighet kalibrert per runde fram (fast starter: P(start) 0.92 i første runde etter grunnlaget, 0.82 i den 7.), krymping av spillerrater mot posisjon og startpris 3 kamper, krymping av DC-treffrate mot posisjonssnitt 4 kamper, CS-faktor 1.046, målfaktor GKP 1.0, DEF 0.799, MID 0.987, FWD 1.001; assistfaktor GKP 1.376, DEF 1.202, MID 1.349, FWD 2.09.
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

- Snittet ligger 4–6 % under fasit i tilbaketesten. Avviket sitter hos spillere med lav startandel (under 0,2: 16 % under); faste startere treffer innenfor 1 %. Start- og spillesannsynligheten er kalibrert uten historisk skadestatus, så FPL-status kommer i tillegg — for en flagget spiller telles en del av skaderisikoen to ganger.
- Straffer ligger i xG slik de har falt. Straffeskytterrolle vises i kolonnen «Str», men modelleres ikke separat. Bommet straffe (−2) er ikke med.
- Tilgjengelighet utover neste runde bygger på FPL-status og -nyhet. Returdatoen i nyheten tolkes som første dag spilleren er tilgjengelig. Tolkningen står i flagget.
- Spillere uten telte kamper i grunnlaget (nysignert, skadet hele perioden) får ingen forventning. De må vurderes for hånd.
- I dobbelrunder er minuttfordelingen tilnærmet. En spiller som har byttet klubb i grunnlaget, får rater som blander to roller. Begge deler flagges.
- Modellen forklarer om lag 20 % av variansen i poeng for én runde og 30–40 % over fem. Over fem runder bommer den i snitt med 5,1–5,8 poeng per spiller.

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

## Troppen (picks GW7)

Bytter gjort etter GW7-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Verbruggen ★ | BHA | GKP | 4.6 | 2.67 | 2.46 | 2.59 | 2.80 | 2.70 | **13.22** | 12.82 | 0.03 | 0.00 | 1.00 |  |  | — |
| Kinsky ★ | TOT | GKP | 4.5 | 2.55 | 2.70 | 2.58 | 2.77 | 2.54 | **13.14** | 13.15 | 0.00 | 0.00 | 1.00 |  |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 4.40 | 3.68 | 4.50 | 3.79 | 3.57 | **19.93** | 18.81 | 0.34 | 0.28 | 1.00 | 0/6 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 3.68 | 3.63 | 3.34 | 3.44 | 3.18 | **17.25** | 16.50 | 0.14 | 0.08 | 1.00 | 4/6 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 3.38 | 3.39 | 3.22 | 3.18 | 3.34 | **16.51** | 15.24 | 0.35 | 0.28 | 1.00 | 0/6 |  | — |
| Diop ★ | IPS | DEF | 4.0 | 2.96 | 3.04 | 2.83 | 2.94 | 2.96 | **14.72** | 14.61 | 0.04 | 0.03 | 1.00 | 3/6 |  | — |
| Egan ★ | HUL | DEF | 4.1 | 2.70 | 3.12 | 2.29 | 2.46 | 2.53 | **13.09** | 12.81 | 0.04 | 0.01 | 1.00 | 3/6 |  | — |
| Saka ★ | ARS | MID | 9.6 | 6.09 | 5.12 | 6.09 | 5.47 | 5.28 | **28.04** | 25.35 | 0.83 | 0.69 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| B.Fernandes ★ | MUN | MID | 11.8 | 5.68 | 5.11 | 5.52 | 4.73 | 5.40 | **26.44** | 20.81 | 0.67 | 0.31 | 1.00 | 0/6 | 1 | én kamp (GW2) står for 62% av xGI | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 5.32 | 4.80 | 5.16 | 4.45 | 5.05 | **24.77** | 20.47 | 0.70 | 0.45 | 1.00 | 0/6 | 2 | — |
| Groß ★ | BHA | MID | 6.1 | 3.81 | 3.70 | 4.14 | 4.00 | 4.20 | **19.85** | 17.88 | 0.51 | 0.41 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Slater ★ | HUL | MID | 4.5 | 2.60 | 2.66 | 2.22 | 2.44 | 2.40 | **12.31** | 11.65 | 0.14 | 0.08 | 1.00 | 0/6 |  | — |
| Haaland ★ | MCI | FWD | 15.7 | 5.80 | 6.13 | 5.63 | 6.04 | 4.40 | **28.00** | 26.24 | 0.91 | 0.78 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 3.72 | 4.62 | 4.87 | 4.35 | 4.35 | **21.91** | 19.41 | 0.82 | 0.64 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| João Pedro ★ | CHE | FWD | 7.8 | 4.57 | 4.50 | 4.13 | 4.39 | 4.13 | **21.71** | 19.66 | 0.64 | 0.47 | 1.00 | 0/5 |  | — |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raya | ARS | GKP | 6.1 | 3.40 | 3.05 | 3.43 | 3.01 | 2.88 | **15.77** | 15.75 | 0.00 | 0.00 | 1.00 |  |  | — |
| Trafford | LEE | GKP | 5.0 | 3.19 | 3.08 | 3.31 | 2.96 | 3.23 | **15.76** | 15.75 | 0.00 | 0.00 | 1.00 |  |  | — |
| Kelleher | BRE | GKP | 5.0 | 3.16 | 3.04 | 2.83 | 3.01 | 2.79 | **14.83** | 14.81 | 0.00 | 0.00 | 1.00 |  |  | — |
| Donnarumma | MCI | GKP | 5.5 | 3.11 | 2.92 | 2.92 | 3.03 | 2.78 | **14.76** | 14.76 | 0.00 | 0.00 | 1.00 |  |  | — |
| Lammens | MUN | GKP | 4.9 | 3.02 | 2.81 | 3.02 | 2.77 | 2.75 | **14.37** | 14.37 | 0.00 | 0.00 | 1.00 |  |  | — |
| Leno | FUL | GKP | 4.5 | 3.03 | 2.87 | 2.86 | 2.58 | 2.77 | **14.11** | 14.12 | 0.00 | 0.00 | 1.00 |  |  | — |
| Horníček | NEW | GKP | 5.0 | 2.88 | 2.97 | 2.81 | 2.74 | 2.65 | **14.05** | 14.05 | 0.00 | 0.00 | 1.00 |  |  | — |
| Tzolakis | HUL | GKP | 4.7 | 2.85 | 2.99 | 2.69 | 2.69 | 2.69 | **13.92** | 13.92 | 0.00 | 0.00 | 1.00 |  |  | — |

### DEF

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calafiori ★ | ARS | DEF | 5.9 | 4.40 | 3.68 | 4.50 | 3.79 | 3.57 | **19.93** | 18.81 | 0.34 | 0.28 | 1.00 | 0/6 |  | — |
| Silva | BOU | DEF | 5.0 | 3.42 | 4.00 | 3.81 | 3.83 | 3.53 | **18.60** | 16.99 | 0.27 | 0.16 | 1.00 | 4/6 |  | én kamp (GW4) står for 50% av xGI |
| Gabriel | ARS | DEF | 7.9 | 3.97 | 3.36 | 4.07 | 3.41 | 3.21 | **18.02** | 17.41 | 0.12 | 0.08 | 1.00 | 2/6 |  | — |
| De Cuyper | BHA | DEF | 5.2 | 3.44 | 3.06 | 3.62 | 3.87 | 3.89 | **17.89** | 13.83 | 0.45 | 0.17 | 1.00 | 0/6 |  | én kamp (GW1) står for 68% av xGI |
| Bogle | LEE | DEF | 4.7 | 3.44 | 3.25 | 3.90 | 3.06 | 3.88 | **17.53** | 15.40 | 0.32 | 0.16 | 1.00 | 0/6 |  | én kamp (GW3) står for 57% av xGI |
| Thomas ★ | COV | DEF | 4.0 | 3.68 | 3.63 | 3.34 | 3.44 | 3.18 | **17.25** | 16.50 | 0.14 | 0.08 | 1.00 | 4/6 |  | — |
| Khalaili | CRY | DEF | 5.0 | 3.64 | 3.42 | 3.22 | 3.34 | 3.63 | **17.24** | 15.62 | 0.32 | 0.23 | 0.94 | 2/5 |  | — |
| Murillo | NFO | DEF | 5.5 | 3.78 | 3.21 | 3.29 | 3.32 | 3.48 | **17.07** | 16.65 | 0.18 | 0.16 | 1.00 | 5/6 |  | — |
| Mukiele | SUN | DEF | 5.4 | 3.62 | 3.51 | 3.21 | 3.13 | 3.51 | **16.98** | 15.13 | 0.23 | 0.10 | 0.94 | 3/5 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv | én kamp (GW4) står for 64% av xGI |
| Muharemović | LEE | DEF | 5.0 | 3.31 | 3.11 | 3.73 | 2.91 | 3.67 | **16.72** | 15.79 | 0.09 | 0.03 | 1.00 | 4/6 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 3.38 | 3.39 | 3.22 | 3.18 | 3.34 | **16.51** | 15.24 | 0.35 | 0.28 | 1.00 | 0/6 |  | — |
| Hill | BOU | DEF | 5.5 | 3.00 | 3.52 | 3.34 | 3.34 | 3.11 | **16.30** | 15.02 | 0.13 | 0.01 | 1.00 | 4/6 |  | — |
| Vuskovic | BHA | DEF | 5.1 | 3.16 | 2.79 | 3.19 | 3.50 | 3.42 | **16.06** | 15.57 | 0.14 | 0.11 | 1.00 | 3/6 |  | — |
| Mitchell | CRY | DEF | 4.5 | 3.29 | 3.20 | 2.99 | 3.14 | 3.43 | **16.06** | 14.39 | 0.19 | 0.08 | 1.00 | 1/6 |  | én kamp (GW3) står for 64% av xGI |
| Justin | LEE | DEF | 4.5 | 3.13 | 2.93 | 3.56 | 2.75 | 3.51 | **15.88** | 15.68 | 0.14 | 0.11 | 1.00 | 2/6 |  | — |

### MID

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Saka ★ | ARS | MID | 9.6 | 6.09 | 5.12 | 6.09 | 5.47 | 5.28 | **28.04** | 25.35 | 0.83 | 0.69 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| B.Fernandes ★ | MUN | MID | 11.8 | 5.68 | 5.11 | 5.52 | 4.73 | 5.40 | **26.44** | 20.81 | 0.67 | 0.31 | 1.00 | 0/6 | 1 | én kamp (GW2) står for 62% av xGI | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 5.32 | 4.80 | 5.16 | 4.45 | 5.05 | **24.77** | 20.47 | 0.70 | 0.45 | 1.00 | 0/6 | 2 | — |
| E.Le Fée | SUN | MID | 5.7 | 4.65 | 4.46 | 4.51 | 4.18 | 4.39 | **22.18** | 19.03 | 0.64 | 0.47 | 1.00 | 0/6 | 2 | — |
| Rogers | CHE | MID | 7.9 | 4.64 | 4.48 | 4.16 | 4.41 | 4.13 | **21.82** | 20.40 | 0.55 | 0.43 | 1.00 | 1/6 |  | — |
| Ødegaard | ARS | MID | 6.8 | 4.66 | 4.01 | 4.65 | 4.21 | 4.08 | **21.62** | 18.49 | 0.65 | 0.40 | 1.00 | 0/6 | 3 | — |
| Gibbs-White | NFO | MID | 8.0 | 3.58 | 4.45 | 4.44 | 4.30 | 4.57 | **21.35** | 20.09 | 0.59 | 0.49 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) | GW8: FPL-sjanse 75 % |
| Groß ★ | BHA | MID | 6.1 | 3.81 | 3.70 | 4.14 | 4.00 | 4.20 | **19.85** | 17.88 | 0.51 | 0.41 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Palmer | CHE | MID | 9.7 | 4.21 | 4.05 | 3.77 | 3.99 | 3.74 | **19.76** | 18.61 | 0.37 | 0.28 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Rudoni | COV | MID | 4.9 | 4.08 | 3.91 | 3.66 | 3.88 | 3.46 | **18.98** | 17.32 | 0.68 | 0.53 | 0.94 | 1/5 | 1 | første straffeskytter (penalties_order 1) |
| Enciso | IPS | MID | 5.5 | 4.00 | 3.83 | 3.82 | 3.52 | 3.77 | **18.93** | 17.96 | 0.55 | 0.47 | 1.00 | 0/6 |  | — |
| Cunha | MUN | MID | 7.9 | 4.02 | 3.70 | 3.91 | 3.50 | 3.79 | **18.92** | 18.55 | 0.32 | 0.28 | 1.00 | 1/6 |  | — |
| Stach | LEE | MID | 6.0 | 3.77 | 3.70 | 3.84 | 3.58 | 3.87 | **18.76** | 18.01 | 0.24 | 0.18 | 1.00 | 3/6 |  | — |
| Tavernier | BOU | MID | 6.1 | 3.63 | 3.88 | 3.78 | 3.82 | 3.53 | **18.64** | 16.41 | 0.48 | 0.35 | 1.00 | 0/6 | 3 | — |
| Gomez | BHA | MID | 5.0 | 3.48 | 3.37 | 3.64 | 3.57 | 3.67 | **17.73** | 16.75 | 0.31 | 0.24 | 1.00 | 2/6 |  | — |

### FWD

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.7 | 5.80 | 6.13 | 5.63 | 6.04 | 4.40 | **28.00** | 26.24 | 0.91 | 0.78 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 3.72 | 4.62 | 4.87 | 4.35 | 4.35 | **21.91** | 19.41 | 0.82 | 0.64 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| João Pedro ★ | CHE | FWD | 7.8 | 4.57 | 4.50 | 4.13 | 4.39 | 4.13 | **21.71** | 19.66 | 0.64 | 0.47 | 1.00 | 0/5 |  | — |
| Gonzalo | FUL | FWD | 6.1 | 4.34 | 4.12 | 4.56 | 3.81 | 4.26 | **21.10** | 19.48 | 0.63 | 0.54 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Thiago | BRE | FWD | 7.8 | 4.35 | 4.44 | 3.96 | 4.34 | 3.82 | **20.92** | 19.35 | 0.59 | 0.48 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Calvert-Lewin | LEE | FWD | 6.0 | 3.75 | 3.72 | 3.84 | 3.62 | 3.98 | **18.91** | 17.87 | 0.54 | 0.46 | 1.00 | 0/6 | 1 | første straffeskytter (penalties_order 1) |
| Havertz | ARS | FWD | 7.5 | 3.86 | 3.33 | 3.83 | 3.52 | 3.42 | **17.96** | 16.91 | 0.40 | 0.31 | 1.00 | 0/6 |  | — |
| Delap | NFO | FWD | 5.5 | 3.73 | 3.48 | 3.43 | 3.29 | 3.49 | **17.42** | 15.45 | 0.60 | 0.40 | 0.91 | 0/4 | 3 | — |
| Wissa | NEW | FWD | 6.2 | 3.70 | 3.81 | 3.45 | 3.06 | 3.34 | **17.36** | 15.82 | 0.45 | 0.33 | 1.00 | 0/6 | 2 | — |
| Evanilson | BOU | FWD | 6.1 | 3.38 | 3.55 | 3.48 | 3.53 | 3.25 | **17.18** | 16.25 | 0.37 | 0.30 | 1.00 | 0/6 |  | — |

## Uavklart fravær i troppen og valgte spillere

Ingen.

