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
