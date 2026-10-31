# Forventede poeng — generert

*Generert 31.10.2026 kl. 18:33 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–8 (data_checked). Horisont: GW10–14. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–8 summerer til sesongtotalene for 188 spillere, 19 felt; 481 spillere på lag som har spilt i GW9 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 31.10.2026 17:16 UTC, 1.3 t gammelt ved kjøring
- ✅ Lagstyrke-prior fra context/lagstyrke-prior.csv (ρ = 0.5); opprykksprior brukt for COV, HUL, IPS

## Modell og estimerte parametre

Formelen står i toppen av `scripts/forventning.py`.

- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel 0.7, start- og spillesannsynlighet kalibrert per runde fram (fast starter: P(start) 0.92 i første runde etter grunnlaget, 0.82 i den 7.), krymping av spillerrater mot posisjon og startpris 3 kamper, krymping av DC-treffrate mot posisjonssnitt 4 kamper, CS-faktor 1.046, målfaktor GKP 1.0, DEF 0.799, MID 0.987, FWD 1.001; assistfaktor GKP 1.376, DEF 1.202, MID 1.349, FWD 2.09.
- **Estimert fra sesongens data ved hver kjøring:**
  - Liga-xG per lag og kamp μ = 1.463. Bane: hjemme ×1.064, borte ×0.936.
  - Lagstyrke krympet mot forrige sesong (dempet med ρ = 0.5) med k = 15 kamper (angrep) og 30 (forsvar).
  - Bonus: k = 29.5 kamper for spillerens eget avvik. Koeffisienter per posisjon (konstant, så felt i rekkefølge):
    - GKP (n = 160): konstant -0.202; cs +1.020, redninger +0.070
    - DEF (n = 644): konstant -0.048; mal +1.181, assist +0.428, cs +0.530, dc +0.090
    - MID (n = 700): konstant +0.006; mal +1.454, assist +0.524, dc +0.095
    - FWD (n = 151): konstant -0.005; mal +1.550, assist +0.332, dc +0.005
  - Gule kort krympes med k = 9.6 kamper mot posisjonssnitt. Strafferedninger per keeper-90: 0.013.

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
| MCI | 1.24 | 0.93 |
| BHA | 1.22 | 0.99 |
| BRE | 1.15 | 1.04 |
| ARS | 1.15 | 0.73 |
| BOU | 1.12 | 0.98 |
| MUN | 1.12 | 0.99 |
| CHE | 1.06 | 0.99 |
| NFO | 1.05 | 0.99 |
| LIV | 1.03 | 0.90 |
| CRY | 0.99 | 1.07 |
| NEW | 0.97 | 1.08 |
| LEE | 0.95 | 0.97 |
| FUL | 0.94 | 1.00 |
| SUN | 0.92 | 1.02 |
| IPS | 0.91 | 1.13 |
| EVE | 0.91 | 1.03 |
| AVL | 0.90 | 1.00 |
| HUL | 0.81 | 1.09 |
| COV | 0.81 | 1.05 |
| TOT | 0.81 | 0.95 |

## Troppen (picks GW9)

