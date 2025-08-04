
# Otra forma de solicitar una contraseña al usuario
# hasta que sea correcta, utilizando un bucle infinito.
password = "Secreto"
while True:
    password_input = input("Introduce la contraseña: ")
    if password_input == password:
        print("Contraseña correcta, acceso concedido.")
        break
    else:
        print("Contraseña incorrecta, acceso denegado.")