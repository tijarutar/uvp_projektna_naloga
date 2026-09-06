# Uporaba generativne umetne inteligence

Pri pripravi projektne naloge sem uporabljala ChatGPT kot pomoč pri načrtovanju projekta, razumevanju kode, odpravljanju napak in interpretaciji rezultatov. Generativne umetne inteligence nisem uporabljala kot nadomestilo za izvedbo analize. Predlagano kodo in dobljene rezultate sem sproti preverjala ter poskrbela, da razumem postopek zajema, obdelave in analize podatkov.

# Primeri uporabe
1. Analiza turistov po državah

Moje vprašanje:

> Kako iz podatkov SURS izločim skupne kategorije in domače turiste, da dobim samo posamezne tuje države ter lahko primerjam število njihovih prenočitev?

Odgovor UI:

Pri analizi podatkov SURS je treba najprej preveriti vrednosti v stolpcu, ki vsebuje države oziroma skupine turistov. Iz podatkov je nato mogoče s filtriranjem odstraniti skupne kategorije, kot so skupno število turistov, domači turisti in druge agregirane skupine, ter ohraniti samo zapise za posamezne tuje države.

Po filtriranju lahko podatke združimo glede na državo z metodo .groupby() in z metodo .sum() seštejemo število prenočitev posamezne države.

Kako sem odgovor uporabila?

Pomoč sem uporabila pri razumevanju filtriranja podatkov in združevanja prenočitev po posameznih državah. Tako sem preprečila, da bi bile med rezultate vključene skupne kategorije, ki niso posamezne države. Na tej podlagi sem nato pripravila analizo tujih turistov in prikaz držav z največ prenočitvami v Mariboru.

2. Filtriranje podatkov za posamezno leto

Moje vprašanje:

> Kako lahko iz podatkovnega okvirja prenocitve izločim samo podatke za leto 2023, da lahko posebej analiziram mesečne prenočitve v tem letu?

Odgovor UI:

V knjižnici Pandas lahko podatke filtriramo z logičnim pogojem nad izbranim stolpcem. Če stolpec leto vsebuje leto posameznega zapisa, lahko izberemo samo vrstice, pri katerih je njegova vrednost enaka 2023.

Rešitev:

prenocitve_2023 = prenocitve[prenocitve["leto"] == 2023]

Kako to deluje?

prenocitve["leto"] == 2023 za vsako vrstico preveri, ali je vrednost v stolpcu leto enaka 2023. Rezultat je logični pogoj, s katerim Pandas izbere samo ustrezne vrstice.

Tako nastane nov podatkovni okvir prenocitve_2023, ki vsebuje samo podatke za leto 2023. Tega sem nato lahko uporabila za ločeno analizo prenočitev po posameznih mesecih.

3. Razvrščanje držav glede na število prenočitev

Moje vprašanje:

> Kako lahko v Pandas podatke po združevanju držav razvrstim glede na skupno število prenočitev od največje do najmanjše in nato prikažem samo prvih 10 držav?

Odgovor UI:

Podatke lahko najprej združimo glede na stolpec drzava z metodo .groupby() in za vsako državo seštejemo vrednosti prenočitev. Nato z metodo .sort_values(ascending=False) rezultate razvrstimo od največje do najmanjše vrednosti, z metodo .head(10) pa izberemo samo prvih deset rezultatov.
Rezultat se shrani v spremenljivko top_drzave, ki sem jo lahko uporabila za nadaljnjo analizo in grafični prikaz desetih držav z največ prenočitvami.

# Druge oblike pomoči

ChatGPT sem uporabljala tudi pri izbiri in zožitvi teme projektne naloge, iskanju primernega uradnega vira podatkov, razlagi delovanja SiStat API-ja, načrtovanju strukture projekta, razlagi in preverjanju kode, oblikovanju idej za analizo in grafe, odpravljanju napak pri izvajanju programa ter razlagi posameznih funkcij knjižnic Pandas in Matplotlib.

Vso uporabljeno kodo sem pred oddajo pregledala, preizkusila na svojih podatkih in preverila, da razumem njen namen ter posamezne korake. Rezultate analiz sem prav tako preverila in jih interpretirala glede na podatke, uporabljene v projektni nalogi.