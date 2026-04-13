import pandas as pd
import sqlite3
import os

# 1. Leer el CSV
# Se usara el CSv de empleados que se creo antes
ruta_csv = os.path.join(os.path.dirname(__file__),"empleados.csv")

# Se verifica que el arcbio exista
# os.path.exists, devolvera True si el archivo existe
if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)
    print("CSV leido correctamente !")
    print(df)
else:
    #Si no existe se creeara
    df= pd.DataFrame({
        "nombre": ["Diego", "Juliana", "David", "Yuls", "Carlos", "Ana"],
        "edad": [28, 28, 30, 31, 25, 27],
        "salario": [1000, 2000, 1500, 800, 2500, 1800],
        "ciudad": ["Medellin", "Bogota", "Cali", "Medellin", "Bogota", "Cali"]
    })
    print("DataFrame creado correctamente!!")
    print(df)

print("------------")
          
# 2 Limpiar los datos con pandas
# Verificar valores vacios
print("Valores vacios:")
print(df.isnull().sum())
print("-------------")

# Eliminar filas con valores vacios si los tienen
df = df.dropna()
# Eliminar duplicados si los hay
df = df.drop_duplicates()

# Estandarizar ciudad
# str.strip() - quita los espacios extras 
# str.capitalize() - primera letra mayuscula
df["ciudad"] = df["ciudad"].str.strip().str.capitalize()

# Agregar columna de bono del 10%
df["bono"] = df["salario"] * 0.10

# Agregat columna de salario total
df["salario_total"] = df["salario"] + df["bono"]

print("Datos limpios y transformados: ")
print(df)
print("--------------------------")

# 3 Guardar en la base de datos SQL
ruta_db = os.path.join(os.path.dirname(__file__), "pipelina.db")
conexion = sqlite3.connect(ruta_db)
# connect() - crea o abre la base de datos

# to_sql - exporta el DataFrame directamente en una tabla SQL
# if_exists="replace" - si la tabla existe la reemplza
# index=False - No guarda el indice de pandas como columna

df.to_sql("empleados", conexion, if_exists="replace", index=False)

print("Datos guardados en bases de datos correctamente!!")
print("---------------------------------------")

# 4 CONSULTAS DATOS DESDE SQL

# SE USA PANDAS PARA LEEER DIRECTAMENTE DESDE SQL
# read_sql()  EJECUTA UNA CONSULTA SQL Y DEVUELVE UN DATAFRAE
df_sql = pd.read_sql("SELECT * FROM empleados", conexion)
print("Datos leidos desde SQL:")
print(df_sql)
print("--------------------------------")

# CONSULTA CON FILTRO DIRECTAMENTO EN SQL
df_filtrado = pd.read_sql("""
    SELECT nombre, salario, salario_total, ciudad
    FROM empleados
    WHERE salario > 1000
    ORDER BY salario DESC
""", conexion)

# COMBINAMOS SQL CON PANDAS EN UNA SOLA CONSULTA
print("Empleados con salario mayor a 1000:")
print(df_filtrado)
print("-----------------------------")

# PROMEDIO DE SALARIO POR CIUDAD USANDO SQL
df_ciudad = pd.read_sql("""
    SELECT ciudad,
        AVG(salario) as promedio_salario,
        COUNT(*) as total_empleados
    FROM empleados
    GROUP BY ciudad
    ORDER BY promedio_salario DESC
""", conexion)
print("Resumen por ciudad:")
print(df_ciudad)
print("-----------------------")

#5 EXPORTAR LOS RESULTADOS A EXCEL

ruta_excel = os.path.join(os.path.dirname(__file__), "reporte_pipeline.xlsx")

with pd.ExcelWriter(ruta_excel, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name = "Datos Limpios", index=False)
    df_filtrado.to_excel(writer, sheet_name = "Filtrados", index=False)
    df_ciudad.to_excel(writer, sheet_name="Resumen Ciudad", index=False)

print("Reporte Excel exportado correctamente!!!")

conexion.close()
print("Pipeline completado exitosamente!!!")