# Kampprogram — verifisert kalender og endringslogg

*Opprettet 20. august 2026. Vedlikeholdes av den planlagte kampprogram-sjekken.*
*Sist oppdatert 3. september 2026, andre versjon — **Man City–Sunderland flyttet til søndag 20.9. 14:00** (nivå 1, mancity.com 28.8.). Ligacupens runde 3-datoer publisert. GW8-betingelsen lukket. GW4-deadline bekreftet i API-et. GW5- og GW6–GW8-tabeller ført inn. Én utledning i forrige versjon vist å være feil (Brentford).*
*⚠️ **Første versjon samme dag hadde to egne feil, begge fanget av brukerens diff mot repo:** elleve klokkeslett i GW6–GW8-tabellen sto i UTC under en kolonne merket UK-tid, og endringsloggen påsto usant at ingenting var fjernet. Begge rettet. Se «Endringer i denne versjonen» nederst.*
*Forrige: 28. august 2026, sent — full pressekonferansetabell for GW2 ført inn (13 klubber, ni av ti relevante klubber verifisert mot nivå 1-kilde), ingen skadeflagg funnet i troppen.*
*Forrige: 28. august 2026 — Chelsea–Luton-resultatet (2–0) ført inn i ligacuptabellen, Leeds' runde 3-motstander dermed avgjort (Chelsea, borte). GW2-deadlinen re-verifisert, ingen endring.*
*Forrige: 27. august 2026 — begge betingede endringene i GW4 og GW5 er avgjort etter ligacuptrekningen 26. august. GW4-tabellen ført inn.*

Denne filen er fasit for **datoer og klokkeslett**. `fixtures2627.csv` er fasit for **hvem som møter hvem i hvilken runde** — den er kontrollert 20. august og stemmer 30/30 på kamppar i GW1–3, men datokolonnen er ubrukelig fordi den setter hele runden til samme dag.

## Status per 3. september 2026

| Sjekkpunkt | Funn |
|---|---|
| Flyttede kamper siden forrige sjekk | **Én. Man City–Sunderland (GW5) flyttet til søndag 20.9. 14:00 UK.** Kunngjort mancity.com fre 28.8. kl. 19:00 |
| Utsatte kamper | **Ingen** |
| Bekreftet blankrunde (BGW) | **Ingen.** GW3–GW8 har alle nøyaktig ti kamper |
| Bekreftet dobbeltrunde (DGW) | **Ingen** |
| Nyeste offisielle PL-fikstursak | **Fortsatt 17. august 2026** (GW6–9). Ingen nyere publisert. Neste kunngjøring (MW10–12, november) ventet **uken fra 21. september** |
| Betinget endring GW8 | **Lukket. Utløses ikke.** Villa spiller hjemme i CL onsdag 21. oktober |
| Ligacupens runde 3 — datoer | **Publisert av EFL 28. august.** Var åpent punkt i forrige versjon. Se egen seksjon |
| GW3-programmet | **Uendret.** Alle ti kamper og deadline identiske med tabellen under |
| GW4-deadline | **Bekreftet i API-et:** `2026-09-12T12:30:00Z` = lør 13:30 BST / 14:30 norsk. Sto tidligere som utledet |

Alle kamptider i GW3–GW8 er verifisert direkte mot FPLs `fixtures`-endepunkt 3. september. Samtlige 60 kamper har `provisional_start_time: false` — tidene er endelige, ikke foreløpige.

**Deadlines lest direkte fra `bootstrap-static` 3. september, ikke utledet:**

| Runde | `deadline_time` (UTC) | BST | Norsk |
|---|---|---|---|
| GW3 | 2026-09-04T17:30:00Z | fre 4.9. 18:30 | 19:30 |
| **GW4** | **2026-09-12T12:30:00Z** | **lør 12.9. 13:30** | **14:30** |
| GW5 | 2026-09-18T17:30:00Z | fre 18.9. 18:30 | 19:30 |
| GW6 | 2026-10-10T10:00:00Z | lør 10.10. 11:00 | 12:00 |

Blank- og dobbeltrunder bekreftes normalt ikke før januar/februar, når FA-cup-omberamminger foreligger. Chip-planen i `02` (Free Hit GW16–19, Triple Captain på dobbeltrunde) hviler derfor fortsatt på antakelser, ikke på kunngjort kalender.

### Forrige status — per 27. august 2026, beholdt for sporbarhet

| Sjekkpunkt | Funn |
|---|---|
| Flyttede kamper i GW2–GW5 | Ingen nye. Alle TV-flyttinger er fra kunngjøringen 7. juli og står uendret |
| Utsatte kamper | Ingen |
| Bekreftet blankrunde (BGW) | Ingen. GW2, GW3, GW4 og GW5 har alle nøyaktig ti kamper |
| Bekreftet dobbeltrunde (DGW) | Ingen |
| Nyeste offisielle PL-kunngjøring | 17. august 2026 (GW6–9). Ingen nyere fikstursak publisert per 27. august |
| Betingede endringer GW4 og GW5 | Begge avgjort 26. august — ingen av dem utløses |
| Betinget endring GW8 | Åpen. Avgjøres av Champions League-trekningen 27. august |

⚠️ **Raden «Flyttede kamper i GW2–GW5: ingen nye» var korrekt da den ble skrevet 27. august, og gal 28. august kl. 19:00.** Se seksjonen under.

## Endringen 28. august — Man City–Sunderland

**Kunngjort på mancity.com fredag 28. august kl. 19:00 (nivå 1):** «City's Premier League fixture against Sunderland at the Etihad Stadium has been moved to Sunday 20 September», avspark 14:00 UK.

Årsaken står i samme artikkel: «The update to our September home tie follows the confirmation of our Carabao Cup third round clash with Norwich, who we will face on Thursday 17 September, with kick-off at the Etihad set for 19:30 (UK).» Norwich-kampen ble bekreftet på mancity.com samme ettermiddag kl. 17:30.

**Hva flyttingen faktisk gjør med Haaland:**

| | Cupkamp → ligakamp | Timer |
|---|---|---|
| Før flyttingen (lør 19.9. 15:00) | tor 17.9. 19:30 → lør 15:00 | **43,5** |
| Etter flyttingen (søn 20.9. 14:00) | tor 17.9. 19:30 → søn 14:00 | **66,5** |

Flyttingen kjøper City 23 timer. Den fjerner ikke torsdagskampen. **GW5-deadline er fredag 18. september 18:30 BST — dagen etter cupkampen, to døgn før Haaland spiller.** Kapteinsvalget låses uten lagnytt fra søndagen og uten å vite hvor mange minutter Haaland fikk mot Norwich torsdag.

⚠️ **Merk hvordan denne ble fanget — og hvordan den ikke ble det.** Forrige kjøring verifiserte GW5 mot API-et 27. august og fant ingenting, men skrev aldri GW5-tabellen inn i filen; bare konklusjonen «kontrollert, ingen endring». Endringen kom dagen etter. Uten tabellen finnes det ingenting å diffe mot, og funnet måtte gjøres via en klubbside i stedet for ved sammenligning. **Regelen som følger: skriv inn tabellen, ikke bare konklusjonen om at den er sjekket.** En påstand om at noe er kontrollert har null verdi i neste kjøring hvis det kontrollerte ikke er skrevet ned. GW5 og GW6–GW8 står nå i filen.

