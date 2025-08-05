for num in range(2,101): # Números del 2 al 100
    primo = True # Suponemos que es primo
    i = 2 # Comenzamos a dividir por 2
    while primo == True and i < num: # Mientras siga siendo primo y no lleguemos al número
            if num % i == 0: # Si es divisible por i
                primo = False # No es primo
            i += 1 # Incrementamos i
    if primo == True: # Si es primo
        print(num) # Lo imprimimos