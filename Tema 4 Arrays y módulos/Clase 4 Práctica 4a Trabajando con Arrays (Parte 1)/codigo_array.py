import numpy as np # import

array = np.zeros(8) # rango de 0

print("Array original",array)

array[:] = 2

print("Array modificado",array)


array_2 = np.arange(2,11,2)
print(array_2)

array_2_revertido = array_2[::-1]
print(array_2_revertido)
array_2_revertido[:] = 2
print(array_2_revertido)
print(array_2)

interseccion_1 = np.intersect1d(array, array_2)
print(interseccion_1)

# Elementos comunes deberias ser 2 en consola

interseccion_1 = np.intersect1d(array_2_revertido, array_2)
print(interseccion_1)


longitud = int(input("Cargar long"))
array_de_1 = np.ones(longitud)

array_de_1 = np.zeros(longitud)
print(array_de_1)
