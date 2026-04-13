import sqlite3
import os

ruta = os.path.join(os.path.dirname(__file__), "futbol_joins.db")
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

#Vemos los datos actuales
cursor.execute("SELECT id, nombre, edad, equipo_id FROM jugadores")
print("Jugadores antes de actualizar:")
for fila in cursor.fetchall():
    print(fila)
print("------------------------- \n")

#UPDATE - actualizara un regitro existente
#SET - indica la columna que actualizara y el nuevo valor
#WHERE - indica la fila acualizara
# ATENCION!!!!! sin  WHERE, se actualizara todos los registros

cursor.execute("""
    UPDATE jugadores
    SET equipo_id = 1
    WHERE nombre = 'Messi'
""")
#Se asigna a Messi al Real Madrid (id=1)
conexion.commit() #commit() guardara los cambios
print("Messi se ha actualizado correctamente!!")
print("-------------------- \n")

# Se verifica el cambio
cursor.execute("SELECT nombre, equipo_id FROM jugadores WHERE nombre = 'Messi'")
print("Messi despues de actualizar:")
print(cursor.fetchone())
print("----------------------------\n")

#UPDATE multiple - actualizar varios cmapos a la vez
cursor.execute("""
    UPDATE jugadores
    SET edad = 23, posicion = 'Mediocampista'
    WHERE nombre = 'Pedri'
""")
#Actualizamos la edad y posicion de Pedri al mismo tiempo
conexion.commit()
print("Pedri actualizado Correctamente!!")
print("---------------------------\n")

#DELETE - elimina una fila de la tabla
#CUIDADOOOOO sin el WHERE eliminaria todos los registros
cursor.execute("""
    DELETE FROM jugadores
    WHERE nombre = 'Benzema'
""")
conexion.commit()
print("Benzema eliminado correctamente!!")
print("-------------------------------\n")

# Se verifica los cambios finales
cursor.execute("SELECT id, nombre, edad, posicion, equipo_id FROM jugadores")
print("Jugadores despues de todos los cambios:")
for fila in cursor.fetchall():
    print(fila)

conexion.close()