
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

red_social_sin_duplicados = []
for usuario, amigos in red_social:
    amigos_sin_duplicados = list(set(amigos))
    red_social_sin_duplicados.append((usuario, amigos_sin_duplicados))

amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    amigos_por_usuario.append((usuario, len(amigos)))

amigos_por_usuario = tuple(amigos_por_usuario)

print("Usuarios con numero de amistades:", amigos_por_usuario)

lista_usuarios = [tupla[0] for tupla in amigos_por_usuario]
numero_amigos = [tupla[1] for tupla in amigos_por_usuario]

indice_con_mas_amigos = numero_amigos.index(max(numero_amigos))
usuario_con_mas_amigos = lista_usuarios[indice_con_mas_amigos]

print("Usuario con mayor conexion:", usuario_con_mas_amigos)

