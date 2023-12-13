#Encapsulamiento
class MyClass:
    def __init__(self):
        self.__private = "valor"
objecte = MyClass()
print(objecte.__private)