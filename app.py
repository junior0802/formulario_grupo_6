import streamlit as st
from PIL import Image
import os

# Configuración de página
st.set_page_config(
    page_title="GRUPO 6",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inicializar estado si no existe
if "mostrar_formulario" not in st.session_state:
    st.session_state.mostrar_formulario = False

if "archivo_subido" not in st.session_state:
    st.session_state.archivo_subido = None

# Función para volver a la pantalla de carga
def volver_a_carga():
    st.session_state.mostrar_formulario = False
    st.session_state.archivo_subido = None

# Pantalla inicial: carga de archivo
if not st.session_state.mostrar_formulario:
    st.markdown("""
    <style>
    .upload-box {
        border: 3px dashed #4A90E2;
        padding: 60px;
        border-radius: 20px;
        text-align: center;
        background-color: #f7faff;
        font-size: 20px;
        font-weight: bold;
        color: #4A90E2;
        animation: fadeIn 1.5s ease-in-out;
        margin-bottom: 20px;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>

    <div class="upload-box">
        📂 Arrastra y suelta tu archivo aquí o selecciónalo abajo
    </div>
    """, unsafe_allow_html=True)

    archivo = st.file_uploader("Selecciona un archivo para continuar", type=["csv", "txt", "xlsx", "json"])

    if st.button("✅ Continuar con el formulario"):
        if archivo is not None:
            st.session_state.archivo_subido = archivo
            st.session_state.mostrar_formulario = True
            st.experimental_rerun()
        else:
            st.warning("⚠️ Por favor, selecciona un archivo para continuar.")

else:
    # Título animado
    st.markdown("""
    <style>
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translate3d(0, 40px, 0);
      }
      to {
        opacity: 1;
        transform: translate3d(0, 0, 0);
      }
    }
    .animated-title {
      font-size: 80px;
      font-weight: 900;
      text-align: center;
      color: #4A90E2;
      animation: fadeInUp 1.5s ease forwards;
      margin: 20px 0 30px 0;
    }
    </style>

    <h1 class="animated-title">📊 CLUSTERING DE RESEÑAS DE PRODUCTOS EN AMAZON</h1>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>RESULTADOS Y DISCUSIÓN</h2>", unsafe_allow_html=True)

    # Botón para volver
    st.button("🔙 Volver a carga de archivo", on_click=volver_a_carga)
    
    # CONTENIDO VISUAL CON SELECTBOX
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
    
     opciones = [f"{i+1}. {g['titulo']}" for i, g in enumerate(graficos)]
    seleccion = st.selectbox("📁 Selecciona un gráfico para visualizar:", opciones)
    indice = opciones.index(seleccion)

    ruta = graficos[indice]["archivo"]
    if os.path.exists(ruta):
        st.image(Image.open(ruta), use_container_width=True)
    else:
        st.warning("⚠️ No se encontró la imagen.")

    st.markdown(f"<h3 style='text-align: center;'>{graficos[indice]['titulo']}</h3>", unsafe_allow_html=True)
    st.markdown(graficos[indice]["descripcion"], unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Agradecimientos
    st.markdown("""
    <hr>
    <p style='font-size:18px; text-align:center;'>
        <span style='font-size:24px;'>🙏</span> <em>Agradecemos profundamente a nuestros docentes y asesores...</em>
    </p>

    <h4 style='text-align:center;'>✍️ <u>AUTORES</u></h4>
    <p style='text-align:center;'>
        👨‍💻 <b>Alvaro Pusaclla, Junior</b><br>
        👨‍💻 <b>Atiro Vargas, Luis</b><br>
        👩‍💻 <b>Campos Domínguez, Carmen</b><br>
        👨‍💻 <b>Ramos Ramos, Cleber</b>
    </p>

    <h4 style='text-align:center;'>🧑‍🏫 <u>ASESORES</u></h4>
    <p style='text-align:center;'>
        🧠 <b>Dr. Necochea Chamorro, Jorge Isaac</b><br>
        🧠 <b>Mg. Soto Martínez, Marco Antonio</b>
    </p>

    <p style='text-align:center; color: gray; font-size: 16px;'>📍 Lima – Perú • 🗓️ 2025</p>

    <hr>
    <p style='text-align:center; color: gray; font-size: 16px; margin-top: 40px;'>
        Grupo 6 • Escuela Profesional de Ingeniería de Sistemas • Universidad César Vallejo
    </p>
    """, unsafe_allow_html=True)
