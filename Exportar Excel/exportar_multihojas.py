import pandas as pd
import os

empleados = pd.DataFrame({
    "nombre": ["Diego", "Juliana", "David", "Yuls", "Juana"],
    "edad": [28, 29, 30, 31, 25],
    "salario": [1000, 2000, 1500, 800, 2500],
    "ciudad": ["Medellin", "Bogota", "Cali", "Medellin", "Bogota"]
})

#Resumen x ciudad
resumen = empleados.groupby("ciudad")["salario"].agg(
    total="sum",
    promedio="mean",
    personas="count"
).reset_index()

#Estadisticas generales 
estadisticas = empleados[["edad", "salario"]].describe().reset_index()

#Guarda las 3 tablas en hojas diferentes
ruta = os.path.join(os.path.dirname(__file__), "reporte_completo.xlsx")

with pd.ExcelWriter(ruta, engine="openpyxl") as writer:
    empleados.to_excel(writer, sheet_name="Empleados", index=False)
    resumen.to_excel(writer, sheet_name="Resumen Ciudad", index=False)
    estadisticas.to_excel(writer, sheet_name="Estadistica", index=False)

    print("Reporte Excel con 3 hojas creados correctamente")