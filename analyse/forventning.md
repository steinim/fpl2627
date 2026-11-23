# Forventede poeng — generert

*Generert 23.11.2026 kl. 10:43 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–10 (data_checked). Horisont: GW12–16. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–10 summerer til sesongtotalene for 54 spillere, 19 felt; 620 spillere på lag som har spilt i GW11 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 23.11.2026 09:45 UTC, 1.0 t gammelt ved kjøring
- ✅ Lagstyrke-prior fra context/lagstyrke-prior.csv (ρ = 0.5); opprykksprior brukt for COV, HUL, IPS

## Modell og estimerte parametre

Formelen står i toppen av `scripts/forventning.py`.

- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel 0.7, start- og spillesannsynlighet kalibrert per runde fram (fast starter: P(start) 0.92 i første runde etter grunnlaget, 0.82 i den 7.), krymping av spillerrater mot posisjon og startpris 3 kamper, krymping av DC-treffrate mot posisjonssnitt 4 kamper, CS-faktor 1.046, målfaktor GKP 1.0, DEF 0.799, MID 0.987, FWD 1.001; assistfaktor GKP 1.376, DEF 1.202, MID 1.349, FWD 2.09.
- **Estimert fra sesongens data ved hver kjøring:**
  - Liga-xG per lag og kamp μ = 1.474. Bane: hjemme ×1.075, borte ×0.925.
  - Lagstyrke krympet mot forrige sesong (dempet med ρ = 0.5) med k = 15 kamper (angrep) og 30 (forsvar).
  - Bonus: k = 38.0 kamper for spillerens eget avvik. Koeffisienter per posisjon (konstant, så felt i rekkefølge):
    - GKP (n = 200): konstant -0.270; cs +1.015, redninger +0.093
    - DEF (n = 801): konstant -0.052; mal +1.214, assist +0.468, cs +0.534, dc +0.093
    - MID (n = 878): konstant +0.010; mal +1.427, assist +0.520, dc +0.061
    - FWD (n = 187): konstant +0.025; mal +1.662, assist +0.266, dc -0.025
  - Gule kort krympes med k = 7.2 kamper mot posisjonssnitt. Strafferedninger per keeper-90: 0.010.

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
| MCI | 1.21 | 0.90 |
| BHA | 1.16 | 0.95 |
| MUN | 1.16 | 1.05 |
| BOU | 1.13 | 0.96 |
| ARS | 1.11 | 0.71 |
| LIV | 1.08 | 0.93 |
| CHE | 1.08 | 1.00 |
| BRE | 1.08 | 1.01 |
| CRY | 1.02 | 1.14 |
| NFO | 1.00 | 0.96 |
| SUN | 0.99 | 1.02 |
| AVL | 0.98 | 1.07 |
| LEE | 0.96 | 0.96 |
| NEW | 0.94 | 1.06 |
| EVE | 0.92 | 1.03 |
| FUL | 0.91 | 0.99 |
| IPS | 0.90 | 1.13 |
| TOT | 0.84 | 0.94 |
| COV | 0.81 | 1.06 |
| HUL | 0.77 | 1.06 |

## Troppen (picks GW11)

