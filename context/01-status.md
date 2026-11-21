# Status — det som ikke ligger i `fpl-data`

*Sist oppdatert: 19. november 2026, før GW11, tredje versjon — **GW11-salget snudd fra Thomas til Egan**: begrunnelsen for å gå mot modellen holdt ikke mot data (`scripts/sjanse.py`, feillogg i `03`). Erstatter `01-strategi-og-tropp.md` og `02-regler-og-sesongplan.md`, som sto stille fra 17. oktober og er flyttet til `arkiv/`.*

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

**Slater → E.Le Fée, Egan → Van Hecke.** Minimumskravene i `03` gjennomgått 19.11. for Le Fée og Van Hecke; lagnytt fra pressekonferansene fredag gjenstår. Utføres etter dem.

**Unntak:** sier Coventry fredag at Thomas er ute lenger enn GW11, selges Thomas i stedet for Egan. Da faller antakelsen modellen bygger på. *20.11.: unntaket utløses ikke. FPL oppgraderte Thomas til d 75 % (speil 09:09 UTC), og LazyFPL 20.11. gjengir Lampard på at han trener og vurderes før helgen.*

**Ikke rulle et frikjøp (20.11.).** LazyFPL anbefaler å spare frikjøp før ti runder på 45 dager. Å vente med Egan → Van Hecke til GW12 koster 1,54 i GW11 og gir dårligere pakker etterpå (beste GW12-variant ligger utenfor topp 400 i `bytter.py`). Verdien av et ekstra frikjøp i desember er ikke modellert, men vi har Wildcard, Free Hit og Bench Boost ubrukt innen GW19 — det er nødkapasiteten de fleste som ruller mangler. Med OR 2 068 776 trenger vi forventede poeng nå, ikke forsikring.

**Thomas eller Egan ut — Egan, med modellen.** Modellen gir Thomas 0,47 sjanse i GW11 og full tilgjengelighet fra GW12. Beste plan som selger Egan er 0,85 bedre over GW11–15. Jeg gikk mot modellen tidligere samme dag, med påstanden at ingen kilde støttet at Thomas er tilbake fra GW12. Det er testet mot speilets historikk (`scripts/sjanse.py`, GW3–10): regulære spillere flagget «d» etter to eller flere runder uten minutter spilte i neste runde i 0,52 av forventet, og 0,87 og 1,08 de to rundene etter (n = 42, 36, 30). Modellens antakelse stemmer for denne gruppen. Forskjellen er liten, men det finnes ikke lenger en grunn til å overstyre.

Anti-drift etter byttene: ingen klubb med 3 (BHA, BOU, IPS, MUN, TOT 2 hver; Hull ut). Keeper og forsvar £31,0m → £32,0m. Bank £4,7m → £2,5m; Diop → Murillo i GW12 (£1,6m) er fortsatt mulig.

Kaptein Haaland, vise Barry. **Fernandes starter, Mbeumo på benken (21.11.).** Med GW8-benkingen under Carrick tatt ut av startgrunnlaget gir modellen Fernandes 4,98 i GW11 (start 9/9); Carrick er sparket, så mekanismen bak raden er borte (regel 8). Lavest blant de åtte offensive er Groß 4,31, Mbeumo 4,43, Evanilson 4,58 — innenfor støy. Mbeumo benkes framfor Groß: koster 0,12, og gir ikke to Man Utd-spillere i samme kamp under en ny trener med uprisede uttaksrisiko. Benk: Kinsky, Mbeumo, Davis, Thomas.

## Åpne saker

- **GW12: Diop → Murillo** er modellens neste trekk. Minimumskravene ikke gjort.
- **B.Fernandes:** benket av Carrick i GW8 (`fravaer.csv`, telles som ikke-start-risiko; startandel 0,85). Carrick er sparket og Pochettino tatt over fra 18.11. (Man Utd, bekreftet 13.11.). Mekanismen bak raden er borte, men ingen årsakskategori i `fravaer.csv` passer, og å lage en er en modellendring. Står som kjent skjevhet: Fernandes er undervurdert med omtrent 0,15 i startsannsynlighet.
- **Gule kort:** Tavernier og Groß har 4 (summert fra `live/gw1–10.csv`). Ett til gir én kamps utestengelse. Ikke prissatt i modellen; benken dekker.
- **Rank:** OR 2 068 776 etter GW10. Gapet til topp 100k lukkes ikke av en tropp som bare unngår tabber, og skal styre hvordan wildcardet bygges.
- **Modell, tilgjengelighet:** FPL-sjansen brukes for neste runde, full tilgjengelighet etter. For spillere som er borte (to+ runder uten minutter) stemmer det. For spillere som **spiller med flagg** (knock) er det for høyt: 0,64–0,71 av forventet i rundene etter, ikke 1,00 (n = 26–61). Ikke endret ennå: én sesong, sju runder, overlappende observasjoner, og tilbaketesten på to sesonger kan ikke teste tilgjengelighet (historikken har ingen flagg). Plan: tilpass på GW3–14, test på GW15–19, endre `tilgjengelighet()` bare hvis det holder.
- **Chipbruk** ligger allerede i speilet (`entry/history.json` → `chips`); `bytter.md` viser nå brukt, igjen og frist.
