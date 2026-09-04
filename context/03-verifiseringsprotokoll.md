# Verifiseringsprotokoll

*Sist oppdatert: 3. september 2026 — ny feillogg: komprimert minnesammendrag brukt som kilde på troppssammensetning og anti-drift-tall. Tredje forekomst av samme feiltype. Snapshot-repoet `steinim/fpl-data` ført inn i kildehierarkiet som nivå 0 for egen tropp, og verktøybegrensningene oppdatert etter at 403-blokkeringen mot FPL-APIet ble omgått.*
*Forrige: 28. august 2026, sent — ny feillogg: en benkerekkefølge-reversering ble selv reversert. Overstyringsklausulen i Regel 7 ble anvendt bokstavelig på det navngitte flagget uten å sjekke om auto-sub-mekanismen fortsatt talte for konklusjonen uavhengig av flagget. Den gjorde det.*
*Forrige: 28. august 2026, kveld — ny feillogg: en Claude-økt hevdet en GW2-deadline-feil i `02` som ikke fantes, forårsaket av at et minnesammendrag hadde slettet skillet mellom BST og norsk tid. Samme feiltype som 27. august, nå utvidet til å gjelde minnesammendrag mot kildefil.*
*Forrige: 28. august 2026 — Gibbs-White-skadeflagget verifisert lukket (offisiell presser slo appens prosentflagg), ny feillogg om filredigering på tvers av chatter uten fersk synk-sjekk.*
*Forrige: 27. august 2026, verifiseringsrunde — to nye feillogger fra en full gjennomgang av alle seks filer før commit: anti-drift-tallet i `01` ikke oppdatert etter en prisendring nevnt i samme fil, og britisk/norsk tidssone blandet i et klokkeslettavsnitt.*
*Forrige: 27. august 2026 — ny feillogg: firukersregelen brutt på egen kontrollert kilde (Gordon/Newcastle), Chelseas europastatus lukket som historisk unntak fra firukersregelen.*
*Forrige: 25. august 2026, kveld — aggregatregelen presisert mot faktiske tall etter låsing, femte feillogg (kilde forkastet i sin helhet).*
*Forrige: 25. august 2026 — GW1-oppgjør. Ny regel om aggregatfelt i API-et, fire nye feillogger, GW1-referanseoppstillinger, keeper-BPS-datapunkt, ny verktøybegrensning.*
*Forrige: 22. august 2026, kveld — filnavnfeilloggen fra tidligere samme dag korrigert (prosjektfilen viste seg å mangle bindestrek likevel), fixtures2627.csv-referanser rettet i alle filer.*
*Forrige: 22. august 2026 — `05` innført som nivå 0, sjekkpunkt 9, keeper-BPS rettet med før/etter, tre nye feillogger.*
*Forrige: 22. august 2026, GW1-oppgjør — ARS–COV-oppstilling ført inn, to åpne punkter avgjort, feillogg om startplass utledet av poengsum.*
*Forrige: 22. august 2026 — to nye feillogger (tapt innhold i omskriving, filnavn lest fra opplastet kopi), Meslier lukket, filnavnsreferanse rettet.*
*Forrige: 21. august 2026, kveld — Bench Boost-feilen rettet (bench-mekanikk forvekslet med kampdeltakelse), ny regel om kildealder, Konsa-punktet lukket, seks nye feillogger fra deadline-døgnet, verktøybegrensninger dokumentert.*

Denne filen finnes fordi hver eneste feil under er faktisk begått i denne sesongforberedelsen. Sjekklistene er destillert av dem.

## Ny regel, 25. august: skill spillerdata fra aggregatdata i FPL-API-et

**Elementnivået i API-et er pålitelig under runden. Aggregatfeltene i `events` er det ikke.**

Verifisert 25. august: `bootstrap-static` ga samtidig **korrekte** poengsummer per spiller (Calafiori 9, Tzolis 6, Raya 6, White 11 — alle bekreftet mot faktisk lagpoengsum) og **gale** rundetall: `average_entry_score: 36` mot faktisk **48**, `highest_score: 114` mot faktisk **131**. Samme svar, samme henting.

**Det utelukker at svaret var hurtiglagret** — da ville spillerdataene vært like gale. Feilen ligger i feltet, ikke i hentingen. Aggregatene skrives tilsynelatende først når `data_checked` blir `true`; fram til da står en delverdi der uten at noe markerer den som ufullstendig.

**Presisert 25. august etter låsing.** Da `data_checked` snudde til `true`, ble hvert felt sammenlignet mot verdien før låsing. Bare tre av dem hadde flyttet seg:

| Felt | Før låsing | Etter låsing | Dom |
|---|---|---|---|
| `average_entry_score` | 36 | **50** | **Ubrukelig før låsing** |
| `highest_score` | 114 | **131** | **Ubrukelig før låsing** |
| `highest_scoring_entry` | 331434 | 120245 | **Ubrukelig før låsing** |
| `ranked_count` | 8 904 519 | 8 903 411 | Brukbar |
| `chip_plays` | 814 606 / 250 816 | identisk | Brukbar |
| `most_selected` · `most_captained` · `top_element` | 411 · 411 · 115 | identisk | Brukbar |

**Regelen, endelig:** de tre **poengaggregatene** — rundesnitt, høyeste lag og hvilken entry som eier det — er verdiløse før `data_checked: true`. Resten av `events`-blokken er brukbar. `elements`-blokken og `fixtures`-endepunktet er gyldige straks kampen er ferdigspilt.

**Appen er heller ikke fasit før låsing.** Appen viste snitt **48** kl. 08:45, altså femten minutter før låsing. Fasit ble **50**. Både API-et og appen bommet, i hver sin retning. Ingen kilde er pålitelig på rundesnitt før 09:00 britisk tid dagen etter siste kamp.

**Generalisering:** at ett felt i en kilde er verifisert riktig, sier ingenting om nabofeltet. Nivå på kilde gjelder per felt, ikke per endepunkt. **Men det gjelder også motsatt vei:** at ett felt er galt, gjør ikke hele blokken gal. Første utkast til denne regelen satte åtte felter i karantene. Sju av dem var riktige.

## Ny regel, 21. august: kilder eldre enn fire uker brukes ikke

**Grense: artikler, pressekonferanser og oppstillinger publisert før ca. 24. juli 2026 er utenfor.** Gjelder nyheter, lagnytt, projeksjoner og prisdata — ikke historisk sesongstatistikk (CBIT-tall, målprosent, fjorårets minuttall) brukt som referansegrunnlag, som per natur er eldre.

**Hvorfor regelen kom:** si.com-artikkelen brukt i Szoboszlai-vurderingen viste seg å omtale Arne Slot som Liverpool-manager. Det er feil sesong — Iraola er bekreftet manager for 2026/27. Artikkelen datostemplet «8-25-25» var fra august **2025**, ett år gammel, og ville vært luket ut av firukersregelen alene, uavhengig av at feil manager også avslørte den.

**Praktisk konsekvens:** sjekk publiseringsdato **før** innholdet brukes, ikke bare når noe virker inkonsistent. Dette er en skjerpelse av kildehierarkiet under, ikke en erstatning for det.

⚠️ **Gjentatt 27. august, med signalet observert og ignorert denne gangen** — se feilloggen. Regelen tåler ikke å bli anvendt delvis: å oppdage at en kilde er fra feil periode og likevel bruke én annen detalj fra den er samme feil som å aldri sjekke datoen i utgangspunktet.