## GW1 — fredag 21. til mandag 24. august

Deadline: fredag 21. august 18:30 BST / 19:30 norsk.

| Dato | UK-tid | Kamp | TV |
|---|---|---|---|
| fre 21.8. | 20:00 | Arsenal – Coventry | Sky |
| lør 22.8. | 12:30 | Hull – Man Utd | TNT |
| lør 22.8. | 15:00 | Everton – Crystal Palace | — |
| lør 22.8. | 15:00 | Ipswich – Sunderland | — |
| lør 22.8. | 15:00 | Nottingham Forest – Leeds | — |
| lør 22.8. | 17:30 | Brentford – Tottenham | Sky |
| søn 23.8. | 14:00 | Brighton – Aston Villa | Sky |
| søn 23.8. | 14:00 | Man City – Bournemouth | Sky |
| søn 23.8. | 16:30 | Newcastle – Liverpool | Sky |
| **man 24.8.** | **20:00** | **Fulham – Chelsea** | Sky |

**Troppens kamper i rekkefølge:** Tzolis + Calafiori fredag · B.Fernandes, Mbeumo, Shaw lørdag 12:30 · Davis, Diop lørdag 15:00 · N.Williams, Gibbs-White lørdag 15:00 · Slater lørdag 12:30 · Kinsky, Dúbravka lørdag 17:30 · Haaland søndag 14:00 · **João Pedro mandag 20:00** · Calvert-Lewin lørdag 15:00.

**Konsekvens:** runden avgjøres ikke før mandag kveld. Bonuspoeng og DefCon låses tirsdag 25. august 09:00 UK. João Pedro er eneste spiller igjen etter søndag — hele restrisikoen i GW1 ligger på ett spissslott i en bortekamp mot Fulham.

## GW2 — fredag 28. til mandag 31. august

Deadline: fredag 28. august 18:30 BST / 19:30 norsk. **Kun fire dager etter at GW1 er ferdigspilt.**

| Dato | UK-tid | Kamp | TV |
|---|---|---|---|
| fre 28.8. | 20:00 | Crystal Palace – Man City | Sky |
| lør 29.8. | 12:30 | Liverpool – Nottingham Forest | TNT |
| lør 29.8. | 15:00 | Bournemouth – Everton | — |
| lør 29.8. | 15:00 | Coventry – Hull | — |
| lør 29.8. | 17:30 | Tottenham – Newcastle | Sky |
| søn 30.8. | 14:00 | Chelsea – Brighton | Sky |
| søn 30.8. | 14:00 | Leeds – Brentford | Sky |
| søn 30.8. | 14:00 | Sunderland – Fulham | Sky |
| søn 30.8. | 16:30 | Man Utd – Ipswich | Sky |
| man 31.8. | 20:00 | Aston Villa – Arsenal | Sky |

Åtte av ti kamper er flyttet fra opprinnelig lørdagsslot. To av flyttingene har oppgitt årsak: Chelsea–Brighton er skjøvet til søndag fordi Brighton spiller Conference League-playoff torsdagen før, og Sunderland–Fulham fordi Fulham–Chelsea ble lagt til mandag 24. august.

**Merk:** Haaland spiller fredag 28. — kapteinsvalget må tas før deadline uten lagnytt fra noen andre kamper. Calafiori og Tzolis spiller mandag 31., altså tre døgn etter Haaland.

**Kontrollert 27. august mot FPL-API-et:** alle ti kamptider identiske med tabellen over. Ingen endring.

## GW3 — fredag 4. til søndag 6. september

Deadline: fredag 4. september 18:30 BST / 19:30 norsk. **Overgangsvinduet stengte tirsdag 1. september 23:00 — signeringer fra siste vindusdøgn er spillbare først her.**

| Dato | UK-tid | Kamp | TV |
|---|---|---|---|
| fre 4.9. | 20:00 | Ipswich – Liverpool | Sky |
| lør 5.9. | 12:30 | Newcastle – Bournemouth | TNT |
| lør 5.9. | 15:00 | Brentford – Sunderland | — |
| lør 5.9. | 15:00 | Brighton – Leeds | — |
| lør 5.9. | 15:00 | Fulham – Crystal Palace | — |
| lør 5.9. | 15:00 | Man City – Coventry | — |
| lør 5.9. | 15:00 | Nottingham Forest – Tottenham | — |
| lør 5.9. | 17:30 | Hull – Aston Villa | Sky |
| søn 6.9. | 14:00 | Everton – Man Utd | Sky |
| søn 6.9. | 16:30 | Arsenal – Chelsea | Sky |

Davis og Diop spiller fredag. Haaland spiller lørdag 15:00 hjemme mot Coventry — `02` avviser Triple Captain her, og den avvisningen står.

**Kontrollert 27. august mot FPL-API-et:** alle ti kamptider identiske med tabellen over. Ingen endring.
**Kontrollert på nytt 3. september mot FPL-API-et:** fortsatt identiske. Ingen endring.

⚠️ **Kildekonflikt, 3. september.** Hentingen av PLs amendment-artikkel (7.7.2026) gjenga «Newcastle v Bournemouth | Saturday 5 Sept | **15:00** BST | TNT Sports». API-et gir 11:30Z = **12:30 BST**, og TNTs lørdagsslot *er* 12:30. **Vi stoler på API-et** (`provisional_start_time: false`, uendret over to kontroller ni dager fra hverandre) og på 12:30. Avviket ligger etter alt å dømme i sammendraget av artikkelen, ikke i PLs tekst — men det er **ikke etterprøvd mot originalen**, og føres derfor som uavklart kildekonflikt, ikke som lukket.

## GW4 — lørdag 12. til mandag 14. september

**GW4 har ingen fredagskamp.** Første avspark er lørdag 12. september 15:00 UK. Deadline **lørdag 12. september 13:30 BST / 14:30 norsk**.

✅ **Bekreftet 3. september.** Tallet sto tidligere med advarsel om at det var *utledet* av 90-minuttersregelen og ikke lest av appen. Det er nå lest direkte fra `bootstrap-static`: `deadline_time: 2026-09-12T12:30:00Z`. Advarselen er lukket. Merk fortsatt at dette er sesongens første lørdagsdeadline — vanen fra fredagsrundene er den reelle risikoen, ikke tallet.

| Dato | UK-tid | Kamp | TV |
|---|---|---|---|
| lør 12.9. | 15:00 | Aston Villa – Nottingham Forest | — |
| lør 12.9. | 15:00 | Bournemouth – Brentford | — |
| lør 12.9. | 15:00 | Chelsea – Hull | — |
| lør 12.9. | 15:00 | Crystal Palace – Ipswich | — |
| lør 12.9. | 15:00 | Liverpool – Fulham | — |
| lør 12.9. | 17:30 | Tottenham – Everton | Sky |
| lør 12.9. | 20:00 | Sunderland – Arsenal | TNT |
| søn 13.9. | 14:00 | Coventry – Brighton | Sky |
| søn 13.9. | 16:30 | Man Utd – Man City | Sky |
| **man 14.9.** | **20:00** | **Leeds – Newcastle** | Sky |

