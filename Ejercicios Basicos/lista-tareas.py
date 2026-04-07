tareas = []

while True:
    print("\n **** Lista de Trabajo ****")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = input ("Elige una opcion: \n")

    if opcion == "1":
        tarea = input("Cual es la tarea? \n")
        tareas.append(tarea)
        print(f"Se agrego la tarea: {tarea}")

    elif opcion == "2":
        for numero, tarea in enumerate(tareas, 1):
            print(f"{numero}. {tarea} \n")

    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para eliminar")
        else: 
            for numero, tarea in enumerate(tareas, 1):
                print(f"{numero}. {tarea}")
            indice = int(input("Indique el numero de la tarea a eliminar? \n"))
            tareas_eliminadas = tareas [indice - 1]
            tareas.pop(indice - 1)
            print(f"Se elimino la tarea: {tareas_eliminadas}")

    elif opcion == "4":
        print("Chao")  
        break  