#crando una funcion que muestre la seria fionacci entre 0 y un numero

def fionacci(num):
    a,b = 0,1
    fionacci_lista = [0]
    for i in range(num):
        if b > num: return fionacci_lista
        else:
            fionacci_lista.append(b)
            a,b = b, a+b

resultado = fionacci(34)
print(resultado)