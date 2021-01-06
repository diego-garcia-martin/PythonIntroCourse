print("Vamos a calcular cuanto crece tu dinero si es invertido")
monto = float(input("Escribe el monto que vas a invertir: "))
interes = float(input("Escribe el interes anual esperado: "))
periodo = int(input("Escribe el periodo en meses en que va a estar invertido ese dinero: "))

interes = interes/100/12

for i in range(periodo):
    monto = monto + (monto * interes) + 1000
    print(f"Mes: {i + 1}      Capital: {monto}")