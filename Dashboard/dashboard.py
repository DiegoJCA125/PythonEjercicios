# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st - Es el objetivo principal de streamlit y se controye toda la interfaz visual

# --- CONFIGURACION DE LA PAGINA
st.set_page_config(
    page_title = "Dashboard de Ventas",     #titulo en las pestana del navegador
    page_icon = "📊",                       # icono en la pestana
    layout = "wide"                         # layout = "wide" usa todo el ancho de la pantalla
)

# ---- TITULO PRINCIPAL ----------
st.title("📊 Dashboard de Ventas")      #titulo grande en la pagina
st.markdown("-------")                  # es una linea divisora

# ------- DATOS ---------
# Usamos los mismos datos del pipeline de ventas
productos = pd.DataFrame({
    "producto_id": [1, 2, 3, 4, 5],
    "nombre": ["Camisa", "Pantalon", "Zapatos", "Chaqueta", "Gorra"],
    "categoria": ["Ropa", "Ropa", "Calzado", "Ropa", "Accesorios"],
    "precio": [50000, 80000, 120000, 150000, 30000]
})

clientes = pd.DataFrame({
    "cliente_id": [1, 2, 3, 4, 5],
    "nombre": ["Diego", "Juliana", "David", "Yuls", "Carlos"],
    "ciudad": ["Medellin", "Bogota", "Cali", "Medellin", "Bogota"]
})

ventas = pd.DataFrame({
    "venta_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "cliente_id": [1, 2, 1, 3, 4, 2, 5, 1, 3, 4],
    "producto_id": [1, 2, 3, 1, 4, 5, 2, 4, 1, 3],
    "cantidad": [2, 1, 1, 3, 1, 2, 1, 2, 1, 1],
    "fecha": ["2024-01", "2024-01", "2024-02", "2024-02",
              "2024-03", "2024-03", "2024-03", "2024-04",
              "2024-04", "2024-04"]
})

# COMBINAR TABLAS
ventas_completas = pd.merge(ventas, productos, on = "producto_id")
ventas_completas = pd.merge(ventas_completas, clientes, on = "cliente_id")
ventas_completas = ventas_completas.rename(columns={
    "nombre_x": "producto",
    "nombre_y": "cliente"
    })
ventas_completas["total"] = ventas_completas["precio"] * ventas_completas["cantidad"]

# ---- METRICAS PRINCIPALES
# st.columns() - divide la pantalla en columnas
col1, col2, col3 = st.columns(3)

with col1:
    #st.metric() - muestra una metrica con ttulo y valor
    st.metric("💰 Total Ventas", f"${ventas_completas['total'].sum():,}")

with col2:
    mejor_cliente = ventas_completas.groupby("cliente")["total"].sum().idxmax()
    #idxmax() - devuelve el valor maximo 
    st.metric("💰 Mejor Cliente", mejor_cliente)

with col3:
    mejor_producto = ventas_completas.groupby("producto")["total"].sum().idxmax()
    st.metric("⭐ Producto Estrella", mejor_producto)

st.markdown("-----")

# --------- GRAFICAS ------------
# SE DIVIDE LA PANTALLA EN 2 COLUMNAS PARA LAS GRAFICAS
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Ventas por Mes")
    #st.subheader() - Titulo mediano en la pagina
    por_mes = ventas_completas.groupby("fecha")["total"].sum()
    fig, ax = plt.subplots()
    #fig, ax = plt.subplots() - crea una figura y in eje para la grafica
    por_mes.plot(kind = "line", ax = ax, marker= "o", color = "steelblue")
    ax.set_xlabel("mes")
    ax.set_ylabel("Total ventas")
    st.pyplot(fig)
    #st.pyplot - muestra la grafica de matplotlib en el dashboard

with col2:
    st.subheader("🏆 Top Productos")
    por_producto = ventas_completas.groupby("producto")["total"].sum()
    por_producto = por_producto.sort_values(ascending=False)
    fig2, ax2 = plt.subplots()
    por_producto.plot(kind = "bar", ax = ax2, color = "green")
    ax2.set_xlabel("Producto")
    ax2.set_ylabel("Total Vendido")
    ax2.tick_params(axis = "x", rotation = 45)
    st.pyplot(fig2)

st.markdown("------------")

