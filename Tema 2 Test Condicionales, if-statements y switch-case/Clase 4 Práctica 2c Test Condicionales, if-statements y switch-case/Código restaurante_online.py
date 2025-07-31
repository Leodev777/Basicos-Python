# ---> Pedir al usuario el tipo de hamburguesa
hamburguesa = input("¿Qué hamburguesa quieres? clásica/vegana: ")

# --- Comprobamos qué hamburguesa ha pedido el usuario
# Si ha elegido la clásica
if hamburguesa.lower() == "clásica" or hamburguesa.lower() == "clasica":
    ## Ofrecemos la opción de elegir un ingrediente extra: queso, jamón, huevo
    ingrediente_extra = input("¿Qué ingrediente extra quieres? Queso / Jamon / Huevo: ")
   
    ## Imprimiremos qué tipo de hamburguesa ha elegido
    if ingrediente_extra.lower() == "queso":
        print("Elegiste una Clásica con Queso")
    elif ingrediente_extra.lower() == "jamon":
        print("Elegiste una Clásica con Jamón")
    elif ingrediente_extra.lower() == "huevo":
        print("Elegiste una Clásica con Huevo")
    else:
        print("Ingrediente no disponible")

# Si ha elegido la vegana
elif hamburguesa.lower() == "vegana":
    ## Ofrecemos la opción de elegir un ingrediente extra: tofu, cebolla caramelizada
    ingrediente_extra = input("¿Qué ingrediente extra quieres? Tofu / Cebolla caramelizada: ")
    ## Imprimiremos qué tipo de hamburguesa ha elegido
    if ingrediente_extra.lower() == "tofu":
        print("Elegiste una Vegana con Tofu")
    elif ingrediente_extra.lower() == "cebolla caramelizada":
        print("Elegiste una Vegana con Cebolla caramelizada")
    else:
        print("Ingrediente no disponible")
        
# Si no elige ninguna de las dos
else:
    print("Lo sentimos, no tenemos ese tipo de hamburguesa")