**Unntak, presisert 27. august:** strukturelle, fastlåste fakta som avgjøres én gang per sesong (europeisk kvalifisering, sluttabell, opprykk/nedrykk) faller **ikke** inn under firukersregelen selv om kildene er eldre enn fire uker — de endrer seg ikke slik lagnytt, skader og priser gjør. Samme unntakskategori som «historisk sesongstatistikk» over. Brukt til å lukke Chelseas europastatus i `01` med kilder fra mai 2026.

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
4. Hva sier kampprogrammet de neste fem rundene? Slå opp i `fixtures2627.csv`.
5. Hva blir klubbfordelingen etter byttet? Maks 3 per klubb.
6. Hvor mange millioner av keeper- og forsvarsbudsjettet ligger på topplag etter byttet? Går tallet ned uten at det er bestemt, stopp.
7. **Hva står igjen i banken etterpå, og hvilke planlagte sidebytter blokkeres av det?** Se salgsprisregelen.
8. **Er hver kilde brukt yngre enn fire uker?** Se regelen øverst i filen.
9. **Er poengregelen slått opp i `05`, eller husket?** Ingen påstand om hvordan en poengsum er satt sammen, og ingen påstand om hva en regel sier, uten at den er lest i `05-spillets-regler.md`. Står den ikke der, skal det sies at den ikke står der.

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

0. **`05-spillets-regler.md` for alt som gjelder spillets regler.** Bygget på FPLs egen regelside (Help → Rules), lastet ned 22. august 2026. Den slår enhver artikkel, også premierleague.coms egne nyhetssaker, fordi den er regelverket og ikke en omtale av det.
1. Klubbens egen nettside for kamper og signeringer
2. `fixtures2627.csv` i prosjektet — validert mot åtte uavhengige ankere, **men kun på rundenivå**, ikke kampdato
3. Premier Leagues egne sider for regler og priser
4. Fantasy Football Hub eller tilsvarende for projeksjoner — bra på tilgjengelighet, ikke bruk dem som fasit på sesonglang verdi
5. Sekundærkilder som FFScout og RotoWire — gode på analyse, men gjenta aldri en fikstursvurdering derfra uten å se kampene selv

### Snapshot-repoet — ført inn 3. september 2026

`github.com/steinim/fpl-data` speiler FPL-APIet på timeplan og er tilgjengelig fra `bash_tool` via `raw.githubusercontent.com`. **Innholdet er APIets egne felt, ikke en omtale av dem** — for din egen tropp, egne poeng og egen plassering rangerer det på **nivå 0**, på linje med `05`. For spillerdata gjelder fortsatt skillet i «Ny regel, 25. august»: spillerfelt er fasit etter låsing, aggregatfelt er det ikke.

| Sti under `data/` | Innhold | Rangering |
|---|---|---|
| `entry/history.csv` | Per runde: `points`, `gw_rank`, `overall_rank`, `total_points`, `value`, `bank`, `transfers`, `hit`, **`bench_points`** | Nivå 0 for egen tropp |
| `entry/picks/gw{n}.csv` | Ditt laguttak per runde med `multiplier`, `captain`, `vice`, `minutes`, `raw_points`, `effective_points`, `bps`, `bonus` | Nivå 0 for egen tropp |
| `live/gw{n}.csv` | Alle spilleres rundefasit: minutter, mål, assist, clean sheet, redninger, `defensive_contribution`, bonus, BPS, `total_points` | Nivå 0 **etter** låsing 09:00 UK |
| `players.csv` | 652 spillere: pris, eierandel, form, `ep_next`, `status`, `news`, overganger inn/ut denne runden | Nivå 0 på spillerfelt, **ikke** på aggregat |
| `events.csv` | Rundesnitt, høyeste score, mest kapteinet, **antall spilte chips per type** | Nivå 0 |
| `fixtures.csv`, `fixtures.json` | APIets eget kampprogram med kampdato | **Slår `fixtures2627.csv` på kampdato**, som kun er validert på rundenivå |

**`bench_points` spores hver runde.** Den er utløseren for Bench Boost i `02` og er den eneste direkte målingen av om benken faktisk er verdt en chip.

**Regel ved konflikt mellom projeksjon og oppstilling:** oppstillingen vinner. En projeksjon er en gjetning skrevet før kampen; en oppstilling er trenerens observerte valg.

**Regel ved konflikt mellom to samtidige projeksjoner:** flertall blant uavhengige kilder vinner over en enkeltstående avviker, men flertallet skal navngis, ikke bare telles. To kilder som uavhengig lander på samme svar med dager mellom seg veier tyngre enn én kilde samme dag som avviker.

| Tilfelle | Projeksjonen sa | Oppstillingen viste | Vi fulgte |
|---|---|---|---|
| Slater, 13.–15. aug | Scout: startplassen er «diskutabel» | Startet i pivot mot Nice 15. aug | Oppstillingen |
| Mbeumo, 15.–17. aug | Scout: ventes å spille spiss, bedre valg enn Cunha | Cunha startet på nieren mot Milan 15. aug, Mbeumo inn for ham | Oppstillingen — punktet står åpent |
| Egan, 15.–19. aug | Clarke: ikke i Hulls XI | Startet mot Nice 15. aug | **Ingen av dem — årsaksregelen avgjorde.** Mendy signerte 12. aug og satt på benken. |
| Szoboszlais rolle, 18.–21. aug | Yahoo (18.8.) og Sportsmole (21.8.): sentral midtbane med Gravenberch. 3addedminutes (21.8.): høyrekant | — | **Topartskonsensusen** (Yahoo + Sportsmole, uavhengige, fire dager mellom seg) foran enkeltkilden samme dag |

**Merk om premierleague.com:** nettstedet motsier seg selv. 17. august skrev Scout at Mbeumo ventes å spille spiss i Seskos fravær; samme dag førte Adrian Clarke Sesko i Uniteds XI. Samme artikkel fører Saliba og Timber i Arsenals XI og skriver i notatet under at begge er skadet. **Clarkes XI-artikkel er en fullt-skadefri-projeksjon merket som GW1-verktøy.** Behandle den som nivå 5, og bare på signeringer og roller.

**Scout Selection er en eierandelsprediktor, ikke en anbefaling.** Alt som står der blir høyt eid. Å avvike er ikke gratis, men å konvergere koster hele separasjonskilden. Se `01`.

## Verifisert 19. august: BPS-endringene 2026/27

Tesen i `02` var delvis feil og ble etterprøvd mot fire uavhengige kilder.

| Endring | Innhold | Konsekvens |
|---|---|---|
| CBI | 1 BPS per **tre**, mot 1 per to | Rammer stillestående midtstoppere |
| Takler | **Urørt — 2 BPS, verifisert begge sesonger** | Holdende midtbanespillere rammes lite |
| Ballerobringer | 1 per 3 i 2026/27. **2025/26-verdien er ikke verifisert** | «Urørt» kan ikke hevdes |
| Å bli taklet | **−1-straffen fjernet** | Ballbærere og offensive backer vinner |
| Keeperredning | **Netto per skudd er uendret.** 2025/26: 3 i boksen, 2 utenfor. 2026/27: 2 for enhver redning + 1 for skudd i boksen = 3 i boksen, 2 utenfor | Gevinsten ligger *ikke* i skuddredninger |
| Keeper, reell gevinst | Redninger som **ikke** kommer av et skudd (f.eks. innlegg via medspiller) gir nå 2 BPS der de før ga null, pluss big chance-kategorien | Favoriserer travle keepere — men av en annen grunn enn tidligere ført |
| Keeper, ny kategori | **+1 for big chance-redning** | Samme retning |
| DefCon | **Uendret** (10 CBIT / 12 CBIRT → 2 poeng) | Der forsvarsverdien fortsatt ligger |

