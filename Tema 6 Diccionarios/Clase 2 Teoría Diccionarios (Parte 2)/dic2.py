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

usuarios3_puntuacion = usuarios[2]['puntuacion']
print(usuarios3_puntuacion)