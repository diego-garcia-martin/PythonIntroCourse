from tkinter import *

def sign_in():
    usuario = e_user.get()
    password = e_pass.get()
    print(f"El usuario puso: {usuario}")
    print(f"La contraseña que puso es: {password}")


window = Tk()
window.title("Pagina")

l_user = Label(window, text="Usuario:", font=("Arial", 22), height=2)
l_pass = Label(window, text="Clave:", font=("Arial", 22), height=2)
e_user = Entry(window, font=("Arial", 22))
e_pass = Entry(window, font=("Arial", 22))
b_signup = Button(window, text="Sign Up:", font=("Arial", 22), height=2)
b_signin = Button(window, text="Sign In:", font=("Arial", 22), height=2, command=lambda: sign_in())

l_user.grid(row=0, column=0, padx=5)
l_pass.grid(row=1, column=0, padx=5)
e_user.grid(row=0, column=1, columnspan=2, padx=20)
e_pass.grid(row=1, column=1, columnspan=2, padx=20)
b_signup.grid(row=2, column=0, padx=15, pady=15)
b_signin.grid(row=2, column=1, padx=15, pady=15)

window.mainloop()