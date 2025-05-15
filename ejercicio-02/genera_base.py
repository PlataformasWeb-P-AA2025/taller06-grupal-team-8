from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///ejercicio2.db')
Base = declarative_base()

class Pais(Base):
    __tablename__ = 'paises'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)          
    capital = Column(String)        
    continente = Column(String)      
    dial = Column(String)            
    geoname_id = Column(String)     
    itu = Column(String)             
    lenguajes = Column(String)       
    es_independiente = Column(String) 

Base.metadata.create_all(engine)

