# Projektna naloga – Uvod v programiranje

## Analiza turizma v Mariboru v obdobju 2020–2025

V projektni nalogi analiziram turistične prihode in prenočitve v Mestni občini Maribor med letoma 2020 in 2025. Za temo sem se odločila, ker me zanima razvoj turizma v domačem okolju in predvsem, kako se obisk Maribora spreminja skozi leto ter iz katerih držav prihajajo obiskovalci.

Glavni podatki so pridobljeni iz uradne podatkovne baze **SiStat Statističnega urada Republike Slovenije (SURS)**. Uporabljena je tabela 2164466S: *Prihodi in prenočitve turistov po državah, občine, Slovenija, mesečno*.

### Vprašanja, ki jih raziskujem

- Kako se je spreminjalo število prihodov in prenočitev med letoma 2020 in 2025?
- V katerih mesecih je v Mariboru največ turističnih prenočitev?
- Iz katerih držav prihaja največ tujih turistov?
- Kako dolgo turisti v povprečju ostanejo v Mariboru?
- Ali v podatkih opazimo posebna odstopanja in kako jih lahko povežemo z dogajanjem v mestu?

Pri interpretaciji rezultatov se dotaknem tudi turistične ponudbe Maribora, predvsem Pohorja, aktivnosti na prostem, vina in kulinarike ter večjih dogodkov. Posebej omenim športni festival OFEM 2023 in prenovo Lenta, vendar teh dejavnikov ne obravnavam kot dokazane vzroke sprememb, temveč kot možne razlage opaženih vzorcev.

## Datoteke

- `zajem_podatkov.py` – prenese podatke iz spletne baze SiStat ter jih shrani v JSON in CSV.
- `podatki/surovi_podatki.json` – surovi odgovor spletnega API-ja; nastane po zagonu programa.
- `podatki/turizem_maribor.csv` – očiščeni podatki za analizo; nastane po zagonu programa.
- `analiza_podatkov.ipynb` – Jupyter Notebook z analizo, grafi in razlago rezultatov.
- `VIRI.md` – uporabljeni spletni viri.
- `uporaba-ui.md` – opis uporabe generativne umetne inteligence.
- `.gitignore` – datoteke, ki se ne shranjujejo v repozitorij.

## Zagon

Najprej namestimo potrebne knjižnice:

```bash
pip install requests pandas matplotlib jupyter
```

Nato v glavni mapi projekta zaženemo:

```bash
python zajem_podatkov.py
```

Po uspešnem prenosu podatkov odpremo:

```bash
jupyter notebook analiza_podatkov.ipynb
```

in izvedemo celoten zvezek od začetka do konca.

## Viri

Statistični urad Republike Slovenije, podatkovna baza SiStat, tabela 2164466S.
