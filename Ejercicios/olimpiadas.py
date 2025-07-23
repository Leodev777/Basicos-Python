# Pedimos el tiempo completo en formato: minutos segundos centesimas
tiempo_str = input("Ingresa el tiempo de Juan (formato: minutos segundos centesimas): ")

# Extraer minutos, segundos y centésimas
minutos_juan, segundos_juan, centesimas_juan = tiempo_str.split(" ")

# Convertimos los valores a números y calculamos el tiempo total en segundos
tiempo_total_segundos = float(minutos_juan) * 60 + float(segundos_juan) + float(centesimas_juan) * 0.01

# Mostrar el resultado
print("Tiempo total en segundos:", tiempo_total_segundos)


# Sustituir partes del string: replace()

# Encontrar un srting dentro de otro string: find() ---> Si no encuentra nada muesta -1 por consola

# Corprueba que el srting empieza de cierta forma: Startwith()

# Comprueba que el string termina de cirta forma: endswith()

# Combinar y conctatenar textos!: 

# nombre = 'Juan'
# apellido = 'Gomez'
# nombre_completo = nombre + " " + apellido
# print(nombre_completo)

# Cosola printea "Juan Gomez"

# nombre = 'Juan'
# apellido = 'Gomez?
# nombre_completo = nombre + " " + apellido
# print("¡Hola, "" + nombre_completo.title() + "!")

# Printea por consola ¡Hola, Juan Gomez!


# tabs y saltos de linea: Tab - \t Salto de linea \

# Podemos acceder a los componentes del srting mediante sus indices:

# nombre = 'Juan'
# print(nombre[0])
# J

# O extraer partes del mismo:0 a 4

# Print(usuario[0:5])
# Print YoSoy

# Revertir un sring: Recorre la cadena -1
# cadena = 'abcde'
# print(cadena[::-1])
# edcba

# Consultar tamaños
# caena = 'abcde'
# print(len(cadena))
# 5

# errores tipicos: pongamos una comilla donde no toca ej:
# A'lejo
# para que python no se confunda con error de sintaxis 
# solo debemos agregar ""

# Numeros enteros:

# >> 2 + 3
# 5
# >> 3 - 2
# 1

# Potencia: **

# >> 3**2
# 9
# >> 3**3
# 27

# Python sirmpre sigue el orden matematico de las operaciones.

# + suma
# - resta
# / division
# * multiplicacion
# ** potenciacion
# % modulo o resto

# python sigue un orden: 
# 1. Contenido de los parentesis
# 2. exponentes
# 3. multiplicacion y division
# 4. suma y resta

# Como combinamos numeros y strings?

# primero debemos tener el tipo de variable para poder combinar, para solucionar esto
# usamos STR comvirte numeros en sting ej:

# numero_dias = 365
# mensaje = 'El año tiene ' + str(numero_dias) + ' dias'
# print(mensaje)
# El año tiene 365 dias



