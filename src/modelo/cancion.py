# Marbellys Campos

#Se define la clase Canción
from sqlalchemy import Column, Integer, String
from modelo.declarative_base import   Base
from sqlalchemy.orm import relationship

class Cancion(Base):

    __tablename__ = 'cancion'
    id = Column(Integer,primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    
    #Cancion tiene una relación de uno a muchos la clase Interprete
    #los intérpretes asociados a una canción deberían ser borrados cuando se elimina la canción, 
    #Relacion 1--N (cancion -- interprete)
    interpretes = relationship('Interprete', cascade = 'all,delete,delete-orphan')
    
    #RelacioN N--N (albun-- cancion) se crea tabla intermedia albun-cancion
    albunes = relationship('Albun', secondary='albun_cancion')
