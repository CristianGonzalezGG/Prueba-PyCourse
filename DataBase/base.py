import mysql.connector

# Configura los detalles de la conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # la contraseña correcta
    database=""
)
cursor = database.cursor()
cursor.execute("USE bd_udemy")
#cursor.execute("INSERT INTO vehiculos VALUES (null , 'KIA' , 'Cerrato', 18000) ")
database.commit()
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
print("----------TODOS MIS COCHES-------")
for car in result:
    print(car[2], car[3])
cursor.execute("DELETE FROM vehiculos WHERE modelo = 'supra'")
database.commit()