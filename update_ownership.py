import json
import requests
from bs4 import BeautifulSoup

# Get the list of media sources
media_sources = {
    "lemonde.fr": "https://fr.wikipedia.org/wiki/Le_Monde",
    "bfmtv.com": "https://fr.wikipedia.org/wiki/BFMTV",
    "cnews.fr": "https://fr.wikipedia.org/wiki/CNews",
    "lesechos.fr": "https://fr.wikipedia.org/wiki/Les_%C3%89chos_(France)",
    "rt.com": "https://fr.wikipedia.org/wiki/RT_(t%C3%A9l%C3%A9vision)"
}

def get_media_owner(wiki_url):
    """Scrape le propriétaire du média depuis la page Wikipedia"""
    response = requests.get(wiki_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="infobox")
        if table:
            for row in table.find_all("tr"):
                header = row.find("th")
                if header and "Propriétaire" in header.text:
                    return row.find("td").text.strip()
    return "Inconnu"

# Générer un dictionnaire avec les propriétaires des médias mis à jour
ownership_data = {}
for media, url in media_sources.items():
    owner = get_media_owner(url)
    ownership_data[media] = {
        "propriétaire": owner,
        "scandales": []
    }

with open("ownership_data.json", "w", encoding="utf-8") as file:
    json.dump(ownership_data, file, indent=4, ensure_ascii=False)

print("Fichier ownership_data.json mis à jour avec succès!")