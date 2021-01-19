from tkinter import *
from tkinter import messagebox


def cambioColor(boton, lab):
    if boton["text"] == "Red":
        lab.config(bg="red")
    if boton["text"] == "Blue":
        lab.config(bg="blue")
    if boton["text"] == "Green":
        lab.config(bg="green")


window = Tk()
window.title("Mi Pantalla")

l1 = Label(window, text="Color",font=("Arial", 22), height=4, width=6)

b1 = Button(window, text="Red", font=("Arial", 22), height=4, width=6, command=lambda: cambioColor(b1, l1))
b2 = Button(window, text="Blue", font=("Arial", 22), height=4, width=6, command=lambda: cambioColor(b2,l1))
b3 = Button(window, text="Green", font=("Arial", 22), height=4, width=6, command=lambda: cambioColor(b3, l1))


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
l1.grid(row=1, column=1)

window.mainloop()