**Størrelsesorden:** BPS avgjør kun bonus, maks 3 poeng per kamp, i konkurranse. En midtstopper taper anslagsvis 5–10 bonuspoeng over en sesong. **Tesen er nedgradert fra «viktigste enkeltendring» til andreordens rebalansering.**

## Feillogg

### Ny feil, 3. september, sent: sekundærkilde avvist på en antakelse i stedet for et oppslag

Claude forkastet en merknad fra starting11.com om at City hadde Champions League-kamp tre dager etter Coventry-kampen, med begrunnelsen at «det stemmer ikke med et normalt UCL-oppsett i september». Merknaden var korrekt: ligafasen 2026/27 starter tirsdag 8. september, og City spiller Porto borte den kvelden (UEFA.com, nivå 1 for egen turnering). Kampen mot Coventry er lørdag 5. september.

Avvisningen hvilte på et mønster fra tidligere sesonger, der ligafasen har startet midt i september. Kalenderen ble aldri slått opp. Feilen forplantet seg: Triple Captain ble låst til GW7 uten at europakalenderen var kontrollert, og GW7 viste seg å ligge mellom MD2 og MD3 — den verste av kandidatrundene, ikke den beste.

**Rotårsak:** en antakelse om hva som er normalt ble brukt som grunnlag for å forkaste en kilde. Det er samme handling som regel 1 forbyr, utført i motsatt retning — ikke å gjette et svar, men å gjette at et svar er galt. «Jeg fant ingen» dekker begge retninger: fravær av bekreftelse er ikke motbevis.

**Regelen som fulgte:** **en sekundærkilde forkastes kun mot et oppslag, aldri mot en antakelse om hva som er sannsynlig.** Kan påstanden ikke kontrolleres i øyeblikket, merkes den som ubekreftet og tas med videre — den forsvinner ikke.

**Avledet regel for chip-planlegging:** **europakalenderen (UCL, EL, Conference) og landslagsvinduer skal kontrolleres før en runde settes for Triple Captain eller Bench Boost.** Fikstursvanskelighet alene er utilstrekkelig når spilleren tilhører en klubb i Europa. Datoene ligger på UEFA.com; kampdato for Premier League i `fpl-data/fixtures.csv`.

### Ny feil, 3. september: komprimert minnesammendrag brukt som kilde på troppssammensetning

Claude listet benken som «Dúbravka, Davis, Diop, Slater» i sitt første svar i økten. **Dúbravka ble solgt 21. august** (→ Verbruggen), noe `01` sier eksplisitt i både troppstabellen og endringsloggen. Feilen ble oppdaget først da benkens faktiske poeng ble hentet fra `entry/picks/gw2.csv`, der Verbruggen står på benken.

Samme feil lå uavhengig i prosjektets minnesammendrag, som daterte seg til GW2 (28. august) men bar en troppssammensetning fra før 21. august. Sammendraget hadde også anti-drift-nevneren på **£31,5m** — tallet fra før Dúbravka→Verbruggen. `01` linje 115 sier «Nå £32,0m etter Verbruggen-byttet (var £31,5m)», og tallet er £32,1m i dag etter Calafioris prisstigning. To feil, én årsak.

**Rotårsak:** et komprimert sammendrag er en gjengivelse av filene på et tidspunkt, ikke filene. Det bærer ingen mekanisme for å oppdatere avledede tall når input endrer seg, og det oppgir sin egen dato uten å garantere at alt innholdet er fra den datoen. Å lese det som fasit er samme feiltype som er loggført 27. august («et tall i `01` fulgte ikke med da input endret seg») og 28. august («tidssoneforveksling mellom minnesammendrag og prosjektfil») — tredje gang på under to uker.

**Regelen som fulgte:** **et komprimert minnesammendrag er aldri kilde på troppssammensetning, priser, eierandeler eller andre tall som endrer seg. Det er en peker til hvor svaret står, ikke svaret.** Skal et slikt tall nevnes, hentes det først fra `01`, fra `context/`-filene eller fra `fpl-data`. Gjelder også når sammendraget virker ferskt og internt konsistent — begge disse gjorde det.

**Avledet sidekonsekvens:** samme regel gjelder Claudes egne tidligere svar i økten. Filen leses fra disk før hver redigering, ikke fra det Claude selv skrev lenger opp.

### Ny feil, 28. august, sent: overstyringsklausul anvendt bokstavelig, uten å sjekke om mekanismen bak den fortsatt gjaldt

Claude reverserte GW2-benkerekkefølgen fra Slater/Davis/Diop til Davis/Diop/Slater med begrunnelsen at Regel 7-overstyringens navngitte vilkår («et konkret, tallfestet skadeflagg») ikke lenger var oppfylt etter at både Gibbs-White- og N.Williams-flaggene ble lukket. Brukeren spurte hvorfor ikke den opprinnelige rekkefølgen sto ved lag, og ved gjennomgang viste reverseringen seg å være feil.

**Hva som ble oversett:** selve mekanismen bak Regel 7 (motoren hopper over en ugyldig erstatning) gjør konsekvensen av rekkefølgen asymmetrisk. En benket forsvarer er ugyldig ved en forsvarerblank uansett hvor lavt han står — rekkefølgen er irrelevant der. Men en benket forsvarer *er* gyldig ved en midtbane- eller spissblank (3-4-3 → 4-3-3 er lovlig), og konkurrerer da reelt med en benket midtbanespiller om plassen. I det reelle valget avgjør ren benkerekkefølge hvem som spilles inn. Fiksturforskjellen mellom Slater (Coventry hjemme) og Davis/Diop (Man Utd borte) eksisterer helt uavhengig av om noen har et navngitt flagg. Flagget var aldri den bærende begrunnelsen for å sette Slater først — det var bare den letteste måten å utløse riktig konklusjon på, og da det forsvant, ble hele konklusjonen feilaktig behandlet som om grunnlaget var borte.

**Regelen som fulgte:** når en klausul er skrevet med et konkret utløsende vilkår (her: et navngitt flagg), og vilkåret forsvinner, skal den **underliggende mekanismen** — ikke bare vilkårets bokstav — sjekkes på nytt før en konklusjon reverseres. Et utløsende vilkår er ofte bare én vei til en konklusjon, ikke den eneste. Regel 7s overstyringsklausul er foreslått omformulert i `01` til å gjelde forventet avkastning direkte, ikke et navngitt flagg — ikke besluttet, kun foreslått.

**Ikke verifisert:** resonnementet om auto-sub-motorens skip-mekanikk ved to eller flere samtidige blank er ikke sjekket mot `05-spillets-regler.md` denne økten. Énblank-tilfellet (det klart vanligste) er robust; flerblank-tilfellet hviler på alminnelig forståelse av hvordan motoren virker, ikke på et fersk oppslag.

