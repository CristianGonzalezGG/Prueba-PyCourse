#parametros posicionales
def frase (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, sos muy makio {adjetivo}"
frase_result = frase("sapo","martines","gay")
print(frase_result)

#se puede cambiar el orden de los parametros declarandolos (keyword arguments)
def frases (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, sos muy makio {adjetivo}"
frase_results = frases(adjetivo="sapo",apellido="martines",nombre="gay")
print(frase_results)

#hay forma de forzar el valor de el parametros definiendolo en la funcion pero se puede modificar
def sumal (nombre ="sapo"):
    return f"hola: {nombre}"
hola = sumal()#entonces ya no hay necesidad de decirle que ira en ese parametro
print(hola)