for numero in range(1, 51):

    # Saltar múltiplos de 3
    if numero % 3 == 0:
        continue

    # Detener en el 42
    if numero == 42:
        print("Amenaza detectada. Proceso detenido.")
        break

    print(f"Procesando registro ID: {numero}")
