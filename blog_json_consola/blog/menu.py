def menu_blog():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        print("Opción inválida, ingrese un número del 1 al 7")
        return None


def pedir_datos_post(estados_post):
    """Pide los datos de un post. Devuelve None si algún campo queda vacío."""
    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()
    tags = [t.strip() for t in input("Tags (separados por coma): ").split(",") if t.strip()]
    estado = input(f"Estado ({', '.join(estados_post)}): ").strip().lower()

    if not titulo or not contenido or not tags or not estado:
        print("Error: no se permiten campos vacíos.")
        return None
    if estado not in estados_post:
        print(f"Error: estado inválido. Opciones: {', '.join(estados_post)}")
        return None
    return titulo, contenido, tags, estado