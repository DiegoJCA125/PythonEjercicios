import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

#  CREAR LOS DATOS
# TABLA PRODUCTOS
productos = pd.DataFrame({
    "producto_id": [1, 2, 3, 4, 5],
    "nombre": ["Camisa", "Pantalon", "Zapatos", "Chaqueta", "Gorra"],
    "categoria": ["Ropa", "Ropa", "Calzado", "Ropa", "Accesorios"],
    "precio": [50000, 80000, 120000, 150000, 30000]
})

# TABLA DE CLIENTE
clientes = pd.DataFrame({
    "cliente_id": [1, 2, 3, 4, 5],
    "nombre": ["Diego", "Juliana", "David", "Yuls", "Carlos"],
    "ciudad": ["Medellin", "Bogota", "Cali", "Medellin", "Bogota"]
})

# TABLA DE VENTAS
ventas = pd.DataFrame({
    "venta_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "cliente_id": [1, 2, 1, 3, 4, 2, 5, 1, 3, 4],
    "producto_id": [1, 2, 3, 1, 4, 5, 2, 4, 1, 3],
    "cantidad": [2, 1, 1, 3, 1, 2, 1, 2, 1, 1],
    "fecha": ["2024-01", "2024-01", "2024-02", "2024-02",
              "2024-03", "2024-03", "2024-03", "2024-04",
              "2024-04", "2024-04"]
})

print("Productos:")
print(productos)
print("---------------------------- \n")
print("Clientes:")
print(clientes)
print("-------------------- \n")
print("Ventas: ")
print(ventas)

# -------------------- PASO 2  - TRANSFORMAR Y CALCULAR ----------------------
# COMBINAR VENTAS CON PRODUCTOS USANDO merge() QUE ESIGUAL A UN JOIN
ventas_completas = pd.merge(ventas, productos, on = "producto_id")
# on = "producto_id" - COLUMNA EN COMUN EN UNA SOLA TABLA

ventas_completas = pd.merge(ventas_completas, clientes, on="cliente_id")
print("Columnas disponibles:")
print(list(ventas_completas.columns))
print("Ventas completas:")
print(ventas_completas[["venta_id", "nombre_x", "nombre_y", "cantidad", "precio", "fecha"]])
# nombre_x  - NOMBRE DEL PRODUCTO
# nombre_y - NOMBRE DEL CLIENTE
# PANDAS AGREGA _X Y _Y CUANDO DOS COLUMNAS TIENEN EL MISMO NOMBRE
print("-------------------------------- \n")

# CALCULAR EL TOTAL DE CADA VENTA
ventas_completas["total"] = ventas_completas["precio"] * ventas_completas["cantidad"]
print("Ventas con total calculado:")
print(ventas_completas[["nombre_x", "nombre_y", "cantidad", "precio", "total", "fecha"]])
print("---------------------------- \n")

# RENOMBRAR COLUMNAS PARA QUE SEAN MAS CLARAS - rename()  CAMBIA EL NOMBRE DE LAS COLUMNAS
ventas_completas = ventas_completas.rename(columns={
    "nombre_x" : "producto",
    "nombre_y" : "cliente"
})
print("Total de ventas", ventas_completas["total"].sum())


# ------------------------------ PASO 3  ANALISIS DE VENTAS ------------------------
# PRODUCTOS MAS VENDIDOS POR TOTAL DE INGRESOS
print("Porudctos mas vendidos:")
por_producto = ventas_completas.groupby("producto")["total"].sum()
# group by("producto") - agrupa por nombre del producto
# sum() SUMA EL TOTAL DE VENTAS DE CADA PRODUCTO
por_producto = por_producto.sort_values(ascending=False)
print(por_producto)
print("----------------------- \n")

# MEJOR CLIENTE POR TOTAL COMPRADO
print("Mejores clientes:")
por_cliente = ventas_completas.groupby("cliente")["total"].sum()
por_cliente = por_cliente.sort_values (ascending=False)
print(por_cliente)
print("--------------------------- \n")

# VENTAS POR MES
print("ventas por mes:")
por_mes = ventas_completas.groupby("fecha")["total"].sum()
print(por_mes)
print("---------------------------------------\n")

# --------------------------- GRAFICAS -------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# subplots() CREA MULTIPLES GRAFICAS EN UNA SOLA VENTANA
# 1, 3 - 1 FILA Y 3 COLUMNAS DE GRAFICAS
# figsize - tama?o total de la ventana

# GRAFICA 1 - VENTAS X PRODUCTO
por_producto.plot(kind = "bar", ax = axes[0],
                  title = " Ventas x Producto", color = "steelblue")
axes[0].set_xlabel("Producto")
axes[0].set_ylabel("Total vendido")
axes[0].tick_params(axis = "x", rotation = 45)
# tick_params() CONFIGURA LAS ETIQUETAS DEL EJE

# GRAFICA 2 - VENTAS X CLIENTE
por_cliente.plot(kind = "bar", ax = axes[1],
                 title = " Ventas x Cliente", color = "green")
axes[1].set_xlabel("cliente")
axes[1].set_ylabel("Total comprado")
axes[1].tick_params(axis = "x", rotation = 45)

# GRAFICA 3 VENTAS X MES
por_mes.plot (kind = "line", ax = axes[2],
              title = "Ventas por mes", color = "orange", marker = "o")
# kind = "line" - GRAFICA DE LINEA, IDEAL PARA MOSTRAR TENDENDICAS
# marker = "o" -  AGREGA UN PUNTO EN CADA DATO
axes[2].set_xlabel("Mes")
axes[2].set_ylabel("Total ventas")

plt.tight_layout()
ruta_grafica = os.path.join(os.path.dirname(__file__), "ventas_graficas.png")
plt.savefig(ruta_grafica)
plt.show()
print("Graficas guardadas correctamente!!")