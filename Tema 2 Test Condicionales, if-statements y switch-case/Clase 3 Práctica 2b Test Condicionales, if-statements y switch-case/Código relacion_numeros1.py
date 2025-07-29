# Pedir tres numeros
#x = float(input("Introduce el primer numero: "))
#y = float(input("Introduce el segundo numero: "))
#z = float(input("Introduce el tercer numero: "))

# Comprobar si alguno de ellos es la suma de los otros dos
# Si es cierto imprimimos True
#if (x==y+z):
#    print("El primero es la suma de los otros dos")
#elif (y==x+z):
#    print("El segundo es la suma de los otros dos")
#elif (z==x+y):
#    print("El tercero es la suma de los otros dos")

# Si es falso imprimir False
#else:
#    print("Ninguno es la suma de los otros dos numeros")



## --------------------------------------------------------------------------------------- ##


# Cargamos los numeros

A = float(input("Cargar el primer numero "))
B = float(input("Carga el segundo numero "))
C = float(input("Carga el tercer numero "))

# Hacemos las comparaciones

if (A == B+C):
    print("El primero es la suma de los otros dos")
elif (B == A+C):
    print("El segundo es la suma de los otros 2")
elif (C == B+A):
    print("El tercero es la suma de los otros 2")
else:
    print("Ninguna de los anteriores")        