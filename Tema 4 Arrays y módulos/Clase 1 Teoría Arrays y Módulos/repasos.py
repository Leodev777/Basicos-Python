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

Un paquete/package es un directorio o carpeta con una coleccion
de modulos, podemos tener paquetes y subpaquetes con distintos
modulos en cada uno de ellos

my_paquete/
    __init__.py # archivo que indica que es un paquete
    trainig.py # archivo con codigo python
    ...
    ...
    submission.py # archivo con codigo python 
    ...
    ...
    subpaquete/
        __init__.py # archivo que indica que es un paquete
        metrics.py # archivo con codigo python  
       
        ... 

        
Tenemos los paquetes y subpaquetes, cada uno con sus modulos
y cada modulo con su codigo python, podemos importar
cualquier modulo desde cualquier otro modulo.


LIBRERIAS: Es un termino general para referirse a
una pieza de codigo reutilizable. 
Normalmente una libreria a contiene una coleccion de
paquetes y modulos.

EJ: Numpy, Pandas, Matplotlib, pytorch, ...

"Libreria": es una coleccion de paquetes
"Un paquete": es una colecicon de modulos

Ahora vamos a los arrays:

Array: Son contenedores que son capaces de guardar mas de un objeto al 
mismo tiempo. COleccion ordenada de elementos.

Diferencia entre listas y arrays:

Lista Es una estructura in-built / Array es una estructura que es necesario importar usando array o numpy
Lista Se crea usando [] / Array se crea usando array() o numpy.array()
Lista Puede contener elementos de distintos tipos / Array no puede contener elementos de distintos tipos
Lista El anidamiento de estructuras de distinta dimension es posible / Array Solo se pueden anidar arrays con mismo tamaño
-----> Lista No se puede aplicar operaciones aritmeticas / Array se pueden aplicar operaciones aritmeticas 
Lista Consume mas memoria / Array consume menos memoria
Lista mayor flexibilidad a la hora de modifcar datos / Array menos flexibilidad a la hora de modificar datos

'''

# Ejemplo lista (no se puede aplicar operaciones aritmeticas)
mi_lista = [1, 2, 3, 4, 5]
nueva_lista = mi_lista + 2 # Error
print(nueva_lista)
# para poder realizar operaciones aritmeticas dentro de una lista debemos
# realizar un bucle for

mi_lista = [1, 2, 3, 4, 5]
nueva_lista = []

for i in mi_lista:
    nueva_lista.append(mi_lista(i) * 3)
print(nueva_lista)

# Ejemplo array (se pueden aplicar operaciones aritmeticas)

