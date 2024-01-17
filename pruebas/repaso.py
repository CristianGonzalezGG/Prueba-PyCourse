class Student:
    def __init__(self, name, lastname, age):
        self.name = name 
        self.lastname = lastname
        self.age = age
    
    def agregar(self):
        print(f"El estudiante{self.name} {self.lastname}, EDAD: {self.age} Se matriculo")
    def denegar(self):
        print(f"El joven {self.name} {self.lastname}, EDAD: {self.age} No se acepta")


def validar():
    name = input("Nombre: ")
    Lname = input("Apellido: ")
    age = int(input("EDAD.."))
    melo = Student(name, Lname, age)
    melo.agregar()
def den():
    names = ("Nombre: ")
    Lname = input("Apellido: ")
    age = int(input("EDAD.."))
    melo = Student(names, Lname, age)
    melo.denegar()


val = input("Acepta o no?.. ")

if val == "si": 
    validar()
else: 
    den()
    
    
    
    