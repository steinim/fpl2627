# Verifiseringsprotokoll

*Sist oppdatert: 21. august 2026, ettermiddag — seks nye feillogger fra deadline-døgnet, verktøybegrensninger dokumentert.*

Denne filen finnes fordi hver eneste feil under er faktisk begått i denne sesongforberedelsen. Sjekklistene er destillert av dem.

## Spillets regler er også fakta som må slås opp

**Verifisert 19. august:**

| | |
|---|---|
| Deadline GW1 | **Fredag 21. august, 18:30 BST = 19:30 norsk tid** |
| Bytter før første deadline | **Ubegrenset, gratis** |
| Priser før første deadline | **Låst.** «All prices will be locked until the Gameweek 1 deadline» — premierleague.com |
| Bindinger før deadline | £100,0m-taket, £0,0m i banken, maks 3 per klubb |
| Frikjøp fra GW1 | 1 per runde, rullerende, maks 5 banket |
| Prisendringer fra GW1 | Daglig, 00:00 britisk tid |

Dette står her fordi det ble antatt feil i fire dager. Rammebetingelsene i spillet er like mye et faktum som en pris eller en oppstilling, og skal verifiseres på samme måte. **Antagelser om regelverket har lengre halveringstid enn antagelser om spillere**, fordi ingen ny kamp motsier dem — de blir bare stående til noen sier ifra.

### Salgsprisregelen og hva den gjør med sidebytter

**Verifisert 19. august, premierleague.com og FFScout:**

| Bevegelse | Din salgspris |
|---|---|
| Spilleren **stiger** | Du beholder 50 % av gevinsten, avrundet ned til £0,1m. PLs ordlyd: *«you only get £0,1m of profit for every £0,2m that the player rises in cost»* |
| Spilleren **faller** | Du får det eksakte lavere beløpet. **Hele tapet, ingen buffer.** |

**Konsekvensen er asymmetrisk, og den rammer sidebytter mellom to like dyre spillere.** Med £0,0m i banken:

| Scenario | Salgspris | Kjøpspris | Utfall |
|---|---|---|---|
| Begge står i ro på £8,0m | 8,0 | 8,0 | Går |
| Din faller til £7,9m | 7,9 | 8,0 | **Blokkert** |
| Hans stiger til £8,1m | 8,0 | 8,1 | **Blokkert** |
| **Begge stiger £0,2m** | **8,1** | **8,2** | **Blokkert** |

Siste rad er den viktigste. To spillere som beveger seg helt likt, glir fra hverandre i dine hender, fordi du bare får halve stigningen mens du betaler hele. **Å eie den som stiger beskytter deg ikke.** Kapasiteten til sidebytter eroderer av seg selv for hver spiller du holder over tid.

**Regel:** £0,0m i banken er ikke et nøytralt valg. Det er et valg om å ikke kunne gjennomføre sidebytter etter GW1. Kostnaden for et prisfall måles ikke i prosent av lagverdien, men i om et planlagt bytte lar seg gjøre.

## VM 2026 — engangsforvrengning i åpningsrundene

VM ble spilt sommeren 2026 og sesongstarten er skjøvet en uke. Dette forsvinner rundt GW5–6, men dominerer de første rundene.

- **Finalehelgen 18.–19. juli:** England, Frankrike, Spania og Argentina. Disse spillerne fikk obligatorisk hvile og returnerte til klubbene rundt **10.–12. august** — omtrent ti dagers oppkjøring før deadline.
- **Kvartfinaletap eller tidligere:** returnerte i månedsskiftet juli/august. Vesentlig bedre forberedt.
- **Ikke i VM:** full oppkjøring. Dette er et reelt fortrinn i GW1–5 og undervurderes av markedet.

**Regel:** før du anbefaler en spiller til GW1–5, slå opp nasjonen hans og hvor langt den kom. Nasjonaliteten alene er ikke nok — sjekk om han faktisk var i troppen.

### Verifiserte utfall relevante for troppen

