# Regler 2026/27 og sesongplan

*Sist oppdatert: 3. september 2026, sent — Triple Captain flyttet fra GW7 til GW5 etter at Champions League-kalenderen ble kontrollert mot UEFA. GW7 ligger klemt mellom MD2 og MD3; GW5 er den eneste rene uka blant Citys svake hjemmekamper før GW19. Feilen som lå bak GW7-valget er loggført i `03`. Kontrollpost etter GW4 lagt inn under Beslutningspunkt.*
*Forrige: 3. september 2026, kveld — Triple Captain flyttet fra utløserbasert uten dato til planlagt GW7 med GW5 som reserve. Bench Boost-utløseren utvidet fra étt til tre ledd.*
*Forrige: 3. september 2026 — Bench Boost-raden tallfestet mot faktiske benkepoeng fra snapshot-repoet (12 og 10 i GW1–2). Betingelsen «avhenger av benken» var uten målestokk; den har nå en utløser. Datakilden ført inn i `03`.*
*Forrige: 28. august 2026 — GW2-deadlinen (18:30 BST / 19:30 norsk) uavhengig re-verifisert mot tre kilder (Fantasy Football Scout, premierleague.com, onsidearena.com) etter at en Claude-økt feilaktig hevdet et avvik mot et komprimert minnesammendrag. Ingen endring i tallet — se feilloggen i `03` for hva som gikk galt.*
*Forrige: 25. august 2026, kveld — sesongplanens byttebegrunnelse korrigert, Chelseas GW16–20-blokk knyttet til wildcardet.*
*Forrige: 25. august 2026 — GW13-premisset for O'Reilly markert som uavklart etter GW1, GW1-datapunkt lagt inn i BPS-seksjonen.*
*Forrige: 22. august 2026 — chip-seksjonen omskrevet: skillet mellom planlagt og utløserbasert, overlappet oppløst, spisser lagt inn i DefCon-linjen.*
*Forrige: 22. august 2026, sluttgjennomgang — spisser lagt inn i DefCon-linjen.*
*Forrige: 22. august 2026 — chip-bindinger fra `05` (én chip per runde, Free Hit ikke to runder på rad, hva som kan avbrytes), BPS-punkt 1 presisert, GW6- og GW19-deadline ført inn, rettet sti til `04`.*
*Forrige: 21. august 2026, kveld — Konsa-kjøpet til Arsenal bekreftet (ikke spilleberettiget GW1), trenerlisten komplettert til 20 av 20, Bench Boost avblokkert, City-risikoen oppgradert fra rykte til faktum.*

## Nøkkeldatoer

| | |
|---|---|
| GW1-deadline | fredag 21. august 2026, 18:30 BST / 19:30 norsk |
| GW1 spilles | **21.–24. august.** Siste kamp er Fulham–Chelsea **mandag 24. august 20:00 BST** |
| GW2-deadline | fredag 28. august, 18:30 BST / 19:30 norsk |
| GW2 spilles | 28.–31. august. Siste kamp Villa–Arsenal mandag 31. august 20:00 |
| GW3-deadline | fredag 4. september, 18:30 BST / 19:30 norsk |
| GW3 spilles | 4.–6. september |
| GW4-deadline | lørdag 12. september, 13:30 BST / 14:30 norsk |
| Sesongen | 21. august 2026 – 30. mai 2027 |
| Overgangsvindu stenger | tirsdag 1. september 2026, 23:00 BST / 00:00 norsk tid natt til 2. sept. |
| Første chip-sett må brukes innen | **GW19-deadline, lør 2. januar 14:30 norsk** |
| GW6-deadline | **lør 10. oktober 12:00 norsk** (11:00 britisk) |
| Full deadlineliste, alle 38 runder | `05-spillets-regler.md` — **oppgitt i norsk tid**, kryssjekket mot API-et på fem ankere |
| Landslagspauser | etter GW5 (19. sep → 10. okt) og etter GW10 (7. nov → 21. nov) |

⚠️ **Rettelse 20. august:** denne tabellen sa tidligere «GW1 spilles 21.–23. august». Det er feil. Fulham–Chelsea ligger mandag 24. august 20:00 (Sky Sports), bekreftet på premierleague.com og chelseafc.com. **João Pedro spiller mandag.** GW1 er dermed ikke ferdig før mandag kveld, bonus/DefCon låses tirsdag 25. august 09:00 UK, og prisendringene før GW2-deadline fredag går på et fire dager kort vindu. Full verifisert kampliste for GW1–3, med deadliner og betingede endringer, ligger i `04-kampprogram-og-endringslogg.md`.

