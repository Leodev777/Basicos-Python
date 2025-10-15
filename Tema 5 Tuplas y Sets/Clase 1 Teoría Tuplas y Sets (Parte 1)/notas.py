# Tuplas: Que son y como funcionan

# Estructura de datos:

# 1. Listas: (in-built: vienen dentro de python) son mutables, es decir, se pueden modificar despues de su creacion
# 2. Arrays: (se importan modulos) son similares a las listas, pero solo pueden contener el mismo tipo de dato
# 3. Tuplas: son inmutables, es decir, no se pueden modificar despues de su creacion

# Cuales son las estructuras de datos in built de python?
# 1. Listas
# 2. Tuplas
# 3. Diccionarios
# 4. Sets

# TUPLAS: LISTAS INMUTABLES
# 1. No permiten añadir, eliminar o mover elementos ( append, remove)
# 2. Permiten extraer porciones pero eso da como resultado una nueva tupla
# 3. Permite comprobar si un elemento se encuentra en la tupla

# Sn mas rapidas que las listas
# Ocupan menos espacio (Mayor optimizacion de memoria)
# Pueden usarse como llaves de un diccionario

# Sintaxis de una Tupla!

mi_tupla_1 = ("fruta", 45, True)
print(type(mi_tupla_1))

# Accerder a los emelementos de una tupla

mi_tupla_1 = ("verdura", 45, True)
print(mi_tupla_1[0])

# Lista VS Tupla VS Array

# Lista: Mutabilidad (si), Acceso a lementos (Por indice), Tamaño de la lista (dimanico), Tipo de elemento(puede contener diferentes tipos), Eficiencia ( no tan eficiente como los array o las tuplas), Uso principal (cuando se requiere modificar listas con frecuencia)
# Array: Mutabilidad (no), Acceso a elementos (Por indice), Tamaño de la lista (fijo), Tipo de elemento (debe ser el mismo tipo), Eficiencia (muy eficiente), Uso principal (cuando se requiere un alto rendimiento y se conoce el tamaño de antemano) 
# Tupla: Mutabilidad (no), Acceso a elementos (Por indice), Tamaño de la lista (fijo), Tipo de elemento (puede contener diferentes tipos), Eficiencia (mas eficiente que las listas), Uso principal (cuando se requiere una coleccion inmutable de elementos)

# Como pasamos de una lista a una tupla?

mi_lista = [1,2,3,4,5,6, "hola mundoxd", True]
print("mi tipo de lista es: ", type(mi_lista))

mi_tupla = tuple(mi_lista)
print("mi tipo de tupla es: ", type(mi_tupla))

# De tupla a lista

mi_tupla = (1,2,3,4,5,6, "hola riky xd", True)
print("mi tipo de tupla es: ", type(mi_tupla))
mi_lista = list(mi_tupla)
print("mi tipo de lista es: ", type(mi_lista))

# como trabajamos y que podemos hacer?
# accedemos a lementors a traves de su indice
# podermos hacer SLICING (tomar de un indice a cierto indice, creamos subtuplas)

mi_nueva_tupla = (1,2,3,4,5,6,7,8,9,10)
print("quiero accerder el 3 al 5: ", mi_nueva_tupla[2:5])
print("La longitud de la tupla es :",len(mi_nueva_tupla))

# Buscar apariciones dentro de una tupla
# apariciones = mi_nueva_tupla.count(5)
# print("El numero de apariciones del 5 es: ", apariciones)

# tambien podemos pedir los indices
# maximo = max(mi_nueva_tupla)
# minimo = min(mi_nueva_tupla)