# Solicitar nombre completo
nombre_completo = input("Ingrese su nombre y apellido: ")

# Convertir a lista
partes_nombre = nombre_completo.split()

# Invertir lista usando slicing negativo
nombre_invertido = partes_nombre[::-1]

# For anidado
for palabra in nombre_invertido:

    for letra in palabra:
        print(letra, end=".")

    print(" ", end="")