### Ny feil, 28. august, kveld: samme tidssoneforveksling gjentatt — denne gangen mellom minnesammendrag og prosjektfil

I en vurdering av et GW2-nyhetsbrev hevdet Claude at deadline var oppgitt til «19:30» i egne notater, at nyhetsbrevets «18:30 BST» dermed avvek fra det, og tilbød å rette en «feil» i `02`. Etter at brukeren lastet opp den faktiske filen, viste `02` seg å ha vært riktig hele tiden: **18:30 BST / 19:30 norsk** — samme klokkeslett i to tidssoner, ikke to ulike klokkeslett. Ingen feil fantes i prosjektet.

Feilen lå i det komprimerte minnesammendraget Claude hadde tilgang til før filene ble lastet opp. Sammendraget skrev «GW2 Friday 19:30 lock» uten å bevare skillet mellom BST og norsk tid som `02` selv holder konsekvent i hver eneste rad. Claude sammenlignet dette upresise tallet direkte mot nyhetsbrevets BST-oppgitte klokkeslett, uten å åpne kildefilen først.

**Dette er nøyaktig samme feiltype som ble loggført 27. august** («Klokkeslett i to tidssoner» — 20:00 minus 19:30 norsk ga feilaktig 30 minutter i stedet for riktig 90). Forskjellen er hvor de to tallene kom fra: den 27. august sto begge i samme fil; denne gangen kom det ene fra et minnesammendrag og det andre fra en ekstern kilde. Regelen fra 27. august dekket ikke dette tilfellet eksplisitt, og ble derfor ikke anvendt.

**Regelen som fulgte:** utvid 27.-august-regelen. Før et tidsavvik påstås — uansett om begge tallene står i én fil, én står i et minnesammendrag, eller én kommer fra en ekstern kilde — konverter til én tidssone **og** åpne kildefilen for å lese den fulle originalteksten, ikke et sammendrag av den. Et komprimert minne kan slette et skille (som BST/norsk) uten at det er synlig at noe mangler. «Jeg har notert X» er aldri sterkere bevis enn kildefilen X angivelig kommer fra.

### Ny feil, 28. august: prosjektfiler redigert på tvers av chat uten fersk sjekk

Claude kopierte `01` og `03` fra `/mnt/project` i én chat og redigerte dem direkte, uten å spørre om en parallell chat kunne ha endret dem siden siste synk. Brukerens dokumenterte arbeidsflyt går på tvers av flere chatter og enheter (Mac og mobil). Resultatet var filer som, hvis lastet opp direkte, ville slettet GW2-beslutningen, GW2-laguttaket, prisstatusoppdateringen 27. august, anti-drift-korrigeringen, Chelsea-europastatusen, Rogers-revurderingen og tidssonerettelsen — alt utført i den andre chatten i mellomtiden. Brukeren fanget det selv, ved å diffe før opplasting.

**Regelen som fulgte:** samme prinsipp som filnavnregelen («stol aldri på en tidligere økts konklusjon uten fersk `ls`»), utvidet til å gjelde på tvers av chatter — spør eksplisitt om en fil kan være endret et annet sted før redigering når arbeidsflyten er kjent å gå på tvers av økter, og lever endringer som isolerte patcher mot brukerens egen innlimte/opplastede tekst når det er noen tvil om hvilken versjon som er gjeldende, ikke som fulle filerstatninger fra en antatt kanonisk kopi.

### Ny feil, 27. august, verifiseringsrunde: et tall i `01` fulgte ikke med da input endret seg

Under en full gjennomgang av alle seks filer før commit ble to interne motsigelser funnet i `01`, begge fra samme økt tidligere samme dag.

**1. Anti-drift-tallet.** Seksjonen «Anti-drift-metrikken» (fastsatt 19. august, definert som løpende, ikke historisk) ga £19,5m av £32,0m = 60,9 % — beregnet fra Calafioris kjøpspris £5,5m. Samme fil førte senere samme økt inn at Calafiori hadde steget til £5,6m natt til 27. august. **De to tallene sto side om side uten at det ene ble oppdatert etter det andre.** Chelsea-seksjonen gjentok i tillegg eksplisitt «Topplagsandelen står uendret på £19,5m» — en påstand skrevet før prisøkningen ble kjent, men aldri korrigert etter at den var det.

**2. Klokkeslett i to tidssoner.** GW2-laguttaket skrev at Man City–Crystal Palace («20:00 britisk tid») sparkes i gang «30 minutter etter GW2-fristen». Fristen er 18:30 BST — 19:30 er den **norske** tiden for samme frist. 20:00 minus 19:30 (norsk) ga 30; riktig avstand i én tidssone er 90 minutter, som også er nøyaktig det `05` fastsetter som standardavstanden mellom frist og første avspark.

Begge feilene ble funnet ved å kryssjekke `01` mot seg selv (mellom to seksjoner) og mot `04`/`05` (nivå 0-kilder for henholdsvis kamptid og regelverk) — ikke ved at brukeren pekte på dem.

**Regelen som fulgte:** når et tall skrives inn ett sted i en fil, søk gjennom **resten av samme fil** etter avledede tall som bygger på det, i samme økt. Og: **konverter alltid til én tidssone før to klokkeslett trekkes fra hverandre** — spesielt når filen selv veksler mellom britisk og norsk tid slik denne gjør konsekvent ellers.

### Ny feil, 27. august: firukersregelen brutt på egen kontrollert kilde

I en vurdering av Newcastles laguttak til GW2 ble Anthony Gordon oppgitt som tvilsom, hentet fra en Spurs Web-artikkel. **Samme artikkel var i samme svar allerede identifisert som å inneholde en feil manager** (Thomas Frank i stedet for bekreftet De Zerbi) — nøyaktig det signalet firukersregelen (21. august) ble skrevet for å fange. Artikkelen viste seg datert **9. februar 2026**, over seks måneder gammel. I stedet for å forkaste hele kilden idet manager-feilen ble oppdaget, ble én annen detalj fra samme artikkel (Gordon) likevel brukt, uten kryssjekk mot en gyldig kilde.

Brukeren fanget feilen. Oppslag viste at Gordon ble solgt til Barcelona, overgang fullført **30. mai 2026** (tre uavhengige kilder samstemte på beløp: ca. £69,3m / €80m). Han har ikke vært Newcastle-spiller siden.

**Dette er nøyaktig samme mønster som Arne Slot-eksemplet regelen selv ble skrevet på grunnlag av** (se firukersregelen under): feil manager avslører feil sesong. Forskjellen er at denne gangen ble signalet faktisk observert — og likevel ikke fulgt til sin konklusjon.

**Regelen som fulgte:** når én detalj i en kilde avslører feil sesong eller periode (feil manager, feil resultat, et datostempel som ikke stemmer), forkastes **hele** kilden i samme øyeblikk — ikke bare den detaljen som utløste mistanken. Dette gjelder også når en annen del av samme kilde virker plausibel eller ikke direkte er motsagt av noe annet. Dette er samme presisering som kildekonflikten 22. august («én gal rad diskvalifiserer ikke kilden»), men med motsatt fortegn: der gjaldt det én gal rad i en ellers pålitelig kilde, her gjelder det én rad som beviser at hele kilden er fra feil periode.

