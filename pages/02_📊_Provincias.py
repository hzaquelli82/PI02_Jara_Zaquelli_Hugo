import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import json
import folium
import os
from streamlit_folium import st_folium


st.set_page_config(
    page_title="Provincias",
    layout="wide",
    initial_sidebar_state="expanded")

alt.theme.enable('opaque')

df_pen = pd.read_csv('penetracion.csv')
df_vmd = pd.read_csv('vmd.csv')
df_tri = pd.read_csv('trimestres.csv')
df_tec = pd.read_csv('tecnologias.csv')
df_con = pd.read_csv('conectividad.csv')


@st.cache_data
def load_geojson():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    geojson_path = os.path.join(script_dir, "..", "ProvinciasArgentina.geojson")
    try:
        with open(geojson_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Archivo GeoJSON no encontrado en la ruta esperada: {geojson_path}. "
                 "Asegúrate de que 'ProvinciasArgentina.geojson' se encuentre en el directorio raíz de tu proyecto.")
        st.stop() 
    except json.JSONDecodeError:
        st.error(f"Error al decodificar el archivo GeoJSON en: {geojson_path}. Verifica el formato del archivo.")
        st.stop()

geojson_provincias = load_geojson()

def mapa_color(df, columna_valor, leyenda_titulo):
    if geojson_provincias is None:
        return

    m = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)

   
    folium.Choropleth(
        geo_data=geojson_provincias,  
        name='choropleth',
        data=df,
        columns=['Provincia', columna_valor],  
        key_on='feature.properties.nombre',  
        fill_color='YlGnBu', 
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=leyenda_titulo
    ).add_to(m)

    # Mostrar el mapa en Streamlit
    st_folium(m, width=700, height=500)


# --- Lógica para selección interactiva del mapa ---
st.sidebar.header("Selección de Datos para el Mapa")

# Diccionario para mapear nombres amigables a DataFrames
dataframes_disponibles = {
    "Penetración de Internet": df_pen,
    "Velocidad Media de Descarga": df_vmd,
    "Acceso a Tecnologías": df_tec,
    "Datos Generales de Conectividad": df_con
}

dataset_seleccionado_nombre = st.sidebar.selectbox(
    "Seleccione el conjunto de datos:",
    options=list(dataframes_disponibles.keys())
)

df_seleccionado = dataframes_disponibles[dataset_seleccionado_nombre]

# Filtrar columnas numéricas para visualización (excluyendo 'Provincia' si existe y no es numérica)
columnas_numericas = [col for col in df_seleccionado.columns if pd.api.types.is_numeric_dtype(df_seleccionado[col])]
if 'Provincia' in columnas_numericas: 
    columnas_numericas.remove('Provincia')

if not columnas_numericas:
    st.warning(f"El conjunto de datos '{dataset_seleccionado_nombre}' no tiene columnas numéricas adecuadas para mostrar en el mapa (además de 'Provincia').")
else:
    columna_seleccionada = st.sidebar.selectbox(
        f"Seleccione la métrica de '{dataset_seleccionado_nombre}':",
        options=columnas_numericas
    )

    st.subheader(f"Mapa de {columna_seleccionada} por Provincia ({dataset_seleccionado_nombre})")
    mapa_color(df_seleccionado, columna_seleccionada, f"{columna_seleccionada} por Provincia")