**To av de tre neste deadlinene er fredager**, fordi både GW2 og GW3 åpner med fredagskamp (Palace–City 28.8., Ipswich–Liverpool 4.9.). Regel 5 i `01` — «ingen bytter før torsdag» — gir dermed under ett døgn margin i GW2 og GW3.

**Overgangsvinduet stenger etter GW2-deadline, ikke før.** Klubbene kan altså fortsatt hente og selge spillere mens GW1 og GW2 spilles. Startplasser som ser avklarte ut nå, kan endres av en signering i siste uke — spesielt hos opprykkslagene, som fortsatt bygger tropp. Gjelder direkte for Slater (Hull) og Davis (Ipswich).

## Det som er endret til 2026/27

**BPS er omskrevet.** Verifisert mot fire kilder 19. august. Den tidligere teksten her var ufullstendig og delvis feil.

| Endring | Verifisert innhold |
|---|---|
| CBI | 1 BPS per **tre** klareringer/blokkeringer/interceptions, mot 1 per to |
| Å bli taklet | **−1 BPS-straffen er fjernet helt.** Sto ikke i denne filen før |
| Keeperredninger | **+2 BPS per redning**, +1 ekstra for skudd innenfor boksen |
| Keeper, ny kategori | **+1 BPS for redning av «big chance»** |
| Redning utenfor boksen | Egen +1-kategori fjernet |
| Strafferedning | 8 → 7 BPS, men +1 tilbake via big chance |
| Låsing | Flyttet til 09:00 UK dagen etter siste kamp — færre tapte DefCon-oppgraderinger |

**Tre korreksjoner til den opprinnelige tesen:**

1. **«Holdende midtbanespillere taper» holder ikke.** Endringen treffer kun C, B og I. **Takler er urørt** — verifisert på begge sider: 2 BPS per vunnet takling både i 2025/26 og i 2026/27-tabellen i `05`. En dyptliggende midtbanespiller som bærer ball *vinner* dessuten på at taklet-straffen er borte. Midtstopper-halvdelen av tesen står; midtbane-halvdelen gjør det ikke.

⚠️ **Presisert 22. august mot `05`.** Denne linjen sa tidligere «takler **og ballerobringer** er urørt», og behandlet de tre kategoriene som sammenlignbare. Det er de ikke:

| Kategori | BPS 2026/27 | Per aksjon |
|---|---|---|
| Vellykket takling | 2 | **2,00** |
| Ballerobring | 1 per 3 | 0,33 |
| Klarering, blokkering, interception | 1 per 3 | 0,33 |

En takling er verdt **seks ganger** så mye per aksjon som en klarering, og CBI ligger nå på nøyaktig samme rate som ballerobringer. Ballerobringsverdien for 2025/26 er **ikke** verifisert, så «urørt» gjelder bare taklingene. Retningen i tesen står; premisset var grovere enn tabellen tillater.

2. **«Keepere vinner» er riktigere enn antatt, men peker motsatt vei av sesongplanen.** Gevinsten er ikke bare relativ — det er en ny big chance-kategori og +1 for skudd i boksen. Men det er **redningsdrevet**. En keeper som redder seks skudd, hvorav to store sjanser, henter langt mer BPS enn en toppklubbkeeper med én redning i en 3–0-seier. **Endringen favoriserer travle keepere i midt- og bunnlag.** Se merknaden til GW16 under.

3. **Størrelsesorden.** BPS avgjør kun bonuspoeng — maks 3 per kamp, i konkurranse med 21 andre spillere. DefCon-poengene (2 per kamp ved 10 CBIT / 12 CBIRT) er **uendret** og er der mesteparten av forsvarsverdien ligger. En midtstopper som mister en tredjedel av BPS-en fra klareringer, mister anslagsvis 5–10 bonuspoeng over en sesong. Det er 1–2 % av en sesongtotal.

**Nedgradert:** dette er **ikke** «den viktigste enkeltendringen for laguttak». Det er en andreordens rebalansering. Retningen — bort fra stillestående midtstoppere, mot offensive backer, ballbærere og travle keepere — er riktig. Vekten var overdrevet, og overdrivelsen drev en bekymring for forsvarsstrukturen som ikke var berettiget.

**Etterprøves etter GW5:** faktisk bonusfordeling mellom keepere, backer og midtstoppere i GW1–5.

⚠️ **GW1-datapunkt, ført inn 25. august.** Full keepertabell ligger i `03`. Kortversjon: Kinsky leverte akkurat profilen punkt 2 kaller vinneren — fem redninger bak et nybygget Spurs-forsvar — og fikk **15 BPS og 2 poeng**. Verbruggen med **null** redninger og clean sheet fikk **25 BPS og 6 poeng**. Tzolakis, som hadde begge deler, fikk 41 BPS og 3 bonus.

