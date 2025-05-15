import requests
import json

url = "https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json"
respuesta = requests.get(url)
datos = respuesta.json()
estructura_final = {"docs": datos}

with open("data/data.json", "w", encoding="utf-8") as archivo:
    json.dump(estructura_final, archivo, ensure_ascii=False, indent=4)

