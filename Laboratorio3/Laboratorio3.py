notas = []

while True:
    print("\n--- SISTEMA DE NOTAS ---")
    print("1. Ingresar notas")
    print("2. Calcular promedio")
    print("3. Mostrar resultado")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            cantidad = input("¿Cuántas notas desea ingresar?: ")

            if cantidad.isdigit():
                cantidad = int(cantidad)
                notas.clear()

                for i in range(cantidad):
                    nota = input(f"Ingrese la nota #{i+1}: ")

                    if nota.replace(".", "", 1).isdigit():
                        notas.append(float(nota))
                    else:
                        print("Nota inválida, se guardará como 0")
                        notas.append(0)
            else:
                print("Cantidad inválida")

        case "2":
            if len(notas) == 0:
                print("No hay notas ingresadas")
            else:
                suma = 0
                for n in notas:
                    suma += n

                promedio = suma / len(notas)
                print(f"Promedio: {promedio:.2f}")

        case "3":
            if len(notas) == 0:
                print("No hay notas ingresadas")
            else:
                suma = 0
                for n in notas:
                    suma += n

                promedio = suma / len(notas)

                print(f"Promedio final: {promedio:.2f}")

                # Evaluación con if
                if promedio >= 6:
                    print("Resultado: Aprobado ✅")
                else:
                    print("Resultado: Reprobado ❌")

        case "4":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción no válida")