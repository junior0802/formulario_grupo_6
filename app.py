import streamlit as st
from PIL import Image
import os

# Configurar página
st.set_page_config(
    page_title="GRUPO 6",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS para títulos
st.markdown("""
<style>
.title-general {
    font-size: 72px;  /* Más grande que los demás */
    font-weight: 900;
    color: #4A90E2;
    text-align: center;
    margin: 30px 0 20px 0;
}
.title-institucional {
    font-size: 56px;
    font-weight: bold;
    text-align: center;
    margin: 10px 0;
}
.title-seccion {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    margin: 30px 0 15px 0;
}
</style>
""", unsafe_allow_html=True)

# Logo UCV centrado y ajustado
st.image("img/ucv_logo.png", use_container_width=True)

# Títulos institucionales
st.markdown("<p class='title-institucional'>UNIVERSIDAD CÉSAR VALLEJO</p>", unsafe_allow_html=True)
st.markdown("<p class='title-institucional'>ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</p>", unsafe_allow_html=True)

# Título general, mucho más grande
st.markdown("<p class='title-general'>📊 CLUSTERING DE RESEÑAS DE PRODUCTOS EN E-COMMERCE CON DATOS REALES – AMAZON</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección I: Introducción
st.markdown("<h2 style='text-align: center;'>I. INTRODUCCIÓN</h2>", unsafe_allow_html=True)
st.image("img/intro.png", use_container_width=True)  # Imagen opcional

st.markdown("""
<div style='text-align: justify;'>
En la actualidad, las plataformas de comercio electrónico como Amazon generan una gran cantidad de datos, entre ellos las reseñas de los productos. 
Estas reseñas son una fuente valiosa de información para las empresas, ya que reflejan la satisfacción del cliente y pueden ser utilizadas para mejorar productos y servicios.
Este estudio se centra en la creación de un sistema automatizado de análisis de reseñas utilizando técnicas de <b>machine learning</b>, con el objetivo de agrupar reseñas similares y clasificarlas en diferentes categorías de sentimientos.
El objetivo principal de este proyecto es desarrollar un sistema de agrupamiento y clasificación utilizando un enfoque <b>semi-supervisado</b>, que permita predecir los sentimientos de los usuarios sobre los productos y facilitar la mejora continua en la calidad de los mismos.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección II: Metodología
st.markdown("<h2 style='text-align: center;'>II. METODOLOGÍA</h2>", unsafe_allow_html=True)
st.image("img/metodologia.png", use_container_width=True)

st.markdown("""
<div style='text-align: justify;'>
La metodología empleada en este proyecto se basa en el uso de técnicas avanzadas de <b>análisis de texto</b> y <b>aprendizaje automático</b> para procesar y clasificar las reseñas de productos. 
Se siguió un enfoque de <b>clustering</b>, utilizando algoritmos como <b>K-means</b> y <b>GMM (Gaussian Mixture Models)</b>, los cuales permiten agrupar las reseñas en función de su similitud semántica.

Para el preprocesamiento de las reseñas, se utilizó el modelo de <b>embedding</b> de palabras <b>Word2Vec</b> para representar las reseñas en vectores numéricos. Posteriormente, se aplicaron técnicas de <b>reducción de dimensionalidad</b> como <b>PCA</b> y <b>t-SNE</b> para visualizar los grupos formados por las reseñas.

Además, se evaluaron distintos modelos de clasificación supervisada, utilizando un enfoque de <b>Stacking</b> para mejorar la precisión del sistema. Se realizaron pruebas con diferentes métricas, como <b>precisión</b>, <b>recall</b> y <b>F1-score</b>, para validar el rendimiento del sistema propuesto.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección III: Resultados y Discusión
st.markdown("<h2 style='text-align: center;'>III. RESULTADOS Y DISCUSIÓN</h2>", unsafe_allow_html=True)

graficos = [
    {
        "titulo": "Gráfico 1: Análisis de Sentimientos por Categoría de Producto",
        "archivo": "img/grafico_1.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Este gráfico muestra cómo se distribuyen los sentimientos (positivos, negativos y neutros) en distintas categorías de productos, como tecnología, hogar o ropa. La visualización evidencia que las categorías tecnológicas presentan una mayor proporción de reseñas negativas en comparación con los productos para el hogar, que tienden a tener opiniones más favorables. Esta segmentación permite identificar áreas con oportunidades de mejora o productos con alta satisfacción del cliente.
        </div>
        <div style='text-align: justify;'>
        A partir de este análisis, se pueden trazar estrategias específicas de atención al cliente, desarrollo de productos y marketing. También se demuestra la utilidad del modelo de clustering al permitir el análisis automático y visual de grandes volúmenes de opiniones, revelando patrones significativos por categoría de producto.
        </div>
        """
    },
    {
        "titulo": "Gráfico 2: Palabras Clave en Reseñas Positivas",
        "archivo": "img/grafico_2.png",
        "descripcion": """
        <div style='text-align: justify;'>
        El gráfico de palabras clave extraídas de reseñas positivas muestra términos frecuentemente utilizados como “excelente”, “rápido”, “calidad” o “recomendado”. Estas palabras clave reflejan los aspectos más valorados por los usuarios, siendo útiles para destacar fortalezas en la descripción de productos y reforzar estrategias de marketing centradas en los atributos preferidos por los consumidores.
        </div>
        <div style='text-align: justify;'>
        Esta visualización fue posible gracias al análisis de frecuencia posterior al preprocesamiento del texto. Su interpretación aporta valor estratégico al reconocer qué factores contribuyen a una experiencia positiva, orientando la toma de decisiones sobre mejoras de productos o campañas enfocadas en la satisfacción del cliente.
        </div>
        """
    },
    {
        "titulo": "Gráfico 3: Evaluación del Modelo de Clasificación Stacking",
        "archivo": "img/grafico_3.png",
        "descripcion": """
        <div style='text-align: justify;'>
        El modelo Stacking alcanzó los mejores valores de precisión, recall y F1-score en comparación con otros clasificadores individuales. El gráfico presenta métricas detalladas del rendimiento del modelo, evidenciando su capacidad de generalizar correctamente la clasificación de sentimientos en reseñas previamente no vistas.
        </div>
        <div style='text-align: justify;'>
        La estrategia de combinar múltiples modelos (como Random Forest y SVM) permitió mejorar la robustez y exactitud de las predicciones. Este resultado refuerza la importancia de los enfoques de ensamblado (ensemble learning) para resolver problemas complejos de análisis de texto en comercio electrónico.
        </div>
        """
    },
    {
        "titulo": "Gráfico 4: Embeddings de Reseñas en Espacio Reducido",
        "archivo": "img/grafico_4.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Este gráfico visualiza las reseñas en un espacio bidimensional reducido usando t-SNE, lo que permite observar la agrupación de reseñas con sentimientos similares. Se aprecia una clara separación entre clústeres positivos y negativos, lo que demuestra que las representaciones vectoriales generadas por Word2Vec capturan adecuadamente la semántica de los textos.
        </div>
        <div style='text-align: justify;'>
        La interpretación gráfica de los embeddings es esencial para validar la calidad del agrupamiento realizado. Esta técnica facilita la comprensión de cómo se estructuran los datos internamente y permite validar si los modelos están capturando patrones relevantes en las opiniones de los usuarios.
        </div>
        """
    },
    {
        "titulo": "Gráfico 5: Comparación Global de Modelos Clasificadores",
        "archivo": "img/grafico_5.png",
        "descripcion": """
        <div style='text-align: justify;'>
        En este gráfico se presenta una comparación directa entre distintos modelos de clasificación aplicados al análisis de sentimientos. El modelo Stacking se destaca claramente por su rendimiento global, superando a métodos como Naive Bayes, SVM y Árboles de Decisión en la mayoría de las métricas.
        </div>
        <div style='text-align: justify;'>
        Esta evaluación integral permite tomar decisiones informadas sobre qué modelo implementar en entornos reales. La capacidad de predecir correctamente los sentimientos es esencial en sistemas de recomendación y monitoreo automático de la experiencia del cliente.
        </div>
        """
    }
]

# Selector
opciones = [f"{i+1}. {g['titulo']}" for i, g in enumerate(graficos)]
seleccion = st.selectbox("📁 Selecciona un gráfico para visualizar:", opciones)
indice = opciones.index(seleccion)

# Mostrar gráfico
ruta = graficos[indice]["archivo"]
if os.path.exists(ruta):
    st.image(Image.open(ruta), use_container_width=True)
else:
    st.warning("⚠️ No se encontró la imagen.")

# Mostrar título centrado
st.markdown(f"<h3 style='text-align: center;'>{graficos[indice]['titulo']}</h3>", unsafe_allow_html=True)
st.markdown(graficos[indice]["descripcion"], unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección IV: Conclusiones
st.markdown("<h2 style='text-align: center;'>IV. CONCLUSIONES</h2>", unsafe_allow_html=True)

# Punto i
st.markdown("#### 4.1. CONCLUSIONES DEL AGRUPAMIENTO")
if os.path.exists("img/conclusion_i.png"):
    st.image("img/conclusion_i.png", use_container_width=True)
st.markdown("""
<div style='text-align: justify;'>
El análisis de agrupamiento permitió identificar patrones consistentes en las opiniones de los usuarios, revelando segmentos diferenciados por experiencias positivas, neutras o negativas. 
Este conocimiento resulta clave para estrategias de personalización y retroalimentación de productos.
</div>
""", unsafe_allow_html=True)

# Punto ii
st.markdown("#### 4.2. CONCLUSIONES DEL MODELO SUPERVISADO")
if os.path.exists("img/conclusion_ii.png"):
    st.image("img/conclusion_ii.png", use_container_width=True)
st.markdown("""
<div style='text-align: justify;'>
Los modelos de clasificación, en especial Stacking, mostraron una capacidad superior para predecir la polaridad de las reseñas con alta precisión, sugiriendo su aplicabilidad para tareas reales de análisis automático de opiniones.
</div>
""", unsafe_allow_html=True)

# Gráfico final decorativo
if os.path.exists("img/grafico_6.png"):
    st.image("img/grafico_6.png", use_container_width=True)

# Conclusión general
st.markdown("""
<div style='text-align: justify;'>
En conclusión, este proyecto ha demostrado que es posible aprovechar el poder del machine learning para extraer conocimiento útil de grandes volúmenes de reseñas en comercio electrónico. A través del uso combinado de modelos de agrupamiento y clasificación, se ha logrado no solo segmentar las opiniones de los clientes, sino también predecir su sentimiento con alta precisión. 
Estas capacidades pueden ser implementadas en sistemas reales para apoyar la toma de decisiones en ventas, marketing y atención al cliente, contribuyendo así a mejorar la experiencia del usuario en plataformas digitales como Amazon.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección Agradecimientos
st.markdown("""
<hr>
<p style='font-size:18px; text-align:center;'>
    <span style='font-size:24px;'>🙏</span> <em>Agradecemos profundamente a nuestros docentes y asesores por su guía y acompañamiento durante el desarrollo de esta investigación.</em>
</p>

<h4 style='text-align:center;'>✍️ <u>AUTORES</u></h4>
<p style='text-align:center;'>
    👨‍💻 <b>Junior Alvaro Pusaclla</b><br>
    👨‍💻 <b>Luis Atiro Vargas</b><br>
    👩‍💻 <b>Carmen Campos Domínguez</b><br>
    👨‍💻 <b>Cleber Ramos Ramos</b>
</p>

<h4 style='text-align:center;'>🧑‍🏫 <u>ASESORES</u></h4>
<p style='text-align:center;'>
    🧠 <b>Dr. Jorge Isaac Necochea Chamorro</b><br>
    🧠 <b>Mg. Marco Antonio Soto Martínez</b>
</p>

<p style='text-align:center; color: gray; font-size: 16px;'>📍 Lima – Perú • 🗓️ 2025</p>

<hr>
<p style='text-align:center; color: gray; font-size: 16px; margin-top: 40px;'>
    Grupo 6 • Escuela Profesional de Ingeniería de Sistemas • Universidad César Vallejo
</p>
""", unsafe_allow_html=True)
