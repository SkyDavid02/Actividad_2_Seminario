precio = float(input("Ingresa el precio sin IVA: "))

iva = precio * 0.16
precio_final = precio + iva

print("IVA:", iva)
print("Precio final con IVA:", precio_final)
