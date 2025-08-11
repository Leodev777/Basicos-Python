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