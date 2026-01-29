# TUPLAS - No se pueden modificar (inmutables)
# Se crean con paréntesis ()

coordenadas = (10, 20, 30)
print(coordenadas)

# Acceder a elementos
print(coordenadas[0])
print(coordenadas[2])

# NO se puede modificar
# coordenadas[0] = 5

# NO se puede agregar
# coordenadas.append(40)

# Desempacar tupla
x, y, z = coordenadas
print(x, y, z)

# Longitud
print(len(coordenadas))