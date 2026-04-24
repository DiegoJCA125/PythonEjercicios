import pandas as pd

# CONFIGURAMOS EL ESCENARIO
datos = {
    'producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Silla Ergonomica', 'Escritorio'],
    'categoria': ['Electronica', 'Accesorios', 'Electronica', 'Accesorios', 'Muebles', 'Muebles'],
    'precio': [1200, 25, 300, 80, 250, 450],
    'cantidad': [5, 10, 4, 0, 3, 2]
}

df = pd.DataFrame(datos)

# COLUMNA CALCULADA
# SE CALCULARA EL VALOR DEL STOCK POR CADA FILA
df['stock_valor'] = df['precio'] * df['cantidad']

# FILTRADO
# Se quiere filtrar solo lo que es "Electronica", se crea un filtro
solo_electronica = df[df['categoria'] == 'Electronica']

# AGREGACION
# Sumamos el valor de stock pero solo de ese filtro
total_electronica = solo_electronica['stock_valor'].sum()

print("------- SUB- TABLA DE ELECTRONICA------")
print(solo_electronica)
print(f"\nInversion total en Electronica: ${total_electronica}")

# AGRUPACION TOTAL
#SE QUIERE VER EL TOTAL DE TODAS LAS CATEGORIA
# SE UTILIZA GROUPBY CORREPSONDIENTE DE PANDAS
resumen_categorias = df.groupby('categoria')['stock_valor'].sum().reset_index()

print("\n ----------- RESUMEN GENERAL POR CATEGORIAS ----------")
print(resumen_categorias)