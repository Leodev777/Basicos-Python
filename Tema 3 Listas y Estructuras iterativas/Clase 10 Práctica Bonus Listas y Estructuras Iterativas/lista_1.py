'''Desarrolla un script en Python que dado una cadena 
de caracteres con la siguiente información: nombre, 
apellido, DNI, código_asignatura, convocatoria, nota1, 
nota2, nota3 ... Por ejemplo: David Fernandez 12311267A 43527 2 2.1 4.6 3.4. 
El script debe crear una lista con esos datos, introducirlo en una lista de 
listas donde se encuentra la información de todos los alumnos e imprimir 
la nota media de los alumnos junto con el DNI.

'''
# base de datos dada (lista con datos de alumnos)
base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]


# Definimos la cadena de caracteres con la informacion de un alumno

cadena = "David Fernandez 12311267A 43527 2 2.1 4.6 3.4"

# Convertir la cadena de entrada en lista
datos_alumno = cadena.split() # split separara la cadena en una lista de valores individuales

# introducir la lista con los datos del alumno en la base de datos

base_datos.append(datos_alumno)

for alumno in base_datos:
    dni = alumno[2]
    
    suma_notas = 0 
    for i in range(5,len(alumno)):
        print(alumno[i])
        suma_notas = suma_notas + float(alumno[i])
    media = suma_notas / (len(alumno) - 5)
    print(f"El alumno con DNI {dni} tiene una nota media de {media:.3f}") # .3f para limitar a 3 decimales