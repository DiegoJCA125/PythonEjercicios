import pandas as pd
import os

def extract(path):
    df = pd.read_csv(path)
    return df

def transform(df):
    df = df.dropna()

    #CONVERTIR LA COLUMNA FECHA A TIPO DATETIME
    df["fecha"] = pd.to_datetime(df["fecha"])

    #CREAR COLUMNA TOTAL (PRECIO * CANTIDAD)
    df["total"] = df["precio"] * df["cantidad"]

    #FILTRAR SOLO CATEGORIA TECH
    df = df[df["categoria"] == "Tech"]

    #AGRUPAR POR CIUDAD
    df_grouped = df.groupby("ciudad").agg({
        "total":"sum",          # suma de ventas
        "cantidad": "sum"       # suma de productos vendidos
    })

    # CIUDAD CON VENTAS MAYORES A 200
    df_grouped["promedio"] =  df_grouped["total"] / df_grouped["cantidad"]
    df_grouped["promedio"] = df_grouped["promedio"].round(2)
    
    #FILTRAR CIUDAD CON VENTAS A 200 
    df_grouped = df_grouped[df_grouped["total"] > 200]
    df_grouped = df_grouped.sort_values(by="total", ascending=False)
    df_grouped = df_grouped.head(3)

    #RESETEAR INDICE
    df_grouped = df_grouped.reset_index()

    # ORDENAR POR VENTAS
    df_grouped = df_grouped.sort_values(by="total", ascending=False)
    
    return df_grouped

def load(df, output_path):
    # GUARDA EL RESULTADO
    df.to_csv(output_path, index=False)

def run_pipeline():
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "data", "ventas2.csv")
    output_path = os.path.join(base_dir, "data", "output2.csv")

    data = extract(input_path)
    transformed = transform(data)
    print("Pipeline Ejecutandose...")  
    #debug (VER RESULTADO)
    print(transformed)
    load(transformed, output_path)
    

if __name__ == "__main__":
    run_pipeline()
