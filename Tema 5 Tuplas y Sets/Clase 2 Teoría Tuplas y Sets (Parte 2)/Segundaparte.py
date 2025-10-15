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

