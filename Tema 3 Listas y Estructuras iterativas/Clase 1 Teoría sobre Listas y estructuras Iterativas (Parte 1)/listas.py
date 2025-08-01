## Que es una lista?

# Una lista es una coleccion de objetos en un orden particular

# lista1 = ["a", "b", "c"]
# lista2 = [1,2,3]
# lista3 = [1,5,7]
# lista4 = [6,"u","Z", 5]

autos = ['audi', 'bmw', 'fiat']
print(autos[1].title) # imprime el string que se encuentre en el orden de la lista
# ahora a estos string podemos agregar todo lo que venimos viendo
# es una coleccion ordenada asi que podemos acceder a los elementros de la coleccion
# diciendole a python el indice del elemento al que queremos acceder.

# para accerder a los demas indices: 

autos = ['audi', 'bmw', 'fiat']
print(autos[1], autos[2])

# podemos tambien hacer con -1 esto lo que hace es indicar
# que tiene que accerder a este ultimo elemento de la lista, esto sirve para no ver cuan larga es la lista
# entonces directamente trae el ultimo elemento de la lista.

# acceder a elementos de una lista: se trata de una coleccion ordenada asi que podemos
# acceder a los elementos de la coleccion diciendole a python el indice del elemento al que queremos accerder.

autos = ['audi', 'mbw','fiat']
print(type(autos))
print(type(autos[0]))

autos = ['audi', 'bmw', 'fiat']
mensaje = 'Si me comprase un auto, elegiria un', autos[-1].title()
print(mensaje)

# Modificar elementos

autos = ['audi','bmw','fiat']
print(autos)
autos[1] = 'Ford'
print(autos)

# añadir elementos: Append() nos permite añadir elementos a una lista en la ultima posicion,
# las lista son objetos dinamicos. Se les puede asignar mas memoria de manera dinamica

autos = ['bmw','audi','ford']
print(autos)
autos.append('mercedes') # append añade el elemento al final de la lista, recordemos que lo podemos llamar con [-1]
print(autos)

# ¿ que imprime esto por consola ? 

# ['bmw', 'audi', 'ford', 'mercedes']

autos = []
autos.append('alfa romeo')
autos.append('renault')
autos.append('peugeot')
print(autos)

# ['alfa romeo', 'renault', 'peugeot']


# si en vez de queremos agregar al final con append lo queremos agregar al principio lo podemos hacer de la sieguiente forma
# insert() nos permite añadir elementoos a una lista en cualquier posicion
autos = ['alfa romeo', 'renault', 'peugeot']
print(autos)
autos.insert(1, 'peugeot')
print(autos)

# ['alfa romeo', 'peugeot', 'renault']

# Borrar elementos: igual que podemos insertar elementos en una lista, tambien
# podemos borrarlos. POP()
# el elemento eliminado lo podemos almacenar en una variable

autos ['alfa romeo', 'renault', 'peugeot']
print(autos)
autos_eliminado = autos.pop()
print(autos)
print(autos_eliminado)

# ['alfa romeo', 'renault']

# para eliminar una posicion en cocreto:

autos ['alfa romeo', 'renault', 'peugeot']
print(autos)
autos_eliminado = autos.pop(1)
print(autos)
print(autos_eliminado)

# ['alfa romeo', 'peugeot']

# para borrar elementos que no sabemos en que posicion esta pero sabemos que es un audi por ejemplo!
# Remove()

autos ['alfa romeo', 'audi', 'peugeot']
autos.remove('audi')
print(autos)

# ['alfa romeo', 'peugeot']

# esto elimina la primer entrada, pero si hay mas audi por ahi dando vueltas, para eliminar todos los audis hay que aplicar mas adelante con los bucles que vamos a ir viendo!

autos ['alfa romeo', 'audi', 'peugeot']
del autos[1] # del no esta asociada solo a lsita, esto se peude usar de formas mas generales, esto lo vamos a ver despues
print(autos)

# ['alfta romeo', 'peugeot']

# Las listas tambien tienen asociadas unas funciones internas o metodos en python
# ordenar elementos: podemos ordenar elementos por orden alfabetico o por numero de 
# manera permanente 

autos ['alfa romeo', 'audi', 'peugeot']
autos.sort()
print(autos)

# audi alfa romeo peugeot

autos ['23', '11', '5']
autos.sort()
print(autos)

# 5 11 23

# Sorted() ordena de manera temporal

autos = ['alfa romeo', 'audi', 'peugeot']
print(sorted(autos))

# audi alfa romeo peugeot

# Reverse() nos ordena alreves

autos = ['alfa romeo', 'audi', 'peugeot']
autos.reverse()
print(autos)

# es de atras hacia adelante


# LEN() longitud, nos da el numero de elementos que tiene una lista

autos = ['alfa romeo', 'audi', 'peugeot']
print(len(autos))

# 3

# Listas y estructuras condicionales: podemos comprobar si un elemento esta en la lista

autos = ['bmw', 'audi', 'mercedes']
auto_elegido = 'audi'
if auto_elegido in autos:
    print("Has seleccionado un", auto_elegido)
else:
    print("No tenemos esa marca")    

# Seleccionaste un audi

autos = ['bmw']
if autos:
    print("La lista tiene el siguiente contenido ", autos)
else:
    print("La lista esta vacia")

    