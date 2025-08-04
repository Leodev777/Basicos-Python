'''
Crea un programa en el que se pregunte al usuario al
por una frase y una letra, y muestre por pantala
el numer ode veces que aparece la letra de la frase.
'''
# Programa que cuenta cuántas veces aparece una letra en una frase

# Pedir frase y letra al usuario
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0

# Contar las apariciones de la letra
for caracter in frase:
    if caracter == letra:
        contador += 1

# Mostrar resultado
print(f"La letra aparece {contador} veces en la frase.") 
# Fin del programa