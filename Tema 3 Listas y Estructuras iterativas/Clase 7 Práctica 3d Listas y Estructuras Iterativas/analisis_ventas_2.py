'''
Supongamos que eres el propieratrio de una tienda y tienes una lista de
ventas de los ultimos 30 dias. Quieres analizar estas ventas para
obtener informacion util sobre el rendimiento de tu tienda.

'''
# Lista de ventas de los ultimos 30 dias
# Lista de los dias de la semana
# Lista donde guardamos las ventas por dia de la semana

# Recorrer lista de ventas con un bucle
## Sumar para cada dia de la semana las ventas realizadas

## imprimir las ventas realizadas para cada dia de la semana
## a lo largo de ese mes


venta_mes = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 2400, 4000]
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
ventas_totales = [0, 0, 0, 0, 0, 0, 0]

dia_venta = 0
for venta in venta_mes:
    # sumar venta al dia correspondiente
    ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
    # pasar al siguiente dia de la semana
    dia_venta = dia_venta + 1
    # si dia_venta es 7, volver a 0
    if dia_venta == 7:
        dia_venta = 0

    print("Ventas por dia de la semana:", dia_venta)