| Nasjon | Utfall | Klubbkonsekvens |
|---|---|---|
| Spania | Vant VM | Zubimendi og Merino sist tilbake av alle |
| England | Semifinale/finalehelg | Saka, Rice sist tilbake til Arsenal |
| Norge | Kvartfinale mot England, Haaland 7 mål | Haaland: null oppkjøringskamper |
| Portugal | Åttedelsfinale mot Spania | B.Fernandes: tre oppkjøringskamper |
| Kamerun | Kvalifiserte seg ikke | Mbeumo: full oppkjøring |
| Ungarn | Kvalifiserte seg ikke | Szoboszlai: lengste ferie i karrieren |
| Brasil | Deltok, men **João Pedro ikke uttatt** | Full sommer og full oppkjøring |

**Utvidelse av regelen:** det holder ikke å sjekke om nasjonen deltok. João Pedro er brasiliansk og ble ikke uttatt i det hele tatt. Sjekk troppslisten, ikke nasjonaliteten.

## Faste sjekker før hvert bytte

0. **Hva koster byttet i bytter?** Før første deadline: null. Fra GW1: ett frikjøp. Ikke anvend in-season-økonomi på førsesongen.
1. Er spilleren tilgjengelig? VM-status, skade, karantene.
2. Har han spilt oppkjøringsminutter, og når?
3. **Startet han generalprøven — og hvorfor?** Se avsnittet under.
4. Hva sier kampprogrammet de neste fem rundene? Slå opp i `fixtures-2627.csv`.
5. Hva blir klubbfordelingen etter byttet? Maks 3 per klubb.
6. Hvor mange millioner av keeper- og forsvarsbudsjettet ligger på topplag etter byttet? Går tallet ned uten at det er bestemt, stopp.
7. **Hva står igjen i banken etterpå, og hvilke planlagte sidebytter blokkeres av det?** Se salgsprisregelen.

## Generalprøven er det sterkeste signalet — men les årsaken

Den siste oppkjøringskampen før seriestart er der trenere stiller opp med det de faktisk planlegger å bruke.

**Hierarki for oppstillingsbevis, sterkest først:**

1. **Community Shield 16. august** — konkurransekamp om et trofé. Gjelder kun Arsenal og Man City, men rangerer over alt annet for de to.
2. Generalprøven (siste oppkjøringskamp før seriestart)
3. Nest siste kamp, hvis generalprøven mangler
4. Trenerens uttalte planer i pressekonferanse
5. Prediksjonsartikler og projeksjoner fra tredjepart

**Årsaksregelen — gjelder begge veier.** En oppstilling er bare bevis hvis du vet hvorfor den ser slik ut.

- **Benket ≠ degradert.** En sen VM-returnerende som benkes bygger minutter. Se hvem som kom inn for ham.
- **Startet ≠ etablert.** En spiller som starter fordi erstatteren signerte for tre dager siden, holder drakten — han eier den ikke. Sjekk signeringsdatoene til konkurrentene før du leser en start som bekreftelse.
- **Regelen gjelder begge spillerne i et bytte.** Hvis du sjekker årsaken for den du vurderer å selge, må du sjekke den for den du vurderer å kjøpe. Mbeumo-feilen 19. august oppsto fordi årsaken ble undersøkt for Egan og ikke for Cunha.

**Underregel, ny 19. august: les referatets forklaring, ikke bare oppstillingen.**
Oppstillingen er nivå 2-bevis. Men når oppstillingen hentes fra et kampreferat, står forklaringen på oppstillingen som regel i samme tekst — hvem som trengte minutter, hvem som gjorde sin første start, hvem som nettopp var syk. **Å plukke XI-en ut av et referat og ignorere avsnittet under den, er å velge bort det sterkeste tilgjengelige årsaksbeviset.** Dette skjedde med Milan-kampen 15. august.

**Underregel, ny 19. august: hedget ordlyd i sekundærkilde er ikke et åpent punkt.**
Når en sekundærkilde skriver at noe *kan* skje, er det ikke et bevis for usikkerhet — det er fravær av bevis. Slå opp primærkilden før du fører det som åpen risiko. Vicario-punktet sto som «betinget, ikke bekreftet» i `01` i to døgn på grunnlag av ordet *could* i en Scout-artikkel, mens Dúbravka var signert som Kinskys toer i juni og Vicario var på vei til Juventus.

## Kildehierarki

