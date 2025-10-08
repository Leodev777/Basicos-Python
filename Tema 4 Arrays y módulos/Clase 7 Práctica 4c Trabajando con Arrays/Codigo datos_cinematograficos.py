# Importación del módulo NumPy, utilizado para operaciones vectorizadas y manejo eficiente de arrays
import numpy as np

# --- Creación del dataset ---
# Definimos un array bidimensional que contiene información de películas.
# Cada fila representa una película con los siguientes campos:
# [Título, Género, Duración (minutos), Año de estreno, Rating promedio]
peliculas = np.array([    
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])

# --- Determinar el género más popular ---
# Extraemos la columna de géneros (columna 1) y usamos np.unique para obtener:
#   - los géneros únicos
#   - la cantidad de ocurrencias de cada uno en el dataset
generos, conteos = np.unique(peliculas[:, 1], return_counts=True)

# Ordenamos los géneros según su frecuencia, de mayor a menor.
# np.argsort devuelve los índices que ordenarían el array,
# y [::-1] invierte el orden para que el primero sea el más frecuente.
conteos_desc = np.argsort(conteos)[::-1]

# Seleccionamos el género con mayor cantidad de apariciones
genero_popular = generos[conteos_desc[0]]

# --- Agrupar las películas por década ---
# Convertimos la columna de años a enteros, dividimos por 10 y multiplicamos por 10
# para obtener la década correspondiente (ejemplo: 1995 -> 1990).
decadas = np.unique(peliculas[:, 3].astype(int) // 10 * 10)

# Contamos cuántas películas fueron lanzadas en cada década
conteos_decadas = []
for decada in decadas:
    # Filtramos las películas cuyo año esté dentro de la década actual
    conteo = np.count_nonzero(
        (peliculas[:, 3].astype(int) >= decada) &
        (peliculas[:, 3].astype(int) < decada + 10)
    )
    conteos_decadas.append(conteo)
    print("En la década de", decada, "se crearon", conteo, "películas")

# --- Calcular duración promedio por género ---
# Extraemos la columna de géneros y duraciones
todos_generos = peliculas[:, 1]
duraciones = peliculas[:, 2]

# Creamos un array vacío para almacenar las duraciones medias
duracion_media = np.zeros(len(generos))

# Calculamos el promedio de duración para cada género
for i in range(len(generos)):
    # Seleccionamos las duraciones correspondientes al género actual
    # Convertimos los valores a float antes de calcular la media
    duracion_media[i] = np.mean(duraciones[todos_generos == generos[i]].astype(float))
    print("Duración media de las películas de tipo:", generos[i], "es de", duracion_media[i], "minutos")