#--------TABLA INTERACTIVA -------------
st.subheader("📋 Detalle de Ventas")
#st.dataframe() - muestra una tabla interactiva que se puede ordenar
st.dataframe(ventas_completas[["venta_id", "producto", "cliente", "cantidad", "precio", "total", "fecha"]])

# --------FILTRO INTERACTIVO ------------
st.subheader("🔍 Filtrar por Cliente")
#st.selectbox() - Crea un menu desplegable interactivo
cliente_seleccionado = st.selectbox(
    "SElecciona un cliente:",
    ventas_completas["cliente"].unique()
    #unique, devuelve los valores unicos de la columna
)

#FILTRA LA TABLA SEGUN EL CLIENTE SELECCIONADO
filtrado = ventas_completas[ventas_completas["cliente"] == cliente_seleccionado]
st.dataframe(filtrado[["producto", "cantidad", "precio", "total", "fecha"]])
st.metric("Total comprado por cliente", f"${filtrado['total'].sum():,}")

st.markdown("-----")

#FILTRAR POR FECHA ----
st.subheader("📅 Filtrar por Mes")
#st.multiselect() - permite seleccionar diferentes opciones
meses_seleccionados = st.multiselect(
    "Selecciona los meses:",
    options = ventas_completas["fecha"].unique(),
    default = ventas_completas["fecha"].unique()
    # default - Valoes seleccionados pordefecto (todos)
)

# FILTRAR POR LO MESES SELECCIONADOS
#isin() - verifica si el valor estan dentro de la lista
filtrado_fecha = ventas_completas[ventas_completas["fecha"].isin(meses_seleccionados)]

# MOSTRAR METRICAS DEL PERIODO SELECICONADO
col1, col2 = st.columns(2)
with col1:
    st.metric("💰 Total periodo", f"${filtrado_fecha['total'].sum():,}")
with col2:
    st.metric("🛒 Ventas realizadas", len(filtrado_fecha))

st.markdown("******")    

# ------------ RESUMEN EJECUTIVO --------------
st.subheader("📊 Resumen Ejecutivo")

col1, col2, col3 = st.columns(3)

with col1:
    # PRODUCTO MA VENDIDO EN EL PERIODO FILTRADO
    if len(filtrado_fecha) > 0:
        top_producto = filtrado_fecha.groupby("producto")["total"].sum().idxmax()
        st.metric("⭐ Top Producto", top_producto)

with col2:
    #CIUDAD CON MAS VENTAS
    if len(filtrado_fecha) > 0:
        top_ciudad = filtrado_fecha.groupby("ciudad")["total"].sum().idxmax()
        st.metric("🗺️ Top Ciudad", top_ciudad)

with col3:
    # PROMEDIO DE VENTA
    if len(filtrado_fecha) > 0:
        promedio = filtrado_fecha["total"].mean()
        st.metric("📈 Venta Promedio", f"${promedio:,.0f}")
        # --- :,.0f - formato de numero con comas y sin decimales

st.markdown("///////////////")

#--------- DESCARGAR REPORTE -------------------
st.subheader("💾 Descargar Reporte")

# CONVERNTIR DATAFRAME A EXCEL EN MEMORIA
# BytesIO() - CREA UN ARCHIVO EN MEMORIA SIN GUARDARLO EN DISCO
import io
buffer = io.BytesIO()
# io - Libreria para manejar archivos en memoria

with pd.ExcelWriter(buffer, engine = "openpyxl") as writer:
    filtrado_fecha[["venta_id", "producto", "cliente", "cantidad", "precio", "total", "fecha"]].to_excel(writer, sheet_name = "Ventas", index = False)
    filtrado_fecha.groupby("producto")["total"].sum()\
        .reset_index().to_excel(writer, sheet_name ="Por Prodcuto", index = False)
    filtrado_fecha.groupby("ciudad")["total"].sum()\
        .reset_index().to_excel(writer, sheet_name = "Por Ciudad", index = False)

#st.download_botton() - CREA UN BOTON DE DESCARGA EN EL DASHBOARD
st.download_button(
    label = "📥 Descargar Reporte Excel",
    data = buffer.getvalue(),
    # getvalue() - OBTIENE EL CONTENIDO DEL ARCHIVO EN MEMORIA
    file_name = "reporte_ventas.xlsx",
    mime = "application/vnd.ms-excel"
    #mime - TIPO DE ARCHIVO QUE SE DESCARGA
)
    