1. Klubbens egen nettside for kamper og signeringer
2. `fixtures-2627.csv` i prosjektet — validert mot åtte uavhengige ankere, **men kun på rundenivå**, ikke kampdato
3. Premier Leagues egne sider for regler og priser
4. Fantasy Football Hub eller tilsvarende for projeksjoner — bra på tilgjengelighet, ikke bruk dem som fasit på sesonglang verdi
5. Sekundærkilder som FFScout og RotoWire — gode på analyse, men gjenta aldri en fikstursvurdering derfra uten å se kampene selv

**Regel ved konflikt mellom projeksjon og oppstilling:** oppstillingen vinner. En projeksjon er en gjetning skrevet før kampen; en oppstilling er trenerens observerte valg.

| Tilfelle | Projeksjonen sa | Oppstillingen viste | Vi fulgte |
|---|---|---|---|
| Slater, 13.–15. aug | Scout: startplassen er «diskutabel» | Startet i pivot mot Nice 15. aug | Oppstillingen |
| Mbeumo, 15.–17. aug | Scout: ventes å spille spiss, bedre valg enn Cunha | Cunha startet på nieren mot Milan 15. aug, Mbeumo inn for ham | Oppstillingen — punktet står åpent |
| Egan, 15.–19. aug | Clarke: ikke i Hulls XI | Startet mot Nice 15. aug | **Ingen av dem — årsaksregelen avgjorde.** Mendy signerte 12. aug og satt på benken. |

**Merk om premierleague.com:** nettstedet motsier seg selv. 17. august skrev Scout at Mbeumo ventes å spille spiss i Seskos fravær; samme dag førte Adrian Clarke Sesko i Uniteds XI. Samme artikkel fører Saliba og Timber i Arsenals XI og skriver i notatet under at begge er skadet. **Clarkes XI-artikkel er en fullt-skadefri-projeksjon merket som GW1-verktøy.** Behandle den som nivå 5, og bare på signeringer og roller.

**Scout Selection er en eierandelsprediktor, ikke en anbefaling.** Alt som står der blir høyt eid. Å avvike er ikke gratis, men å konvergere koster hele separasjonskilden. Se `01`.

## Verifisert 19. august: BPS-endringene 2026/27

Tesen i `02` var delvis feil og ble etterprøvd mot fire uavhengige kilder.

| Endring | Innhold | Konsekvens |
|---|---|---|
| CBI | 1 BPS per **tre**, mot 1 per to | Rammer stillestående midtstoppere |
| Takler og ballerobringer | **Urørt** | Holdende midtbanespillere rammes lite |
| Å bli taklet | **−1-straffen fjernet** | Ballbærere og offensive backer vinner |
| Keeperredning | **+2 BPS**, +1 for skudd i boksen | Favoriserer travle keepere, ikke toppklubbkeepere |
| Keeper, ny kategori | **+1 for big chance-redning** | Samme retning |
| DefCon | **Uendret** (10 CBIT / 12 CBIRT → 2 poeng) | Der forsvarsverdien fortsatt ligger |

**Størrelsesorden:** BPS avgjør kun bonus, maks 3 poeng per kamp, i konkurranse. En midtstopper taper anslagsvis 5–10 bonuspoeng over en sesong. **Tesen er nedgradert fra «viktigste enkeltendring» til andreordens rebalansering.**

## Feillogg

⚠️ **Seks nye oppføringer 20.–21. august. Alle er begått av Claude i løpet av det siste døgnet før GW1-deadline.**

