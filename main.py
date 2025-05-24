import streamlit as st
from modules.file_loader import load_data, parse_value
from modules.indicators import show_indicators
from modules.tables import show_tables
from modules.charts import show_charts

st.set_page_config(
    page_title="Análisis de Estadísticas de Jugadores",
    layout="wide"
)

st.markdown("""
    <style>
        .main {padding-top: 2rem;}
        .stMetric {border-left: 4px solid #4CAF50; padding-left: 1rem;}
        h1 {color: #2e86c1;}
        h2 {color: #3498db;}
        .stSelectbox, .stSlider {margin-bottom: 1.5rem;}
        .stDataFrame {border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

if "data" not in st.session_state:
    st.session_state["data"] = None

# Sidebar mejorado
with st.sidebar:
    st.title("Menú de Navegación")
    st.markdown("---")
    section = st.radio(
        "Seleccione una sección:",
        ["Cargar Archivo", "Estadísticas e Indicadores", "Tablas", "Gráficas"],
        index=0
    )
    st.markdown("---")
    if st.session_state["data"] is not None:
        st.success("Datos cargados correctamente")
    else:
        st.warning("ℹPor favor cargue datos en la primera sección")

data = st.session_state["data"]

# Contenido principal
if section == "Cargar Archivo":
    load_data()

elif section == "Estadísticas e Indicadores":
    st.title("Estadísticas e Indicadores")
    if data is not None:
        show_indicators(data)
    else:
        st.error("Por favor, cargue un archivo CSV en la sección 'Cargar Archivo'.")

elif section == "Tablas":
    st.title("Tablas Interactivas")
    if data is not None:
        show_tables(data)
    else:
        st.error("Por favor, cargue un archivo CSV en la sección 'Cargar Archivo'.")

elif section == "Gráficas":
    st.title("Gráficas Interactivas")
    if data is not None:
        show_charts(data)
    else:
        st.error("Por favor, cargue un archivo CSV en la sección 'Cargar Archivo'.")