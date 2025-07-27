# Pedir contraseña al usuario
password = input("Introduce la contraseña ")

# Comprobar si la contraseña es segura
# Si cumple los requisistos diremos que es segura
# Debe tener una vocal (a,e,o)
# Debe tener un simbolo especial (*,#)
if ("a" in password or "e" in password or "o" in password) and ("*" in password or "#" in password):
     print("La contraseña es segura")
else:
    print("La constraseña no es segura")
# Si no los cumple diremos que es insegura

## --------------------------------------------------------

password = input("Introducir la contraseña, que contenga volares y simobolos * # ")

# comprobar contraseña segurda
# si coumple los requisitros diremos que es segura
# debe tener una vocal
# debe tener un simbolo especial

if ("a" in password or "e" in password or "i" in password or "o" in password or "u" in password) and ("*" in password or "#" in password):
     print("Contraseña segura")
else:
     print("Cargar contraseña con volares y simobolos")     