from decimal import Decimal

total = Decimal("0")

while True:
    entrada = input("Ingrese el precio del producto (0 para salir): ")

    try:
        precio = Decimal(entrada)

        if precio == 0:
            break

        total += precio

    except ValueError:
        print("Advertencia: Debe ingresar un número válido.")
        continue

    except:
        print("Advertencia: Entrada inválida.")
        continue

print(f"Total acumulado: ${total}")
