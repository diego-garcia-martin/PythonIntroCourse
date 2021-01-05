import random

textos = ["piedra", "papel", "tijera"]

def juego():
    intentos = 3
    while intentos > 0:
        print(f"Juguemos Piedra Papel o Tijera, tenemos {intentos} intentos")
        s_usuario = input("Escribe piedra, papel o tijera, y yo escojo lo mio: ").lower()
        i_usuario = textos.index(s_usuario)
        i_compu = random.randint(0,2)
        s_compu = textos[i_compu]
        print()
        print(s_compu + "!")
        print()
        if i_compu == i_usuario:
            print()
            print("Empatamos!!")
            print()
        elif i_compu == 0 and i_usuario == 2 or i_compu == 1 and i_usuario == 0 or i_compu == 2 and i_usuario == 1:
            print()
            print("Te gane!!! tienes un intento menos.")
            print()
            intentos = intentos - 1
        else:
            print()
            print("Felicidades, me ganaste!!!")
            print()
            intentos = 0


juego()