import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import json
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go


st.set_page_config(
    page_title="Provincias",
    layout="wide",
    initial_sidebar_state="expanded")

alt.theme.enable('opaque')

df_pen = pd.read_csv('penetracion.csv')
df_vmd = pd.read_csv('vmd.csv')
df_tri = pd.read_csv('trimestres.csv')
df_tec = pd.read_csv('tecnologias.csv')

def mostrar_kpi_dona(kpi_actual, objetivo):
    # Determinar el color según el valor del KPI
    if kpi_actual >= objetivo:
        color = 'green'
    elif kpi_actual >= 0.75 * objetivo:
        color = 'orange'
    else:
        color = 'red'

    # Crear la figura de la dona usando Plotly
    fig = go.Figure(go.Pie(
       
        values=[min(kpi_actual, objetivo), max(0, objetivo - min(kpi_actual, objetivo))],
        hole=0.6,  # Dona
        marker_colors=[color, 'lightgray'],  # Color dinámico para KPI
        textinfo='none',  # No mostrar etiquetas dentro de la dona
    ))

    # Añadir el texto del KPI al centro de la dona
    fig.update_layout(
        annotations=[dict(
            text=f"{kpi_actual}",
            x=0.5, y=0.5, font_size=20, showarrow=False
        )],
        showlegend=False,
        margin=dict(t=20, b=20, l=20, r=20)
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

st.sidebar.header("Selección de Datos para ver Indicadores")
provincia = st.sidebar.selectbox("Selecciona una provincia", df_pen['Provincia'].unique())
anio = st.sidebar.selectbox("Selecciona un año", df_pen['Año'].unique())
trimestre = st.sidebar.selectbox("Selecciona un trimestre", df_pen['Trimestre'].unique())

# Filtrar los datos según la selección del usuario
df_filtrado_pen = df_pen[(df_pen['Provincia'] == provincia) & (df_pen['Año'] == anio) & (df_pen['Trimestre'] == trimestre)]
kpi1 = df_filtrado_pen['kpi_1'].values[0]
kpi1 = round(kpi1, 2)

df_filtrado_vmd = df_vmd[(df_vmd['Provincia'] == provincia) & (df_vmd['Año'] == anio) & (df_vmd['Trimestre'] == trimestre)]
kpi2 = df_filtrado_vmd['kpi_2'].values[0]
kpi2 = round(kpi2, 2)


df_filtrado_tecnologias = df_tec[(df_tec['Provincia'] == provincia) & (df_tec['Año'] == anio) & (df_tec['Trimestre'] == trimestre)]
kpi3 = df_filtrado_tecnologias['kpi_3'].values[0]
kpi3 = round(kpi3, 2)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### KPI 1")
    st.markdown("Acceso a Internet")
    mostrar_kpi_dona(kpi1, 2)
with col2:
    st.markdown("#### KPI 2")
    st.markdown("Velocidad de Internet")
    mostrar_kpi_dona(kpi2, 3)
with col3:
    st.markdown("#### KPI 3")
    st.markdown("Tecnologías de Internet")    
    mostrar_kpi_dona(kpi3, 5)
