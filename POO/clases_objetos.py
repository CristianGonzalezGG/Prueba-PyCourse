class Celular:
    #se ejecuta automaticamente cuando se crea un objeto de la clase
    def __init__(self, marca, modelo, camara): #Se crea el constructor de la clase
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
         
    def llamar(self):
        print(f"Estas llamando desde tu: {self.modelo}")

#Instanciando objetos
Celular1 = Celular("Samsunge", "A51", "48MP") #se asignan los valores de las variables 
Celular2 = Celular("Apple", "Iphone 15 Pro Max", "20MP")
Celular3 = Celular("Apple", "Iphone 15 Pro Max", "20MP")
print(Celular3.camara)
Celular1.llamar()
                           