import csv
import json
import os

import requests


URL = "https://pxweb.stat.si/SiStatData/api/v1/sl/Data/2164466S.px"
MAPA_PODATKI = "podatki"
SUROVI_PODATKI = os.path.join(MAPA_PODATKI, "surovi_podatki.json")
CSV_PODATKI = os.path.join(MAPA_PODATKI, "turizem_maribor.csv")


def pripravi_mesece():
    """Vrne mesece od januarja 2020 do decembra 2025."""
    meseci = []
    for leto in range(2020, 2026):
        for mesec in range(1, 13):
            meseci.append(f"{leto}M{mesec:02d}")
    return meseci


def pripravi_poizvedbo():
    """Pripravi poizvedbo za podatke o turizmu v občini Maribor."""
    return {
        "query": [
            {
                "code": "MESEC",
                "selection": {
                    "filter": "item",
                    "values": pripravi_mesece(),
                },
            },
            {
                "code": "OBČINE",
                "selection": {
                    "filter": "item",
                    "values": ["070"],
                },
            },
            {
                "code": "DRŽAVA",
                "selection": {
                    "filter": "all",
                    "values": ["*"],
                },
            },
            {
                "code": "MERITVE",
                "selection": {
                    "filter": "all",
                    "values": ["*"],
                },
            },
        ],
        "response": {
            "format": "json-stat",
        },
    }


def prenesi_podatke():
    """Prenese podatke iz baze SiStat in jih vrne kot slovar."""
    poizvedba = pripravi_poizvedbo()
    odgovor = requests.post(URL, json=poizvedba)

    if odgovor.status_code != 200:
        print("Pri prenosu podatkov je prišlo do napake.")
        print("Statusna koda:", odgovor.status_code)
        return None

    return odgovor.json()


def shrani_surove_podatke(podatki):
    """Shrani odgovor API-ja v datoteko JSON."""
    os.makedirs(MAPA_PODATKI, exist_ok=True)
    with open(SUROVI_PODATKI, "w", encoding="utf-8") as datoteka:
        json.dump(podatki, datoteka, ensure_ascii=False, indent=2)


def kategorije(dataset, koda):
    """Vrne pare (koda, ime) v pravilnem vrstnem redu."""
    kategorija = dataset["dimension"][koda]["category"]
    indeksi = kategorija["index"]
    imena = kategorija["label"]

    kode = sorted(indeksi, key=indeksi.get)
    return [(koda_vrednosti, imena[koda_vrednosti]) for koda_vrednosti in kode]


def pretvori_v_vrstice(podatki):
    """Pretvori JSON-stat podatke v seznam slovarjev."""
    dataset = podatki["dataset"]

    meseci = kategorije(dataset, "MESEC")
    obcine = kategorije(dataset, "OBČINE")
    drzave = kategorije(dataset, "DRŽAVA")
    meritve = kategorije(dataset, "MERITVE")

    vrstice = []
    kazalec = 0

    for mesec_koda, mesec_ime in meseci:
        for obcina_koda, obcina_ime in obcine:
            for drzava_koda, drzava_ime in drzave:
                for meritev_koda, meritev_ime in meritve:
                    vrednost = dataset["value"][kazalec]

                    vrstice.append({
                        "mesec": mesec_ime,
                        "obcina": obcina_ime,
                        "drzava": drzava_ime,
                        "meritev": meritev_ime,
                        "vrednost": vrednost,
                    })

                    kazalec += 1

    return vrstice


def shrani_csv(vrstice):
    """Shrani očiščene podatke v CSV."""
    os.makedirs(MAPA_PODATKI, exist_ok=True)

    glava = ["mesec", "obcina", "drzava", "meritev", "vrednost"]

    with open(CSV_PODATKI, "w", encoding="utf-8", newline="") as datoteka:
        pisec = csv.DictWriter(datoteka, fieldnames=glava)
        pisec.writeheader()
        pisec.writerows(vrstice)


def main():
    podatki = prenesi_podatke()

    if podatki is None:
        return

    shrani_surove_podatke(podatki)
    vrstice = pretvori_v_vrstice(podatki)
    shrani_csv(vrstice)

    print("Podatki so uspešno preneseni.")
    print("Število vrstic:", len(vrstice))
    print("CSV datoteka:", CSV_PODATKI)


if __name__ == "__main__":
    main()