**Troppens kamper:** Davis + Diop, N.Williams + Gibbs-White, Slater og João Pedro lørdag 15:00 · Kinsky lørdag 17:30 · Calafiori + Tzolis lørdag 20:00 · Verbruggen søndag 14:00 · **B.Fernandes, Mbeumo, Shaw og Haaland i samme kamp søndag 16:30** · **Calvert-Lewin mandag 20:00.**

To ting følger av tabellen. Man Utd–Man City samler fire av troppens spillere i én kamp — det er den største konsentrasjonen av kamprisiko på ett avspark denne sesongen så langt, og kapteinsvalget mellom Haaland og B.Fernandes avgjøres innenfor samme 90 minutter. Og som i GW1 avgjøres runden først mandag kveld, denne gangen av Calvert-Lewin.

**Kilde:** premierleague.com 7. juli 2026, kryssjekket mot FPLs `fixtures`-endepunkt 27. august og på nytt 3. september. Slottene kl. 15:00 er de kampene som ikke er TV-flyttet; klokkeslettet er bekreftet direkte i API-et, ikke utledet av standardregelen.

## GW5 — fredag 18. til søndag 20. september

Deadline: fredag 18. september 18:30 BST / 19:30 norsk.

*Ført inn 3. september. Tabellen manglet i forrige versjon, og det var grunnen til at Man City-flyttingen ikke kunne oppdages ved diff.*

| Dato | UK-tid | Kamp | TV |
|---|---|---|---|
| fre 18.9. | 20:00 | Brentford – Chelsea | Sky |
| lør 19.9. | 12:30 | Tottenham – Aston Villa | TNT |
| lør 19.9. | 15:00 | Brighton – Arsenal | — |
| lør 19.9. | 15:00 | Everton – Ipswich | — |
| lør 19.9. | 15:00 | Newcastle – Hull | — |
| lør 19.9. | 17:30 | Nottingham Forest – Coventry | Sky |
| søn 20.9. | 14:00 | Bournemouth – Liverpool | Sky |
| søn 20.9. | 14:00 | Leeds – Crystal Palace | — |
| **søn 20.9.** | **14:00** | **Man City – Sunderland** | **— (flyttet 28.8.)** |
| søn 20.9. | 16:30 | Fulham – Man Utd | Sky |

**Troppens kamper i rekkefølge:** João Pedro fredag 20:00 · Kinsky lørdag 12:30 · Calafiori + Tzolis, Verbruggen, Davis + Diop, Calvert-Lewin, Slater lørdag 15:00 · N.Williams + Gibbs-White lørdag 17:30 · **Haaland søndag 14:00** · B.Fernandes + Mbeumo + Shaw søndag 16:30.

**Ikke verifisert:** Leeds–Crystal Palace står søndag 20.9. 14:00 og var **ikke** i PLs amendment-liste fra 7. juli, som betyr at den er flyttet fra standardslottet lørdag 15:00 på et eller annet tidspunkt. Palace spiller Europa League torsdag 17. september, hvilket er den nærliggende forklaringen. **Om flyttingen skjedde før eller etter 27. august er ikke fastslått** — forrige kjøring skrev ikke ned GW5-tabellen, så det finnes ikke noe sammenligningsgrunnlag. Ingen spillere i troppen berøres, og punktet har lav prioritet.

## GW6–GW8 — kontrollert 3. september, ingen endring

Alle 30 kamper hentet fra FPL-API-et 3. september, `provisional_start_time: false` gjennomgående, ti kamper per runde. Kryssjekket rad for rad mot PLs amendment-artikkel av 17. august for de kampene den dekker. Ingen avvik.

**Alle tretti kampene står her, ikke bare de med spillere i troppen** — det er hele poenget med regelen fra Man City-flyttingen: en runde uten tabell kan ikke diffes neste gang.

⚠️ **Klokka stilles natt til søndag 25. oktober.** Fram til og med lørdag 24. oktober er UK-tid = UTC + 1 (BST). Fra søndag 25. oktober er UK-tid = UTC (GMT). GW8 har derfor to omregningsregler internt i samme runde. Kolonnen under er UK-tid, ferdig omregnet.

### GW6 — lørdag 10. til mandag 12. oktober

| Dato | UK-tid | Kamp | Troppen |
|---|---|---|---|
| lør 10.10. | 12:30 | Arsenal – Leeds | Calafiori, Tzolis |
| lør 10.10. | 15:00 | Aston Villa – Brentford | — |
| lør 10.10. | 15:00 | Chelsea – Bournemouth | João Pedro |
| lør 10.10. | 15:00 | Ipswich – Fulham | Davis, Diop |
| lør 10.10. | 15:00 | Sunderland – Brighton | Verbruggen |
| lør 10.10. | 17:30 | Man Utd – Tottenham | B.Fernandes, Mbeumo, Shaw, Kinsky |
| søn 11.10. | 14:00 | Crystal Palace – Nottingham Forest | N.Williams, Gibbs-White |
| søn 11.10. | 14:00 | Hull – Everton | Slater, Calvert-Lewin |
| søn 11.10. | 16:30 | Liverpool – Man City | Haaland |
| man 12.10. | 20:00 | Coventry – Newcastle | — |

Man Utd–Tottenham samler fire spillere i én kamp, som Man Utd–Man City i GW4. Hull–Everton setter Slater direkte mot Calvert-Lewin.

### GW7 — lørdag 17. til mandag 19. oktober

| Dato | UK-tid | Kamp | Troppen |
|---|---|---|---|
| lør 17.10. | 12:30 | Everton – Chelsea | Calvert-Lewin, João Pedro |
| lør 17.10. | 15:00 | Brentford – Liverpool | — |
| lør 17.10. | 15:00 | Fulham – Hull | Slater |
| lør 17.10. | 15:00 | Man City – Ipswich | Haaland, Davis, Diop |
| lør 17.10. | 17:30 | Newcastle – Aston Villa | — |
| søn 18.10. | 14:00 | Bournemouth – Sunderland | — |
| søn 18.10. | 14:00 | Brighton – Crystal Palace | Verbruggen |
| søn 18.10. | 14:00 | Leeds – Man Utd | B.Fernandes, Mbeumo, Shaw |
| søn 18.10. | 16:30 | Nottingham Forest – Arsenal | N.Williams, Gibbs-White, Calafiori, Tzolis |
| man 19.10. | 20:00 | Tottenham – Coventry | Kinsky |

To interne oppgjør: Everton–Chelsea og Forest–Arsenal, sistnevnte med fire spillere fordelt på begge sider. Man City–Ipswich setter Haaland mot Davis og Diop.

### GW8 — fredag 23. til søndag 25. oktober

