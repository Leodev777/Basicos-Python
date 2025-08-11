'''
Dado una lista de números enteros,
escribe un script en Python que 
devuelva una nueva lista con los 
números primos de la lista original. 
Además, el script debe devolver el número 
total de números primos encontrados y 
la suma de los números primos encontrados
'''

# Lista de números enteros
# Lista vacia para primos
# Numeros total de numeros primos
# Suma de los numeros primos

numeros = [10, 15, 23, 42, 7, 19, 4, 29, 30]
primos = []
total_primos = 0
suma_primos = 0

# Bucle para recorrer la lista de números
for numero in numeros:
    primo = True
    # Comprobar si el número es primo
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
        # Si es primo, añadir a la lista de primos
    if primo == True:
        primos.append(numero)
        print(f"{numero} es primo")
        print(f"Total de primos: {len(primos)}")

        total_primos = total_primos +1
        suma_primos = suma_primos + numero
    
    print(f"Suma de primos: {suma_primos}")

# --- ANOTACIONES DEL CÓDIGO ---
# 1. Se define una lista de números enteros llamada 'numeros'.
# 2. Se inicializan las variables 'primos' (lista vacía), 'total_primos' y 'suma_primos' en 0.
# 3. Se recorre cada número de la lista 'numeros' usando un bucle for.
# 4. Para cada número, se asume inicialmente que es primo (primo = True).
# 5. Se verifica si el número tiene algún divisor entre 2 y el número-1.
#    Si encuentra un divisor, se marca como no primo (primo = False).
# 6. Si el número es primo, se agrega a la lista 'primos', se incrementa el contador y se suma el número.
# 7. Se imprime el número primo encontrado, el total de primos y la suma acumulada de primos.
# 8. El código imprime la suma de primos en cada iteración, lo que puede generar información repetida.
# 9. Al finalizar, la lista 'primos' contiene todos los números primos encontrados, 'total_primos' indica cuántos son y 'suma_primos' su suma


# Tengamos en cuenta que python ya contiene una funcion para realizar este tipo de operaciones, sin embargo, el objetivo de este ejercicio es practicar la logica de programacion y el uso de bucles y condicionales
# con sum(primos) podemos obtener la suma de los numeros primos