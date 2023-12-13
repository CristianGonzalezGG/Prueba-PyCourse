class Animal:
    def eat (self):
        print("El animal esta comiendo")

class Bird(Animal):
    def fly(self):
        print("El animal esta volando")
        
class Mammal(Animal):
    def breast_feed(self):
        print("El animal esta amamantando")
class Murci(Mammal,Bird):
    pass

ave = Murci()
ave.eat()
ave.fly()