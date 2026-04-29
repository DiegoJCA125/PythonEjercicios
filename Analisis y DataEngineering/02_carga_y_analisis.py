import pandas as pd

# LA FUNCION READ_CSV es la puerta para la mayoria de datos
try:
    df = pd.read_csv('ventas_mensuales.csv')
    print("Archivo cargado exitosamente. \n")
except FileNotFoundError:
    print("Error: No se encontro el archivo CSV. asegurate de que esté en la misma carpeta")

#   SE CONOCER LOS DATOS
print("---------- Primeras 3 filas del dataset --------")
print(df.head(3))

print("\n ----- Informacion tecnica de las columnas: -------")
print(df.info())
# info() Nos dice si hay nulos y que tipo de dato tiene cada columna


