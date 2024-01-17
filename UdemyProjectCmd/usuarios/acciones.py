import usuarios.usuario as userm
import notas.acciones as s
class Acciones:
    
    def registro(self):
        print("OK!! Vamos a Registrarte en el sistema....")
        
        name = input("Cual es tu nombre.. ")
        lastName = input("Cual es tu apellido.. ")
        mail = input("Introduce tu correo: ")
        password = input("Introduce tu contraseña: ")
        
        usuario = userm.Usuario(name, lastName, mail, password)
        registrer = usuario.registrar()
        if registrer[0] >= 1:
            print(f'Perfecto {registrer[1].name} te haz registrado con el email: {registrer[1].mail}')
        else:
                print("No te haz registrado correctamente")
                
    def login(self):
        print("OK! vamos a indentificarte en el sistema.... ")
        try:
            mail = input("Introduce tu correo: ")
            password = input("Introduce tu contraseña: ")
            usuario = userm.Usuario('','',mail,password)
            login = usuario.identificar()
            if mail == login[3]:
                print(f"Bienvenido{login[1]} te haz registrado el: {login[5]}")
                self.proximasAcciones(login)
        except:
            print("revise crendenciales")           
    def proximasAcciones(self, usuario):
        print("""
        Bien!! Ahora puedes administrar tus notas...
        
        1 - Crear Nota
        2 - Mostrar tus notas
        3 - Elimiar una nota 
        4 - Salir
        """)
        
        accionNotas = input("¿Que quieres hacer?: ")
        doIT = s.Acciones()
        
        if accionNotas == "1":
            doIT.crear(usuario)
            print("Vamos a crear una nueva Nota!!")
            self.proximasAcciones(usuario)
        elif accionNotas == "2":
            doIT.mostrar(usuario)
            print("Estas son tus notas Creadas Anteriormente!")
            self.proximasAcciones(usuario)
        elif accionNotas == "3":
            doIT.deletes(usuario)
            print("Cual nota deseas eliminar?...")
            self.proximasAcciones(usuario)
        elif accionNotas == "4":
            exit()
                    