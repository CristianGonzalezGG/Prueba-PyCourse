import re

texto = """Hola mani 7., esta es la primera linea 1 de texto, como andas
esta es la segunda 2. linea de texto 4 
y esta es la final 5 y la definitiva"""

#HACIENDO busqueda simple que encuentre "Hola" en texto
resultado = re.search("Hola",texto)

#busqueda simple que encuentre todas las palabras "esta", sin importar mayusculas o minusculas
resultado2 = re.findall("Esta",texto,flags=re.IGNORECASE)

#\d --> busca digitos numericos de 0-9
resultado3 = re.findall(r"\d",texto)

#\D muestra todo menos digitos numericos del 0-9
resultado4 = re.findall(r"\D",texto)

#\w muestra caracteres alfanumericos [A-Z][a-z][0-9][ _ ]
resultado5 = re.findall(r"\w",texto)

#\W muestra TODO menos caracteres alfanumericos [A-Z][a-z][0-9][ _ ]
resultado6 = re.findall(r"\W",texto)

#\s busca espacios en blanco -> tabs, saltos de linea, 
resultado7 = re.findall(r"\s",texto)

#\S busca TODO MENOS  saltos de linea 
resultado8 = re.findall(r".",texto)

#\n busca todos los saltos en linea
resultado9 = re.findall(r"\n",texto)

#\ -> cancela todos los caractetres especiales
resultado10 = re.findall(r"\.",texto)

#armando una cadena que busque un numerom, seguido de un punto y un espacio
resultado11 = re.findall(f'\d\.\s',texto)

#^ -> busca el comienzo de una linea (buscando hola al principio de la linea)
#flags=re.M activa la multilinea
#resultado = re.findall(r'^Esta',texto,flags=re.M)


#$ -> busca el final de una linea 
#resultado = re.findall(r'capitan$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda (3 numeros juntos esta vez)
#resultado = re.findall(r'\d{3}',texto)

#{n,m} -> al menos n, como máximo m
#resultado = re.findall(r'\d{2,4}',texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)

print(resultado)

print(resultado11)