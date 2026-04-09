import pandas as pd
import os

#Lee el dataset
ruta = os.path.join(os.path.dirname(__file__), "players_22.csv")
df = pd.read_csv(ruta, low_memory=False)

#Explorar el archivo
print(f"Filas y columnas: {df.shape}")
print("----------------------------")
print(f"Primeras columnas disponibles:")
print(list(df.columns[:20]))
print("----------------------------------")
print("Primeras 5 filas")
print(df.head())

#Se selecciona las columnas que se necesitan
columnas = ["short_name", "age", "overall", "potential", "value_eur", "wage_eur", "club_name", "league_name", "player_positions"]

#Se crea uevo DataFrame con solo esas columnas 
df = df[columnas]

print("Dataset reducido:")
print(df.head(10))
print("---------------------")

print(f"Jugadores totales: {len(df)}")
#Len() cuenta cuantas filas tiene el frame

#Se verifica si hay valores vacion en las columnas
print("Valores vacios por columna:")
print(df.isnull().sum())
# isnull() - detecta las celdas vacias // sum() cuantas hay por columna
print("----------------------------------------")

#Los 10 mejores jugadores por Overall
print("Top 10 mejores jugadores:")
top10 = df.nlargest(10, "overall")
# nlargest() devuelve las filas con los valores mas grandes de la columna que se indique dentro de las ""
print(top10[["short_name", "age", "overall", "club_name"]])
print("-----------------------------------------")

#Promedio de overall por liga
print("Promedio de Overall por liga:")
por_liga = df.groupby("league_name")["overall"].mean() #mean calcula el promedio
por_liga = por_liga.sort_values(ascending=False).head(10)
print(por_liga)

import matplotlib.pyplot as plt

#Cuanto gana el jugador con mejor salario
mejor_pagado = df.nlargest(10, "wage_eur")
#nlargest() trae los 10 salarios mas altos
print("Tops 10 mejor pagados:")
print(mejor_pagado[["short_name", "club_name", "wage_eur"]])
print("---------------------------------------")

# Promedio de edad por liga
print("Promedio de edad por ligar:")
edad_liga = df.groupby("league_name")["age"].mean()
edad_liga = edad_liga.sort_values(ascending=False).head(10)
print(edad_liga)
print("-----------------------")

#Jugadores mayores e 35 a?os
veteranos = df[df["age"] >= 35]
#filtramos solo los jugadores con 35 o + a?os
print(f"Jugadores veteranos (+35 a?os): {len(veteranos)}")
print(veteranos[["short_name", "age", "club_name", "overall"]].head(10))
print("-----------------------------------")

#Jugadores menores de 20 a?os con overall mayor a 75
promesas = df[(df["age"] < 20) & (df["overall"] > 75)]
print(f"Promesas del futbol: {len(promesas)}")
print(promesas[["short_name", "age", "overall", "club_name"]].head(10))

import matplotlib.pyplot as plt
import os

#Grafica 1 top 10 jugadores mejor pagos
top_pagados = df.nlargest(10, "wage_eur")

top_pagados.plot(
    kind="barh",        # barras horizontales
    x="short_name",     # nombre de jugadores
    y="wage_eur",       #Salario
    title="Top 10 jugadores mejor pagados",
    color="steelblue",
    legend=False        # oculta la leyenda
)

plt.xlabel("Salario semanas (EUR)") #xlabel es la etiqueta del eje X
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "top_pagados.png"))
plt.show()

#Grafica 2 - distribucion de edades
df["age"].plot(
    kind="hist",        #Histograma, muestra distribucion
    bins=20,            #cantidad de barras en el histograma
    title="Distribucion de edades",
    color="green"
)
plt.xlabel("Edad")
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "edades.png"))
plt.show()

#Grafica 3 - Top 10 ligar por overall promedio

df.groupby("league_name")["overall"].mean()\
    .sort_values(ascending=False)\
    .head(10)\
    .plot(
        kind="bar",
        title="Top 10 ligar por overall promedio",
        color="orange"
    )

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "ligas.png"))
plt.show()

#exportae el excel completo con el analisis
ruta_excel = os.path.join(os.path.dirname(__file__), "reporte_futbol.xlsx")

with pd.ExcelWriter(ruta_excel, engine="openpyxl") as writer:

    #Hoja 1 - top 10 mejores jugadores
    df.nlargest(10, "overall")[["short_name", "age", "overall", "potential", "club_name", "wage_eur"]]\
    .to_excel(writer, sheet_name="Top 10 Jugadores", index=False)

    #Hoja 2 - Top 10 mejor pagados
    df.nlargest(10, "wage_eur")[["short_name", "age", "club_name", "wage_eur", "overall"]]\
    .to_excel(writer, sheet_name="Top 10 Mejor Pagados", index=False)

    #Hoja 3 - Menores de 20 a?os
    promesas = df[(df["age"] < 20) & (df["overall"] > 75)]
    promesas[["short_name", "age", "overall", "potential", "club_name"]]\
    .to_excel(writer, sheet_name="Promesas", index=False)

    #Hoja 4 - Promedio de overall por liga
    df.groupby("league_name")["overall"].mean()\
    .sort_values(ascending=False)\
    .reset_index()\
    .to_excel(writer, sheet_name="Ligas", index=False)

print("Reporte de Excel creado correctamente!!")