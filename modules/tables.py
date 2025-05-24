import streamlit as st
import pandas as pd

def show_tables(df):
    st.header("Tablas de Jugadores")
    
    with st.container():
        st.subheader("Jugadores por Club")
        clubs = df["club"].unique()
        selected_club = st.selectbox(
            "Seleccione un club:", 
            clubs,
            key="club_selector",
            help="Filtre los jugadores por club"
        )
        st.dataframe(
            df[df["club"] == selected_club].style.background_gradient(cmap='Greens'),
            height=400
        )
    
    st.markdown("---")
    
    with st.container():
        st.subheader("Mejores Pasadores por Edad")
        max_age = st.slider(
            "Edad máxima:", 
            min_value=int(df["age"].min()), 
            max_value=int(df["age"].max()), 
            value=30,
            help="Filtre los jugadores por edad máxima"
        )
        filtered_by_age = df[df["age"] <= max_age]
        top_passers = filtered_by_age.sort_values(by="short_pass", ascending=False)
        st.dataframe(
            top_passers[["player", "age", "club", "short_pass", "vision"]]
            .style.highlight_max(color='green', axis=0)
        )
    
    st.markdown("---")
    
    with st.container():
        st.subheader("Especialistas en los Disparos Lejanos")
        countries = df["country"].unique()
        selected_country = st.selectbox(
            "Filtrar por país:", 
            countries, 
            key="country_filter",
            help="Filtre los jugadores por nacionalidad"
        )
        filtered_by_country = df[df["country"] == selected_country]
        top_longshots = filtered_by_country.sort_values(by="long_shots", ascending=False)
        st.dataframe(
            top_longshots[["player", "country", "club", "shot_power", "long_shots"]]
            .style.highlight_max(color='purple', axis=0)
        )