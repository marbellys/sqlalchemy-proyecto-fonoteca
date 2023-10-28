# Marbellys Campos

#Se define la clase Albun
import enum
from sqlalchemy import Column, Integer, String,Enum
from modelo.declarative_base import   Base
from sqlalchemy.orm import relationship

class Medio(enum.Enum):
   DISCO = 1
   CASETE = 2
   CD = 3


class Albun(Base):
    __tablename__ = 'albun'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    ano = Column(Integer)
    descripcion =Column(String)
    medio = Column(Enum(Medio))
    
    #otraforma
    #medio = Column(Enum( MedioDISCO = 1, CASETE = 2,CD = 3 ))
    
    #la relación uno a muchos de Album a AlbumCancion, se utiliza una propiedad llamada canciones
    #la cual se crea como una relación con la palabra relationship, y a continuación se especifica 
    # la clase con la cual se relaciona, y como enlace secundario el nombre de la propiedad tablename 
    # de AlbumCancion
    #RelacioN N--N  (albun-- cancion) se crea tabla intermedia albun-cancion
    canciones = relationship('Cancion',secondary='albun_cancion')
    