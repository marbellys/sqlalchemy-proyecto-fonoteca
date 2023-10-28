# Marbellys Campos

#Se define la clase Canción
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from modelo.declarative_base import Session, engine, Base
from modelo.cancion import Cancion
from modelo.interprete import Interprete
from modelo.albuncancion import AlbunCancion
from modelo.albun import Albun


if __name__ == '__main__':
    session = Session()
    
    cancion2 = session.query(Cancion).get(2)
    
    print("Se eliminara la cancion: "+ cancion2.titulo + ", escrita por: "+ cancion2.compositor)
    session.delete(cancion2)
    session.commit()
    session.close()
    
    