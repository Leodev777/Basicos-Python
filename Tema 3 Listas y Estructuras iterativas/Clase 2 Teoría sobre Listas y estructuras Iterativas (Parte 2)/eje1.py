'''
Pide al usuario 4 numeros y devuelve
los numeros introducidos en orden ascendente.
Para eso puedes usar listas y bucles for
'''

# --- Inicializamos una lista de numeros
lista_numeros = []

# --- Creamos un bucle para ir piediendo los numeros y añadirlo a la lista
for i in range(0,4):
    numeros = int(input('Introduce un número: '))
    lista_numeros.append(numeros)
  # Añadimos el numero a la lista

# --- Salida del bucle busco los 4 numeros
print('Los números introducidos son:', lista_numeros)
# --- Imprime el mayor numero
print('El mayor número es:', max(lista_numeros))
# --- Vemos la lista en orden
lista_numeros.sort()  # Ordenamos la lista
print('Los números en orden ascendente son:', lista_numeros)