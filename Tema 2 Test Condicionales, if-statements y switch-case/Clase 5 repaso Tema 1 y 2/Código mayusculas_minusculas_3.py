
# pedir datos al usuario
letra = input("Introduce una letra: ")

#mayuscula 65 -- 90
#minusculas 97 -- 122

if 65 <= ord(letra) <=90: 
    print("La letra es mayuscula")
elif 97 <= ord(letra) <= 122:
    print("La letra es minuscula")
else: 
    print("La letra introducida no es valida")