| Feil | Hva skjedde | Regelen som fulgte |
|---|---|---|
| **Protokollen brukt som optimeringsverktøy** | Gjennom hele deadline-dagen ble hvert forslag testet mot «velter ny informasjon den gamle konklusjonen?» — aldri mot «hva ville jeg valgt hvis jeg bygget troppen i dag?». Denne filen er bygget for å hindre *feil*. Ingen regel i den tester *allokering*. En tropp kan passere hele protokollen og likevel være middelmådig. Brukeren måtte spørre «hvorfor vil du ikke vurdere endringer?» før gjennomgangen ble gjort. | **Fravær av feil er ikke bekreftelse.** Før hver deadline: still spørsmålet «hvis troppen var tom, ville jeg valgt denne spilleren til denne prisen?» for hvert slott — separat fra spørsmålet om noe har endret seg. |
| **Gulvpris forvekslet med handlingsrom** | Dúbravka-slottet ble avvist to ganger med «£4,0m er gulvet for keepere, ingen handling mulig». Gulvprisen er irrelevant. Spørsmålet var om £0,5m kjøpte en toer som **spiller** — og det gjorde den (Verbruggen £4,5m, 37 av 37 kamper). Rotårsak: `01`s beslutning fra 19. august om å beholde Dúbravka ble lest som at slottet var avgjort. Den beslutningen avviste et *dårlig argument mot* Dúbravka; den svarte aldri på om slottet var godt brukt. | **En trukket anbefaling lukker ikke slottet.** Skill mellom «argumentet mot var galt» og «valget er riktig». Og enumerér alltid hva et beløp faktisk kjøper — ikke hva som er billigst i klassen. |
| **Forhåndsomtale lest som skadeliste — tredje gang samme mønster på to døgn** | Brit Briefs artikkel var en *forhåndsomtale av hva Maresca kom til å bli spurt om*: «Maresca will provide injury updates on the likes of Doku and Nunes… Marmoush also picked up a knock». Det ble gjengitt som en skadeliste med seks poster og formuleringen «systematisk demontert». Marescas faktiske ord samme ettermiddag: **kun Doku ute, 2–3 uker, Nunes tilbake, Marmoush ikke nevnt.** | **Se de tre oppføringene over og under denne.** Šeško (Yahoo/AOL), Mbeumo-posisjonen (Yahoo) og City-skadene (Brit Brief) er samme feil tre ganger på under 48 timer: **en sekundærkildes parafrase, forhåndsomtale eller projeksjon gjengitt som primærkildens ord.** Mønsteret er nå navngitt som egen regel — se under. |
| **Inflatert premiss drev en avvisning** | Gibbs-White → Semenyo ble avvist med «å øke City-eksponeringen motsier min egen City-analyse». Den analysen var den inflaterte skadelisten over. Konklusjonen holdt — £0,5m for 0,20 i fikstursforskjell er en dårlig handel — men begrunnelsen var sirkulær: en feil jeg selv hadde laget, ble brukt som argument. | **Fjerde gang samme mønster: riktig konklusjon, gal begrunnelse.** Når en avvisning hviler på en analyse fra samme økt, kryssjekk analysen før du bruker den som premiss. |
| **Manglende oppkjøringsminutter lest som fravær fra planene** | Det ble hevdet i to svar at «Spurs' bakre firer ikke finnes» fordi Porro, Udogie og van de Ven ikke hadde spilt i sommer. De Zerbi utpekte samme dag fem lagkapteiner, og **van de Ven og Porro var to av dem.** | **Fravær fra oppkjøringen er ikke fravær fra planene**, særlig for sene VM-returnerende. Det er samme feiltype som VM-flagget på Groß: et *filter* brukt som en *dom*. |
| **Sekundærkilde oppgraderte hedget primæruttalelse** | Det ble rapportert at «Carrick har bekreftet at Šeško er tilgjengelig for uttak». Carricks faktiske ord: «*Ben is back training… looking forward to getting him some minutes.*» Yahoo og AOL skrev «set to be available for selection, Carrick has confirmed», og oppgraderingen ble gjentatt som faktum. | **Speilbildet av Vicario-feilen.** Der ble et *could* lest som usikkerhet; her ble «back training» lest som bekreftelse. Samme rotårsak: primærkilden ble ikke lest. **Les alltid trenerens egne ord før du gjengir en sekundærkildes sammendrag av dem.** |
| **Gruppeuttalelse lest som navngitt klarering** | Glasners «Yates og Savona blir ikke i troppen, vi har 23 spillefør spillere» ble rapportert som «en eksplisitt klarering av både N.Williams og Gibbs-White». Ingen av de to ble nevnt. Glasner sa dessuten «*I will make my decisions tomorrow*». | **Tilgjengelighet er ikke uttak, og fravær fra en skadeliste er ikke nærvær i en ellever.** Kravet om positivt signal krever et navn. |
| **Aggregator prioritert foran klubbside** | Kl. 15:24 ble det meldt at «ingenting fra dagens pressekonferanser er publisert». Arsenal.com hadde da lagt ut fullt referat fra Artetas pressekonferanse. Det ble søkt på FFScouts liveblogg og generiske nyhetssøk, men ikke gått til klubbens egen nettside — **nivå 1 i kildehierarkiet**. | **Gå klubb for klubb til primærkilden før du melder at noe ikke finnes.** «Jeg fant det ikke» er ikke «det er ikke publisert». |
| **Mbeumo-posisjonen revidert fire ganger på tre dager** | Framstillingen gikk fra «bekreftet spiss» til «uavklart» til «Cunha på nieren» til «uavklart» mellom 19. og 20. august, uten at noen beslutning endret seg. | **Når et spørsmål ikke lar seg besvare fra tilgjengelig bevis, skal det avklares som irrelevant — ikke besvares på nytt hver runde.** Spørsmålet som betydde noe var «starter han», og svaret var ja hele veien. |


