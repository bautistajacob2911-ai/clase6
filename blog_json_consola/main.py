from blog.datos import cargar_posts, guardar_posts, estados_post, perfil_autor
from blog.menu import menu_blog, pedir_datos_post
from blog.modelos import Blog


def main():
    blog = Blog(estados_post)
    blog.cargar_desde_diccionarios(cargar_posts())

    while True:
        opcion = menu_blog()
        if opcion is None:
            continue
        if opcion == 1:
            blog.listar_posts()
        elif opcion == 2:
            blog.buscar_por_titulo(input("Ingrese el título que desea buscar: "))
        elif opcion == 3:
            blog.filtrar_por_tag(input("Ingrese el tag que desea buscar: "))
        elif opcion == 4:
            datos = pedir_datos_post(estados_post)
            if datos:
                titulo, contenido, tags, estado = datos
                blog.crear_post(titulo, contenido, perfil_autor, tags, estado)
        elif opcion == 5:
            blog.validar_posts()
        elif opcion == 6:
            guardar_posts(blog.obtener_todos_los_posts())
        elif opcion == 7:
            guardar_posts(blog.obtener_todos_los_posts())
            print("Saliendo... ¡hasta luego!")
            break
        else:
            print("Opción inválida, ingrese un número del 1 al 7")


if __name__ == "__main__":
    main()
    
