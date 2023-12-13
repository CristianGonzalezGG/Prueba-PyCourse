#EJERCICIOS PRACTICOS #2

#Creando funcion 
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("Ingrese el nombre de el compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(5)
print(f'El asistente es: {asistente}')
print(f'El Profesor es: {profesor}')