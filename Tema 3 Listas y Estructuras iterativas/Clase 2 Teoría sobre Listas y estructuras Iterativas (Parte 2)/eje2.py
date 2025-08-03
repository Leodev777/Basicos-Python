# --- Inicializo la lista de numeros
numeros = [] 
terminado = False

# --- Crea bucle para pedir numeros
while not terminado:
    # Pedimos el número al usuario
    numero = int(input('Introduce un número: '))
    
    # Añadimos el número a la lista
    numeros.append(numero)
    
    # Si ya tenemos 4 números, cambiamos terminado a True
    if len(numeros) == 4:
        terminado = True

# --- Salida: 4 numeros enteros
print('Números introducidos:', numeros)
print('El número mayor es:', max(numeros))
print('Números en orden ascendente:', sorted(numeros))
