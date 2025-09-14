# El sentido principarl de convertir listas en arrays es por
# una cuestion de eficiencia y velocidad

# sabemos que en las listas podemos tener diferentes tipos de datos
# booleanos, entetos, strings, etc vamos a dar un ejemplo

# booleano! verdadero o falso / 1 o 0 / solo tengo 2 opciones
# pero en string podemos tener 
# 26 minuculas
# 26 mayusculas
# 10 signos de puntuacion
# entonces para 1 solo caracter tenemos +70 opciones
# esto hace que las listas sean mas lentas ya que tienen
# que reservar mas espacio en memoria para cada elemnto
# en cambio los arrays son mas eficientes ya que solo
# pueden tener un tipo de dato

import numpy as np
# de lista a arrays

lista_a_array = np.array([1,2,3,4,5])
print(type(lista_a_array[0]))
# Esto regresa que es un entero de 64 bits

# Necestamos 64 bits para representar los numeros 1 2 y 3?

# 1 es 01
# 2 es 10
# 3 es 11
# en este caso el maximo de bits que necesitamos es 2
# y no 64.

# para poder consumir menos memoria podemos pasar de 64 a 8 bites, como? 

lista_a_array = np.array([1,2,3,4,5], dtype=np.int8) # int8 es un entero de 8 bits
print(type(lista_a_array[0])) # Esto regresa que es un entero de 8 bits

# esta es una de las cosas por las cueles los arrays son tan importantes! y asi podemos optimizar nuestro cdigo

# array bisimensional

lista_a_array_bi = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.int8)
print(lista_a_array_bi)

# Tambien tenemos array 3D, 4D, etc
lista_a_array_3d = np.array([[[10,11,3],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]], dtype=np.int8)
print(lista_a_array_3d)
print(lista_a_array_3d.shape) # nos dice la forma del array
# (2, 3, 3) -> 2 matrices de 3x3

# Ya visto esto podemos avanzar a ver la redimension de arrays con reshape
# reshape -> cambiar la forma del array

array_1 = np.array([1,2,3], [4,5,6], type=np.int8) # array de 1 dimension
print("array_1 shape: ", array_1.shape) # (6,) -> 1 dimension con 6 elementos
print(array_1) # [1 2 3 4 5 6]
array_2 = array_1.reshape(3,2) # 3 filas y 2 columnas
print("array_2 shape: ", array_2.shape) # (3, 2) -> 2 dimension con 3 filas y 2 columnas
print(array_2) # [[1 2]

'''
array_1 shape: (2, 3)
[[1 2 3]
[4 5 6]]

array_2 shape: (3, 2)
[[1 2]
[3 4]
[5 6]]

'''

# Tambien podemos cambiar si queremos 6 filas y una columna
# por ende lo podemos convertir en un array univsimensional

# Creacion de arrays sin usar listas!
# Para eso podemos utilizar numpy.arange():

mi_array = np.arange(8)
print(mi_array)
print(type(mi_array))

# imprime:
# [0 1 2 3 4 5 6 7]

my_array_2 = np.array([1,2,3,4,5,6,7])
print(my_array_2)
print(type(my_array_2))

# imprime:
# [1 2 3 4 5 6 7]

# Es lo mismo! pero de la otra forma es la manera mas eficiente! 

# podemos iniciar por ejmplo en 2 o 3 como lo hacemos?
my_array_3 = np.arange(3, 8) # inicia en 3 y termina en 8

print(my_array_3) # [3 4 5 6 7]

# si solo quiero numeros imppares podemos utilizar un step

my_array_4 = np.arange(3, 20, 2) # inicia en 3 y termina en 20 con step de 2    
# va a ir de valoes de 2 en 2
print(my_array_4) # [ 3  5  7  9 11 13 15 17 19]

# si queremos trabajar con decimales?

my_array_5 = np.arange(3, 20, 0.5) # inicia en 3 y termina en 20 con step de 0.5
print(my_array_5)

# ahora hace saltos de 0.5
# [ 3.   3.5  4.   4.5  5.   5.5  6.   6.5  7.   7.5  8.   8.5

