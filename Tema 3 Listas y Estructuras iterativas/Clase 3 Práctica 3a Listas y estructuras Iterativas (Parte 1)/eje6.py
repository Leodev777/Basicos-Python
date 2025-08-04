'''
Crea un programa que imprima todos los
numeros primos entre el 2 y el 100. Un numero
primo es un numero positivo y entero mayor que uno que
no tiene un divisor positivo y entero que no sea 1 o si mismo.
'''
num = 0
# bucle que recorre los numeros del 2 al 100
for num in range(2, 101):
    primo = True

    for i in range(2, num):
      if num % i == 0:
            primo = False
    if primo:
        print(num)     
# Para dicho numero, hay alguno que sea sub divisor