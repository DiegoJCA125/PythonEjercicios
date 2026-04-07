import pandas as pd
import numpy as np

datos = {
    "nombre": ["Diego", "Juliana", "David", None, "Yuls", "Carlos", "Diego"],
    "edad": [28, None, 30, 31, -5, 28, 35],
    "salario": [1000, 3000, None, 800, 2200, 1000, 500],
    "ciudad": ["medellin", "Bogota", "CALI", "Cali ", "Bogota", "medellin", "Armenia"]
}

df = pd.DataFrame(datos)
print("Datos sucios: ")
print(df)

#Cuantos valores vacios hay por columna
print("Valores vacios por columna: ")
print(df.isnull().sum())
print("----")

#Elimina filas con valores vacios
df_limpio = df.dropna()
print("Sin valores vacios: ")
print(df_limpio)
print("****")

#Elimina duplicados
df_limpio = df_limpio.drop_duplicates()
print("Sin duplicados: ")
print(df_limpio)
print("////")

#Elimina edades imposibles
df_limpio = df_limpio[df_limpio["edad"] > 0]
print("Sin edades imposibles: ")
print(df_limpio)

#Organiza las minusculas y mayusculas en la columna Ciudad
df_limpio["ciudad"] = df_limpio["ciudad"].str.strip() # Quita los espacios
df_limpio["ciudad"] = df_limpio["ciudad"].str.capitalize() # primera letra mayuscula
print("Ciudades Limpias: ")
print(df_limpio)
print("***")

# Resultado final
print("Tabla final limpia: ")
print(df_limpio.to_string(index=False))

#Gardar en archivo .csv
df_limpio.to_csv("Limpieza Datos/empleados_limpios.csv", index=False)
print("Archivo guardado correctamente")

## Crear la ruta correcta automaticamente
#ruta = os.path.join(os.path.dirname(__file__), "empleados_limpios.csv")
#df_limpio.to_csv(ruta, index=False)
#print("Archivo guardado correctamente!")