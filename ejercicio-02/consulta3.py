from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///ejercicio2.db')
Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

for pais in paises:
    print(f"{pais.nombre}: {pais.lenguajes}")
