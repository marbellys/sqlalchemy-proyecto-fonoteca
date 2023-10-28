#Hacer consultas a la BD
from modelo.cancion import Cancion
from modelo.albun import Albun,Medio
from modelo.interprete import Interprete
from modelo.albuncancion import AlbunCancion
from modelo.declarative_base import Session, engine, Base

if __name__ =='__main__':
        session = Session()
        # int interpre =[]
        canciones =  session.query(Cancion).all()
        print('Las canciones almacenadas son:')
        for cancion in canciones:
             
                print('titulo:'+ cancion.titulo+' (00:'+
                str(cancion.minutos)+':'+
                str(cancion.segundos)+')')

                print('Interpretes')
                for interprete in cancion.interpretes:
                    print('-'+interprete.nombre)
                    
                for albun in cancion.albunes:
                    print(' presente en el albun: '+albun.titulo)
                    
                print('')
        
        print('Los albums almacenaos en DISCO son:')
              
        albunes =  session.query(Albun).filter(Albun.medio==Medio.DISCO).all()
        for albun in albunes:
            print('Albun: '+ albun.titulo)         
        
        session.close()