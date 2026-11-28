# Forventede poeng — generert

*Generert 28.11.2026 kl. 10:22 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–11 (data_checked). Horisont: GW13–17. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–11 summerer til sesongtotalene for 608 spillere, 19 felt; 66 spillere på lag som har spilt i GW12 er kontrollert mot grunnlaget pluss live-fila
- ✅ Speilet hentet 28.11.2026 09:26 UTC, 0.9 t gammelt ved kjøring
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

## Troppen (picks GW12)

Bytter gjort etter GW12-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW13 | GW14 | GW15 | GW16 | GW17 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tzolakis ★ | HUL | GKP | 4.7 | 3.33 | 3.21 | 3.32 | 3.13 | 3.11 | **16.10** | 16.11 | 0.00 | 0.00 | 1.00 |  |  | — |
| Trafford ★ | LEE | GKP | 5.1 | 3.10 | 3.39 | 3.01 | 3.27 | 3.03 | **15.81** | 15.80 | 0.00 | 0.00 | 1.00 |  |  | — |
| Silva ★ | BOU | DEF | 5.1 | 3.70 | 4.49 | 3.06 | 4.29 | 3.59 | **19.12** | 18.03 | 0.17 | 0.11 | 1.00 | 8/11 |  | — |
| De Cuyper ★ | BHA | DEF | 5.6 | 3.14 | 3.31 | 4.27 | 4.39 | 3.46 | **18.57** | 16.05 | 0.43 | 0.29 | 1.00 | 0/11 |  | — |
| Van Hecke ★ | TOT | DEF | 5.2 | 4.13 | 3.40 | 3.78 | 2.95 | 3.40 | **17.66** | 16.19 | 0.23 | 0.14 | 1.00 | 4/11 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 3.97 | 2.96 | 3.62 | 2.79 | 3.38 | **16.73** | 16.36 | 0.16 | 0.13 | 1.00 | 6/9 |  | — |
| Justin ★ | LEE | DEF | 4.6 | 2.78 | 3.94 | 2.82 | 3.69 | 3.11 | **16.33** | 15.71 | 0.16 | 0.12 | 1.00 | 4/11 |  | — |
| Tavernier ★ | BOU | MID | 6.8 | 4.86 | 5.21 | 3.61 | 5.03 | 4.07 | **22.79** | 21.12 | 0.64 | 0.56 | 1.00 | 1/11 | 3 | — |
| Gibbs-White ★ | NFO | MID | 7.8 | 4.64 | 4.70 | 4.27 | 4.84 | 4.30 | **22.75** | 21.81 | 0.54 | 0.48 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| E.Le Fée ★ | SUN | MID | 5.7 | 4.13 | 4.42 | 4.65 | 5.04 | 4.23 | **22.47** | 20.50 | 0.55 | 0.46 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| B.Fernandes ★ | MUN | MID | 11.6 | 3.55 | 5.45 | 4.83 | 3.56 | 4.87 | **22.26** | 19.14 | 0.67 | 0.46 | 0.90 | 0/10 | 1 | første straffeskytter (penalties_order 1) | GW13: FPL-sjanse 75 % |
| Groß ★ | BHA | MID | 6.4 | 3.94 | 3.90 | 4.51 | 4.73 | 3.83 | **20.91** | 18.95 | 0.53 | 0.43 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| Haaland ★ | MCI | FWD | 15.7 | 5.85 | 5.20 | 6.00 | 6.11 | 5.21 | **28.38** | 27.11 | 0.83 | 0.76 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 4.76 | 5.12 | 4.37 | 4.34 | 4.97 | **23.56** | 21.91 | 0.77 | 0.68 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson ★ | BOU | FWD | 6.6 | 4.74 | 4.98 | 3.45 | 4.82 | 3.88 | **21.86** | 20.20 | 0.64 | 0.55 | 1.00 | 0/11 |  | — |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW13 | GW14 | GW15 | GW16 | GW17 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tzolakis ★ | HUL | GKP | 4.7 | 3.33 | 3.21 | 3.32 | 3.13 | 3.11 | **16.10** | 16.11 | 0.00 | 0.00 | 1.00 |  |  | — |
| Trafford ★ | LEE | GKP | 5.1 | 3.10 | 3.39 | 3.01 | 3.27 | 3.03 | **15.81** | 15.80 | 0.00 | 0.00 | 1.00 |  |  | — |
| Lammens | MUN | GKP | 4.8 | 2.94 | 3.17 | 2.81 | 2.74 | 2.85 | **14.50** | 14.46 | 0.00 | 0.00 | 1.00 |  |  | — |
| A.Becker | LIV | GKP | 5.5 | 3.05 | 2.65 | 2.87 | 3.02 | 2.86 | **14.44** | 14.43 | 0.00 | 0.00 | 1.00 |  |  | — |
| Horníček | NEW | GKP | 5.0 | 2.92 | 3.01 | 2.86 | 2.72 | 2.73 | **14.24** | 14.24 | 0.00 | 0.00 | 1.00 |  |  | — |
| Suzuki | AVL | GKP | 5.1 | 3.11 | 2.88 | 2.84 | 2.64 | 2.74 | **14.22** | 14.20 | 0.00 | 0.00 | 0.99 |  |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Donnarumma | MCI | GKP | 5.4 | 2.99 | 2.63 | 2.81 | 3.13 | 2.65 | **14.21** | 14.21 | 0.00 | 0.00 | 1.00 |  |  | — |
| Raya | ARS | GKP | 6.2 | 2.19 | 3.17 | 2.96 | 2.95 | 2.82 | **14.09** | 14.08 | 0.00 | 0.00 | 1.00 |  |  | GW13: FPL-sjanse 75 % |

