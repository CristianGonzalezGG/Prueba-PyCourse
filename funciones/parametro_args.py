#forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
    
result = suma([3,7,9,1])
print(result)

#forma optima con parametro args
def sumas(nombre,*numeros):
    return f"{nombre}, la suma es: {sum(numeros)}"

resultado = sumas("carlos",2,3,4,5,6,8)
print(resultado) 