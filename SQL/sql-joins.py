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
conexion.close()

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
conexion.close()

