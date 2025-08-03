numeros = list(range(1,6))
print(numeros)

# [1, 2, 3, 4, 5]

numeros_pares = list(range(2,11,2)) # del 2 hasta el 10 con paso 2
print(numeros_pares)

# [2, 4, 6, 8, 10]


numeros_cuadrados = []
for valor in range(1,11): # ira del 0 al 10
    cuadrado = valor ** 2
    numeros_cuadrados.append(cuadrado)
print(numeros_cuadrados)

# Comprimida

numeros_cuadrados = [valor**2 for valor in range(1,11)]
print(numeros_cuadrados)


# Trabajar con partes de la lista, accedemos a una porcion
#          0,1,2,3,4,5,6,7,8,9 # los indices no siempre estan en orden
digitos = [1,2,3,4,5,6,7,8,9,0]
algunos_digitos = digitos[1:6]
print(algunos_digitos)

juadores = ['leo', 'pepe', 'juan', 'tito', 'alberto', 'lucio', 'ricardito']
equipo_A = juadores[:3] # podemos oviar el 0, python inicia en 0 por defecto tambien podmeos hacer al reves [3:] esto iria del 3 al fin de la lista
equipo_B = juadores[3:6] # podemos iniciar indices negativos, empiezan en -1 - 2 -3 -4 t comienza de atras hacia adelante el ultimo seria -1 el penultimo -2 y asi

print('En el equipo A los juagadores son: ', equipo_A)
print('En el equipo B los jugadores son:' ,equipo_B)


