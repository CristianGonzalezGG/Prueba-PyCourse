
#sobre agrega el texto pero no borra lo que este solo añade lo que se le indique
with open('archivos\\texto_de_cris.txt','a') as archivo:
    archivo.write("que hace manito")
    
#usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f"linea {i+1} agregada\n")
        