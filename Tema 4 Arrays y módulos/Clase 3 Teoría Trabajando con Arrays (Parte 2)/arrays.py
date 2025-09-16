import numpy as np

a = np.zeros((3,3), dtype=np.int64) # Array creado desde 0 de 3x3 con dato de tipo entero de 64b
a[:] = 2 # decimos que todo el array a cambiamos los valores a 2
print(a)

#[[2 2 2]
#[2 2 2]
#[2 2 2]]

b = np.arange(1,10) # rango de 1 a 9
print(b)
# 1, 2, 3, 4, 5, 6, 7, 8, 9

b = b.reshape((3,3))
print(b)

#[[1 2 3]
#[4 5 6]
#[7 8 9]]

b1 = np.arange(1,10).reshape((3,3))

print(b1)

# Suma elementos de un array sum()

b = np.arange(1,10).reshape((3,3))
suma = b.sum()
print(suma)

# 45

# Suma de columnas de un array sum(0)

b = np.arange(1,10).reshape((3,3))
suma_columna = b.sum(axis=0) # seleccionamos el eje, en este  caso es 0
print(b)
print(suma_columna)

# 12 15 18

# Suma de las filas del array sum(1)

b = np.arange(1,10).reshape((3,3))
suma_fila = b.sum(1)
print(b)
print(suma_fila)

# 6 15 24}

# Multiplicacion de elementos de un array!





# prod() Multiplica todos los elementos de un array
b = np.arange(1,10).reshape((3,3))
prod_array = b.prod()
print(b)
print(prod_array)

# prod(0) multiplica columnas
b = np.arange(1, 10).reshape((3,3))
m_columna = b.prod(axis = 0) # indila el eje
print(b)
print(m_columna)

# prod(1) multiplica las filas

b = np.arange(1,10).reshape((3,3))
m_filas = b.prod(axis = 1) # indica el eje
print(b)
print(m_filas)

# Valor maximo, minimo y medio de un array

# mean() valor medio

b = np.arange(1,10).reshape((3,3))
valor_medio = b.mean()
print(b)
print(valor_medio)


# max() valor maximo

b = np.arange(1,10).reshape((3,3))
valor_maximo = b.max()
print(b)
print(valor_maximo)

# min() valor minimo

b = np.arange(1,10).reshape((3,3))
valor_minimo = b.min()
print(b)
print(valor_minimo)


