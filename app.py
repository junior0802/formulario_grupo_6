import streamlit as st
from PIL import Image
import os

# Configurar página
st.set_page_config(
    page_title="Clustering de Reseñas - AMAZON",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cabecera con logo y título
col1, col2 = st.columns([6, 1])
with col1:
    st.markdown("<h1 style='color:#4A90E2;'>📊 Clustering de Reseñas de Productos en E-Commerce con datos reales – AMAZON</h1>", unsafe_allow_html=True)
with col2:
    logo_path = "img/amazon_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=80)

st.markdown("<hr>", unsafe_allow_html=True)

# Lista de gráficos
graficos = [
    {
        "archivo": "img/grafico_1.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Este gráfico muestra la distribución de sentimientos (positivos, negativos y neutros) dentro de distintas categorías de productos en Amazon. 
        Su análisis permite descubrir patrones emocionales vinculados a la naturaleza del producto, lo cual resulta esencial para identificar fortalezas y debilidades percibidas por los usuarios.

        A través de esta visualización, se pueden tomar decisiones más informadas sobre cuáles categorías requieren mayor atención o mejora. También sirve como insumo para estrategias de marketing específicas según la percepción del cliente.
        </div>
        """
    },
    {
        "archivo": "img/grafico_2.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Este gráfico ilustra las palabras más frecuentes encontradas en las reseñas positivas. El análisis de frecuencia semántica permite identificar los aspectos más valorados por los consumidores, como sabor, calidad, rapidez de entrega o presentación del producto.

        Al conocer estos patrones lingüísticos, las marcas pueden reforzar estos atributos en sus estrategias de producto o comunicación, alineando mejor la oferta con las expectativas reales del usuario.
        </div>
        """
    },
    {
        "archivo": "img/grafico_3.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Aquí se muestra el desempeño del modelo de clasificación basado en Stacking, una técnica que combina múltiples algoritmos para obtener un rendimiento más robusto. 
        Se presentan métricas como precisión, recall y F1-score frente a modelos individuales.

        El resultado evidencia que el modelo ensamblado ofrece un balance más sólido, permitiendo clasificaciones más confiables en escenarios de reseñas reales y desbalanceadas.
        </div>
        """
    },
    {
        "archivo": "img/grafico_4.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Esta visualización muestra cómo se agrupan semánticamente las reseñas en un espacio reducido de dimensiones (por ejemplo, mediante t-SNE o PCA). 
        Las reseñas similares aparecen cercanas entre sí, revelando estructuras latentes que no son evidentes a simple vista.

        Este tipo de análisis es clave para validar que el modelo lingüístico capta las relaciones entre términos y temas, ayudando a mejorar la calidad de los embeddings y su aplicabilidad a clustering.
        </div>
        """
    },
    {
        "archivo": "img/grafico_5.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Se presenta una comparación entre diversos modelos de clasificación utilizados en el estudio: Naive Bayes, SVM, Random Forest y Stacking. 
        Cada uno fue evaluado bajo las mismas condiciones y métricas estándar.

        El análisis final muestra que el modelo Stacking logra superar a los demás tanto en precisión como en capacidad de generalización, destacándose como el mejor candidato para implementaciones reales en comercio electrónico.
        </div>
        """
    },
    {
        "archivo": "img/grafico_6.png",
        "descripcion": """
        <div style='text-align: justify;'>
        Este gráfico representa la conclusión general del proyecto, integrando los resultados de clustering, embeddings, análisis de sentimiento y desempeño de modelos.
        Resume visualmente las predicciones logradas y cómo se distribuyen en función del aprendizaje automático aplicado.

        La conclusión permite identificar con claridad el valor que aporta este sistema inteligente para segmentar, comprender y anticipar las opiniones de los usuarios en plataformas como Amazon.
        </div>
        """
    }
]

# Selector
opciones = [f"Gráfico {i+1}" for i in range(len(graficos))]
seleccion = st.selectbox("📁 Selecciona un gráfico para visualizar:", opciones)
indice = opciones.index(seleccion)

# Mostrar imagen
ruta = graficos[indice]["archivo"]
if os.path.exists(ruta):
    img = Image.open(ruta)
    st.image(img, use_container_width=True)
else:
    st.warning("⚠️ No se encontró la imagen.")

# Descripción justificada
st.markdown(graficos[indice]["descripcion"], unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Footer
st.markdown(
    "<p style='text-align: center; color: gray;'>Grupo 6 • Escuela Profesional de Ingeniería de Sistemas • UCV</p>",
    unsafe_allow_html=True
)
