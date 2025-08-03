# Como podemos agregar elementos a una lista a otra
# a partir de una lista ya existente.

mis_autos = ['BMW', 'FIAT', 'MERCEDES', 'AUDI']
autos_invitados = mis_autos[:] # Copiamos la lista mis_autos
autos_invitados.append('VOLKSWAGEN')   # Agregamos un nuevo elemento
print(mis_autos)
print(autos_invitados)  # Mostramos la lista de invitados

# las listas son colecciones de objetos, pero a su vez
# son un objeto tambien. Igual que una lista
# puede contener objetos como string, int, float, etc.
# una lista puede contener otras listas.
# Por ejemplo, podemos crear una lista de listas.

datos_alumnos = [
    ['Juan', 20, 'Ingeniería'],
    ['Ana', 22, 'Medicina'],
    ['Luis', 21, 'Arquitectura']
    ]
print(datos_alumnos)

print(type(datos_alumnos[2])) # Mostramos el tipo de dato del tercer elemento
print(datos_alumnos[2][0]) # Mostramos el nombre del tercer alumno
print(datos_alumnos[1][2]) # Mostramos la carrera del segundo alumno

# Repaso

# Listas son colecciones de objetos
# Pueden contener cualquier tipo de objeto
# Pueden contener otras listas 
# Podemos accedes a los elementos
# Usar los elementos
# Modificar los elementos
# Agregar nuevos elementos
# Eliminar elementos
# Ordenar los elementos
# Repetir los elementos
# Copiar las listas
# Longitud de las listas
# Iterar sobre las listas
# Comprobar si un elemento está en la lista
# Listas numericas + funciones especificas
# Acceder a partes de una lista
# Copiar listas y partes de listas
# Anidamiento de listas
# Estructura condicional + Lista ---> Comprobar existencia de elementos


# En las estructuras de control que vimos recien!

# Funcionamiento general
# uso de range 
# uso de break
# uso de continue
