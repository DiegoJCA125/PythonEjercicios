import pandas as pd

datos ={
    "nombre": ["Diego", "Juliana", "David", "Yuls"],
    "edad": [28, 28, 30, 31],
    "salario": [1000, 2000, 1500, 800]
}
df = pd.DataFrame(datos)
print(df)

#primeras filas
print(df.head())

#informacion general de la tabla
print(df.info())

#estadistica basica
print(df.describe())

#solo una colomna
print(df["salario"])

#salario promedio   
print(df["salario"].mean())

#Salario maximo
print(df["salario"].max())

#Salario minimo
print(df["salario"].min())

#Salario mayor a 1000
print(df[df["salario"] > 1000])

#Personas con edad menor a 30
print(df[df["edad"] < 30])

#Ordenar por salario mayor a menor
print(df.sort_values("salario", ascending=False))

# Agregar una columna nueva ? bono del 10% del salario
df["bono"] = df["salario"] * 0.10
print(df)

#Salario total con bono
df["salario total"] = df["salario"] + df["bono"]
print(df)