peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu estatura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal es: {imc:.2f}")
