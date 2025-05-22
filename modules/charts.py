import streamlit as st
import plotly.express as px
import math

def show_charts(df):
    st.write("Finishing por jugador")
    club = st.selectbox("Selecciona un club", df["club"].unique(), key="bar")
    club_df = df[df["club"] == club]
    fig1 = px.bar(club_df, x="player", y="finishing", title=f"Capacidad de definición en {club}")
    st.plotly_chart(fig1, use_container_width=True)

    st.write("Relación entre dribbling y pase corto por país")
    countries = df["country"].unique()
    selected_country = st.selectbox("Selecciona un país", options=["Todos"] + list(countries), key="scatter_filter")

    if selected_country != "Todos":
        scatter_df = df[df["country"] == selected_country]
    else:
        scatter_df = df

    fig2 = px.scatter(scatter_df, x="dribbling", y="short_pass", color="country", hover_name="player",
        title="Relación entre regate y pase corto")
    st.plotly_chart(fig2, use_container_width=True)

    st.write("🌍 Distribución de nacionalidades")

    # Paso 1: Contar jugadores por país
    country_counts = df["country"].value_counts().reset_index()
    country_counts.columns = ["country", "count"]

    # Paso 2: Selector de modo
    mode = st.radio("¿Qué deseas visualizar?", ["Todos los países", "Ver por grupos de 10"], key="pie_view_mode")

    if mode == "Todos los países":
        # Mostrar todos
        fig = px.pie(country_counts, names="country", values="count", title="Distribución por país (todos)")
        st.plotly_chart(fig, use_container_width=True)

    else:
        # Paginación por grupos de 10
        group_size = 10
        total_groups = math.ceil(len(country_counts) / group_size)
        selected_group = st.slider("Selecciona un grupo", 1, total_groups, 1)

        start = (selected_group - 1) * group_size
        end = selected_group * group_size
        grouped = country_counts.iloc[start:end]

        fig = px.pie(grouped, names="country", values="count", title=f"Distribución por país - Grupo {selected_group}")
        st.plotly_chart(fig, use_container_width=True)