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

import numpy as np

mi_array = np.array([1, 2, 3, 4, 5])
nuevo_array = mi_array * 2
print(nuevo_array)

# Consola: 2 4 6 8 10

# Ejemplo array 2D

import numpy as np
mi_array_2d = np.array([[1, 2, 3], [4, 5, 6]])
nuevo_array_2d = mi_array_2d + 3
print(nuevo_array_2d)

# Consola:
# [[4 5 6]

import numpy as np
mi_array_2d = np.array([1, 2, 3, 4, 5])
nuevo_array_2d = mi_array_2d / 2
print(nuevo_array_2d)
# Consola: [0.5 1.  1.5 2.  2.5]

'''

Una estructura in-built es una estructura que viene por defecto
con el lenguaje de programacion, no es necesario importar

pero para los arrays debemos utilizar numpy o el modulo array
porque no viene por defecto

Existe un modulo y una libreria:

Modulo array: Este viene con las instalacion de python
Libreria: Esta libreria la insntalamos aparte

array sepan que existe pero no se utiliza mucho por no decir nunca
es muy basico.

'''

'''
Lo que tiene numpy es que si llamamos al typo de elemento
np.array([1, 2, 3, 4], true) convierte todos los elementos
a strings.

'''

'''
Cuando usamos un array y cuando usamos una lista?

Una LISTA es facilmente mutable, podemos agregar, eliminar, es mucho mas flexible
y es una estructura in-built y necesitas mas memoria.

Un ARRAY necesitan menos memoria que las listas y ademas podemos realizar operaciones
aritmeticas directamente y no es in-built, necesitamos importar numpy o array,
solo manejas elementos del mismo tipo.

USAMOS ARRAYS CUANDO VAMOS A TRABAJAR CON UNA 
SECUENCIA GRANDE DE ELEMENTOS O QUEREMOS REALIZAR
OPERACIONES ARITMETICAS DIRECTAMENTE

USAMOS LISTA CUANDO ES UNA SECUENCIA PEQUEÑA DE ELEMENTOS
Y NECESITAMOS FLEXIBILIDAD PARA MODIFICARLA Y NO QUEREMOS
REALIZAR OPERACIONES ARITMETICAS DIRECTAMENTE

'''

# Hay 2 maneras de declarar un array este es bastante basico
# no se suele utilizar pero debemos saber que existe

#EJ

import array as arr # importamos el modulo array y le ponemos un alias arr
mi_array = arr.array('i', [1, 2, 3, 4, 5]) # 'i' indica que son enteros
print(type(mi_array)) # Consola: <class 'array.array'>

# para los numeros enteros 'i'


# Ahora si vamos a ll que nos interesa numpy, tiene muchisimas
# funcionalidades, vamos a ver las mas basicas

import numpy as np # importamos numpy y le ponemos un alias np
mi_array = np.array([1, 2, 3, 4, 5]) # no necesitamos indicar el tipo
print(type(mi_array)) # Consola: <class 'numpy.ndarray'>

# Como instalamos numpy?
'''
Para que sirve instalar conda?

sive para crear entornos de trabajo aislados, cada entorno puede tener sus propias
versiones de python y paquetes instalados sin que afecte
a otros entornos.

Como instalamos conda? 

1. descargamos e instalamos anaconda o miniconda
2. abrimos la consola de anaconda o miniconda
3. creamos un entorno de trabajo conda create --name "nombre de mi entorno de laburo" python=3.x
Activamos nuestro environment de trabajo:

1. conda activate "nombre de mi entorno de laburo"

2. conda install numpy ( si estamos usando conda)

3. si no estamos usando conda pip install numpy

'''

# Que vimos?

# 1. Que es un modulo y como se crea
# 2. que es un paquete
# 3. que es una libreria
# 4. que es un array y diferencias con las listas
# 5. como se instala numpy
