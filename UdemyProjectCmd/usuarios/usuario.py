import datetime
import hashlib
import usuarios.conection as connection

connect = connection.conectar()
dataBase = connect[0]
cursor = connect[1]
class Usuario:
    def __init__(self, name, lastName, mail, password):
        self.name = name
        self.lastName = lastName
        self.mail = mail
        self.password = password    
    def registrar(self):
        dateT = datetime.datetime.now()
        #CIFRAR LA PASSWORD
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))
        sql = "INSERT INTO users VALUES (null, %s,%s,%s,%s,%s)"
        user = (self.name, self.lastName, self.mail, encryption.hexdigest(), dateT)
        try:
            cursor.execute(sql, user)
            dataBase.commit()
            
            resulta = [cursor.rowcount, self]
        except:
            resulta = [0, self]
            
        return resulta
            
        
        
    def identificar(self):
        #Consulta para comprobar si existe y si coincide
        sql = "SELECT * FROM users WHERE mail = %s AND password = %s"
        #cifrado
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))
        ususario = (self.mail, encryption.hexdigest())
        cursor.execute(sql, ususario)
        result = cursor.fetchone()
        return result
        


