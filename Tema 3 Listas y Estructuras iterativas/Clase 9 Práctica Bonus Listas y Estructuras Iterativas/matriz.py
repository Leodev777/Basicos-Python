'''
Definimos dos listas de listas:
- M es una matriz válida (todas las filas tienen la misma cantidad de columnas).
- M2 NO es una matriz (una de las filas tiene distinta cantidad de elementos).
'''

M = [[2, 5, 3],
     [6, 1, 8],
     [7, 5, 4]]

M2 = [[4, 2, 3],
      [4, 5],
      [6, 8, 2]]

# --------------------------------------------------------
# Verificar si una lista de listas es realmente una matriz
# --------------------------------------------------------

# Tomamos la primera fila de M2 para contar cuántas columnas debería tener
n_columnas = len(M2[0])

# Número de filas de M2
n_filas = len(M2)

# Inicializamos la variable como True (suponemos que es matriz)
matriz = True

# Recorremos todas las filas de M2
for i in range(n_filas):
    # Si alguna fila no tiene el mismo número de columnas, dejamos de verificar
    if len(M2[i]) != n_columnas:
        matriz = False
        break   # Cortamos el bucle porque ya sabemos que no es matriz

# Al salir del bucle, comprobamos el resultado final
if matriz:
    print("Es una matriz")
else:
    print("No es una matriz")
