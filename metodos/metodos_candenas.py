#DIR SE USA PARA VER LOS ATRIBUTOS DE EL TIPO DE DATO DE EL OBJETO

#UPPER Y LOWER SE USAN PARA VOLVER EL TEXTO TODO EN MAYUSCULAS O MINUSCULAS (upper Mayus) (lower Min)
cadena1 = "Hola! broder que contas"
cadena2 = "WELCOME TO COLOMBIA"

resultado =cadena1.upper()
print(cadena2.lower())
print(resultado)

#CAPITALIZE Se usa para poner la primera letrea de el texto en Mayuscula 

cadena3 = "hola"
print(cadena3.capitalize())

#FIND busca una cadena en otra cadena, si no hay condiciones devuelve -1

busqueda_find = cadena1.find("que")

print(busqueda_find)

#INDEX este funciona igual que find, su diferencia es que si no encuentra una coincidencia usa la exception  

busqueda_index = cadena1.index("a")
print(busqueda_index)

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumèrico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("la ma")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena2)

#verificamos si una cadena empieza con otra cadena dada, si es asì devuelve True
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asì devuelve True
termina_con = cadena1.endswith("H")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("!"," b")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_nueva)