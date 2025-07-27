# Pedir nombre por pantalla
nombre = input("Introduce tu nombre de usuario: ")

# Solucionar nombre mal escrito por el usuario
nombre = nombre.replace(".", "")
nombre = nombre.replace("#", "")

# Variables con nombres de  los usuarios
usuario_1 = "alejandro"
usuario_2 = "naomi"
usuario_3 = "sergio"

# Comprobar si el nombre coincide con el de usuarios
# Si coincide entonces damos bienvenida al usuario
if nombre.lower() == usuario_1 or nombre.lower() == usuario_2 or nombre.lower() == usuario_3:
    print("¡Bienvenido", nombre.title(), "!")
# Si no damos bienvenida generica
else:
    print("¡Bienvenido usuario invitado!")


# Pedir nombre

nombre = input('Carga tu nombre!!!!!!!!')

# variables con nombres de los usuarios

usuario_4 = "Chiche"
usuario_5 = "Cachito"
usuario_6 = "Raulio"

# comparamos nombres ingreados con nombres de variables

if nombre.lower == usuario_4 or nombre.lower == usuario_5 or nombre.lower == usuario_6:
    print('Bienvenido', nombre.title, "!")
else:
    print('Bienvenido!')



# Si coincide el nombre damos bienvenida al usuario

# Si no damos la generica