# Proyecto de Telecomunicaciones en Argentina
***

## Descripción del Proyecto
Este proyecto consiste en un análisis exploratorio de datos (EDA) realizado sobre una base de datos proporcionada por ENACOM (Ente Nacional de Comunicaciones de Argentina). El objetivo principal es analizar el estado actual e histórico de las telecomunicaciones en Argentina, particularmente en lo que respecta a accesos a Internet, penetración de mercado, y tecnología utilizada en el país.

## Contenido del Proyecto
El análisis se lleva a cabo en varias fases, que incluyen la limpieza y visualización de los datos para obtener conclusiones relevantes. Las secciones principales del notebook son las siguientes:

### Introducción

Explicación del contexto y los objetivos del análisis.
Descripción del conjunto de datos de telecomunicaciones proporcionados por ENACOM.
### Importación de Librerías

Las siguientes librerías de Python fueron utilizadas para el análisis:
pandas: Para la manipulación de los datos.
numpy: Para operaciones numéricas.
matplotlib y seaborn: Para la visualización de los datos.
openpyxl: Para manejar archivos Excel.
warnings: Para manejar advertencias.
### Lectura de Datos

El conjunto de datos principal se encuentra en un archivo Excel llamado Internet.xlsx que contiene varias hojas con datos desglosados por acceso, tecnología, velocidad, penetración de mercado, entre otros.
Se utilizó el método read_excel de pandas para cargar todas las hojas del archivo en un diccionario de dataframes, con los siguientes nombres de hojas:
Acc_vel_loc_sinrangos
Velocidad_sin_Rangos
Accesos_tecnologia_localidad
Velocidad % por prov
Y otros...
### Limpieza y Exploración de Datos

Procesos de selección, filtrado y limpieza de los datos para asegurar su integridad y preparar las visualizaciones.
### Visualización de Datos

Se utilizaron gráficos de barras, histogramas, y gráficos de dispersión para analizar la distribución de los datos y obtener insights clave sobre el estado de las telecomunicaciones en Argentina.
## Instrucciones de Ejecución
Para ejecutar este notebook y realizar el análisis, sigue los siguientes pasos:

Clona este repositorio o descarga el archivo del notebook.
Asegúrate de tener instaladas las librerías necesarias. Puedes instalarlas usando pip:
bash
Copiar código
pip install pandas numpy matplotlib seaborn openpyxl
Ejecuta el notebook con Jupyter Notebook, JupyterLab o Visual Studio Code.
## Conclusiones
Este análisis permite comprender cómo ha evolucionado el acceso a Internet en Argentina, las tecnologías más utilizadas, y las diferencias en velocidad y penetración entre distintas regiones. Los resultados obtenidos podrán servir para tomar decisiones basadas en datos en el sector de telecomunicaciones.

