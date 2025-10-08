# Importación del módulo NumPy para manipular arrays de forma eficiente
import numpy as np

# --- Creación del dataset ---
# Cada fila representa un registro de producción con:
# [Fecha, Tipo de componente, Lote, Puntuación de calidad]
datos = np.array([
    ['2022-01-01', 'Componente 1', 'Lote A', 80],
    ['2022-01-15', 'Componente 1', 'Lote B', 90],
    ['2022-02-01', 'Componente 2', 'Lote C', 85],
    ['2022-02-15', 'Componente 2', 'Lote D', 95],
    ['2022-03-01', 'Componente 1', 'Lote E', 75],
    ['2022-03-15', 'Componente 2', 'Lote F', 90]
])

# --- Identificar el componente con la puntuación media más alta ---
# Extraemos la columna con los nombres de componentes
tipos_componente = datos[:, 1]

# Obtenemos una lista de tipos únicos sin repeticiones
tipos_unicos = np.unique(tipos_componente)

# Extraemos la columna de puntuaciones de calidad y la convertimos a tipo numérico
calidad = datos[:, 3].astype(float)

# Inicializamos un array para almacenar el promedio de calidad por tipo de componente
promedios = np.zeros(len(tipos_unicos))

# Recorremos cada tipo de componente y calculamos su puntuación promedio
i = 0
for tipo in tipos_unicos:
    # Seleccionamos las filas que coinciden con el tipo actual
    # y calculamos la media de sus puntuaciones
    promedios[i] = np.mean(calidad[tipos_componente == tipo])
    i += 1

# Identificamos el índice del valor máximo dentro de los promedios
indice_maximo = np.argmax(promedios)

# Obtenemos el nombre del componente con la puntuación media más alta
tipo_mejor_calidad = tipos_unicos[indice_maximo]

print("El tipo de componente con la puntuación de calidad más alta es:", tipo_mejor_calidad)

# --- Contar cuántos componentes se produjeron en cada mes ---
# Extraemos las fechas completas
fechas = datos[:, 0]

# Obtenemos los meses en formato 'YYYY-MM' y contamos ocurrencias
# La expresión [fecha[0:7] for fecha in fechas] genera una lista de meses a partir de las fechas
meses, counts = np.unique([fecha[0:7] for fecha in fechas], return_counts=True)

# Mostramos la cantidad de componentes producidos en cada mes
for i in range(len(meses)):
    print("Mes:", meses[i], "Cantidad producida:", counts[i])

# --- Calcular la puntuación de calidad promedio de cada tipo de componente ---
# Inicializamos un array para almacenar los promedios de nuevo (redundante, pero mantiene la estructura del script)
promedio_por_tipo = np.zeros(len(tipos_unicos))

# Recalculamos la media de cada tipo para mostrar los valores finales
for i in range(len(tipos_unicos)):
    promedio_por_tipo[i] = np.mean(calidad[tipos_componente == tipos_unicos[i]])
    print("La puntuación de calidad promedio para el", tipos_unicos[i], "es:", promedio_por_tipo[i])
