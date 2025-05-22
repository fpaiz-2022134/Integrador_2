import streamlit as st
from modules.file_loader import load_data, parse_value
from modules.indicators import show_indicators
from modules.tables import show_tables
from modules.charts import show_charts

st.set_page_config(page_title="Análisis de Estadísticas de Jugadores", layout="wide")

if "data" not in st.session_state:
    st.session_state["data"] = None

st.sidebar.title("Menú")
section = st.sidebar.radio("Ir a:", ["Cargar Archivo", "Estadísticas e Indicadores", "Tablas", "Gráficas"])



data = st.session_state["data"]

if section == "Cargar Archivo":
    
    load_data()

elif section == "Estadísticas e Indicadores":
    st.title(" Estadísticas e Indicadores")
    if data is not None:
        show_indicators(data)
    else:
        st.warning("Por favor, cargue un archivo CSV en la sección 'Cargar Archivo'.")

elif section == "Tablas":
    st.title("Tablas Interactivas")
    if data is not None:
        show_tables(data)
    else:
        st.warning("Por favor, cargue un archivo CSV en la sección 'Cargar Archivo'.")

elif section == "Gráficas":
    st.title(" Gráficas Interactivas")
    if data is not None:
        show_charts(data)
    else:
        st.warning("Por favor, cargue un archivo CSV en la sección 'Cargar Archivo'.")



