import sys
#practica

#crear un programa donde se evalue un registro de contraseña y usuario si son correctos entra, si va a comprar los lunes tiene 30% de dec, y jueves 20% dec, si no
#es ninguno de esos dias paga normal luego entrara el precio de cada producto y dira que producto es el mas caro y cual es para la factura el nombre de el cliente paselo a mayus, 
#si el cliente quiere factura electronica debe registrar el nit y correo, donde se le enviara cuanto es el iva correspondiente de la factura (19%) y dira cuantos productos llevo en la compra

#crear registro 
user = "pabloG"
password = "CG1234"
user_caja= input("Ingrese el usuario: ")
pass_caja= input("Ingrese la contraseña: ")
if user_caja == user and pass_caja == password:
    print("Ingresando...")
else:
    print("Usuario y/o contraseña Incorrectos")
    sys.exit()

#descuentos
dia_lunes = 30
dia_jueves = 20

#facturacion productos
productos0 = int(input("Precio de el primer producto"))
productos1 = int(input("Precio de el segundo producto"))
productos2 = int(input("Precio de el tercer producto"))
productos3 = int(input("Precio de el cuarto producto"))
mayor = "s"
#condicional para saber cual producto sale mas caro
if productos0 > productos1 and productos0>productos2 and productos0 > productos3:
    print(f"El primer producto costo mas y fue:  {productos0}")
    mayor = "1"
elif  productos1 > productos0 and productos1>productos2 and productos1 > productos3:
    print(f"El segundo producto costo mas y fue:  {productos1}")
    mayor = "2"
elif productos2 > productos0 and productos2>productos1 and productos2 > productos3:
    print(f'El tercer producto costo mas y fue:  {productos2}')
    mayor = "3"
elif productos3 > productos0 and productos3>productos1 and productos3 > productos2:
    print(f'El cuarto producto costo mas y fue:  {productos3}')
    mayor = "4"
else: 
    print("")

#sacar dec si es algun dia 
dia = input("Que dec aplica lunes, o jueves? ")
total = productos0 + productos1+ productos2 + productos3
dec = total*30/100
dec2 = total*20/100
if dia == "lunes":
    print(f"El dec es de 30%, su compra queda con un descuento de: {dec} y quedaria en: {total - dec}")
elif dia == "jueves":
        print(f'El dec es de 20%, su compra queda con un descuento de: {dec2} y quedaria en: {total - dec2}')
else: 
    print(f"no tiene descuento y su compra le queda en: {total}")
    
#facturar
nombre_cliente = input("Cual es su nombre: ")
nombre_mayus = nombre_cliente.upper()
print(nombre_mayus)

facturacion_electronica = input("Desea factura electronica ? ")

if facturacion_electronica == "si":
    nit = input("NIT de empresa")
    correo = input("Correo electronico")
else:
    print("⬜")

#cuanto es el iva de la compra
iva = total*19/100
total_iva = total - iva

print(f"El iba de la compra es de {iva}")
print(f'Total sin iva {total_iva}')    

#FACTURA 
print(f"nombre: {nombre_mayus}")
print(f"productos 4, producto mas caro: {mayor}")
print(f"total: {total}")
#print(f"correo: {correo}")