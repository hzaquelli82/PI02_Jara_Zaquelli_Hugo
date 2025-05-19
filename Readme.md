
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
### Insights y KPIs
En la gráfica se observa que el análisis de acceso a internet por cada 100 hogares como por cada 100 habitantes, tienen la misma pendiente. Incluso son gráficos idénticos. Pero se nota además que tomando los hogares estaríamos en casi un 80% de hogares, sin embargo tomando en cuenta los habitantes estaríamos casi en un 25%. Pero se evidencia un crecimiento constante en accesos.

En general hay diferencias entre provincias. Se nota una mayor penetración en las provincias del sur. Además hay una marcada diferencia entre penetracion por hogar y habitante, sobre todo en Capital Federal.
En una secuencia de gráficos se observa que la evolución ha sido diferente la lo largo de los años para las distintas provincias. Puede inferirse un mayor desplazamiento de la tecnología hacia las provincias. Mientras en Capital Federal el grado de penetración ya es alto.

Se observa que las provincias con más penetración no son exactamente las mismas que tienen las velocidades medias más altas. Por ello se evaluará a continuación la relación que existe con el acceso a la tegnología en las provincias.

Se observa un importante aumento en la velocidad media de bajada en loś últimos 2 años, por las características del gráfico del año 2022 es probable que se haya dado en los últimos trimestres.

Se observa que se ha incrementado el acceso a través de wireless, algo que puede ser interesante por representar una tegnología de bajo coste de instalación.

Observando los cuadros se puede ver que ADSL y Cablemodem son tegnologías concentradas en Buenos Aires, Capital Federal, Santa Fe y Córdoba. Incluso la fibra óptica.

También se observa que las provincias del sur que tienen una alta penetración, no tienen velocidades medias muy altas ni acceso a tecnologías más rápidas.

#### KPIs
####  Aumentar 2% el acceso a internet
Se pretende aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia. La fórmula es la siguiente:

_KPI_ = ((Nuevoacceso - Accesoactual)/ Accesoactual)* 100

Donde:

- "Nuevo acceso" se refiere al número de hogares con acceso a Internet después del próximo trimestre.
- "Acceso actual" se refiere al número de hogares con acceso a Internet en el trimestre actual.

####  Aumentar 3% la velocidad media de bajada
e pretende aumentar en un 3% la velocidad media de bajada, para el próximo trimestre, por provincia. La fórmula es la siguiente:

_KPI_ = ((vmd_nuevo - vmd_actual)/ vmd_actual)* 100

Donde:

- vmd_nuevo se refiere a la velocidad media de bajada del próximo trimestre.
- vmd_actual se refiere a la velocidad media de bajada en el trimestre actual.

####  Aumentar un 5% los accesos a internet via Fibra Óptica
Se pretende aumentar en un 5% los acceso de fibra óptica, para el próximo trimestre, por provincia. La fórmula es la siguiente:

_KPI_ = ((fibra_nuevo - fibra_actual)/ fibra_actual)* 100

Donde:

- fibra_nuevo se refiere los accesos de fibra óptica del próximo trimestre.
- fibra_actual se refiere a los accesos de fibra óptica en el trimestre actual.


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

=======
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