### DEF

| Spiller | Lag | Pos | Pris | GW13 | GW14 | GW15 | GW16 | GW17 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel | ARS | DEF | 8.1 | 3.67 | 4.02 | 3.90 | 3.98 | 3.68 | **19.25** | 18.52 | 0.16 | 0.12 | 1.00 | 5/11 |  | — |
| Silva ★ | BOU | DEF | 5.1 | 3.70 | 4.49 | 3.06 | 4.29 | 3.59 | **19.12** | 18.03 | 0.17 | 0.11 | 1.00 | 8/11 |  | — |
| De Cuyper ★ | BHA | DEF | 5.6 | 3.14 | 3.31 | 4.27 | 4.39 | 3.46 | **18.57** | 16.05 | 0.43 | 0.29 | 1.00 | 0/11 |  | — |
| Hill | BOU | DEF | 5.7 | 3.54 | 4.31 | 3.00 | 4.12 | 3.49 | **18.44** | 17.65 | 0.12 | 0.06 | 1.00 | 7/11 |  | én kamp (GW2) står for 54% av xGI |
| Murillo | NFO | DEF | 5.5 | 3.94 | 3.50 | 3.42 | 4.01 | 3.04 | **17.92** | 17.48 | 0.18 | 0.16 | 1.00 | 7/11 |  | — |
| Van Hecke ★ | TOT | DEF | 5.2 | 4.13 | 3.40 | 3.78 | 2.95 | 3.40 | **17.66** | 16.19 | 0.23 | 0.14 | 1.00 | 4/11 |  | — |
| Virgil | LIV | DEF | 6.4 | 3.76 | 3.03 | 3.48 | 3.71 | 3.46 | **17.44** | 17.12 | 0.09 | 0.07 | 1.00 | 6/11 |  | — |
| Jacquet | LIV | DEF | 5.1 | 3.70 | 2.99 | 3.44 | 3.66 | 3.42 | **17.22** | 16.85 | 0.08 | 0.06 | 1.00 | 5/11 |  | — |
| Muharemović | LEE | DEF | 5.2 | 2.92 | 3.98 | 2.94 | 3.76 | 3.21 | **16.81** | 16.23 | 0.08 | 0.05 | 1.00 | 7/11 |  | — |
| Calafiori | ARS | DEF | 5.9 | 3.15 | 3.47 | 3.40 | 3.50 | 3.21 | **16.74** | 15.96 | 0.24 | 0.20 | 0.90 | 0/10 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 3.97 | 2.96 | 3.62 | 2.79 | 3.38 | **16.73** | 16.36 | 0.16 | 0.13 | 1.00 | 6/9 |  | — |
| Konsa | ARS | DEF | 4.9 | 3.29 | 3.57 | 3.34 | 3.34 | 3.09 | **16.62** | 16.02 | 0.08 | 0.04 | 0.98 | 4/9 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Vuskovic | BHA | DEF | 5.4 | 2.80 | 2.97 | 3.72 | 3.75 | 3.12 | **16.36** | 15.81 | 0.14 | 0.10 | 1.00 | 4/11 |  | — |
| Justin ★ | LEE | DEF | 4.6 | 2.78 | 3.94 | 2.82 | 3.69 | 3.11 | **16.33** | 15.71 | 0.16 | 0.12 | 1.00 | 4/11 |  | — |
| Araujo | LIV | DEF | 5.5 | 3.59 | 2.88 | 3.23 | 3.37 | 3.14 | **16.23** | 14.87 | 0.17 | 0.07 | 0.98 | 4/9 |  | én kamp (GW10) står for 61% av xGI |

### MID

