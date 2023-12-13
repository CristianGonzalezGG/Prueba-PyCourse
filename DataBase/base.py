import mysql.connector

# Configura los detalles de la conexión
config = {
    'host': 'localhost',
    'user': 'BDcoca',  # Reemplaza 'tu_usuario' con el nombre de usuario correcto
    'password': 'camilo11',  # Reemplaza 'tu_contraseña' con la contraseña correcta
    'database': 'bd_cotizacion',
    'raise_on_warnings': True,
}


# Crea la conexión a la base de datos
try:
    lista=[]
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Conexión exitosa a la base de datos")

        # Crea un objeto cursor para ejecutar consultas SQL
        cursor = connection.cursor()

        # Ejecuta una consulta para obtener todos los usuarios de la tabla "usuarios"
        query = "SELECT * FROM preensamblado"
        cursor.execute(query)

        # Recupera todos los resultados
        usuarios = cursor.fetchall()

        # Muestra los usuarios
        for usuario in usuarios:
            lista.append(usuario)
            print(lista)
        
except mysql.connector.Error as err:
    print("Error: {}".format(err))

finally:
    # Cierra el cursor y la conexión al finalizar
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
print(lista[0])

