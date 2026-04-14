import pandas as pd
import os

# EXTRAER DATOS
def extract(path):
    df = pd.read_csv(path)
    return df

# TRANSFORMAR LOS DATOS
def transform(df):
    df = df.dropna() # SE ELIMINAN VALORES NULOS
    #SE CRE UNA NUEVA COLUMNA LLAMADA "TOTAL" MULTIPLICANDO PRECIO * CANTIDAD
    df["total"] = df["precio"] * df["cantidad"]
    #SE FILTRA PRODUCTOS POR CATEGORIA "TECH"
    df = df[df["categoria"] == "Tech"]
    #AGRUPAMOS POR PRODUCTO Y SUMAMOS LAS VENTAS TOTALES
    df_grouped = df.groupby("producto")["total"].sum()
    #CONVERTIMOS EL RESULTADO EN DATAFREAME NORMAL
    df_grouped = df_grouped.reset_index()
    #ORDENAMOS DE MAYOR A MENOR SEGUN VENTAS
    df_grouped = df_grouped.sort_values(by="total", ascending=False)
    #LOS 3PRODUCTOS MAS VENDIDOS
    df_top = df_grouped.head(3)

    #RESULTADO FINAL
    return df_top

# GUARDAR LOS DATOS
def load(df, output_path):
    #SE GUARDA EN UN ARCHIVO .CSV /// index=False EVITA QUE SE GUARDE LA COLUMNA DE INDICE
    df.to_csv(output_path, index = False)

# PIPELINE COMPLETO------------------
def run_pipeline():
    # SE DEFINE LA RUTA DEL ARCHIVO DE ENTRADA (DATOS)
    input_path = "Pipeline/Pipeline_project/data/ventas.csv"
    # SE DEFINE LA RUTA EN LA QUE SE GUARDARA EL RESULTADO
    output_path = "Pipeline/Pipeline_project/data/output.csv"

    # FORMA CORRECTA QUE SIEMPRE FUNCIONARA SIN IMPORTAR DONDE SE EJECUTE EL SCRIPT
    #import os
    #base_dir = os.path.dirname(__file__)
    #input_path = os.path.join(base_dir, "data", "ventas.csv")
    #output_path = os.path.join(base_dir, "data", "output.csv")



    # EJECUTAMOS CADA FASE DEL PIPELINE
    data = extract(input_path)               # 1. EXTRAE LOSD DATOS
    transformed = transform(data)            # 2. TRANSFORMAR LOS DATOS
    print("Datos Transformados:")
    print(transformed.head())
    load(transformed, output_path)           # 3. GUARDA EL RESULTADO

# ---------------------- PUNTO DE ENTRADA

if __name__ == "__main__":
    run_pipeline()