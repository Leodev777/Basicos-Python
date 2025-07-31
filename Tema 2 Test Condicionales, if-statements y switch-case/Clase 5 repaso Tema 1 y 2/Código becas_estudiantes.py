'''
EJERCICIOS 2A
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes 
con un mínimo de un 8 de media. Además para acceder a la beca el 
estudiante debe tener entre 17 y 21 años. Crea un script que pida
el nombre, la edad y la nota media del estudiante e indique si 
puede optar a la beca o no.
'''

# --- Pedir los datos al usuario

nombre = input("¿Cual es tu nombre?")

edad = int(input("¿Cual es tu edad?"))

nota = float(input("¿Que nota sacaste en el examen? "))


# -- Comprobar si cumple las condiciones
# nota media > 8 + edad 17 - 21

if edad >= 17 and edad <= 21 and nota >= 8:
   
    # Imprimiremos que la condicion la cumple
     print(nombre, "Excelente, ya tienes una BECA")

else:
    # si no imprimiremos que la condicion no se cumple
    print("Lamentablemente no calificas para la BECA")  

