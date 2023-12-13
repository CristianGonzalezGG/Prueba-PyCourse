
#modo para abrir archivos .txt con open
archivos = open("archivos\\texto_de_cristian.txt")
#print(archivos.read())

#para volver a leer el archivo toca cerrarlo ya que no lo puede leer si ya se abrio y no se ah cerrado

#asi lee el archivo y lo convierte en una lista, cada linea es un elemento de la lista
linea_1 = archivos.readlines()

#cerrrar el archivo
archivos.close()
print(linea_1)

print(linea_1[0]) 