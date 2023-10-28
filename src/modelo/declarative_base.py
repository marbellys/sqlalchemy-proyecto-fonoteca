# Marbellys Campos

# Definición de motor, sesión y base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Para interactuar con una base de datos
#engine = create_engine('sqlite:///baseDeDatos.sqlite')
#engine = create_engine('sqlite:///aplicacion.sqlite')

# CSG
#engine = create_engine('postgresql://postgres:postgres@10.10.3.132:5432/sqlalchemy', echo=False)

#casa
engine = create_engine('postgresql://postgres:postgres@localhost:5432/fonoteca', echo=False)       

#Para definir la sesión, permitirá crear los objetos para cada sesión y realizar el almacenamiento y recuperación de los datos. 
Session = sessionmaker(bind=engine)

#crear una clase Base, de la cual heredarán las clases del diagrama presentado con el propósito
#de definir las propiedades a almacenar sobre la base de datos, y sobre la que se definirá el
#dialecto con el cual se traducirán las consultas en la base de datos
Base = declarative_base()