### Ny feil, 25. august: aggregatfelt fra API-et ført som verifisert rundefasit

Claude rapporterte «Snitt 36» og «Høyeste enkeltlag 114» i en tabell merket som API-verifisert. Faktisk: **48 og 131**. Brukeren måtte korrigere.

Feilen har to lag. Det ytre er tallene. Det indre er at hele `events`-blokken ble behandlet som én kilde med én pålitelighet, fordi *andre* felter fra samme henting stemte. Claude skrev riktignok at runden ikke var låst, men lot så tallene stå i en tabell uten forbehold — **et generelt forbehold øverst opphever ikke en presis påstand lenger nede.**

Samme henting ble brukt til chipbruk, rangerte lag, «mest kaptein: Haaland» og «rundens beste spiller: De Cuyper 17». **Alle disse viste seg riktige etter låsing** — se tabellen i regelen øverst. Bare de tre poengaggregatene var gale.

**Det gir en andre feil i samme sak:** karantenen ble satt for bredt. Åtte felter ble erklært uverifiserte fordi to var gale, uten at de øvrige seks ble sjekket. Det er samme overkorreksjon i motsatt retning av den opprinnelige feilen — først for tillitsfull mot hele blokken, så for mistroisk mot hele blokken. **Ingen av delene er en sjekk.**

**Regelen som fulgte:** se regelen om aggregatfelt øverst i filen. Og: når ett tall fra en kilde viser seg galt, karanteneres hele feltgruppen fra samme kilde til hver enkelt er etterprøvd — den skal ikke reddes felt for felt med «men dette virker riktig».

### Ny feil, 25. august kveld: to påstander om marked og priser

**1. `price_change_projections` lest feil.** Claude skrev at Calafiori «passerer 100 % i neste kjøring — stiger etter alt å dømme i natt», basert på `offset 0: 92,3 %` og `offset 1: 127,0 %`. **`offset 0` er progresjonen ved kveldens frist, ikke et varsel om at den passeres.** 92,3 % utløser ingenting. Riktig lesning: stigning natt til torsdag, ikke i natt. Bekreftet mot LiveFPL, som lander på samme døgn.

**Regelen som fulgte:** `offset n` er en tilstand ved frist *n*, ikke en hendelse. En stigning inntreffer først i den første offseten der verdien er **over 100**.

**2. «Alternativet ingen hadde lagt på bordet».** Claude presenterte B.Fernandes → Palmer som et upåaktet trekk. Det er det **tiende hyppigste byttet i spillet**, gjort av 4 899 lag. Påstanden var en retorisk figur uten datagrunnlag, i en fil hvor separasjon fra template er hele formålet.

**Regelen som fulgte:** påstander om at et trekk er upåaktet krever byttetall. Uten dem skrives forslaget som forslag, uten adjektiv.

### Ny feil, 25. august: en kilde forkastet i sin helhet fordi én kolonne var ubrukelig

Claude skrev at Sportradars oppstilling for Fulham–Chelsea var «ubrukelig på banerolle» og begrunnet det med at den førte **seks forsvarere** i elleveren. Konklusjonen om posisjonsetikettene var riktig. Slutningen om at elleveren dermed ikke kunne brukes, var det ikke — **seks forsvarere er nøyaktig hva en treer bak med to wingbacker gir**, og alle elleve navnene stemte mot lagoppstillingsgrafikken brukeren la fram etterpå.

Kilden inneholdt altså svaret Claude etterlyste, og Claude kastet den fordi én kolonne var feil.

**Regelen som fulgte:** forkast felt, ikke kilder. Når noe i et datasett er åpenbart galt, skal det navngis **hvilken kolonne** som er gal og hva resten fortsatt kan brukes til. Dette er samme feiltype som karantenen av `events`-blokken over, begått i samme økt.

### Ny feil, 25. august: projisert ellever brukt som avgjørende bevis (Egan → Diop)

`01` skrev 19. august: «Hulls projiserte GW1-ellever fører **Mendy i midtstopperparet og Egan ute**. Ipswich' projiserte XI fører Diop og Davis i bakre firer. **Byttet er ikke lenger valgfritt.**»

Hulls faktiske ellever mot Man Utd: Tzolakis; **Mendy, Egan**, Ajayi, Coyle, Stroud; Crooks, Slater, Giles; Belloumi, McBurnie. **Begge startet.** Egan: 21 DefCon, clean sheet, 27 BPS — 8 poeng (regnet mot `05`). Diop: 2 poeng.

Konklusjonen om å eie en startende £4,0m-forsvarer var ikke gal i seg selv. Formuleringen **«ikke lenger valgfritt»** var det: den ga nivå 5-bevis vetorett over et valg, i direkte strid med kildehierarkiet i denne filen. Merk at årsaksregelen ble anvendt riktig (Mendy signerte 12. august), men på feil spørsmål — den svarte på «eier Egan drakta?» og ikke på «starter han i GW1?».

**Regelen som fulgte:** en projisert ellever kan aldri gjøre et bytte obligatorisk. Den kan bare flytte et bytte fra «avvist» til «vurderes». Ord som «ikke lenger valgfritt», «tvunget» og «må» krever nivå 1–2-bevis.

### Ny feil, 25. august: to avvisninger hvilte på premisser GW1 motbeviste

| Spiller | Skrevet i `01-vurderte-spillere.md` | Hva som faktisk skjedde |
|---|---|---|
| **Guehi £6,0m** | «han er **midtstopper** — den ene profilen den verifiserte BPS-endringen faktisk rammer» | Spilte sentral midtbane i Citys 4-2-3-1, scoret utligningen, 31 BPS, 2 bonus. **10 poeng** (regnet mot `05`). Rollen er fra ESPNs kampreferat — sekundærkilde, ikke bekreftet fra mancity.com |
| **Semenyo £8,5m** | «**Ikke i FFScouts predikerte GW1-ellever** mot Bournemouth» | Startet på venstrekanten i Dokus fravær. Bekreftet fra **mancity.com** sin egen elleverliste, nivå 1 |

Semenyo-raden er samme feil som Egan-raden: en predikert ellever brukt som bevis for det motsatte av det som skjedde. Guehi-raden er en annen feiltype — **posisjon antatt fra fjorårets rolle og deretter brukt som tesegrunnlag.**

**Regelen som fulgte:** en avvisning som hviler på posisjon skal oppgi *hvor* posisjonen er verifisert. FPLs posisjonsklassifisering er ikke bevis på hvor en spiller står på banen; den er bevis på hvordan poengene beregnes.

### Ny feil, 22. august: regelendring utledet av at noe manglet i egen fil

Claude meldte to ganger at «spisser får DefCon-poeng i 2026/27» som et nytt funn fra API-et, og skrev at det motsier `02`s «DefCon uendret». Begge deler var feil. Spisser har hatt DefCon siden 2025/26, og `02`s «uendret» var korrekt hele veien. Det eneste som manglet i `02` var at spisser ikke sto nevnt i en parentes.

Grunnlaget for påstanden var at API-et viser `FWD: 2` mens `02` bare nevner forsvarere og midtbane. **Fraværet av en linje i vår egen fil ble lest som bevis på en endring i spillets regler.** Påstanden ble dessuten gjentatt som «den som faktisk kan flytte en beslutning» før den var slått opp.