**Konsekvens for punkt 2:** «endringen favoriserer travle keepere» er for upresist. Redninger løfter BPS *gitt* clean sheet; uten clean sheet gjør de lite. Det trekker GW16-vurderingen tilbake mot clean sheet-aksen, altså **mot** Raya, ikke bort fra ham. Ett datapunkt av fem — ingen beslutning endres nå.

**Uendret:** DefCon-poeng (forsvarere 10 CBIT, **midtbane og spisser** 12 CBIRT → 2 poeng, tak på 2 per kamp — se `05`), 5 rullerende frie bytter med tak på 5, to sett med chips (Wildcard, Free Hit, Triple Captain, Bench Boost per halvsesong).

**Nytt ellers:** live poeng, rank og miniligaoppdatering. Projisert bonus etter 20 minutter. Offisiell price change predictor, som fjerner mye av informasjonsfortrinnet i prisspekulasjon. Lockdown flyttet til 09:00 UK dagen etter siste kamp.

⚠️ **Status 21. august:** den offisielle predictoren og tredjeparts-verktøyene (FFScout, FPLedits) viste alle «under oppgradering, kommer tilbake før GW2-deadline» da vi sjekket. Ingen prisendringsprognose er dermed verifiserbar i dag for noen spiller, inkludert Konsa. Se `01` for konsekvensen.

**11 posisjonsendringer:**
- Til forsvar: Rio Cardines, Eric Moreira, Ryan Sessegnon, Mats Wieffer
- Til midtbane fra forsvar: Lamare Bogarde, Patrick Dorgu, Keane Lewis-Potter, Myles Lewis-Skelly
- Til midtbane fra angrep: Eli Junior Kroupi (£7,5m, opp £3,0m)
- Til angrep fra midtbane: Omar Marmoush, Georginio Rutter

## Ligaen 2026/27

Opprykk: Coventry City, Ipswich Town, Hull City. Nedrykk fra 25/26: West Ham, Burnley, Wolves.
Regjerende mestere: Arsenal. Champions League: Arsenal, Man City, Man Utd, Aston Villa, Liverpool. Europa League: Bournemouth, Sunderland, Crystal Palace. Conference League: Brighton.

## Trenersituasjon — komplett liste over endringer

*Den tidligere listen manglet tre klubber. Se feilloggen i `03`.*

| Klubb | Trener | Endring | Konsekvens for laguttak |
|---|---|---|---|
| Man City | Enzo Maresca | Ny, etter Guardiolas avgang | Uprøvd system, VM-belastet tropp |
| Liverpool | Andoni Iraola | Ny | Szoboszlai brukes sentralt, ikke som høyreback |
| Chelsea | **Xabi Alonso** | Ny fra 1. juli 2026 | Manglet i tidligere liste |
| Ipswich | **Gary O'Neil** | Ny 23. juni, McKenna trakk seg | Manglet i tidligere liste. Spiller 4-2-3-1 og treer med wingbacker |
| Bournemouth | **Marco Rose** | Ny, etter Iraola til Liverpool | Manglet i tidligere liste |
| Forest | Oliver Glasner | Ny | Spiller 3-4-2-1 med offensive wingbacker |
| Spurs | Roberto De Zerbi | Ny | Tropp under full ombygging |
| Crystal Palace | Sage | Ny | — |
| Man Utd | Michael Carrick | Fast etter interimperiode | 4-2-3-1 med backfirer |
| Hull | Sergej Jakirović | Uendret | Førte klubben opp via playoff |
| Leeds | Daniel Farke | Uendret | Treer bak med wingbacker |

Newcastle har mistet Howe, Guimarães og solgt for over £240m — behandle dem som svekket mot fjorårets nivå.

### Komplettering 21. august — alle tjue er nå navngitt

Pressekonferanselistene for 19.–21. august navngir hver enkelt trener med klubb. Det er primærkildebekreftelse på identitet, ikke på taktikk.