Bytter gjort etter GW11-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Verbruggen ★ | BHA | GKP | 4.7 | 3.05 | 2.61 | 2.68 | 2.93 | 2.93 | **14.20** | 13.91 | 0.02 | 0.00 | 1.00 |  |  | — |
| Kinsky ★ | TOT | GKP | 4.4 | 2.64 | 2.89 | 2.58 | 2.83 | 2.39 | **13.33** | 13.33 | 0.00 | 0.00 | 1.00 |  |  | — |
| Van Hecke ★ | TOT | DEF | 5.2 | 3.58 | 4.07 | 3.34 | 3.90 | 3.13 | **18.02** | 16.44 | 0.24 | 0.14 | 1.00 | 4/10 |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 3.35 | 3.22 | 3.54 | 3.41 | 3.42 | **16.93** | 16.14 | 0.26 | 0.21 | 0.85 | 0/9 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 3.17 | 3.65 | 2.79 | 3.37 | 2.73 | **15.71** | 15.08 | 0.13 | 0.09 | 1.00 | 5/8 |  | — |
| Diop ★ | IPS | DEF | 3.9 | 2.94 | 2.92 | 2.54 | 2.89 | 2.14 | **13.42** | 13.31 | 0.03 | 0.02 | 1.00 | 5/10 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 2.32 | 2.96 | 2.50 | 3.03 | 2.10 | **12.92** | 12.01 | 0.23 | 0.18 | 1.00 | 0/10 |  | GW12: FPL-sjanse 75 % |
| E.Le Fée ★ | SUN | MID | 5.7 | 4.87 | 4.25 | 4.54 | 4.62 | 5.05 | **23.32** | 21.20 | 0.59 | 0.49 | 1.00 | 1/10 | 1 | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 5.02 | 4.63 | 5.09 | 4.67 | 3.51 | **22.92** | 20.03 | 0.60 | 0.44 | 1.00 | 0/10 | 2 | — |
| B.Fernandes ★ | MUN | MID | 11.6 | 4.94 | 4.58 | 5.10 | 4.69 | 3.45 | **22.76** | 19.27 | 0.68 | 0.45 | 0.85 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Tavernier ★ | BOU | MID | 6.7 | 4.39 | 4.53 | 4.88 | 3.49 | 4.76 | **22.04** | 20.21 | 0.61 | 0.51 | 1.00 | 1/10 | 3 | — |
| Groß ★ | BHA | MID | 6.3 | 4.55 | 3.78 | 3.74 | 4.26 | 4.46 | **20.79** | 18.61 | 0.54 | 0.42 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Haaland ★ | MCI | FWD | 15.8 | 4.32 | 5.68 | 5.21 | 5.70 | 5.88 | **26.78** | 25.38 | 0.80 | 0.72 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 5.13 | 5.00 | 5.18 | 4.50 | 4.48 | **24.30** | 22.58 | 0.82 | 0.73 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson ★ | BOU | FWD | 6.6 | 4.15 | 4.34 | 4.59 | 3.29 | 4.49 | **20.86** | 18.96 | 0.59 | 0.48 | 1.00 | 0/10 |  | — |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trafford | LEE | GKP | 5.1 | 3.59 | 3.12 | 3.36 | 3.08 | 3.28 | **16.42** | 16.41 | 0.00 | 0.00 | 1.00 |  |  | — |
| Tzolakis | HUL | GKP | 4.7 | 3.18 | 3.21 | 3.05 | 3.24 | 2.98 | **15.66** | 15.66 | 0.00 | 0.00 | 1.00 |  |  | — |
| Lammens | MUN | GKP | 4.8 | 2.98 | 2.91 | 3.13 | 2.77 | 2.69 | **14.50** | 14.44 | 0.00 | 0.00 | 1.00 |  |  | — |
| Horníček | NEW | GKP | 5.0 | 2.92 | 2.92 | 2.97 | 2.90 | 2.78 | **14.50** | 14.50 | 0.00 | 0.00 | 1.00 |  |  | — |
| Raya | ARS | GKP | 6.3 | 2.29 | 2.96 | 3.22 | 3.00 | 2.93 | **14.41** | 14.39 | 0.00 | 0.00 | 1.00 |  |  | GW12: FPL-sjanse 75 % |
| Suzuki | AVL | GKP | 5.1 | 3.01 | 3.01 | 2.85 | 2.85 | 2.66 | **14.37** | 14.36 | 0.00 | 0.00 | 0.99 |  |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Donnarumma | MCI | GKP | 5.4 | 2.71 | 2.98 | 2.64 | 2.77 | 3.15 | **14.25** | 14.25 | 0.00 | 0.00 | 1.00 |  |  | — |
| Verbruggen ★ | BHA | GKP | 4.7 | 3.05 | 2.61 | 2.68 | 2.93 | 2.93 | **14.20** | 13.91 | 0.02 | 0.00 | 1.00 |  |  | — |

