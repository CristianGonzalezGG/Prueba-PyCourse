class Estudiantes:
    def __init__(self,nombre, edad, estadoCivil):
        self.nombre = nombre
        self.edad = edad
        self.estestadoCivil = estadoCivil
    def dejarEstudiar():
        print("Fin de estudiar me retiro")
        
nombre = input("Ingrese su nombre")
try:
    edad = int(input("EDAD? "))
except:
    print("Es un numero tontin")
estadoCivil = input("Solter@ o casad@: ")
estudianteList = Estudiantes(nombre,edad,estadoCivil)
print(f"Nombre: {estudianteList.nombre}")        