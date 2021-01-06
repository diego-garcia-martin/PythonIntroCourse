print("Vamos a calcular el precio de un producto agregando el IVA")
iva = 0.16
precio = float(input("Dame el precio de un producto: "))

precio_nuevo = precio + (precio * iva)

print(f"El precio del producto con el IVA incluido es de ${precio_nuevo}")