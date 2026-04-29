import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st - Es el objetivo principal de streamlit y se controye toda la interfaz visual

# --- CONFIGURACION DE LA PAGINA
st.set_páge_config(
    page_title = "Dashboard de Ventas",     #titulo en las pestana del navegador
    page_icon = "??",                       # icono en la pestana
    layout = "wide"                         # layout = "wide" usa todo el ancho de la pantalla
)

# ---- TITULO PRINCIPAL ----------
st.title("?? Dashboard de Ventas")      #titulo grande en la pagina
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
