# Forventede poeng — generert

*Generert 21.10.2026 kl. 23:21 UTC av `scripts/forventning.py` fra `fpl-data`. **Rør ikke fila for hånd.** Grunnlag: GW1–7 (data_checked). Horisont: GW8–12. Fraværsfil: context/fravaer.csv.*

## Kontroller

- ✅ Poengregler: alle 13 kategorier i API-ets game_config stemmer med skriptet
- ✅ Rundedata GW1–7 summerer til sesongtotalene for alle 668 spillere, 19 felt
- ✅ Speilet hentet 21.10.2026 22:43 UTC, 0.6 t gammelt ved kjøring
- ✅ Lagstyrke-prior fra context/lagstyrke-prior.csv (ρ = 0.5); opprykksprior brukt for COV, HUL, IPS

## Modell og estimerte parametre

Formelen står i toppen av `scripts/forventning.py`.

- **Faste konstanter** (valgt på 2024/25 og 2025/26, se `scripts/historikk.py`): avtak i startandel 0.7, start- og spillesannsynlighet kalibrert per runde fram (fast starter: P(start) 0.92 i første runde etter grunnlaget, 0.82 i den 7.), krymping av spillerrater mot posisjon og startpris 3 kamper, krymping av DC-treffrate mot posisjonssnitt 4 kamper, CS-faktor 1.046, målfaktor GKP 1.0, DEF 0.799, MID 0.987, FWD 1.001; assistfaktor GKP 1.376, DEF 1.202, MID 1.349, FWD 2.09.
- **Estimert fra sesongens data ved hver kjøring:**
  - Liga-xG per lag og kamp μ = 1.508. Bane: hjemme ×1.082, borte ×0.918.
  - Lagstyrke krympet mot forrige sesong (dempet med ρ = 0.5) med k = 15 kamper (angrep) og 30 (forsvar).
  - Bonus: k = 38.0 kamper for spillerens eget avvik. Koeffisienter per posisjon (konstant, så felt i rekkefølge):
    - GKP (n = 140): konstant -0.196; cs +0.976, redninger +0.066
    - DEF (n = 566): konstant -0.040; mal +1.167, assist +0.359, cs +0.537, dc +0.068
    - MID (n = 606): konstant +0.005; mal +1.415, assist +0.551, dc +0.114
    - FWD (n = 133): konstant -0.014; mal +1.513, assist +0.383, dc +0.014
  - Gule kort krympes med k = 9.1 kamper mot posisjonssnitt. Strafferedninger per keeper-90: 0.014.

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
| MCI | 1.23 | 0.94 |
| BHA | 1.18 | 0.99 |
| BRE | 1.13 | 1.02 |
| ARS | 1.13 | 0.73 |
| MUN | 1.11 | 0.98 |
| BOU | 1.10 | 0.98 |
| CHE | 1.09 | 0.99 |
| LIV | 1.04 | 0.91 |
| NFO | 1.02 | 1.01 |
| CRY | 1.00 | 1.06 |
| NEW | 0.98 | 1.07 |
| LEE | 0.97 | 0.98 |
| FUL | 0.96 | 1.00 |
| IPS | 0.93 | 1.12 |
| SUN | 0.93 | 1.02 |
| AVL | 0.92 | 1.01 |
| EVE | 0.91 | 1.03 |
| COV | 0.83 | 1.06 |
| TOT | 0.81 | 0.97 |
| HUL | 0.80 | 1.08 |

## Troppen (picks GW7)

