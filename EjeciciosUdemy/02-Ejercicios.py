lista = []
x = 0

while x < 120:
    lista.append(f'Elemento-{x}')
    print(f"Mostrando el: {lista[x]}")
    x += 1
    
listasEdades = []
for x in range(0,100):
    if x <= 1:
        listasEdades.append(f"Visiste {x} año")
        print(f"{listasEdades[x]}")
    else: 
        listasEdades.append(f"Visiste {x} años")
        print(f"{listasEdades[x]}")