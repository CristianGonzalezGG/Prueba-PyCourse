# Clase que representa un personaje
class Characters:
    def __init__(self, name, force, duration):
        """
        Constructor de la clase Characters.

        Parameters:
        - name (str): Nombre del personaje.
        - force (float): Fuerza del personaje.
        - duration (float): Duración o resistencia del personaje.
        """
        self.name = name
        self.force = force
        self.duration = duration 

    def __repr__(self):
        """
        Método de representación que devuelve una cadena que representa el objeto Characters.
        """
        return f'{self.name}(fuerza: {self.force}, Resistencia: {self.duration})'

    def __add__(self, addOther):
        """
        Método especial para la suma de dos personajes. 
        Crea un nuevo personaje con un nombre combinado, fuerza y duración promediadas y redondeadas.

        Parameters:
        - addOther (Characters): Otro personaje para la fusión.

        Returns:
        - Characters: Nuevo personaje fusionado.
        """
        newName = f"{self.name}-{addOther.name}"
        newForce = round(((self.force + addOther.force) / 2) ** 1.2)
        newDuration = round(((self.duration + addOther.duration) / 2) ** 1.2)
        return Characters(newName, newForce, newDuration)

def showCharacters(characters_list):
    """
    Muestra la lista de personajes.

    Parameters:
    - characters_list (list): Lista de personajes.
    """
    if not characters_list:
        print("Aun no hay personajes")
    else:
        print("Personajes Disponibles: ")
        for i, character in enumerate(characters_list):
            print(f'{i + 1}. {character}')

def CreatePJ():
    """
    Solicita al usuario el nombre, fuerza y duración de un nuevo personaje y devuelve un objeto Characters creado con esos valores.

    Returns:
    - Characters: Nuevo personaje creado.
    """
    name = input("Ingrese el nombre del PJ: ")
    force = float(input("Ingrese la fuerza del PJ: "))
    duration = float(input("Ingrese la resistencia del PJ: "))
    return Characters(name, force, duration)

# Lista para almacenar personajes
characters_list = []

# Menú principal
while True: 
    print("\n1. Crear personaje")
    print("2. Fusionar Pj's")
    print("3. Mostrar Personajes")
    print("4. Salir del programa")
    option = input("Ingrese una opción: ")
    
    if option == "1": 
        # Opción: Crear personaje
        new_character = CreatePJ()
        characters_list.append(new_character)
    elif option == "2":
        # Opción: Fusionar personajes
        if len(characters_list) < 2:
            print("Debes tener al menos dos Pj para poder fusionarlos.")
        else:
            showCharacters(characters_list)
            num_Pj1 = int(input("Ingrese el número del primer PJ: "))
            num_Pj2 = int(input("Ingrese el número del segundo PJ: "))
            
            if 1 <= num_Pj1 <= len(characters_list) and 1 <= num_Pj2 <= len(characters_list) and num_Pj1 != num_Pj2:
                char1 = characters_list[num_Pj1 - 1]
                char2 = characters_list[num_Pj2 - 1]
                new_character = char1 + char2
                characters_list.append(new_character)
                print(f"Fusión Exitosa! El nuevo personaje es: {new_character}")
            else:
                print("Selección Inválida")
    
    elif option == "3":
        # Opción: Mostrar personajes
        showCharacters(characters_list)
    elif option == "4":
        # Opción: Salir del programa
        print("Saliendo del programa")
        break
    else: 
        print("Elija una Opción válida")

# Fin del programa
print("Juego Finalizado")

    
                
