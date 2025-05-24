import streamlit as st

def show_indicators(df):
    st.subheader("Resumen Estadístico")
    st.dataframe(df.describe())
    
    filas, columnas = df.shape

    st.write(f"Número de filas: {filas}")
    st.write(f"Número de columnas: {columnas}")
    

    st.subheader("Indicadores Clave")
    col1, col2 = st.columns(2)

    with col1:import streamlit as st

def show_indicators(df):
    st.header("Resumen Estadístico")
    
    with st.expander("Ver estadísticas descriptivas completas"):
        st.dataframe(df.describe().style.background_gradient(cmap='Blues'))
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Número de filas", df.shape[0])
    with col2:
        st.metric("Número de columnas", df.shape[1])
    
    st.markdown("---")
    
    st.subheader("Indicadores Clave de Rendimiento")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Promedio de Finishing", 
            round(df["finishing"].mean(), 2),
            help="Capacidad promedio de definición de los jugadores"
        )
        st.caption(
            "Capacidad promedio de definición de los jugadores"
        )
        st.caption(
            "Útil para evaluar si los jugadores tienen buen rendimiento ofensivo."
        )
        st.metric(
            "Poder de Disparo Promedio", 
            round(df["shot_power"].mean(), 2),
            help="Fuerza promedio en los disparos"
        )
        st.caption(
            "Fuerza promedio en los disparos"
        )
        st.caption(
            "Sirve para analizar si el equipo es fuerte en ataque a distancia."
        )
        st.metric(
            "Visión Promedio", 
            round(df["vision"].mean(), 2),
            help="Capacidad promedio de visión de juego"
        )
        st.caption(
            "Evalúa qué tan creativos y tácticos son los jugadores."
        )
        st.caption(
            "Refleja inteligencia de juego, importante en creación ofensiva."
        )
    with col2:
        best_long_shots = df.loc[df["long_shots"].idxmax()]
        st.metric(
            "Especialista en Disparos Lejanos", 
            f"{best_long_shots['player']} ({best_long_shots['club']})",
            int(best_long_shots["long_shots"]),
            help=f"Puntuación: {best_long_shots['long_shots']}"
        )
        st.caption(
            "Jugador con mayor puntería desde lejos."
        )
        st.caption(
            "Revela talentos destacados en remates de media distancia."
        )
        best_passer = df.loc[df["short_pass"].idxmax()]
        st.metric(
            "Mejor Pasador Corto", 
            f"{best_passer['player']} ({best_passer['club']})",
            int(best_passer["short_pass"]),
            help=f"Puntuación: {best_passer['short_pass']}"
        )

        st.caption(
            "Jugador con mayor precisión en pases cortos."
        )
        st.caption(
            "Identifica al jugador más confiable en la construcción de juego."
        )
        best_dribbler = df.loc[df["dribbling"].idxmax()]
        st.metric(
            "Mejor Regateador", 
            f"{best_dribbler['player']} ({best_dribbler['club']})",
            help=f"Puntuación: {best_dribbler['dribbling']}"
        )
        
        st.caption(
            "Jugador con mejor habilidad para eludir rivales."
        )
        st.caption(
            "Indica al jugador más habilidoso técnicamente."
        )