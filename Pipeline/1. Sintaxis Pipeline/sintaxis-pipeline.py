# INSTALAR LAS DEPENDIENTES EN CADA ENTORNO
# pip install pandas sqlalchemy apache-airflow

import pandas as pd

# EXTREAR DATOS DEL CSV
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Extracion de datos exitosa!!")
        return data
    except Exception as e:
        print(f"Error al extraer datos: {e}")
        return None
    
#EJEMPLO DE USO
file_path = 'productos.csv'
raw_data = extract_data(file_path)

def transform_data(data):
    # ELIMIANR FILAS CON VALORES NULOS
    data.dropna(inplace = True)

    # NORMALIZAR COLUMNAS DE TEXTO A MINUSCULAS
    data['nombre_producto'] = data['nombre_producto'].str.lower()

    # CONVERTIR EL PRECIO A UN FORMATO NUMERICO
    data['precio'] = pd.to_numeric(data['precio'], errors = 'coerce')

    # ASEGURAR QUE NO HAYA PRECIOS NEGATIVOS
    data = data[data['precio'] >= 0]

    print("Transformacion de datos exitosa!")

# TRANSFORMAR LOS DATOS EN BRUTO
cleaned_data = transform_data(raw_data)

# ---------------------- CARGAR LOS DATOS A UNA BASE DE DATOS ------------------------

from sqlalchemy import create_engine

# CONECTAR A LA BASE DE DATOS MYSQL
def get_db_connection():
    try:
        engine = create_engine("mysql+mysqlconnector://usuario:contraseña@localhost/nombre_bd")
        print("Conexion a la base de datos exitosa!")
        return engine
    except Exception as e:
        print(f"Error en la conexion a la base de datos_ {e}")
        return None
    
# INSERTAR DATOS EN MYSQL
def load_data (data, engine):
    try:
        data.to_sql('productos', con = engine, if_exists = 'replace', index = False)
        print("Datos cargados exitosamente!")
    except Exception as e:
        print(f"Erro al cargar los datos: {e}")

# EJEMPLO DE USO
engine = get_db_connection()
if engine:
    load_data(cleaned_data, engine)

# Nota de Seguridad: Usa variables de entorno o un gestor de contraseñas para las credenciales en entornos de producción.

# ------- AUTOMATIZACION DEL PROCEDO ETL CON AIRFLOW
# DEFINIR DAG
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
dag = DAG(
    'pipeline_etl',
    description = 'Pipeline ETL usando Python y Airflow',
    schedule_interval = '@daily',
    start_date = datetime(2023, 1, 1),
    catchup = False,
)

# TAREAS EN AIRFLOW
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    op_kwargs={'file_path': 'productos.csv'},
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    op_kwargs={'data': raw_data},
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    op_kwargs={'data': cleaned_data, 'engine': engine},
    dag=dag,
)

# Dependencias entre tareas
extract_task >> transform_task >> load_task