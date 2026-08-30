import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Cómo Aprende la IA", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    .titulo { font-size: 2rem; color: #1e3a8a; text-align: center; font-weight: bold; margin-bottom: 0.3rem; }
    .subtitulo { font-size: 1rem; color: #64748b; text-align: center; margin-bottom: 1.5rem; }
    .caja { background: #f0f9ff; border-left: 5px solid #3b82f6; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .caja-verde { background: #d1fae5; border-left: 5px solid #059669; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .caja-roja { background: #fee2e2; border-left: 5px solid #dc2626; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .caja-morada { background: #faf5ff; border-left: 5px solid #9333ea; padding: 1rem 1.5rem; border-radius: 0.5rem; margin: 1rem 0; }
    .formula { background: #1e293b; color: #e2e8f0; padding: 0.8rem 1.5rem; border-radius: 0.5rem; font-family: monospace; font-size: 1rem; text-align: center; margin: 0.8rem 0; }
    .ganador { background: linear-gradient(135deg, #d1fae5, #a7f3d0); border: 2px solid #059669; padding: 1.5rem; border-radius: 1rem; text-align: center; font-size: 1.5rem; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="titulo">🧠 ¿Cómo Decide la IA?</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Descubrí que la IA solo hace cuentas — y por qué se equivoca</p>', unsafe_allow_html=True)

# ============================================================================
# DATOS: familiares y pesos estadísticos
# ============================================================================
familiares_fijos = [
    ("👩 Mamá", 0.85),
    ("👨 Papá", 0.70),
    ("👧 Hermano/a", 0.55),
    ("👴 Abuelo/a", 0.45),
    ("👨‍👩‍👦 Tío/a", 0.30),
    ("🧑 Primo/a", 0.20),
    ("🐕 Mascota", 0.40),
    ("🏠 Vecino", 0.15),
]

# ============================================================================
# SECCIÓN 1: TUS PESOS
# ============================================================================
st.header("1️⃣ ¿A quién quieres más? (Tus pesos)")

st.markdown("""
<div class="caja">
Dale un peso del <strong>0 al 10</strong> a cada familiar según cuánto lo querés.
El <strong>0</strong> significa "no lo conozco" y el <strong>10</strong> es "lo quiero muchísimo".
</div>
""", unsafe_allow_html=True)

# Layout: 4 columnas
col1, col2, col3, col4 = st.columns(4)

pesos_usuario = {}
familiares_nombres = []
familiares_pesos_estadisticos = []

for i, (nombre, peso_est) in enumerate(familiares_fijos):
    col = [col1, col2, col3, col4][i % 4]
    with col:
        pesos_usuario[nombre] = st.slider(
            nombre, 0, 10, 8, key=f"peso_{i}",
            help=f"Peso estadístico promedio: {peso_est}"
        )

# Campo libre
st.markdown("---")
col_libre1, col_libre2 = st.columns([1, 2])
with col_libre1:
    nombre_libre = st.text_input("➕ Agregá alguien más (opcional)", placeholder="Ej: novio/a, profesor...")
with col_libre2:
    peso_libre = st.slider("Peso de esa persona", 0, 10, 7, key="peso_libre") if nombre_libre else 0

# Preparar datos
for nombre, peso_est in familiares_fijos:
    familiares_nombres.append(nombre)
    familiares_pesos_estadisticos.append(peso_est)

if nombre_libre.strip():
    familiares_nombres.append(nombre_libre.strip())
    familiares_pesos_estadisticos.append(0.25)  # peso desconocido

pesos_user_array = np.array([pesos_usuario[n] for n, _ in familiares_fijos] + 
                            ([peso_libre] if nombre_libre.strip() else []))

# ============================================================================
# SECCIÓN 2: EL CÁLCULO
# ============================================================================
st.markdown("---")
st.header("2️⃣ La operación matemática")

st.markdown("""
<div class="caja">
La IA <strong>no sabe</strong> quién es tu familia. Solo tiene <strong>pesos estadísticos</strong>
(promedio de miles de personas). Multiplica tus pesos por esos promedios y gana el más alto.
</div>
""", unsafe_allow_html=True)

# Calcular
resultados = []
for i, (nombre, peso_est) in enumerate(zip(familiares_nombres, familiares_pesos_estadisticos)):
    peso_user = pesos_user_array[i]
    resultado = peso_user * peso_est
    resultados.append({
        "Familiar": nombre,
        "Tu peso": peso_user,
        "×": "×",
        "Estadístico": f"{peso_est:.2f}",
        "=": "=",
        "Resultado": resultado
    })

# Encontrar ganador
idx_ganador = np.argmax(resultados[i]["Resultado"] for i in range(len(resultados)))

st.dataframe(resultados, use_container_width=True, hide_index=True)

# Fórmula
st.markdown(f"""
<div class="formula">
Resultado = Tu_Peso × Peso_Estadístico<br><br>
{resultados[idx_ganador]['Familiar']}: {pesos_user_array[idx_ganador]} × {familiares_pesos_estadisticos[idx_ganador]:.2f} = <strong>{resultados[idx_ganador]['Resultado']:.2f}</strong> ← GANADOR
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SECCIÓN 3: LA RESPUESTA
# ============================================================================
st.markdown("---")
st.header("3️⃣ La respuesta de la IA")

ganador = familiares_nombres[idx_ganador]
score = resultados[idx_ganador]["Resultado"]

st.markdown(f"""
<div class="ganador">
🤖 "Yo quiero más a mi {ganador}"<br>
<span style="font-size: 1rem; color: #64748b;">(puntuación: {score:.2f})</span>
</div>
""", unsafe_allow_html=True)

# Gráfico de barras
fig_barras = go.Figure()
colores = ['#059669' if i == idx_ganador else '#94a3b8' for i in range(len(familiares_nombres))]
fig_barras.add_trace(go.Bar(
    x=familiares_nombres, y=[r["Resultado"] for r in resultados],
    marker_color=colores,
    text=[f'{r["Resultado"]:.1f}' for r in resultados],
    textposition='outside'
))
fig_barras.update_layout(
    yaxis_title="Resultado (Tu peso × Estadístico)",
    height=350, margin=dict(l=20, r=20, t=20, b=80),
    xaxis_tickangle=-45
)
st.plotly_chart(fig_barras, use_container_width=True)

st.markdown("""
<div class="caja">
<strong>🔑 ¿Por qué "mamá"?</strong><br>
No porque la IA "sienta" algo. Sino porque mamá tiene el <strong>peso estadístico más alto</strong> (0.85)
y vos le diste un peso alto también. Si le dabas 0 a mamá y 10 a la mascota,
la IA respondería "mi mascota". <strong>Solo hace cuentas.</strong>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SECCIÓN 4: ALUCINACIÓN
# ============================================================================
st.markdown("---")
st.header("4️⃣ ¿Qué pasa si los datos son malos?")

st.markdown("""
<div class="caja-morada">
<strong>🔬 Experimento:</strong> A continuación podés ver qué pasa cuando la IA recibe
datos incorrectos, incompletos o inventados. La IA <strong>no tiene sentido común</strong>,
solo sigue sus pesos estadísticos.
</div>
""", unsafe_allow_html=True)

escenario = st.selectbox("Elegí un escenario:", [
    "✅ Tus datos son correctos",
    "❌ Error de tipeo: escribiste 'mam' sin tilde",
    "❌ Nombre inventado: 'Batman'",
    "❌ Todos los pesos en 0",
    "❌ Pesos contradictorios: todo en 10",
])

st.markdown("---")

if escenario == "✅ Tus datos son correctos":
    st.markdown("""
    <div class="caja-verde">
    <strong>✅ Resultado correcto</strong><br>
    La IA recibe datos válidos y responde según tus pesos reales.<br>
    Respuesta: <strong>"Yo quiero más a mi {ganador}"</strong>
    </div>
    """.format(ganador=ganador), unsafe_allow_html=True)

elif escenario == "❌ Error de tipeo: escribiste 'mam' sin tilde":
    st.markdown("""
    <div class="caja-roja">
    <strong>❌ Alucinación por error de tipeo</strong><br>
    Vos escribiste <code>"mam"</code> en vez de <code>"mamá"</code>.<br><br>
    La IA <strong>no entiende</strong> que "mam" es "mamá". Como no reconoce el nombre,
    usa el <strong>promedio de internet</strong>: "En internet la gente dice que quiere más a su mamá".<br><br>
    🤖 <strong>"Yo quiero más a mi mamá"</strong><br><br>
    <strong>Resultado:</strong> la IA te dio una respuesta que no es tuya. Respondió con el promedio
    de otros miles de personas. <strong>Eso es una alucinación.</strong>
    </div>
    """, unsafe_allow_html=True)

elif escenario == "❌ Nombre inventado: 'Batman'":
    st.markdown("""
    <div class="caja-roja">
    <strong>❌ Alucinación con nombre inventado</strong><br>
    Preguntaste por <code>"Batman"</code>, pero Batman no existe en la base de datos de la IA.<br><br>
    La IA <strong>no dice "no lo conozco"</strong>. En su lugar, <strong>inventa</strong> una respuesta
    basada en lo que aprendió de otros contextos.<br><br>
    🤖 <strong>"Yo quiero más a mi mamá"</strong> (o cualquier cosa parecida)<br><br>
    <strong>Resultado:</strong> la IA fingió saber la respuesta en vez de decir "no sé".
    <strong>Esto es una alucinación clásica.</strong>
    </div>
    """, unsafe_allow_html=True)

elif escenario == "❌ Todos los pesos en 0":
    st.markdown("""
    <div class="caja-roja">
    <strong>❌ Alucinación por falta de datos</strong><br>
    Le diste <strong>0 a todos</strong>. La IA no tiene información tuya.<br><br>
    ¿Qué hace? <strong>No dice "no tengo datos"</strong>. Usa el promedio de internet:
    "La mayoría de la gente dice que quiere más a su mamá".<br><br>
    🤖 <strong>"Yo quiero más a mi mamá"</strong><br><br>
    <strong>Resultado:</strong> sin datos, la IA <strong>adivina</strong> con lo que aprendió de otros.
    Si vos no querés a tu mamá (o no la tenés), la IA te da una respuesta incorrecta.
    </div>
    """, unsafe_allow_html=True)

elif escenario == "❌ Pesos contradictorios: todo en 10":
    st.markdown("""
    <div class="caja-roja">
    <strong>❌ Alucinación por datos irreales</strong><br>
    Le diste <strong>10 a todos</strong>. Pero nadie quiere igual a todos.<br><br>
    La IA ve que todos tienen el mismo peso y <strong>elige al primero</strong> (mamá)
    porque estadísticamente es la más común.<br><br>
    🤖 <strong>"Yo quiero más a mi mamá"</strong><br><br>
    <strong>Resultado:</strong> cuando los datos no tienen sentido, la IA <strong>inventa</strong>
    una respuesta "razonable" en vez de decir "estos datos no me sirven".
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SECCIÓN 5: ¿POR QUÉ NECESITA GPU?
# ============================================================================
st.markdown("---")
st.header("5️⃣ ¿Por qué la IA necesita una GPU?")

st.markdown("""
<div class="caja">
<strong>🔑 La clave:</strong> una IA como ChatGPT tiene <strong>miles de millones de pesos</strong>.
No son 8 como en nuestro ejemplo. Son <strong>175,000,000,000</strong>.
Cada respuesta necesita multiplicar todos esos pesos. Una GPU hace miles de cálculos
al mismo tiempo. Una CPU solo hace uno por vez.
</div>
""", unsafe_allow_html=True)

# Gráfico estático: CPU vs GPU
fig_gpu = make_subplots(
    rows=1, cols=2,
    subplot_titles=["🧠 CPU: 1 cálculo a la vez", "🎮 GPU: Miles a la vez"],
    horizontal_spacing=0.12
)

# Simular 100 cálculos
np.random.seed(42)
n_calc = 100

# CPU: secuencial
tiempos_cpu = np.arange(n_calc)
fig_gpu.add_trace(go.Scatter(
    x=tiempos_cpu, y=np.ones(n_calc),
    mode='markers',
    marker=dict(size=8, color='#ef4444'),
    name='CPU', showlegend=False
), row=1, col=1)

# Agregar flechas de tiempo
for i in range(0, n_calc, 10):
    fig_gpu.add_annotation(
        x=i, y=1, ax=i+5, ay=1.3,
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True, arrowhead=2, arrowcolor="#ef4444",
        row=1, col=1
    )

# GPU: paralelo
x_gpu = np.tile(np.arange(10), n_calc // 10)
y_gpu = np.repeat(np.arange(n_calc // 10), 10)
fig_gpu.add_trace(go.Scatter(
    x=x_gpu, y=y_gpu,
    mode='markers',
    marker=dict(size=5, color='#059669'),
    name='GPU', showlegend=False
), row=1, col=2)

fig_gpu.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=30))
fig_gpu.update_xaxes(showticklabels=False, title_text="Tiempo →", row=1, col=1)
fig_gpu.update_xaxes(showticklabels=False, title_text="Tiempo →", row=1, col=2)
fig_gpu.update_yaxes(showticklabels=False, title_text="Cálculos", row=1, col=1)
fig_gpu.update_yaxes(showticklabels=False, title_text="Cálculos", row=1, col=2)

st.plotly_chart(fig_gpu, use_container_width=True)

# Números comparativos
col_cpu, col_gpu = st.columns(2)
with col_cpu:
    st.markdown("""
    <div class="caja-roja">
    <strong>🧠 CPU (procesador normal)</strong><br>
    Hace <strong>1 cálculo</strong> por vez.<br>
    Para 175 mil millones de pesos:<br>
    <strong>~5 años</strong> para responder una frase.
    </div>
    """, unsafe_allow_html=True)
with col_gpu:
    st.markdown("""
    <div class="caja-verde">
    <strong>🎮 GPU (tarjeta gráfica)</strong><br>
    Hace <strong>miles de cálculos</strong> al mismo tiempo.<br>
    Para 175 mil millones de pesos:<br>
    <strong>~2 segundos</strong> para responder una frase.
    </div>
    """, unsafe_allow_html=True)

# Ejemplo numérico
st.markdown("""
<div class="caja-morada">
<strong>📊 Ejemplo simplificado:</strong><br><br>
Imaginá que ChatGPT recibe la frase <code>"¿A quién quieres?"</code> y debe calcular
la probabilidad de cada palabra siguiente. Tiene que hacer:<br><br>

<code>175,000,000,000 multiplicaciones × 50,000 palabras posibles = 8,750,000,000,000,000 operaciones</code><br><br>

Eso son <strong>8.7 mil billones de operaciones</strong> para UNA sola palabra.
Una GPU con 8,000 núcleos puede hacer eso en <strong>unos pocos segundos</strong>.
Una CPU tardaría <strong>años</strong>.<br><br>

<strong>Por eso las GPUs son caras y por eso las empresas de IA las compran por miles.</strong>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# RESUMEN
# ============================================================================
st.markdown("---")
st.header("📋 Resumen de la clase")

st.markdown("""
<div class="caja">
<strong>🔑 Lo que aprendimos hoy:</strong><br><br>

<strong>1. La IA solo hace cuentas.</strong><br>
Multiplica pesos y elige el más alto. No "siente", no "entiende".<br><br>

<strong>2. La IA necesita datos correctos.</strong><br>
Si le das datos malos (typos, inventados, vacíos), te da respuestas malas.
Esto se llama <strong>alucinación</strong>.<br><br>

<strong>3. La IA usa estadística.</strong><br>
Los pesos que usó para responder "mamá" son el <strong>promedio de miles de personas</strong>.
No son TUS pesos. Son los de todos.<br><br>

<strong>4. La IA necesita GPUs.</strong><br>
Miles de millones de pesos × miles de palabras = billones de operaciones.
Solo una GPU puede hacer eso a tiempo real.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 0.85rem;">
Cómo Aprende la IA — Herramienta educativa para Clase 1<br>
La IA no "sabe" — solo calcula probabilidades con pesos estadísticos
</div>
""", unsafe_allow_html=True)
