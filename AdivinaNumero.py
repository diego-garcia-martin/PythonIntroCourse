import random

def Adivinar_Usuario(x):
    numero = random.randint(1, x)
    numero_usuario = 0
    print(f"Adivina un numero entre el 1 y el {x}")
    while numero_usuario != numero:
        numero_usuario = int(input("Escribe un numero: "))
        if numero_usuario < numero:
            print("Tu numero es muy bajo")
        elif numero_usuario > numero:
            print("Tu numero es muy alto")
    print("¡Felicidades lo adivinaste!")

def Adivinar_Compu(x):
    min = 1
    max = x
    control = "no"
    print(f"Piensa en un numero entre el 1 y el {x}, yo lo voy a adivinar")
    while control != "si":
        numero = random.randint(min, max)
        print(f"Tu numero es {numero}?")
        control = input("Escribe 'si' 'alto' o 'bajo': ").lower()
        if control == "alto":
            max = numero - 1
        elif control == "bajo":
            min = numero + 1
    print("¡Yay, adivine el numero!")


Adivinar_Usuario(20)
Adivinar_Compu(20)