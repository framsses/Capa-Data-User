import os
from dotenv import load_dotenv
from logger_base import log
from psycopg2 import pool
import sys

load_dotenv()


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = os.getenv('USERNAME')
    _PASSWORD = os.getenv('PASSWORD')
    _DB_PORT = '5432'
    _HOST = os.getenv('HOST') # local host used to test
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, 
                                                    host = cls._HOST, 
                                                    user = cls._USERNAME, 
                                                    password = cls._PASSWORD, 
                                                    port = cls._DB_PORT, 
                                                    database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obteber el pool {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenidad de pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')
    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool.closeall()
    
if __name__ == '__main__':
    # Test connection
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()

