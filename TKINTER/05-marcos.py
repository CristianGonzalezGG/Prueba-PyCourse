from tkinter import *

#los frames o marcos son ventanas dentro de otras ventanas
window = Tk()
window.title("Interfaz Grafica en Python")
window.iconbitmap("./Tkinter/images/icon.ico")
window.geometry("920x600")
marcop = Frame(window, width=250,height=250)
marcop.config(bg="light green",bd=5,relief="raised")
marcop.pack(side=BOTTOM,fill=X, expand=YES)
marco = Frame(marcop, width=250,height=250)   #<---   #se creas y se le da unas dimensiones
marco.config(bg="red",bd=5,relief="raised")   #<---   #se puede cambiar sus propiedades
marco.pack(side=LEFT,anchor=SW)               #<---   #y modificar la pocision
marco = Frame(marcop, width=250,height=250)
marco.config(bg="light green",bd=5,relief="raised")
marco.pack(side=RIGHT,anchor=SE)
marcop = Frame(window, width=250,height=250)
marcop.config(bg="light green",bd=5,relief="raised")
marcop.pack(side=TOP,fill=X, expand=YES)
window.mainloop()
