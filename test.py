import pandas as pd
import requests
from bs4 import BeautifulSoup


payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label": "Médecin généraliste",
    "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements",
}

url = "http://annuairesante.ameli.fr/recherche.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
}

req = requests.Session()
page = requests.post(url, params=payload, headers=header)

if page.status_code == 200:
    search_url = page.url

soup = BeautifulSoup(page.text, 'html.parser')
doctors = soup.find_all("div", class_="item-professionnel")
infos = []
for doctor in doctors:
    id = doctor.find("span", class_="num").text
    name = doctor.find("h2", class_="ignore-css").text.strip()
    # tel = doctor.find("div", class_="tel").text.strip()
    address = doctor.find("div", class_="adresse").text.strip()

    infos.append({"id": id, "name": name, "address": address})
    # infos.append({"id": id, "name": name, "address": address, "tel": tel})

    df = pd.DataFrame(infos)
    df.to_csv("all_doctors.csv", index=False)
