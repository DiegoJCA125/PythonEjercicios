import sqlite3
import os

ruta = os.path.join(os.path.dirname(__file__), "futbol.db")
conexion = sqlite3.connect(ruta)
cursor= conexion.cursor()

#SELECT * - Selecionara todas las columnas # FROM jugadores - solo traera los jugadores

cursor.execute("SELECT * FROM jugadores")
todos = cursor.fetchall() #fetchall - Trae todos los resultos de la consulta

print("Todos los jugadores:")
for jugador in todos:
    print(jugador)
print("-------------------------")

#SELECT especifico - traera las columnas que se le diga
cursor.execute("SELECT nombre, equipo, salario FROM jugadores")
parcial = cursor.fetchall()
print("Nombre, equipo y salario:")
for jugador in parcial:
    print(jugador)
print("******************************")

#WHERE - filtra los resultados con lo que se le pida
cursor.execute("SELECT nombre, edad FROM jugadores WHERE edad <30")
jovenes = cursor.fetchall()
print("Jugadores menores de 30 a?os")
for jugador in jovenes:
    print(jugador)
print("------------------")

#ORDER By - ordenara los valores de acuerdo: ASC ascendente / DESC descendente
cursor.execute("SELECT nombre, salario FROM jugadores ORDER BY salario DESC")
por_salario = cursor.fetchall()
print("Jugadores ordenados por salario:")
for jugador in por_salario:
    print(jugador)

conexion.close

