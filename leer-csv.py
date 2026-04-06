import pandas as pd

#Creas el archivo CSV manual
datos = {
    "nombre": ["Diego", "Juliana", "David", "Yuls", "Carlos", "Ana"],
    "edad": [28, 28, 30, 31, 25, 27],
    "salario": [1000,2500,1500,800,1900,1800],
    "ciudad": ["Medellin", "Medellin", "Bogota", "Cali", "Cartagena", "Bogota"] 
}

df = pd.DataFrame(datos)
df.to_csv("empleados.csv", index=False) #Guarda el csv
print("CSV creado correctamente \n")

#Lee el archivo en csv
df = pd.read_csv("empleados.csv")

print(df)
print("----")

#Muestra las filas y columnas tiene
print(f"Filas y Columnas: {df.shape}")
print("----")

#Las primeras 3 lineas
print(df.head(3))
print("****")

#nombres de columnas
print(f"Columnas: {list(df.columns)}")

#promedio del salario por ciudad
print(df.groupby("ciudad")["salario"].mean())
print("---- Promedio salario x ciudad \n")

#total de salario por ciudad
print(df.groupby("ciudad")["salario"].sum())
print("**** Total de salario x ciudad \n")

#Cuenta personas por ciudad
print(df.groupby("ciudad")["nombre"].count())
