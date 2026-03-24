while True:
    print("Ingresa los valores para realizar la cuenta")

    try:
        total = float(input("Cual es el valor de la cuenta? \n"))
        porcentaje = float(input("Cual es el porcentaje de propinar que quieres dar? (Ejemplo: 10, 15, 20) \n"))
        personas = int(input("Cuantas personas se divide la cuenta? \n"))

        propina = total * (porcentaje / 100)
        total_propina = total + propina
        por_persona = total_propina / personas

        print (f"La propina corresponde a: {propina}\n")
        print(f"Total con propina es: {total_propina}\n")
        print(f"Cada persona debe pagar: {por_persona}\n")

    except ValueError:
        print("Ingresa valores numericos")
        continue

