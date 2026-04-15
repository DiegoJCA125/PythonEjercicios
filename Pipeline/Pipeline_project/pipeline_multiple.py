import pandas as pd
import os

def extract(folder_path):
    #LISTA PARA GUARDAR TODOS LOS DATAFRAMES
    all_data = []

    #RECORRE TODOSL OS ARCGIVOS EN LA CARPETA
    for file in os.listdir(folder_path):
        #VALIDA QUE SEA CSV y que sean de ventas, no los output
        if file.endswith(".csv") and file.startswith("ventas"):
            # CONTRUIR RUTA COMPLETA
            full_path = os.path.join(folder_path, file)

            # VALIDA QUE NO ESTE VACIO
            if os.path.getsize(full_path) > 0:
                print(f"Leyendo archivo: {file} \n")
                #LEER ARCHIVO
                df = pd.read_csv(full_path)
                # SE VALIDA QUE TENGA LAS COLUMNAS NECESARIAS PARA PROGRESAR
                columnas_necesarias = ["fecha", "ciudad", "categoria", "precio", "cantidad"]

                if all(col in df.columns for col in columnas_necesarias):
                    all_data.append(df)
                else:
                    print(f"Archivo ignorado por estructura incorrecta: {file}")
            else:
                print(f"Archivo vacio ignorado: {file}")

    # VALIDAR QUE HAYA DATOS ANTES DE CONCATENAR
    if len(all_data) == 0:
        print("No hay datos validos para procesar")
        return pd.DataFrame()

    # UNIR TODOS LOS DATAFRAMES EN UN SOLO
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df

def transform(df):
    # EVITAR ERROR SI EL DF ESTA VACIO
    if df.empty:
        print("DataFrame vacio en transform")
        return df
    
    df = df.dropna()
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["total"] = df["precio"] * df["cantidad"]
    df = df[df["categoria"] == "Tech"]

    df_grouped = df.groupby("ciudad").agg({
        "total": "sum",
        "cantidad": "sum"
    })

    df_grouped["promedio"] = df_grouped["total"] / df_grouped["cantidad"]
    df_grouped["promedio"] = df_grouped["promedio"].round(2)

    df_grouped = df_grouped[df_grouped["total"] >200]
    df_grouped = df_grouped.sort_values(by="total", ascending=False)
    df_grouped = df_grouped.head(2)

    df_grouped = df_grouped.reset_index()

    return df_grouped

def load(df, output_path):
    #EVITAR GUARDAR ARCHIVO VACIO
    if df.empty:
        print("No se guarda archivo porque esta vacio")
        return
    df.to_csv(output_path, index=False)
    print(f"Archivo guardado en: {output_path}")

def run_pipeline():
    base_dir = os.path.dirname(__file__)

    #AHORA ES CARPETA, NO UN ARCHIVO
    input_folder = os.path.join(base_dir, "data")
    
    #CAMBIO NOMBRE PARA EVITAR MEZCLA CON OTROS OUTPUTS
    output_path = os.path.join(base_dir, "data", "output_batch_final.csv")

    output_path = os.path.join(base_dir, "data", "out_batch.csv")

    data = extract(input_folder)
    transformed = transform(data)

    print("Pipeline batch ejecutandose...\n")
    print(transformed)

    load(transformed, output_path)

# OBLIGATORIO IR EN TODOS LOS CODIGOS PARA QUE SE EJECUTE
if __name__ == "__main__":
    run_pipeline()