| Spiller | Lag | Pos | Pris | GW13 | GW14 | GW15 | GW16 | GW17 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tavernier ★ | BOU | MID | 6.8 | 4.86 | 5.21 | 3.61 | 5.03 | 4.07 | **22.79** | 21.12 | 0.64 | 0.56 | 1.00 | 1/11 | 3 | — |
| Gibbs-White ★ | NFO | MID | 7.8 | 4.64 | 4.70 | 4.27 | 4.84 | 4.30 | **22.75** | 21.81 | 0.54 | 0.48 | 1.00 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| E.Le Fée ★ | SUN | MID | 5.7 | 4.13 | 4.42 | 4.65 | 5.04 | 4.23 | **22.47** | 20.50 | 0.55 | 0.46 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| B.Fernandes ★ | MUN | MID | 11.6 | 3.55 | 5.45 | 4.83 | 3.56 | 4.87 | **22.26** | 19.14 | 0.67 | 0.46 | 0.90 | 0/10 | 1 | første straffeskytter (penalties_order 1) | GW13: FPL-sjanse 75 % |
| Mbeumo | MUN | MID | 7.8 | 4.30 | 4.89 | 4.34 | 3.30 | 4.36 | **21.20** | 18.60 | 0.58 | 0.43 | 1.00 | 0/11 | 2 | — |
| Groß ★ | BHA | MID | 6.4 | 3.94 | 3.90 | 4.51 | 4.73 | 3.83 | **20.91** | 18.95 | 0.53 | 0.43 | 1.00 | 1/11 | 1 | første straffeskytter (penalties_order 1) |
| Ødegaard | ARS | MID | 6.7 | 4.01 | 3.89 | 4.25 | 4.47 | 4.08 | **20.70** | 18.66 | 0.52 | 0.40 | 1.00 | 0/11 | 3 | — |
| Rogers | CHE | MID | 8.3 | 4.68 | 3.99 | 3.45 | 4.23 | 3.82 | **20.18** | 19.15 | 0.44 | 0.37 | 1.00 | 1/11 |  | — |
| Wirtz | LIV | MID | 7.6 | 4.23 | 3.72 | 3.92 | 3.89 | 3.74 | **19.50** | 18.02 | 0.46 | 0.35 | 1.00 | 0/11 | 4 | — |
| Palmer | CHE | MID | 9.7 | 4.43 | 3.79 | 3.28 | 4.01 | 3.63 | **19.15** | 17.87 | 0.36 | 0.29 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Rayan | BOU | MID | 6.3 | 4.04 | 4.31 | 3.14 | 4.16 | 3.47 | **19.11** | 17.92 | 0.38 | 0.32 | 1.00 | 1/11 |  | — |
| Barcola | LIV | MID | 8.1 | 4.17 | 3.61 | 3.80 | 3.75 | 3.58 | **18.91** | 17.05 | 0.50 | 0.36 | 0.98 | 0/8 |  | — |
| Rudoni | COV | MID | 5.0 | 4.28 | 3.57 | 3.84 | 3.26 | 3.69 | **18.64** | 17.36 | 0.47 | 0.39 | 0.99 | 1/10 | 1 | første straffeskytter (penalties_order 1) |
| McAtee | NFO | MID | 5.5 | 3.78 | 3.75 | 3.51 | 3.83 | 3.47 | **18.34** | 17.88 | 0.30 | 0.28 | 1.00 | 5/11 |  | — |
| Rice | ARS | MID | 7.5 | 3.54 | 3.47 | 3.68 | 3.82 | 3.55 | **18.06** | 17.62 | 0.30 | 0.28 | 1.00 | 2/11 |  | — |

### FWD

| Spiller | Lag | Pos | Pris | GW13 | GW14 | GW15 | GW16 | GW17 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.7 | 5.85 | 5.20 | 6.00 | 6.11 | 5.21 | **28.38** | 27.11 | 0.83 | 0.76 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Barry ★ | EVE | FWD | 5.7 | 4.76 | 5.12 | 4.37 | 4.34 | 4.97 | **23.56** | 21.91 | 0.77 | 0.68 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | 9.4 | 4.94 | 4.32 | 4.51 | 4.40 | 4.23 | **22.41** | 21.26 | 0.71 | 0.62 | 0.95 | 0/10 | 2 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Evanilson ★ | BOU | FWD | 6.6 | 4.74 | 4.98 | 3.45 | 4.82 | 3.88 | **21.86** | 20.20 | 0.64 | 0.55 | 1.00 | 0/11 |  | — |
| Calvert-Lewin | LEE | FWD | 6.1 | 3.78 | 4.92 | 3.69 | 4.33 | 3.92 | **20.65** | 18.99 | 0.57 | 0.48 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |
| N.Jackson | AVL | FWD | 7.3 | 4.30 | 4.49 | 3.76 | 3.63 | 3.82 | **20.00** | 18.32 | 0.53 | 0.43 | 1.00 | 0/10 | 3 | — |
| Delap | NFO | FWD | 5.3 | 3.59 | 3.66 | 3.29 | 3.68 | 3.34 | **17.56** | 16.12 | 0.44 | 0.35 | 0.99 | 0/9 | 3 | — |
| Havertz | ARS | FWD | 7.4 | 3.26 | 3.11 | 3.46 | 3.64 | 3.34 | **16.80** | 16.07 | 0.40 | 0.35 | 0.90 | 0/10 |  | — |
| Gonzalo | FUL | FWD | 5.7 | 3.03 | 3.23 | 3.51 | 3.09 | 3.47 | **16.33** | 15.51 | 0.52 | 0.45 | 0.69 | 0/10 | 1 | første straffeskytter (penalties_order 1) |
| McBurnie | HUL | FWD | 5.5 | 3.46 | 3.07 | 3.25 | 2.85 | 3.14 | **15.77** | 14.40 | 0.34 | 0.25 | 1.00 | 0/11 | 1 | første straffeskytter (penalties_order 1) |

## Uavklart fravær i troppen og valgte spillere

Ingen.