Bytter gjort etter GW7-deadline vises ikke.

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Verbruggen ★ | BHA | GKP | 4.6 | 2.64 | 2.40 | 2.63 | 2.81 | 2.74 | **13.22** | 12.87 | 0.03 | 0.00 | 1.00 |  |  | — |
| Kinsky ★ | TOT | GKP | 4.5 | 2.50 | 2.76 | 2.53 | 2.76 | 2.52 | **13.08** | 13.08 | 0.00 | 0.00 | 1.00 |  |  | — |
| Calafiori ★ | ARS | DEF | 6.0 | 4.65 | 3.65 | 4.70 | 3.79 | 3.66 | **20.44** | 19.42 | 0.34 | 0.28 | 1.00 | 0/7 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 3.96 | 3.93 | 3.49 | 3.67 | 3.24 | **18.28** | 17.58 | 0.14 | 0.09 | 1.00 | 5/7 |  | — |
| Davis ★ | IPS | DEF | 4.0 | 3.33 | 3.28 | 3.00 | 3.02 | 3.29 | **15.93** | 14.70 | 0.32 | 0.25 | 1.00 | 0/7 |  | — |
| Diop ★ | IPS | DEF | 3.9 | 3.11 | 3.16 | 2.82 | 3.00 | 3.08 | **15.17** | 15.05 | 0.04 | 0.02 | 1.00 | 4/7 |  | — |
| Egan ★ | HUL | DEF | 4.1 | 2.95 | 3.28 | 2.41 | 2.67 | 2.63 | **13.94** | 13.66 | 0.04 | 0.01 | 1.00 | 4/7 |  | — |
| Mbeumo ★ | MUN | MID | 7.8 | 5.49 | 4.82 | 5.40 | 4.40 | 5.22 | **25.33** | 21.52 | 0.69 | 0.48 | 1.00 | 0/7 | 2 | — |
| B.Fernandes ★ | MUN | MID | 11.8 | 5.43 | 4.75 | 5.33 | 4.33 | 5.16 | **25.00** | 19.74 | 0.59 | 0.28 | 1.00 | 0/7 | 1 | én kamp (GW2) står for 60% av xGI | første straffeskytter (penalties_order 1) |
| Saka ★ | ARS | MID | 9.6 | 3.01 | 4.82 | 5.96 | 5.16 | 5.17 | **24.12** | 21.80 | 0.73 | 0.60 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) | GW8: FPL-sjanse 50 % |
| Groß ★ | BHA | MID | 6.2 | 3.63 | 3.54 | 4.05 | 3.80 | 4.08 | **19.09** | 17.30 | 0.49 | 0.40 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| Slater ★ | HUL | MID | 4.5 | 2.60 | 2.66 | 2.16 | 2.40 | 2.32 | **12.14** | 11.52 | 0.13 | 0.08 | 1.00 | 0/7 |  | — |
| Haaland ★ | MCI | FWD | 15.7 | 6.01 | 6.46 | 5.71 | 6.30 | 4.44 | **28.92** | 27.43 | 0.94 | 0.84 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| João Pedro ★ | CHE | FWD | 7.9 | 4.69 | 4.59 | 4.18 | 4.43 | 4.02 | **21.90** | 19.90 | 0.58 | 0.44 | 1.00 | 0/6 |  | — |
| Barry ★ | EVE | FWD | 5.7 | 3.69 | 4.53 | 4.91 | 4.23 | 4.29 | **21.65** | 19.23 | 0.74 | 0.58 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |

## Beste per posisjon (sum over horisonten)

Spillere med minst 180 minutter og status ulik «u». ★ = i troppen. Sortert på sum; «Robust» er samme modell uten spillerens beste xGI-kamp — en følsomhetssjekk, ikke et bedre estimat. Sjekk begge før et bytte. Forskjeller under 2–3 poeng over fem runder er innenfor modellens usikkerhet.

### GKP

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raya | ARS | GKP | 6.1 | 3.65 | 3.14 | 3.64 | 3.10 | 2.99 | **16.52** | 16.50 | 0.00 | 0.00 | 1.00 |  |  | — |
| Trafford | LEE | GKP | 5.0 | 3.25 | 3.03 | 3.39 | 2.93 | 3.27 | **15.87** | 15.85 | 0.00 | 0.00 | 1.00 |  |  | — |
| Kelleher | BRE | GKP | 5.0 | 3.25 | 3.09 | 2.85 | 3.09 | 2.79 | **15.08** | 15.06 | 0.00 | 0.00 | 1.00 |  |  | — |
| Tzolakis | HUL | GKP | 4.7 | 3.07 | 3.14 | 2.84 | 2.85 | 2.82 | **14.73** | 14.73 | 0.00 | 0.00 | 1.00 |  |  | — |
| Lammens | MUN | GKP | 4.9 | 3.06 | 2.85 | 3.11 | 2.79 | 2.82 | **14.62** | 14.63 | 0.00 | 0.00 | 1.00 |  |  | — |
| Donnarumma | MCI | GKP | 5.5 | 3.09 | 2.92 | 2.85 | 3.03 | 2.70 | **14.58** | 14.58 | 0.00 | 0.00 | 1.00 |  |  | — |
| Horníček | NEW | GKP | 5.0 | 2.90 | 3.05 | 2.80 | 2.75 | 2.61 | **14.12** | 14.12 | 0.00 | 0.00 | 1.00 |  |  | — |
| Pickford | EVE | GKP | 5.5 | 2.75 | 2.79 | 3.09 | 2.58 | 2.75 | **13.97** | 13.94 | 0.00 | 0.00 | 1.00 |  |  | — |

