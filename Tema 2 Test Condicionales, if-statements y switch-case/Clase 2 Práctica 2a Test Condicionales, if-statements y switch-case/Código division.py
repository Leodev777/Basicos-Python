# --- Pedir dos numeros al usuario
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisor: "))

# --- Comprobar si el divisor es cero
if m == 0.0:
    print("ERROR: No se puede dividir por 0")
else:
    division = n/m
    print("El resultado de dividir", n, "entre", m, "es", division)
# Si no es cero realizamos la division
# Si es cero imprimimos un error

## ----------------------------------------------------- ##

dividendo = float(input("Cargar dividendo"))
divisor = float(input("Cargar divisor"))

if dividendo == 0.0:
    print("ERROR: No se puede dividir")
else:
    division = dividendo/divisor
    print("El resultado de dividir", dividendo, "entre ", divisor, "es ", division)    