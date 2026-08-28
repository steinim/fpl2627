# Kampprogram — verifisert kalender og endringslogg

*Opprettet 20. august 2026. Vedlikeholdes av den planlagte kampprogram-sjekken.*
*Sist oppdatert 27. august 2026 — begge betingede endringene i GW4 og GW5 er avgjort etter ligacuptrekningen 26. august. GW4-tabellen ført inn.*

Denne filen er fasit for **datoer og klokkeslett**. `fixtures2627.csv` er fasit for **hvem som møter hvem i hvilken runde** — den er kontrollert 20. august og stemmer 30/30 på kamppar i GW1–3, men datokolonnen er ubrukelig fordi den setter hele runden til samme dag.

## Status per 27. august 2026

| Sjekkpunkt | Funn |
|---|---|
| Flyttede kamper i GW2–GW5 | **Ingen nye.** Alle TV-flyttinger er fra kunngjøringen 7. juli og står uendret |
| Utsatte kamper | **Ingen** |
| Bekreftet blankrunde (BGW) | **Ingen.** GW2, GW3, GW4 og GW5 har alle nøyaktig ti kamper |
| Bekreftet dobbeltrunde (DGW) | **Ingen** |
| Nyeste offisielle PL-kunngjøring | 17. august 2026 (GW6–9). **Ingen nyere fikstursak publisert per 27. august** |
| Betingede endringer GW4 og GW5 | **Begge avgjort 26. august — ingen av dem utløses.** Se under |
| Betinget endring GW8 | **Åpen.** Avgjøres av Champions League-trekningen 27. august |

Alle klokkeslett i GW2–GW5 er verifisert direkte mot FPLs `fixtures`-endepunkt 27. august, hvor samtlige 40 kamper har `provisional_start_time: false` — tidene er endelige, ikke foreløpige.

Blank- og dobbeltrunder bekreftes normalt ikke før januar/februar, når FA-cup-omberamminger foreligger. Chip-planen i `02` (Free Hit GW16–19, Triple Captain på dobbeltrunde) hviler derfor fortsatt på antakelser, ikke på kunngjort kalender.

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

## GW4 — lørdag 12. til mandag 14. september

**GW4 har ingen fredagskamp.** Første avspark er lørdag 12. september 15:00 UK, som gir deadline **lørdag 12. september 13:30 BST / 14:30 norsk**. ⚠️ Tallet er **utledet** av regelen om 90 minutter før første avspark, ikke lest av appen. Bekreft mot appen når GW3 er avviklet — dette er første runde i sesongen med lørdagsdeadline, og det er lett å planlegge etter fredag av vane.

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

**Kilde:** premierleague.com 7. juli 2026, kryssjekket mot FPLs `fixtures`-endepunkt 27. august. Slottene kl. 15:00 er de kampene som ikke er TV-flyttet; klokkeslettet er bekreftet direkte i API-et, ikke utledet av standardregelen.

## Betingede endringer

### Avgjort 26. august 2026 — ingen av dem utløses

Ligacupens tredje runde ble trukket onsdag 26. august. Utløseren i begge tilfeller var at én av klubbene skulle møte et **Champions League-lag** i tredje runde. Trekningen ga:

| Klubb | Motstander i ligacup runde 3 | I Champions League? |
|---|---|---|
| Leeds | Chelsea eller Luton (borte) | **Nei** — Chelsea spiller ikke europacup i 2026/27 |
| Newcastle | Millwall (borte) | **Nei** |
| Brentford | Reading (borte) | **Nei** |
| Chelsea | Leeds (hjemme), hvis de slår Luton | **Nei** |

| Kamp | Runde | Utfall |
|---|---|---|
| Leeds – Newcastle | GW4 | **Står fast man 14.9. 20:00.** Flyttes ikke til lørdag |
| Brentford – Chelsea | GW5 | **Står fast fre 18.9. 20:00.** **GW5-deadlinen blir dermed fredag 18. september 18:30 BST / 19:30 norsk** |

