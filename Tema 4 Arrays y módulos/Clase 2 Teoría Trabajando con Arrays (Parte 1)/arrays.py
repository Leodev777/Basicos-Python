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