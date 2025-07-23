# Pedir ingresar cantidad de euros a convertir!

euros = input("Ingresa la cantidad de euros que deseas convertir: ")

# Convertimos la cantidad ingresada a un FLOAT

euros = float(euros)

# Convertir la cantidad de euros a dolares

dolares = euros * 1.2


# Calculamos la parte que se queda la casa de cambio como comision por servicio!

comision_por_gestion = dolares * 0.001

# dolares que le damos al usuario en mano!

dolares_recibidos = dolares - comision_por_gestion

# Printear resultados!

print("Monto ingresado: ", euros, "euros")
print("Cambio en dolares: ", dolares, "dolares")
print("Comision de servicio: ", comision_por_gestion, " dolares")
print("Mondo recibidos ", dolares_recibidos, " dolares")