palabra = input("Ingresa una palabra \n")
contador = 0

for letra in palabra:
    if letra in "aeiou":
        contador = contador + 1

print(f"Tiene {contador} vocales")