import streamlit as st
import plotly.express as px
import math

def show_charts(df):
    st.header("Visualización de Datos de Jugadores")
    
    # Sección 1 de gráficas god
    with st.container():
        st.subheader("Finishing por Jugador")
        club = st.selectbox(
            "Selecciona un club:",
            df["club"].unique(),
            key="bar",
            help="Seleccione un club para ver las estadísticas de finishing de sus jugadores"
        )
        club_df = df[df["club"] == club]
        fig1 = px.bar(
            club_df, 
            x="player", 
            y="finishing", 
            title=f"Capacidad de definición en {club}",
            color="finishing",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("---")
    
    # Sección 2 de gráficas god
    with st.container():
        st.subheader("Relación entre el Dribbling y el Pase Corto")
        countries = df["country"].unique()
        selected_country = st.selectbox(
            "Filtrar por país:",
            options=["Todos"] + list(countries),
            key="scatter_filter",
            index=0
        )

        if selected_country != "Todos":
            scatter_df = df[df["country"] == selected_country]
        else:
            scatter_df = df

        fig2 = px.scatter(
            scatter_df, 
            x="dribbling", 
            y="short_pass", 
            color="country", 
            hover_name="player",
            title="Relación entre regate y pase corto",
            size="age",
            size_max=15
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Sección 3 de gráficas god
    with st.container():
        st.subheader("Distribución de las Nacionalidades")
        country_counts = df["country"].value_counts().reset_index()
        country_counts.columns = ["country", "count"]

        mode = st.radio(
            "Modo de visualización:",
            ["Todos los países", "Ver por grupos de 10"], 
            key="pie_view_mode",
            horizontal=True
        )

        if mode == "Todos los países":
            fig = px.pie(
                country_counts, 
                names="country", 
                values="count", 
                title="Distribución por país (todos)",
                hole=0.3
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            group_size = 10
            total_groups = math.ceil(len(country_counts) / group_size)
            selected_group = st.slider(
                "Grupo a visualizar:", 
                1, total_groups, 1,
                help=f"Cada grupo muestra {group_size} países"
            )

            start = (selected_group - 1) * group_size
            end = selected_group * group_size
            grouped = country_counts.iloc[start:end]

            fig = px.pie(
                grouped, 
                names="country", 
                values="count", 
                title=f"Distribución por país - Grupo {selected_group}",
                hole=0.3
            )
            st.plotly_chart(fig, use_container_width=True)