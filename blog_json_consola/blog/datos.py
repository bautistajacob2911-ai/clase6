import json

from blog.modelos import Autor

RUTA_POSTS = "posts.json"

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blogs = {"Python", "Arduino", "Electrónica"}

perfil_autor = Autor(
    nombre="Bautista",
    bio="Aspirante a ingeniero",
    redes_sociales=["Instagram:Jacobb_041", "Linkedin: Bautista_Jacob"],
    especialidad="Técnico en Informática",
)


def cargar_posts(ruta=RUTA_POSTS):
    """Devuelve una lista de diccionarios. Si hay algún problema devuelve []."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"Aviso: '{ruta}' no existe. Se inicia con un blog vacío.")
        return []
    except OSError as e:
        print(f"Error al leer '{ruta}': {e}")
        return []

    if not contenido.strip():
        print(f"Aviso: '{ruta}' está vacío. Se inicia con un blog vacío.")
        return []

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as e:
        print(f"Error: '{ruta}' tiene un JSON inválido ({e}). Se inicia con un blog vacío.")
        return []

    if not isinstance(datos, list):
        print(f"Error: '{ruta}' debe contener una lista de posts.")
        return []
    return datos


def guardar_posts(posts, ruta=RUTA_POSTS):
    """Convierte los posts a diccionarios y los guarda en JSON."""
    try:
        lista = []
        for p in posts:
            if not hasattr(p, "a_diccionario"):
                raise TypeError(f"El objeto {p!r} no se puede convertir a diccionario.")
            lista.append(p.a_diccionario())
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)
        print(f"Posts guardados en '{ruta}'.")
        return True
    except TypeError as e:
        print(f"Error de conversión: {e}")
    except OSError as e:
        print(f"Error al escribir '{ruta}': {e}")
    return False