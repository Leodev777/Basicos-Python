# importacion de modulos
import numpy as np

# datos de entrada

import numpy as np

datos = np.array([
    ['2022-01-01', 'Componente 1', 'Lote A', 80],
    ['2022-01-15', 'Componente 1', 'Lote B', 90],
    ['2022-02-01', 'Componente 2', 'Lote C', 85],
    ['2022-02-15', 'Componente 2', 'Lote D', 95],
    ['2022-03-01', 'Componente 1', 'Lote E', 75],
    ['2022-03-15', 'Componente 2', 'Lote F', 90],
    ['2022-03-30', 'Componente 1', 'Lote G', 88],
    ['2022-04-10', 'Componente 1', 'Lote H', 92],
    ['2022-04-25', 'Componente 2', 'Lote I', 81],
    ['2022-05-05', 'Componente 2', 'Lote J', 89],
    ['2022-05-20', 'Componente 1', 'Lote K', 78],
    ['2022-06-01', 'Componente 2', 'Lote L', 84],
    ['2022-06-15', 'Componente 1', 'Lote M', 91],
    ['2022-07-01', 'Componente 1', 'Lote N', 87],
    ['2022-07-15', 'Componente 2', 'Lote O', 79],
    ['2022-07-30', 'Componente 2', 'Lote P', 93],
    ['2022-08-10', 'Componente 1', 'Lote Q', 85],
    ['2022-08-25', 'Componente 2', 'Lote R', 90],
    ['2022-09-05', 'Componente 1', 'Lote S', 82],
    ['2022-09-20', 'Componente 1', 'Lote T', 94],
    ['2022-10-01', 'Componente 2', 'Lote U', 76],
    ['2022-10-15', 'Componente 1', 'Lote V', 88],
    ['2022-11-01', 'Componente 1', 'Lote W', 91],
    ['2022-11-15', 'Componente 2', 'Lote X', 83],
    ['2022-11-30', 'Componente 2', 'Lote Y', 86],
    ['2022-12-10', 'Componente 1', 'Lote Z', 95],
    ['2023-01-01', 'Componente 2', 'Lote AA', 80],
    ['2023-01-15', 'Componente 1', 'Lote AB', 84],
    ['2023-02-01', 'Componente 1', 'Lote AC', 77],
    ['2023-02-15', 'Componente 2', 'Lote AD', 92],
    ['2023-03-01', 'Componente 2', 'Lote AE', 89],
    ['2023-03-15', 'Componente 1', 'Lote AF', 81],
    ['2023-03-30', 'Componente 2', 'Lote AG', 94],
    ['2023-04-10', 'Componente 2', 'Lote AH', 86],
    ['2023-04-25', 'Componente 1', 'Lote AI', 90],
    ['2023-05-05', 'Componente 2', 'Lote AJ', 75],
    ['2023-05-20', 'Componente 1', 'Lote AK', 93],
    ['2023-06-01', 'Componente 1', 'Lote AL', 82],
    ['2023-06-15', 'Componente 2', 'Lote AM', 88],
    ['2023-07-01', 'Componente 1', 'Lote AN', 91],
    ['2023-07-15', 'Componente 1', 'Lote AO', 85],
    ['2023-07-30', 'Componente 2', 'Lote AP', 79],
    ['2023-08-10', 'Componente 2', 'Lote AQ', 92],
    ['2023-08-25', 'Componente 1', 'Lote AR', 83]
])


# identificamos el componente con la puntuacion mas alta

tipos_componentes = datos [:,1]
tipos_unicos = np.unique(tipos_componentes)
calidad_datos = datos [:,3].astype(float)

for tipo in tipos_unicos:
    np.mean(calidad_datos[tipos_componentes == tipo])
    print("la calicad media del", tipo, "es de", np.mean(calidad_datos[tipos_componentes == tipo]))

