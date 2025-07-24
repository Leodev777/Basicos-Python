hasPagado = input()
precio = float(input())
# Condicional IF anidado
if hasPagado == "False":
    print('No has pagado aun')
    if precio <= 20:
        print('Tienes que pagar menos de 20 pesos')
    else:
        print('Tienes que pagar mas de 20 pesos')
else:
    print('Ya pagaste')        