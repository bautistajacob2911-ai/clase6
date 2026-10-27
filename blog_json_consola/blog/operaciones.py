def listar_posts(posts):
    for i in range(len(posts)):
        print("El título del post", i, "es:", posts[i]["título"])
        print("El autor del post", i, "es:", posts[i]["autor"]["nombre"])


def buscar_por_titulo(posts, termino):
    encontrado = False
    for post in posts:
        if termino in post["título"].lower():
            print("Post encontrado:", post["título"])
            print("Autor del post encontrado:", post["autor"]["nombre"])
            encontrado = True
    if not encontrado:
        print("No se encontró ningún post con el título ingresado")  


def filtrar_por_tag(posts, tag):
    encontrado = False
    for post in posts:
        # Convertimos la lista/tupla de tags a minúsculas
        tags_lower = [t.lower() for t in post["tags"]]
        if tag in tags_lower:
            print("Post encontrado:", post["título"])
            print("Autor del post encontrado:", post["autor"]["nombre"])
            encontrado = True
     
    if not encontrado:
        print("No se encontró ningún post con el tag ingresado")
