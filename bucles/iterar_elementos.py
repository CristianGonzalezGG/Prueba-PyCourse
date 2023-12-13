#bucles FOR para iterar listas / tuplas funcionan exactamente igual ambas y conjuntos igual
animales = ["perro","gato","loro"]

for animal in animales:
    print(animal)
    
#iterando y recorriendo numeros
numeros = [12,34,43]

for numero in numeros:
    resultado = numero * 2
    print(resultado)
    
#iterando 2 listas en un solo FOR+
for numero,animal in zip(animales,numeros):
    print(f'Recorrido lista 1: {numero}')
    print(f'Recorrido lista 2: {animal}')

#iterando numero con RANGE
for num in range(5,10):
    print(num)
    
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)

#usando el ELSE en FOR (estos siempre se van a ejecutar) (forelse)
for num in numeros:
    print(num)
else:
    print("El bucle termino")

