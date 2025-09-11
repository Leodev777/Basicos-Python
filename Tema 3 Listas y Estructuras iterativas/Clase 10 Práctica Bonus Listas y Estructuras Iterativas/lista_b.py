'''
Supón ahora que tu input es un string como este: 
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ''’

'''

# Base de datos

base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]

# input con informacion de varios alumnos

cadena_alumno = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n \
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n \
Juan Perez 647829236A 43527 2 8.1 8.5 8.4" 

# convertir cadena en una seria de listas diferentes para cada alumno

alumnos = cadena_alumno.split("\n") # split separara la cadena en una lista de valores individuales


for alumno in alumnos:
    alumno = alumno.strip() # strip elimina espacios en blanco al inicio y final de la cadena
    datos_alumno = alumno.split()
    if datos_alumno:
        base_datos.append (datos_alumno) # split separara la cadena en una lista de valores individuales
    print("---> ", datos_alumno)