| Klubb | Trener | Kilde |
|---|---|---|
| Coventry | **Frank Lampard** | Presser onsdag 19.8. |
| Hull | Sergej Jakirović | Presser 20.8. 13:00 |
| Crystal Palace | Sage | Presser 20.8. 13:00 |
| Arsenal | Mikel Arteta | Presser 20.8. 13:30 |
| Bournemouth | Marco Rose | Presser 20.8. 13:30 |
| Chelsea | Xabi Alonso | Presser 20.8. 13:30 |
| Leeds | Daniel Farke | Presser 20.8. 13:30 |
| Sunderland | **Régis Le Bris** | Presser 20.8. 13:30 |
| Forest | Oliver Glasner | Presser 20.8. 14:00 |
| Newcastle | **Matthias Jaissle** | Presser 20.8. 16:30 |
| Man Utd | Michael Carrick | Presser 20.8. 17:30 |
| Fulham | **Álvaro Arbeloa** | Presser 21.8. 10:00 |
| Brighton | Fabian Hürzeler | Presser 21.8. 12:00 |
| Brentford | **Keith Andrews** | Presser 21.8. 13:30 |
| Everton | **David Moyes** | Presser 21.8. 13:30 |
| Ipswich | Gary O'Neil | Presser 21.8. 13:30 |
| Liverpool | Andoni Iraola | Presser 21.8. 13:30 |
| Man City | Enzo Maresca | Presser 21.8. 13:30 |
| Tottenham | Roberto De Zerbi | Presser 21.8. 13:30 |
| Aston Villa | Unai Emery | Presser 21.8. 14:00 |

**Tjue av tjue.** Feilen «trenerlisten ufullstendig» i `03` er dermed lukket. Merk at Newcastle = Jaissle og Fulham = Arbeloa var **helt fraværende** fra tidligere versjoner, ikke bare uverifiserte.

⚠️ **Kolonnen «konsekvens for laguttak» i tabellen over dekker fortsatt bare elleve klubber.** Identitet er verifisert; spillestil er det ikke.

**Strukturell observasjon:** minst fire av klubbene i troppen vår spiller nå med treer bak og wingbacker (Forest, Leeds, Ipswich i noen kamper, Hull i noen kamper). Det forsterker BPS-tesen — wingbacker samler både DefCon og offensive returer.

## Fikstursvanskelighet per blokk

Beregnet fra `fixtures2627.csv`. Lavere er lettere for clean sheets. Motstandere i tre nivåer, justert for hjemme/borte.

| Klubb | GW1–5 | 6–10 | 11–15 | 16–20 | 21–25 |
|---|---|---|---|---|---|
| Man Utd | **1,86** | 2,34 | 2,06 | 2,34 | **2,74** |
| Arsenal | 2,46 | **1,74** | 2,46 | 1,94 | 2,06 |
| Tottenham | 2,14 | 2,06 | **1,74** | **2,66** | 1,74 |
| Man City | 1,94 | 2,46 | 2,14 | **1,86** | 2,66 |
| Forest | 2,14 | 2,26 | 2,26 | 1,94 | 2,46 |
| Leeds | 2,14 | **2,66** | 2,26 | 2,14 | 2,26 |
| Liverpool | 1,86 | 2,54 | 2,14 | 2,06 | 2,26 |
| Ipswich | 2,46 | 1,94 | 2,06 | 2,34 | 2,34 |
| Hull | 2,46 | 1,94 | 2,34 | 2,26 | 2,14 |
| Chelsea | 2,26 | 2,34 | 2,14 | 1,86 | 2,06 |

**Beste seksrundersvindu, GW6–25:** Arsenal GW17–22 (1,67) · Tottenham GW7–12 (1,67) · Man City GW13–18 (1,83) · Liverpool GW15–20 (1,83)

⚠️ **Merknad 25. august:** **Chelseas beste blokk er GW16–20 på 1,86**, og GW16 er runden wildcardet allerede er planlagt til. Det er den strukturelt riktige inngangen for Chelsea-aktiva — ikke GW6, som gir dem 2,34, dårligere enn Forest-eksponeringen troppen alt har. Se beslutningspunktet i `01`.

### ⚠️ Begrensning i datasettet

`fixtures2627.csv` daterer alle kamper i en runde til samme dag. Faktiske avspark er spredt over fire dager: GW1 går fredag 21. til **mandag 24.** august (Hull–Man Utd 22., Man City–Bournemouth 23., **Fulham–Chelsea 24.**). GW2 går fredag 28. til mandag 31. august.

**Konsekvens:** CSV-en er gyldig på rundenivå og for all fikstursvanskelighet. Den er **ikke** brukbar til kampdatoplanlegging — altså blankrunder, dobbeltrunder, kamputsettelser eller chip-timing knyttet til konkrete datoer. Bruk Premier Leagues egne sider til det.

**Rundenivået er kontrollert 20. august:** alle 30 kampparene i GW1–3 i CSV-en stemmer mot premierleague.com. Feilen i den forrige opplastede CSV-en (null av ti GW1-kamper korrekte, logget i `03`) gjentar seg ikke i denne filen. **Kun datokolonnen er ubrukelig.**

