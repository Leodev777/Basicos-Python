'''
EJERCICIOS 2B
MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra 
(del alfabeto latino) como input. Comprueba 
si esta es una mayúscula o una minúscula.

'''

# --- Pedir al usuario una letra

letra = input("¿Que letra queres comprobar?")

abc_min = "abcdefghijklmnopqrstuvwxyz"
abc_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# --- Comprobacion del input

if len(letra) == 1:

        # --- Condicional
        # Si es mayuscula imprimiremos que es mayuscula
    if letra in abc_min:
        print("Tu letra es minúscula")
            
        # Si es minuscula imprimiremos que es minuscula
    elif letra in abc_may:
        print("Tu letra es Mayúscula")     
            
        # Si es un caracter no reconocido lo indicaremos
    else:
        print("No jodas, eso no es una letra ")    
else:
    print("No te hagas el vivo, ingresa una letra")