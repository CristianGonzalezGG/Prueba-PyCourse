#Escribe un programa en Python que calcule la suma de los números pares y la suma de los números impares en un rango de 
#números desde 1 hasta un número entero que el usuario ingresará. El programa debe hacer lo siguiente:

#Solicitar al usuario que ingrese un número entero positivo.
#Calcular la suma de todos los números pares en el rango desde 1 hasta el número ingresado.
#Calcular la suma de todos los números impares en el mismo rango.
#Mostrar las sumas separadamente, es decir, la suma de los números pares y la suma de los números impares.

#----------------

    
def suma_pares_impares(rango):
    pares = []
    impares = []

    for num in range(1, rango + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return pares, impares

numero = int(input("Ingrese un número entero positivo: "))
pares, impares = suma_pares_impares(numero)

print(f'Números pares en el rango: {pares}')
print(f'Números impares en el rango: {impares}')
suma = sum(pares)
suma_impa = sum(impares)
print(f"La suma de los numeros pares es: {suma}")
print(f"La suma de los numeros impares es: {suma_impa}")