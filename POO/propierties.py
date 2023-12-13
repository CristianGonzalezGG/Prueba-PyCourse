#permite definir getter and setter y dilayters 
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,nameNew):
        self._name = nameNew
                         
        
        
        
cristian = Person("cristian","17")
cristian.name="Gorgojo"
nombre = cristian.name
name = cristian.name
print(name)