| Dato | UK-tid | Kamp | Troppen |
|---|---|---|---|
| fre 23.10. | 20:00 | Ipswich – Nottingham Forest | Davis, Diop, N.Williams, Gibbs-White |
| lør 24.10. | 12:30 | Aston Villa – Man City | Haaland |
| lør 24.10. | 15:00 | Arsenal – Everton | Calafiori, Tzolis, Calvert-Lewin |
| lør 24.10. | 15:00 | Coventry – Fulham | — |
| lør 24.10. | 17:30 | Chelsea – Tottenham | João Pedro, Kinsky |
| søn 25.10. | 14:00 | Crystal Palace – Newcastle | — |
| søn 25.10. | 14:00 | Hull – Brentford | Slater |
| søn 25.10. | 14:00 | Liverpool – Brighton | Verbruggen |
| søn 25.10. | 14:00 | Man Utd – Bournemouth | B.Fernandes, Mbeumo, Shaw |
| søn 25.10. | 16:30 | Sunderland – Leeds | — |

**Fire interne oppgjør i én runde:** Ipswich–Forest (fire spillere), Arsenal–Everton (tre), Chelsea–Tottenham (to). Det er den tetteste runden så langt på spillere som møter hverandre.

⚠️ **Rettet 3. september, samme dag.** Første versjon av disse tre tabellene hadde UTC-verdier i en kolonne merket UK-tid — elleve av tjue rader én time gale, og én rad med feil ukedag (Ipswich–Fulham). Feilen sto i en tabell hvor teksten over påsto at den var kryssjekket mot PLs artikkel; kryssjekken ville tatt den umiddelbart, og var altså ikke gjort. **Dette er tredje gang samme tidssonefeil er loggført** (27.8., 28.8., 3.9. — se `03`). De to første gangene var det to klokkeslett som ble trukket fra hverandre uten å konvertere; denne gangen var det et felt kopiert fra API-et uten å konverteres i det hele tatt.

**Regelen som følger:** API-et oppgir UTC. Skriver du et klokkeslett i en kolonne merket UK-tid, skal konverteringen gjøres i samme operasjon som avlesningen, ikke som et etterarbeid. Og en påstand om at en tabell er kryssjekket mot en annen kilde skal ikke skrives før kryssjekken faktisk er utført rad for rad.

## Ligacupen — runde 3, datoer bekreftet

**Publisert av EFL 28. august 2026.** Dette sto som «Ikke verifisert» i forrige versjon, med merknaden at det «har konsekvens for rotasjonsrisiko rundt GW4 og bør bekreftes når EFL setter datoene». EFL oppgir at datoene ble satt «following the announcement of fixture details for the league phase of the UEFA Champions League».

| Dato | UK-tid | Kamp | Klubb i troppen |
|---|---|---|---|
| tir 8.9. | 19:45 | Sunderland – Hull | Slater |
| tir 8.9. | 20:00 | Millwall – Newcastle | — |
| **ons 9.9.** | **20:00** | **Chelsea – Leeds** | **João Pedro** |
| tir 15.9. | 20:00 | Ipswich – Arsenal | **Calafiori, Tzolis, Davis, Diop** |
| tir 15.9. | 20:00 | Liverpool – Tottenham | Kinsky |
| tir 15.9. | 20:00 | Reading – Brentford | — |
| ons 16.9. | 19:45 | Everton – Wolves | Calvert-Lewin |
| **ons 16.9.** | **20:00** | **Man Utd – Brighton** | **B.Fernandes, Mbeumo, Shaw, Verbruggen** |
| ons 16.9. | 20:00 | Coventry – Aston Villa | — |
| **tor 17.9.** | **19:30** | **Man City – Norwich** | **Haaland** |

**Nottingham Forest er ute** (tapte 0–2 for Leeds i runde 2). N.Williams og Gibbs-White er de eneste i troppen uten cupbelastning inn mot GW5.

**Hvile mellom cupkamp og neste ligakamp:**

| Klubb | Cupkamp | Neste ligakamp | Timer |
|---|---|---|---|
| Hull | tir 8.9. 19:45 | lør 12.9. 15:00 (GW4) | 87 |
| Chelsea | ons 9.9. 20:00 | lør 12.9. 15:00 (GW4) | 67 |
| Arsenal | tir 15.9. 20:00 | lør 19.9. 15:00 (GW5) | 91 |
| Ipswich | tir 15.9. 20:00 | lør 19.9. 15:00 (GW5) | 91 |
| Tottenham | tir 15.9. 20:00 | lør 19.9. 12:30 (GW5) | 88,5 |
| Everton | ons 16.9. 19:45 | lør 19.9. 15:00 (GW5) | 67,25 |
| Brighton | ons 16.9. 20:00 | lør 19.9. 15:00 (GW5) | 67 |
| Man Utd | ons 16.9. 20:00 | søn 20.9. 16:30 (GW5) | 92,5 |
| **Man City** | **tor 17.9. 19:30** | **søn 20.9. 14:00 (GW5)** | **66,5** |

**Konsekvens for GW5:** de tre korteste hvilene i troppen tilhører Everton (Calvert-Lewin), Brighton (Verbruggen) og **Man City (Haaland)** — alle på 66–67 timer. Kalenderen avgjør ingenting alene; rotasjon er en trenerbeslutning. Men **GW5-deadline er fredag 18.9. 18:30 BST, før samtlige tre spiller**, og for Haalands del før det finnes noe lagnytt overhodet fra søndagen. Det er kapteinsslottet dette treffer.

**Merk også GW4-siden:** Chelsea spiller cup onsdag 9.9. og liga lørdag 12.9. — 67 timer. Det gjelder João Pedro, og det er den korteste hvilen i troppen inn mot GW4.

**Verifisering.** Nivå 1: mancity.com (28.8., Man City–Norwich tor 17.9. 19:30, Sky Sports+), brightonandhovealbion.com («Wednesday 16 September, kick off 8pm» for Man Utd–Brighton), chelseafc.coms egen kamp-URL med datostempel `2026-09-09` for Chelsea–Leeds. Øvrige rader er kryssjekket mot to uavhengige nivå 5-lister (live-footballontv.com og Fan Banter, begge 28.8.) som er innbyrdes identiske og samstemte med alle tre nivå 1-radene. **efl.com sin egen sak (28.8.) ble hentet, men artikkelteksten lastet ikke — kun publiseringsdatoen er lest derfra.** arsenal.com svarte 403 og tottenhamhotspur.com svarte 401; Arsenal- og Tottenham-radene hviler derfor på nivå 5 alene.

### ⚠️ Feil i forrige versjon — rettet 3. september

Forrige versjon utledet at «Leeds', Newcastles og Brentfords kamper havner i uken fra 7. september ... følger logisk av PLs egen betingelse», og merket det eksplisitt som **utledet, ikke kunngjort**. Merkingen var riktig og reddet filen fra å påstå noe den ikke visste. Selve utledningen var likevel gal:

| Klubb | Utledet | Faktisk |
|---|---|---|
| Leeds | uken fra 7.9. | ✅ ons 9.9. |
| Newcastle | uken fra 7.9. | ✅ tir 8.9. |
| **Brentford** | **uken fra 7.9.** | ❌ **tir 15.9.** |

