# Proyecto: Sistema de Gestión de Biblioteca
# Descripción:
# Crea un sistema de gestión de biblioteca en Python que permita a los usuarios interactuar con una colección de libros. El sistema debería incluir las siguientes funcionalidades:
# Clase Libro:
# Define una clase Libro con atributos como titulo, autor, anio_publicacion, y disponible (indicando si el libro está disponible para préstamo).
# Clase Biblioteca:
# Crea una clase Biblioteca que almacene una lista de libros.
# Implementa métodos para:
# Agregar un libro a la biblioteca.
# Buscar un libro por título o autor.
# Prestar un libro (cambiar su estado a no disponible).
# Devolver un libro (cambiar su estado a disponible).
# Manejo de Colecciones:
# Utiliza listas, diccionarios y/o tuplas para organizar la colección de libros en la biblioteca.
# Interacción con el Usuario:
# Implementa un programa principal que permita a los usuarios:
# Ver la lista de libros disponibles.
# Buscar libros por título o autor.
# Prestar y devolver libros.
# Manejo de Errores:
# Implementa manejo de excepciones para casos como buscar un libro que no está en la biblioteca o tratar de devolver un libro que no ha sido prestado.
# Principios SOLID:
# Intenta seguir los principios SOLID en el diseño de tus clases, como la responsabilidad única y la inversión de dependencias.
# Funciones Lambda:
# Puedes utilizar funciones Lambda para realizar búsquedas más específicas o para filtrar la lista de libros de alguna manera.
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
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def listar_libros_disponibles(self):
        libros_disponibles = [libro for libro in self.libros if libro.disponible]
        if libros_disponibles:
            return libros_disponibles
        else:
            return None

# Función para agregar un libro a la biblioteca
def agregar_libro_a_biblioteca(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    nuevo_libro = Libro(titulo, autor)
    biblioteca.agregar_libro(nuevo_libro)

# Ejemplo de uso
mi_biblioteca = Biblioteca()

while True:
    print("\n1. Agregar libro")
    print("2. Mostrar libros disponibles")
    print("3. Buscar libros por nombre")
    print("4. Alquilar libro")
    print("5. Devolver libro")
    print("6. Salir")
    option = input("Ingrese una opción: ")

    if option == "1":
        agregar_libro_a_biblioteca(mi_biblioteca)
    elif option == "2":
        libros_disponibles = mi_biblioteca.listar_libros_disponibles()
        if libros_disponibles:
            print("\nLibros disponibles:")
            for libro in libros_disponibles:
                print(f"- {libro.titulo} ({libro.autor})")
        else:
            print("No hay libros disponibles en la biblioteca.")
    elif option == "3":
        buscar_libro = input("Ingrese el libro a buscar: ")
        libro_encontrado = mi_biblioteca.buscar_libro(buscar_libro)
        if libro_encontrado:
            print(f"Libro encontrado: '{libro_encontrado.titulo}' ({libro_encontrado.autor}) - {'Disponible' if libro_encontrado.disponible else 'No disponible'}")
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
        libro_a_devolver = input("Ingrese el título del libro que desea devolver: ")
        libro_encontradoD = mi_biblioteca.buscar_libro(libro_a_devolver)
        if libro_encontradoD and not libro_encontradoD.disponible:
            libro_encontradoD.devolver_libro()
            print(f"Se ha devuelto el libro '{libro_encontradoD.titulo}'.")
        elif libro_encontradoD and libro_encontradoD.disponible:
            print(f"El libro '{libro_encontradoD.titulo}' no se ha alquilado.")
        else:
            print(f"No se encontró el libro '{libro_a_devolver}'.")
    elif option == "6":
        break
class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def agregar(self):
        print(f"El estudiante {self.name} {self.lastname}, EDAD: {self.age} se matriculó")

    def denegar(self):
        print(f"El joven {self.name} {self.lastname}, EDAD: {self.age} no se acepta")


def validar():
    name = input("Nombre: ")
    Lname = input("Apellido: ")
    age = int(input("EDAD: "))

    student = Student(name, Lname, age)
    student.agregar()


def denegar():
    name = input("Nombre: ")
    Lname = input("Apellido: ")
    age = int(input("EDAD: "))

    student = Student(name, Lname, age)
    student.denegar()


val = input("¿Acepta o no? (si/no): ")

if val.lower() == "si":
    validar()
else:
    denegar()
    

