# Solicitar etiqueta de rastreo
etiqueta = input("Ingrese la etiqueta de rastreo: ")

# Validación de seguridad
if etiqueta == "" or etiqueta is None:
    print("Error: La etiqueta no puede estar vacía.")
else:
    # Extraer categoría usando slicing
    primer_guion = etiqueta.find("-")
    ultimo_guion = etiqueta.rfind("-")

    categoria = etiqueta[primer_guion + 1 : ultimo_guion]

    print(f"Categoría detectada: {categoria}")

    # Operador ternario
    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"

    print(ruta)
