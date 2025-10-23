# Que venimos viendo?

# Que es un diccionario y su sintaxis
# Manipular pares clave-valor (añadir, reasignar, eliminar)
# Casos de uso
# Metodos aplicables a diccionarios
# Relacion entre listas/tuplas/sets y diccionarios

# Recorrer pares de un diccionario

user_0 = {'username': 'toto123',
          'nombre': 'Luis',
          'apllido': 'Suarez',
          }

for clave, valor in user_0.items(): # items() devuelve todos los pares clave–valor de un diccionario para poder recorrerlos o verlos juntos.
    print("Clave:", clave)
    print("Valor:", valor)
    print("")

# Desempacamos

user_0 = {'username': 'toto123',
          'nombre': 'Luis',
          'apllido': 'Suarez',
          }
print(user_0.items()) # Lista de tuplas

# -------------------

# Se crea un diccionario llamado 'programadores'
# Cada clave es el nombre de un programador y cada valor es el lenguaje que domina
programadores = {
    'juan': 'python',
    'sara': 'c',
    'eduardo': 'solidity',
    'felipe': 'python',
}

# Recorre el diccionario usando el método .items()
# En cada iteración, 'nombre' toma la clave y 'lenguaje' toma el valor asociado
for nombre, lenguaje in programadores.items():
    # .title() convierte la primera letra de cada palabra en mayúscula
    # Se construye una cadena concatenando nombre y lenguaje formateados
    print("El programador " + nombre.title() + " domina el lenguaje " + lenguaje.title() + ".")

# Salida: 
# El programador Juan domina el lenguaje Python.
# El programador Sara domina el lenguaje C.
# El programador Eduardo domina el lenguaje Solidity.
# El programador Felipe domina el lenguaje Python.

# Recorrer las claves

# Se crea un diccionario llamado 'programadores'
# Cada clave representa el nombre de un programador
# Cada valor indica el lenguaje que domina
programadores = {
    'juan': 'python',
    'sara': 'c',
    'eduardo': 'solidity',
    'felipe': 'python',
}

# Se usa el método .keys() para obtener todas las claves del diccionario
# Esto devuelve una vista iterable con los nombres de los programadores
for nombre in programadores.keys():
    # En cada iteración, 'nombre' contiene una de las claves del diccionario
    # Se imprime el nombre de cada programador
    print(nombre)


programadores = {
    'juan': 'python',
    'sara': 'c',
    'eduardo': 'solidity',
    'felipe': 'python',
}

for lenguaje in programadores.values():
    print(lenguaje)


programadores = {
    'juan': 'python',
    'sara': 'c',
    'eduardo': 'solidity',
    'felipe': 'python',
}

for lenguaje in set(programadores.values()):
    print(lenguaje)


# Aminadmiento listas de diccionarios

# tenemos una serie de usuarios. Para cada usuario tenemos un diccionario con la
# informacion de esta forma...

usuario_1 = {
    "username": "jonas",
    "nacionalidad": "peruano",
    "puntuacion": 73,
}

print(usuario_1)

# Para guardar la infomracion de todos los usuarios podemos crear una lista
# de diccionarios, donde cada diccionario guarda la
# infomraicon de cada uno de los usuarios


usuario_0 = {
    "username": "john_doe",
    "nacionalidad": "USA",
    "puntuacion": 85,
}

usuario_1 = {
    "username": "jane_doe",
    "nacionalidad": "Canada",
    "puntuacion": 92,
}

usuario_2 = {
    "username": "bob_smith",
    "nacionalidad": "UK",
    "puntuacion": 78,
}

usuarios = [usuario_0, usuario_1, usuario_2]

print(usuarios)

# Recorrer elementos de una lista de diccionarios:

usuarios3_puntuacion = usuarios[2]['puntuacion'] # 2 es el indice, puntuacion es la clave correspondiente al valor
print(usuarios3_puntuacion)

# Anidamiento Listas en diccionarios

# --- NIDAMIENTO: LISTAS DENTRO DE DICCIONARIOS ---

# Ejemplo 1: Pedido en un restaurante
# Se crea un diccionario que representa un pedido de pizza
# Tiene dos claves:
#   - 'masa': tipo de masa
#   - 'ingredientes': lista con varios ingredientes
pizza = {
    "masa": "fina",
    "ingredientes": ["aceitunas", "champiñones"]
}

# Se imprime un resumen del pedido accediendo a los valores del diccionario
print("Has pedido una pizza de masa " + pizza["masa"] + " con los siguientes ingredientes:")

# Se recorre la lista almacenada en la clave 'ingredientes'
for ingrediente in pizza["ingredientes"]:
    print(ingrediente)

# Resultado:
# Has pedido una pizza de masa fina con los siguientes ingredientes:
# aceitunas
# champiñones


# Ejemplo 2: Trabajadores en una compañía
# Se crea un diccionario llamado 'programadores'
# Cada clave es el nombre de un trabajador
# Cada valor es una lista con los lenguajes que domina
programadores = {
    "juan": ["python", "c++"],
    "sara": ["c", "rust"],
    "eduardo": ["solidity", "fortran"],
    "felipe": ["python", "fortran", "r"]
}

# Se recorre el diccionario usando .items() para obtener clave y valor
for nombre, lenguajes in programadores.items():
    # Se imprime el nombre del programador formateado
    print("\n" + nombre.title() + " sabe usar los lenguajes:")
    
    # Luego se recorre la lista de lenguajes de cada programador
    for lenguaje in lenguajes:
        print(lenguaje.title())

# Resultado:
# Juan sabe usar los lenguajes:
# Python
# C++
#
# Sara sabe usar los lenguajes:
# C
# Rust
#
# Eduardo sabe usar los lenguajes:
# Solidity
# Fortran
#
# Felipe sabe usar los lenguajes:
# Python
# Fortran
# R



# Anidamientos de DICCIONARIOS EN DICCIONARIOS:

userrs = {
    'vene':{
        'nombre': 'lucas',
        'apellido': 'varela',
        'ubicacion': 'alemania'
    },
    'crodri':{
        'nombre': 'roberto',
        'apellido': 'garcia',
        'ubicacion': 'peru'
    },
    'bros':{
        'nombre': 'daniel',
        'apellido': 'pereyra',
        'ubicacion': 'bolivia'
    }
}

# Diccionario de usuarios con información personal
users = {
    'lvene': {
        'nombre': 'Lucas',
        'apellido': 'Vene',
        'ubicacion': 'Paris'
    },
    'crodriguez': {
        'nombre': 'Carlos',
        'apellido': 'Rodríguez',
        'ubicacion': 'Madrid'
    },
    'tbauer': {
        'nombre': 'Thomas',
        'apellido': 'Bauer',
        'ubicacion': 'Berlin'
    }
}

# Iterar a través de cada usuario en el diccionario
for username, user_info in users.items():
    # Imprimir el nombre de usuario
    print("\nUsername: " + username)
    
    # Combinar nombre y apellido para crear el nombre completo
    full_name = user_info['nombre'] + " " + user_info["apellido"]
    
    # Obtener la ubicación del usuario
    ubicacion = user_info["ubicacion"]
    
    # Imprimir la información formateada del usuario
    print("\tNombre completo: " + full_name.title())
    print("\tUbicacion: " + ubicacion.title())