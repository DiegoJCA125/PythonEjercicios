import pandas as pd

# 1. DATOSCRUDOS
# Se simula quye se reciben una lidta de diccionario (comun en api o json)

datos_sucios = [
    {"producto": "Laptop", "precio": 1200, "cantidad": 5},
    {"producto": "Mouse", "precio": 25, "cantidad": 10},
    {"producto": "Teclado", "precio": 80, "cantidad": None}, # Cuidado aqui
    {"producto": "Monitor", "precio": -100, "cantidad": 2},   # precio negativo!
]

# 2. CARGAR LOS DATOS
# Se convierte la lista en un dataframe de pandas
df = pd.DataFrame(datos_sucios)

# LIMPIEZA DE DATOS
# 3.1 manejo de valores nulos
# Si sedesconoce la cantidad de teclados que hay, por seguridad se pondra 0 para que no rimpa los calculos a futuro
df['cantidad'] = df['cantidad'].fillna(0)

# 3.2 CORRECION DE ERRORES LOGICOS
# un precio no puede ser negativo, se aplica la regla de si el precio es menor a 0, se convierte a valor absoluto, positivo
df['precio'] = df['precio'].abs()

# ANALISIS DE LOS DATOS ---- GENERACION DE VALOR
# 3.3 CREACION DE COLUMNA CALCULADA
df['valor_total_stock'] = df['precio'] * df['cantidad']

#4 RESULTADOOOO
print("Tabla Final Limpia:")
print(df)

# RESUMEN ESTADISTICO SIMPLE
total_tienda = df['valor_total_stock'].sum()
print(f"\nEl valor total de toda la tienda es: ${total_tienda}")