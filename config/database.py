import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = 'database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

# Se pasa como parametro la cadena de conexion a la base de datos
engine =create_engine(database_url)

Session = sessionmaker(bind=engine)

# Metodo que nos permite mapear los modelos
Base = declarative_base()