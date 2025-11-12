# Base de datos con puntajes
registros = {}
continuar = True

# Seguimiento de los puntajes --> actualizados

while continuar:
    # Pedir al usuario su nombre
    nombre = input("Ingrese su nombre: ")
    if nombre.lower() == 'Salir':
        continuar = False
    else:
        puntaje = int(input("Ingrese el puntaje"))
        registros[nombre] = puntaje
    # Puntaje mas alto
    juagador_mas_alto = max(registros, key=registros.get)
    puntaje_mas_alto = registros[juagador_mas_alto]
    print("El puntaje mas alto es de", juagador_mas_alto, "con", puntaje_mas_alto, "puntos.")

    # Promedio de puntajes

    promedio = sum(registros.values())
    cantidad_jugadores = len(registros)
    promedio_final = promedio / cantidad_jugadores
    print("El puntaje promedio es de:", promedio_final)