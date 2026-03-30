import random
palabras = ["python", "programacion", "computador"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
letras_incorrectas = []
intentos = 6

print (f"La palabra tiene {len(palabra_secreta)} letras")

while intentos > 0:
#muestra progreso del participante
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            print(letra, end=" ") # mostrara la letra
        else:
            print("_", end=" ") #Mostrara el guion

    print()
    print(f"Intentos restantes: {intentos}")
    print(f"Letras inconrrectas: {letras_incorrectas}")

    letra = input("Adivina la letra: \n").lower

    if letra in letras_adivinadas or letra in letras_incorrectas:
        print(f"Ya ingresaste esa letra, intenta con otra")
        continue

    if letra in palabra_secreta:
        letras_adivinadas.append(letra)
        print(f"Bien!!, la letra {letra} esta en la palabra \n")
    else:
        letras_incorrectas.append(letra)
        intentos -= 1
        print(f"Fallaste, la letra {letra} no se encuentra en la palabra")
            
    if all (letra in letras_adivinadas for letra in palabra_secreta):
        print(f"GANASTE!! la palabra es: ||{palabra_secreta}||")
        break

if intentos == 0:
    print(f"PERDISTE TODOS INTENTOS!! la palabra es: \n |{palabra_secreta}|")