### DEF

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel | ARS | DEF | 8.1 | 4.02 | 3.85 | 4.20 | 4.01 | 4.00 | **20.09** | 19.34 | 0.17 | 0.13 | 1.00 | 5/10 |  | — |
| De Cuyper | BHA | DEF | 5.5 | 4.33 | 3.24 | 3.42 | 4.11 | 4.25 | **19.36** | 16.53 | 0.43 | 0.27 | 1.00 | 0/10 |  | — |
| Murillo | NFO | DEF | 5.5 | 3.94 | 4.13 | 3.61 | 3.54 | 4.04 | **19.27** | 18.79 | 0.19 | 0.17 | 1.00 | 7/10 |  | — |
| Silva | BOU | DEF | 5.1 | 3.75 | 3.57 | 4.35 | 3.02 | 4.17 | **18.86** | 17.67 | 0.17 | 0.10 | 1.00 | 7/10 |  | — |
| Hill | BOU | DEF | 5.6 | 3.63 | 3.43 | 4.19 | 2.94 | 4.01 | **18.19** | 17.36 | 0.13 | 0.06 | 1.00 | 6/10 |  | én kamp (GW2) står for 56% av xGI |
| Van Hecke ★ | TOT | DEF | 5.2 | 3.58 | 4.07 | 3.34 | 3.90 | 3.13 | **18.02** | 16.44 | 0.24 | 0.14 | 1.00 | 4/10 |  | — |
| Muharemović | LEE | DEF | 5.1 | 4.23 | 2.97 | 3.92 | 3.10 | 3.75 | **17.98** | 17.33 | 0.09 | 0.05 | 1.00 | 7/10 |  | — |
| Vuskovic | BHA | DEF | 5.3 | 3.92 | 3.03 | 3.21 | 3.75 | 3.81 | **17.71** | 17.12 | 0.15 | 0.11 | 1.00 | 4/10 |  | — |
| Jacquet | LIV | DEF | 5.1 | 3.44 | 3.58 | 3.00 | 3.49 | 3.70 | **17.21** | 16.81 | 0.08 | 0.06 | 1.00 | 5/10 |  | — |
| Konsa | ARS | DEF | 4.9 | 3.55 | 3.33 | 3.61 | 3.35 | 3.28 | **17.12** | 16.49 | 0.08 | 0.04 | 0.97 | 4/8 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Virgil | LIV | DEF | 6.4 | 3.42 | 3.55 | 2.97 | 3.47 | 3.68 | **17.09** | 16.72 | 0.07 | 0.05 | 1.00 | 6/10 |  | — |
| Bogle | LEE | DEF | 4.8 | 4.10 | 2.68 | 3.84 | 2.83 | 3.59 | **17.05** | 15.46 | 0.29 | 0.20 | 1.00 | 0/10 |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 3.35 | 3.22 | 3.54 | 3.41 | 3.42 | **16.93** | 16.14 | 0.26 | 0.21 | 0.85 | 0/9 |  | — |
| N.Williams | NFO | DEF | 4.8 | 3.42 | 3.62 | 3.11 | 3.04 | 3.54 | **16.72** | 16.09 | 0.21 | 0.18 | 1.00 | 2/10 |  | — |
| Justin | LEE | DEF | 4.5 | 3.99 | 2.68 | 3.70 | 2.83 | 3.51 | **16.71** | 16.03 | 0.17 | 0.12 | 1.00 | 3/10 |  | — |

