#GETTERS Y SETTERS PARA ACCEDER A CLASES PRIVADAS ATRIBUTOS Y DEMAS
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def get_name(self):
        return self._name
        
cristian = Person("cristian","17")
nombre = cristian.get_name()
print(nombre)