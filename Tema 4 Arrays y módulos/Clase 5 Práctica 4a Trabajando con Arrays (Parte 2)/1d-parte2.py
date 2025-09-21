import numpy as np

# ------------------- CREACIÓN DE ARRAYS -------------------

# Array de 15 enteros aleatorios entre 1 y 100
array_enteros = np.random.randint(1, 101, size=15)

# Array de 15 decimales aleatorios entre 0.0 y 1.0
array_decimales = np.random.random(15)

print("Array de enteros   :", array_enteros)
print("Array de decimales :", array_decimales)

# ------------------- OPERACIONES -------------------

# 1. Suma usando el operador +
suma_operador = array_enteros + array_decimales
print("\nSuma con operador + :", suma_operador)

# 2. Suma usando la función de NumPy
suma_numpy = np.add(array_enteros, array_decimales)
print("Suma con np.add      :", suma_numpy)

# 3. Resta usando el operador -
resta_operador = array_enteros - array_decimales
print("\nResta con operador - :", resta_operador)

# 4. Resta usando la función de NumPy
resta_numpy = np.subtract(array_enteros, array_decimales)
print("Resta con np.subtract:", resta_numpy)

import numpy as np

# ------------ MULTIPLICACIÓN CON NUMPY ------------

# Dos valores simples
coso1 = 1
cosito2 = 3

# Multiplicación con np.multiply
multi_numpy = np.multiply(coso1, cosito2)
print("Multiplicación con np.multiply:", multi_numpy)

# ------------ ARRAY ALEATORIO Y VALOR MÁXIMO ------------

# Generamos un array con 15 números enteros entre 1 y 100
array_random = np.random.randint(1, 101, size=15)
print("\nArray random:", array_random)

# Buscamos el valor más alto en ese array
maximo_valor = np.max(array_random)
print("El valor máximo es:", maximo_valor)

# Media de valores con mean()

media_ramdom = np.mean(array_random)
print("Valor medio!", media_ramdom)