**Regelen som fulgte:** en fil kan være ufullstendig uten at verden har endret seg. Et avvik mellom en datakilde og en kontekstfil er først og fremst en hypotese om **filen**, ikke om regelverket. Regelendringer slås opp i regelverket — se sjekkpunkt 9 og nivå 0 i kildehierarkiet.

### Ny feil, 22. august: reparert fil overskrevet med den ureparerte originalen

Under arbeidet med regelfunnene kopierte Claude `02` fra opplastingsmappen inn i arbeidsmappen for å ha en «ren» fil. Opplastingen er **prosjektversjonen fra før reparasjonen**, så kopien slettet stirettingen `claude/04-…` → `04-…` og begge oppdaterte headerlinjer. Feilen ble oppdaget fordi et skript stoppet av en helt annen grunn og filen ble inspisert.

**Regelen som fulgte:** opplastingsmappen er et **arkiv av det som ble sendt**, ikke en kilde til gjeldende versjon. Etter første redigering er arbeidsmappen fasit. Kopier aldri «tilbake til original» uten å sjekke hvilke endringer originalen mangler — det er samme feiltype som «opplastet kopi lest som kanonisk», bare i motsatt retning.

### Kildekonflikt, 22. august: strafferedning oppgitt som −8 BPS

En brukerlevert oppsummering av 2025/26-endringene (fpl.page) skriver at «a penalty save deduction was adjusted to -8 BPS». Det er feil fortegn. premierleague.com skriver 20. juli 2026 at en keeper **tjente** 8 BPS for en strafferedning i 2025/26, og at tallet faller til 7 i 2026/27. `05` bekrefter 7 for inneværende sesong.

**Vi stoler på premierleague.com og `05`.** De øvrige påstandene i samme oppsummering — straffemål 12 flatt, mål 24/18/12 etter posisjon, redning på strek 9, takling 2 — stemmer alle mot `05`, og er derfor brukt som bekreftelse på at de kategoriene er uendret fra 2025/26. **Én gal rad diskvalifiserer ikke kilden, men den avgjør at ingen rad derfra brukes uten kryssjekk mot `05`.**

### Ny feil, 22. august: startplass utledet av en poengsum

Claude skrev «Tzolis startet og fikk 6» på grunnlag av miniligafilens poengtabell. Poengsummen alene beviser ikke start. Seks poeng for en midtbanespiller går opp på minst tre måter, og **1 (innbytt under 60 min) + 5 (mål) = 6** er én av dem. Påstanden om start kom altså før beviset for den.

Konklusjonen viste seg riktig da kamptroppen ble slått opp — Tzolis sto i elleveren. Men det er femte gang mønsteret **riktig konklusjon, gal begrunnelse** er loggført i denne filen, og det er mønsteret som er problemet, ikke utfallet.

**Regelen som fulgte:** en poengsum er et *resultat*, ikke en *oppstilling*. Den kan bekrefte at en spiller deltok, aldri at han startet. Skal startplass hevdes, skal den hentes fra kamptroppen. Dette er en utvidelse av «oppstillingen vinner over projeksjonen» til også å gjelde bakover: **oppstillingen vinner også over poengsummen.**

### Ny feil, 22. august: innhold slettet i en omskriving uten at slettingen ble flagget

Ved omskrivingen av `01` 21. august kveld forsvant linjen om at **Arteta selv navnga Illan Meslier** som ny Arsenal-signering. Femten linjer ble fjernet i den økten. Fjorten var erstatninger — en linje byttet mot en som inneholdt den. Én var et rent tap. Ingen så det før `git diff` viste det dagen etter.

Faktumet overlevde i `03`s «mangler»-rad, men kilden gjorde det ikke. En nivå 1-observasjon ble redusert til en huskelapp om at noe manglet i en prisliste.

**Regelen som fulgte:** når en seksjon skrives om, list hva som **fjernes**, ikke bare hva som legges til. Fra nå gjør git dette automatisk. Det er hovedgrunnen til at filene skal ligge i repo og ikke bare i prosjektet — prosjektet viser siste versjon, git viser hva siste versjon kostet.

### Ny feil, 22. august: opplastet kopi lest som kanonisk filnavn

Claude hevdet at fem referanser til `fixtures-2627.csv` (med bindestrek) i `02` og `03` var brutte, og at filen skulle hete `fixtures2627.csv` (uten). Konklusjonen den gang var at motsatt var sant — at den lokale filen hadde bindestrek med identisk hash, og at opplastingen til prosjektet hadde strippet den.

⚠️ **Den konklusjonen holdt ikke. Rettet 22. august, kveld.** Ved gjennomgangen samme kveld var prosjektfilen `fixtures2627.csv` — **uten bindestrek** — mens alle fem tekstreferansene fortsatt brukte bindestrek. Enten var «identisk hash»-sjekken feil den 22. august tidligere på dagen, eller filen ble lastet opp på nytt uten bindestrek i mellomtiden. Ingen av delene er etterprøvd nå; det faktiske filnavnet er verifisert direkte med `ls` mot `/mnt/project/`, ikke utledet. **Alle referanser i `01`–`04` og `CLAUDE.md` er rettet til `fixtures2627.csv`** for å matche det bekreftede filnavnet.

**Regelen som fulgte, stående:** én observert artefakt slår ikke fem samstemte referanser *uten at artefakten er verifisert på nytt*. Men motsatt gjelder også: fem samstemte referanser beviser ikke et filnavn hvis ingen av dem er sjekket mot disk samme økt. **Ved filnavnkonflikt: sjekk disk direkte (`ls`) hver gang, stol aldri på forrige økts konklusjon om at det er avklart** — filnavn kan endre seg mellom opplastinger på en måte ingen tekstreferanse fanger opp.

### Ny feil, 21. august kveld: bench-mekanikk forvekslet med kampdeltakelse

Kinsky ble omtalt som «garantert null poeng» i en Bench Boost-vurdering, med begrunnelsen at han er benket i vår ellever. Det er sant i **normale** runder — bench teller ikke da, uansett hvem som er der. Men Kinsky **spiller** for Tottenham mot Brentford uansett, og med Bench Boost aktivert ville hans faktiske poeng fra den kampen ha telt fullt ut. Feilen ble brukt som argument for å utsette Bench Boost i GW1 — et argument som falt bort idet feilen ble rettet, men konklusjonen (vent til etter GW16-wildcarden) sto likevel, nå på riktig grunnlag: chipen er engangs, og et bevisst bygget benk i en dobbeltrunde har høyere forventet verdi enn en tilfeldig sammensatt GW1-benk, ikke fordi GW1-benken er «død».

**Regelen som fulgte:** skill mellom «teller ikke i vårt lag» og «spiller ikke sin kamp». Det første er en konsekvens av chip-valg; det andre er en faktisk tilgjengelighetsstatus. Sjekk alltid om en benket spiller faktisk spiller for klubben sin før en påstand om «null poeng» brukes i en chip-vurdering — de to spørsmålene har forskjellige svar.

⚠️ **Syv nye oppføringer 20.–21. august. Alle er begått av Claude i løpet av det siste døgnet før GW1-deadline.**

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

### Ny feil, 21. august kveld: årstall ikke sjekket før bruk