### DEF

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calafiori ★ | ARS | DEF | 6.0 | 4.65 | 3.65 | 4.70 | 3.79 | 3.66 | **20.44** | 19.42 | 0.34 | 0.28 | 1.00 | 0/7 |  | — |
| Gabriel | ARS | DEF | 7.9 | 4.56 | 3.64 | 4.60 | 3.73 | 3.59 | **20.11** | 19.30 | 0.17 | 0.12 | 1.00 | 3/7 |  | — |
| Silva | BOU | DEF | 5.0 | 3.49 | 4.13 | 3.79 | 3.90 | 3.53 | **18.84** | 17.35 | 0.24 | 0.14 | 1.00 | 5/7 |  | — |
| Thomas ★ | COV | DEF | 4.0 | 3.96 | 3.93 | 3.49 | 3.67 | 3.24 | **18.28** | 17.58 | 0.14 | 0.09 | 1.00 | 5/7 |  | — |
| Mukiele | SUN | DEF | 5.4 | 3.88 | 3.62 | 3.37 | 3.18 | 3.69 | **17.74** | 15.97 | 0.19 | 0.08 | 0.96 | 4/6 |  | UAVKLART FRAVÆR GW1 — telt som ikke-start; før årsaken i context/fravaer.csv | én kamp (GW4) står for 63% av xGI |
| Khalaili | CRY | DEF | 5.0 | 3.84 | 3.46 | 3.29 | 3.32 | 3.77 | **17.68** | 16.13 | 0.29 | 0.20 | 0.96 | 2/6 |  | — |
| Bogle | LEE | DEF | 4.7 | 3.55 | 3.07 | 4.04 | 2.99 | 4.00 | **17.66** | 15.70 | 0.33 | 0.20 | 1.00 | 0/7 |  | — |
| Vuskovic | BHA | DEF | 5.1 | 3.40 | 3.00 | 3.60 | 3.79 | 3.81 | **17.60** | 16.89 | 0.19 | 0.14 | 1.00 | 4/7 |  | — |
| De Cuyper | BHA | DEF | 5.3 | 3.29 | 2.90 | 3.65 | 3.77 | 3.87 | **17.48** | 13.83 | 0.40 | 0.16 | 1.00 | 0/7 |  | én kamp (GW1) står for 65% av xGI |
| Murillo | NFO | DEF | 5.5 | 3.86 | 3.30 | 3.45 | 3.20 | 3.62 | **17.44** | 16.85 | 0.21 | 0.18 | 1.00 | 5/7 |  | — |
| Muharemović | LEE | DEF | 5.0 | 3.38 | 2.93 | 3.84 | 2.85 | 3.75 | **16.76** | 15.94 | 0.11 | 0.06 | 1.00 | 4/7 |  | — |
| Richards | CRY | DEF | 4.9 | 3.45 | 3.33 | 3.13 | 3.20 | 3.56 | **16.67** | 16.63 | 0.03 | 0.03 | 1.00 | 5/7 |  | — |
| Hill | BOU | DEF | 5.5 | 3.04 | 3.63 | 3.31 | 3.41 | 3.11 | **16.50** | 15.36 | 0.14 | 0.03 | 1.00 | 4/7 |  | — |
| Van Hecke | TOT | DEF | 4.9 | 3.01 | 3.59 | 3.09 | 3.63 | 3.12 | **16.43** | 15.27 | 0.17 | 0.09 | 1.00 | 3/7 |  | én kamp (GW5) står for 55% av xGI |
| Hall | NEW | DEF | 5.3 | 3.34 | 3.85 | 3.24 | 3.10 | 2.74 | **16.28** | 15.95 | 0.17 | 0.14 | 1.00 | 4/7 |  | — |