## Sesongplan

| GW | Handling | Begrunnelse |
|---|---|---|
| 1–5 | Spar bytter, null strukturelle endringer | Fem frie ved GW6. Taket er 5, så sparing utover GW6 er bortkastet. |
| 6 | Calvert-Lewin ut. Arsenal-forsvarer inn. | Leeds går inn i 2,66-blokk. Arsenal inn i sin beste tidlige blokk på 1,74. |
| 9 | Shaw og Mbeumo ut | Uniteds verste tidlige blokk: Chelsea (B), Villa (H), Liverpool (B). |
| 12 | United-eksponering tilbake | Brentford (H), Newcastle (B), Coventry (H), Palace (B). |
| 13 | O'Reilly £6,5m inn | Citys beste vindu er GW13–18. |
| 16 | **Wildcard.** Restrukturer inn i Arsenals GW17–22. United ut permanent. Keeperbyttet er ikke lenger gitt — se under. | Spurs' verste blokk (2,66) møter Arsenals beste (1,67). United går inn i 2,74. Bruker også chipen før GW19-fristen. |

⚠️ **Merknad til rad GW1–5, ny 25. august: begrunnelsen holder ikke som skrevet.**

Raden begrunner sparingen med «fem frie ved GW6, taket er 5». Men planen **bruker ikke fem i GW6** — den bruker ett (Calvert-Lewin ut). Bytter kjøpt inn i GW2–5 kommer altså fra en beholdning planen selv ikke har jobb til.

**Riktig formulering av kostnaden:** ett bytte i GW2 tar deg fra fem til fire ved GW6, og det femte hadde ingen oppgave. Den reelle kostnaden er derfor ikke byttet — den er **at du handler på ett kampdatapunkt**, som er det `03` finnes for å hindre. Argumentet mot tidlig handling er metodisk, ikke økonomisk. **Ikke bruk taket som unnskyldning når det ikke binder.**

**Merknad til GW6, oppdatert 17. august:** planen sier «Arsenal-forsvarer inn». Saliba (rygg) og Timber (lyske) er begge langtidsskadet og sto over Community Shield. Arsenals faktiske bakre fire 16. august var **White, Mosquera, Gabriel, Calafiori** i 4-3-3. Kandidatlisten er altså Gabriel £8,0m, Mosquera £5,5m eller White £5,5m — ikke de to som var tenkt.

To bevegelige deler før valget tas: Arsenal jakter **Ezri Konsa** fra Villa som forsvarsdekning, og Saliba kan være tilbake. Begge deler treffer Mosquera, som har plassen nettopp fordi Saliba mangler. Gabriel og Calafiori er de eneste to som ikke berøres.

**Vi eier allerede Calafiori.** Vurder derfor om GW6-byttet i det hele tatt skal gå til forsvar, eller om Arsenal-eksponeringen heller bør tas offensivt (Tzolis £6,5m startet Community Shield med to assists).

**Merknad til GW6, oppdatert 19. august:** Arsenal-eksponeringen er **allerede tatt**, offensivt, via Tzolis £6,5m (Szoboszlai ut). GW6-byttet skal derfor ikke lenger gå til Arsenal-forsvar. Det frigjorte byttet går til Calvert-Lewin-utgangen alene.

**Merknad til GW6, ny 21. august — Konsa-kjøpet bekreftet, rykte er nå fakta.** Arsenal har kjøpt **Ezri Konsa** fra Aston Villa: £51m + £4m i tillegg (Sky Sports, ESPN, Just Arsenal, alle 21. august). FPL-pris **£4,5m** (FFScout, FPL Mate).

⚠️ **Ikke spilleberettiget i GW1.** Sky Sports (20. august): Konsa rakk ikke torsdagens registreringsfrist for kampen mot Coventry. Han har heller ingen oppkjøring — forlenget VM-ferie innvilget av Emery, misset Super Cup og generalprøven mot Gladbach. Tidligst tenkelige debut: **Villa borte, GW2 (31. august)** — ikke garantert (FPL Mate: «far from guaranteed in GW2 either»).

**Konsekvens for GW6-planen:** Konsa er nå det bekreftede navnet for «Arsenal-forsvareren», forutsatt at han er integrert innen GW6 og Saliba fortsatt er ute. Mosqueras plass er fortsatt kortsiktig betinget av Saliba-fraværet. **Vurdert som GW1-bytte (Diop → Konsa) 21. august og avvist** — se `01` for detaljene. Beslutningen om Konsa til GW6 tas på faktisk spilletid i GW2–5, ikke nå.

