while True:
    print("******** Es PAR o IMPAR? ********")
    print("* 1- Jugar *")
    print(" // 2- SALIR //")
    opcion = input("Elige una opciones para iniciar o finalizar: \n")

    if opcion == "2":
        print(" Hasta Luego # ")
        break
    try:
        numero = float(input("-- Ingrese el numero: -- .\n"))

        if numero % 2 == 0:
            print(f"{numero} es PAR") 

        else:
            print(f"{numero} es IMPAR")
    
    except ValueError:
        print("Ingrese un valor numerico")
        continue

