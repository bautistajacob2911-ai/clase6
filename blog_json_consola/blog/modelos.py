class Autor:
    def __init__(self, nombre, bio, redes_sociales, especialidad):
        self.nombre = nombre
        self.bio = bio
        self.redes_sociales = redes_sociales
        self.especialidad = especialidad

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "redes_sociales": list(self.redes_sociales),
            "especialidad": self.especialidad,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError("El autor debe ser un diccionario.")
        campos = ["nombre", "bio", "redes_sociales", "especialidad"]
        faltantes = [c for c in campos if c not in datos]
        if faltantes:
            raise ValueError(f"Autor incompleto, faltan los campos: {', '.join(faltantes)}")
        return cls(**{c: datos[c] for c in campos})


class Post:
    def __init__(self, id_post, titulo, contenido, autor, tags, estado):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # instancia de Autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        autor = self.autor.a_diccionario() if isinstance(self.autor, Autor) else None
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": autor,
            "tags": list(self.tags) if isinstance(self.tags, (list, tuple)) else self.tags,
            "estado": self.estado,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError("El post debe ser un diccionario.")
        campos = ["id", "titulo", "contenido", "autor", "tags", "estado"]
        faltantes = [c for c in campos if c not in datos]
        if faltantes:
            raise ValueError(f"Post incompleto, faltan los campos: {', '.join(faltantes)}")
        autor = Autor.desde_diccionario(datos["autor"])
        return cls(datos["id"], datos["titulo"], datos["contenido"],
                   autor, datos["tags"], datos["estado"])


class Blog:
    def __init__(self, estados_post=("borrador", "publicado", "archivado")):
        self.posts = []
        self.estados_post = estados_post

    def siguiente_id(self):
        return max((p.id for p in self.posts), default=0) + 1

    def crear_post(self, titulo, contenido, autor, tags, estado):
        nuevo = Post(self.siguiente_id(), titulo, contenido, autor, tags, estado)
        self.posts.append(nuevo)
        print(f"¡Post '{titulo}' creado con éxito! (ID {nuevo.id})")
        return nuevo

    def obtener_todos_los_posts(self):
        return self.posts

    def posts_a_diccionarios(self):
        return [p.a_diccionario() for p in self.posts]

    def cargar_desde_diccionarios(self, lista):
        """Reconstruye los posts desde una lista de diccionarios. Omite los inválidos."""
        self.posts = []
        for i, d in enumerate(lista):
            try:
                self.posts.append(Post.desde_diccionario(d))
            except ValueError as e:
                print(f"Se omitió el elemento {i} del JSON: {e}")

    def listar_posts(self):
        if not self.posts:
            print("No hay posts cargados en el blog.")
            return
        for i, post in enumerate(self.posts):
            nombre = post.autor.nombre if isinstance(post.autor, Autor) else "Desconocido"
            print(f"\n--- Post {i} ---")
            print(f"ID: {post.id}")
            print(f"Título: {post.titulo}")
            print(f"Autor: {nombre}")
            print(f"Estado: {post.estado}")
            print(f"Tags: {', '.join(post.tags)}")

    def buscar_por_titulo(self, termino):
        termino = termino.strip().lower()
        encontrados = [p for p in self.posts if termino in p.titulo.lower()]
        if not encontrados:
            print("No se encontró ningún post con el título ingresado.")
            return []
        for p in encontrados:
            print(f"\n[Post encontrado] {p.titulo} - Autor: {p.autor.nombre}")
        return encontrados

    def filtrar_por_tag(self, tag):
        tag = tag.strip().lower()
        encontrados = [p for p in self.posts if tag in [t.lower() for t in p.tags]]
        if not encontrados:
            print(f"No se encontró ningún post con el tag '{tag}'.")
            return []
        for p in encontrados:
            print(f"\n[Post con tag '{tag}'] {p.titulo} - Autor: {p.autor.nombre}")
        return encontrados

    def validar_post(self, post):
        errores = []
        if not post.titulo or not str(post.titulo).strip():
            errores.append("Título vacío o faltante")
        if not post.contenido or not str(post.contenido).strip():
            errores.append("Contenido vacío o faltante")
        if not isinstance(post.autor, Autor):
            errores.append("Autor inválido o faltante")
        if not isinstance(post.tags, (list, tuple)):
            errores.append("Tags inválidos o faltantes")
        if post.estado not in self.estados_post:
            errores.append("Estado inválido o faltante")
        return errores

    def validar_posts(self):
        if not self.posts:
            print("No hay posts para validar.")
            return False
        todos_validos = True
        for i, post in enumerate(self.posts):
            errores = self.validar_post(post)
            if errores:
                todos_validos = False
                print(f"Post {i} (ID {post.id}) inválido:")
                for e in errores:
                    print(f"  - {e}")
            else:
                print(f"Post {i} (ID {post.id}): válido")
        return todos_validos