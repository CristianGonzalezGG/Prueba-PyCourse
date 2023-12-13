#CREANDO UNA FUNCION SIMPLE

def saludar():
    print("hola Cristian")

#EJECUTANDO LA FUNCION SIMPLE
saludar()

#creando uina funcion con parametros
def saludo (nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else: 
        adjetivo = 'rarito'
    
    print(f'Hola {nombre} como estas, {adjetivo}?')

saludo("cristian gonzalez","HomBre")

#crear una funcion que retorne multiples valores

def crear_contraseña_random (num):
    chars ="abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
#desempaquetar para devolver mas valores
password, primer_numero = crear_contraseña_random(3432)
print(f"nueva contraseña {password}")
print(f"numero usado: {primer_numero}")


     