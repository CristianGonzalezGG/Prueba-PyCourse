#decoradores para agregar codigo a una funcion sin cambiar su codigo
def decor(functions):
    def function_modify():
        print("Antes de llamar a la funcion ")
        functions()
    return function_modify

@decor
def saludo():
    print("Hola")
    
saludo()
