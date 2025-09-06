'''
Supongamos que eres un administrador de sistemas 
y necesitas validar el acceso de los usuarios a 
un sitio web. Crea un script que verifique si el 
+nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos.

'''
# lista de usuarios y contraseñas válidos
usuarios = ["admin", "usuario1", "usuario2"]  
# Se crea una lista con tres nombres de usuario permitidos.

# lista de contraseñas válidas
passwords = ["admin123", "pass1", "pass2"]  
# Se crea una lista con las contraseñas correspondientes a cada usuario, en el mismo orden.

# pedir al usuario que ingrese su nombre de usuario
usuario = input("Ingresa tu usuario: ")  
# Se solicita al usuario que escriba su nombre de usuario y se guarda en la variable 'usuario'.

# pedir al usuario que ingrese su contraseña
password = input("Ingresa tu contraseña: ")  
# Se solicita al usuario que escriba su contraseña y se guarda en la variable 'password'.

# recorrer la lista de usuarios y contraseñas
# con while debemos inicializar la variable
autorizado = False  
# Se crea una variable booleana 'autorizado' para indicar si el acceso será concedido o no.  
# Inicialmente está en False, es decir, no autorizado.

x = 0  
# Se inicializa un contador 'x' en 0, que servirá para recorrer las listas.

while x < len(usuarios):  
    # Mientras 'x' sea menor que la cantidad de usuarios en la lista, el bucle seguirá ejecutándose.
    
    print(usuarios[x], passwords[x])  
    # Muestra en pantalla el usuario y contraseña actual en la posición 'x'.  
    # (Esto normalmente se usaría solo para depuración, porque revela contraseñas).

    if usuario == usuarios[x] and password == passwords[x]:  
        # Compara si el usuario y la contraseña ingresados coinciden con los de la posición 'x'.
        autorizado = True  
        # Si hay coincidencia, cambia la variable 'autorizado' a True (acceso permitido).

    x = x + 1  
    # Incrementa el contador 'x' en 1 para pasar al siguiente usuario y contraseña en la lista.

if autorizado == True:  
    # Cuando termina el bucle, se revisa si 'autorizado' cambió a True.
    print("Acceso autorizado")  
    # Si es True, se muestra un mensaje de éxito.
else:  
    print("Acceso no autorizado")  
    # Si sigue siendo False, significa que el usuario/contraseña no estaban en las listas, 
    # y se niega el acceso.
