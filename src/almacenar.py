from modelo.cancion import Cancion
from modelo.albun import Albun, Medio
from modelo.interprete import Interprete
from modelo.albuncancion import AlbunCancion
from modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    #creamos la BD
    Base.metadata.create_all(engine)

    #Abrimos una session
    session = Session()
    
    #crear registros de Interpretes
    interprete1 = Interprete(nombre = "Shakiras" )
    interprete2 = Interprete(nombre = "Lazzoo" )
    interprete3 = Interprete(nombre = "JUan Gabriell" )
    interprete4 = Interprete(nombre = "Ana Gabriell" )
    
    #se añaden a la session
    session.add(interprete1)
    session.add(interprete2)
    session.add(interprete3)
    session.add(interprete4)
    
    #Otra forma
'''     session.add_all([
     Interprete(nombre = "Shakiras" ),
     Interprete(nombre = "Lazzoo" ),
     Interprete(nombre = "JUan Gabriell" ),
     Interprete(nombre = "Ana Gabriell" )
    ]) '''
     
    #realizar el almacenamiento
    session.commit()
    
    #Crear registros de Albums
    albun1 = Albun(titulo="Albun Pies descalzos l",ano=2000,descripcion='buen albun', medio=Medio.DISCO)
    albun2 = Albun(titulo="Albun El rey l",ano=1900,descripcion='buen albun', medio=Medio.CASETE)
    albun3 = Albun(titulo="mexico lindo l",ano=2003,descripcion='buen albun', medio=Medio.CD)
    albun4 = Albun(titulo="Albun Ojos marrones l",ano=2022,descripcion='buen albun de lazzo', medio=Medio.CD)
  
    session.add(albun1)
    session.add(albun2)
    session.add(albun3)
    session.add(albun4)
    session.commit()
    
    #crear registros de  canciones 
    cancion1 = Cancion(titulo = "Pies descalzos", minutos = 3, segundos = 1, compositor = "Samuel Torres")
    cancion2 = Cancion(titulo = "Ojos marrones", minutos = 1, segundos = 5, compositor = "Lazzo ")
    cancion3 = Cancion(titulo = "guaca guaca", minutos = 3, segundos = 1, compositor = "shakira")
    cancion4 = Cancion(titulo = "El rey", minutos = 3, segundos = 1, compositor = "Alejandro")
    
    session.add(cancion1)
    session.add(cancion2)
    session.add(cancion3)
    session.add(cancion4)
    session.commit()
        
    #relacionar albun con canciones
    albun1.canciones = [cancion1,cancion3]
    albun2.canciones = [cancion4]
    albun3.canciones = [cancion4]
    albun4.canciones = [cancion2]
        
    #relacionar caciones con interpretes
    cancion1.interpretes = [interprete1]
    cancion2.interpretes = [interprete2]    
    cancion3.interpretes = [interprete1]    
    cancion4.interpretes = [interprete3]  
    session.commit()
    
    session.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    