class Notify:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notifyUser(self):
        return NotImplementedError
    
class NotifyEmail(Notify):
    def notifyUser(self):
        print(f"Enviando EMAIL a {self.usuario.email}")
        
class NotifySMS(Notify):
    def notifyUser(self):
        print(f"Enviando SMS a {self.usuario.sms}")