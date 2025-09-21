import numpy as np

longitud = int(input("Ingresar la longitud del array: "))
array_ones = np.ones(longitud)
print(array_ones)

# Cambiar forma para que sea tipo y columnas

import numpy as np

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Suponiendo que quieres crear un array de unos y luego cambiarle la forma
array_original = np.ones(filas * columnas)  # array lineal con la cantidad total de elementos

if filas * columnas == longitud:
    nuevo_array = np.reshape(array_ones, (filas,columnas))
    print("Array con nueva forma: ", nuevo_array)
else:
    print("La cantidad de filas y columnas no es compatible con la longitud del array")

# input 9 ouput 3x3

