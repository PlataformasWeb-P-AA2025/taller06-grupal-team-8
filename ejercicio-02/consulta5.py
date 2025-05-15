from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from genera_base import Pais

engine = create_engine('sqlite:///ejercicio2.db')
Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).filter(
    or_(
        Pais.nombre.like('%uador%'),
        Pais.capital.like('%ito%')
    )
).all()

for pais in paises:
    print(f"{pais.nombre} - Capital: {pais.capital}")
