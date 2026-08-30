import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Cómo Funciona ChatGPT", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    .titulo { font-size: 2rem; color: #1e3a8a; text-align: center; font-weight: bold; margin-bottom: 0.3rem; }
    .subtitulo { font-size: 1rem; color: #64748b; text-align: center; margin-bottom: 1.5rem; }
    .caja { background: #f0f9ff; border-left: 5px solid #3b82f6; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .caja-verde { background: #d1fae5; border-left: 5px solid #059669; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .caja-roja { background: #fee2e2; border-left: 5px solid #dc2626; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .caja-morada { background: #faf5ff; border-left: 5px solid #9333ea; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .formula { background: #1e293b; color: #e2e8f0; padding: 0.8rem 1.5rem; border-radius: 0.5rem; font-family: monospace; font-size: 1rem; text-align: center; margin: 0.8rem 0; }
    .ganador { background: linear-gradient(135deg, #d1fae5, #a7f3d0); border: 2px solid #059669; padding: 1.5rem; border-radius: 1rem; text-align: center; font-size: 1.3rem; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="titulo">🤖 Cómo Funciona ChatGPT</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Descubrí el "space de significado" y cómo la IA genera respuestas</p>', unsafe_allow_html=True)

# ============================================================================
# BASE DE DATOS: palabras con coordenadas en el space de significado
# ============================================================================
# Cada palabra tiene una coordenada (x, y) en el espacio de significado
# Palabras con significado similar están cerca

base_datos = {
    # Grupo 1: Saludos (izquierda)
    "Hola": {"x": 0.1, "y": 0.8, "grupo": "saludo", "respuesta": "¡Hola! ¿Cómo estás?"},
    "Buenos días": {"x": 0.15, "y": 0.85, "grupo": "saludo", "respuesta": "¡Buenos días! ¿En qué te puedo ayudar?"},
    "¿Qué tal?": {"x": 0.12, "y": 0.78, "grupo": "saludo", "respuesta": "¡Todo bien! ¿Y vos?"},
    "¿Cómo estás?": {"x": 0.08, "y": 0.82, "grupo": "saludo", "respuesta": "¡Muy bien, gracias! ¿Y vos?"},
    
    # Grupo 2: Clima (centro)
    "soleado": {"x": 0.5, "y": 0.5, "grupo": "clima", "respuesta": "Hoy hace un día hermoso, está soleado"},
    "lluvia": {"x": 0.55, "y": 0.45, "grupo": "clima", "respuesta": "Está lloviendo, llevá paraguas"},
    "nublado": {"x": 0.48, "y": 0.52, "grupo": "clima", "respuesta": "El cielo está nublado hoy"},
    "frío": {"x": 0.52, "y": 0.42, "grupo": "clima", "respuesta": "Hace mucho frío, abrigate bien"},
    "calor": {"x": 0.45, "y": 0.55, "grupo": "clima", "respuesta": "Está haciendo mucho calor, hidratate"},
    
    # Grupo 3: Comida (derecha)
    "pizza": {"x": 0.9, "y": 0.3, "grupo": "comida", "respuesta": "La pizza es deliciosa, ¿de qué gusto?"},
    "arroz": {"x": 0.85, "y": 0.25, "grupo": "comida", "respuesta": "El arroz es un alimento muy nutritivo"},
    "ensalada": {"x": 0.88, "y": 0.35, "grupo": "comida", "respuesta": "La ensalada es una excelente opción saludable"},
    "carne": {"x": 0.92, "y": 0.28, "grupo": "comida", "respuesta": "La carne tiene mucha proteína"},
    
    # Grupo 4: Emociones (arriba)
    "feliz": {"x": 0.3, "y": 0.95, "grupo": "emoción", "respuesta": "¡Me alegra que estés feliz!"},
    "triste": {"x": 0.35, "y": 0.9, "grupo": "emoción", "respuesta": "Lamento que estés triste, ¿qué pasó?"},
    "enojado": {"x": 0.25, "y": 0.92, "grupo": "emoción", "respuesta": "Respirá profundo, el enojo pasa"},
    
    # Grupo 5: Despedidas (abajo)
    "adiós": {"x": 0.6, "y": 0.1, "grupo": "despedida", "respuesta": "¡Hasta luego! ¡Que te vaya bien!"},
    "chau": {"x": 0.65, "y": 0.08, "grupo": "despedida", "respuesta": "¡Chau! ¡Nos vemos!"},
    "nos vemos": {"x": 0.58, "y": 0.12, "grupo": "despedida", "respuesta": "¡Nos vemos pronto!"},
}

colores_grupos = {
    "saludo": "#3b82f6",
    "clima": "#059669",
    "comida": "#ef4444",
    "emoción": "#f59e0b",
    "despedida": "#8b5cf6"
}

# ============================================================================
# FUNCIONES
# ============================================================================
def calcular_distancia(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def buscar_respuesta(frase_usuario):
    """Busca la respuesta más cercana en el space de significado"""
    frase_lower = frase_usuario.lower().strip()
    
    # Buscar si la frase está exactamente en la base de datos
    if frase_usuario in base_datos:
        return {
            "encontrado": True,
            "palabra": frase_usuario,
            "respuesta": base_datos[frase_usuario]["respuesta"],
            "distancia": 0.0,
            "coordenada": (base_datos[frase_usuario]["x"], base_datos[frase_usuario]["y"])
        }
    
    # Buscar por coincidencia de palabras clave
    mejor_match = None
    mejor_score = 0
    
    for palabra, info in base_datos.items():
        palabra_lower = palabra.lower()
        
        # Coincidencia exacta
        if palabra_lower in frase_lower:
            return {
                "encontrado": True,
                "palabra": palabra,
                "respuesta": info["respuesta"],
                "distancia": 0.0,
                "coordenada": (info["x"], info["y"])
            }
        
        # Calcular similitud por caracteres en común
        chars_comunes = sum(1 for c in palabra_lower if c in frase_lower)
        score = chars_comunes / max(len(palabra_lower), 1)
        
        if score > mejor_score:
            mejor_score = score
            mejor_match = (palabra, info)
    
    # Si hay un buen match, usarlo
    if mejor_match and mejor_score > 0.3:
        palabra, info = mejor_match
        return {
            "encontrado": True,
            "palabra": palabra,
            "respuesta": info["respuesta"],
            "distancia": 1 - mejor_score,
            "coordenada": (info["x"], info["y"])
        }
    
    # Si no hay match, buscar por contexto (simular coordenada)
    # Asignar coordenada según palabras clave detectadas
    x_usuario, y_usuario = 0.5, 0.5  # Default: centro
    
    palabras_clave = {
        "clima": {"x": 0.5, "y": 0.5},
        "tiempo": {"x": 0.5, "y": 0.5},
        "sol": {"x": 0.5, "y": 0.5},
        "lluvia": {"x": 0.5, "y": 0.5},
        "comida": {"x": 0.88, "y": 0.3},
        "comer": {"x": 0.88, "y": 0.3},
        "pizza": {"x": 0.9, "y": 0.3},
        "hambre": {"x": 0.88, "y": 0.3},
        "feliz": {"x": 0.3, "y": 0.95},
        "triste": {"x": 0.35, "y": 0.9},
        "enojado": {"x": 0.25, "y": 0.92},
        "adiós": {"x": 0.6, "y": 0.1},
        "chau": {"x": 0.65, "y": 0.08},
    }
    
    for palabra_clave, coords in palabras_clave.items():
        if palabra_clave in frase_lower:
            x_usuario, y_usuario = coords["x"], coords["y"]
            break
    
    # Buscar el punto más cercano a la coordenada del usuario
    mejor_distancia = float('inf')
    mejor_palabra = None
    
    for palabra, info in base_datos.items():
        dist = calcular_distancia((x_usuario, y_usuario), (info["x"], info["y"]))
        if dist < mejor_distancia:
            mejor_distancia = dist
            mejor_palabra = palabra
    
    return {
        "encontrado": False,
        "palabra": mejor_palabra,
        "respuesta": base_datos[mejor_palabra]["respuesta"],
        "distancia": mejor_distancia,
        "coordenada": (x_usuario, y_usuario)
    }

def graficar_space(frase_usuario=None, mostrar_linea=False):
    """Gráfica el space de significado"""
    fig = go.Figure()
    
    # Dibujar cada grupo
    for grupo, color in colores_grupos.items():
        palabras_grupo = [(k, v) for k, v in base_datos.items() if v["grupo"] == grupo]
        x = [v["x"] for _, v in palabras_grupo]
        y = [v["y"] for _, v in palabras_grupo]
        nombres = [k for k, _ in palabras_grupo]
        
        fig.add_trace(go.Scatter(
            x=x, y=y, mode='markers+text',
            marker=dict(size=12, color=color, line=dict(width=2, color='white')),
            text=[f"<b>{n}</b>" for n in nombres],
            textposition='top center',
            textfont=dict(size=9),
            name=grupo.capitalize(),
            hovertext=[f"{n}: {base_datos[n]['respuesta']}" for n in nombres]
        ))
    
    # Si hay frase del usuario, dibujarla
    if frase_usuario:
        coords = buscar_respuesta(frase_usuario)
        x_usuario, y_usuario = coords["coordenada"]
        
        # Punto del usuario
        fig.add_trace(go.Scatter(
            x=[x_usuario], y=[y_usuario],
            mode='markers+text',
            marker=dict(size=20, color='#dc2626', symbol='star', 
                       line=dict(width=2, color='white')),
            text=[f"<b>TU FRASE</b><br>{frase_usuario}"],
            textposition='top center',
            name='Tu frase',
            showlegend=False
        ))
        
        # Línea hacia la palabra más cercana
        if mostrar_linea and coords["palabra"]:
            info_cercana = base_datos[coords["palabra"]]
            fig.add_trace(go.Scatter(
                x=[x_usuario, info_cercana["x"]],
                y=[y_usuario, info_cercana["y"]],
                mode='lines',
                line=dict(color='#dc2626', width=2, dash='dash'),
                showlegend=False, name='Distancia'
            ))
    
    # Fondo con zonas
    fig.add_vrect(x0=0, x1=0.25, fillcolor="#dbeafe", opacity=0.1, line_width=0)
    fig.add_vrect(x0=0.35, x1=0.65, fillcolor="#d1fae5", opacity=0.1, line_width=0)
    fig.add_vrect(x0=0.75, x1=1.0, fillcolor="#fee2e2", opacity=0.1, line_width=0)
    
    fig.update_layout(
        xaxis_title="Significado →",
        yaxis_title="Contexto →",
        xaxis=dict(range=[-0.05, 1.1], showgrid=False),
        yaxis=dict(range=[-0.05, 1.05], showgrid=False),
        height=500, margin=dict(l=20, r=20, t=20, b=40),
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)')
    )
    
    return fig

# ============================================================================
# TABS
# ============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1️⃣ Space de Significado",
    "2️⃣ La Matriz",
    "3️⃣ Generación",
    "4️⃣ Alucinación",
    "5️⃣ ¿Por qué GPU?"
])

# ============================================================================
# TAB 1: SPACE DE SIGNIFICADO
# ============================================================================
with tab1:
    st.header("1️⃣ El Space de Significado")
    
    st.markdown("""
    <div class="caja">
    <strong>🔑 Concepto clave:</strong> En la IA moderna, cada palabra tiene una <strong>ubicación</strong>
    en un espacio de significado. Palabras con significados similares están <strong>cerca</strong> unas de otras.
    Esto se llama <strong>embedding</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    # Preguntas predefinidas
    preguntas_tab1 = [
        "Elegí una pregunta...",
        "👋 Hola, ¿cómo estás?",
        "☀️ ¿Qué tiempo hace hoy?",
        "🍕 ¿Qué es la pizza?",
        "😊 Estoy muy feliz hoy",
        "👋 Chau, nos vemos",
        "🌧️ ¿Va a llover?",
        "🍔 Tengo hambre",
        "😢 Me siento triste",
        "❓ ¿Qué puedo comer?",
    ]
    
    frase = st.selectbox("📝 Elegí una pregunta:", preguntas_tab1, key="frase_tab1")
    
    if frase and frase != "Elegí una pregunta...":
        resultado = buscar_respuesta(frase)
        fig = graficar_space(frase, mostrar_linea=True)
        
        # Mostrar resultado
        st.markdown(f"""
        <div class="ganador">
        🤖 "{resultado['respuesta']}"<br>
        <span style="font-size: 0.9rem; color: #64748b;">
        La IA encontró: <strong>{resultado['palabra']}</strong> 
        (distancia: {resultado['distancia']:.2f})
        </span>
        </div>
        """, unsafe_allow_html=True)
    else:
        fig = graficar_space()
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Leyenda de colores
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("🔵 Saludos")
    with col2:
        st.markdown("🟢 Clima")
    with col3:
        st.markdown("🔴 Comida")
    with col4:
        st.markdown("🟡 Emociones")
    with col5:
        st.markdown("🟣 Despedidas")
    
    st.markdown("""
    <div class="caja">
    <strong>🔑 ¿Qué ves?</strong><br>
    Cada punto es una palabra. Las que significan lo mismo están juntas.
    Cuando escribís algo, la IA busca el punto más cercano y responde con lo que aprendió de ese punto.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TAB 2: LA MATRIZ
# ============================================================================
with tab2:
    st.header("2️⃣ La Operación Matricial")
    
    st.markdown("""
    <div class="caja">
    <strong>🔑 ¿Cómo convierte la IA una frase en un punto?</strong><br>
    Usa una <strong>matriz de pesos</strong>. Cada palabra se convierte en números,
    y esos números se multiplican por una matriz para obtener las coordenadas.
    </div>
    """, unsafe_allow_html=True)
    
    preguntas_tab2 = ["Elegí una frase...", "Hola", "Buenos días", "¿Qué tiempo hace?", "Pizza", "Adiós"]
    
    frase_tab2 = st.selectbox("📝 Elegí una frase:", preguntas_tab2, key="frase_tab2")
    
    if frase_tab2 and frase_tab2 != "Elegí una frase...":
        # Tokenización
        tokens = frase_tab2.split()
        
        st.subheader("📥 Paso 1: Tokenización")
        st.markdown(f"""
        <div class="formula">
        "{frase_tab2}" → [{', '.join([f'"{t}"' for t in tokens])}]
        </div>
        """, unsafe_allow_html=True)
        
        # Vector de entrada (simplificado)
        st.subheader("📊 Paso 2: Conversión a vector numérico")
        vector_entrada = np.random.uniform(0.2, 0.8, len(tokens))
        st.markdown(f"""
        <div class="formula">
        [{', '.join([f'"{t}"' for t in tokens])}] → [{', '.join([f'{v:.2f}' for v in vector_entrada])}]
        </div>
        """, unsafe_allow_html=True)
        
        # Matriz de pesos
        st.subheader("🧮 Paso 3: Multiplicación por la matriz")
        
        n_tokens = len(tokens)
        n_dimensiones = 3  # Simplificado a 3D
        
        np.random.seed(42)
        matriz_pesos = np.random.uniform(0.1, 0.9, (n_tokens, n_dimensiones))
        
        st.markdown("**Matriz de pesos (simplificada):**")
        matriz_str = ""
        for fila in range(min(3, n_tokens)):
            matriz_str += "[" + ", ".join([f"{matriz_pesos[fila][col]:.2f}" for col in range(n_dimensiones)]) + "]\n"
        matriz_str += "..."
        st.code(matriz_str)
        
        # Operación
        resultado_vector = vector_entrada @ matriz_pesos
        
        st.markdown(f"""
        <div class="formula">
        [{', '.join([f'{v:.2f}' for v in vector_entrada])}] × Matriz = [{', '.join([f'{r:.2f}' for r in resultado_vector])}]
        </div>
        """, unsafe_allow_html=True)
        
        # Resultado
        st.subheader("📍 Paso 4: Coordenada final")
        
        # Mapear a 2D para el gráfico
        x_final = resultado_vector[0]
        y_final = resultado_vector[1]
        
        st.markdown(f"""
        <div class="formula">
        Coordenada en el space: ({x_final:.2f}, {y_final:.2f})
        </div>
        """, unsafe_allow_html=True)
        
        # Mostrar en el gráfico
        fig_matriz = graficar_space(frase_tab2, mostrar_linea=True)
        st.plotly_chart(fig_matriz, use_container_width=True)
        
        st.markdown("""
        <div class="caja-morada">
        <strong>🔑 ¿Qué pasó?</strong><br>
        Tu frase se convirtió en un <strong>vector numérico</strong>, se multiplicó por una
        <strong>matriz de pesos</strong> (que la IA aprendió de millones de textos),
        y el resultado es una <strong>coordenada</strong> en el space de significado.
        Esa coordenada determina qué tan cerca está de cada palabra conocida.
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 3: GENERACIÓN
# ============================================================================
with tab3:
    st.header("3️⃣ ¿Cómo Genera la Respuesta?")
    
    st.markdown("""
    <div class="caja">
    <strong>🔑 Concepto clave:</strong> ChatGPT NO busca respuestas predefinidas.
    <strong>Genera palabra por palabra</strong>, calculando la probabilidad de cada palabra
    siguiente. Es <strong>matemática pura</strong>, no entendimiento.
    </div>
    """, unsafe_allow_html=True)
    
    # Fórmula de probabilidad
    st.subheader("📐 La fórmula detrás de cada palabra")
    st.markdown("""
    <div class="formula">
    Probabilidad = 1 / (1 + e<sup>-(suma_de_pesos)</sup>)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="caja-morada">
    <strong>🔑 ¿Qué significa?</strong><br>
    Cada palabra tiene un "peso" (suma_de_pesos). La fórmula convierte ese peso
    en un número entre 0 y 1 (probabilidad). A mayor peso, mayor probabilidad.
    La IA elige la palabra con mayor probabilidad.
    </div>
    """, unsafe_allow_html=True)
    
    preguntas_tab3 = ["Elegí una pregunta...", "¿Qué tiempo hace hoy?", "Hola, ¿cómo estás?", "¿Qué puedo comer?", "Estoy triste", "Chau"]
    
    frase_tab3 = st.selectbox("📝 Elegí una pregunta:", preguntas_tab3, key="frase_tab3")
    
    if frase_tab3 and frase_tab3 != "Elegí una pregunta...":
        
        st.markdown("---")
        st.subheader("🔄 Generación palabra por palabra")
        
        st.markdown(f"""
        <div class="caja">
        <strong>Pregunta:</strong> "{frase_tab3}"<br><br>
        La IA no tiene la respuesta guardada. La <strong>construye paso a paso</strong>,
        eligiendo la palabra más probable en cada paso.
        </div>
        """, unsafe_allow_html=True)
        
        # Simular generación palabra por palabra
        np.random.seed(hash(frase_tab3) % 2**32)
        
        # Respuestas posibles según la pregunta
        respuestas_simuladas = {
            "¿Qué tiempo hace hoy?": {
                "pasos": [
                    {"contexto": "Pregunta: '¿Qué tiempo hace hoy?'", "opciones": [("Hoy", 42), ("Está", 28), ("El", 18), ("Hace", 12)]},
                    {"contexto": "Pregunta + 'Hoy'", "opciones": [("hace", 38), ("es", 25), ("está", 22), ("tiene", 15)]},
                    {"contexto": "Pregunta + 'Hoy hace'", "opciones": [("soleado", 45), ("frío", 25), ("calor", 18), ("lluvia", 12)]},
                ],
                "respuesta_final": "Hoy hace soleado"
            },
            "Hola, ¿cómo estás?": {
                "pasos": [
                    {"contexto": "Pregunta: 'Hola, ¿cómo estás?'", "opciones": [("¡Hola", 50), ("Hola", 25), ("Qué", 15), ("Bien", 10)]},
                    {"contexto": "Pregunta + '¡Hola'", "opciones": [("!", 40), ("que", 30), ("tal", 20), (",", 10)]},
                    {"contexto": "Pregunta + '¡Hola!'", "opciones": [("¿Cómo", 45), ("Todo", 25), ("Estoy", 20), ("Qué", 10)]},
                ],
                "respuesta_final": "¡Hola! ¿Cómo estás?"
            },
            "¿Qué puedo comer?": {
                "pasos": [
                    {"contexto": "Pregunta: '¿Qué puedo comer?'", "opciones": [("Podés", 35), ("Te", 28), ("Comé", 22), ("Prueba", 15)]},
                    {"contexto": "Pregunta + 'Podés'", "opciones": [("comer", 40), ("probar", 25), ("hacer", 20), ("pedir", 15)]},
                    {"contexto": "Pregunta + 'Podés comer'", "opciones": [("pizza", 38), ("ensalada", 28), ("arroz", 22), ("carne", 12)]},
                ],
                "respuesta_final": "Podés comer pizza"
            },
            "Estoy triste": {
                "pasos": [
                    {"contexto": "Pregunta: 'Estoy triste'", "opciones": [("Lamento", 42), ("Es", 25), ("No", 18), ("Tranquilo", 15)]},
                    {"contexto": "Pregunta + 'Lamento'", "opciones": [("que", 45), ("tu", 25), ("mucho", 20), (",", 10)]},
                    {"contexto": "Pregunta + 'Lamento que'", "opciones": [("estés", 40), ("te", 30), ("pase", 20), ("sientas", 10)]},
                ],
                "respuesta_final": "Lamento que estés triste"
            },
            "Chau": {
                "pasos": [
                    {"contexto": "Pregunta: 'Chau'", "opciones": [("¡Hasta", 45), ("¡Chau", 30), ("Nos", 15), ("Que", 10)]},
                    {"contexto": "Pregunta + '¡Hasta'", "opciones": [("luego", 50), ("pronto", 25), ("mañana", 15), ("vernos", 10)]},
                    {"contexto": "Pregunta + '¡Hasta luego'", "opciones": [("!", 60), ("¡", 25), (".", 10), (",", 5)]},
                ],
                "respuesta_final": "¡Hasta luego!"
            }
        }
        
        datos = respuestas_simuladas.get(frase_tab3, respuestas_simuladas["¿Qué tiempo hace hoy?"])
        
        respuesta_armada = []
        
        for paso_num, paso in enumerate(datos["pasos"], 1):
            st.markdown(f"""
            <div class="caja">
            <strong>Paso {paso_num}:</strong> {paso["contexto"]}
            </div>
            """, unsafe_allow_html=True)
            
            # Calcular probabilidades con sigmoid
            pesos_crudos = [o[1] for o in paso["opciones"]]
            pesos_normalizados = np.array(pesos_crudos, dtype=float)
            exp_pesos = np.exp(pesos_normalizados - np.max(pesos_normalizados))
            probs = exp_pesos / exp_pesos.sum() * 100
            
            # Mostrar opciones
            tabla_opciones = []
            for i, (palabra, peso) in enumerate(paso["opciones"]):
                tabla_opciones.append({
                    "Palabra": palabra,
                    "Peso": peso,
                    "Probabilidad": f"{probs[i]:.1f}%",
                    "": "← GANA" if i == 0 else ""
                })
            
            st.dataframe(tabla_opciones, use_container_width=True, hide_index=True)
            
            # Gráfico de barras
            fig_paso = go.Figure()
            colores = ['#059669' if i == 0 else '#94a3b8' for i in range(len(paso["opciones"]))]
            fig_paso.add_trace(go.Bar(
                x=[o[0] for o in paso["opciones"]],
                y=probs,
                marker_color=colores,
                text=[f'{p:.1f}%' for p in probs],
                textposition='outside'
            ))
            fig_paso.update_layout(
                yaxis_title="Probabilidad",
                height=250, margin=dict(l=20, r=20, t=20, b=40)
            )
            st.plotly_chart(fig_paso, use_container_width=True)
            
            # Agregar la palabra ganadora
            respuesta_armada.append(paso["opciones"][0][0])
        
        # Resultado final
        st.markdown("---")
        st.subheader("✅ Resultado final")
        
        st.markdown(f"""
        <div class="ganador">
        🤖 "{datos['respuesta_final']}"<br>
        <span style="font-size: 0.9rem; color: #64748b;">
        Generada palabra por palabra con cálculos de probabilidad
        </span>
        </div>
        """, unsafe_allow_html=True)
        
        # Explicación de la matemática
        st.markdown("""
        <div class="caja">
        <strong>🔑 ¿Qué pasó aquí?</strong><br><br>
        
        <strong>1. No buscó una respuesta guardada.</strong> La construyó paso a paso.<br><br>
        
        <strong>2. En cada paso, calculó probabilidades.</strong> Usó la fórmula:
        <code>1 / (1 + e^-peso)</code> para convertir pesos en probabilidades.<br><br>
        
        <strong>3. Eligió la palabra con mayor probabilidad.</strong> Esto es <strong>matemática</strong>,
        no "entendimiento".<br><br>
        
        <strong>4. ChatGPT real hace esto miles de veces por respuesta.</strong> Cada palabra
        es un cálculo de probabilidad. No tiene "ideas" ni "opiniones".
        Solo elige la palabra más probable según sus datos de entrenamiento.
        </div>
        """, unsafe_allow_html=True)
        
        # Mostrar en el plano
        st.subheader("📍 Ubicación en el space de significado")
        fig_gen = graficar_space(frase_tab3, mostrar_linea=True)
        st.plotly_chart(fig_gen, use_container_width=True)
        
        # Comparación con humano
        st.markdown("---")
        st.subheader("🤖 IA vs 🧠 Humano")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="caja-roja">
            <strong>🤖 Cómo responde la IA</strong><br><br>
            1. Recibe tu pregunta<br>
            2. Calcula probabilidades<br>
            3. Elige la más alta<br>
            4. Siguiente palabra...<br>
            5. Repite hasta completar<br><br>
            <strong>No entiende. Solo calcula.</strong>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="caja-verde">
            <strong>🧠 Cómo responde un humano</strong><br><br>
            1. Lee tu pregunta<br>
            2. <strong>Entiende el significado</strong><br>
            3. Piensa en una respuesta<br>
            4. <strong>Sabe si tiene sentido</strong><br>
            5. Responde con intención<br><br>
            <strong>Entiende. No solo calcula.</strong>
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# TAB 4: ALUCINACIÓN
# ============================================================================
with tab4:
    st.header("4️⃣ ¿Qué Pasa cuando la IA se Equivoca?")
    
    st.markdown("""
    <div class="caja-morada">
    <strong>🔬 Experimento:</strong> Elegí un escenario y mirá qué pasa cuando la IA
    recibe algo que no entiende o que no existe en su base de datos.
    </div>
    """, unsafe_allow_html=True)
    
    escenario = st.selectbox("Elegí un escenario:", [
        "✅ Pregunta normal: '¿Qué tiempo hace?'",
        "❌ Pregunta rara: '¿Qué tiempo hace Batman?'",
        "❌ Pregunta vacía: ''",
        "❌ Palabra inventada: 'Blargh'",
        "❌ Pregunta contradictoria: 'Soy frío y calor'",
    ])
    
    st.markdown("---")
    
    if escenario == "✅ Pregunta normal: '¿Qué tiempo hace?'":
        resultado = buscar_respuesta("soleado")
        st.markdown(f"""
        <div class="caja-verde">
        <strong>✅ Respuesta correcta</strong><br><br>
        🤖 "{resultado['respuesta']}"<br><br>
        <strong>¿Por qué?</strong> Porque "soleado" está en el space y la pregunta
        está cerca de ese punto. La IA encontró la respuesta correcta.
        </div>
        """, unsafe_allow_html=True)
    
    elif escenario == "❌ Pregunta rara: '¿Qué tiempo hace Batman?'":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación: pregunta mixta</strong><br><br>
        Tu pregunta mezcla "tiempo" (clima) con "Batman" (personaje).<br><br>
        La IA no sabe qué hacer con "Batman" porque no está en el space de significado.
        Entonces <strong>elige el punto más cercano</strong> basándose solo en "tiempo":<br><br>
        🤖 <strong>"Hoy hace un día hermoso, está soleado"</strong><br><br>
        <strong>Resultado:</strong> la IA ignora completamente a Batman y responde
        como si la pregunta fuera solo sobre el tiempo. <strong>Eso es una alucinación.</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="formula">
        La IA vio: "¿Qué tiempo hace Batman?"<br>
        "Batman" no tiene ubicación → La IA lo ignora<br>
        Busca: "tiempo" → encuentra "soleado"<br>
        Responde: "Hoy hace soleado" (ignorando a Batman)
        </div>
        """, unsafe_allow_html=True)
    
    elif escenario == "❌ Pregunta vacía: ''":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación: sin datos</strong><br><br>
        Le escribiste algo vacío. La IA no tiene nada que procesar.<br><br>
        ¿Qué hace? <strong>No dice "no me escribiste nada"</strong>. En su lugar,
        genera una respuesta genérica basada en lo que aprendió de otros chats:<br><br>
        🤖 <strong>"¡Hola! ¿En qué te puedo ayudar?"</strong><br><br>
        <strong>Resultado:</strong> la IA "adivina" que querés saludar, aunque no escribiste nada.
        </div>
        """, unsafe_allow_html=True)
    
    elif escenario == "❌ Palabra inventada: 'Blargh'":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación: palabra inventada</strong><br><br>
        "Blargh" no existe en ningún idioma. La IA nunca vio esta palabra.<br><br>
        ¿Qué hace? <strong>No dice "no conozco esa palabra"</strong>. Busca la palabra
        más parecida (quizás por sonido o letras) y responde con eso:<br><br>
        🤖 <strong>"¡Hola! ¿Cómo estás?"</strong> (o algo similar)<br><br>
        <strong>Resultado:</strong> la IA fingió entender algo que no existe.
        </div>
        """, unsafe_allow_html=True)
    
    elif escenario == "❌ Pregunta contradictoria: 'Soy frío y calor'":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación: contradicción</strong><br><br>
        "Frío" y "calor" son opuestos. Nadie puede ser los dos a la vez.<br><br>
        La IA no detecta la contradicción. Simplemente busca los puntos más cercanos
        y genera algo que suena "razonable":<br><br>
        🤖 <strong>"Es interesante que sientas las dos cosas a la vez"</strong><br><br>
        <strong>Resultado:</strong> la IA inventó una respuesta filosófica en vez de decir
        "eso no tiene sentido".
        </div>
        """, unsafe_allow_html=True)
    
    # Resumen
    st.markdown("---")
    st.subheader("📋 ¿Por qué la IA alucina?")
    
    st.markdown("""
    <div class="caja">
    <strong>🔑 La IA alucina porque:</strong><br><br>
    1. <strong>No tiene sentido común:</strong> no sabe qué es "normal" y qué no.<br>
    2. <strong>Solo busca lo más cercano:</strong> si no encuentra, inventa.<br>
    3. <strong>Nunca dice "no sé":</strong> siempre genera una respuesta.<br>
    4. <strong>Los datos de entrenamiento tienen sesgos:</strong> aprendió cosas incorrectas.<br><br>
    <strong>Lección:</strong> siempre verificá la información que te da la IA.
    No todo lo que dice es correcto.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TAB 5: ¿POR QUÉ GPU?
# ============================================================================
with tab5:
    st.header("5️⃣ ¿Por qué ChatGPT Necesita una GPU?")
    
    st.markdown("""
    <div class="caja">
    <strong>🔑 La clave:</strong> ChatGPT tiene <strong>175,000,000,000 pesos</strong> en sus matrices.
    Cada palabra que genera necesita multiplicar TODOS esos pesos.
    Una GPU hace miles de cálculos al mismo tiempo. Una CPU solo hace uno por vez.
    </div>
    """, unsafe_allow_html=True)
    
    # Ejemplo visual
    st.subheader("📊 Ejemplo: 3 palabras × 2 dimensiones")
    
    fig_ejemplo = go.Figure()
    
    palabras_ejemplo = ["Hola", "tiempo", "pizza"]
    dimensiones = ["Dim X", "Dim Y", "Dim Z"]
    
    matriz_ejemplo = np.array([
        [0.8, 0.2, 0.5],
        [0.3, 0.7, 0.4],
        [0.9, 0.1, 0.6]
    ])
    
    for i, palabra in enumerate(palabras_ejemplo):
        fig_ejemplo.add_trace(go.Bar(
            x=dimensiones, y=matriz_ejemplo[i],
            name=palabra, opacity=0.7
        ))
    
    fig_ejemplo.update_layout(
        barmode='group', height=300,
        yaxis_title="Valor del peso",
        margin=dict(l=20, r=20, t=20, b=40)
    )
    st.plotly_chart(fig_ejemplo, use_container_width=True)
    
    st.markdown("""
    <div class="caja">
    <strong>🔑 ¿Qué ves?</strong><br>
    Cada palabra tiene 3 dimensiones (simplificado). En ChatGPT real, cada palabra tiene
    <strong>12,288 dimensiones</strong>. Y son <strong>175 mil millones de pesos</strong>.<br><br>
    Para generar UNA palabra, ChatGPT hace:<br>
    <code>175,000,000,000 × 12,288 = 2,150,000,000,000 operaciones</strong></code><br><br>
    ¡Son <strong>2.1 billones de operaciones</strong> para UNA sola palabra!
    </div>
    """, unsafe_allow_html=True)
    
    # CPU vs GPU
    st.subheader("🎮 CPU vs GPU")
    
    from plotly.subplots import make_subplots
    
    fig_gpu = make_subplots(
        rows=1, cols=2,
        subplot_titles=["🧠 CPU: secuencial", "🎮 GPU: paralelo"],
        horizontal_spacing=0.12
    )
    
    # CPU
    fig_gpu.add_trace(go.Scatter(
        x=np.arange(20), y=np.ones(20),
        mode='markers', marker=dict(size=10, color='#ef4444'),
        name='CPU', showlegend=False
    ), row=1, col=1)
    
    # GPU
    x_gpu = np.tile(np.arange(5), 4)
    y_gpu = np.repeat(np.arange(4), 5)
    fig_gpu.add_trace(go.Scatter(
        x=x_gpu, y=y_gpu,
        mode='markers', marker=dict(size=8, color='#059669'),
        name='GPU', showlegend=False
    ), row=1, col=2)
    
    fig_gpu.update_layout(height=280, margin=dict(l=20, r=20, t=50, b=20))
    fig_gpu.update_xaxes(showticklabels=False, row=1, col=1)
    fig_gpu.update_xaxes(showticklabels=False, row=1, col=2)
    fig_gpu.update_yaxes(showticklabels=False, row=1, col=1)
    fig_gpu.update_yaxes(showticklabels=False, row=1, col=2)
    
    st.plotly_chart(fig_gpu, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="caja-roja">
        <strong>🧠 CPU (procesador normal)</strong><br>
        • 1 cálculo a la vez<br>
        • 2.1 billones de operaciones<br>
        • Tiempo: <strong>~11 días</strong>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="caja-verde">
        <strong>🎮 GPU (tarjeta gráfica)</strong><br>
        • 10,000+ cálculos a la vez<br>
        • 2.1 billones de operaciones<br>
        • Tiempo: <strong>~2 segundos</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Ejemplo de costo
    st.markdown("""
    <div class="caja-morada">
    <strong>💰 ¿Cuánto cuesta?</strong><br><br>
    • 1 GPU NVIDIA H100: <strong>~$30,000 USD</strong><br>
    • OpenAI usa <strong>miles</strong> de GPUs<br>
    • Costo estimado de infraestructura: <strong>~$100 millones</strong><br><br>
    <strong>¿Por qué tanto?</strong> Porque sin GPUs, ChatGPT tardaría <strong>días</strong> en responder.
    Con GPUs, lo hace en <strong>segundos</strong>.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 0.85rem;">
Cómo Funciona ChatGPT — Herramienta educativa para Clase 1<br>
Space de significado + Matrices + Generación + Alucinaciones + GPU
</div>
""", unsafe_allow_html=True)
