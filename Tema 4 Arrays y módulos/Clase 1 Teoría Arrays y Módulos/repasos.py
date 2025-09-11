# Módulo: Archivo con extension .py que contien codigo en python
# que puede importarse desde otro archivo python.

# Arrays, modulos y librerias nos sirven para interconectar
# codigo y poder hacer estrucutras muchisimos mas complejas
# podremos llamar scripts, funciones, etc.

# Ej:

'''
constantes
pi = 3.14
tau = 6.28
e_euler = 2.71
G_gauss = 0.83

-----------

import constantes

print(constantes.pi)

cuando los nombres son muy largos
al importarlos por ejemplo print(constantes.pi) podemos
dentro del import poner un alias
import constantes as cte y quedaria asi:
print(cte.pi)

esto es algo que utiliza mucho para agilizar la lectura del codigo

'''

# Ejemplazo 

import constantes 
radio = 12.5
area = constantes.pi * radio**2
print(area)

# Ejemplo 2

import constantes as cte
radio = 12.5
area = cte.pi * radio**2
print(area)

'''
Concepto de paqueres y librerias:

Un paquete es una carpeta que contiene varios modulos,
podemos,


'''