Et si.com-oppslag om Szoboszlai ble brukt i Szoboszlai-vurderingen. Artikkelen omtalte Arne Slot som Liverpool-manager — han er avgått, Iraola er bekreftet manager for 2026/27. URL-en bar datostempelet «8-25-25»: artikkelen var fra august **2025**, ett år gammel. Feilen ble oppdaget fordi manager-navnet var åpenbart galt, ikke fordi datoen ble sjekket først.

**Regelen som fulgte:** se firukersregelen øverst i filen. Sjekk publiseringsdato før innhold brukes, ikke som feilsøking etterpå.

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
| `web_fetch` mot bildebaserte oppstillingsgrafikker (FFScout predicted XI) | Leverer ofte kun rundtekst, ikke spillernavnene i selve grafikken. Posisjonsdetaljer må da bekreftes fra en tekstbasert kilde i tillegg |
| **`web_fetch` mot `event/{n}/live/` og `bootstrap-static`** | **Kutter etter ca. 120 000 tegn.** `live` gir kun element-ID 1–167; `bootstrap-static` gir `events`, `teams`, `element_types` og deretter kun de ~30 første spillerne. Spillere med høyere ID må hentes en annen vei. `text_content_token_limit` har ingen virkning — kuttet er fast |
| **`element-summary/{id}/`** | **Avvises av `web_fetch`** med PERMISSIONS_ERROR, fordi den konkrete URL-en ikke har stått i et tidligere søkeresultat. Malen i dokumentasjonen teller ikke |
| **`fantasy.premierleague.com` fra `bash`** | **Blokkert på vertsnivå** (HTTP 403, `x-deny-reason: host_not_allowed`). ⚠️ **Løst 3. september:** gå ikke via `web_fetch` lenger — bruk snapshot-repoet, som gir samme data uten kutt og uten 403. `curl -s https://raw.githubusercontent.com/steinim/fpl-data/main/data/{fil}` |
| **`api.github.com` fra `bash`** | Uautentiserte kall treffer ratebegrensning raskt. For å liste filer i repoet: hent `https://github.com/steinim/fpl-data/tree/main/data/{katalog}` og `grep` ut `"path":"..."` fra HTML-en i stedet |
| **LiveFPL Price Predictor, lagret som .mht** | Parses med `email.message_from_bytes`; sidas HTML ligger i den største `text/html`-delen. **Kun «Risers»-fanen lagres** — fallerlista er klientrendret og følger ikke med. Sida har **ingen tidsstempel**, så alderen på tallene må oppgis av den som lagret den |
| ID → navn-oppslag | `raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2026-27/player_idlist.csv` er tilgjengelig fra `bash` og gir hele ID-listen. **`players_raw.csv` i samme repo er et førsesongsnapshot** — priser og eierandeler der er utdaterte, kun ID, navn, klubb og posisjon kan brukes |

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
| Maguire og Semenyo | **Vurdert og avvist 21. august kveld.** Se `01` |
| Bench Boost i GW1 | **Avvist — men på riktig grunnlag etter rettelsen over.** Chip spares til etter GW16-wildcarden |

### Åpne punkter etter deadline

| Punkt | Frist | Hva som avgjør det |
|---|---|---|
| **Tzolis' plass** | ~~GW1~~ → GW2–3 | **GW1 avgjort:** startet mot Coventry, bekreftet fra kamptroppen. Det blinde slottet leverte. Gakpo £7,0m står fortsatt som førstevalg hvis han ryker senere |
| **Calafiori/Hincapié** | ~~GW1~~ → GW2–3 | **GW1 avgjort:** Calafiori startet, Hincapié på benken. Parformuleringen ga ikke utslag i første uttak |
| **Šeško tar nieren?** | GW3–5 | Avgjør om Mbeumo er permanent kantspiller. Ikke et salgssignal i seg selv |
| **Citys tilførsel** | Løpende | Seks avganger/skader på fjorten dager. Berører Haaland direkte og GW13-planen for O'Reilly |
| Slaters og Davis' plass | 1. september 23:00 BST | Vinduet stenger **etter** GW2-deadline. Opprykkslagene bygger fortsatt tropp |
| **Konsa** | — | **Lukket 21. august.** Arsenal kjøpte ham fra Villa (£51m + £4m, Sky Sports/ESPN/Just Arsenal). Ikke spilleberettiget GW1 — rakk ikke registreringsfristen torsdag. Se `01` og `02`. |
| Full gjennomgang av prislisten | Etter 1. september | Trafford-feilen viser at klubbkolonnen drifter under vinduet. **Cherki (MCI) mangler.** Meslier (ARS) £5,0m lagt inn i `01` 22. august |
| BPS-tesen — holder den? | Etter GW5 | **Mekanikken er nå verifisert mot regelsiden, ikke bare mot artikler** (se `05`). Keeperdelen er korrigert: netto per skuddredning er uendret. Det som gjenstår er faktisk bonusfordeling. Avgjør GW16-keepervalget, som nå gjelder Verbruggen/Kinsky → Raya |
| **2025/26-BPS som sammenligningsgrunnlag** | Før GW16 | `05` gir 2026/27-tabellen komplett. Fjorårets tabell er kun delvis verifisert (straffemål 12, takling 2, redning på strek 9, posisjonsbaserte mål 24/18/12 — alle uendret). **Ballerobringsverdien for 2025/26 mangler.** Uten den kan «urørt» ikke hevdes om den halve |
| **Manglende rader i `02`s vanskelighetstabell** | Før GW6 | Brighton, Brentford, Aston Villa, Sunderland, Newcastle, Coventry, Everton, Fulham, Palace og Bournemouth mangler. **Verbruggen ble kjøpt uten et beregnet fikstursstall for Brighton.** Roefs og Thiaw ble ført som «uvurdert», ikke avvist, av samme grunn |

⚠️ **Den siste raden er den viktigste.** `02`-tabellen dekker ti av tjue klubber, og halve troppens beslutningsgrunnlag hviler på tall som ikke finnes for motparten. Beregn de ti resterende fra `fixtures2627.csv` før GW6, med samme metode som de eksisterende.

## Referanseoppstillinger

**Arsenal 3–0 Coventry, 21. august 2026, Emirates. GW1.**
Arsenal: Raya; White, Mosquera, Gabriel, Calafiori; Ødegaard, Rice, Lewis-Skelly; Saka, Havertz, Tzolis. Benk brukt: Nwaneri, Dowman, Hincapié, Zubimendi.
Coventry: Rushworth; **Van Ewijk**, B.Thomas, Amenda, DaSilva; Onyeka, Yirenkyi, Grimes; Thomas-Asante, Simms, Tchaouna.
Mål 15', 23', 49'. Coventry hadde **ett skudd på mål** i hele kampen. Arsenals bakre firer er identisk med Community Shield — Mosquera holder plassen så lenge Saliba er ute og Konsa ikke er integrert.

⚠️ **Datapunkt til BPS-etterprøvingen etter GW5:** Raya endte på 6 poeng med **én redning** — nøyaktig profilen `02` beskriver som taperen av keeperomskrivingen (toppklubbkeeper, få redninger, verdien i clean sheet). Ett datapunkt beviser ingenting. Før det inn i GW5-gjennomgangen.

**Community Shield 16. august, Principality Stadium, Arsenal 3–0 Man City.**
Arsenal (4-3-3): Raya; White, Mosquera, Gabriel, Calafiori; Ødegaard, Guimarães, Lewis-Skelly; Madueke, Havertz, Tzolis.
Man City (4-3-3): Donnarumma; Khusanov, Dias, Gvardiol, O'Reilly; Kovacic, E.Anderson, Semenyo; Foden, Haaland, Doku.

