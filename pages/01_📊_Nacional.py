import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(
    page_title="Datos Nacionales",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable('opaque')

sns.set_style("whitegrid")
sns.set_palette("Set2")  

df_n = pd.read_csv('nacion.csv')
df_tec = pd.read_csv('tecnologias.csv')
df_melted = pd.melt(df_tec, id_vars=['Año', 'Trimestre'], value_vars=['ADSL', 'Cablemodem', 'Fibra_óptica', 'Wireless'], var_name='Tecnología', value_name='Accesos')
df_melted['Accesos (en miles)'] = df_melted['Accesos'] / 1000


with st.sidebar:
    st.title('Tecnologías de Conexión')

    tec_lista =  df_melted['Tecnología'].unique().tolist()
    tecnologias = st.multiselect('Seleccione Tecnologías de comunicación', tec_lista, default=tec_lista)
    df_melted_tec = df_melted[df_melted['Tecnología'].isin(tecnologias)]


def penetracion_nacional():
    fig, ax = plt.subplots(figsize=(8, 3))
    sns.lineplot(x='Año', y='acc_cien_hogares', data=df_n, marker='o', ax=ax)

    #ax.set_title('Evolución de accesos por cada 100 habitantes', fontsize=16, weight='bold')
    ax.set_xlabel('Año')
    ax.set_ylabel('Accesos por cada 100 habitantes')
    ax.grid(True)

    st.pyplot(fig)


# Cargar el dataset de tecnologías

def tecnologia_nacion():
    
    fig, ax = plt.subplots(figsize=(6,3))

    sns.lineplot(x='Año', y='Accesos (en miles)', hue='Tecnología', data=df_melted_tec, marker='o', ax=ax)

    #ax.set_title('Evolución de las tecnologías de acceso a Internet', fontsize=16, weight='bold')
    ax.set_xlabel('Año', fontsize=12)
    ax.set_ylabel('Accesos (en miles)', fontsize=12)
    ax.grid(True)
    ax.ticklabel_format(axis='y', style='plain') 
    ax.legend(title='Tecnología', title_fontsize='10', fontsize='8')

    st.pyplot(fig)

def vmd_nacional():
    df_vmd = pd.read_csv('vmd_t.csv')

    #st.write(df_vmd.head())

    fig, ax = plt.subplots(figsize=(6,6)) 

    sns.barplot(data=df_vmd, x='año', y='vmd', ax=ax, palette='Blues_d')

    #ax.set_title('Evolución de la Velocidad de Descarga Promedio', fontsize=16, weight='bold')
    ax.set_xlabel('Periodo (Año-Trimestre)', fontsize=12)
    ax.set_ylabel('Velocidad Media de Descarga (Mbps)', fontsize=12)

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)


st.markdown('### Evolución de accesos por cada 100 habitantes')

with st.markdown('## Evolución de accesos por cada 100 habitantes'):
    
    penetracion_nacional()

col = st.columns((0.65,0.35), 
                 gap='large')

with col[0]:
    st.markdown('#### Tecnologías de Acceso')
    tecnologia_nacion()

with col[1]:
    st.markdown('####  Velocidad de Descarga Promedio')

    vmd_nacional()


