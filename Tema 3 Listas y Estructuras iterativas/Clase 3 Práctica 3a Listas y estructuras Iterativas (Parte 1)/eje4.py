'''
Crea un script que pida al usuario una palabra
y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la ultima.
'''

# Pedir palabra al usuario

palabra = input("Introduce una palabra: ")

# buble para recorrer cada letra de la palabra desde la ultima hasta la primera
for i in range(len(palabra)-1, -1, -1): # desde la ultima letra (len(palabra)-1) hasta la primera (-1) en pasos de -1
# imprimir cada letra de atras hacia adelante
    print(palabra[i])  # imprimir la letra en la posicion i

# Otra manera que podemos hacerlo es:

lapalabra = input("Introduce una palabra: ")

for letra in lapalabra[::-1]:
    print(letra)  # imprimir cada letra de la palabra en orden inverso
# Fin del programa