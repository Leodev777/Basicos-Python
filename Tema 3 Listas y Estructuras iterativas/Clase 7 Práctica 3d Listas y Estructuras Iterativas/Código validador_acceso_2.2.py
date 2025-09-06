'''
Supongamos que eres un administrador de sistemas 
y necesitas validar el acceso de los usuarios a 
un sitio web. Crea un script que verifique si el 
+nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos.

'''

# lista de usuarios y contraseñas válidos
usuarios = ["admin", "usuario1", "usuario2"]
# lista de contraseñas válidas
passwords = ["admin123", "pass1", "pass2"]

# pedir al usuario que ingrese su nombre de usuario
usuario = input("Ingresa tu usuario: ")
# pedir al usuario que ingrese su contraseña
password = input("Ingresa tu contraseña: ")

# recorrer la lista de usuarios y contraseñas
# con while debemos inicialirzar la variable
autorizado = False

x = 0
while x < len(usuarios):
    print(usuarios[x], passwords[x])
    if usuario == usuarios[x] and password == passwords[x]:
        autorizado = True
    x = x + 1
    
if autorizado == True:
    print("Acceso autorizado")
else:
    print("Acceso no autorizado")