**Merk at utfallet er uavhengig av Chelsea–Luton torsdag 27. august.** Verken Chelsea eller Luton spiller Champions League, så ingen av de to betingelsene kan utløses uansett resultat. Dette er endelig avgjort, ikke betinget videre.

De fem engelske Champions League-lagene i 2026/27 er Arsenal, Man City, Man Utd, Aston Villa og Liverpool. Alle fem er i trekningen plassert mot andre motstandere: Ipswich–Arsenal, Man City–Norwich, Man Utd–Brighton, Coventry–Aston Villa, Liverpool–Tottenham.

### Fortsatt åpen

| Kamp | Runde | Står nå | Flyttes til hvis | Avgjøres av |
|---|---|---|---|---|
| Aston Villa – Man City | GW8 | lør 24.10. 12:30 | lør 24.10. 20:00 | Villa trukket bortekamp i CL onsdag 21. oktober (ligafase runde 3, spilles 20.–21. oktober). **CL-trekningen er 27. august**; kampoppsettet publiseres normalt et døgn eller to senere |

Endringen flytter ingen kamp ut av sin runde og har derfor ingen poengkonsekvens. Den flytter Haalands avspark åtte timer innenfor samme lørdag. Sjekkes ved neste kjøring.

## Kilder og sjekkelogg

| Dato sjekket | Kilde | Funn |
|---|---|---|
| 20.8.2026 | premierleague.com «All 380 fixtures for 2026/27» (19.6.2026) | Grunnliste GW1–4 |
| 20.8.2026 | premierleague.com «Fixture amendments … August and September» (7.7.2026) | Alle TV-flyttinger GW1–5 |
| 20.8.2026 | premierleague.com «Fixture amendments … October and November» (17.8.2026) | GW6–9. Ingen endring for GW1–3 |
| 20.8.2026 | chelseafc.com, liverpoolfc.com, tottenhamhotspur.com, mancity.com | Kryssjekk av fire enkeltkamper |
| 20.8.2026 | Sky Sports (19.6. og 22.7.2026) | Uavhengig bekreftelse av tider |
| **27.8.2026** | **FPL `fixtures`-endepunkt, event 2–5** | **Alle 40 kamptider bekreftet. `provisional_start_time: false` gjennomgående. Ti kamper per runde — ingen BGW/DGW** |
| **27.8.2026** | **premierleague.com «Possible fixture changes in 2026/27» (7.7.2026)** | **Ordlyden i alle tre betingede endringene, verifisert direkte** |
| **27.8.2026** | **premierleague.com nyhets- og publikasjonsarkiv** | **Ingen fikstursak publisert etter 17. august** |
| **27.8.2026** | **leedsunited.com (26.8.2026) — nivå 1** | **Leeds borte mot vinneren av Chelsea–Luton i ligacupens runde 3** |
| **27.8.2026** | **101greatgoals (26.8.2026) — nivå 5** | **Full trekningsliste for runde 3. Se konsistenssjekken under** |
| **27.8.2026** | **Sky Sports (27.5.2026 og 26.8.2026)** | **Ni engelske europacuplag: Arsenal, Man City, Man Utd, Aston Villa, Liverpool (CL); Bournemouth, Sunderland, Crystal Palace (EL); Brighton (Conference). Chelsea er ikke blant dem** |
| **27.8.2026** | **uefa.com** | **CL-ligafasetrekning 27. august. Runde 3 spilles 20.–21. oktober** |

**Konsistenssjekk av trekningslisten (nivå 5-kilden).** De ni engelske europacuplagene kommer inn først i runde 3 og spilte ikke runde 2. Nøyaktig ni lag i trekningslisten har ikke spilt runde 2: Crystal Palace, Man Utd, Brighton, Man City, Sunderland, Arsenal, Aston Villa, Bournemouth og Liverpool. Det er identisk med listen fra Sky. Chelsea spilte runde 2 mot Luton og er dermed ikke europacuplag. Listen er intern konsistent, og Leeds-raden er dessuten bekreftet fra klubbens egen side. **Konklusjonen om at ingen av de to betingelsene utløses, hviler ikke på nivå 5-kilden alene.**

