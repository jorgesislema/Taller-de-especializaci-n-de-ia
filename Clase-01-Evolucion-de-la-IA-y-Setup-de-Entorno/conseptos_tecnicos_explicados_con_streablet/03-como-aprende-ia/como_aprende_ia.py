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
# DATOS BASE
# ============================================================================
familiares = [
    ("👩 Mamá", 0.85, 1.0),
    ("👨 Papá", 0.70, 0.9),
    ("👧 Hermano/a", 0.55, 0.7),
    ("👴 Abuelo/a", 0.45, 0.5),
    ("👨‍👩‍👦 Tío/a", 0.30, 0.4),
    ("🧑 Primo/a", 0.20, 0.3),
    ("🐕 Mascota", 0.40, 0.6),
    ("🏠 Vecino", 0.15, 0.2),
]

nombres = [f[0] for f in familiares]
pesos_est = np.array([f[1] for f in familiares])
# Posición X en el plano: qué tan "cercano" es el familiar (1=más cercano)
posicion_x = np.array([f[2] for f in familiares])

# ============================================================================
# TABS
# ============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1️⃣ Mis Pesos",
    "2️⃣ Plano Cartesiano",
    "3️⃣ Operación Matricial",
    "4️⃣ Alucinaciones",
    "5️⃣ ¿Por qué GPU?"
])

