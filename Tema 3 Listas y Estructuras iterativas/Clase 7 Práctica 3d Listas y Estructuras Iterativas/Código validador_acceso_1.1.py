'''
validar el acceso de los usuarios a un sitio web. crear un script que verifique
s el nombre de usuario y la contraseña son correctos, y permite el acceso
solo si ambos son validos.

'''

# Lista de usuarios

usuarios = ["administrador", "pepe", "manuel", "ana", "antonio"]

# Lista de contraseñas

contra = ["admin123", "pepe123", "manuel123", "ana123", "antonio123"]

# Pedir al usuario ingresar el nombre de usuario y la contraseña

input_usuario = input("Ingresar nombre de usuario: ")
input_contra = input("Ingresar contraseña: ")

# Recorrer la lista de usuarios y contraseñas con un bucle

autorizacion = False

for x in range(len(usuarios)):
    if usuarios[x] == input_usuario and contra[x] == input_contra:
        autorizacion = True
    if autorizacion:
        print("Acceso permitido")
    else:
        print("Acceso denegado")
        

