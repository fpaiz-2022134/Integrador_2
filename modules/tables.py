import streamlit as st

def show_tables(df):
    clubs = df["club"].unique()
    selected_club = st.selectbox("Selecciona un club", clubs)
    st.write("Jugadores del club seleccionado")
    st.dataframe(df[df["club"] == selected_club])

    st.write("Mejores pasadores filtrados por edad máxima")
    max_age = st.slider("Edad máxima del jugador", min_value=int(df["age"].min()), max_value=int(df["age"].max()), value=30)
    filtered_by_age = df[df["age"] <= max_age]
    top_passers = filtered_by_age.sort_values(by="short_pass", ascending=False)
    st.dataframe(top_passers[["player", "age", "club", "short_pass", "vision"]])

    st.write("Especialistas en disparos lejanos por país")
    countries = df["country"].unique()
    selected_country = st.selectbox("Selecciona un país", countries, key="country_filter")
    filtered_by_country = df[df["country"] == selected_country]
    top_longshots = filtered_by_country.sort_values(by="long_shots", ascending=False)
    st.dataframe(top_longshots[["player", "country", "club", "shot_power", "long_shots"]])