**Ikke verifisert:** ligacupens runde 3 spilles i ukene fra 7. og 14. september, men EFL har ikke publisert dato per kamp — leedsunited.com skriver eksplisitt at fulle kampdetaljer kommer senere. At Leeds', Newcastles og Brentfords kamper havner i uken fra 7. september følger logisk av PLs egen betingelse (CL-lagene spiller ligafase 8.–10. september og må derfor ha cupkampen i uken fra 14. september), men det er **utledet, ikke kunngjort.** Har konsekvens for rotasjonsrisiko rundt GW4 og bør bekreftes når EFL setter datoene.

**Motstridende kilde, avklart:** Wikipedias «2026–27 Premier League» oppgir sesongstart 22. august. Det er feil — premierleague.com og to Sky-artikler gir fredag 21. august. Wikipedia-siden er ikke oppdatert etter programslippet. Vi stoler på premierleague.com.

**Forkastet kilde, 27. august:** chelseafc.coms artikkel «Chelsea handed home tie in Carabao Cup third round draw» ble hentet og viste seg å omtale Middlesbrough/Barnsley og datoene 22.–23. september **2020**. Feil sesong, fanget av firukersregelen i `03`. Ikke brukt.

**Ikke verifisert:** premierleague.com/en/fixtures lastes ikke uten JavaScript, så kampdatabasen er ikke lest direkte per i dag. Verifiseringen bygger på PLs egne artikler og FPL-API-ets `fixtures`-endepunkt. 15:00-kampene uten TV-dekning er utledet av PLs standardregel («all kick-off times are 15:00 BST unless otherwise mentioned») for GW1–3, men for GW4 er de bekreftet direkte i API-et.


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

## Kilder — tillegg 20.–21. august

| Dato | Kilde | Funn |
|---|---|---|
| 20.8. | arsenal.com | Fullt Arteta-referat. **Nivå 1** |
| 20.8. | chelseafc.com | Alonso-referat. João Pedro har nierdrakten |
| 20.8. | BBC Sport liveblogg `c8kgv7dvg5d0t` | Carrick, Glasner, Le Bris ordrett. Paginert i sju sider |
| 21.8. | FFScout | Fredagens pressekonferansetider, Brighton-skader |
| 21.8. | Goal.com, mancity.com | Brightons oppstilling mot Villa; Maresca-pressekonferanse 13:30 |

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

**Bekreftet for GW2-planleggingen:** ingen av de betingede endringene i tabellen over er utløst ennå.

## Ligacupen 2026/27 — troppens klubber

Ført inn 27. august 2026 fordi cupkampene i uken fra 7. og 14. september ligger tett på GW4 og påvirker rotasjonsrisiko.

| Klubb i troppen | Runde 2 | Runde 3 |
|---|---|---|
| Arsenal | — (europacuplag, kom inn i runde 3) | Ipswich (borte) |
| Man City | — (europacuplag) | Norwich (hjemme) |
| Man Utd | — (europacuplag) | Brighton (hjemme) |
| Brighton | — (europacuplag) | Man Utd (borte) |
| Ipswich | Slo Leicester 3–1 | Arsenal (hjemme) |
| Hull | Slo Stoke på straffer | Sunderland (borte) |
| Leeds | Slo Nottingham Forest 2–0 | Chelsea eller Luton (borte) |
| Chelsea | Luton (hjemme), 27. august | Leeds (hjemme) hvis de vinner |
| Nottingham Forest | **Ute** — tapte 0–2 for Leeds | — |
| Tottenham | Slo Charlton | Liverpool (borte) |

Man Utd–Brighton og Ipswich–Arsenal er kamper mellom to klubber troppen har spillere i. Ingen av rundene kolliderer med en Premier League-runde, men datoene per kamp er ikke satt ennå.
