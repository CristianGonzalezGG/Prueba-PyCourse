class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showData(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")

class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade = grade
        
    def showGrade(self):
        print(f"Grado: {self.grade}")

Students = Student("Juan","24","10mo")
Students.showData()
Students.showGrade()