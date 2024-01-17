from tkinter import *

window = Tk()
window.title("Prueba de Textos Tkinter")
window.iconbitmap("./Tkinter/images/icon.ico")
window.geometry("920x600")
window.resizable(0,0)
texto = Label(window, text="Bienvenido a mi programa")
#Para modificar el texto usamos el ".config" para modificarlo donde:fg="modifica el color de la letra",bg="clor fondo",padx=padding X,pady=padding Y 
texto.config(fg="white",bg="black",padx=520,pady=20,font=("Consolas",20))
texto.pack()
texto = Label(window, text="Soy Cristian Gonzalez")
#para poder manejar ele movimiento de el texto se debehacer desde el "pack"
texto.config(width=20,height=7,bg="orange",cursor="spider")
texto.pack(anchor = W)
texto = Label(window, text="Portafolio")
#para poder manejar ele movimiento de el texto se debehacer desde el "pack"
texto.config(width=20,height=7,bg="orange",cursor="spider")
texto.pack(anchor = E)
window.mainloop()