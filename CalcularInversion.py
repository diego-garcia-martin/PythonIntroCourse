print("Vamos a calcular cuanto crece tu dinero si es invertido")
monto = float(input("Escribe el monto que vas a invertir: "))
interes = float(input("Escribe el interes mensual esperado: "))
periodo = int(input("Escribe el periodo en meses en que va a estar invertido ese dinero: "))

interes = interes/100

for mes in range(0, periodo):
    monto = monto + (monto * interes)
    print(f"Mes: {mes + 1}      Capital: {monto}")