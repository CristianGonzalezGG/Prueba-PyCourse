from tkinter import *
#CREAR VENTANA RAIZ
window = Tk()
#Titulo de la ventana
window.title("Interfaz Grafica en Python")
#icono de la ventana
window.iconbitmap("./Tkinter/images/icon.ico")
#cambio de tamaño de la ventana
window.geometry("920x600")
#bloquear la redimensacion
window.resizable(0,0)
#texto
text = Label(window, text="Hola Chavalines")
text.pack()
#arrancar y mostrar la ventana hasta que se cierre
window.mainloop()
