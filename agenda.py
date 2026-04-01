agenda = []

while True:
    print("**AGENDA DE CONTACTOS**")
    print("1. Guardar Contactos")
    print("2. Ver Contactos")
    print("3. Buscar Contactos")
    print("4. Eliminar Contactos")
    print("5. Salir")
    opcion = input ("Elige una opcion \n")

    if opcion == "1": 
        agenda_nombre = input("Nombre del contacto \n")
        agenda_numero = int(input("Numero del contacto \n"))
        agenda.append({"nombre": agenda_nombre, "numero": agenda_numero})
        print(f"Se agrego el contacto: {agenda_nombre} - {agenda_numero}\n")
    #Deja ver los contactos guardados
    elif opcion == "2":
        for numero, contacto in enumerate(agenda, 1):
            print(f"{numero}. {contacto['nombre']} - {contacto['numero']} \n")
    #Busca el contacto
    elif opcion == "3":
        buscar = input("Nombre a buscar: \n")
        for contacto in agenda:
            if contacto["nombre"].lower() == buscar.lower: #buscara sin importar mayusculas 
                print(f"Contacto encontrado: {contacto['nombre']} - {contacto['numero']}")
                encontrado = True
            if not encontrado:
                print("No se encontro el contacto")    
    #Elimina el contacto 
    elif opcion == "4":
        if len(agenda) == 0:
            print("No hay contactos para eliminar")
        else: 
            for numero, contacto in enumerate(agenda, 1):
                print(f"{numero}. {contacto['nombre']} - {contacto['numero']}")
            indice = int(input("Indique el numero del contacto a eliminar? \n"))
            contacto_eliminado = agenda [indice - 1]
            agenda.pop(indice - 1)
            print(f"Se elimino la tarea: {contacto_eliminado}")

    elif opcion == "5":
        print("Chao")  
        break              
