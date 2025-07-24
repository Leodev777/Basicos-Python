# muchas veces pueden ser util comprobar si varias condiciones
# se cumplen simultaneamente
# EJ
# nombre_usuario = 'Juan'
# edad = 16
# (nombre_usuario = 'juan') and (edad >= 21)
# False

# ______________-

# En otras ocasiones nos basta si una de las varias condciones se cumplen
# Ej hay un local en el que solo pueden entrar gente mayor de edad

edad_juan = 17
edad_lucas = 22
(edad_juan > 18) or (edad_lucas > 18)
# TRUE
edad_juan = 17
edad_lucas = 16
(edad_juan > 18) or (edad_lucas > 18)
# FALSE
