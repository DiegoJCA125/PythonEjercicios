import sqlite3
import os

ruta = os.path.join(os.path.dirname(__file__), "futbol_joins.db")
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

#Tabla 1 - Jugadores
cursor.execute("""
    CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER,
        posicion TEXT,
        equipo_id INTEGER 
    )  
""")
# Equipo id es la columna que conecta con la tabla equipos
        # A la llave foranea (FOREIGN KEY) de la otra tabla
    

#Tabla2 - Equipos
cursor.execute("""
     CREATE TABLE IF NOT EXISTS equipos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        ciudad TEXT,
        estadio TEXT
    )
""")

conexion.commit()
print("Tablas creadas correctamente")

import sqlite3
import os

ruta = os.path.join(os.path.dirname(__file__), "futbol_joins.db")
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

#insertar equipos primero
#Siempre se insertan primero los datos de la tabla principal
equipos = [
    (1, "Real Madrid", "Madrid", "Santiago Bernabeu"),
    (2, "Barcelona", "Barcelona", "Camp Nou"),
    (3, "PSG", "Paris", "Parc des Princes"),
    (4, "Man City", "Manchester", "Etihad Stadium"),
    (5, "Liverpool", "Liverpool", "Anfield")
]

cursor.executemany("""
    INSERT OR IGNORE INTO equipos VALUES (?, ?, ?, ?)          
""", equipos)
#INSERT OR IGNORE - Evita insertar datos duplicados
#insertar jugadores/ equipo_id hace referencia la id de la tabla equipos
#ejemplo: equipo_id=1  es el Real Madrid

jugadores =[
    (1, "Vinicius Jr", 22, "Delantero", 1),
    (2, "Benzema", 35, "Delantero", 1),
    (3, "Pedri", 20, "Mediocampista", 2),
    (4, "Lewandowski", 34, "Delantero", 2),
    (5, "Mbappe", 24, "Delantero", 3),
    (6, "Neymar", 31, "Delantero", 3),
    (7, "Haaland", 22, "Delantero", 4),
    (8, "De Bruyne", 32, "Mediocampista", 4),
    (9, "Salah", 31, "Delantero", 5),
    (10, "Van Dijk", 31, "Defensa", 5),
    (11, "Messi", 36, "Delantero", None)
]
# NONE significa que Messi no tiene equipo asignado en esta base de datos
# servira de ejemplo para la diferencia entre JOINs

cursor.executemany("""
    INSERT OR IGNORE INTO jugadores VALUES (?, ?, ?, ?, ?)
""", jugadores)

conexion.commit()
print("Datos insertados correctamente")

#INNER JOIN - solo jugadores que tienen equipos asginados
#Une las tablas donde equipo_id coindice con el id delequipo

cursor.execute("""
    SELECT jugadores.nombre, jugadores.posicion, equipos.nombre, equipos.ciudad
    FROM jugadores
    INNER JOIN equipos ON jugadores.equipo_id = equipos.id
""")
# ON - indica por que columna se unen las tablas
# jugadores.equipo_id = equipos.id es la columna en comun

inner = cursor.fetchall()
print("INNER JOIN - jugadores con equipo:")
for fila in inner:
    print(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]}")
print("---------------------------")

#LEFT JOIN - todos los jugadores aunque no tengan equipo
cursor.execute("""
    SELECT jugadores.nombre, jugadores.posicion, equipos.nombre
    FROM jugadores
    LEFT JOIN equipos ON jugadores.equipo_id = equipos.id
""")
#LEFT JOIN - trae todos la tabla izquierdo (jugadores)
#Si no tienen equipo, muestra el NULL en las columnas de equipo
left = cursor.fetchall()
print("LEFT JOIN - todos los jugadores:")
for fila in left:
    print(f"{fila[0]} | {fila[1]} | {fila[2]}")
print("----------------------")

#JOIN con WHERE - jugadores del real madrid
cursor.execute("""
    SELECT jugadores.nombre, jugadores.edad, equipos.estadio
    FROM jugadores
    INNER JOIN equipos ON jugadores.equipo_id = equipos.id
    WHERE equipos.nombre = 'Real Madrid'
""")
#Combinamos JOIN con WHERE para filtrar los reusltados

real_madrid = cursor.fetchall()
print("Jugadores del Real Madrid:")
for fila in real_madrid:
    print(f"{fila[0]} | Edad: {fila[1]} | Estadio: {fila[2]}")

conexion.close()