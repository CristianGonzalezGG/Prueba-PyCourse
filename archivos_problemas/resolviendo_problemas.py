#dos listas una con nombres y la otra con apellidos
nombres = ["Lucas","Cristian","Mario","Carlos","Roberto"]
apellidos = ["Gonzalez","Rodriguez","Hernandez","Montes","Tarado"]

#registrar esa informacion en un TXT con un FOR
with open("nombres_y_apellidos.txt","w") as arch:
          arch.writelines("Los datos son: \n")
          [arch.writelines(f"nombre: {n}\n Apellido: {a}\n-----\n")for n,a in zip(nombres,apellidos)]