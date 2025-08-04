# --- Pedir numero al usuario
num = int(input("Introduce la anchura con un número entero: "))
# --- bucle ascendente
for x in range(1, num + 1): # 1 hasta num incluido ya que el sistema toma el numero menos 1 entonces lo debemos agregar para compensarlo
    print("*" * x +  " " * (num - x)) # espacio para alinear a la derecha
# --- bucle descendente
for x in range(num - 1, 0, -1): #  # desde num - 1 hasta 1 incluido
    print("*" * x + " " * (num - x)) # espacio para alinear a la derecha
# --- fin del programa
print("Fin del programa")
