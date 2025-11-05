# diccionario base de datos
asistencias = dict()

# Registrar asistencias de estudiantes
asistencias["Estudiante1"] = ["2022-01-01", "2025-10-03", "2025-09-05"]
asistencias["Estudiante2"] = ["2022-01-02", "2025-10-05", "2025-09-07"]
asistencias["Estudiante3"] = ["2022-01-01", "2025-10-07", "2025-09-09"]

# Agregar nuevas fechas
asistencias["Estudiante1"].append("2025-01-07")
asistencias["Estudiante2"].append("2025-01-09")

# Mostrar la lista de estudiantes y las fechas en las que asistieron
print("Registro de Asitencias:")
for estudiante, fechas in asistencias.items():
    print("Estudiante:", estudiante)
    print("Fechas de Asistencia:", ", ".join(fechas))
    print()