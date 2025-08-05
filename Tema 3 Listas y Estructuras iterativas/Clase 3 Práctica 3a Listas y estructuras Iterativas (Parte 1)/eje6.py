'''
Crea un programa que imprima todos los
numeros primos entre el 2 y el 100. Un numero
primo es un numero positivo y entero mayor que uno que
no tiene un divisor positivo y entero que no sea 1 o si mismo.
'''
num = 0
# bucle que recorre los numeros del 2 al 100
for num in range(2, 101): # 2 es el primer primo
    # variable que indica si es primo
    primo = True # inicializamos como primo
    # bucle que comprueba si es primo
    # si es divisible por algun numero entre 2 y num-1, no es primo

    for i in range(2, num): # comprobamos desde 2 hasta num-1
      if num % i == 0: # si es divisible % es el resto de la division
            primo = False # no es primo
    if primo: # si es primo, lo imprimimos
        print(num)     # Imprime el numero primo
# Para dicho numero, hay alguno que sea sub divisor