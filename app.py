import streamlit as st
from PIL import Image
import os

# Configurar página
st.set_page_config(
    page_title="Clustering de Reseñas - AMAZON",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Logo de la Universidad
ucv_logo_path = "img/ucv_logo.png"
if os.path.exists(ucv_logo_path):
    st.image(ucv_logo_path, width=150)

# Título general y logo de Amazon debajo
st.markdown("""
<h1 style='text-align: center; color:#4A90E2; font-size: 30px;'>
📊 CLUSTERING DE RESEÑAS DE PRODUCTOS EN E-COMMERCE CON DATOS REALES – AMAZON
</h1>
""", unsafe_allow_html=True)

amazon_logo_path = "img/amazon_logo.png"
if os.path.exists(amazon_logo_path):
    st.image(amazon_logo_path, width=80)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección I: Introducción
st.markdown("<h2 style='text-align: center;'>I. INTRODUCCIÓN</h2>", unsafe_allow_html=True)
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

# Lista de gráficos (Gráfico 6 removido)
graficos = [
    {
        "titulo": "Gráfico 1: Análisis de Sentimientos por Categoría de Producto",
        "archivo": "img/grafico_1.png",
        "descripcion": """<div style='text-align: justify;'>...</div>"""
    },
    {
        "titulo": "Gráfico 2: Palabras Clave en Reseñas Positivas",
        "archivo": "img/grafico_2.png",
        "descripcion": """<div style='text-align: justify;'>...</div>"""
    },
    {
        "titulo": "Gráfico 3: Evaluación del Modelo de Clasificación Stacking",
        "archivo": "img/grafico_3.png",
        "descripcion": """<div style='text-align: justify;'>...</div>"""
    },
    {
        "titulo": "Gráfico 4: Embeddings de Reseñas en Espacio Reducido",
        "archivo": "img/grafico_4.png",
        "descripcion": """<div style='text-align: justify;'>...</div>"""
    },
    {
        "titulo": "Gráfico 5: Comparación Global de Modelos Clasificadores",
        "archivo": "img/grafico_5.png",
        "descripcion": """<div style='text-align: justify;'>...</div>"""
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

# Mostrar título y descripción
st.markdown(f"### {graficos[indice]['titulo']}")
if graficos[indice]["descripcion"]:
    st.markdown(graficos[indice]["descripcion"], unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección IV: Conclusiones
st.markdown("<h2 style='text-align: center;'>IV. CONCLUSIONES</h2>", unsafe_allow_html=True)

# Punto i
st.markdown("#### i. Conclusiones del Agrupamiento")
grafico_i = "img/conclusion_i.png"  # reemplaza con tu imagen real
if os.path.exists(grafico_i):
    st.image(grafico_i, use_container_width=True)
st.markdown("""
<div style='text-align: justify;'>
El análisis de agrupamiento permitió identificar patrones consistentes en las opiniones de los usuarios, revelando segmentos diferenciados por experiencias positivas, neutras o negativas. 
Este conocimiento resulta clave para estrategias de personalización y retroalimentación de productos.
</div>
""", unsafe_allow_html=True)

# Punto ii
st.markdown("#### ii. Conclusiones del Modelo Supervisado")
grafico_ii = "img/conclusion_ii.png"  # reemplaza con tu imagen real
if os.path.exists(grafico_ii):
    st.image(grafico_ii, use_container_width=True)
st.markdown("""
<div style='text-align: justify;'>
Los modelos de clasificación, en especial Stacking, mostraron una capacidad superior para predecir la polaridad de las reseñas con alta precisión, sugiriendo su aplicabilidad para tareas reales de análisis automático de opiniones.
</div>
""", unsafe_allow_html=True)

# Gráfico final decorativo
grafico_6 = "img/grafico_6.png"
if os.path.exists(grafico_6):
    st.image(grafico_6, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Footer
st.markdown(
    "<p style='text-align: center; color: gray;'>Grupo 6 • Escuela Profesional de Ingeniería de Sistemas • Universidad César Vallejo</p>",
    unsafe_allow_html=True
)
