import streamlit as st
from PIL import Image
import os

# Configurar página
st.set_page_config(
    page_title="Clustering de Reseñas - AMAZON",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título y logo de Amazon
col1, col2 = st.columns([6, 1])
with col1:
    st.markdown("""
    <h1 style='text-align: center; color:#4A90E2; font-size: 30px;'>
    📊 CLUSTERING DE RESEÑAS DE PRODUCTOS EN E-COMMERCE CON DATOS REALES – AMAZON
    </h1>
    """, unsafe_allow_html=True)
with col2:
    logo_path = "img/amazon_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=80)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección I: Introducción
st.markdown("<h2 style='text-align: center;'>I. INTRODUCCIÓN</h2>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: justify;'>
En la actualidad, las plataformas de comercio electrónico como Amazon generan una gran cantidad de datos, entre ellos las reseñas de los productos. 
Estas reseñas son una fuente valiosa de información para las empresas, ya que reflejan la satisfacción del cliente y pueden ser utilizadas para mejorar productos y servicios.
Este estudio se centra en la creación de un sistema automatizado de análisis de reseñas utilizando técnicas de **machine learning**, con el objetivo de agrupar reseñas similares y clasificarlas en diferentes categorías de sentimientos.
El objetivo principal de este proyecto es desarrollar un sistema de agrupamiento y clasificación utilizando un enfoque **semi-supervisado**, que permita predecir los sentimientos de los usuarios sobre los productos y facilitar la mejora continua en la calidad de los mismos.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección II: Metodología
st.markdown("<h2 style='text-align: center;'>II. METODOLOGÍA</h2>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: justify;'>
La metodología empleada en este proyecto se basa en el uso de técnicas avanzadas de **análisis de texto** y **aprendizaje automático** para procesar y clasificar las reseñas de productos. 
Se siguió un enfoque de **clustering**, utilizando algoritmos como **K-means** y **GMM (Gaussian Mixture Models)**, los cuales permiten agrupar las reseñas en función de su similitud semántica.

Para el preprocesamiento de las reseñas, se utilizó el modelo de **embedding** de palabras **Word2Vec** para representar las reseñas en vectores numéricos. Posteriormente, se aplicaron técnicas de **reducción de dimensionalidad** como **PCA** y **t-SNE** para visualizar los grupos formados por las reseñas.

Además, se evaluaron distintos modelos de clasificación supervisada, utilizando un enfoque de **Stacking** para mejorar la precisión del sistema. Se realizaron pruebas con diferentes métricas, como **precisión**, **recall** y **F1-score**, para validar el rendimiento del sistema propuesto.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sección III: Resultados y Discusión
st.markdown("<h2 style='text-align: center;'>III. RESULTADOS Y DISCUSIÓN</h2>", unsafe_allow_html=True)

# Lista de gráficos con títulos y descripciones
graficos = [
    {
        "titulo": "Gráfico 1: Análisis de Sentimientos por Categoría de Producto",
        "archivo": "img/grafico_1.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Este gráfico muestra la distribución de sentimientos (positivos, negativos y neutros) dentro de distintas categorías de productos alimenticios dentro del marketplace de Amazon. 
        Nos permite identificar qué tipos de productos generan experiencias positivas y cuáles están asociados a valoraciones críticas.

        Este tipo de análisis es fundamental para que los proveedores comprendan las percepciones de los consumidores y prioricen mejoras según los segmentos más débiles en satisfacción. 
        Asimismo, es útil para diseñar campañas focalizadas por categoría emocionalmente más aceptada.
        </div>
        """
    },
    {
        "titulo": "Gráfico 2: Palabras Clave en Reseñas Positivas",
        "archivo": "img/grafico_2.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Aquí se muestran las palabras más frecuentes en reseñas con calificaciones altas (4 y 5 estrellas), obtenidas mediante un análisis de frecuencias de texto. 
        Palabras como “sabor”, “natural”, “entrega rápida” o “presentación” son indicadores directos de atributos bien valorados.

        Estas palabras clave son esenciales para optimizar la estrategia comercial, ya que permiten reforzar los elementos percibidos como ventajas competitivas en las futuras campañas de producto o branding.
        </div>
        """
    },
    {
        "titulo": "Gráfico 3: Evaluación del Modelo de Clasificación Stacking",
        "archivo": "img/grafico_3.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Este gráfico compara el rendimiento del modelo de clasificación basado en Stacking frente a algoritmos tradicionales como Naive Bayes o SVM. 
        Stacking logra un mayor equilibrio entre las métricas de precisión, recall y F1-score.

        El resultado sugiere que usar un enfoque de ensamblaje puede ser una estrategia sólida para sistemas reales que manejan lenguaje natural ruidoso, como las reseñas de usuarios.
        </div>
        """
    },
    {
        "titulo": "Gráfico 4: Embeddings de Reseñas en Espacio Reducido",
        "archivo": "img/grafico_4.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Mediante técnicas de reducción de dimensionalidad (como t-SNE), este gráfico proyecta los embeddings de las reseñas para visualizar cómo se agrupan semánticamente. 
        Los puntos cercanos indican reseñas con contenido temático similar.

        Esta vista ofrece evidencia visual del buen funcionamiento del modelo de lenguaje, permitiendo usar estos vectores para clustering no supervisado o segmentación de clientes según estilo de reseña.
        </div>
        """
    },
    {
        "titulo": "Gráfico 5: Comparación Global de Modelos Clasificadores",
        "archivo": "img/grafico_5.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Se comparan diversos algoritmos de clasificación aplicados a sentimientos de reseñas: Naive Bayes, SVM, Random Forest y Stacking. 
        Las métricas muestran el desempeño bajo condiciones iguales de prueba, destacando a Stacking por su precisión y adaptabilidad.

        Esta visualización facilita elegir el mejor enfoque para aplicaciones reales de análisis de opinión, ofreciendo soporte empírico para justificar decisiones técnicas.
        </div>
        """
    },
    {
        "titulo": "Gráfico 6: Conclusión General del Proyecto",
        "archivo": "img/grafico_6.png",
        "descripcion": None  # Sin descripción, solo imagen decorativa
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

# Footer
st.markdown(
    "<p style='text-align: center; color: gray;'>Grupo 6 • Escuela Profesional de Ingeniería de Sistemas • Universidad César Vallejo</p>",
    unsafe_allow_html=True
)
