# Pedir datos al usuario
# edad
edad = int(input("¿Que edad tienes?"))
# ingresos
ingresos = float(input("¿Que ingresos tienes mensual?"))

# Comprobar si se debe aplicar el tipo impositivo y comprobar cual
# Comprobar si el usuario es mayor de edad y sus ingresos --> si debe tributar: Sí

if edad >= 18 and ingresos > 1000:
    print("Usted debe tributar")
    ## calcular su renta anual
    renta_anual = ingresos * 12
      
    ## comprobar en que tramo se encuentra su ingreso anual
    if renta_anual < 15000:
        print("Tu impuesto es del 5%")
    elif 15000 <= renta_anual <= 25000:
        print("Tu impuesto es del 15%")
    elif 25000 <= renta_anual <= 50000:
        print("Tu impuesto es del 20%")
    else:
        print("Tu impuesto es del 25%")       

# Si el usuario no esta en el rango de edad o ingresos
else:
    print("Usted no tiene obligaciones tributarias")

    ## imprimir que no tiene obligacio de tributar 
