import pandas as pd
# Se crea un set de datos "sucios" para el ejemplo

data = {
    'fecha': ['2023-01-01', '2023-0102', 'None', '2023-01-04'],
    'ventas': [100, 150, 200, 150],
    'producto': ['A', 'B', 'A', 'B']
}
df = pd.DataFrame(data)
#Paso 1: Identificar y mejorar los valores nulos
#Se rellena la fecha faltante o eliminamos la fila segun la estrategia necesaria
df['fecha'] = df['fecha'].fillna('2023-01-03')

#Paso 2: Eliminar duplicados
df = df.drop_duplicates()

# Paso 3: Conversion de tipos
# Se asegura que la columna 'fecha' sea tipo datetime para poder hacer calculos temporales
df['fecha']=pd.to_datetime(df['fecha'])

print(df)

