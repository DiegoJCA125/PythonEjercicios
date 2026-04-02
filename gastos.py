gastos = []

while True:
    print("**REGISTROS DE GASTOS")
    print("1. Agregar gasto")
    print("2. Ver los gastos")
    print("3. Ver total de gastados")
    print("4. Ver categorias")
    print("5. Salir")
    opcion = input ("Elige una opcion \n")

    if opcion == "1":
        gasto_categoria = input("Ingrese la categoria del gasto \n")
        gasto_valor = int(input("ingrese el valor del gasto \n"))
        gastos.append({"categoria": gasto_categoria, "valor": gasto_valor})
        print(f"El gasto que se agreso es: {gasto_categoria} - {gasto_valor}")

    #Muestras los gastos
    elif opcion == "2":
        for numero, categoria in enumerate (gastos, 1):
            print(f"{numero}. {categoria['categoria']} - {categoria['valor']} \n")

    elif opcion == "3":
        total_gastos = sum(gasto['valor'] for gasto in gastos)
        print(f"El total de gastos es: {total_gastos} \n")
    
    elif opcion == "4":
        categoria_buscar = input("Que categoria desea ver? \n")
        encontrado = False
        for gasto in gastos:
            if gasto["categoria"].lower() == categoria_buscar.lower():
                print(f"Gasto encontrado: {gasto['categoria']} - {gasto['valor']}")
                encontrado = True
        if not encontrado:
            print("No se encontro la categoria")

    elif opcion == "5":
        print("Chao")  
        break