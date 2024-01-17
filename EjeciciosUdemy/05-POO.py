class Celular:
    def __init__(self, modelo, almacenamiento):
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.defectuoso = False

    def __str__(self):
        return f"Modelo: {self.modelo}, Almacenamiento: {self.almacenamiento}GB, Defectuoso: {self.defectuoso}"

    def reportarDefecto(self):
        self.defectuoso = True

    def ArreglarDefecto(self):
        self.defectuoso = False

def addCelulares():
    modelo = input("Ingrese el modelo de el celular: ")
    almacenamiento = int(input("GBS de almacenamiento: "))
    # defectuoso
    newCha = Celular(modelo, almacenamiento)
    return newCha

def showCharacters(listaCelulares):
    if not listaCelulares:
        print("Aun no hay celulares")
    else:
        print("Celulares disponibles: ")
        for celular in listaCelulares:
            print(celular)

def showCharactersDef(listaCelularesDefec):
    if not listaCelularesDefec:
        print("No hay celulares defectuosos en reparación")
    else:
        print("Celulares Defectuosos en Reparacion: ")
        for celular in listaCelularesDefec:
            print(f" - {celular}")

def agregaCeluDef(modelo, listaCelulares):
    for celular in listaCelulares:
        if celular.modelo == modelo:
            return celular
    return None

listaCelulares = []
listaCelularesDefec = []

while True:
    print("\n1. Agregar celular. ")
    print("2. Mostrar celulares. ")
    print("3. Reportar uno defectuoso. ")
    print("4. Mostrar Celulares defectuosos. ")
    print("5. Retirar un Celular defectuoso. ")
    option = input("Ingrese una opción: ")

    if option == "1":
        new_character = addCelulares()
        listaCelulares.append(new_character)
    elif option == "2":
        showCharacters(listaCelulares)
    elif option == "3":
        showCharacters(listaCelulares)
        agregarCelu = input("Ingrese el celular que salió defectuoso: ")
        defectu = agregaCeluDef(agregarCelu, listaCelulares)
        if defectu and not defectu.defectuoso:
            defectu.reportarDefecto()
            print(f"El celular {defectu.modelo} está defectuoso")
            listaCelularesDefec.append(defectu)
        elif defectu and defectu.defectuoso:
            print(f"Ya está reportado como defectuoso")
        else:
            print("No se encontró el celular")
    elif option == "4":
        showCharactersDef(listaCelularesDefec)
    elif option == "5":
        showCharactersDef(listaCelularesDefec)
        celNoDef = input("Ingrese el modelo del celular que desea retirar de estado defectuoso: ")
        celEnDefectuoso = agregaCeluDef(celNoDef, listaCelularesDefec)
        
        if celEnDefectuoso:
            celEnDefectuoso.ArreglarDefecto()
            print(f"El celular {celEnDefectuoso.modelo} sale de estado defectuoso y entra a stock")
            listaCelularesDefec.remove(celEnDefectuoso)
        else:
            print(f"El celular {celNoDef} no se encuentra en estado defectuoso")

    else:
        print("Opción no válida")