### Regel, ny 21. august: skill parafrase fra sitat

Tre feil på under 48 timer hadde identisk rotårsak. Alle tre kom av at en sekundærkilde beskrev hva en primærkilde hadde sagt eller kom til å si, og beskrivelsen ble gjengitt som primærkildens ord.

| Sak | Sekundærkilden skrev | Primærkilden sa faktisk |
|---|---|---|
| Šeško | «set to be available for selection, Carrick has confirmed» | «*Ben is back training… getting him some minutes*» |
| Citys skader | «Maresca **will provide** injury updates on the likes of Doku and Nunes» | «kun Doku ute, 2–3 uker, Nunes tilbake» |
| Mbeumos posisjon | «Cunha deputises centrally, **meaning** Mbeumo moves out to the right» | Carrick ble ikke spurt og sa ingenting |

**Regelen:** før en påstand om hva en trener har sagt føres inn i en fil eller en anbefaling, skal den finnes som **sitat**, ikke som referat. Merk særlig futurum — «*will provide*», «*is set to*», «*is expected to*» — som er varsel om et spørsmål, ikke svar på det.

**Praktisk konsekvens:** klubbens egen nettside og BBCs liveblogg gjengir ordrett. Aggregatorer gjør det ikke. Gå til de to første.

### Verktøybegrensninger — verifisert 20.–21. august

| Verktøy | Begrensning |
|---|---|
| `web_fetch` mot FFScouts liveblogg | Serverte **hurtiglagret versjon** som sto på «Coming soon…» mens søkeindeksen viste oppdatert innhold to timer gammelt. Innholdet måtte hentes via søkefragmenter |
| `web_fetch` mot `bbc.com` | **Blokkert** (SITE_BLOCKED). `feeds.bbci.co.uk` fungerer, men URL-en må først komme fra et søkeresultat |
| BBCs liveblogg | Paginert. Én henting gir **én av sju sider**, nyeste først. En pressekonferanse fra kl. 13:00 ligger seks sider bakover |
| `web_fetch` generelt | Avviser URL-er som ikke har stått i et tidligere søke- eller hentingsresultat, selv om de sto som lenke i en hentet side |

**Konsekvens:** når brukeren limer inn et transkript, er det som regel raskere og mer pålitelig enn noe Claude kan hente selv. Be om det tidlig i stedet for å bruke ti søk på å rekonstruere det.

### Tidligere feillogg

