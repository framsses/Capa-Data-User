from sqlite3 import Cursor
from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:
    '''
    DAO - Data Access Objetct for the User Table
    CRUD - Create - Read - Update - Delete for the User Table
    '''

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username,password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            log.debug('Users Selected')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insert(cls, user):
        with CursorDelPool() as cursor:
            log.debug(f'Insert User: {user}')
            valores = (user.username,  user.password)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def update(cls, user):
        with CursorDelPool() as cursor:
            log.debug(f'Update User: {user}')
            valores = (user.username, user.password, user.id_usuario)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount
    
    @classmethod
    def delete(cls, user):
        with CursorDelPool() as cursor:
            log.debug(f'Delete User: {user}')
            valores = (user.id_usuario,)
            cursor.execute(cls._DELETE, valores)
            return cursor.rowcount
