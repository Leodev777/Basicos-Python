# Pedir NUMEROS al usuario
n1 = float(input("Introduce un numero: "))
n2 = float(input("Introduce otro numero: "))
n3 = float(input("Introduce otro numero: "))
n4 = float(input("Introduce otro numero: "))


# Imprimir el mayor de los cuatro números
if (n1>n2):
    n1, n2 = n2, n1 

if (n2>n3):
    n2, n3 = n3, n2

if (n3>n4):
    n3, n4 = n4, n3

print(" El mayor de los 4 es ", n4)
print("El orden de los numeros es: ", n1, n2, n3, n4)