#declaracion varibles y entrada de datos
from typing import Any


variable = "This text is Defaul.."
print(variable)
var = input("That a Desfault exist: ")
if var == "si": print(variable)
else: print("No isn't Default..")
#Bucles y condicionales Basicos
while True:
    print("Exit with 4")
    var = input("That a Desfault exist: ")
    if var.lower() == "yes": print(variable)
    elif var.lower() == "no": print("No isn't Default..")
    elif var == "4":
        break
    
#Create a class called "Student" that needs to has atrributes like name, age, grade. 
#Create method called study with this text "The studen {student's name} is studying" 
class StudentEx:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def study(self):
        print(f"The student {self.name} is studying...")

registrerName = input("What the student's name..")
registrerAge = input("What's the student's age..")
registrerGrade = input("What course is coursing?..")

estudiante1 = StudentEx(registrerName,registrerAge,registrerGrade)
yesOrNot = input("Do u Like Study?..")
if yesOrNot.lower() == "yes":
    estudiante1.study()
else: 
    print("Ok come on to search phentanilo")    

#-----------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printed(self):
        print(F"Name: {self.name} and Age: {self.age} ")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade = grade
    def printedS(self):
        print(F"Name: {self.name} and Age: {self.age} and Grade {self.grade} ")

estudiante = Student("Named", "11", "10")
estudiante.printed()
estudiante.printedS()
