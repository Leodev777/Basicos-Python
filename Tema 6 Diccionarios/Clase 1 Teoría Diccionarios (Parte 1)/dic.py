# vemos a ver los diccionarios! esta estructura es in built en python
# los diccionarios son colecciones de datos que almacenan pares de clave:valor
# se definenn con llaves {}
# las claves deben ser unicas e inmutables (strings, numero, tuplas)
# los valores pueden ser de cualquier tipo de dato

# DEFINICION DE UN DICCIONARIO: Colecciones no ordenadas de pares CLAVE:VALOR

# Sintaxis:
mi_diccionario = {
    "correo": "contraseña", # clave:valor
    "gmail": "mi_contraseña123",
    "yahoo": "otra_contraseña456"
}

# Sintaxis

mi_diccionario_1 = {'pera': 1, 'manzana': 2, 'toronja': 3} # clave:valor 
print(mi_diccionario_1)
print(type(mi_diccionario_1))

# Diccionario vacio
diccionario_vacio = {}

# Accedemos al valor a traves de llaves

dicc = {'pera': 1, 'manzana': 2, 'toronja': 3}
print(dicc['manzana']) # accedemos al valor 2

# Modificar los valores:

dicc = {'pera': 1, 'manzana': 2, 'toronja': 3}
dicc['manzana'] = 5 # modificamos el valor de la clave 'manzana'
print(dicc)

# Agregar nuevos pares clave:valor
dicc = {'pera': 1, 'manzana': 2, 'toronja': 3}
dicc['Banana'] = 3 # agregamos un nuevo par clave:valor
print(dicc)

# Eliminar pares clave:valor

dicc = {'pera': 1, 'manzana': 2, 'toronja': 3}
del dicc['pera']
print(dicc)

# Diccionarios vacios
dicc_vacio = {}
mi_diccionario['manzana'] = 129
mi_diccionario ['pera'] = 493
mi_diccionario ['toronja'] = 129
print(mi_diccionario)
print(type(mi_diccionario))

# Metodos de diccionarios Keys()

diccionarioo = {'pera': 1, 'manzana': 2, 'toronja': 3}
print(diccionarioo.keys())

# Podemos acceder a los diccionarios de varias maneras GET

diccionarioo = {'pera': 1, 'manzana': 2, 'toronja': 3}
print(diccionarioo.get('manzana'))
print(diccionarioo.get('uva'))

# Si la clave no existe, get() devuelve None en lugar de generar un error

# Metodo Pop()
# Elimina un par clave:valor y devuelve el valor asociado a la clave
diccionarioo = {'pera':1, 'manzana':2, 'uva':5}
valor = diccionarioo.pop('manzana')
print(valor) # salida 2


# Metodo Clear() 
# Elimina todos los elementos del diccionario
diccionarioo.clear()
print(diccionarioo) # salida {}

# De TUPLAS A DICCIONARIOS
#mis_tuplas = [(key1, value1), (key2, value2), (key3, value3)]
#mi_dict = dict(mis_tuplas)
# print(mi_dict)
# Importante: Si hay dos tuplas con la misma clave en la lista
# de tuplas, solo se conservara la ultima tupla.
# Es decir, el valor de la clave correspondiente sera el valor de la ultima
# tupla en la lista.

# Casos de uso comunes:
# Diccionario con infomraciones diversas sobre un objeto:

persona = {'edad': 23, 'altura': 1.60, 'nombre': 'Ana', 'ciudad': 'Atlantis'}
edad = persona['edad']
print(edad) # salida 23

# Diccionario con un tipo de infomracion sobre varios objetos:

lenguaje_programacion = {"Juan": "Python", "Pedro": "Java", "Maria": "C++"}
lenguajes_de_juan = lenguaje_programacion["Juan"]
print(lenguajes_de_juan) # Salida python

# BUENAS PRACTICAS: en este caso escribimos los fragmentos de codigo para que lo podamos ver de mejor manera pero
# en un script aplicando las buenas practicas se veria asi:

persona = {
      'edad': 23,
      'altura': 1.60,
      'nombre': 'Ana',
      'ciudad': 'Atlantis',
      'DNI': '20987456', # Esta ultima coma es una buena practica
      }                    # al igual que la esctructura
edad = persona['edad']
print(edad) # salida 23


