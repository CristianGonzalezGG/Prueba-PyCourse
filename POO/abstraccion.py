class Car():
    def __init__(self):
        self._estado = "apagado"
    def TurnOn(self):
        self._estado = "Encendido"
        print("El auto esta encendido")
    def Drive(self):
        if self._estado == "apagado":
            self.TurnOn()
        print("Conduciendo el Auto")
        
MyCar = Car()
MyCar.Drive()