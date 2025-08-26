'''
El sistema debe pedir al usuario que ingrese si es menor de 35 años? si es asi el sistema debe tomar el aporte de obra social
que es un numero como por ejemplo $65,123.89 
y ese dicho valor debe ser multiplicado por 100 y el resultado devivirlo por 3, eso es solo si la persona es menor de 35 años
no esta casado ni tiene hijos, si no cumple con esas condiciones el sistema debe preguntar si la mutual es para el o para el grupo familiar
si es para el grupo familiar debe realizar el mismo caluculo y al resultado sumarle el valor asigando en mi tabla personal, ademas si la persona es menor de 26 años
tiene aun mas beneficios y un descuento extra
'''
# Preguntar tipo de empleo
tipo_empleo = input("¿Tenés bono de sueldo o sos autónomo? (bono/autonomo): ").lower()

if tipo_empleo == "bono":
    # Pedir aporte de obra social
    aporte_str = input("Ingresá tu aporte de obra social (ej: $65,312.14): ")
    # Limpiar y convertir a float
    aporte_limpio = float(aporte_str.replace('$', '').replace(',', ''))
    
    # Preguntar datos personales
    edad = int(input("¿Cuántos años tenés? "))
    estado_civil = input("¿Estás casado? (si/no): ").lower()
    tiene_hijos = input("¿Tenés hijos? (si/no): ").lower()
    
    # Cálculo base
    calculo_base = (aporte_limpio * 10) / 3
    
    # Inicializar variables para extras
    extra_casado = 0
    extra_hijos = 0
    
    # Verificar si está casado
    if estado_civil == 'si':
        extra_casado = float(input("Ingresá el monto extra por estar casado: "))
    
    # Verificar si tiene hijos
    if tiene_hijos == 'si':
        num_hijos = int(input("¿Cuántos hijos tenés? "))
        extra_por_hijo = float(input("Ingresá el monto extra por hijo: "))
        extra_hijos = num_hijos * extra_por_hijo
    
    # Calcular resultado final
    if edad < 35:
        if estado_civil == 'no' and tiene_hijos == 'no':
            # Menor de 35 sin hijos ni casado - solo cálculo base
            resultado = calculo_base
        else:
            # Menor de 35 con hijos o casado - cálculo base + extras
            resultado = calculo_base + extra_casado + extra_hijos
    else:
        # Mayor de 35 años
        if estado_civil == 'no' and tiene_hijos == 'no':
            # Mayor de 35 sin hijos ni casado - paga extra de cuota mutual
            extra_mutual = float(input("Ingresá el extra de cuota mutual para mayores de 35: "))
            resultado = calculo_base + extra_mutual
        else:
            # Mayor de 35 con hijos o casado - cálculo base + extras
            resultado = calculo_base + extra_casado + extra_hijos
    
    # Mostrar resultado
    print(f"El resultado es: ${resultado:,.2f}")

elif tipo_empleo == "autonomo":
    print("Para autónomos el cálculo no aplica según el sistema actual.")
else:
    print("Opción no válida. Por favor ingresá 'bono' o 'autonomo'.")