**Hull City v Nice, 15. august, MKM Stadium, 0–0.**
Hull (4-2-3-1): Tzolakis; Giles, Egan, Ajayi, Coyle; Crooks, Slater; Stroud, Dahl, Belloumi; McBurnie.
Benk inkluderte Mendy, Herrington, McNair, Targett, Dowell, McCarthy.

**Coventry v Monaco, 15. august.**
Coventry XI: Rushworth, van Ewijk, Thomas, Amenda, Dasilva, Onyeka, Grimes, Yirenkyi, Tchaouna, Simms, Thomas-Asante. Lampard gjorde bare to bytter — førstelagspreg.

## GW1-referanseoppstillinger og datapunkter — ført inn 25. august

**Hull City 2–0 Man Utd, 22. august, MKM Stadium.**
Hull: Tzolakis; Mendy, Egan, Ajayi, Coyle, Stroud; Crooks, Slater, Giles; Belloumi, McBurnie. Innbyttere brukt: Herrington, Hjerto-Dahl, Drameh, Gourna-Douath (alle inn 64' eller senere).
Man Utd: Lammens; Mazraoui, Maguire, Heaven, Shaw; Andrey Santos, Tielemans; Mbeumo, Fernandes, Dorgu; Cunha. Innbyttere brukt: Lacey, Mainoo, Yoro, Sesko, **Rashford (inn i pausen)**.
Mål: Ajayi 17', Mendy 38' (**assist Slater**, frispark). ⚠️ **Hvem som gikk av for Rashford er ikke funnet i noen kilde.** Ikke ført som kjent.

**Man City 2–1 Bournemouth, 23. august, Etihad.**
City (mancity.com, nivå 1): Donnarumma; Khusanov, Dias (K), Guehi, Gvardiol, Lewis, Anderson, O'Reilly, Semenyo, Foden, Haaland.
Bytter: Nunes for Rico Lewis 56', **Cherki for O'Reilly 63'**, Kovacic for E.Anderson (skade etter sammenstøt), én bytte 82'.
Mål: Tavernier 26' (BOU), **Guehi 84'** (assist Cherki), **Gvardiol 90'** (assist Cherki). Haaland hadde skudd på mål 75' — **derfor over 60 minutter**, som er det eneste minuttbeviset vi har for ham.

⚠️ **Uavklart: O'Reillys posisjon.** mancity.com lister elleveren uten posisjoner. FotMob fører 4-2-3-1 med Rico Lewis høyreback, Gvardiol venstreback og O'Reilly i treeren bak spissen — **nivå 5**. Sportradar klassifiserer ham som forsvarer, men det er FPL-posisjon, ikke banerolle. Én liveblogg skrev «you'd also have to assume Nico O'Reilly will be in midfield» — **hedget, ikke bevis** (se regelen om parafrase mot sitat). **Dette er ikke avklart, og GW13-planen i `02` kan ikke bygges om på det.** Krever bekreftelse fra mancity.com eller et fulltekstreferat.

### Keeper-BPS — første datapunkt til etterprøvingen etter GW5

Alle tall fra `fixtures`-endepunktet. Poengsummene er regnet mot `05` der de ikke er hentet direkte.

| Keeper | Redninger | Clean sheet | BPS | Bonus | Poeng |
|---|---|---|---|---|---|
| Tzolakis (HUL) | 5 | ✓ | **41** | 3 | 10 |
| Kelleher (BRE) | 4 | ✓ | 34 | 0 | **7** (API-verifisert) |
| Trafford (LEE) | 3 | ✓ | 28 | 2 | 9 |
| Verbruggen (BHA) | **0** | ✓ | 25 | 0 | **6** (API-verifisert) |
| Raya (ARS) | 1 | ✓ | 24 | 0 | **6** (API-verifisert) |
| Kinsky (TOT) | **5** | ✗ (3 baklengs) | 15 | 0 | 2 |

**Hva raden Kinsky gjør med tesen:** `02` hevder at BPS-omskrivingen favoriserer travle keepere i midt- og bunnlag. Kinsky leverte akkurat den profilen — fem redninger bak et nybygget forsvar — og fikk 15 BPS. Verbruggen med **null** redninger fikk 25. Clean sheet dominerer fortsatt; redninger er en modifikator oppå den, ikke en erstatning for den. Retningen i tesen (travle keepere henter mer enn før) kan fortsatt stemme, men **den slår ikke ut uten clean sheet.** Ett datapunkt. Føres videre til GW5-gjennomgangen.

### DefCon — første datapunkt

**Null av de femten i troppen nådde terskelen** (forsvarere 10, midtbane/spiss 12). Høyeste: Davis 7, N.Williams 6, B.Fernandes 6, Tzolis 6.

Til sammenligning i samme runde: Egan (HUL) 21, Acheampong (CHE) 15, Mendy (HUL) 13, Janelt (BRE) 13, Ajer (BRE) 10 — alle over terskel. Rundens høyestscorende spiller var **De Cuyper (BHA, DEF, £4,5m) med 17 poeng** (mål, assist, clean sheet, 2 bonus, 46 BPS) — men **DefCon-tallet hans var 4**. Han passer profilen tesen peker mot og hentet null poeng gjennom mekanismen tesen påberoper seg.

**Merk:** at De Cuyper var rundens beste er hentet fra `top_element` i `events`-blokken og er derfor **ikke verifisert** — se regelen om aggregatfelt. De 17 poengene hans er derimot hentet fra elementnivået og står.

## Verifisert 28. august: Gibbs-White-skadeflagget løst — presser slår appens prosentflagg

FPL-appen viste 25. august «Knee injury – 75 % chance of playing» for Gibbs-White (nivå 5, modellert av FPL selv, ikke en klubbkilde). Glasner bekreftet 28. august i offisiell pressekonferanse foran Liverpool-kampen (nottinghamforest.co.uk, nivå 1): «Morgan is available and Ryan Yates is available, which is good news.» Spiller.

Samtidig kom informasjon som ikke fantes 25. august: **Ibrahim Sangaré ute** — mindre leggskade fra onsdagens trening (skjedde etter at 75 %-flagget ble avlest, kan derfor ikke ha vært priset inn i det). **Ryan Yates tilgjengelig for første gang denne sesongen.** Savona **ikke nevnt** i sitatet — fravær av opplysning er ikke bekreftet tilgjengelighet, og føres ikke som det.

**Regelen som fulgte:** FPLs prosentflagg er en modellert sannsynlighet på avlesningstidspunktet, ikke en prognose fram til kampdag. Et 70–90 %-flagg lest flere dager før kamp skal ikke behandles som avgjort — hverken i positiv eller negativ retning — før en fersk offisiell kilde (klubbside, pressekonferanse nær kampen) foreligger. Jo lenger tid mellom avlesning og kamp, desto svakere er flagget som bevis.

Lukket i `01-strategi-og-tropp.md`, raden «Gibbs-White skadeflagget» i tabellen «Åpne risikoer inn i GW1». **Følgeeffekt ikke lukket:** GW2-benkbegrunnelsen for Slater i samme fil hviler delvis på dette flagget og er markert for revurdering, ikke revurdert i denne økten.
