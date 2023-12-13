#LSP 
class Bird:
    def fly(self):
        return 'Estoy volando'
    
class Pin(Bird):
    def fly(self):
        return 'no puedo volar'

def DoFly(bird = Bird):
    return bird.fly()

print(DoFly(Pin()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'Estoy volando'

class AveNoVoladora(Ave):
    pass