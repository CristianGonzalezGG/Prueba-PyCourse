#encontrando el numero mayor de una lista

numeros = [2,6,23,61,13,10]
numero_mas_alto = max(numeros)
#print(numero_mas_alto)

#numero mas pequeño
numero_mas_bajo = min(numeros)
#print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.45334,2)
print(numero)

#bool se usa como boolea no  da false cuando le damos (0, false, none, vacio) 
resultado_bool = bool(0)
print(resultado_bool)

#ALL retorne true si todos los parametros son verdaderos si algunos de los datos es falso ya se rompe la condicion ya arroja False
resultado_all = all(["hola", True, 12])
print(resultado_all)

#SUM suma todos los valores de un iterable 
suma_total = sum(numeros)
print(suma_total)