from abc import ABC, abstractclassmethod #es un decorador que indica que es un metodo abstracto

class Person():
    @abstractclassmethod
    def __init__(self,name,age,gender,worki):
        self.name = name
        self.age = age
        self.gender = gender
        self.worki = worki
    
    @abstractclassmethod
    def work(self):
        pass
    
    def presentation(self):
        print(f"Hi, my name is: {self.name} and i'm {self.age}")

class Student(Person):
    def __init__ (self,name,age,gender,worki):
        super().__init__(name,age,gender,worki)
    def DoActivity(self):
        print(f"Estoy estudiando {self.worki}")

class Worker(Person):
    def __init__ (self,name,age,gender,worki):
        super().__init__(name,age,gender,worki)
    def DoActivity(self):
        print(f"Estoy trabajando en: {self.worki}")

dalto = Student("lucas","21","masculino","Soccer")
cristian = Worker("Cristian","17","Masculino","Programador Back-end")
cristian.presentation()
cristian.DoActivity()
dalto.presentation()
dalto.DoActivity()
        