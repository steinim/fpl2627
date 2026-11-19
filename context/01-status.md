# Status — det som ikke ligger i `fpl-data`

*Sist oppdatert: 19. november 2026, før GW11. Erstatter `01-strategi-og-tropp.md` og `02-regler-og-sesongplan.md`, som sto stille fra 17. oktober og er flyttet til `arkiv/`.*

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
| Wildcard 1 | Igjen |
| Free Hit 1 | Igjen |
| Bench Boost 1 | Igjen |

**Frist for alle tre: GW19-deadline, lørdag 2. januar kl. 14:30 norsk tid** (`05`). Én chip per runde, så de tre trenger tre ulike runder blant GW11–19.

**Plan, 19.11.:** ingen fast dato.
- **Wildcard:** ikke i GW11. Beste wildcardtropp innenfor £99,8m ga 271,15 forventede poeng over GW11–15, mot 260,65 med de to frikjøpene: +10,5 over fem runder, under modellens feilmargin (5–6 poeng per spiller). Regnes på nytt hver runde. Tas når gevinsten over frikjøpene er tydelig større enn feilmarginen.
- **Bench Boost:** rett etter wildcardet, som bygger benken.
- **Free Hit:** runden der flest av våre startere har svak kamp. Avskrives ikke.

**Trukket 19.11.:** «Wildcard GW16» fra `02`. Skrevet før sesongen på fikstursvanskelighet, aldri regnet med modellen og aldri besluttet av brukeren.

## Bytter siden 17. oktober (fra speilet)

| Runde | Ut | Inn |
|---|---|---|
| GW8 | — | — |
| GW9 | João Pedro, Saka | Evanilson, Tavernier |
| GW10 | — | — |

## GW11 — besluttet 19.11., deadline lørdag 21.11. kl. 12:00

**Slater → E.Le Fée, Thomas (COV) → Van Hecke.** Minimumskravene i `03` gjennomgått 19.11.; lagnytt fra pressekonferansene fredag gjenstår. Utføres etter dem.

Anti-drift etter byttene: ingen klubb med 3 (BHA, BOU, IPS, MUN, TOT 2 hver). Keeper og forsvar £31,0m → £32,1m. Bank £4,7m → £2,4m.

Kaptein: ikke avgjort.

## Åpne saker

- **GW12: Diop → Murillo** er modellens neste trekk. Minimumskravene ikke gjort.
- **B.Fernandes:** benket i GW8 uten offisiell grunn (`fravaer.csv`); modellen gir 0,80 sjanse for å spille.
- **Rank:** OR 2 068 776 etter GW10. Gapet til topp 100k lukkes ikke av en tropp som bare unngår tabber, og skal styre hvordan wildcardet bygges.
- **Verktøy:** `bytter.py --wildcard` (beste tropp innenfor budsjett, med innbytterledd). Chipbruk speilet i `fpl-data`.
