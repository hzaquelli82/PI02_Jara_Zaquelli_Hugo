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

alt.themes.enable('opaque')

df_pen = pd.read_csv('penetracion.csv')
df_vmd = pd.read_csv('vmd.csv')
df_tri = pd.read_csv('trimestres.csv')
df_tec = pd.read_csv('tecnologias.csv')
df_con = pd.read_csv('conectividad.csv')

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
        values=[kpi_actual, objetivo - kpi_actual],
        hole=0.6,  # Dona
        marker_colors=[color, 'lightgray'],  # Color dinámico para KPI
        textinfo='none',  # No mostrar etiquetas dentro de la dona
    ))

    # Añadir el texto del KPI al centro de la dona
    fig.update_layout(
        annotations=[dict(
            text=f"{kpi_actual} / {objetivo}",
            x=0.5, y=0.5, font_size=20, showarrow=False
        )],
        showlegend=False,
        margin=dict(t=20, b=20, l=20, r=20)
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)


col0 = st.columns((2,3,2))

with col0[2]:
    mostrar_kpi_dona(kpi0, 2)
    st.markdown('Incremento trimestral de Penetracion')
