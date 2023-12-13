#crear listas para interar
frutas = ["Banano", "fresa", "sandia", "Manzana","pera","naranja"]
numeros = [1,2,3,4,5]

#nos saltamos la iteracion de un elemento con CONTINUE
for fruta in frutas:
    if fruta == 'sandia':
     continue
    print(fruta)
    
#para romper el bucle en un elemento preciso osea cuando lo itera que se termine ahi el bucle / no ejecuta el else

for frute in frutas:
    print(frute)
    #if frute == 'fresa':
        #break
        
#Recorriendo una cadena
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
    
print(numeros_duplicados)

#LO ANTERIOR PERO EN UNA SOLA LINEA DE CODIGO
numeros_duplicado = [x*2 for x in numeros]
print(numeros_duplicado) 