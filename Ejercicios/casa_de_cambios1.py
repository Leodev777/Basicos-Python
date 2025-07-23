# Pedir ingresar cantidad de euros a convertir!

euros = input("Ingresa la cantidad de euros que deseas convertir: ")

# Convertimos la cantidad ingresada a un FLOAT

euros = float(euros)

# Convertir la cantidad de euros a dolares

dolares = euros * 1.3

# printeamos el resultado

print(euros, "Euros son:", dolares, "dolares")