### MID

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E.Le Fée ★ | SUN | MID | 5.7 | 4.87 | 4.25 | 4.54 | 4.62 | 5.05 | **23.32** | 21.20 | 0.59 | 0.49 | 1.00 | 1/10 | 1 | første straffeskytter (penalties_order 1) |
| Mbeumo ★ | MUN | MID | 7.8 | 5.02 | 4.63 | 5.09 | 4.67 | 3.51 | **22.92** | 20.03 | 0.60 | 0.44 | 1.00 | 0/10 | 2 | — |
| Gibbs-White | NFO | MID | 7.8 | 4.84 | 4.55 | 4.49 | 4.25 | 4.67 | **22.79** | 21.82 | 0.54 | 0.48 | 1.00 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| B.Fernandes ★ | MUN | MID | 11.6 | 4.94 | 4.58 | 5.10 | 4.69 | 3.45 | **22.76** | 19.27 | 0.68 | 0.45 | 0.85 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Tavernier ★ | BOU | MID | 6.7 | 4.39 | 4.53 | 4.88 | 3.49 | 4.76 | **22.04** | 20.21 | 0.61 | 0.51 | 1.00 | 1/10 | 3 | — |
| Groß ★ | BHA | MID | 6.3 | 4.55 | 3.78 | 3.74 | 4.26 | 4.46 | **20.79** | 18.61 | 0.54 | 0.42 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Ødegaard | ARS | MID | 6.7 | 4.19 | 4.04 | 3.92 | 4.16 | 4.30 | **20.60** | 18.45 | 0.53 | 0.40 | 1.00 | 0/10 | 3 | — |
| Rogers | CHE | MID | 8.3 | 3.90 | 4.63 | 4.02 | 3.54 | 4.29 | **20.37** | 19.28 | 0.47 | 0.39 | 1.00 | 1/10 |  | — |
| Palmer | CHE | MID | 9.8 | 3.74 | 4.43 | 3.86 | 3.39 | 4.11 | **19.54** | 18.18 | 0.38 | 0.31 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| McGinn | AVL | MID | 5.5 | 3.81 | 3.89 | 4.03 | 3.56 | 3.35 | **18.64** | 17.14 | 0.46 | 0.38 | 0.89 | 0/9 | 1 | første straffeskytter (penalties_order 1) |
| Rayan | BOU | MID | 6.3 | 3.63 | 3.70 | 3.96 | 2.99 | 3.86 | **18.15** | 16.78 | 0.33 | 0.26 | 1.00 | 1/10 |  | — |
| Rudoni | COV | MID | 4.9 | 3.55 | 4.08 | 3.47 | 3.79 | 3.24 | **18.13** | 16.80 | 0.48 | 0.39 | 0.99 | 1/9 | 1 | første straffeskytter (penalties_order 1) |
| Iwobi | FUL | MID | 5.4 | 3.84 | 3.54 | 3.59 | 3.76 | 3.39 | **18.12** | 16.88 | 0.47 | 0.38 | 1.00 | 0/10 | 3 | — |
| Enciso | IPS | MID | 5.5 | 3.97 | 3.61 | 3.33 | 3.79 | 3.20 | **17.90** | 17.21 | 0.46 | 0.41 | 1.00 | 0/10 |  | — |
| Wirtz | LIV | MID | 7.4 | 3.54 | 3.73 | 3.33 | 3.53 | 3.51 | **17.63** | 17.47 | 0.35 | 0.33 | 1.00 | 0/10 | 4 | — |

### FWD

| Spiller | Lag | Pos | Pris | GW12 | GW13 | GW14 | GW15 | GW16 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.8 | 4.32 | 5.68 | 5.21 | 5.70 | 5.88 | **26.78** | 25.38 | 0.80 | 0.72 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 5.13 | 5.00 | 5.18 | 4.50 | 4.48 | **24.30** | 22.58 | 0.82 | 0.73 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson ★ | BOU | FWD | 6.6 | 4.15 | 4.34 | 4.59 | 3.29 | 4.49 | **20.86** | 18.96 | 0.59 | 0.48 | 1.00 | 0/10 |  | — |
| Isak | LIV | FWD | 9.3 | 4.16 | 4.44 | 3.93 | 4.14 | 4.04 | **20.72** | 19.72 | 0.62 | 0.56 | 0.93 | 0/9 | 2 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |
| N.Jackson | AVL | FWD | 7.3 | 4.12 | 4.18 | 4.39 | 3.78 | 3.61 | **20.07** | 18.22 | 0.54 | 0.43 | 1.00 | 0/9 | 3 | — |
| Calvert-Lewin | LEE | FWD | 6.0 | 4.31 | 3.49 | 4.31 | 3.45 | 3.88 | **19.44** | 18.58 | 0.48 | 0.43 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Gonzalo | FUL | FWD | 5.8 | 4.08 | 3.63 | 3.75 | 4.00 | 3.53 | **18.99** | 17.91 | 0.53 | 0.46 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| Delap | NFO | FWD | 5.3 | 3.82 | 3.52 | 3.51 | 3.30 | 3.57 | **17.71** | 16.14 | 0.46 | 0.35 | 0.98 | 0/8 | 3 | — |
| Havertz | ARS | FWD | 7.4 | 3.25 | 3.16 | 3.01 | 3.26 | 3.39 | **16.07** | 15.30 | 0.40 | 0.34 | 0.85 | 0/9 |  | — |
| Kostoulas | BHA | FWD | 5.7 | 3.41 | 2.92 | 2.85 | 3.14 | 3.26 | **15.59** | 15.12 | 0.35 | 0.32 | 0.99 | 0/9 |  | — |

## Uavklart fravær i troppen og valgte spillere

Ingen.

