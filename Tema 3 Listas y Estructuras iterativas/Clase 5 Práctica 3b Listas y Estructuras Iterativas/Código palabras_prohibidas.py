# Lista inicial con varias palabras
palabras_aleatorias = ['gato', 'perro', 'elefante', 'jirafa', 'tigre', 'kata', 'wanaco']

# Lista con letras que no queremos que aparezcan en las palabras
letras_prohibidas = ['y', 'k', 'w']

# Lista vacía donde guardaremos las palabras que pasen el filtro
lista_de_palabras_filtradas = []

# Recorremos cada palabra de la lista inicial
for palabra in palabras_aleatorias:
    incluir = True  # Suponemos inicialmente que la palabra es válida
    
    # Recorremos cada letra prohibida
    for letra in letras_prohibidas:
        # Si la letra prohibida aparece en la palabra
        if letra in palabra:
            incluir = False  # Marcamos que NO se debe incluir
            break  # Salimos del bucle interno porque ya no hace falta seguir comprobando
    
    # Si después de revisar todas las letras, la palabra sigue siendo válida...
    if incluir:
        lista_de_palabras_filtradas.append(palabra)  # La añadimos a la lista filtrada

# Mostramos el resultado final
print("Lista de palabras filtradas:", lista_de_palabras_filtradas)
print("Lista de palabras originales:", palabras_aleatorias)
