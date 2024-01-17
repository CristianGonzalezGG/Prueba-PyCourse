import sqlite3

conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"ID INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo VARCHAR(255), "+
"Descripcion text, "+
"Precio int(255)"+
               ")")
#Guardar cambios
conexion.commit()

#Insertar Datos
#cursor.execute("INSERT INTO productos VALUES (null, 'Primer Producto', 'Descripcion de mi producto', 250)")

#Guardar
#conexion.commit()

#Borrar datos

#cursor.execute("DELETE FROM productos")
conexion.commit()
#Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(producto)
    
#Cerrar la conexion
conexion.close()