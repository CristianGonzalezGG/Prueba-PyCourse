class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar_libro(self):
        self.disponible = False

    def devolver_libro(self):
        self.disponible = True

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def listar_libros_disponibles(self):
        libros_disponibles = [libro for libro in self.libros if libro.disponible]
        return libros_disponibles

def agregar_libro_a_biblioteca(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    nuevo_libro = Libro(titulo, autor)
    biblioteca.agregar_libro(nuevo_libro)

# Ejemplo de uso
mi_biblioteca = Biblioteca()

while True:
    print("\n1.Agregar libro")
    print("2.Mostrar libros disponibles")
    print("3.Buscar libros por nombre")
    print("4.Alquilar libro")
    print("5.Devolver libro")
    option = input("Ingrese una opción: ")

    if option == "1":
        agregar_libro_a_biblioteca(mi_biblioteca)
    elif option == "2":
        libros_disponibles = mi_biblioteca.listar_libros_disponibles()
        print("\nLibros disponibles:")
        for libro in libros_disponibles:
            print(f"- {libro.titulo} ({libro.autor})")
    elif option == "3":
        buscar_libro = input("Ingrese el libro a buscar: ")
        libro_encontrado = mi_biblioteca.buscar_libro(buscar_libro)
        if libro_encontrado not in libros_disponibles:
            print(f"El libro '{libro_encontrado.titulo}' no está disponible y su autor es ({libro_encontrado.autor}).")
        elif libro_encontrado:
            print(f"El libro '{libro_encontrado.titulo}' no disponible y su autor es ({libro_encontrado.autor}).")
        else:
            print(f"No se encontró el libro '{buscar_libro}'.")
    elif option == "4":
        libro_a_alquilar = input("Ingrese el título del libro que desea alquilar: ")
        libro_encontrado = mi_biblioteca.buscar_libro(libro_a_alquilar)
        if libro_encontrado and libro_encontrado.disponible:
            libro_encontrado.prestar_libro()
            print(f"Se ha alquilado el libro '{libro_encontrado.titulo}'.")
        elif libro_encontrado and not libro_encontrado.disponible:
            print(f"El libro '{libro_encontrado.titulo}' no está disponible.")
        else:
            print(f"No se encontró el libro '{libro_a_alquilar}'.")
    elif option == "5":
        libro_a_devol = input("Ingrese el título del libro que desea alquilar: ")
        libro_encontradoD = mi_biblioteca.buscar_libro(libro_a_devol)
        if libro_encontradoD and libro_encontradoD.disponible:
            libro_encontradoD.devolver_libro()
            print(f"Se ha devuelto el libro '{libro_encontradoD.titulo}'.")
        elif libro_encontradoD and not libro_encontradoD.disponible:
            print(f"El libro '{libro_encontradoD.titulo}' no se ah alquilado.")
        else:
            print(f"No se encontró el libro '{libro_a_devol}'.")
    
    elif option == "6":
        break

