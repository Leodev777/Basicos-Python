
# Pedimos por pantalla los datos del usuario.

genero = input("Elige tu género (chico/chica): ")

# chico/chica

nombre = input("Por favor, me dirias tu nombre?: ")
# Nombre
nombre_chicas_A = "EHIJKLM"
nombre_chicos_A = "ABCDEFGHRSTUVWXYZ"


# Elegir grupo que corresponda
# chica

if genero.lower() == "chica":
    if nombre[0].upper() in nombre_chicas_A:
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")    


## E hasta la M ---> enviamos el usuario al grupo A
## el resto --> enviamos el usuario al grupo B


# chico
elif genero.lower() == "chico":
    if nombre[0].upper() in nombre_chicos_A:
        print("Tu grupo es el A")
    else:
        print("Tu gupo es el B")        

## A hasta la H, R hasta la Z ---> enviamos el usuario al grupo A
## el resto ---> enviamos el usuario al grupo B

else: print("Eso no es un sexo")