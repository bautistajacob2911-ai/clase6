def validar_posts(posts,estados_post):
    valido = True
    try:
        post_a_validar = int(input(f"Ingrese el número del post que desea validar (0 al {len(posts)-1}): "))
        target = posts[post_a_validar]
    except (ValueError, IndexError):
        print("Índice de post no válido.")
        return False


    # Validar Título
    if "título" not in target or target["título"].strip() == "":
        print("Post inválido: Título vacío o faltante")
        valido = False


    # Validar Contenido
    if "contenido" not in target or target["contenido"].strip() == "":
        print("Post inválido: Contenido vacío o faltante")
        valido = False


    # Validar Autor
    if "autor" in target and isinstance(target["autor"], dict):
        pass
    else:
        print("Post inválido: Autor inválido o faltante")
        valido = False


    # Validar Tags (pueden ser lista o tupla)
    if "tags" in target and isinstance(target["tags"], (list, tuple)):
        pass
    else:
        print("Post inválido: Tags inválidos o faltantes")
        valido = False


    # Validar Estado
    if "estado" in target and target["estado"] in estados_post:
        pass
    else:
        print("Post inválido: Estado inválido o faltante")
        valido = False


    return valido