| Feil | Hva skjedde | Regelen som fulgte |
|---|---|---|
| **Årsaksregelen anvendt på én side av byttet** | Generalprøven mot Milan ble lest som bevis mot Mbeumo: Cunha startet på nieren, Mbeumo kom inn for ham. Årsaken sto i samme referat — Mbeumo hadde startet to ganger den uken, Cunha gjorde sin første oppkjøringsstart etter fem VM-kamper og sykdom. Byttet ville erstattet full oppkjøring med sen VM-returnerende, i strid med VM-regelen over. | **Sjekk årsaken for begge spillerne i et bytte, ikke bare den du eier.** Og les referatets forklaring, ikke bare XI-en i det. |
| **Hedget sekundærkilde ført som åpen risiko** | `01` førte Dúbravkas toerrolle som «betinget, ikke bekreftet» fordi Scout skrev at Vicarios avgang *kunne* gi ham plassen. Vicario var utlånt til Juventus, og Dúbravka var signert i juni eksplisitt som Kinskys reserve. Det ble anbefalt et unødvendig bytte på dette grunnlaget. | **Slå opp primærkilden før et *could* føres som usikkerhet.** Fravær av bevis er ikke bevis på usikkerhet. |
| **Fikstursargument i strid med egen tabell** | `01` begrunnet Egan → Diop delvis med «Ipswich har tre realistiske clean sheet-kamper, Hull har én». `02` gir begge 2,46 i GW1–5. Konklusjonen var riktig; det ene av to argumenter for den var det ikke. | **Kryssjekk fikstursutsagn mot vanskelighetstabellen i `02` før de skrives.** Tredje gang samme mønster: riktig konklusjon, feil begrunnelse. |
| **BPS-tesen overvektet i fire dager** | `02` kalte BPS-omskrivingen «den viktigste enkeltendringen for laguttak» og hevdet at den rammer holdende midtbanespillere. Endringen treffer kun C, B og I — ikke takler, ikke ballerobringer. Den fjernede taklet-straffen sto ikke i filen i det hele tatt. Overvektingen drev en bekymring for forsvarsstrukturen som ikke var berettiget, og skrev inn et keeperbytte i GW16 som peker motsatt vei av mekanikken. | **En tese som styrer laguttak skal verifiseres mot primærkilden med samme grundighet som en pris.** Se regelen om spillets regler øverst i filen — den gjelder også regelendringer man selv har tolket. |
| **Ubegrensede bytter oversett** | Hele førsesongen ble rådgitt som om troppen kostet ett frikjøp per endring. Konkret utslag: Egan-byttet ble rangert *under* Mbeumo-byttet «fordi du bare har ett frikjøp», og forsvarssvakheten ble utsatt til GW16-wildcardet. Ingen av delene er sanne før 21. august 19:30. Brukeren måtte selv korrigere. | **Slå opp spillets regler før du anvender dem.** Punkt 0 i sjekklisten. En feil om rammebetingelsene forplanter seg til hver eneste anbefaling og blir aldri motsagt av en kamp — den blir bare stående. |
| **Dokumentrettelse utsatt** | Da feilen var kjent, ble det foreslått å vente med å oppdatere `01` «for å slippe å skrive den om to ganger». `01` inneholdt da en konklusjon som var kjent gal. | **En kjent feil i kontekstfilene rettes samme time den oppdages.** Churn er billigere enn en gal fil som blir lest som fasit i neste runde. |
| **£0,1m avfeid som ubetydelig** | Prisfallsrisiko på en £4,0m-spiller ble avvist med «£0,1m av £100,0m». Feil målestokk. Med £0,0m i banken avgjør £0,1m om et sidebytte i det hele tatt lar seg gjennomføre — Mbeumo↔Cunha til £8,0m er blokkert av enhver ugunstig bevegelse på £0,1m. Brukeren måtte korrigere. | **Mål prisrisiko i blokkerte bytter, ikke i prosent av lagverdi.** Konklusjonen (Egan → Diop) var riktig, men begrunnelsen var gal — samme feiltype som Diop-oppføringen lenger ned. |
| **Egan lest som bekreftet** | Han startet generalprøven mot Nice 15. august, og det ble lest som at han har plassen. Mendy — klubbrekord £21m, 11,37 DefCon per 90 i La Liga, samme side av midtstopperparet — hadde signert 12. august og satt på benken. | Årsaksregelen. Sjekk signeringsdatoene til konkurrentene før du leser en start som bekreftelse. |
| Coventry-forsvarere anbefalt | Valgt på at de var sikre startere, uten å se kampprogrammet. Coventry har ligaens dårligste åpning. | Sjekk alltid kampene, ikke bare spilleren. |
| Igor Jesus kjøpt | Valgt på fire treningskampmål mot League Two- og Championship-motstand. Faktisk fasit: 2 ligamål på 23 kamper, 18 % skudd på mål. | Treningskampmål er aldri bevis. Slå opp ligastatistikken. |
| Rice kjøpt | Valgt på 35 starter forrige sesong. Overså at han var sen VM-returnerende med skadehistorikk og null oppkjøring. | Startfrekvens i fjor sier ingenting om tilgjengelighet nå. |
| «United hardner etter GW8» | Gjentatt fra en sekundærkilde. Den faktiske listen viser vekslende program uten sammenhengende dårlig periode. | Ikke gjenta fikstursvurderinger uten å se listen. |
| Forsvaret uthulet gradvis | Fire enkeltbytter, hvert forsvarlig isolert, flyttet topplagseksponeringen fra £13,5m til £5,5m uten at noen bestemte det. | Anti-drift-sjekken i punkt 6 over. |
| Guimarães kalt uthvilt | Antatt fordi Brasil ikke nådde finalehelgen. Han startet alle fem VM-kampene. | Sjekk kamper spilt, ikke bare hvor langt laget kom. |
| Opplastet fikstur-CSV | En CSV med korrekt kalenderstruktur, men fabrikkerte kamper. Null av ti GW1-kamper stemte. | Kryssjekk alltid nye datasett mot minst tre kjente ankere før bruk. |
| Calafiori flagget gult | Han satt på benken mot Como 12. august, og det ble lest som skadesignal. | Én benking i nest siste oppkjøringskamp er rotasjon, ikke signal. Vent på generalprøven. |
| Trenerlisten ufullstendig | `02` listet fem trenerbytter. Ipswich, Chelsea og Bournemouth manglet. | Gå gjennom alle 20 klubber systematisk. |
| Trafford ført som Man City-keeper | Prislisten i `01` hadde ham som MCI £5,0m. Han gikk til Leeds for rundt £40m og er førstekeeper. Prisen var riktig, klubben var feil. | Klubbtilhørighet i prislisten må verifiseres like nøye som prisen. |
| CSV lest som kampdatoer | Alle GW1-kamper står 21. august i datasettet. Faktiske avspark: 21.–23. august. | CSV-en er på rundenivå. Ikke bruk den til chip-timing. |
| Diop-avvisningen ble stående på feil grunnlag | Avvist på «uavklart startplass». Han startet som midtstopper i begge Ipswich' siste oppkjøringskamper. | Oppdater begrunnelsen når faktagrunnlaget endrer seg, selv når konklusjonen holder. En riktig konklusjon med feil begrunnelse smitter over på neste beslutning. |
| Feil Sangare slått opp | Claude søkte opp Ibrahim Sangaré i Forest. Det var Mamadou Sangare, Brentford, £5,5m. | Etternavn er ikke identifikasjon. Verifiser fornavn, pris *og* klubb. |
| Formasjonen antatt, ikke telt | Claude antok 3-4-3 og kalte Scout-elleveren umulig. Laget går opp i 3-5-2. | Tell posisjonene i troppen før du hevder at en oppstilling ikke går opp. |
| VM-flagget trukket for langt på Groß | Presentert som at han «bryter VM-regelen». Han hadde oppkjøringsminutter og hadde overtatt Brightons straffer. | VM-status er et *filter*, ikke en dom. |

