from tkinter import *
from PIL import Image, ImageTk #se usa la libreria PIL y se importa Image, y ImageTK

window = Tk()
window.title("Imagenes en python")
window.iconbitmap("./Tkinter/images/icon.ico")
window.geometry("920x600")
Label(window, text="Ojitos Chiquitos").pack()
image = Image.open("./Tkinter/images/sapo.jpg") #se guarda la ruta en una variable que la abre
render = ImageTk.PhotoImage(image) #se renderiza la imagen
Label(window, image=render).pack() #se abre en un label y se hace el pack
window.mainloop()
