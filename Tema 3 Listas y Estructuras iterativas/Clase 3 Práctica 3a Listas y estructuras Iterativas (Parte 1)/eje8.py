# 1. Crear lista de frutas
frutas = ['Manzana', 'Naranja', 'Fresa', 'Banana', 'Kiwi', 'Mango', 'Pera', 'Uva', 'Piña', 'Melón', 'Sandía']

# 2. Longitud de la lista

longitud_de_ftutas = len(frutas)

# 3. Accerder al tercer objeto de la lista

print(frutas[2])  # Fresa

# 4. Modificar el segundo objeto de la lista

frutas[1] = 'Mandarina'

# 5. Añadir un nuevo objeto al final de la lista

frutas.append('Toronja')

# 6. Eliminar el primer objeto de la lista

frutas.pop(0)

# 7. Imprimir todos los objetos de la lista

print(frutas)

# 8. Imprimir los objetos de la lista en orden inverso

print(frutas[::-1])

# 9. Añadir uva al principio de la lista

frutas.insert(0, 'Uva_Mendocina')

# 10. Eliminar el último objeto de la lista y guardarlo en una variable llamada ultima fruta

ultima_fruta = frutas.pop()

# 11. Imprimir la lista y la última fruta eliminada
print(frutas)
print(ultima_fruta)