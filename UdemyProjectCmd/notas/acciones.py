import notas.nota as model
class Acciones:
    def crear(self, usuario):
        print(f"Hola!! {usuario[1]}, vamos a crear una nueva nota.. ")
        titleSave = input("Primero dime como quieres llamar a la nota:  ")
        descripSave = input("Escribe lo que deseas guardar en esta nota:  ")
        notes = model.Nota(usuario[0],titleSave, descripSave)
        guardar = notes.save()
        if guardar[0] >= 1:
            print(f"\n Perfecto has guardado la nota: {notes.Title}")
        else:
            print(f"\n No se ha podido guardar la nota, lo siento{usuario[1]}")
    def mostrar(self, usuario):
        print(f"Hola!! {usuario[1]}, Estas son las notas que tienes guardas.. ")
        note = model.Nota(usuario[0],"","")
        notes = note.listar()
        for nota in notes:
            print("***************************************")
            print(f"ID de Author: {nota[1]}")
            print(nota[2])
            print(nota[3])
            print("***************************************")
    def deletes(self, usuario):
        print(f"OK! {usuario[1]} Vamos a borrar una de tus notas")
        title = input("Titulo de la Nota que quieres borrar: ")
        #description = ""  # Puedes dejar la descripción vacía o solicitarla al usuario
        note = model.Nota(usuario[0], title, "")
        delete2 = note.delete()
        if delete2[0] >= 1:
            print(f"Hemos borrado correctamente la nota: {title}")
        else:
            print("No se ha borrado la nota. Prueba luego")