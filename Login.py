from tkinter import *
from tkinter import messagebox

def sign_in():
    usuario = e_user.get()
    password = e_pass.get()
    lista_datos = []
    with open("datos.txt", "r") as reader:
        for line in reader.readlines():
            lista_datos.append(line)    # lista_datos = ["usuario1", "pass1", "usuario2", "pass2"]
    lista_usuarios = []
    lista_passwords = []
    for i in range(len(lista_datos)):
        if i == 0 or i%2 == 0:
            lista_usuarios.append(lista_datos[i]) # lista_usuarios = ["usuario1", "usuario2"]
        else:
            lista_passwords.append(lista_datos[i]) # lista_passwords = ["pass1", "pass2"]
    if (usuario + "\n") not in lista_usuarios:
        messagebox.showinfo("Login","Usuario no encontrado")
    else:
        index = lista_usuarios.index(usuario + "\n")
        if (password + "\n") != lista_passwords[index]:
            messagebox.showinfo("Login","Password Incorrecto")
        else:
            messagebox.showinfo("Login", "Acceso Concedido!")

def sign_up():
    usuario = e_user.get()
    password = e_pass.get()
    with open("datos.txt", "r") as reader:
        for line in reader.readlines():
            if line == usuario + "\n":
                messagebox.showinfo("Login", "Usuario ya registrado!")
                return
    with open("datos.txt", "a") as writer:
        writer.write(f"{usuario}\n{password}\n")
    messagebox.showinfo("Login", "Usuario Registrado correctamente")
    e_user.delete(0, END)
    e_pass.delete(0, END)


'''Creamos el archivo de los datos si es que no existe'''
try:
    archivo_datos = open("datos.txt", "x")
    archivo_datos.close()
except FileExistsError:
    print("El archivo ya existe")

'''Todo lo de la interfaz grafica '''
window = Tk()
window.title("Pagina")

l_user = Label(window, text="Usuario:", font=("Arial", 22), height=2)
l_pass = Label(window, text="Clave:", font=("Arial", 22), height=2)
e_user = Entry(window, font=("Arial", 22))
e_pass = Entry(window, font=("Arial", 22), show='*')
b_signup = Button(window, text="Sign Up:", font=("Arial", 22), height=2, command=lambda: sign_up())
b_signin = Button(window, text="Sign In:", font=("Arial", 22), height=2, command=lambda: sign_in())

l_user.grid(row=0, column=0, padx=5)
l_pass.grid(row=1, column=0, padx=5)
e_user.grid(row=0, column=1, columnspan=2, padx=20)
e_pass.grid(row=1, column=1, columnspan=2, padx=20)
b_signup.grid(row=2, column=0, padx=15, pady=15)
b_signin.grid(row=2, column=1, padx=15, pady=15)

window.mainloop()