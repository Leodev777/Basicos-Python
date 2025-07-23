# Pedir el nombre de usuario
# Printear como te llamas?
# nombre = input
# estado = input

nombre = input("¿Cómo te llamas? ")  # Tipo string
mensaje = "Hola, ¿cómo estás " + nombre.title() + "?, ¡espero te conviertas en un excelente programador!"
print(mensaje)

estado = input("¿Cómo te sientes hoy? ")
print("Estoy " + estado.upper())
print("Estoy " + estado.lower())
