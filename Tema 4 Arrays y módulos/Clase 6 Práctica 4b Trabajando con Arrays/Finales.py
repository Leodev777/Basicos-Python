import numpy as np

# pedir cantidad de filas al usuario
filas = int(input("Número de filas: "))

# generar array con n filas y 4 columnas
# valores aleatorios enteros entre 3 y 10
array = np.random.randint(3, 11, size=(filas, 4))

print(array)


