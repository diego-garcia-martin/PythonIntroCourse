import random

palabras = ("demorado","programa","Salamandra","Escofina","quilla","asiento trasero","Castor","cucharon","maestro","Leon Marino","Gavilan","Urraca","capitan","Rinoceronte","bandeja","vestibulo","Pinzas","prensa","sargento","suelo","piso","Serpiente","Dados","Lima","plana","papel","Canguro","Caballito de Mar","despensa","espejo","lateral","Camaron","Pulpo","bateria","Luciernaga","puerta","chimenea","viaje de ida","molde para tortas","Caracol","Prensa de banco","tornillo de banco","pava","Mazo de goma","Cisne","alumno","pasillo","carburador","Morsa","capot","volate","lata","inmigracion","Pulga","Gato","Periquito")

def generar_guiones(palabra):
    guiones = []
    for letra in palabra:
        if letra == ' ':
            guiones.append(' ')
        else:
            guiones.append('-')
    return guiones

def juego():
    intentos = 5
    palabra = palabras[random.randint(0,len(palabras)-1)].lower()
    palabra_oculta = generar_guiones(palabra)
    letras_usadas = []
    while intentos > 0:
        acertado = False
        print(f"Te quedan {intentos} intentos")
        print()
        print()
        for elemento in palabra_oculta:
            print(elemento, end='')
        print()
        print("Letras usadas:")
        for letra in letras_usadas:
            print(letra, end=' ')
        print()
        usuario = input("Escribe una letra: ").lower()
        for i in range(len(palabra)):
            if usuario == palabra[i]:
                palabra_oculta[i] = usuario
                acertado = True
        if acertado == False:
            print("Error!")
            intentos = intentos - 1
        guiones = 0
        for i in palabra_oculta:
            if i == '-':
                guiones = guiones + 1
        if guiones == 0:
            intentos = 0
        if usuario not in letras_usadas:
            letras_usadas.append(usuario)
    print("La palabra era:", palabra)


juego()