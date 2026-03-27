import random
opciones = ["piedra", "papel" , "tijera"]
# random.choice() va a elegir al azar una opcion de una lista 

while True:
    eleccion_computador = random.choice(opciones)
    print("Juguemos a Piedra, Papel, Tijera \n" )
    try:
        eleccion_usuario = input("Elige ( Piedra / Papel / Tijera )\n").lower()

        if eleccion_computador == eleccion_usuario:
            print(f"Empate {eleccion_computador} vs {eleccion_usuario}\n")
            continue
        elif (eleccion_usuario == "piedra" and eleccion_computador == "tijera") or (eleccion_usuario == "tijera" and eleccion_computador == "papel") or (eleccion_usuario == "papel" and eleccion_computador == "piedra"):
            print("**GANASTE!**")

        else: 
            print("*GANO LA COMPUTADORA :(*")
            
        opcion = input("Desea jugar de nuevo? 1. Si / 2. No \n")
        if opcion == "2":
            break

    except ValueError:
        print("Ingrese los valores correctos")
        continue

        