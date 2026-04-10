import sqlite3
import os

ruta = os.path.join(os.path.dirname(__file__), "futbol.db")
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

#COUNT() - cuenta los registro que existen
cursor.execute("SELECT COUNT (*) FROM jugadores")
total = cursor.fetchone() #fetchone trae solo un resultado en vez de todos
print(f"Total de jugadores: {total[0]}")
print("-----------------------------------------")

#AVG() - promedio
#MAX() - valor maximo
#MIN() - valor minimo

cursor.execute("SELECT AVG(salario), MAX(salario), MIN(salario) FROM jugadores")
estadisticas = cursor.fetchone()
print(f"Salario promedio es de:  {estadisticas[0]}")
print(f"Salario maximo es de: {estadisticas[1]}")
print(f"Salario minimo es de: {estadisticas[2]}")
print("-----------------------------")

#GRUPO BY agrupo resultados por una columna
cursor.execute("""
    SELECT posicion, COUNT(*) as total, AVG(salario) as promedio
    FROM jugadores
    GROUP BY posicion
    ORDER BY promedio DESC
""") # AS - le da nombre a la columna solicitada

por_posicion = cursor.fetchall()
print("Jugadores y salario promedio por posicion:")
for fila in por_posicion:
    print(f"{fila[0]} - {fila[1]} Jugadores - promedio: {fila[2]}")
print("--------------------------------------")

#LIKE -  busca texto que contenga algo
cursor.execute("SELECT nombre, equipo FROM jugadores WHERE equipo LIKE '%PSG%'")
# % - Significa que cualquier texto antes o despues de la palabra asignada
psg = cursor.fetchall()
print("Jugadores del PSG:")
for jugador in psg:
    print(jugador)

conexion.close()      