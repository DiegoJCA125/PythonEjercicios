import sqlite3
import os

ruta = os.path.join(os.path.dirname(__file__), "futbol.db")
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

# Insertar jugadores en la tabla
# INSERT INTO ? inserta una fila nueva en la tabla
# VALUES ? los valores de cada columna
jugadores = [
    (1, "Lionel Messi", 35, "Delantero", 50000, "PSG"),
    (2, "Cristiano Ronaldo", 37, "Delantero", 45000, "Al Nassr"),
    (3, "Neymar Jr", 30, "Delantero", 40000, "PSG"),
    (4, "Kylian Mbappe", 23, "Delantero", 55000, "PSG"),
    (5, "Erling Haaland", 22, "Delantero", 48000, "Man City"),
    (6, "Luka Modric", 37, "Mediocampista", 30000, "Real Madrid"),
    (7, "Kevin De Bruyne", 31, "Mediocampista", 35000, "Man City"),
    (8, "Virgil Van Dijk", 31, "Defensa", 25000, "Liverpool"),
    (9, "Thibaut Courtois", 30, "Portero", 28000, "Real Madrid"),
    (10, "Robert Lewandowski", 34, "Delantero", 32000, "Barcelona")
]

# executemany() ? inserta multiples filas de una sola vez
cursor.executemany("""
    INSERT OR IGNORE INTO jugadores 
    VALUES (?, ?, ?, ?, ?, ?)
""", jugadores)
# INSERT OR IGNORE ? si el jugador ya existe no lo duplica
# ? ? son marcadores de posicion para los valores

conexion.commit()
print("Jugadores insertados correctamente!")
conexion.close()