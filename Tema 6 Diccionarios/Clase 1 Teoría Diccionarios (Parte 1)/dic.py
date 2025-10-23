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

# Metodos especificos para diccionarios
# Luego tenemos metodos que no son especificos pero los podemos usar en los diccionarios

# Keys():

diccionario_x = {'pera': 1, 'manzana': 2, 'toronja': 3}
print(diccionario_x.keys()) # salida dict_keys(['pera', 'manzana', 'toronja'])

# Get():

diccionario_xx = {'pera': 1, 'manzana': 2, 'toronja': 3}
print(diccionario_xx.get('manzana')) # Salida 2
print(diccionario_xx.get('wiki')) # Salida none

# si buscamos una clave que no existe con los corchetes nos
# dara un error keyerror

# diccionario_xx = {'pera': 1, 'manzana': 2, 'toronja': 3}
# print(diccionario_xx['tomate']) # salida keyerror

# El metodo get tiene caracteristicas interesantes
# agregmoas el .get y la clave que me ieteresa y nos retorna el valor
# pero si introducimos una clave que no existe nos 
# retorna none
# pero podemos agregar un segundo parametro al get
# que seria el valor por defecto en caso de que la clave no
# exista
# EJ: 

diccionario_xx = {'pera': 1, 'manzana': 2, 'toronja': 3}
print(diccionario_xx.get('manzana')) # Salida 2
print(diccionario_xx.get('wiki',0)) # salida 0

# devuelve el valor de una clave en un diccionario.
# Si la clave no existe, devuelve un valor predeterminado
# en este caso 0 en lugar de generar un error.


# Ahora metodos que ya conocemos pero aplicados a los diccionarios
# Pop():
# Elimina y devuelve el valor de una clave en un diccionario

diccionarioo = {'pera': 1, 'manzana': 2, 'toronja': 3}
valorrr = diccionarioo.pop('manzana')
print(diccionarioo)
print(valor)

# pop no solo elimina sino que tambien guarda



# DE TUPLAS A DICCIONARIOS
# Sintaxis:
key1 = 'tateti'
value1 = 0
key2 = 'tateta'
value2 = 0
key3 = 'tateto'
value3 = 0
mis_tuplass = [(key1, value1), (key2, value2), (key3, value3)]
my_dicc = dict(mis_tuplass) # Lista de tuplas

# Ejemplo:

eventos = [('2025-01-01', 100),
           ('2025-05-02', 85),
           ('2025-02-03', 10),
            ]
eventos_dict = dict(eventos)
print(eventos_dict)

# IMPORTANTE: Si hay dos tuplas con la misma clave
# en la lista de tuplas, solo se conservara la ultima tupla.
# Es decir, el valor de la clave correspondiente sera el valor
# de la utlima tupla en la lista.

# DE LISTAS A DICCIONARIOS
# zip(): función built-in que devuelve un iterador de tuplas
# Cada tupla contiene elementos en la misma posición de varios iterables

# Ejemplo general
keys = ['key1', 'key2', 'key3']
values = ['value1', 'value2', 'value3']

# zip une las dos listas en pares (clave, valor)
# dict convierte esas tuplas en un diccionario
mi_dict = dict(zip(keys, values))
print("Diccionario general:", mi_dict)

# Ejemplo práctico
materias = ['mate', 'history', 'filosofia']
notas = [8.5, 7.0, 10]

# Une materias con sus notas correspondientes
notas_dict = dict(zip(materias, notas))
print("Diccionario de notas:", notas_dict)

# Resultado esperado:
# Diccionario general: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# Diccionario de notas: {'mate': 8.5, 'history': 7.0, 'filosofia': 10}
# La funcion ZIP() combina las dos listas
# materias y notas en una lista de tuplas
# de elementos correspondientes, y leugo el
# constructor de diccionarios dict() crea un
# diccionario a partir de esta lista de tuplas.

# Importante: AMBAS LISTAS DEBEN TENER LA MISMA LONGITUD
# EN OTRO CASO SOLO COPIARA HASTA LA LOGITUD DE LA LISTA MAS CORTA


# De SET A DICCIONARIO
# Sintaxis
my_set = {('key1', value1), ('key2', value2), ('key3', value3)}
mi_dictt = dict(my_set)

# Ej:

notas_set = {('mate', 7.0), ('historia', 3.0), ('lengua', 9.0)}
notas_dict = dict(notas_set)
print(notas_dict)
