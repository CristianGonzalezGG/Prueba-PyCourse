"""
Ejercicios 1: 
Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- recorrera y printearla
- hacer funcion que reccora lista de string y muestre un string
- ordenarla y mostrarla
- buscar algun elemento que se pida a el usuario
"""
def recorreFunction(lista):
    numerosString = ""
    for x in lista:
        numerosString += str(x)
    return numerosString

listaEdades = [13,12,16,17,11,10]
for x in listaEdades:
    print(x)
    
listaDesmpaquetada = recorreFunction(listaEdades)
print(listaDesmpaquetada)
print(f'Cambia string la lista: {type(listaDesmpaquetada)}')
listaEdades.sort()
print(f'Lista Ordenada: {listaEdades}')
print(f'Longitud de la lista: {len(listaEdades)}')
IndexOrNumber = input("Desea Buscarlo por indice o numero? ")
if IndexOrNumber.lower() == "indice":  
    SearchIndex = int(input("Indique el indice "))
    print(f"El numero en el indice {SearchIndex} es: {listaEdades[SearchIndex]}")
elif IndexOrNumber.lower() == "numero":
    SearchNumber = int(input("Ingrese el numero a buscar en la lista: "))
    if SearchNumber in listaEdades: print(f"El numero {SearchNumber} Si esta en la lista.. ")
    else: print("El numero ingresado no existe en la lista")       
else: print("Valor no valido...")
    