Resonnementet var at CL-lagene må ha cupkampen i uken fra 14. september fordi ligafasen spilles 8.–10. september. Det sier noe om hvor CL-lagene *ikke* kan spille, men ingenting om hvor klubbene utenfor den gruppen *må* plasseres. Brentford er ikke CL-lag og var aldri bundet til uken fra 7. september i det hele tatt. To av tre traff, og de to traff av andre grunner enn den oppgitte.

**Regelen som følger:** en betingelse som utelukker ett alternativ for én gruppe, bestemmer ikke plasseringen for gruppen utenfor. Utledningen var strukturelt for sterk, ikke bare uheldig. Ingen beslutning hvilte på den — Brentford har ingen spillere i troppen — men den sto i filen som nær-fakta i seks dager.

## Betingede endringer — alle avgjort

### GW8 Aston Villa – Man City: lukket 3. september, utløses ikke

Betingelsen fra premierleague.com (7.7.2026), slik den ble verifisert direkte mot primærkilden 27. august: kampen flyttes fra lørdag 24. oktober 12:30 til 20:00 **hvis Villa er trukket til bortekamp i Champions League onsdag 21. oktober** (ligafase runde 3, spilles 20.–21. oktober).

**UEFAs ligafaseoppsett ble bekreftet 29. august.** Villas runde 3: **onsdag 21. oktober, hjemme mot Viking.** Hjemmekamp — betingelsen krever bortekamp. **Utløses ikke. Kampen står lørdag 24. oktober 12:30.**

Kryssjekk, to uavhengige: FPL-API-et gir fortsatt `2026-10-24T11:30:00Z` = 12:30 BST med `provisional_start_time: false`, og PLs egen amendment-artikkel fra 17. august fører Aston Villa–Man City 12:30 BST på TNT **uten asterisk**. Asterisken i den artikkelen gjelder Bournemouth, Sunderland og Palace, som spiller Europa League torsdagen før.

Slik betingelsen sto beskrevet fram til 3. september: «Endringen flytter ingen kamp ut av sin runde og har derfor ingen poengkonsekvens. Den flytter Haalands avspark åtte timer innenfor samme lørdag. Sjekkes ved neste kjøring.» Den vurderingen holdt — konsekvensen ville uansett vært null i poeng — men den er nå uansett moot, siden endringen ikke utløses.

**Dermed er samtlige tre betingede endringer fra 7. juli avgjort.** De to i GW4 og GW5 falt 26.–27. august; denne var den siste. Ingen betingede endringer står åpne per 3. september.

### Avgjort 26. august 2026 — ingen av dem utløses

Ligacupens tredje runde ble trukket onsdag 26. august. Utløseren i begge tilfeller var at én av klubbene skulle møte et **Champions League-lag** i tredje runde. Trekningen ga:

| Klubb | Motstander i ligacup runde 3 | I Champions League? |
|---|---|---|
| Leeds | Chelsea (borte) | **Nei** — Chelsea spiller ikke europacup i 2026/27 |
| Newcastle | Millwall (borte) | **Nei** |
| Brentford | Reading (borte) | **Nei** |
| Chelsea | Leeds (hjemme) | **Nei** |

| Kamp | Runde | Utfall |
|---|---|---|
| Leeds – Newcastle | GW4 | **Står fast man 14.9. 20:00.** Flyttes ikke til lørdag |
| Brentford – Chelsea | GW5 | **Står fast fre 18.9. 20:00.** **GW5-deadlinen blir dermed fredag 18. september 18:30 BST / 19:30 norsk** |

**Merk at utfallet var uavhengig av Chelsea–Luton torsdag 27. august.** Verken Chelsea eller Luton spiller Champions League, så ingen av de to betingelsene kunne utløses uansett resultat. Dette var endelig avgjort, ikke betinget videre.

De fem engelske Champions League-lagene i 2026/27 er Arsenal, Man City, Man Utd, Aston Villa og Liverpool. Alle fem er i trekningen plassert mot andre motstandere: Ipswich–Arsenal, Man City–Norwich, Man Utd–Brighton, Coventry–Aston Villa, Liverpool–Tottenham.

## Kilder og sjekkelogg

| Dato sjekket | Kilde | Funn |
|---|---|---|
| 20.8.2026 | premierleague.com «All 380 fixtures for 2026/27» (19.6.2026) | Grunnliste GW1–4 |
| 20.8.2026 | premierleague.com «Fixture amendments … August and September» (7.7.2026) | Alle TV-flyttinger GW1–5 |
| 20.8.2026 | premierleague.com «Fixture amendments … October and November» (17.8.2026) | GW6–9. Ingen endring for GW1–3 |
| 20.8.2026 | chelseafc.com, liverpoolfc.com, tottenhamhotspur.com, mancity.com | Kryssjekk av fire enkeltkamper |
| 20.8.2026 | Sky Sports (19.6. og 22.7.2026) | Uavhengig bekreftelse av tider |
| 27.8.2026 | FPL `fixtures`-endepunkt, event 2–5 | Alle 40 kamptider bekreftet. `provisional_start_time: false` gjennomgående. Ti kamper per runde — ingen BGW/DGW |
| 27.8.2026 | premierleague.com «Possible fixture changes in 2026/27» (7.7.2026) | Ordlyden i alle tre betingede endringene, verifisert direkte |
| 27.8.2026 | premierleague.com nyhets- og publikasjonsarkiv | Ingen fikstursak publisert etter 17. august |
| 27.8.2026 | leedsunited.com (26.8.2026) — nivå 1 | Leeds borte mot vinneren av Chelsea–Luton i ligacupens runde 3 |
| 27.8.2026 | 101greatgoals (26.8.2026) — nivå 5 | Full trekningsliste for runde 3. Se konsistenssjekken under |
| 27.8.2026 | Sky Sports (27.5.2026 og 26.8.2026) | Ni engelske europacuplag: Arsenal, Man City, Man Utd, Aston Villa, Liverpool (CL); Bournemouth, Sunderland, Crystal Palace (EL); Brighton (Conference). Chelsea er ikke blant dem |
| 27.8.2026 | uefa.com | CL-ligafasetrekning 27. august. Runde 3 spilles 20.–21. oktober |
| 28.8.2026 | ESPN, Sky Sports (begge 27.8.2026) | Chelsea slo Luton 2–0 i ligacupens runde 2 (Welbeck 50', Odofin selvmål 79'). Leeds' runde 3-motstander dermed avgjort: Chelsea (borte), ikke lenger betinget |
| **3.9.2026** | **FPL `fixtures`-endepunkt, event 3–8** | **Alle 60 kamptider hentet. `provisional_start_time: false` gjennomgående. Ti kamper per runde — ingen BGW/DGW i GW3–GW8** |
| **3.9.2026** | **FPL `bootstrap-static`, `events` 3–6** | **Deadlines lest direkte. GW4 = `2026-09-12T12:30:00Z`, som bekrefter den tidligere utledede lørdagsdeadlinen** |
| **3.9.2026** | **mancity.com (28.8.2026, 19:00) — nivå 1** | **«City's Premier League fixture against Sunderland … has been moved to Sunday 20 September», 14:00 UK. Eneste flytting funnet i denne kjøringen** |
| **3.9.2026** | **mancity.com (28.8.2026, 17:30) — nivå 1** | **Man City–Norwich, ligacup runde 3, torsdag 17. september 19:30, Sky Sports+** |
| **3.9.2026** | **brightonandhovealbion.com — nivå 1** | **Man Utd–Brighton, «Wednesday 16 September, kick off 8pm», Sky Sports** |
| **3.9.2026** | **chelseafc.com kamp-URL `…english-league-cup-2026-09-09` — nivå 1** | **Chelsea–Leeds onsdag 9. september** |
| **3.9.2026** | **premierleague.com «Champions League league phase schedule confirmed» (29.8.2026)** | **Villas runde 3: onsdag 21. oktober, HJEMME mot Viking. Lukker GW8-betingelsen** |
| **3.9.2026** | **premierleague.com «Fixture amendments … October and November» (17.8.2026), hentet på nytt** | **Aston Villa–Man City lør 24.10. 12:30 BST, TNT, uten asterisk. Asterisken gjelder Bournemouth/Sunderland/Palace (Europa League torsdagen før)** |
| **3.9.2026** | **premierleague.com «Dates when 2026/27 live TV fixtures will be announced» (19.6.2026)** | **Neste kunngjøring: MW10–12 (november), uken fra 21. september. Deretter MW13–20 uken fra 19. oktober. Full plan ført inn under** |
| **3.9.2026** | **efl.com (28.8.2026)** | **Publiseringsdato bekreftet. Artikkelteksten lastet ikke — innholdet er hentet fra andre kilder** |
| **3.9.2026** | **live-footballontv.com + Fan Banter (28.8.2026) — begge nivå 5** | **Full runde 3-liste. Innbyrdes identiske, og samstemte med de tre nivå 1-radene** |
| **3.9.2026** | **premierleague.com nyhets- og publikasjonsarkiv** | **Fortsatt ingen fikstursak publisert etter 17. august** |

