# Marbellys Campos

#Se define la clase Canción
from sqlalchemy import Column, Integer, String
from modelo.declarative_base import   Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Interprete(Base):
    __tablename__ = 'interprete'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    cancion = Column(Integer, ForeignKey('cancion.id'))