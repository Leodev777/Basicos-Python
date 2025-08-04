'''Escribit un programa que almacene la cadena
de caracteres contraseña en una variable, pregunte al
usuario por la contraseña hasta que introduzca
la contraseña correcta.
'''

# Contraseña guardada

password = "Secreto"
password_input = ""

# Bucle para perdir la contraseña

# out: contraseña correcta
while password_input != password: # mientras la contraseña introducida no sea igual a la guardada
    password_input = input("Introduce la contraseña: ") # pedir contraseña al usuario
if password_input != password: # si la contraseña introducida no es igual a la guardada
    print("Contraseña incorrecta, acceso denegado.") # mensaje de error (Que el bucle no deveria tocar)

print("Contraseña correcta, acceso concedido.") # mensaje de éxito
# Fin del programa