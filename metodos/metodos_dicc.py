diccionario = {
    "nombre": 'cristian',
    "Apellido": 'Gonzalez',
    "Edad": 17
}
#KEYS Devuelve las claves (Tambien sirve para iterar)
claves = diccionario.keys()

#GET devuelve el valor que este dentro de la clave 
get = diccionario.get("Edad")

#CLEAR elimina todo del diccionario
#POP elimina un elemento de el diccionario


print(claves)
print(get)