Bytter gjort etter GW9-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW10 | GW11 | GW12 | GW13 | GW14 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kinsky ★ | TOT | GKP | 4.4 | 2.79 | 2.96 | 2.73 | 2.83 | 2.56 | **13.88** | 13.89 | 0.00 | 0.00 | 1.00 |  |  | — |
| Verbruggen ★ | BHA | GKP | 4.6 | 2.69 | 2.91 | 2.80 | 2.44 | 2.48 | **13.34** | 13.00 | 0.03 | 0.00 | 1.00 |  |  | — |
| Calafiori ★ | ARS | DEF | 5.9 | 2.87 | 3.31 | 3.13 | 3.04 | 3.47 | **15.81** | 15.04 | 0.33 | 0.27 | 0.68 | 0/7 |  | GW10: FPL-sjanse 75 % |
| Davis ★ | IPS | DEF | 4.0 | 2.88 | 3.05 | 3.22 | 3.05 | 2.65 | **14.85** | 13.78 | 0.28 | 0.22 | 1.00 | 0/8 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 1.68 | 3.45 | 3.13 | 3.52 | 2.81 | **14.60** | 14.05 | 0.13 | 0.09 | 1.00 | 5/8 |  | GW10: FPL-sjanse 50 % |
| Diop ★ | IPS | DEF | 3.9 | 2.69 | 2.99 | 3.01 | 2.91 | 2.58 | **14.17** | 14.05 | 0.03 | 0.02 | 1.00 | 4/8 |  | — |
| Egan ★ | HUL | DEF | 4.1 | 2.58 | 2.74 | 2.83 | 2.93 | 2.53 | **13.62** | 13.38 | 0.04 | 0.01 | 1.00 | 5/8 |  | — |
| Mbeumo ★ | MUN | MID | 7.9 | 5.26 | 4.39 | 5.13 | 4.78 | 5.13 | **24.69** | 21.14 | 0.65 | 0.46 | 1.00 | 0/8 | 2 | — |
| Tavernier ★ | BOU | MID | 6.5 | 4.82 | 4.71 | 4.32 | 4.52 | 4.85 | **23.22** | 20.92 | 0.67 | 0.56 | 1.00 | 0/8 | 3 | — |
| B.Fernandes ★ | MUN | MID | 11.7 | 3.98 | 3.44 | 4.16 | 3.95 | 4.30 | **19.85** | 15.68 | 0.59 | 0.28 | 0.68 | 0/7 | 1 | UAVKLART FRAVÆR GW8 — telt som ikke-start; før årsaken i context/fravaer.csv | én kamp (GW2) står for 60% av xGI | første straffeskytter (penalties_order 1) |
| Groß ★ | BHA | MID | 6.2 | 4.12 | 3.92 | 4.10 | 3.51 | 3.52 | **19.17** | 17.46 | 0.47 | 0.39 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Slater ★ | HUL | MID | 4.5 | 2.19 | 2.39 | 2.34 | 2.37 | 2.21 | **11.51** | 10.99 | 0.13 | 0.08 | 1.00 | 0/8 |  | — |
| Haaland ★ | MCI | FWD | 15.8 | 5.66 | 6.12 | 4.43 | 5.79 | 5.52 | **27.53** | 26.03 | 0.87 | 0.77 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.6 | 4.92 | 4.42 | 4.29 | 4.19 | 4.50 | **22.32** | 19.91 | 0.69 | 0.55 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson ★ | BOU | FWD | 6.3 | 4.29 | 4.20 | 3.84 | 4.07 | 4.27 | **20.67** | 18.13 | 0.54 | 0.39 | 1.00 | 0/8 |  | — |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW10 | GW11 | GW12 | GW13 | GW14 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raya | ARS | GKP | 6.2 | 3.75 | 3.29 | 3.10 | 3.01 | 3.38 | **16.53** | 16.51 | 0.00 | 0.00 | 1.00 |  |  | — |
| Trafford | LEE | GKP | 5.0 | 3.59 | 3.15 | 3.45 | 2.99 | 3.26 | **16.44** | 16.43 | 0.00 | 0.00 | 1.00 |  |  | — |
| Tzolakis | HUL | GKP | 4.7 | 3.03 | 2.99 | 2.98 | 2.99 | 2.86 | **14.85** | 14.85 | 0.00 | 0.00 | 1.00 |  |  | — |
| Suzuki | AVL | GKP | 5.0 | 2.94 | 3.08 | 2.89 | 2.95 | 2.83 | **14.69** | 14.68 | 0.00 | 0.00 | 0.97 |  |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Lammens | MUN | GKP | 4.8 | 3.13 | 2.78 | 2.75 | 2.76 | 3.08 | **14.50** | 14.43 | 0.01 | 0.00 | 1.00 |  |  | — |
| Horníček | NEW | GKP | 5.0 | 2.94 | 2.83 | 2.69 | 2.77 | 2.89 | **14.11** | 14.12 | 0.00 | 0.00 | 1.00 |  |  | — |
| Kelleher | BRE | GKP | 5.0 | 2.79 | 3.06 | 2.74 | 2.77 | 2.69 | **14.04** | 14.03 | 0.00 | 0.00 | 1.00 |  |  | — |
| Leno | FUL | GKP | 4.5 | 3.00 | 2.57 | 2.73 | 2.92 | 2.75 | **13.97** | 13.97 | 0.00 | 0.00 | 1.00 |  |  | — |

### DEF

