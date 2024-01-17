import usuarios.conection as concected
connectBase = concected.conectar()
dataBase = connectBase[0]
cursor = connectBase[1]
class Nota:
    def __init__(self, user_id, Title, Description):
        self.user_id = user_id
        self.Title = Title
        self.Description = Description
    def save(self):
        sql = "INSERT INTO notes VALUES (null, %s,%s,%s, NOW())"
        note = (self.user_id, self.Title, self.Description)
        cursor.execute(sql, note)
        dataBase.commit()
        return [cursor.rowcount, self]
    def listar(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    def delete(self):
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND title LIKE '%{self.Title}%'"
        cursor.execute(sql)
        dataBase.commit()
        return [cursor.rowcount, self]
    
    