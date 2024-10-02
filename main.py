import streamlit as st
import pandas as pd

st.title('Introducción al Análisis de Telecomunicaciones')

st.markdown('***')

st.sidebar.markdown('Visualizaciones')

df_pen_nac = pd.read_csv('penetracion_nacional.csv')
df_cap = pd.read_csv('capitales.csv')

st.map(data=df_cap)