| Spiller | Lag | Pos | Pris | GW10 | GW11 | GW12 | GW13 | GW14 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel | ARS | DEF | 8.0 | 5.06 | 4.27 | 3.96 | 3.80 | 4.31 | **21.41** | 20.57 | 0.21 | 0.17 | 1.00 | 4/8 |  | — |
| Silva | BOU | DEF | 5.0 | 4.03 | 3.91 | 3.72 | 3.53 | 4.31 | **19.50** | 18.04 | 0.21 | 0.12 | 1.00 | 6/8 |  | — |
| De Cuyper | BHA | DEF | 5.3 | 3.71 | 3.93 | 3.95 | 3.09 | 3.19 | **17.87** | 14.42 | 0.39 | 0.19 | 1.00 | 0/8 |  | én kamp (GW1) står for 57% av xGI |
| Bogle | LEE | DEF | 4.8 | 4.06 | 3.14 | 4.00 | 2.71 | 3.80 | **17.70** | 15.88 | 0.32 | 0.21 | 1.00 | 0/8 |  | — |
| Hill | BOU | DEF | 5.5 | 3.65 | 3.54 | 3.40 | 3.17 | 3.92 | **17.68** | 16.57 | 0.12 | 0.03 | 1.00 | 5/8 |  | — |
| Muharemović | LEE | DEF | 5.1 | 4.06 | 3.17 | 3.95 | 2.77 | 3.70 | **17.65** | 16.90 | 0.11 | 0.07 | 1.00 | 5/8 |  | — |
| Vuskovic | BHA | DEF | 5.2 | 3.60 | 3.87 | 3.82 | 3.08 | 3.18 | **17.54** | 16.88 | 0.18 | 0.14 | 1.00 | 4/8 |  | — |
| Murillo | NFO | DEF | 5.5 | 3.45 | 3.25 | 3.66 | 3.84 | 3.33 | **17.53** | 17.01 | 0.21 | 0.19 | 1.00 | 5/8 |  | — |
| Virgil | LIV | DEF | 6.4 | 3.35 | 3.33 | 3.38 | 3.60 | 3.01 | **16.67** | 16.22 | 0.05 | 0.02 | 1.00 | 5/8 |  | — |
| Jacquet | LIV | DEF | 5.1 | 3.33 | 3.30 | 3.36 | 3.57 | 2.99 | **16.53** | 16.05 | 0.06 | 0.03 | 1.00 | 4/8 |  | — |
| Van Hecke | TOT | DEF | 4.9 | 3.24 | 3.68 | 3.22 | 3.44 | 2.87 | **16.44** | 15.41 | 0.15 | 0.08 | 1.00 | 3/8 |  | én kamp (GW5) står for 54% av xGI |
| Konsa | ARS | DEF | 4.7 | 4.00 | 3.28 | 2.97 | 2.81 | 3.24 | **16.30** | 15.57 | 0.10 | 0.05 | 0.94 | 2/6 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Richards | CRY | DEF | 4.9 | 3.28 | 3.44 | 3.66 | 2.83 | 3.10 | **16.30** | 16.25 | 0.03 | 0.03 | 1.00 | 6/8 |  | — |
| N.Williams | NFO | DEF | 5.0 | 3.19 | 2.99 | 3.42 | 3.60 | 3.09 | **16.29** | 15.64 | 0.26 | 0.22 | 1.00 | 2/8 |  | — |
| Tarkowski | EVE | DEF | 6.2 | 3.81 | 2.79 | 3.18 | 3.15 | 3.30 | **16.23** | 16.10 | 0.04 | 0.03 | 1.00 | 5/8 |  | — |

### MID

