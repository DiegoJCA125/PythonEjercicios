import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ("empleados.csv")

#Grafica de barras vertical / salario x persona

df.plot(kind="bar", x="nombre", y="salario", title="Salario por Persona")
plt.tight_layout()
plt.show()

#Grafica de barras horizontal / salario x persona
df.plot(kind="barh", x="nombre", y="salario", title="Salario por persona")
plt.tight_layout()
plt.show()

#Grafica de dispersion - Edad vs Salario
df.plot(kind="scatter", x="edad", y="salario", title="Edad vs Salario")
plt.tight_layout()
plt.show()

#Grafica torta - Persona x ciudad
df["ciudad"].value_counts().plot(kind="pie", title="Personas por Ciudad", autopct="%1.1f%%")
plt.tight_layout()
plt.show()