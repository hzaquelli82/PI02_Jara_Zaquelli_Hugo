import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import json
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import seaborn as sns



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

with st.sidebar:
    st.title('🏂 Indicadores')
    
    year_list = list(df_vmd['Año'].unique())    
    selected_year = st.selectbox('Selecccione un Año', year_list)

    trimes_list = list(df_tri['Trimestre'])
    selected_tri = st.selectbox('Selecccione un Trimestre', trimes_list)

    prov_list = list(df_vmd.Provincia.unique())
    selected_provincia = st.selectbox('Selecccione una Provincia', prov_list)


@st.cache_data
def load_geojson():
    with open('./ProvinciasArgentina.geojson') as f:
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
        fill_color='Reds',  # Paleta de colores
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Valor por Provincia'
    ).add_to(m)

    # Mostrar el mapa en Streamlit
    st_data = st_folium(m, width=500, height=500)


def vmd_provincia():
    mask = df_pen.Año ==  selected_year
    mask1= df_pen.Trimestre == selected_tri

    df_vmd_f =  df_vmd[mask & mask1]
    df_vmd_f =  df_vmd_f.sort_values(by='vmd_prov',ascending=True)
    df_vmd_f = df_vmd_f.reset_index(drop=True)
    df_vmd_f = df_vmd_f.head(7)


    fig, ax = plt.subplots(figsize=(4,2)) 

    sns.barplot(data=df_vmd_f, x='Provincia', y='vmd_prov', ax=ax, palette='Blues_d')

    #ax.set_title('Evolución de la Velocidad de Descarga Promedio', fontsize=16, weight='bold')
    ax.set_xlabel('Provincias')
    ax.set_ylabel('Velocidad Media de Descarga (Mbps)')

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

def fibra_provincia():
    mask = df_pen.Año ==  selected_year
    mask1= df_pen.Trimestre == selected_tri

    df_tec_f =  df_tec[mask & mask1]
    df_tec_f =  df_tec_f.sort_values(by='Fibra_óptica',ascending=True)
    df_tec_f = df_tec_f.reset_index(drop=True)
    df_tec_f = df_tec_f.head(7)


    fig, ax = plt.subplots(figsize=(4,2)) 

    sns.barplot(data=df_tec_f, x='Provincia', y='Fibra_óptica', ax=ax, palette='Blues_d')

    #ax.set_title('Evolución de la Velocidad de Descarga Promedio', fontsize=16, weight='bold')
    ax.set_xlabel('Provincias')
    ax.set_ylabel('Accesos de Fibra Óptica')

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

col0 = st.columns((2,1))

with col0[0]:
    st.markdown('## Penetración cada 100 hogares por Provincia')
    mask = df_pen.Año ==  selected_year
    mask1= df_pen.Trimestre == selected_tri

    df_pen_filtro =  df_pen[mask & mask1]
    mapa_color(df_pen_filtro, 'pen_c_cien_hog')


with col0[1]:
    st.markdown('###  Velocidad de Descarga Promedio')
    vmd_provincia()

    st.markdown('###   Accesos de Fibra Óptica')
    fibra_provincia()
    


st.write(df_pen.head())
st.write(df_vmd.head())
st.write(df_tec.head())
st.write(df_con)
top_ten = df_con.sort_values(by='Población', ascending=False)
st.write(top_ten.head(10))