#ejercicio fizz, buzz, fizzbuzz
for numero in range(1, 11):
    if numero % 2 == 0 and numero % 4 == 0:
        print("fizzbuzz")
    elif numero % 2 == 0:
        print("fizz")
    elif numero % 6 == 0:
        print("buzz")
    else:
        print(numero)
#ejemplo de switch case para manejar opciones

def opcion_1():
    print(f"Su helado cuesta: {precio}")

def opcion_2():
    print(f"Su helado cuesta: {precioSin}")

opciones = {
    1: opcion_1,
    2: opcion_2
}

tipoDeHelado1 = "con Pasas $10"
tipoDeHelado2 = "sin Pasas $6"
tipoDeHelado3 = "con Pasas y Almendras"
precio = 10
precioSin = 6

print("Opciones de helado:")
print("1. " + tipoDeHelado1)
print("2. " + tipoDeHelado2)

helado = input("¿Qué tipo de helado quiere? (Ingrese el número correspondiente): ")

# Convierte la entrada del usuario a un entero
helado = int(helado)

if helado in opciones:
    opciones[helado]()
else:
    print("Opción inválida")
#ejemplo de como ingresar un dato por consola y lo valide si esta dentro de una variable

coach = input("Nombre \n")
if "Mario" in coach:
    print("Szs si esta")
else: 
    print("Que busca jajaj")
#creando listas 
lista = ["Nico Arias", "cantante", "Cali", "GTA cali"]

print(lista[0])

#creando tuplas no se pueden modificar los valores a diferencia de la lista 

tupla= ("Nico Arias", "cantante", "Cali", "GTA cali")

print(tupla[0])

dicionario = {
    "soa": "nombre"
} 

print(dicionario["soa"])

