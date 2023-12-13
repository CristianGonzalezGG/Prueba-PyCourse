class TanqueC:
    def __init__(self):
        self.combustible = 100
    
    def agregarC(self,cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usarC(self,cantidad):
        self.combustible -= cantidad
        
class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible() > distancia / 2:
            self.posicion += distancia
            self.tanque.usarC(distancia /2)
            print("El auto se ha movido exitosamente")
        else:
            print("No hay suficiente combustible")
            
    def obtenerP(self):
        return self.posicion
        
    


tanque = TanqueC()
auti = Auto(tanque)

print(auti.obtenerP())
auti.mover(10)
print(auti.obtenerP())
auti.mover(30)
print(auti.obtenerP())
auti.mover(50)
print(auti.obtenerP())
auti.mover(60)
print(auti.obtenerP())
auti.mover(70)
print(auti.obtenerP())
auti.mover(80)