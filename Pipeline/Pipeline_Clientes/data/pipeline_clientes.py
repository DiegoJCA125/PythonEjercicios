import pandas as pd
import os

def extract(folder_path):
    all_data = []

    for file in os.listdir(folder_path):
        # SOLO ARCHIVOS DE CLIENTES
        if file.endswith(".csv") and file.startswith("clientes"):
            full_path = os.path.join(folder_path, file)

            if os.path.getsize(full_path) > 0:
                print(f"Leyendo archivo: {file}")

                df = pd.read_csv(full_path)
                all_data.append(df)

    if len(all_data) == 0:
        print("No hay datos")
        return pd.DataFrame()
    
    return pd.concat(all_data, ignore_index=True)

def transform(df):
    if df.empty:
        return df

    #LIMPIEZA 
    df = df.dropna()
    df["fecha"] = pd.to_datetime(df["fecha"])

    #TOTAL
    df["total"] = df["precio"] * df["cantidad"]

    #AGRUPAR POR CLIENTE
    df_grouped = df.groupby(["cliente", "ciudad"]).agg({
        "total": "sum",        #CUANTO SE GASTO
        "cantidad": "sum",      # CUANTOS PRODUCTOS COMPRO      
        "id": "count"           # NUMERO DE COMPRAS
    })
#RENOMBRAR
    df_grouped = df_grouped.rename(columns={
        "id": "num_compras"
})
    
    # TICKET PROMEDIO
    df_grouped["ticket_promedio"] = df_grouped["total"] / df_grouped["num_compras"]
    df_grouped["ticket_promedio"] = df_grouped["ticket_promedio"].round(2)

    #RANKING PRIMERO (SOBRE TODOS LOS DATOS)
    df_grouped["rank"] = df_grouped.groupby("ciudad")["total"].rank(method="first", ascending=False)

    # ORDENAR ( MEJORES CLIENTES)
    df_grouped = df_grouped.sort_values(by=["ciudad", "rank"])

    # TOP CLIENTE POR CIUDAD
    df_grouped["rank"] = df_grouped["rank"].astype(int)

    #TOTAL POR CIUDAD
    df_grouped["total_ciudad"] = df_grouped.groupby("ciudad")["total"].transform("sum")

    # PORCENTAJE DE PARTICIPACION
    df_grouped["participacion"] = (df_grouped["total"] / df_grouped["total_ciudad"]) *100
    df_grouped["participacion"] = df_grouped["participacion"].round(2)
    df_grouped["participacion_label"] = df_grouped["participacion"].astype(str) + "%"

    # RECUPERAR COLUMNA
    df_grouped = df_grouped.reset_index()

    # SEGMENTAR CLIENTES
    def clasificar_cliente(total):
        if total > 900:
            return "VIP"
        elif total > 500:
            return "Medio"
        else:
            return "Bajo"

    df_grouped["segmento"] = df_grouped["total"].apply(clasificar_cliente)
    return df_grouped

def load(df, output_path):

    if df.empty:
        print("No se guarda el archivo")
        return
    df.to_csv(output_path, index=False)
    print(f"\n Archivo guardado en: {output_path} \n")

def run_pipeline():

    base_dir = os.path.dirname(__file__)
    input_folder = os.path.join(base_dir, "data")
    output_path = os.path.join(base_dir, "data", "output_clientes.csv")

    data = extract(input_folder)
    transformed = transform(data)

    print("\n Top clientes: \n")
    print(transformed)

    load(transformed, output_path)

if __name__ == "__main__":
    run_pipeline()