# Se definen dos bases de datos como listas de tuplas con información sobre clientes
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]

# Se crean dos conjuntos de nombres de clientes en ambas bases de datos, utilizando una comprensión de listas
nombres1 = set([cliente[0] for cliente in base_datos1])
nombres2 = set([cliente[0] for cliente in base_datos2])

# Se encuentra la intersección de ambos conjuntos, esd decir, los clientes que aparecen en ambas bases de datos
nombres_comunes = nombres1.intersection(nombres2)

# Se imprime la lista de nombres de clientes comunes
print(nombres_comunes)

clientes_comunes = []
for cliente1 in base_datos1:
    if cliente1[0] in nombres_comunes:
        for cliente2 in base_datos2:
            if cliente2[0] == cliente1[0]:
                clientes_comunes.append((cliente1[0], cliente1[1],cliente1[2], cliente2[1], cliente2[2]))
                break

# Se imprime la lista completa de clientes comunes
print(clientes_comunes)
