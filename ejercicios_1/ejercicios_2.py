#A) Pedirle a el usuario que diga un texto real y que calcule cuanto tardaria eb decir esa frase y cuantas palabras dijo 
#B) si tarda mas de un minuto decir "te demoraste mucho, tontin"
#C) Dalto habla un 30% mas rapido ¿cuanto tardaria el en decirlo?

#PEDIR EL TEXTO
texto = input("Dime un texto donde calculare el tiempo y las palabras: ")

#separar el texto en palbras para calcular tiempo y las palabras totales 
palabras = texto.split()
cantidad_palabras = len(palabras)
tiempo_aproximado = cantidad_palabras/2

#Imprimir Cant y Tiempo 
print("-----------------------------")
print(f'Tiempo que se tarde en decir el texto es de: {tiempo_aproximado} Segundos Aproximadamente')
print(f'Y la cantidad de palabras fueron: {cantidad_palabras}') 

#B) si tarda mas de un minuto decir "te demoraste mucho, tontin"
print("-----------------------------")
if tiempo_aproximado > 60:
    print("te demoraste mucho, tontin")
else:
    print("Melos de tiempo")
    
#C) Dalto habla un 30% mas rapido ¿cuanto tardaria el en decirlo?
porcentaje_dalto = (tiempo_aproximado*30)/100


print("-----------------------------")
print(f'Dalto diria ese mismo texto en: {tiempo_aproximado-porcentaje_dalto} Segundos aproximadamente con una diferencia de {porcentaje_dalto} segundos ')