from modelo.cancion import Cancion
from modelo.albun import Albun, Medio
from modelo.interprete import Interprete
from modelo.albuncancion import AlbunCancion
from modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()
    cancion = session.query(Cancion).get(2)
    interprete = session.query(Interprete).get(1)
    
    print('cancion a modificar: '+ cancion.titulo)
    print('interprete a modificar: '+ interprete.nombre)
    
    cancion.titulo = 'Ojos Verdosos'
    cancion.minutos =10
    
    
    #La cancion 2 se le asocia a interprete cod id 1 ( en la tabla interprete) 
    cancion.interpretes.append(interprete)
    
    session.add(cancion)
    session.commit()
    session.close()