# podemos crear arrays vacios con np.zeros()
# esto es util cuando queremos reservar espacio en memoria
array_vacio = np.zeros((3,4)) # array de 3 filas y 4 columnas
print(array_vacio)

# imprime:
# [[0. 0. 0. 0.]

# otra forma es tambien con unos np.ones()
array_unos = np.ones((2,3)) # array de 2 filas y 3 columnas
print(array_unos)

# imprime:
# [[1. 1. 1.]

# a veces no sabemos de antemano que valores va a contener el arrat
# en estos casos puede interesarnos crear un array vacio

# np.empty() -> crea un array sin inicializar
array_sin_inicializar = np.empty((2,3)) # array de 2 filas y 3 columnas
print(array_sin_inicializar)
# imprime valores basura
# [[1. 1. 1.]

# en funcionamiento es el mismo! el tema es que si utilzamos empty
# nos trae numeros aleaorios cuando imporimimos! no se por ejemplo

# imporime: [6.177777777777777777773123e-307 6.177777777777777777773123e-307
# 6.177777777777777777773123e-307   6.177777777777777777773123e-307

# TENGAMOS CUIDADO CON ESTE ARAY, UTILICEN NP.ZEROS O NP.ONES SIEMPRE QUE PUEDAN

# tambien podemos crear arrays unidad con numpy.eye()
# esto es util para crear matrices identidad

array_identidad = np.eye(3) # matriz identidad de 3x3
print(array_identidad)

# imprime:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

eye_array = np.eye(3, k=1) 
print(eye_array)
# imprime:
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# k=1 desplaza la diagonal principal una posicion a la derecha

eye_array = np.eye(3, k=-1) 
print(eye_array)

# imprime:
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]

# Esto en matetmaticas se llama matriz de unidad! 

# Una vez creado el array podemos agregar sus valores, lo podemos maniupular
# lo podemos hacer con todos los arrays! 
# np.array(), np.arange(), np.zeros(), np.ones(), np.empty(), np.eye()

# podemos cambiar todos los 0 en cualuier numero por ejempolo 9

eye_array = np.eye(3, k=-1)
eye_array[eye_array == 0] = 9
print(eye_array)

# imprime:
# [[9. 9. 9.]
#  [1. 9. 9.]
#  [9. 1. 9.]]

eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2
eye_array[eye_array <= 2] = 9
print(eye_array)

# imprime:
# [[9. 1. 9.]
#  [9. 9. 1.]
#  [9. 9. 9.]]

# sustituye todas las filas hasta el 2

eye_array = np.eye(3, k=1)
eye_array[0:2, :] = 2
print(eye_array)

# imprime:
# [[2. 2. 2.] 
#  [2. 2. 2.]
#  [0. 0. 1.]]

# Sustituye desde la fila 1 hasta la ultima

eye_array = np.eye(3, k=1)
eye_array[1:] = 2 # no se incluye el stop value
print(eye_array)

# imprime:
# [[0. 1. 0.]
#  [2. 2. 2.]
#  [2. 2. 2.]]

# Podemos una vez creado el array reasignar sus valores!
# podemos hacerlo con todos los arrays, los creamos ocn np.array(), np.arange(), np.zeros(), np.ones(), np.empty(), np.eye()
# np.orange() es el mas eficiente

# sustituimos desde la fila 1 hasta la ultima y desde la columna 2 hasta la ultima

eye_array = np.eye(3, k=1)
eye_array[1:, 2:] = 0.11 # no se incluye el stop value
print(eye_array)

# imprime:
# [[0.   1.   0.  ] 
#  [0.   0.   0.11]
#  [0.   0.   0.11]]
# Podemos reasignar valores en arrays de cualquier dimension


# Tambien podemos ordenar el contenido con np.sort()

eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2
eye_array[eye_array <= 2] = 9
eye_array[1:, 2:] = 0.11 # no se incluye el stop value
print(eye_array)

# imprime:
# [[9.   1.   9.  ]
#  [9.   9.   0.11]
#  [9.   9.   0.11]]

eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2
eye_array[eye_array <= 2] = 9
eye_array[1:, 2:] = 4
sorted_array = np.sort(eye_array)
print(sorted_array)

# imprime:  
