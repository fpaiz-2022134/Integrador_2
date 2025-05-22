import streamlit as st
import pandas as pd

def parse_value(values):
    try:
        cleaned = values.replace("$", "")  
        return float(cleaned)
    except:
        return None

def load_data():
    st.title("Cargar archivo")
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        if "value" in df.columns:
            df["value"] = df["value"].apply(parse_value)
        
        st.session_state["data"] = df
        st.sidebar.success("Archivo cargado correctamente!")