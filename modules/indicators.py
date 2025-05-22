import streamlit as st

def show_indicators(df):
    st.subheader("Resumen Estadístico")
    st.dataframe(df.describe())
    
    filas, columnas = df.shape

    st.write(f"Número de filas: {filas}")
    st.write(f"Número de columnas: {columnas}")
    
    st.write("Tipos de datos por columna:")
    st.write(df.dtypes)

    st.subheader("Indicadores Clave")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Promedio de Definición / Finishing por jugador", round(df["finishing"].mean(), 2))
        st.metric("Promedio de Shot Power (Poder de disparo)", round(df["shot_power"].mean(), 2))
        st.metric("Promedio de vision", round(df["vision"].mean(), 2))

    with col2:
        best_long_shots = df.loc[df["long_shots"].idxmax()]
        st.metric("Especialista en disparos lejanos", best_long_shots["player"], int(best_long_shots["long_shots"]))

        best_passer = df.loc[df["short_pass"].idxmax()]
        st.metric("Mejor pasador corto", best_passer["player"], int(best_passer["short_pass"]))

        best_dribbler = df.loc[df["dribbling"].idxmax()]
        st.metric("Mejor regateador", best_dribbler["player"])
