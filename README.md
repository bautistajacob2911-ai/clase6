[README.md](https://github.com/user-attachments/files/34052400/README.md)
# Blog por consola (POO + JSON)

## Qué hace
Gestiona posts de un blog desde la consola: listar, buscar por título, filtrar por tag, crear, validar y guardar en `posts.json`.

## Ejecución
Desde la raíz del proyecto (donde está `main.py` y la carpeta `blog/`):

    python main.py

## Estructura
- `main.py`: punto de entrada. Carga datos, crea el `Blog` y maneja el menú.
- `blog/modelos.py`: clases `Autor`, `Post` y `Blog`.
- `blog/datos.py`: carga y guardado de `posts.json`, estados y autor por defecto.
- `blog/menu.py`: menú y entrada de datos del usuario.

## Clases
- **Autor**: nombre, bio, redes sociales y especialidad. Se convierte a/desde diccionario.
- **Post**: id, título, contenido, tags, estado y una instancia de `Autor`. Se convierte a/desde diccionario.
- **Blog**: guarda la lista de `Post` y centraliza listar, buscar, filtrar, crear y validar.

## Persistencia
- Al iniciar, `cargar_posts()` lee `posts.json` y devuelve diccionarios; `Blog.cargar_desde_diccionarios()` los convierte en objetos `Post`/`Autor`.
- Al guardar (opción 6 o al salir), `guardar_posts()` convierte cada `Post` con `a_diccionario()` y lo escribe con `json`.
- Si el archivo no existe, está vacío o es inválido, se informa y se inicia con un blog vacío. Los posts incompletos se omiten con un mensaje.

## Cambios respecto al checkpoint anterior
- Se pasó de listas y diccionarios sueltos a clases (`Autor`, `Post`, `Blog`).
- Se agregó persistencia en JSON y la opción de crear posts.
- La lógica de `operaciones.py` y `validaciones.py` pasó a la clase `Blog` (esos archivos ya no se usan).
- Profe, aviso que cree otro repositorio porque si actualizo el mismo cuando me corrijan la anterior entrega el link te lleva al archivo actualizado, por lo que no se podrá ver el archivo anterior.
