#Creando funcionm que suma numeros
def suma():
    while True:
        #pidiendo los numeros
        a = input("Ingrese el numero 1: ")
        b = input("Ingrese el numero 2: ")
        #intentando convertilos a eneteros y sumarlos
        try:
            result = int(a) + int(b)
        
        #si lanza una excepcion, pedirle que reingrese los datos
        except: 
            print("Porfavor, ingrese un numero tontin")
        #si todo sale bien terminanos el bucle
        else:
            break
        #siempre se ejecuta, dependiendo si ejecuta la excepcion o no 
        finally:
            print("Melos")
            
    return result
#mostrando
print(suma())