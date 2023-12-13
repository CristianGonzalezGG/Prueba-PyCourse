from abc import ABC, abstractmethod

class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
class Trabajador():  
    @abstractmethod
    def trabajar(self):
        pass
    
class Dormilon(): 
    @abstractmethod
    def dormir(self):
        pass
class Humano(Trabajador,Comedor,Dormilon):
    
    def comer(self):
        print("Esta comiendo el humano")
    
    def trabajar(self):
        print("Esta trabajando el humano")
    
    def dormir(self):
        print("Esta durmiendo el humano")

class Robo(Trabajador):
       
    def trabajar(self):
        print("Esta trabajando el robot")

robot = Robo()
hum = Humano()
hum.trabajar()
robot.trabajar()
        
    