def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error, no se puede dividir entre 0"
    return a / b

def calculadora():
    print("****CALCULADORA****")
    print("Operaciones +, -, *, / ")

    while True:
        print("Que calculo requiere?")
        print("1. Realizar calculos")
        print("2. Salir")

        opcion = input("Elige (1. / 2.)")

        if opcion == "2":
            print("Chao")
            break
        elif opcion != "1":
            print("Opcion invalida, por favor vuelve a escribir una opcion valida")
            continue

        try:
            a = float(input("Ingrese primer numero:"))
            operador = input("Operador (+, -, *, /):")
            b = float(input("Ingrese segundo numero:"))
        except ValueError:
            print("Por favor ingresar numeros validos")
            continue    

        if operador == "+":
            resultado = suma(a, b)
        elif operador == "-":
            resultado = resta(a, b)
        elif operador == "*":
            resultado = multiplicacion(a, b)
        elif division == "/":
            resultado = division(a, b)
        else:
            print ("No se reconoce la operacion a realizar")
            continue

        print(f"Resultado: {a} {operador} {b} = {resultado}")

#Se ejecuta
calculadora()
