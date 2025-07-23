# Pedimos el tiempo completo en formato: minutos segundos centesimas
tiempo_str = input("Ingresa el tiempo de Juan (formato: minutos segundos centesimas): ")

# Extraer minutos, segundos y centésimas
minutos_juan, segundos_juan, centesimas_juan = tiempo_str.split(" ")

# Convertimos los valores a números y calculamos el tiempo total en segundos
tiempo_total_segundos = float(minutos_juan) * 60 + float(segundos_juan) + float(centesimas_juan) * 0.01

# Mostrar el resultado
print("Tiempo total en segundos:", tiempo_total_segundos)
