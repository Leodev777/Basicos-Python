# ¿ Que es una estructura iterativa o bucle ?
# Es una secuencia de instrucciones que se ejecuta repedidamente mientras se cumpla cienta
# condicion establecida previamente.

# Estructuras en Python ---> WHILE = MIENTRAS
#                       ---> FOR = PARA

# Repasemos un toque de sintaxis para recordar
# Pseint:
# MIENTRAS expr_logica HACER
#   ejecucion_codigo
#FINMIENTRAS

# MIENTRAS (expr_logica_1) OP LOG (expr_logica2) HACER
# FINMIENTRAS

# En python:

# while (expresion_logica):
#    ejecucion_codigo
# while (expr_logica_1) and/or (expr_logica_2)
#    ejcucion_codigo

# Para entrar en el ciclo WHILE debe cuplirse la condicion de la expresion logica
# pero debe haber alguna opcion para que la expresion no se cumpla y se salga del bucle
# debe cambiarse el valor de la expresion logica


import time

temporizador = int(input('Cuantos segundos quieres que tenga el temporizador?'))

print('Comienza el temporizador')

while (temporizador > 0):

    print('Quedan ', temporizador, 'segundos')
    time.sleep(1)
    temporizador = temporizador -1


print('¡El temporizador ha finalizado!')  


# Bucle PARA en Pseint

# PARA i = valor_inicial HASTA valor_final CON PASO incre_decre HACER
#       ejecucion_codigo
# FINPARA

# En python

# FOR i IN range(valor_inicial, valor_final, paso):
#       ejecucion_codigo


temporizador = int(input("Cargar segundos"))


print("Comienza el tiempo")

for i in range(temporizador,0,-1): # ---> "i" va hasta -1 para contemplar el 0
    print("quedan ", i, "segundos")
    time.sleep(1)

print("finalizo")

# Para mas claridad

for i in range(0,3): # ---> "i" va de 0 a 2
    print(i)

# Como interrumpimos un bucle? BREAK = romper

# for valor en rango
#    set_instrucciones
#    if condicion_a
#    break ---> punto de salida
#set_intrucciones

# while condicion
#    set_instrucciones
#    if condicion_a:
#    brack ---> punto de salida
# set_instrucciones

# salimos del while y continua con las siguiente instruccion

# en rengue podemos agregar el 0 pero podemos agregar diratemente el numero final ya que por defecto comienza con 0

for i in rangue(5):
    if i == 3:
        break
    print(i)
print("Fuera de aqui")

# CONTINUE

# for valor en rango
#   set_instrucciones
#   if condicion_a:
#       continue --> vuelve al for
# set_instrucciciones

for i in range(5):
    if i == 3:
        print("Estoy dentro del if")
        continue
        print("Estoy dentro del if")
    print("Estamos fuera del bucle reeey!")    

# CONTIUE Y BEACK:
# Son estrucutras muy utiles y comodas a la hora de escribir el cdigo pero
# hay que intetar no abusar de ellas
# crear muchos exit point con break complica la lectura
# y el flujo del codigo, es prefierible que se priorice salir del bucle de manera natural

# BRACK: EXIT POINT 
# CONTINUE: EXIT POINT que vuelve al for

# La base de la programacion estructurada es tener unos puntos de entrada y puntos de salida bien definidos
# entonces el problema que trae abusar de esto, crearemos trampa de codigos
# y al tener codigos muy largos, se arma la de San Quintin

# Regla de estilo a seguir: piensa si hay alguna manera de escribir el codigo
# sin usar break y continue y que mantenga el codigo solido, sencillo y elegante
# si ves que esto no es posible entonces si usa brack y continue
