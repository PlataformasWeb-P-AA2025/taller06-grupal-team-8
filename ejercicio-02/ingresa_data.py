from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from genera_base import Pais

engine = create_engine('sqlite:///ejercicio2.db')
Session = sessionmaker(bind=engine)
session = Session()

with open("data/data.json", "r", encoding="utf-8") as archivo:
    datos_json = json.load(archivo)

documentos = datos_json["docs"]

for d in documentos:
    pais = Pais(
        nombre=d.get("CLDR display name"),
        capital=d.get("Capital"),
        continente=d.get("Continent"),
        dial=d.get("Dial"),
        geoname_id=str(d.get("Geoname ID")),
        itu=d.get("ITU"),
        lenguajes=d.get("Languages"),
        es_independiente=d.get("is_independent")
    )
    session.add(pais)

session.commit()
print("Todos los países fueron insertados correctamente.")
