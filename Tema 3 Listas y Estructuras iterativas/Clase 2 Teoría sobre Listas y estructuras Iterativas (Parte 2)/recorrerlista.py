lista = ['bmw','audi','mercedes']  # Crea una lista con tres cadenas
for lista in lista:               # Recorre cada elemento de la lista (sobrescribe el nombre 'lista')
    print(lista)                  # Imprime el elemento actual


lista = ['bmw','audi','mercedes']   # Crea una lista con tres cadenas
for i in range(0,len (lista)):      # Recorre los índices desde 0 hasta len(lista)-1
    print(lista[i])                 # Imprime el elemento en la posición i

lista = ['bmw','audi','mercedes']   
for i in range(0,len(lista)):
    print('Este coche es un, ', lista[i].title())
#Este coche es un,  Bmw
#Este coche es un,  Audi
#Este coche es un,  Mercedes

print('Lista terminada') #Lista terminada