**Konsistenssjekk av trekningslisten (nivå 5-kilden), fra 27. august.** De ni engelske europacuplagene kommer inn først i runde 3 og spilte ikke runde 2. Nøyaktig ni lag i trekningslisten har ikke spilt runde 2: Crystal Palace, Man Utd, Brighton, Man City, Sunderland, Arsenal, Aston Villa, Bournemouth og Liverpool. Det er identisk med listen fra Sky. Chelsea spilte runde 2 mot Luton og er dermed ikke europacuplag. Listen er internt konsistent, og Leeds-raden er dessuten bekreftet fra klubbens egen side. **Konklusjonen om at ingen av de to betingelsene utløses, hviler ikke på nivå 5-kilden alene.**

**Motstridende kilde, avklart 20. august:** Wikipedias «2026–27 Premier League» oppgir sesongstart 22. august. Det er feil — premierleague.com og to Sky-artikler gir fredag 21. august. Wikipedia-siden er ikke oppdatert etter programslippet. Vi stoler på premierleague.com.

**Forkastet kilde, 27. august:** chelseafc.coms artikkel «Chelsea handed home tie in Carabao Cup third round draw» ble hentet og viste seg å omtale Middlesbrough/Barnsley og datoene 22.–23. september **2020**. Feil sesong, fanget av firukersregelen i `03`. Ikke brukt.

**Forkastet kilde, 3. september:** en henting av `premierleague.com/en/news/3774835` (i søketreffet titulert «Possible Premier League fixture changes in 2026/27») returnerte innhold om **2025/26** — Spurs–Wolves, Fulham–Brentford, Liverpool–Man Utd 19. oktober. Wolves spiller ikke i Premier League 2026/27. Feil sesong. **Hele hentingen forkastet, ikke bare raden som avslørte den** — jf. regelen fra 27. august i `03`. Ordlyden i GW8-betingelsen er derfor tatt fra forrige versjon av denne filen, hvor den ble verifisert mot primærkilden 27. august, ikke fra dagens henting.

**Forkastet kilde, 3. september:** leedsunited.com «Fixture Update: Crystal Palace (H)» ble hentet for å datere Leeds–Palace-flyttingen. Artikkelen er datert **11. november 2025** og omhandler 20. desember 2025. Feil sesong. Ikke brukt — og punktet står derfor fortsatt uavklart.

**Ikke verifisert:** premierleague.com/en/fixtures lastes ikke uten JavaScript, så kampdatabasen er ikke lest direkte per i dag. Verifiseringen bygger på PLs egne artikler, klubbenes egne sider og FPL-API-ets `fixtures`-endepunkt. 15:00-kampene uten TV-dekning er utledet av PLs standardregel («all kick-off times are 15:00 BST unless otherwise mentioned») for GW1–3, men for GW4–GW8 er de bekreftet direkte i API-et.

## Kunngjøringsplan for TV-flyttinger — resten av sesongen

Fra premierleague.com «Dates when 2026/27 Premier League live TV fixtures will be announced» (19.6.2026). **Dette er når neste endring kan komme — sett sjekk i disse ukene.**

| Periode | MW | Ventet kunngjøring |
|---|---|---|
| August/september | 2–5 | uken fra 13. juli ✅ kom 7. juli |
| Oktober | 6–9 | uken fra 24. august ✅ kom 17. august |
| **November** | **10–12** | **uken fra 21. september** |
| Desember/januar | 13–20 | uken fra 19. oktober |
| Januar | 21–23 | uken fra 30. november |
| Februar | 24–27 | uken fra 21. desember |
| Mars | 28–30 | uken fra 18. januar |
| April | 31–33 | uken fra 22. februar |
| April/mai | 34 | uken fra 22. mars |
| Mai | 35 | uken fra 29. mars |
| Mai | 36 | uken fra 5. april |
| Mai | 37 | etter FA-cupsemifinalene |

PL presiserer at «fixtures are always advertised as being subject to change». **Merk at desember/januar-kunngjøringen (MW13–20, uken fra 19. oktober) er den som treffer Free Hit-vinduet GW16–19 i `02`.** Chip-planen kan ikke låses før den foreligger.

## GW1 — faktisk resultat, ført inn 25. august 2026

Alle ti kamper spilt 21.–24. august som oppsatt. **Ingen utsettelser, ingen flyttinger.**

| Kamp | Resultat | Troppens spillere |
|---|---|---|
| Arsenal–Coventry | 3–0 | Calafiori, Tzolis |
| Hull–Man Utd | **2–0** | Slater (benk) mot B.Fernandes, Mbeumo, Shaw |
| Everton–Crystal Palace | 2–0 | — |
| Ipswich–Sunderland | 2–1 | Davis, Diop (begge benk) |
| Forest–Leeds | **0–1** | N.Williams, Gibbs-White mot Calvert-Lewin |
| Brentford–Tottenham | **3–0** | Kinsky (benk) |
| Brighton–Aston Villa | **4–0** | Verbruggen |
| Man City–Bournemouth | 2–1 | Haaland |
| Newcastle–Liverpool | 2–2 | — |
| Fulham–Chelsea | 2–3 | João Pedro |

**Låsing:** poengene var **ikke** låst kl. 06:47 britisk tid 25. august (`finished: false`, `data_checked: false` i API-et). Låsing kl. 09:00 britisk samme dag, som `02` oppgir.

