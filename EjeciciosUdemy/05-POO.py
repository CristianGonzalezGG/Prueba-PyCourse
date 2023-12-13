class Celular:
    def __init__(self,modelo,almacenamiento):
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.defectuoso = False
    def reportarDefecto(self):
        self.defectuoso = True
    def ArreglarDefecto(self):
        self.defectuoso = True
class Tienda:
    def __init__(self):
        self.stock = []
        self.defec = []
    
    def add(self,stocki):
        self.stock.append(stocki)
        print(f'libro {stocki.modelo} agregado....')
        
    def buscarDefec(self,defectuoso):
        print("melo")
        
    
# def agregarCelular(self):
#     modelo = input("Ingrese el modelo de el Dispositivo: ")
#     almacenamiento = input("Ingrese el Espacio de el Dispositivo: ")
#         #nuevo_phone = stock()