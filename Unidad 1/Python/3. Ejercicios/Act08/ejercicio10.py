from CreaUsuario import CreaUsuario

listaUsuarios = [['Pedro', ['Rodriguez', 'Saavedra']],['Iker', ['Fernandez', 'Ochoa']],['Carlos', ['Izu', 'Rodriguez']],['Paco', ['Rodriguez', 'Ochoa']]]
usernames = []
for usuario in listaUsuarios:
    usuarioCreado = CreaUsuario(usuario)
    usernames.append(usuarioCreado.crearUsuario())

print("Lista de usuarios: ", usernames)