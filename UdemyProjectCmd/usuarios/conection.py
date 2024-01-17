import mysql.connector
def conectar():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="udemycmd",
        port = 3306
    )
    cursor = dataBase.cursor(buffered = True)
    return[dataBase, cursor]