⚠️ **Prisrisikoen er snudd — verifisert 25. august. Denne linjen er avlyst, ikke bekreftet.**

Konsa star i **£4,5m uendret**, eierandel **12,2 %**, og markedet **selger**: 94 054 ut mot 18 675 inn i inneværende byttevindu. FPLs egen prisendringsprediktor gir **−35,8 %** mot prisfall.

**Risikoen for at han blir dyrere før GW6 finnes ikke lenger. Den nye risikoen er motsatt: at han fortsatt ikke har spilletid når GW6 kommer.** Fallende pris og fallende eierandel på en nysignert spiller uten minutter er ikke et kjøpssignal — det er markedet som priser inn samme usikkerhet vi selv har ført.

✅ **Verktøyspørsmålet er også løst.** `price_change_percent` og `price_change_projections` ligger nå per spiller i FPLs eget `bootstrap-static`. **Bruk den i stedet for FFScout og FPLedits** — det er samme kilde som prisene selv.

**Historikk, skrevet 21. august:** «om Konsas eierandel stiger raskt før han faktisk spiller, kan prisen gå opp før GW6-vinduet. Verken FFScouts eller FPLedits' price change-verktøy leverte tall 21. august.»

**Merknad til GW9, oppdatert 21. august:** den forrige merknaden sa at Mbeumo er «projisert som Uniteds spiss». Det premisset er borte — Šeško er tilbake i trening og nierkonkurransen er fire-fem navn (se `01`). **GW9-utgangen står uendret, fordi den alltid hvilte på program og ikke på rolle.** Men begrunnelsen skal ikke lenger vise til spissrollen.

