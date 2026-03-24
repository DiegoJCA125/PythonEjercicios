import random
numero_secreto = random.randint(1,10)

while True:
    print("Adivinaremos tu numero")
    
    try:
        numero = int(input("-- Ingresa un numero del 1 al 10 \n"))

        if numero == numero_secreto:
            print(f"Adivinaste el numero al azar")
            break

        elif numero < numero_secreto:
            print(f"Tu numero esta por debajo")

        else:
            print(f"Tu numero esta por encima")

    except ValueError:
            print("Ingrese un valor numerico")
            continue


