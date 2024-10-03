import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import json
import folium
from streamlit_folium import st_folium


st.set_page_config(
    page_title="Provincias",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable('opaque')

df_pen = pd.read_csv('penetracion.csv')
df_vmd = pd.read_csv('vmd.csv')
df_tri = pd.read_csv('trimestres.csv')
df_tec = pd.read_csv('tecnologias.csv')
df_con = pd.read_csv('conectividad.csv')

@st.cache_data
def load_geojson():
    with open('.\ProvinciasArgentina.geojson') as f:
        return json.load(f)

geojson_provincias = load_geojson()

def mapa_color(df, columna,):
    # Mapa centrado en Argentina
    m = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)

    # Crear un mapa choropleth
    folium.Choropleth(
        geo_data=geojson_provincias,  # GeoJSON con las provincias de Argentina
        name='choropleth',
        data=df,
        columns=['Provincia', columna],  # Las columnas del DataFrame: ubicación y valor
        key_on='feature.properties.nombre',  # Clave en el GeoJSON para coincidir con las provincias
        fill_color='YlGnBu',  # Paleta de colores
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Valor por Provincia'
    ).add_to(m)

    # Mostrar el mapa en Streamlit
    st_data = st_folium(m, width=700, height=500)

st.write(df_pen.head())
st.write(df_vmd.head())
st.write(df_tec.head())
st.write(df_con)
top_ten = df_con.sort_values(by='Población', ascending=False)
st.write(top_ten.head(10))