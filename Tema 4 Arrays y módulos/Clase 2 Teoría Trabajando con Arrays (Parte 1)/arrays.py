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