# ============================================================================
# TAB 1: MIS PESOS
# ============================================================================
with tab1:
    st.header("1️⃣ ¿A quién quieres más? (Tus pesos)")

    st.markdown("""
    <div class="caja">
    Dale un peso del <strong>0 al 10</strong> a cada familiar según cuánto lo querés.
    No importa cuánto le des a cada uno: <strong>mamá siempre ganará</strong>
    porque el peso estadístico que la IA tiene de ella es el más alto (0.85).
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    pesos_usuario = []

    for i, (nombre, peso_est, _) in enumerate(familiares):
        col = [col1, col2, col3, col4][i % 4]
        with col:
            p = st.slider(
                f"{nombre}", 0, 10, 8, key=f"peso_{i}",
                help=f"Estadístico promedio: {peso_est}"
            )
            pesos_usuario.append(p)

    pesos_usuario = np.array(pesos_usuario)

    st.markdown("---")
    st.subheader("📊 Tus pesos vs Los pesos de la IA")

    fig_tus = go.Figure()
    fig_tus.add_trace(go.Bar(
        x=nombres, y=pesos_usuario,
        name='Tus pesos', marker_color='#3b82f6',
        text=[f'{p}' for p in pesos_usuario], textposition='outside'
    ))
    fig_tus.add_trace(go.Bar(
        x=nombres, y=pesos_est * 10,
        name='Estadístico (×10)', marker_color='#94a3b8',
        text=[f'{p:.0f}' for p in pesos_est * 10], textposition='outside'
    ))
    fig_tus.update_layout(
        barmode='group', height=350,
        yaxis_title="Peso", margin=dict(l=20, r=20, t=20, b=80),
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig_tus, use_container_width=True)

    st.markdown("""
    <div class="caja-morada">
    <strong>🔑 Observá:</strong> los pesos estadísticos (grises) son el <strong>promedio de miles de personas</strong>.
    No son TUS pesos. Son los de todos. La IA usa esos promedios para "adivinar".
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TAB 2: PLANO CARTESIANO
# ============================================================================
with tab2:
    st.header("2️⃣ Plano Cartesiano: ¿Dónde está cada familiar?")

    st.markdown("""
    <div class="caja">
    Cada familiar es un <strong>punto en el plano</strong>.<br>
    <strong>Eje X:</strong> qué tan cercano es (1.0 = familiar directo, 0.1 = casi no lo conocés).<br>
    <strong>Eje Y:</strong> el peso que le diste vos (0 a 10).
    </div>
    """, unsafe_allow_html=True)

    fig_plano = go.Figure()

    # Puntos de cada familiar
    for i, (nombre, peso_est, pos_x) in enumerate(familiares):
        color = '#059669' if i == 0 else '#3b82f6'  # mamá en verde
        tamano = 15 if i == 0 else 10
        fig_plano.add_trace(go.Scatter(
            x=[pos_x], y=[pesos_usuario[i]],
            mode='markers+text',
            marker=dict(size=tamano, color=color, line=dict(width=2, color='white')),
            text=[f"<b>{nombre}</b><br>({pesos_usuario[i]})"],
            textposition='top center',
            textfont=dict(size=10),
            name=nombre,
            hovertext=f"{nombre}<br>Tu peso: {pesos_usuario[i]}<br>Estadístico: {peso_est}"
        ))

    # Línea de tendencia: recta que mejor ajusta tus puntos
    z = np.polyfit(posicion_x, pesos_usuario, 1)
    linea_x = np.linspace(0, 1.1, 100)
    linea_y = np.polyval(z, linea_x)
    fig_plano.add_trace(go.Scatter(
        x=linea_x, y=linea_y,
        mode='lines', line=dict(color='#94a3b8', width=2, dash='dash'),
        name='Tendencia', showlegend=False
    ))

    # Región de "familia directa"
    fig_plano.add_vrect(x0=0.6, x1=1.1, fillcolor="#d1fae5", opacity=0.15,
                        line_width=0, annotation_text="Familia directa", annotation_position="top left")

    fig_plano.update_layout(
        xaxis_title="Cercanía (1.0 = más cercano)",
        yaxis_title="Tu peso (0 a 10)",
        xaxis=dict(range=[0, 1.15], dtick=0.2),
        yaxis=dict(range=[-0.5, 11]),
        height=450, margin=dict(l=20, r=20, t=20, b=40),
        showlegend=True, legend=dict(x=0.01, y=0.99)
    )

    st.plotly_chart(fig_plano, use_container_width=True)

    st.markdown(f"""
    <div class="caja-verde">
    <strong>🔑 ¿Qué ves?</strong><br>
    Los familiares directos (mamá, papá, hermano) están a la <strong>derecha</strong> del plano
    y más arriba. Los lejanos (primo, vecino) están a la <strong>izquierda</strong> y abajo.<br><br>
    <strong>Mamá está arriba a la derecha</strong> porque tiene alta cercanía (1.0) Y alto peso tuyo ({pesos_usuario[0]}).
    Por eso <strong>siempre gana</strong>.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TAB 3: OPERACIÓN MATRICIAL
# ============================================================================
with tab3:
    st.header("3️⃣ La operación matricial")

    st.markdown("""
    <div class="caja">
    La IA hace una <strong>multiplicación de vectores</strong>: tu vector de pesos × el vector de pesos estadísticos.
    El resultado es un número por cada familiar. El más alto gana.
    </div>
    """, unsafe_allow_html=True)

    # Vector de usuario
    st.subheader("📥 Paso 1: Tu vector de entrada")
    st.markdown(f"""
    <div class="formula">
    Tu = [{', '.join([str(p) for p in pesos_usuario])}]
    </div>
    """, unsafe_allow_html=True)

    # Vector estadístico
    st.subheader("📊 Paso 2: Vector de pesos estadísticos de la IA")
    st.markdown(f"""
    <div class="formula">
    IA = [{', '.join([f'{p:.2f}' for p in pesos_est])}]
    </div>
    """, unsafe_allow_html=True)

    # Operación
    st.subheader("🧮 Paso 3: Multiplicación punto a punto")
    st.markdown("""
    <div class="caja">
    Cada resultado = <strong>Tu peso × Peso estadístico</strong><br>
    El familiar con el resultado más alto es el que "la IA dice que querés más".
    </div>
    """, unsafe_allow_html=True)

    # Tabla de operaciones
    resultados = pesos_usuario * pesos_est
    tabla_ops = []
    for i, (nombre, _, _) in enumerate(familiares):
        tabla_ops.append({
            "Familiar": nombre,
            "Tu peso": int(pesos_usuario[i]),
            "×": "×",
            "Estadístico": f"{pesos_est[i]:.2f}",
            "=": "=",
            "Resultado": f"{resultados[i]:.2f}",
            "": "← GANADOR" if i == np.argmax(resultados) else ""
        })

    st.dataframe(tabla_ops, use_container_width=True, hide_index=True)

    # Fórmula matricial
    st.subheader("📐 Paso 4: En notación matemática")

    ganador_idx = np.argmax(resultados)
    ganador_nombre = nombres[ganador_idx]
    ganador_score = resultados[ganador_idx]

    st.markdown(f"""
    <div class="formula">
    Resultado = Tu × Peso_IA<br><br>
    [{', '.join([str(p) for p in pesos_usuario])}] × [{', '.join([f'{p:.2f}' for p in pesos_est])}]<br><br>
    = [{', '.join([f'{r:.2f}' for r in resultados])}]<br><br>
    Máximo = {ganador_score:.2f} → <strong>{ganador_nombre}</strong>
    </div>
    """, unsafe_allow_html=True)

    # Respuesta
    st.markdown(f"""
    <div class="ganador">
    🤖 "Yo quiero más a mi {ganador_nombre}"<br>
    <span style="font-size: 1rem; color: #64748b;">(puntuación: {ganador_score:.2f})</span>
    </div>
    """, unsafe_allow_html=True)

    # Gráfico de resultados
    fig_res = go.Figure()
    colores = ['#059669' if i == ganador_idx else '#3b82f6' for i in range(len(nombres))]
    fig_res.add_trace(go.Bar(
        x=nombres, y=resultados,
        marker_color=colores,
        text=[f'{r:.2f}' for r in resultados],
        textposition='outside'
    ))
    fig_res.update_layout(
        yaxis_title="Resultado (Tu × Estadístico)",
        height=350, margin=dict(l=20, r=20, t=20, b=80),
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig_res, use_container_width=True)

    st.markdown("""
    <div class="caja">
    <strong>🔑 ¿Por qué mamá siempre gana?</strong><br>
    Porque tiene el <strong>peso estadístico más alto</strong> (0.85). Aunque le des 0 a mamá
    y 10 a todos los demás, mamá tiene ventaja porque la IA asume que
    "la mayoría de la gente quiere más a su mamá". Tus pesos personales
    <strong>casi no cambian</strong> el resultado final. Eso es lo peligroso de la IA:
    <strong>responde con el promedio, no con tu realidad</strong>.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TAB 4: ALUCINACIONES
# ============================================================================
with tab4:
    st.header("4️⃣ ¿Qué pasa si los datos son malos?")

    st.markdown("""
    <div class="caja-morada">
    <strong>🔬 Experimento:</strong> Elegí un escenario y mirá qué pasa cuando la IA
    recibe datos incorrectos. La IA <strong>no tiene sentido común</strong>, solo sigue sus pesos estadísticos.
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
        st.markdown(f"""
        <div class="caja-verde">
        <strong>✅ Resultado correcto</strong><br>
        La IA recibe datos válidos y responde según tus pesos.<br><br>
        🤖 <strong>"Yo quiero más a mi {ganador_nombre}"</strong><br><br>
        <strong>¿Por qué?</strong> Porque mamá tiene el peso estadístico más alto (0.85).
        No importa cuánto le des a los demás: mamá siempre tiene ventaja.
        </div>
        """, unsafe_allow_html=True)

    elif escenario == "❌ Error de tipeo: escribiste 'mam' sin tilde":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación por error de tipeo</strong><br><br>
        Vos escribiste <code>"mam"</code> en vez de <code>"mamá"</code>.<br><br>
        La IA <strong>no entiende</strong> que "mam" es "mamá". Como no reconoce el nombre,
        usa el <strong>promedio de internet</strong>:<br><br>
        🤖 <strong>"Yo quiero más a mi mamá"</strong><br><br>
        <strong>Resultado:</strong> la IA te dio una respuesta que no es tuya. Respondió con el promedio
        de otros miles de personas. <strong>Eso es una alucinación.</strong>
        </div>
        """, unsafe_allow_html=True)

        # Mostrar qué vio la IA
        st.markdown("""
        <div class="formula">
        Lo que la IA vio: "mam" → No lo reconoce → Usa promedio → "mamá"
        </div>
        """, unsafe_allow_html=True)

    elif escenario == "❌ Nombre inventado: 'Batman'":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación con nombre inventado</strong><br><br>
        Preguntaste por <code>"Batman"</code>, pero Batman no existe en la base de datos de la IA.<br><br>
        La IA <strong>no dice "no lo conozco"</strong>. En su lugar, <strong>inventa</strong> una respuesta
        basada en lo que aprendió de otros contextos.<br><br>
        🤖 <strong>"Yo quiero más a mi mamá"</strong> (o cualquier cosa parecida)<br><br>
        <strong>Resultado:</strong> la IA fingió saber la respuesta en vez de decir "no sé".
        <strong>Esto es una alucinación clásica.</strong>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="formula">
        Lo que la IA vio: "Batman" → No está en datos → Inventa respuesta → "mamá"
        </div>
        """, unsafe_allow_html=True)

    elif escenario == "❌ Todos los pesos en 0":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación por falta de datos</strong><br><br>
        Le diste <strong>0 a todos</strong>. La IA no tiene información tuya.<br><br>
        ¿Qué hace? <strong>No dice "no tengo datos"</strong>. Usa el promedio de internet:
        "La mayoría de la gente dice que quiere más a su mamá".<br><br>
        🤖 <strong>"Yo quiero más a mi mamá"</strong><br><br>
        <strong>Resultado:</strong> sin datos, la IA <strong>adivina</strong> con lo que aprendió de otros.
        Si vos no querés a tu mamá (o no la tenés), la IA te da una respuesta incorrecta.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="formula">
        Tu vector: [0, 0, 0, 0, 0, 0, 0, 0] → Todos dan 0 → IA usa promedio → "mamá"
        </div>
        """, unsafe_allow_html=True)

    elif escenario == "❌ Pesos contradictorios: todo en 10":
        st.markdown("""
        <div class="caja-roja">
        <strong>❌ Alucinación por datos irreales</strong><br><br>
        Le diste <strong>10 a todos</strong>. Pero nadie quiere igual a todos.<br><br>
        La IA ve que todos tienen el mismo peso y <strong>elige al primero</strong> (mamá)
        porque estadísticamente es la más común.<br><br>
        🤖 <strong>"Yo quiero más a mi mamá"</strong><br><br>
        <strong>Resultado:</strong> cuando los datos no tienen sentido, la IA <strong>inventa</strong>
        una respuesta "razonable" en vez de decir "estos datos no me sirven".
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="formula">
        Tu vector: [10, 10, 10, 10, 10, 10, 10, 10] → Todos empatados → IA elige al primero → "mamá"
        </div>
        """, unsafe_allow_html=True)

    # Resumen de alucinaciones
    st.markdown("---")
    st.subheader("📋 Tipos de alucinación")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="caja-roja">
        <strong>🔴 La IA alucina cuando:</strong><br>
        • Los datos tienen errores (typos)<br>
        • Los datos no existen (nombres inventados)<br>
        • Los datos están vacíos (todo en 0)<br>
        • Los datos no tienen sentido (todo en 10)
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="caja-verde">
        <strong>🟢 La IA acierta cuando:</strong><br>
        • Los datos son correctos<br>
        • Los datos son completos<br>
        • Los datos tienen sentido<br>
        • El problema es simple y predecible
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 5: ¿POR QUÉ GPU?
# ============================================================================
with tab5:
    st.header("5️⃣ ¿Por qué la IA necesita una GPU?")

    st.markdown("""
    <div class="caja">
    <strong>🔑 La clave:</strong> una IA como ChatGPT tiene <strong>175,000,000,000 pesos</strong>.
    No son 8 como en nuestro ejemplo. Cada respuesta necesita multiplicar todos esos pesos.
    Una GPU hace miles de cálculos al mismo tiempo. Una CPU solo hace uno por vez.
    </div>
    """, unsafe_allow_html=True)

    # Ejemplo simple
    st.subheader("📊 Ejemplo: 8 pesos × 3 opciones")

    fig_ejemplo = go.Figure()

    # Simular: 8 pesos, 3 opciones de respuesta
    opciones = ["mamá", "papá", "mascota"]
    pesos_chatgpt = np.random.uniform(0.3, 0.9, (8, 3))

    for j, op in enumerate(opciones):
        fig_ejemplo.add_trace(go.Bar(
            x=nombres, y=pesos_chatgpt[:, j],
            name=op, opacity=0.7
        ))

    fig_ejemplo.update_layout(
        barmode='group', height=300,
        yaxis_title="Peso de cada conexión",
        margin=dict(l=20, r=20, t=20, b=80),
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig_ejemplo, use_container_width=True)

    st.markdown("""
    <div class="caja">
    <strong>🔑 ¿Qué pasa aquí?</strong><br>
    Con 8 pesos y 3 opciones: <strong>8 × 3 = 24 multiplicaciones</strong>. Fácil.<br>
    Pero ChatGPT tiene <strong>175 mil millones de pesos</strong> y <strong>50,000 opciones</strong> por palabra.<br>
    Eso es: <strong>175,000,000,000 × 50,000 = 8,750,000,000,000,000 operaciones</strong>.<br>
    ¡Son <strong>8.7 mil billones</strong> de operaciones para UNA sola palabra!
    </div>
    """, unsafe_allow_html=True)

    # CPU vs GPU
    st.subheader("🎮 CPU vs GPU")

    fig_gpu = make_subplots(
        rows=1, cols=2,
        subplot_titles=["🧠 CPU: secuencial", "🎮 GPU: paralelo"],
        horizontal_spacing=0.12
    )

    np.random.seed(42)
    n = 50

    # CPU: puntos en línea
    fig_gpu.add_trace(go.Scatter(
        x=np.arange(n), y=np.ones(n),
        mode='markers', marker=dict(size=8, color='#ef4444'),
        name='CPU', showlegend=False
    ), row=1, col=1)

    # GPU: puntos en cuadrícula
    filas = 5
    cols = 10
    x_gpu = np.tile(np.arange(cols), filas)
    y_gpu = np.repeat(np.arange(filas), cols)
    fig_gpu.add_trace(go.Scatter(
        x=x_gpu, y=y_gpu,
        mode='markers', marker=dict(size=7, color='#059669'),
        name='GPU', showlegend=False
    ), row=1, col=2)

    fig_gpu.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=30))
    fig_gpu.update_xaxes(showticklabels=False, row=1, col=1)
    fig_gpu.update_xaxes(showticklabels=False, row=1, col=2)
    fig_gpu.update_yaxes(showticklabels=False, row=1, col=1)
    fig_gpu.update_yaxes(showticklabels=False, row=1, col=2)

    st.plotly_chart(fig_gpu, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="caja-roja">
        <strong>🧠 CPU</strong><br>
        • 1 cálculo a la vez<br>
        • 175 mil millones de pesos<br>
        • Tiempo: <strong>~5 años</strong>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="caja-verde">
        <strong>🎮 GPU</strong><br>
        • Miles de cálculos a la vez<br>
        • 175 mil millones de pesos<br>
        • Tiempo: <strong>~2 segundos</strong>
        </div>
        """, unsafe_allow_html=True)

    # Ejemplo numérico grande
    st.markdown("""
    <div class="caja-morada">
    <strong>📊 ¿Por qué las GPUs son caras?</strong><br><br>
    Una NVIDIA H100 (la que usan en centros de IA) cuesta <strong>~$30,000 USD</strong>.
    Las empresas de IA compran <strong>miles</strong> de ellas.<br><br>
    ¿Por qué? Porque sin GPUs, ChatGPT tardaría <strong>años</strong> en responder una sola frase.
    Con GPUs, lo hace en <strong>segundos</strong>.<br><br>
    <strong>El negocio:</strong> pagar $30,000 por GPU para que millones de personas usen la IA
    y paguen $20/mes. En 2 meses se paga sola.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 0.85rem;">
Cómo Aprende la IA — Herramienta educativa para Clase 1<br>
La IA no "sabe" — solo calcula probabilidades con pesos estadísticos
</div>
""", unsafe_allow_html=True)
