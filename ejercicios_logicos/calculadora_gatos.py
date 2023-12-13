# Ejercicio: CALCULADORA DE GATOS
# Crea un programa que permita a un usuario llevar un registro de sus gastos diarios. El programa debe tener las siguientes características:

# Utiliza un diccionario para almacenar los gastos, donde las claves son las categorías de gastos (por ejemplo, "comida", "transporte", "entretenimiento") y los valores son
# listas de gastos en esa categoría.

# El programa debe mostrar un menú con las siguientes opciones:

# - Agregar un gasto
# - Ver gastos por categoría
# - Ver el gasto total
# - Salir
# Al agregar un gasto, el usuario debe ingresar la categoría y el monto del gasto. El programa debe agregar este gasto a la categoría correspondiente en el diccionario.

# Al ver los gastos por categoría, el usuario debe seleccionar una categoría y el programa mostrará todos los gastos en esa categoría.

# Al ver el gasto total, el programa debe calcular y mostrar el gasto total de todas las categorías.

# El programa debe funcionar hasta que el usuario elija la opción "Salir".

# Este ejercicio combina el uso de variables, diccionarios, bucles (por ejemplo, un bucle while para mostrar el menú y otro bucle para agregar gastos), condicionales, entrada de datos
# (para que el usuario seleccione opciones y agregue gastos), y operaciones aritméticas para calcular el gasto total. También se pueden utilizar funciones para organizar mejor el código.

#crando el diccionario que llevara los gastos

def iniciar_registro_gastos():
    gastos = {
        'comida': [],
        "entrenimiento": [],
        "transporte": []
    }
    while True:
        opciones = input("Menu de opciones: \n1. Agregue un gasto\n2. Ver gastos por categoria\n3. Ver el gasto Total\n4.Salir")
        if opciones == "1": agregar_gastos(gastos)
        elif opciones == "2": ver_gastos_por_cat(gastos)
        elif opciones == "3": gastos_totales(gastos)
        elif opciones == "4": break
        else: print("Opcion invalida intente nuevamente")
        
def agregar_gastos(gastos):
    categoria = input("Ingrese la categoria del Gasto: ")
    monto = int(input(f"Ingrese el monto gastado en: {categoria}"))
    
    if categoria in gastos:
        gastos[categoria].append(monto)
    else: 
        print("Catergoria invalida: ")

def ver_gastos_por_cat(gastos):
    categoria = input("Que categoria quiere ver? ")
    if categoria in gastos:
        print(f"Gastos en la categoria: {categoria}: Son {gastos[categoria]}")
    else: 
        print("Categoria paila")

def gastos_totales(gastos):
    total = sum(sum(gastos[categoria]) for categoria in gastos)
    print(f"Gastos totales: {total}")
    
if __name__ == "__main__":
    iniciar_registro_gastos()