## Hva oppkjøringen kan og ikke kan brukes til

**Kan:** hvem som spiller, hvor mange minutter, i hvilken posisjon, hvem som er tilbake fra skade eller VM, hvem som tar corner og frispark, hvilken formasjon en ny manager bruker.

**Kan ikke:** vurdere form. Motstandsnivået spenner fra League Two til Barcelona, laguttakene er treningsdoser, og flere klubber kjører to lag samtidig.

**Splittet tropp er et signal:** klubber som legger to kamper på samme dag har to treningsgrupper. Eksempler denne sommeren: Spurs (Hoffenheim 15. og 16. august), Liverpool (Como to ganger 16. august), Ipswich (Oxford og Wycombe samme dag 1. august).

## Status per 21. august — GW1-deadline 19:30

**Alle punkter merket «må avgjøres før fredag» er nå enten gjennomført eller falt bort.**

| Punkt | Utfall |
|---|---|
| Full gjennomgang av troppen | **Gjennomført to ganger.** 19. august (fire endringer) og 21. august (enumerering av £0,5m, se `01`) |
| Bank | **£0,0m.** Brukt på Dúbravka → Verbruggen. Salgsprisregelen gjelder nå fullt ut: sidebytter er blokkert fra GW1 |
| Toerkeeperslottet | **Løst 21. august.** Dúbravka £4,0m → Verbruggen £4,5m. Bench Boost avblokkert |
| Keeper i GW1-XI | **Verbruggen.** Se `01` |
| Forsvarsstrukturen | Lukket som bevisst valg. £14,5m av £32,0m = 45,3 % |
| Mbeumos posisjon | **Avklart som irrelevant**, ikke lukket. Se `01` |
| Torsdagens pressekonferanser | Gjennomgått. Ingen endret en beslutning; tre endret en begrunnelse (Timber, Calafiori, Šeško) |
| Fredagens pressekonferanser | ⚠️ **Ikke lest.** O'Neil, De Zerbi og Maresca gikk 13:30 UK; ingen referater hadde landet da denne filen ble skrevet. Gjelder Davis, Diop, Kinsky og **Haaland** |