| Spiller | Lag | Pos | Pris | GW10 | GW11 | GW12 | GW13 | GW14 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mbeumo ★ | MUN | MID | 7.9 | 5.26 | 4.39 | 5.13 | 4.78 | 5.13 | **24.69** | 21.14 | 0.65 | 0.46 | 1.00 | 0/8 | 2 | — |
| Tavernier ★ | BOU | MID | 6.5 | 4.82 | 4.71 | 4.32 | 4.52 | 4.85 | **23.22** | 20.92 | 0.67 | 0.56 | 1.00 | 0/8 | 3 | — |
| Ødegaard | ARS | MID | 6.7 | 4.81 | 4.30 | 4.15 | 4.05 | 3.94 | **21.25** | 18.65 | 0.58 | 0.41 | 1.00 | 0/8 | 3 | — |
| E.Le Fée | SUN | MID | 5.7 | 4.44 | 4.11 | 4.27 | 3.75 | 4.08 | **20.64** | 18.07 | 0.52 | 0.38 | 1.00 | 1/8 | 2 | — |
| Rayan | BOU | MID | 6.3 | 4.14 | 4.04 | 3.75 | 3.88 | 4.14 | **19.95** | 18.24 | 0.39 | 0.31 | 1.00 | 1/8 |  | — |
| Gibbs-White | NFO | MID | 7.9 | 3.95 | 3.75 | 4.12 | 4.05 | 4.06 | **19.93** | 19.03 | 0.64 | 0.56 | 0.78 | 0/7 | 1 | UAVKLART FRAVÆR GW7 — telt som ikke-start; før årsaken i context/fravaer.csv | første straffeskytter (penalties_order 1) |
| B.Fernandes ★ | MUN | MID | 11.7 | 3.98 | 3.44 | 4.16 | 3.95 | 4.30 | **19.85** | 15.68 | 0.59 | 0.28 | 0.68 | 0/7 | 1 | UAVKLART FRAVÆR GW8 — telt som ikke-start; før årsaken i context/fravaer.csv | én kamp (GW2) står for 60% av xGI | første straffeskytter (penalties_order 1) |
| Rogers | CHE | MID | 8.1 | 3.98 | 4.09 | 3.74 | 4.18 | 3.76 | **19.76** | 18.45 | 0.45 | 0.35 | 1.00 | 1/8 |  | — |
| Groß ★ | BHA | MID | 6.2 | 4.12 | 3.92 | 4.10 | 3.51 | 3.52 | **19.17** | 17.46 | 0.47 | 0.39 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Palmer | CHE | MID | 9.8 | 3.74 | 3.84 | 3.51 | 3.92 | 3.53 | **18.54** | 17.50 | 0.33 | 0.27 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Rudoni | COV | MID | 4.9 | 3.67 | 3.87 | 3.37 | 3.85 | 3.27 | **18.04** | 16.52 | 0.52 | 0.40 | 0.97 | 1/7 | 1 | første straffeskytter (penalties_order 1) |
| Iwobi | FUL | MID | 5.4 | 3.98 | 3.36 | 3.62 | 3.41 | 3.45 | **17.82** | 16.22 | 0.45 | 0.33 | 1.00 | 0/8 | 3 | — |
| Enciso | IPS | MID | 5.5 | 3.74 | 3.47 | 3.72 | 3.52 | 3.31 | **17.77** | 16.95 | 0.46 | 0.39 | 1.00 | 0/8 |  | — |
| Dewsbury-Hall | EVE | MID | 6.6 | 3.80 | 3.37 | 3.35 | 3.28 | 3.46 | **17.27** | 16.46 | 0.31 | 0.25 | 1.00 | 0/8 |  | — |
| Gomez | BHA | MID | 5.0 | 3.62 | 3.49 | 3.59 | 3.18 | 3.18 | **17.05** | 16.19 | 0.29 | 0.23 | 1.00 | 2/8 |  | — |

### FWD

| Spiller | Lag | Pos | Pris | GW10 | GW11 | GW12 | GW13 | GW14 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.8 | 5.66 | 6.12 | 4.43 | 5.79 | 5.52 | **27.53** | 26.03 | 0.87 | 0.77 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.6 | 4.92 | 4.42 | 4.29 | 4.19 | 4.50 | **22.32** | 19.91 | 0.69 | 0.55 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Thiago | BRE | FWD | 7.8 | 4.38 | 4.82 | 4.23 | 3.70 | 4.33 | **21.45** | 20.34 | 0.64 | 0.57 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson ★ | BOU | FWD | 6.3 | 4.29 | 4.20 | 3.84 | 4.07 | 4.27 | **20.67** | 18.13 | 0.54 | 0.39 | 1.00 | 0/8 |  | — |
| Gonzalo | FUL | FWD | 6.0 | 4.60 | 3.81 | 4.16 | 3.75 | 3.88 | **20.20** | 18.89 | 0.59 | 0.51 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | 9.1 | 4.03 | 4.12 | 3.84 | 4.11 | 3.69 | **19.80** | 18.84 | 0.70 | 0.62 | 0.84 | 0/7 | 2 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Calvert-Lewin | LEE | FWD | 6.1 | 3.94 | 3.66 | 4.02 | 3.44 | 4.13 | **19.19** | 18.21 | 0.49 | 0.42 | 1.00 | 0/8 | 1 | første straffeskytter (penalties_order 1) |
| Delap | NFO | FWD | 5.4 | 3.77 | 3.49 | 3.71 | 3.57 | 3.60 | **18.13** | 16.33 | 0.52 | 0.39 | 0.96 | 0/6 | 3 | — |
| N.Jackson | AVL | FWD | 6.9 | 3.42 | 3.67 | 3.56 | 3.58 | 3.62 | **17.85** | 16.97 | 0.44 | 0.39 | 1.00 | 0/7 | 2 | — |
| Kostoulas | BHA | FWD | 5.8 | 3.43 | 3.18 | 3.32 | 2.89 | 2.88 | **15.69** | 15.23 | 0.39 | 0.36 | 0.97 | 0/7 |  | — |

## Uavklart fravær i troppen og valgte spillere

Telles som ikke-start til årsaken er ført i `context/fravaer.csv`. Slå opp årsaken — ikke gjett.

| Spiller | Lag | Runder |
|---|---|---|
| B.Fernandes | MUN | GW8 |

