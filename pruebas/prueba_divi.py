def divisibles(lis_nueva,numero):
    lista= []
    for elemento in lis_nueva:
        if elemento % numero == 0: 
            lista.append(elemento)
    return lis_nueva,lista,numero

lis_nueva,lista,numero = divisibles([12,5,10,8,5,2,9,21],3)
print(f'lista inicial: {lis_nueva } numeros divisibles {lista} y numero {numero}')