### Åpne punkter etter deadline

| Punkt | Frist | Hva som avgjør det |
|---|---|---|
| **Tzolis' plass** | GW1–3 | Arsenal spilte 21:00 norsk, tre timer etter deadline. Slottet ble låst blindt. Gakpo £7,0m er førstevalget hvis han ryker |
| **Calafiori/Hincapié** | GW1–3 | Artetas parformulering 20. august. Ett gult flagg, ingen handling |
| **Šeško tar nieren?** | GW3–5 | Avgjør om Mbeumo er permanent kantspiller. Ikke et salgssignal i seg selv |
| **Citys tilførsel** | Løpende | Seks avganger/skader på fjorten dager. Berører Haaland direkte og GW13-planen for O'Reilly |
| Slaters og Davis' plass | 1. september 23:00 BST | Vinduet stenger **etter** GW2-deadline. Opprykkslagene bygger fortsatt tropp |
| **Hvor gikk Konsa?** | 1. september | **Emery bekreftet 21. august at Konsa har forlatt Villa.** Arteta sa 20. august at Arsenal fortsatt søker en forsvarer og har ikke annonsert noe. **Destinasjonen er ukjent.** Punktet er omformulert, ikke lukket |
| Full gjennomgang av prislisten | Etter 1. september | Trafford-feilen viser at klubbkolonnen drifter under vinduet. **Meslier (ARS) og Cherki (MCI) mangler** |
| BPS-tesen — holder den? | Etter GW5 | Mekanikken er verifisert. Det som gjenstår er faktisk bonusfordeling. Avgjør GW16-keepervalget, som nå gjelder Verbruggen/Kinsky → Raya |
| **Manglende rader i `02`s vanskelighetstabell** | Før GW6 | Brighton, Brentford, Aston Villa, Sunderland, Newcastle, Coventry, Everton, Fulham, Palace og Bournemouth mangler. **Verbruggen ble kjøpt uten et beregnet fikstursstall for Brighton.** Roefs og Thiaw ble ført som «uvurdert», ikke avvist, av samme grunn |

⚠️ **Den siste raden er den viktigste.** `02`-tabellen dekker ti av tjue klubber, og halve troppens beslutningsgrunnlag hviler på tall som ikke finnes for motparten. Beregn de ti resterende fra `fixtures2627.csv` før GW6, med samme metode som de eksisterende.

## Referanseoppstillinger

**Community Shield 16. august, Principality Stadium, Arsenal 3–0 Man City.**
Arsenal (4-3-3): Raya; White, Mosquera, Gabriel, Calafiori; Ødegaard, Guimarães, Lewis-Skelly; Madueke, Havertz, Tzolis.
Man City (4-3-3): Donnarumma; Khusanov, Dias, Gvardiol, O'Reilly; Kovacic, E.Anderson, Semenyo; Foden, Haaland, Doku.

**Hull City v Nice, 15. august, MKM Stadium, 0–0.**
Hull (4-2-3-1): Tzolakis; Giles, Egan, Ajayi, Coyle; Crooks, Slater; Stroud, Dahl, Belloumi; McBurnie.
Benk inkluderte Mendy, Herrington, McNair, Targett, Dowell, McCarthy.

**Coventry v Monaco, 15. august.**
Coventry XI: Rushworth, van Ewijk, Thomas, Amenda, Dasilva, Onyeka, Grimes, Yirenkyi, Tchaouna, Simms, Thomas-Asante. Lampard gjorde bare to bytter — førstelagspreg.
