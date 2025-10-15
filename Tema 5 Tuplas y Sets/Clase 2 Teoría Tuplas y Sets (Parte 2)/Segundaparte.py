# Sets Que es?
# Def: Colecciones no ordenadas de elementos unicos e inmutables.

# Los elementos no llevan un indice asociado
# No podemos reasignar valores a los elementos del set
# Podemos añadir y borrar elementos
# Los elementos son unicos, no hay duplicados

# SINTAXIS DE SET
mi_set = {'fantasma', 45, True}
print(mi_set)

# Tupla:
tupla = ('fantasma', 45, True)
print(type(tupla))

# Lista:

mi_lista = ['fantasma', 23, True]
print(type(mi_lista))


# Tenemos que tener cuidado con el siguiente ejemplo para crear un set vacion y no crear un diccionario, esto lo vamos a ver mas adalante

set_vacio = () # Forma de crear un set vacio
print(type(set_vacio))

# salida: <class 'set'>
mi_set = {}
print(type(mi_set))

# Salida: <class 'dict'>

# Los set no preservan el orden de los elementos y los elementos no llevan un indice asociado, tampoco se pueden repetir tampoco podemoss
# reasignar valores a los elementos del set


# QUE PODEMOS HACER CON LOS SETS?
# podemos comprobar pertenetencias ejemplo
print('fantasma' in mi_set) # vemos si fantasta esta en el set
# esto es mucho mas eficientes que las listas porque?

# Los elementos en una lista tienen asociado un indice ----------> Para comprobar la pertenencia se recorren todos los elementos de la lista hasta encontrar o no el coincidente
# Los elementos en un set no tiene un indice si no un HASH
# (Un set es una hash table o tabla de hash) ---------> Python comprueba si el bucket correspondiente a ese set y ve si esta lleno o no.
# El hash es unico para acada elemento, de manera que a ese elemento siempre va a estar guardado en el mismo lugar dentro de ese set(en el mismo "bucket")
# bucket es: un espacio de memoria reservado para guardar un elemento


# Podemos añadir y borrar elementos de un set

# Añadir:

frutas = {'manzana', 'naranja', 'pera'}
frutas.add('kiwi')
print(frutas)
# salida: naranja, kiwi, manazana, pera
# recordemos que no respeta orden

# Borrar:
frutas = {'manzana', 'naranja', 'pera'}
frutas.discard('kiwi')
print(frutas)

# Salida: manazana, pera, naranja

# tenemos dos metodos remove y discard
# la diferencia intento borrar algo que no esta con remove da error
# si embargo con discard no da error


# Tambien PODEMOS PASAR DE LISTAS A SETS

mi_lista = ['manzana', 'pera', 'naranja']
print(type(mi_lista))
# salida_ lista
mi_set = set(mi_lista)
print(type(mi_set))
# salida: set

# Union de conjuntos

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2) 
print(set.union(set2))

# salida: 1, 2, 3, 4, 5

# Interseccion de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)
print(set.intersection(set2))

# salida: 3

# Diferencia de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 - set2)
print(set.difference(set2))

# salida: 1, 2
# Basicamente estoy pidiendo que me muestre los elementos que estan en el set1 pero no en el set2

# Diferencia simetrica
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 ^ set2)
print(set.symmetric_difference(set2))

# salida: 1, 2, 4, 5
# lo que esta haciendo es mostrarme los elementos que estan en el set1 y no el set2 y los elementos
# que estan el set2 y no en el set1

# salida: 1, 2, 4, 5
