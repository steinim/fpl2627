# Status — det som ikke ligger i `fpl-data`

*Sist oppdatert: 27. november 2026, før GW12. Wildcardbeslutningen fra 26.11. ble tatt i en økt som ikke skrev til repoet; ført inn her 27.11. fra den samtalen.*

**Regel for fila:** maks én skjermside. Ingenting som kan leses fra speilet kopieres hit. Fila oppdateres i samme økt som en beslutning tas, via PR.

## Hvor status ligger

| Hva | Kilde |
|---|---|
| Tropp, kaptein, poeng, rank | `fpl-data`: `entry/picks/gw{n}.csv`, `entry/history.csv` |
| Bank, frikjøp, salgspriser | `analyse/bytter.md` (kontrollert mot historikken ved hver kjøring) |
| Forventede poeng | `analyse/forventning.md` |
| Kampprogram og datoer | `04` (generert blokk), `fixtures2627.csv` |

## Roller

Claude spiller laget: foreslår og begrunner bytter, kaptein og chips. Brukeren utfører i appen og kan overstyre.

## Chips

| Chip | Status |
|---|---|
| Triple Captain 1 | Brukt GW5 (Haaland, 6 × 3 = 18) |
| Wildcard 1 | Spilt GW12 (besluttet 26.11.) |
| Free Hit 1 | Igjen |
| Bench Boost 1 | Igjen |

**Frist for alle tre: GW19-deadline, lørdag 2. januar kl. 14:30 norsk tid** (`05`). Én chip per runde, så de tre trenger tre ulike runder blant GW11–19.

**Plan, 26.11.:**
- **Wildcard:** spilt GW12. +6,99 mot beste plan over GW12–16 (robust +7,31); samme chip i GW13 ga +3,73.
- **Bench Boost og Free Hit:** to runder blant GW13–19. Vurderes hver runde mot beste senere runde før fristen, ikke mot å spare.

**Trukket 19.11.:** «Wildcard GW16» fra `02`. Skrevet før sesongen på fikstursvanskelighet, aldri regnet med modellen og aldri besluttet av brukeren.

## Bytter siden 17. oktober (fra speilet)

| Runde | Ut | Inn |
|---|---|---|
| GW8 | — | — |
| GW9 | João Pedro, Saka | Evanilson, Tavernier |
| GW10 | — | — |

## GW11 — fasit

38 poeng (snitt 35). OR 3 024 051 → 2 930 717. Benkepoeng 12. Plass 100 000: 737 poeng, vi 634 (−103).

## GW12 — besluttet 26.11., deadline fredag 27.11. kl. 19:30

**Wildcard:** Verbruggen → Trafford, Kinsky → Tzolakis, Calafiori → De Cuyper, Diop → Silva, Davis → Justin, Mbeumo → Gibbs-White. Brukeren godkjente strukturendringen (+£2,0m bak, Arsenal ut av bakre ledd).

Oppstilling 3-4-3: Trafford; De Cuyper, Silva, Justin; Fernandes (C), Gibbs-White (V), Tavernier, Groß; Haaland, Barry, Evanilson. Benk: Tzolakis, Le Fée, Van Hecke, Thomas. Evanilson starter foran Le Fée (overstyrer modellen med 0,50, begrunnet med markedets lagmål). **Endret 27.11.: kaptein Gibbs-White, vise Barry. Fernandes på benken, Le Fée starter.** Fernandes har virus (FPL «d» 75 % kl. 14:29 UTC), avgjøres lørdag morgen — etter deadline. Selv frisk ga modellen ham bare 0,39 mer enn Le Fée (5,29 mot 4,90); et innhopp på slutten (1–2 poeng, ingen automatisk innbytter) koster rundt 3,4. Benk: Tzolakis, Fernandes, Van Hecke, Thomas — Fernandes dekker Groß (belastningsspørsmål før Newcastle).

Bank £0,2m. Frikjøp inn i GW13: 2. Alle 15 med status «a» i speilet 27.11. 10:07 UTC.

## Åpne saker

- **B.Fernandes:** benket av Carrick i GW8 (`fravaer.csv`, telles som ikke-start-risiko; startandel 0,85). Carrick er sparket og Pochettino tatt over fra 18.11. (Man Utd, bekreftet 13.11.). Mekanismen bak raden er borte, men ingen årsakskategori i `fravaer.csv` passer, og å lage en er en modellendring. Står som kjent skjevhet: Fernandes er undervurdert med omtrent 0,15 i startsannsynlighet.
- **Gule kort:** Tavernier og Groß har 4 (summert fra `live/gw1–10.csv`). Ett til gir én kamps utestengelse. Ikke prissatt i modellen; benken dekker.
- **Rank:** OR 3 024 051 etter GW10 (596 poeng). *(Rettet 21.11.: 2 068 776 var rundeplasseringen i GW10, ikke OR.)* Gapet til topp 100k lukkes ikke av en tropp som bare unngår tabber, og skal styre hvordan wildcardet bygges.
- **Modell, tilgjengelighet:** FPL-sjansen brukes for neste runde, full tilgjengelighet etter. For spillere som er borte (to+ runder uten minutter) stemmer det. For spillere som **spiller med flagg** (knock) er det for høyt: 0,64–0,71 av forventet i rundene etter, ikke 1,00 (n = 26–61). Ikke endret ennå: én sesong, sju runder, overlappende observasjoner, og tilbaketesten på to sesonger kan ikke teste tilgjengelighet (historikken har ingen flagg). Plan: tilpass på GW3–14, test på GW15–19, endre `tilgjengelighet()` bare hvis det holder.
- **`bytter.py` velger elleveren etter forventede poeng per spiller**, ikke etter lagverdi med innbyttere. Den starter derfor ikke en usikker spiller med en sikker dekning på benken, selv når det gir mer (Thomas/Diop i GW11: +0,45). Bør velge elleveren som maksimerer `runde()`.
- **Chipbruk** ligger allerede i speilet (`entry/history.json` → `chips`); `bytter.md` viser nå brukt, igjen og frist.