### MID

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mbeumo ★ | MUN | MID | 7.8 | 5.49 | 4.82 | 5.40 | 4.40 | 5.22 | **25.33** | 21.52 | 0.69 | 0.48 | 1.00 | 0/7 | 2 | — |
| B.Fernandes ★ | MUN | MID | 11.8 | 5.43 | 4.75 | 5.33 | 4.33 | 5.16 | **25.00** | 19.74 | 0.59 | 0.28 | 1.00 | 0/7 | 1 | én kamp (GW2) står for 60% av xGI | første straffeskytter (penalties_order 1) |
| Saka ★ | ARS | MID | 9.6 | 3.01 | 4.82 | 5.96 | 5.16 | 5.17 | **24.12** | 21.80 | 0.73 | 0.60 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) | GW8: FPL-sjanse 50 % |
| E.Le Fée | SUN | MID | 5.7 | 4.75 | 4.42 | 4.54 | 4.13 | 4.43 | **22.27** | 19.26 | 0.55 | 0.39 | 1.00 | 1/7 | 2 | — |
| Tavernier | BOU | MID | 6.2 | 4.17 | 4.54 | 4.34 | 4.43 | 3.96 | **21.45** | 18.92 | 0.63 | 0.48 | 1.00 | 0/7 | 3 | — |
| Rogers | CHE | MID | 8.0 | 4.65 | 4.45 | 4.10 | 4.33 | 3.92 | **21.45** | 20.07 | 0.51 | 0.39 | 1.00 | 1/7 |  | — |
| Ødegaard | ARS | MID | 6.8 | 4.69 | 3.86 | 4.63 | 4.06 | 4.05 | **21.31** | 18.32 | 0.57 | 0.36 | 1.00 | 0/7 | 3 | — |
| Palmer | CHE | MID | 9.7 | 4.20 | 4.01 | 3.70 | 3.91 | 3.53 | **19.34** | 18.22 | 0.34 | 0.27 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| Stach | LEE | MID | 6.0 | 3.94 | 3.73 | 4.00 | 3.61 | 4.02 | **19.29** | 18.69 | 0.27 | 0.23 | 1.00 | 3/7 |  | — |
| Groß ★ | BHA | MID | 6.2 | 3.63 | 3.54 | 4.05 | 3.80 | 4.08 | **19.09** | 17.30 | 0.49 | 0.40 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| Rudoni | COV | MID | 4.9 | 4.16 | 4.05 | 3.60 | 3.88 | 3.36 | **19.04** | 17.38 | 0.58 | 0.45 | 0.96 | 1/6 | 1 | første straffeskytter (penalties_order 1) |
| Enciso | IPS | MID | 5.5 | 3.95 | 3.69 | 3.69 | 3.37 | 3.69 | **18.39** | 17.43 | 0.47 | 0.40 | 1.00 | 0/7 |  | — |
| Iwobi | FUL | MID | 5.4 | 3.82 | 3.61 | 3.95 | 3.29 | 3.64 | **18.31** | 16.49 | 0.46 | 0.33 | 1.00 | 0/7 | 3 | — |
| Buendía | AVL | MID | 5.9 | 3.65 | 3.73 | 3.30 | 3.64 | 3.44 | **17.77** | 16.53 | 0.32 | 0.24 | 1.00 | 1/7 | 1 | første straffeskytter (penalties_order 1) |
| Tielemans | MUN | MID | 5.7 | 3.72 | 3.41 | 3.64 | 3.20 | 3.49 | **17.46** | 16.72 | 0.29 | 0.23 | 1.00 | 3/7 | 3 | — |

### FWD

| Spiller | Lag | Pos | Pris | GW8 | GW9 | GW10 | GW11 | GW12 | Sum | Robust | xGI/90 | Uten beste | Start | DC | Str | Flagg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haaland ★ | MCI | FWD | 15.7 | 6.01 | 6.46 | 5.71 | 6.30 | 4.44 | **28.92** | 27.43 | 0.94 | 0.84 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| João Pedro ★ | CHE | FWD | 7.9 | 4.69 | 4.59 | 4.18 | 4.43 | 4.02 | **21.90** | 19.90 | 0.58 | 0.44 | 1.00 | 0/6 |  | — |
| Barry ★ | EVE | FWD | 5.7 | 3.69 | 4.53 | 4.91 | 4.23 | 4.29 | **21.65** | 19.23 | 0.74 | 0.58 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| Gonzalo | FUL | FWD | 6.1 | 4.45 | 4.20 | 4.74 | 3.86 | 4.34 | **21.59** | 20.16 | 0.63 | 0.55 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| Thiago | BRE | FWD | 7.8 | 4.47 | 4.65 | 4.02 | 4.53 | 3.87 | **21.54** | 20.17 | 0.60 | 0.52 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| Evanilson | BOU | FWD | 6.1 | 3.99 | 4.29 | 4.13 | 4.21 | 3.75 | **20.37** | 17.69 | 0.54 | 0.37 | 1.00 | 0/7 |  | — |
| Calvert-Lewin | LEE | FWD | 6.0 | 4.05 | 3.83 | 4.12 | 3.73 | 4.25 | **19.98** | 19.07 | 0.56 | 0.49 | 1.00 | 0/7 | 1 | første straffeskytter (penalties_order 1) |
| Isak | LIV | FWD | 9.0 | 4.00 | 3.29 | 3.75 | 3.93 | 3.64 | **18.60** | 17.65 | 0.73 | 0.64 | 0.77 | 0/6 | 2 | UAVKLART FRAVÆR GW6 — telt som ikke-start; før årsaken i context/fravaer.csv |
| Delap | NFO | FWD | 5.5 | 4.00 | 3.64 | 3.70 | 3.36 | 3.69 | **18.39** | 16.41 | 0.54 | 0.39 | 0.94 | 0/5 | 3 | — |
| Havertz | ARS | FWD | 7.5 | 4.01 | 3.32 | 3.94 | 3.51 | 3.53 | **18.31** | 17.31 | 0.41 | 0.33 | 1.00 | 0/7 |  | — |

## Uavklart fravær i troppen og valgte spillere

Ingen.

