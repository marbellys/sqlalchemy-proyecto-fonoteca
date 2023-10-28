# Marbellys Campos

#Se define la clase Canción
from sqlalchemy import Column, Integer, String
from modelo.declarative_base import   Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class AlbunCancion(Base):
    __tablename__ = 'albun_cancion'
    
    #se crea como una columna que hace referencia al identificador de Album
    # Ademas, por cada clase a "mapear" en la base de datos se defina una llave 
    # primaria, por lo cual, se establece que la llave primaria para esta clase son los atributos album y canción
    albun   = Column(Integer, ForeignKey('albun.id'),primary_key = True)
    
    cancion = Column(Integer, ForeignKey('cancion.id'),primary_key = True)