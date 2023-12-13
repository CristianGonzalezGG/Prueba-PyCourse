#acceder desde una clase hija a una clase padre
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
        def saludar(self):
            return f'hpta'
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
#herencia multiple 
class EmpleadoArtista(Empleado,Artista):
    def __init__(self,nombre, edad, nacionalidad,trabajo,salario,habilidad,invensible):
        Empleado.__init__(self,nombre, edad, nacionalidad,trabajo,salario)
        Artista.__init__(self,habilidad)
        self.invensible = invensible
        
    def mostrar_habilidad(self):
            print("No tengo")
            
    def szs (self):
            return f'{super().mostrar_habilidad()}'   
             
artista1 = EmpleadoArtista("Cris",10,"veneco","bombero",1200000,"fuego","al agua")        
roberto = Empleado("Cris",10,"veneco","bombero",1200000)
print(f'''Nombre: {artista1.nombre}
      Edad: {artista1.edad}
      Habilidad: {artista1.habilidad} y {artista1.szs}''')