⚠️ **Merknad om kilder:** rundesnitt og høyeste enkeltlag er **ikke** hentbare fra noen kilde før låsing — verken API-et eller appen. Se regelen om poengaggregater i `03`. Endelige tall for GW1, hentet etter låsing: **snitt 50, høyeste enkeltlag 131, høyeste entry 120245.**

**Bekreftet for GW2-planleggingen (skrevet 25. august, nå historisk):** ingen av de betingede endringene i tabellen over var utløst på det tidspunktet. Alle tre er siden avgjort — se «Betingede endringer».

## Ligacupen 2026/27 — troppens klubber

Ført inn 27. august 2026 fordi cupkampene i uken fra 7. og 14. september ligger tett på GW4 og GW5 og påvirker rotasjonsrisiko. **Datokolonnen lagt til 3. september.**

| Klubb i troppen | Runde 2 | Runde 3 | Dato |
|---|---|---|---|
| Arsenal | — (europacuplag, kom inn i runde 3) | Ipswich (borte) | tir 15.9. 20:00 |
| Man City | — (europacuplag) | Norwich (hjemme) | **tor 17.9. 19:30** |
| Man Utd | — (europacuplag) | Brighton (hjemme) | ons 16.9. 20:00 |
| Brighton | — (europacuplag) | Man Utd (borte) | ons 16.9. 20:00 |
| Everton | — | Wolves (hjemme) | ons 16.9. 19:45 |
| Ipswich | Slo Leicester 3–1 | Arsenal (hjemme) | tir 15.9. 20:00 |
| Hull | Slo Stoke på straffer | Sunderland (borte) | tir 8.9. 19:45 |
| Leeds | Slo Nottingham Forest 2–0 | **Chelsea (borte)** — avgjort 27. august | ons 9.9. 20:00 |
| Chelsea | **Slo Luton 2–0 (hjemme), 27. august** (Welbeck 50', Odofin selvmål 79') | Leeds (hjemme) | ons 9.9. 20:00 |
| Nottingham Forest | **Ute** — tapte 0–2 for Leeds | — | — |
| Tottenham | Slo Charlton | Liverpool (borte) | tir 15.9. 20:00 |

Man Utd–Brighton og Ipswich–Arsenal er kamper mellom to klubber troppen har spillere i. Ingen av rundene kolliderer med en Premier League-runde. **Everton var ikke ført i denne tabellen før 3. september** — klubben er med i runde 3, og Calvert-Lewin har dermed cupkamp onsdag 16.9., 67 timer før GW5-kampen mot Ipswich.

## Pressekonferanser før GW1 — faktisk avviklet

| Dag | Tid UK | Trener | Klubb |
|---|---|---|---|
| ons 19.8. | — | Lampard | Coventry |
| tor 20.8. | 13:00 | Jakirović · Sage | Hull · Crystal Palace |
| tor 20.8. | 13:30 | Arteta · Rose · Alonso · Farke · Le Bris | Arsenal · Bournemouth · Chelsea · Leeds · Sunderland |
| tor 20.8. | 14:00 | Glasner | Forest |
| tor 20.8. | 16:30 | Jaissle | Newcastle |
| tor 20.8. | 17:30 | Carrick | Man Utd |
| fre 21.8. | 10:00 | Arbeloa | Fulham |
| fre 21.8. | 12:00 | Hürzeler | Brighton |
| fre 21.8. | 13:30 | Andrews · Moyes · O'Neil · Iraola · Maresca · De Zerbi | Brentford · Everton · Ipswich · Liverpool · Man City · Tottenham |
| fre 21.8. | 14:00 | Emery | Aston Villa |

**Mønster å planlegge etter i GW2:** klubber som spiller sent i runden legger pressekonferansen på fredag, og enkelte så sent som 17:30 UK — **én time før deadline**. I GW1 fikk fire av femten spillere lagnytt først på deadline-dagen, inkludert kapteinen.

**Motstridende tidsangivelse, uavklart:** FFScout oppga Carrick 17:30 UK, The Peoples Person oppga 16:30. BBCs liveblogg tidsstempler første Carrick-innlegg 17:36. **FFScout stemte best.**

## Pressekonferanser før GW2 — faktisk avviklet

| Dag | Tid UK | Trener | Klubb |
|---|---|---|---|
| ons 26.8. | — | Sage | Crystal Palace |
| tor 27.8. | 10:30 | Maresca | Man City |
| tor 27.8. | 13:00 | Jakirović | Hull |
| tor 27.8. | 13:30 | Arteta · Rose · Iraola | Arsenal · Bournemouth · Liverpool |
| tor 27.8. | 14:30 | Lampard | Coventry |
| tor 27.8., kveld | (embargo til fre. ettermiddag) | Alonso | Chelsea |
| tor 27.8. | 18:30 | Jaissle | Newcastle |
| fre 28.8. | 09:00 | Hürzeler · Glasner | Brighton · Forest |
| fre 28.8. | 10:00 | Arbeloa | Fulham |
| fre 28.8. | 10:30 | Moyes | Everton |
| fre 28.8. | 13:15 | Carrick | Man Utd |
| fre 28.8. | 13:30 | Andrews · O'Neil · Farke · Le Bris · De Zerbi | Brentford · Ipswich · Leeds · Sunderland · Tottenham |
| fre 28.8. | 14:00 | Emery | Aston Villa |

**Avvik fra planlagt skjema:** FFScouts forhåndsvarslede tidspunkt for Alonso var fredag 13:30, men Chelsea la faktisk pressen torsdag kveld med sitatene sperret til fredag ettermiddag. Planlagte klokkeslett i denne typen skjema er altså varsler, ikke garantier — samme lærdom som Carrick-avviket i GW1-tabellen over.

**Troppens elleve startende utespillere — dekning per klubb:**

| Klubb | Spiller(e) | Nevnt i noen presser? |
|---|---|---|
| Arsenal | Calafiori, Tzolis | Nei |
| Man City | Haaland | Nei |
| Man Utd | B.Fernandes, Mbeumo, Shaw | Nei |
| Tottenham | Kinsky | Nei |
| Chelsea | João Pedro | Nei |
| Brighton | Verbruggen | Nei |
| Everton | Calvert-Lewin | Nei |
| Ipswich | Davis, Diop | Nei |
| Nottingham Forest | N.Williams, Gibbs-White | **Ja — begge friskmeldt** (Glasner, se `01`) |

**Konklusjon: null skadeflagg i troppen inn mot GW2**, verifisert mot primærkilde (klubbenes egne nettsider) for ni av ti klubber. Kryssjekket mot sekundærkilde (FFScout) for samtlige.

## Kilder — tillegg 27.–28. august

