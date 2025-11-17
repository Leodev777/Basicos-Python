# Lista donde se guardarán todos los empleados como diccionarios individuales
empleados = []

# Variable de control para mantener activo el ciclo del menú
continuar = True

# Bucle principal del programa
while continuar:
    # Menú mostrado en cada iteración del ciclo
    print("1. Agregar empleado")
    print("2. Actualizar salario de empleado")
    print("3. Mostrar lista de empleados")
    print("4. Calcular promedio salarial por departamento")
    print("5. Salir")

    # Lectura de la opción elegida por el usuario
    opcion = input("Seleccione una opción: ").strip()

    # Opción 1: agregar un nuevo empleado
    if opcion == "1":
        # Lectura de datos básicos del empleado
        nombre = input("Ingrese el nombre del empleado: ").strip()
        raw_salario = input("Ingrese el salario del empleado: ").strip().replace(",", ".")

        # Conversión controlada del salario a número
        try:
            salario = float(raw_salario)
        except ValueError:
            # Si no se puede convertir, se detiene la carga del empleado
            print("Salario inválido. Use solo números.")
            continue

        departamento = input("Ingrese el departamento del empleado: ").strip()

        # Creación del diccionario que representa al empleado
        empleado = {
            "nombre": nombre,
            "salario": salario,
            "departamento": departamento
        }

        # Se agrega el diccionario a la lista principal
        empleados.append(empleado)
        print("Empleado agregado exitosamente.")

    # Opción 2: actualizar salario de un empleado existente
    elif opcion == "2":
        # Nombre buscado para identificar al empleado
        nombre_buscar = input("Ingrese el nombre del empleado: ").strip().lower()
        raw_nuevo = input("Ingrese el nuevo salario del empleado: ").strip().replace(",", ".")

        # Validación del salario nuevo
        try:
            nuevo_salario = float(raw_nuevo)
        except ValueError:
            print("Salario inválido. Operación cancelada.")
            continue

        # Indicador para saber si se encontró al empleado
        encontrado = False

        # Recorrido de la lista para localizar el diccionario correspondiente
        for empleado in empleados:
            if empleado["nombre"].strip().lower() == nombre_buscar:
                # Actualización directa del valor
                empleado["salario"] = nuevo_salario
                encontrado = True
                print("Salario actualizado.")
                break

        # Si no se halló coincidencia
        if not encontrado:
            print("Empleado no encontrado.")

    # Opción 3: mostrar todos los empleados
    elif opcion == "3":
        # Verificación de lista vacía
        if not empleados:
            print("No hay empleados registrados.")
        else:
            # Recorrido y muestra estructurada de cada empleado
            for empleado in empleados:
                print(f"Nombre: {empleado['nombre']}, Salario: {empleado['salario']:.2f}, Departamento: {empleado['departamento']}")

    # Opción 4: calcular el salario promedio por departamento
    elif opcion == "4":
        # Departamento a buscar
        departamento_buscar = input("Ingrese el departamento: ").strip().lower()

        total_salarios = 0.0
        contador = 0

        # Revisión de todos los empleados para el cálculo
        for empleado in empleados:
            if empleado["departamento"].strip().lower() == departamento_buscar:
                total_salarios += empleado["salario"]
                contador += 1

        # Se calcula promedio solo si hay coincidencias
        if contador > 0:
            promedio_salario = total_salarios / contador
            print(f"Promedio salarial del departamento {departamento_buscar}: {promedio_salario:.2f}")
        else:
            print(f"No hay empleados en el departamento {departamento_buscar}")

    # Opción 5: cierre del programa
    elif opcion == "5":
        print("Cerrando programa")
        continuar = False

    # Cualquier otra entrada no válida
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
