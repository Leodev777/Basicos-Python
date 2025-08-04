'''
Analisi de precios de productos:

Escribir un programa en python que analice
una lista de precios de productos
y determine el precio mas alto, el precio
mas bajo y el precio promeio de todos los prudctos.
Soluciona el ejercicio sin usar las funciones MAX() o MIN()
'''

# Lista de precios

precios = [10.5, 20.0, 15.75, 30.0, 25.0,0.35,40.0,87,4,3,523,123,0.58,0.32,0.98,0.211,0.58,0.228,0.875,0.99]
precio_total = 0
precio_maximo = 0.0
precio_minimo = float('inf')  # Inicializamos con infinito positivo
precio_promedio = 0.0
# bucle para recorrer la lista
for precio in precios:
    
# if staement
# comprobamos si el precio es mas alto que el anteior

    if precio > precio_maximo:
        precio_maximo = precio

# coprobamos si el precio es mas bajo que el anteior

    if precio < precio_minimo:
        precio_minimo = precio
# sumamos los valores de la lista
    precio_total += precio

print("Precio máximo:", precio_maximo)
print("Precio mínimo:", precio_minimo)

# calculamos el precio promedio
# imrpimimos por pantalla el resultado
print("Precio promedio:", precio_total / len(precios))
