class Character:
    def __init__(self,name,force,speed):
        self.name = name
        self.force = force
        self.speed = speed
    
    def __repr__(self):
        return f'{self.name}(fuerza: {self.force}, velocidad: {self.speed})'
    
    def __add__(self,OtherPj):
        newName = self.name + "-" +OtherPj.name
        newForce= ((self.force+OtherPj.force)/2)**2
        newspeed= ((self.speed+OtherPj.speed)/2)**2
        return Character(newName,newForce,newspeed)

goku = Character("Goku",100,100)
vegeta = Character("Vegeta",50,50)
volketa = goku + vegeta
print(vegeta)
print(goku)
print(volketa)
