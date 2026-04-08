import os
ruta = os.path.join(os.path.dirname(__file__), "nombre_archivo.csv")

import pandas as pd

#Tabla 1 - empleados
empleados = pd.DataFrame({
    "nombre": ["Diego", "Juliana", "David", "Yuls", "Carlos"],
    "edad": [28, 28, 30, 31, 25],
    "departamento": ["Ventas", "Software", "Software", "RRHH", "Ventas"]
})

#Tabla 2 - departamentos
departamentos = pd.DataFrame({
    "departamento": ["Ventas", "Software", "Contabilidad"],
    "presupuesto": [50000, 100000, 125000],
    "jefe": ["Ana", "Diego", "Juliana"]
})

print("Tabla empleados:")
print(empleados)
print("----")
print("Tabla departamentos:")
print(departamentos)

#Combinacion completa - Coinciden en ambas tablas
union = pd.merge(empleados, departamentos, on ="departamento", how="inner")
print("Inner join - Solo las coincidencias:")
print(union)
print("----------------")

#Todos los empleados asi no tengan departamentos en la tabla 2
union_left = pd.merge(empleados, departamentos, on="departamento", how="left")
print("Left join - Todos los empleados:")
print(union_left)
print("---------------------------------")

#Todos los departamento asi no tengan empleados
union_right = pd.merge(empleados, departamentos, on="departamento", how="right")
print("Right join - Todos los departamentos")
print(union_right)

import matplotlib.pyplot as plt

#Grafica presupuesto x departamento
union_right.groupby("departamento")["presupuesto"].mean().plot(
    kind="bar",
    title="Presupuesto por departamento",
    color="steelblue"
)
plt.ylabel("presupuesto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "presupuesto.png"))
plt.show()