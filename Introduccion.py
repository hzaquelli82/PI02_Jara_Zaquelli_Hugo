import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt


st.set_page_config(
    page_title="Inicio",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable('opaque')

st.markdown('## Análisis de Telecomunicaciones - Internet ')

st.markdown('***')

image = st.image('img/Smart-City-redes.jpg')

#st.sidebar.header("Índice")

with st.sidebar:
    st.title('Argentina Internet')
    