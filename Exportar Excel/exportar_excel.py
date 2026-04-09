#Antes de exportar se debe de instalar en el bash la libreria
# py -m pip instal openpyxl 
# Libreria de pandas para escribir archivos

import pandas as pd
import os

empleados = pd.DataFrame({
    "nombre": ["Diego", "Juliana", "David", "Yuls", "Juana"],
    "edad": [28, 29, 30, 31, 25],
    "salario": [1000, 2000, 1500, 800, 2500],
    "ciudad": ["Medellin", "Bogota", "Cali", "Medellin", "Bogota"]
})

#Guarda el excel
ruta = os.path.join(os.path.dirname(__file__), "empleados.xlsx")
empleados.to_excel(ruta, index=False, sheet_name="Empleados")
print("Archivo de Excel creado correctamente")