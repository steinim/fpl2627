# Status — det som ikke ligger i `fpl-data`

*Sist oppdatert: 19. november 2026, før GW11, andre versjon — wildcardsøk og chipstatus i `bytter.py`; Thomas-salget begrunnet på nytt etter at fraværsraden endret modellen. Erstatter `01-strategi-og-tropp.md` og `02-regler-og-sesongplan.md`, som sto stille fra 17. oktober og er flyttet til `arkiv/`.*

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
- **Wildcard:** ikke i GW11. `analyse/bytter.md`, seksjon «Wildcard», regner beste wildcardtropp mot beste byttepakke hver kjøring. 19.11.: +5,70 over beste plan over GW11–15 (robust +4,85), godt under modellens feilmargin. Tas når gevinsten over beste plan er tydelig større enn feilmarginen. *(Første tall, +10,5, kom fra et ad hoc-skript uten innbytterledd og før Thomas-raden i `fravaer.csv` — erstattet.)*
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

**Thomas eller Egan ut — besluttet Thomas, mot modellen.** Etter at Thomas' fravær i GW9–10 ble ført som skade, gir modellen ham 14,78 (var 10,73), og beste plan som selger Egan er 0,85 bedre enn beste som selger Thomas. Mekanismen: modellen bruker FPL-sjansen (50 %) bare for neste runde og regner ham som tilgjengelig fra GW12 (3,17 og 3,65 i GW12–13). Det finnes ingen kilde for at han er tilbake: flagget har stått på 50 % siden 24.10. og han har 0 minutter i GW9–10. 0,85 over fem runder er under feilmarginen, og antakelsen som bærer den, er ikke belagt. Egan har spilt alle minutter.

Anti-drift etter byttene: ingen klubb med 3 (BHA, BOU, IPS, MUN, TOT 2 hver). Keeper og forsvar £31,0m → £32,1m. Bank £4,7m → £2,4m.

Kaptein: ikke avgjort.

## Åpne saker

- **GW12: Diop → Murillo** er modellens neste trekk. Minimumskravene ikke gjort.
- **B.Fernandes:** benket i GW8 uten offisiell grunn (`fravaer.csv`); modellen gir 0,80 sjanse for å spille.
- **Rank:** OR 2 068 776 etter GW10. Gapet til topp 100k lukkes ikke av en tropp som bare unngår tabber, og skal styre hvordan wildcardet bygges.
- **Modell:** skade med FPL-sjanse under 100 % gjelder bare neste runde; senere runder regnes som full tilgjengelighet. Gir lange «50 %»-skader for høy verdi (Thomas). Bør løses i `forventning.py` med tilbaketest (regel 5 i `03`).
- **Chipbruk** ligger allerede i speilet (`entry/history.json` → `chips`); `bytter.md` viser nå brukt, igjen og frist.
