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

# como odenar elementos de una tupla revertirlos? Recordemos que sorted ordena pero si lo utilizamos para tuplas retorna una lista para eso lo debemos utilizar de la siguiente manera

la_tupla = (2,3,4,5,7,4,2,2,3,5,3,3,4,6,3,2,34,4,2,3,4,2,3,4,6,6,6,6,2,3,4)
tupla_ordenada = tuple(sorted(la_tupla))
print(type(tupla_ordenada))
print("tupla ordenada ", tupla_ordenada)

tupla_2 = (1,3,5,7,2,3,4,6,2,2,2,2,2,2)
tupla_2 = tuple(reversed(sorted(tupla_2)))
print("tupla 2 ordenada de mayor a menor: ", tupla_2)

# Combinacion de tuplas fromando una tupla de tuplas

tupla_a = (1,2,3)
tupla_b = ('a', 'b', 'c')
tupla_combinada = tuple(zip(tupla_a, tupla_b))
print(tupla_combinada)

# accerder a los elementos de una tupla de tuplas

la_re_tupla = ((1, 'a'), (2, 'b'), (3, 'c'))

print(la_re_tupla[0][0])  # primer elemento del primer par -> 1
print(la_re_tupla[1][1])  # segundo elemento del segundo par -> 'b'
print(la_re_tupla[2][0])  # primer elemento del tercer par -> 3


# SLICING de una tupla de tuplas

tuplaa = ((2,3,4), (4,5,6), (7,8,9))

# slicing de una tupla interior
tupla_interior = mi_tupla[1]
print(tupla_interior) # salida: 4,5,6

# Slicing de una porcion de la tupla de tuplas

porcion_tupla = mi_tupla[0:2]
print(porcion_tupla) # salida: ((2,3,4), (4,5,6))

# Slicing de una porcion de una tupla interior

# porcion_interior = mi_tupla[1][0:2] # lo que hacemos es accerder a la tupla interior y luego hacer slicing
# print(porcion_interior) # salida: (4,5)

# Tuplas unitarias

tupla_unitaria = (5) # tipo entero
print(type(tupla_unitaria))

tupla_unitaria = (5,) # tipo tupla añadimos esta , para que interpete que es una tupla
print(type(tupla_unitaria))
print(tupla_unitaria)

# Epaquetamiento y desempaquetamiento de tuplas

# empaquetado
# consiste en vez de poner parentesis, siplemente separar los elemntos por comas y python lo interpreta como una tupla
tutupla = "pizza", 12, True
print(tutupla)

# salida: ('pizza', 12, True)

# desempaquetado
# String toma el valor el primer elemento de la tupla, int el segundo y bool el tercero.
tutupla = ("pizza", 12, True)
str, int, bool = tutupla
print(str)
print(int)
print(bool)

# salida: pizza, 12, True