| Dato | Kilde | Funn |
|---|---|---|
| 27.8. | mancity.com | Fullt Maresca-referat, Bouaddi/Doku/Nunes. **Nivå 1** |
| 27.8. | arsenal.com | Fullt Arteta-referat, Guimarães/Konsa/Timber/Saliba. **Nivå 1** |
| 27.8. | leedsunited.com | Farke-referat, Gruev/Gudmundsson/Gnonto. **Nivå 1** |
| 27.8. | (klubbside, Liverpool-mønster) | Iraola på Chiesa. Domenet ikke eksplisitt vist i innsendingen — ikke ført som nivå 1 uten bekreftet URL |
| 27.8. | (klubbside, Newcastle-mønster) | Jaissle på González. Domenet ikke eksplisitt vist — samme forbehold |
| 26.8. | chelseafc.com | Alonso-referat, Caicedo/Palestra/Palmer. **Nivå 1**, bekrefter tidligere funn |
| 28.8. | manutd.com | Fullt Carrick-referat, Amad/Mount/Baleba/de Ligt. **Nivå 1** |
| 28.8. | evertonfc.com | Moyes-referat, Hackney/Nørgaard/Garner. **Nivå 1** |
| 26.8. | (klubbside, Crystal Palace-mønster) | Sage på Sarr/Riad/Disasi. Domenet ikke eksplisitt vist — samme forbehold |

**Ikke funnet noe sted, verken nivå 1 eller sekundærkilde:** Kinsky, Verbruggen, Davis, Diop nevnt ved navn i noen pressekonferanse. Fraværet er konsistent på tvers av alle kilder som er sjekket, men er fortsatt fravær av bevis, ikke bevis for fravær av risiko.

## Kilder — tillegg 20.–21. august

| Dato | Kilde | Funn |
|---|---|---|
| 20.8. | arsenal.com | Fullt Arteta-referat. **Nivå 1** |
| 20.8. | chelseafc.com | Alonso-referat. João Pedro har nierdrakten |
| 20.8. | BBC Sport liveblogg `c8kgv7dvg5d0t` | Carrick, Glasner, Le Bris ordrett. Paginert i sju sider |
| 21.8. | FFScout | Fredagens pressekonferansetider, Brighton-skader |
| 21.8. | Goal.com, mancity.com | Brightons oppstilling mot Villa; Maresca-pressekonferanse 13:30 |

## Åpne punkter per 3. september

| Punkt | Frist | Hva som avgjør det |
|---|---|---|
| **Neste PL-fikstursak** | **uken fra 21.9.** | MW10–12 (november). Sett sjekk i den uken |
| **MW13–20-kunngjøringen** | **uken fra 19.10.** | Treffer Free Hit-vinduet GW16–19 i `02`. Chip-planen kan ikke låses før den |
| Europa League- og Conference League-oppsett | Før GW5 | Ikke hentet denne kjøringen. Berører Bournemouth, Sunderland, Palace og Brighton — hvorav **Brighton (Verbruggen)** er i troppen. Palaces EL-kamp tor 17.9. er antatt, ikke verifisert |
| Newcastle–Bournemouth GW3: 12:30 eller 15:00? | Lav | API-et gir 12:30 to ganger. PL-artikkelens sammendrag ga 15:00. Ikke etterprøvd mot originalteksten |
| Leeds–Palace GW5: når ble den flyttet? | Lav | Ingen spillere i troppen berørt. Nivå 1-kilden som ble hentet var fra feil sesong |
| Arsenal- og Tottenham-radene i cuptabellen | Lav | Hviler på nivå 5 alene — arsenal.com (403) og tottenhamhotspur.com (401) avviste henting |
| **GW6–GW8-tabellene bør etterprøves** | Før GW6 | De ble skrevet gale én gang allerede (UTC/BST). Klokkeslettene er nå rettet mot både API-et og PL-artikkelen av 17. august, men rettelsen er gjort av samme part som lagde feilen |
| BGW/DGW | jan/feb | Bekreftes normalt ikke før FA-cup-omberamminger foreligger |

## Endringer i denne versjonen — 3. september 2026

Filen er **utvidet, ikke omskrevet**. Ingen tidligere seksjon er slettet. Endringene:

**Lagt til:** «Endringen 28. august — Man City–Sunderland» · GW5-tabellen · «GW6–GW8 — kontrollert» · «Ligacupen — runde 3, datoer bekreftet» med hviletabell · feilloggen om Brentford-utledningen · «Kunngjøringsplan for TV-flyttinger» · deadline-tabellen lest fra API-et · elleve nye rader i sjekkeloggen · to nye «forkastet kilde»-notater · datokolonne i ligacuptabellen · Everton lagt inn i ligacuptabellen · ny tabell over åpne punkter.

**Erstattet:** statustabellen «per 27. august» er avløst av «per 3. september». **Den gamle tabellen står fortsatt i filen**, under overskriften «Forrige status», fordi én av radene i den (ingen flyttinger i GW2–GW5) ble gal dagen etter at den ble skrevet, og det er verdt å kunne se.

**Endret:** GW4-deadlinen har mistet ⚠️-advarselen om at tallet var utledet — det er nå lest av API-et. GW8-betingelsen er flyttet fra «Fortsatt åpen» til «Lukket». Merknaden «Ikke verifisert: ligacupens runde 3 ... EFL har ikke publisert dato per kamp» er erstattet av de faktiske datoene, og den utledningen den inneholdt er ført opp som feil. Fet skrift er fjernet fra sjekkeloggens rader for 27.–28. august, siden de ikke lenger er nyeste kjøring. «Listen er intern konsistent» rettet til «internt».

### ⚠️ Rettelse samme dag, etter diff mot repo

Første versjon av denne seksjonen påsto **«Fjernet: ingenting.»** Det var galt, og brukeren fanget det ved å diffe mot repoet. Tre passasjer var faktisk slettet uten å være listet:

| Slettet | Status nå |
|---|---|
| `(Welbeck 50', Odofin selvmål 79')` i ligacuptabellen | **Gjeninnsatt** |
| «Bekreftet for GW2-planleggingen: ingen av de betingede endringene i tabellen over er utløst ennå» | **Gjeninnsatt**, merket som historisk |
| «Endringen flytter ingen kamp ut av sin runde ... Den flytter Haalands avspark åtte timer innenfor samme lørdag» | **Gjeninnsatt** som sitat i den lukkede GW8-seksjonen |

Dessuten mistet ligacuptabellen annoteringen «— avgjort 27. august» på Leeds-raden, og setningen «Dette er endelig avgjort, ikke betinget videre» falt ut. Begge er gjeninnsatt.

**Dette er samme feil som 22. august** («innhold slettet i en omskriving uten at slettingen ble flagget»), med en forverring: den gangen ble slettingen bare ikke nevnt. Denne gangen ble det skrevet en eksplisitt forsikring om at ingenting var slettet. **En usann «Fjernet: ingenting» er verre enn ingen endringslogg**, fordi den fjerner grunnen til å diffe.

**Regelen som følger:** «Fjernet: ingenting» skal aldri skrives fra hukommelse om hva som ble gjort. Enten produseres listen fra en faktisk diff mot forrige versjon, eller så skrives feltet som «ikke kontrollert». I denne økten fantes ikke diffen på Claudes side — bare i brukerens repo — og da er «ikke kontrollert» det eneste sanne svaret.

**Fjernet, endelig liste:** ingenting utover det som er erstattet av nyere innhold og listet under «Erstattet» og «Endret» over. Denne linjen er skrevet etter diff, ikke før.
