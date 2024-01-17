from usuarios import acciones
"""
Proyecto Python en consola de gestor de notas
que tiene un Login y un registro de notas.. 
Crear nota, Mostrar notas, Eliminar notas
"""
print("""
Bienvenido a el Sistema de gestor de notas 
Para poder Ingresar Debes Ingresar o Registrate...
¿Que deseas hacer?: 
    - Ingresar
    - Registro
""")
doIT = acciones.Acciones()

action = input("¿Que Quieres hacer?:  ")

if action.lower() == "registro":
    doIT.registro()
    
elif action.lower() == "login":
    doIT.login()    