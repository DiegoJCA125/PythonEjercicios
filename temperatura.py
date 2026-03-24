while True:
    print ("**Que deseas convertir?**")
    print ("*1. Celsius a Fahrenheit*")
    print ("**2. Fahrenheit a Celsius**")
    print ("***3. Salir***")
    opcion = input("Elige (1. / 2. / 3.): \n")

    if opcion == "3":
        print("Chao")
        break

    if opcion == "1":
        try:
            celsius = float(input("----Ingresa la temperatura en Celsius:---- \n"))
            fahrenheit = (celsius * 9/5) + 32 
            print(f"******La tempratura en Fahrenheit es: {fahrenheit}******")
        except ValueError:
            print("Por favor ingrese valores numericos")
            continue
    elif opcion == "2":
        try:
            fahrenheit = float(input("-----Ingresa la temperatura en Fahrenheit:---- \n"))
            celsius = (fahrenheit - 32) * 5/9
            print(f"******El resultado en Celius es: {celsius}******")
        except ValueError:
            print("---Por favor ingrese valores numericos---")
            continue
    else: 
        print("//No se reconoce la opcion a realizar//")
        continue

