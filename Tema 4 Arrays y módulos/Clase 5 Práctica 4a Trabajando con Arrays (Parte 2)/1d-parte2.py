import numpy as np

array_randon = np.random.randint(1,101, size=15) # generamos numeros aleatorios entre 1 y 100 con random.randint y size para crear el array unidemensinal de 15 elementos

array_decimales = np.random.random(15)

print("Array random ", array_randon)
print("Array decimales ", array_decimales)

# Suma usando operador

suma_operador = array_randon - array_decimales
print("Suma usando operador ", suma_operador)


# -------------------------- ADD SUMA

suma_de_operadores = np.add(array_randon, array_decimales)
print("La suma es: ", suma_de_operadores)

# -------------------- 

resta_numpy = np.subtract(array_randon, array_decimales)
print("La resta es ", resta_numpy)


