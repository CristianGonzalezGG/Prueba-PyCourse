class Person():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Person(nombre={self.nombre},edad={self.edad})'
    
dakt = Person ("Lucas",21)
print(dakt)

lista = (1,2,3)