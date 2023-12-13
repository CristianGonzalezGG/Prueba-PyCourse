class Estudiante:
    def __init__(self, nombre, edad, grado) :
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("Estudiando...")
        
nombre = input("Digame su nombre: ")
edad = int(input("Ahora su edad: "))
grado = int(input("Y su grado: "))

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      Datos de el estudiante:\n\n
      Nombre: {estudiante.nombre}\n
      Nombre: {estudiante.edad}\n
      Nombre: {estudiante.grado}\n
      """)
while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()