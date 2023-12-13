#crear diccionario 

#otra forma de crearlas es definiendo las claves es como si definieramos variables
diccionario = dict(nombre = "lucas", apellido = "gonzalez")

print(diccionario)

#creando diccionarios con fromkeys donde todas las claves estan vacias quedan none, y el primer dato es un iterable donde toma este como clave

diccionario = dict.fromkeys(["nombre", "apellido"])

print(diccionario)

#son iterables los conjuntos 