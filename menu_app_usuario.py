from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('''
Options:
1. List Users
2. Add User
3. Update User
4. Delete User
5. Exit    
    ''')
    opcion = int(input('Select Option (1-5):'))
    if opcion == 1:
        usuarios = UsuarioDAO.select()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Write username: ')
        password_var = input('Write Password: ')
        usuario = Usuario(username=username_var,password=password_var)
        usuarios_insertados = UsuarioDAO.insert(usuario)
        log.info(f'Users Inserted: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Write the user id to modify: '))
        username_var = input('Write the new username: ')
        password_var = input('Write the new password: ')
        usuario = Usuario(id_usuario_var,username_var,password_var)
        usuarios_actualizados = UsuarioDAO.update(usuario)
        log.info(f'Users Updated: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Write the user id to delete: '))
        usuario = Usuario(id_usuario_var)
        usuarios_eliminados = UsuarioDAO.delete(usuario)
        log.info(f'Users Deleted: {usuarios_eliminados}')
else:
    log.info('Exit App')