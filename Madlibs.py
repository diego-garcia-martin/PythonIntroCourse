import random
def Madlib():
    num = random.randint(1,1) # Agregar más Madlibs y cambiar el número
    if num == 1:
        sus1 = input("Sustantivo masculino: ")
        adj1 = input("Adjetivo masculino: ")
        adj2 = input("Adjetivo masculino: ")
        adj3 = input("Adjetivo masculino: ")
        verb1 = input("Verbo infinitivo: ")
        adj4 = input("Adjetivo masculino: ")
        adj5 = input("Adjetivo femenino: ")
        adj6 = input("Adjetivo masculino: ")
        verb2 = input("Verbo infinitivo: ")
        sus2 = input("Sustantivo masculino: ")
        adj7 = input("Adjetivo masculino: ")
        verb3 = input("Verbo pasado: ")
        sus3 = input("Parte del cuerpo: ")
        verb4 = input("Verbo infinitivo: ")

        print(f"Había ido yo a visitar a mi {sus1} el señor Sherlock Holmes cierto día de otoño del año pasado,\n\
        y me lo encontré muy {adj1} en conversación con un caballero {adj2} muy {adj3},\n\
        de cara rubicunda y cabellera de un subido color rojo. Iba yo a {verb1}, disculpándome por mi\n\
        entremetimiento, pero Holmes me hizo {verb4} bruscamente de un tirón, y cerró la puerta a mis\n\
        espaldas.\n\
        -Mi {adj4} Watson, no podía usted {verb2} en mejor momento -me dijo con expresión {adj5}.\n\
        -Creí que estaba usted {adj6}.\n\
        -Lo estoy, y muchísimo.\n\
        -Entonces puedo esperar en la habitación de al lado.\n\
        -De ninguna manera. Señor Wilson, este {sus2} ha sido compañero y colaborador mío en muchos\n\
        de los casos que mayor éxito tuvieron.\n\
        El {adj7} caballero me {verb3} con una inclinación de\n\
        {sus3}.")


Madlib()