**Merknad til GW13, ny 17. august:** O'Reilly startet som venstreback i firer i Maresca's første konkurransekamp (Community Shield 16. august, 4-3-3: Donnarumma; Khusanov, Dias, Gvardiol, O'Reilly). Rollen er bekreftet under den nye treneren, ikke bare antatt fra i fjor. Han ble byttet ut etter 54 minutter i en 0-3-kamp.

⚠️ **Merknad til GW13, ny 25. august — premisset er nå usikkert, men ikke motbevist.**

I seriedebuten (City 2–1 Bournemouth) startet O'Reilly igjen, men **Gvardiol spilte venstreback og scoret**, mens Rico Lewis startet i bakre kjede. **O'Reilly ble byttet ut på 63'** — bekreftet fra play-by-play. Det er de to harde faktaene.

Hvor O'Reilly selv sto, er **ikke avklart**: mancity.com lister elleveren uten posisjoner, FotMob fører ham i midtbanen (nivå 5), og Sportradars «defender» er FPL-klassifisering, ikke banerolle. **Denne merknaden endrer derfor ikke planen.** Den flytter et punkt fra «bekreftet venstreback» til «uavklart rolle, bekreftet startplass, byttet ut på 63'».

**To reelle risikoer å følge fram til GW13, uavhengig av rolleavklaringen:**
1. **Minutter.** Byttet ut på 54' i Community Shield og 63' i seriedebuten. To av to under 65 minutter.
2. **Konkurranse om venstrebacken.** Gvardiol tok den i seriedebuten og scoret.

Rollen skal bekreftes fra mancity.com eller et fulltekstreferat før GW13-beslutningen tas. Se `03` for hvorfor den ikke føres inn som fakta nå.

**Bonus fra samme kamp:** Guehi startet og scoret (10 poeng, £6,0m), Semenyo startet (mot det som var ført i arkivfila), og Cherki kom inn på 63' og la begge målgivende. Alle tre står i `01`.

**Merknad til GW16, oppdatert 21. august — spørsmålet er nå Verbruggen/Kinsky → Raya.** Troppen har fra 21. august to keepere som begge spiller (Verbruggen £4,5m BHA, Kinsky £4,5m TOT). Et Raya-kjøp må derfor erstatte én av dem, ikke en død toer, og den frigjorte £4,5m-en må plasseres. Avveiningen under gjelder fortsatt.

**Merknad til GW16, ny 19. august — Kinsky → Raya er satt på hold.** Byttet ble skrevet inn under premisset «BPS-omskrivingen gjør keepere til vinnerne», og ble derfor lest som et argument for å oppgradere til en toppklubbkeeper. Den verifiserte mekanikken sier det motsatte: keepergevinsten kommer fra **redninger og big chance-redninger**, ikke fra clean sheets. Raya på £6,0m bak Arsenals forsvar redder få skudd. Kinsky på £4,5m bak et nybygget Spurs-forsvar redder mange.

Byttet kan fortsatt være riktig **på clean sheet-aksen** i Arsenals 1,67-blokk. Men det er nå en avveining mellom to akser, ikke en følge av tesen. **Avgjøres på faktisk BPS-data etter GW5, ikke før.**

**City-eksponeringen — oppgradert fra rykte til faktum 21. august.** Formuleringen «berører Haaland indirekte» var for mild.

⚠️ **Denne seksjonen ble skrevet to ganger 21. august. Første versjon var inflatert.** Den førte seks poster og kalte tilførselen «demontert». Tre av postene holdt ikke mot Marescas egen pressekonferanse samme ettermiddag. Korrekt bilde:

| Bevegelse | Status 21. august | Kilde |
|---|---|---|
| Rodri | **Ute av klubben** | Bekreftet. Var rykte i `01` |
| Reijnders | **Ute av klubben** | Bekreftet |
| Savinho | **£75m-avtale med Spurs** | Bekreftet |
| Doku | **Skadet, 2–3 uker** | **Maresca, primærkilde** |
| Nunes | **Tilbake. Ikke skadet** | **Maresca, primærkilde** |
| Marmoush | **Ingen bekreftelse.** Maresca nevnte ham ikke | — |

**Marescas ordlyd: kun Doku er ute.** Skadebildet er altså lite; det er avgangene som er reelle.

**Haaland blir stående — regel 1 og 3 i `01`.** Tre avganger på fjorten dager er verdt å følge, men «demontert» var feil ord, og feilen er loggført i `03`.

**Konsekvens for GW13-planen:** O'Reilly-inngangen forutsetter at City kontrollerer kamper. Avgangene trekker svakt i feil retning, men ikke nok til å svekke planen. Merk at Maresca ifølge FFScout foretrekker en **inverterende** back, og at Gvardiol og Dias framstår som hans faste valg — **det er den reelle risikoen mot O'Reilly, ikke troppstynningen.** Etterprøves før GW13.

## Chip-plassering

⚠️ **Omskrevet 22. august. Den forrige tabellen planla fire chips i faste vinduer. To av dem lot seg ikke planlegge, og de to vinduene kolliderte.**

**Den harde bindingen:** hele første chip-sett forfaller ved **GW19-deadline, lørdag 2. januar 14:30 norsk tid**. Ubrukt er tapt.

### Hvorfor to av fire ikke kan planlegges nå

`04` fastslår at blank- og dobbeltrunder normalt ikke bekreftes før **januar/februar**, når FA-cupomberammingene foreligger. Første chip-sett forfaller **2. januar**. Informasjonen som skulle styre timingen kommer altså i praksis etter fristen for å bruke den.

Kontrollert mot `fixtures2627.csv` 22. august: **alle 38 runder har nøyaktig 10 kamper**, 190 i hver halvsesong. Ingen blank- eller dobbeltrunde ligger i det opprinnelige programmet. De kan bare oppstå gjennom utsettelser — og det er nettopp derfor de kunngjøres sent.

**Konsekvens:** «Triple Captain på dobbeltrunde» og «Free Hit GW16–19 på blank- eller dobbeltrunde» var ikke planer. Det var betingelser uten kjent utløser. De føres nå som **utløserbaserte beslutninger**, ikke som runder i en tabell.

### Plan

| Chip | Status | Grunnlag |
|---|---|---|
| **Wildcard 1** | **Planlagt: GW16–17** | Den eneste av de fire som *kan* planlegges. Fikstursblokker er kjent hele sesongen. Restrukturering inn i Arsenals GW17–22 (1,67). Ikke GW6 — de fem sparte byttene gjør den jobben. **Kan ikke avbrytes** |
| **Bench Boost 1** | **Betinget: etter Wildcard 1.** Terskel tallfestet 3. september | Benken er £17,0m og leverte **12 poeng i GW1 og 10 i GW2** (`entry/history.csv`, kolonne `bench_points`). Målt mot rundesnittet per startende spiller — 4,5 i GW1, 7,4 i GW2 — ga benken 3,0 og 2,5, altså **67 % og 34 %**. Keeperslottet er dødvekten: 6 og 0, snitt 3 per runde for £4,5m, uten oppside utover clean sheet. **Utløser, alle tre ledd må være oppfylt:** (1) benkepoeng over 20 i minst to av de tre foregående rundene, (2) alle fire benkespillere bekreftet i startellevern for målrunden, (3) fikstursjekk mot `fixtures2627.csv` for målrunden. Ledd 1 alene er utilstrekkelig — det måler realisert avkastning bakover, mens beslutningen er framoverrettet, og kan utløses av en benk som nettopp har hatt tre gode kamper og møter topplag i målrunden. Det inntreffer ikke før wildcardet har bygget benken. **Kan avbrytes** |
| **Triple Captain 1** | **Planlagt: GW5.** Flyttet fra GW7 3. september, sent | Kandidatene er Citys svake hjemmekamper: **GW3 Coventry (H), GW5 Sunderland (H), GW7 Ipswich (H), GW16 Hull (H)** — alle FDR 2. **GW16 er blokkert av wildcardet** (én chip per runde). Avgjørende er europakalenderen, ikke fiksturet: ligafasen starter **8. september** (UEFA.com). **GW3** (lør 5. sep 14:00) ligger tre dager før Porto borte tirsdag 8. sep. **GW7** (lør 17. okt 14:00) ligger mellom MD2 13./14. okt og MD3 20./21. okt — dobbelt klem. **GW5** (søn 20. sep 13:00) har full uke uten midtukekamp foran seg og landslagspause bak seg. Kostnaden er motstanderen: Sunderland har sluppet inn 2 mål på to runder, mot Coventrys 4 og Ipswichs 6. **Utløser: spilles i GW5. Reserve GW3 hvis Haaland flagges for GW5, eller hvis en dobbeltrunde kunngjøres først.** Startoppstilling kan ikke verifiseres ved fredagsdeadline for søndagskamper; chipen **kan avbrytes**. Hard bakstopp: GW19-deadline 2. januar |
| **Free Hit 1** | **Utløserbasert** | Spilles kun hvis en blankrunde faktisk kunngjøres før GW19. Skjer ikke det, er den svakeste av de fire og er den som ofres. **Kan ikke avbrytes.** Kan ikke spilles i to påfølgende runder — legges den i GW19, er Free Hit 2 blokkert til GW21 |

**Overlappet er dermed borte.** Konflikten oppsto fordi Wildcard og Free Hit begge var tildelt spekulative vinduer rundt GW16. Kun Wildcard har et vindu nå, og «én chip per runde» er ikke lenger brutt.

### Beslutningspunkt

**Sjekk kunngjorte omberamminger ved hver månedsskifte fra november.** Kommer en blankrunde før GW19, aktiveres Free Hit. Kommer den ikke, ofres Free Hit bevisst. **Triple Captain er ikke lenger avhengig av dette — den har fått en dato (GW5) og trenger ingen kunngjøring for å fyre.** Det som ikke skal skje, er at fristen passerer mens en chip står som «venter på dobbeltrunde».

**Rekkefølge ved knapphet:** Wildcard er verdt mest og har lavest usikkerhet. Free Hit er svakest og ofres først.

### Kontrollpost: Triple Captain, etter GW4

**Når:** mandag 14. september, etter at GW4 er ferdigspilt (12.–14. september) og før GW5-deadline fredag 18. september. Fire dager margin.

**Hvorfor den finnes:** GW5-valget hviler på at europakalenderen veier tyngre enn motstanderens kvalitet. Den avveiningen ble gjort på to runders data. Sunderland hadde da sluppet inn **2 mål på to runder** — 1,00 per runde, mot Coventrys 2,00 og Ipswichs 3,00. Sunderland er altså det tetteste av de tre kandidatforsvarene, og det er den erkjente kostnaden ved GW5.

**Hva som sjekkes:** Sunderlands innslupne mål per runde etter fire runder (`fpl-data/live/gw{n}.csv`), Haalands status og minutter, og om Porto borte 8. september ga skade- eller rotasjonssignal.

**Beslutningsregel:**

| Sunderland innsluppet per runde etter GW4 | Handling |
|---|---|
| Over 1,50 | GW5 bekreftes. Kalender og motstander peker samme vei |
| 1,00–1,50 | GW5 står. Kalenderfordelen alene bærer valget — men den bærer det |
| Under 1,00 | **Stopp og sammenlign GW5 mot GW7 eksplisitt på nytt.** Ikke la GW5 stå som standardvalg fordi det allerede står i fila |

**Det som ikke lenger er tilgjengelig:** GW3 er passert når denne kontrollposten nås. Faller Sunderland-premisset, står du igjen med GW7 og dens klem mellom MD2 og MD3, eller GW13 Leeds (H) i en midtukerunde. Begge er dårligere enn det GW3 var. **Det er den reelle prisen for å vente, og den er betalt allerede når kontrollposten nås — ikke når den vurderes.**

**Merk om avbryting:** Wildcard og Free Hit låses idet byttene bekreftes. Bench Boost og Triple Captain kan trekkes fram til deadline. I GW1 landet fire av femten spilleres lagnytt på deadline-dagen, én pressekonferanse én time før. For de to første finnes ingen angremulighet etter det.
