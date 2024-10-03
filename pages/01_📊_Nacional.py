import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
sns.set_palette("Set2")  

st.markdown('## Datos a Nivel Nacional')


def penetracion_nacional():
    df_n = pd.read_csv('nacion.csv')
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='Año', y='acc_cien_hogares', data=df_n, marker='o', ax=ax)

    ax.set_title('Evolución de accesos por cada 100 habitantes', fontsize=16, weight='bold')
    ax.set_xlabel('Año', fontsize=12)
    ax.set_ylabel('Accesos por cada 100 habitantes', fontsize=12)
    ax.grid(True)

    st.pyplot(fig)


# Cargar el dataset de tecnologías

def tecnologia_nacion():
    df_tec = pd.read_csv('tecnologias.csv')
    df_melted = pd.melt(df_tec, id_vars=['Año', 'Trimestre'], value_vars=['ADSL', 'Cablemodem', 'Fibra_óptica', 'Wireless'], var_name='Tecnología', value_name='Accesos')
    df_melted['Accesos (en miles)'] = df_melted['Accesos'] / 1000
    tec_lista =  df_melted['Tecnología'].unique().tolist()

    tecnologias = st.multiselect('Seleccione Tecnologías de comunicación', tec_lista, default=tec_lista)
    df_melted_tec = df_melted[df_melted['Tecnología'].isin(tecnologias)]

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.lineplot(x='Año', y='Accesos (en miles)', hue='Tecnología', data=df_melted_tec, marker='o', ax=ax)

    ax.set_title('Evolución de las tecnologías de acceso a Internet', fontsize=16, weight='bold')
    ax.set_xlabel('Año', fontsize=12)
    ax.set_ylabel('Accesos (en miles)', fontsize=12)
    ax.grid(True)
    ax.ticklabel_format(axis='y', style='plain') 
    ax.legend(title='Tecnología', title_fontsize='13', fontsize='11')

    st.pyplot(fig)

# def vmd_nacional():
#     fig, ax = plt.subplots()
#     df_vmd = pd.read_csv('vmd.csv')
#     st.write(df_vmd.head())
#     df_vmd_nac =  df_vmd.groupby(['Año','Trimestre'])['vmd_prov'].sum().reset_index()
    
#     sns.barplot(data=df_vmd_nac,x='Año', y='vmd_prov')
#     ax.set_title('Evolución de la velocidad de descarga promedio', fontsize=12)

#     st.pyplot()


def vmd_nacional():
    df_vmd = pd.read_csv('vmd_t.csv')

    st.write(df_vmd.head())

    fig, ax = plt.subplots(figsize=(10, 6)) 

    sns.barplot(data=df_vmd, x='año', y='vmd', ax=ax, palette='Blues_d')

    ax.set_title('Evolución de la Velocidad de Descarga Promedio', fontsize=16, weight='bold')
    ax.set_xlabel('Periodo (Año-Trimestre)', fontsize=12)
    ax.set_ylabel('Velocidad Media de Descarga (Mbps)', fontsize=12)

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

penetracion_nacional()
tecnologia_nacion()
vmd_nacional()

