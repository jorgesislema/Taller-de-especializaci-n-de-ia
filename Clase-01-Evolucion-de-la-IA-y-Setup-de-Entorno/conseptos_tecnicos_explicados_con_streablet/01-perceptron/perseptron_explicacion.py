import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="El Perceptrón: La Neurona que Aprende",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
    .titulo-principal {
        font-size: 2.2rem;
        color: #1e3a8a;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitulo {
        font-size: 1.1rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .explicacion {
        background-color: #f0f9ff;
        border-left: 5px solid #3b82f6;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        font-size: 1.05rem;
    }
    .paso {
        background-color: #fefce8;
        border-left: 5px solid #eab308;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .resultado-culpable {
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        border: 3px solid #dc2626;
        color: #991b1b;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .resultado-inocente {
        background: linear-gradient(135deg, #d1fae5, #a7f3d0);
        border: 3px solid #059669;
        color: #065f46;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .formula {
        background-color: #1e293b;
        color: #e2e8f0;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        text-align: center;
        margin: 1rem 0;
    }
    .dato-clave {
        background-color: #faf5ff;
        border-left: 5px solid #9333ea;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="titulo-principal">🧠 El Perceptrón: La Neurona que Aprende</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Interactuá con una neurona artificial y entendé cómo toma decisiones</p>', unsafe_allow_html=True)

tab_teoria, tab_practica = st.tabs(["📚 Qué es el Perceptrón", "⚖️ Jurado Interactivo"])

# ============================================================================
# TAB 1: TEORÍA
# ============================================================================
with tab_teoria:
    st.header("¿Qué es un Perceptrón?")

    st.markdown("""
    <div class="explicacion">
    El <strong>perceptrón</strong> es la neurona artificial más simple que existe. Fue inventado por
    <strong>Frank Rosenblatt en 1957</strong> y es la pieza fundamental de toda la inteligencia artificial moderna.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("La analogía del Jurado")

    st.markdown("""
    Imaginá que sos un **jurado** en un juicio. Tenés que decidir si alguien es **culpable** o **inocente**.

    Para tomar esa decisión, escuchás **8 tipos de evidencia**. Cada tipo de evidencia tiene un **peso**
    (cuánta importancia le das). Tu trabajo es:

    1. Recibir cada evidencia
    2. Multiplicarla por su peso
    3. Sumar todo
    4. Si la suma supera un umbral → **CULPABLE**
    5. Si no lo supera → **INOCENTE**
    """, unsafe_allow_html=True)

    st.subheader("Las 3 piezas del perceptrón")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **📥 Entradas (Inputs)**
        Son los datos que le llegan a la neurona.
        En nuestro jurado: los 8 tipos de evidencia.

        Cada evidencia tiene un valor del **0 al 10**.
        """)

    with col2:
        st.markdown("""
        **⚖️ Pesos (Weights)**
        Cuánta importancia le da a cada evidencia.
        Un peso **positivo** = incrimina.
        Un peso **negativo** = exculpa (defiende).

        Los pesos son los que la IA **aprende**.
        """)

    with col3:
        st.markdown("""
        **📤 Salida (Output)**
        El veredicto final.
        El perceptrón **suma todo** y compara con un umbral.

        Si la suma pasa el umbral → 1 (culpable).
        Si no → 0 (inocente).
        """)

    st.subheader("La fórmula matemática (simplificada)")

    st.markdown("""
    <div class="formula">
    Salida = (Evidencia₁ × Peso₁) + (Evidencia₂ × Peso₂) + ... + (Evidencia₈ × Peso₈)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="paso">
    <strong>Ejemplo rápido:</strong><br>
    Evidencia física = 8, Peso = 5 → Contribución: 8 × 5 = <strong>40</strong><br>
    Testigos = 3, Peso = 2 → Contribución: 3 × 2 = <strong>6</strong><br>
    Coartada = 9, Peso = -4 → Contribución: 9 × (-4) = <strong>-36</strong> (exculpa)<br><br>
    <strong>Suma total:</strong> 40 + 6 + (-36) = <strong>10</strong>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("¿Por qué importa?")

    st.markdown("""
    <div class="dato-clave">
    <strong>Dato clave:</strong> El perceptrón no "piensa". No sabe qué es un juicio. Solo hace <strong>cuentas</strong>.
    Multiplica, suma y compara. Eso es todo lo que hace una neurona artificial.<br><br>
    Pero cuando juntás <strong>miles de neuronas</strong> conectadas entre sí (redes neuronales),
    podés crear sistemas que reconocen caras, traducen idiomas y escriben textos.
    Todo empieza con esta cuentita simple.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("El problema del perceptrón simple")

    st.markdown("""
    El perceptrón original solo puede separar datos con una **línea recta**. Funciona para decisiones simples:

    - ✅ Si tengo evidencia Y testigos → culpable
    - ✅ Si tengo coartada SOLA → inocente
    - ❌ Pero NO puede aprender cosas como: "culpable SI tiene evidencia O tiene testigos, pero NO si tiene coartada"

    Para resolver esto, se apilan **múltiples capas** de perceptrones (redes neuronales profundas).
    """, unsafe_allow_html=True)

# ============================================================================
# TAB 2: PRÁCTICA INTERACTIVA
# ============================================================================
with tab_practica:
    st.header("⚖️ Jurado Interactivo")

    st.markdown("""
    <div class="explicacion">
    Ajustá la intensidad de cada evidencia y los pesos del jurado. Observá cómo cambia
    el veredicto en tiempo real. Este es exactamente el mecanismo que usa una neurona artificial.
    </div>
    """, unsafe_allow_html=True)

    # Definir factores
    factores = {
        "📹 Evidencia física": {"peso_defecto": 5, "descripcion": "Huellas, objetos, pruebas directas"},
        "👥 Testigos presenciales": {"peso_defecto": 3, "descripcion": "Personas que vieron los hechos"},
        "🕐 Coartada sólida": {"peso_defecto": -6, "descripcion": "Prueba de que NO estaba en el lugar"},
        "💰 Motivo financiero": {"peso_defecto": 4, "descripcion": "Beneficio económico del acusado"},
        "🧬 Pruebas de ADN": {"peso_defecto": 6, "descripcion": "Match genético con la escena"},
        "📹 Cámaras de seguridad": {"peso_defecto": 5, "descripcion": "Grabaciones del momento"},
        "📱 Ubicación celular": {"peso_defecto": 4, "descripcion": "GPS del teléfono del acusado"},
        "🔍 Huellas dactilares": {"peso_defecto": 3, "descripcion": "Huellas en la escena del crimen"},
    }

    # Escenarios predefinidos
    escenario = st.selectbox(
        "📋 Elegí un escenario o personalizá el tuyo:",
        ["🎭 Personalizado", "🔴 Robo con evidencia abrumadora", "🟢 Robo sin pruebas", "🟡 Caso dudoso", "💔 Crimen pasional"]
    )

    if escenario == "🔴 Robo con evidencia abrumadora":
        valores = {"📹 Evidencia física": 9, "👥 Testigos presenciales": 8, "🕐 Coartada sólida": 1,
                   "💰 Motivo financiero": 7, "🧬 Pruebas de ADN": 9, "📹 Cámaras de seguridad": 8,
                   "📱 Ubicación celular": 7, "🔍 Huellas dactilares": 8}
    elif escenario == "🟢 Robo sin pruebas":
        valores = {"📹 Evidencia física": 2, "👥 Testigos presenciales": 1, "🕐 Coartada sólida": 9,
                   "💰 Motivo financiero": 3, "🧬 Pruebas de ADN": 1, "📹 Cámaras de seguridad": 2,
                   "📱 Ubicación celular": 2, "🔍 Huellas dactilares": 1}
    elif escenario == "🟡 Caso dudoso":
        valores = {"📹 Evidencia física": 5, "👥 Testigos presenciales": 4, "🕐 Coartada sólida": 4,
                   "💰 Motivo financiero": 5, "🧬 Pruebas de ADN": 5, "📹 Cámaras de seguridad": 4,
                   "📱 Ubicación celular": 5, "🔍 Huellas dactilares": 4}
    elif escenario == "💔 Crimen pasional":
        valores = {"📹 Evidencia física": 7, "👥 Testigos presenciales": 5, "🕐 Coartada sólida": 2,
                   "💰 Motivo financiero": 8, "🧬 Pruebas de ADN": 7, "📹 Cámaras de seguridad": 3,
                   "📱 Ubicación celular": 6, "🔍 Huellas dactilares": 6}
    else:
        valores = {f: 5 for f in factores}

    # --- INTERFAZ DE ENTRADAS ---
    col_entradas, col_pesos = st.columns(2)

    entradas = {}
    pesos = {}

    with col_entradas:
        st.subheader("📥 Evidencia (Entradas)")
        st.caption("Del 0 (nada) al 10 (máxima evidencia)")
        for factor, info in factores.items():
            entradas[factor] = st.slider(
                f"{factor}",
                min_value=0, max_value=10, value=valores[factor],
                help=info["descripcion"],
                key=f"ent_{factor}"
            )

    with col_pesos:
        st.subheader("⚖️ Pesos del Jurado")
        st.caption("Positivo = incrimina · Negativo = defiende")
        for factor, info in factores.items():
            pesos[factor] = st.slider(
                f"Peso: {factor}",
                min_value=-10, max_value=10, value=info["peso_defecto"],
                key=f"pes_{factor}"
            )

    # --- PROCESO DEL PERCEPTRÓN ---
    st.markdown("---")
    st.header("🧮 Proceso de Decisión (Paso a paso)")

    # Paso 1: Calcular contribuciones
    st.subheader("Paso 1: Multiplicar cada evidencia por su peso")

    contribuciones = {}
    datos_tabla = []
    for factor in factores:
        contrib = entradas[factor] * pesos[factor]
        contribuciones[factor] = contrib
        signo = "+" if contrib >= 0 else ""
        datos_tabla.append({
            "Evidencia": factor,
            "Valor": entradas[factor],
            "×": "×",
            "Peso": pesos[factor],
            "=": "=",
            "Contribución": f"{signo}{contrib:.0f}"
        })

    st.dataframe(datos_tabla, use_container_width=True, hide_index=True)

    # Paso 2: Suma total
    st.subheader("Paso 2: Sumar todas las contribuciones")

    suma_total = sum(contribuciones.values())

    col_formula, col_suma = st.columns([3, 1])

    with col_formula:
        partes = []
        for factor in factores:
            c = contribuciones[factor]
            partes.append(f"({c:+.0f})")
        formula_texto = " + ".join(partes)
        st.markdown(f"""
        <div class="formula">
        Suma = {formula_texto}<br><br>
        Suma = {suma_total:+.0f}
        </div>
        """, unsafe_allow_html=True)

    with col_suma:
        if suma_total > 0:
            st.metric("Suma Total", f"{suma_total:+.0f}", delta="Inclina hacia culpable", delta_color="inverse")
        elif suma_total < 0:
            st.metric("Suma Total", f"{suma_total:+.0f}", delta="Inclina hacia inocente", delta_color="normal")
        else:
            st.metric("Suma Total", f"{suma_total:+.0f}", delta="Neutral")

    # Paso 3: Función de activación
    st.subheader("Paso 3: Función de activación (el umbral)")

    st.markdown("""
    <div class="explicacion">
    La <strong>función de activación</strong> decide si la neurona se "enciende" o no.
    Es como un interruptor: si la suma pasa cierto umbral, la neurona responde "SÍ" (1).
    Si no, responde "NO" (0).
    </div>
    """, unsafe_allow_html=True)

    umbral = st.slider(
        "📍 Umbral de decisión",
        min_value=-50, max_value=50, value=0, step=5,
        help="Si la suma supera este valor → culpable. Si no → inocente."
    )

    culpable = suma_total > umbral

    # Paso 4: Veredicto
    st.subheader("Paso 4: Veredicto final")

    if culpable:
        st.markdown(f"""
        <div class="resultado-culpable">
        🔴 VEREDICTO: CULPABLE<br>
        <span style="font-size: 1.2rem;">Suma ({suma_total:+.0f}) {'>' if suma_total > umbral else '≤'} Umbral ({umbral})</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="resultado-inocente">
        🟢 VEREDICTO: INOCENTE<br>
        <span style="font-size: 1.2rem;">Suma ({suma_total:+.0f}) {'≤' if suma_total <= umbral else '>'} Umbral ({umbral})</span>
        </div>
        """, unsafe_allow_html=True)

    # --- VISUALIZACIÓN DE LA NEURONA ---
    st.markdown("---")
    st.header("🧠 Visualización de la Neurona")

    st.markdown("""
    <div class="explicacion">
    Esta gráfica muestra cómo los datos fluyen desde las entradas hasta la decisión final.
    Las líneas <span style="color: green;">verdes</span> son pesos positivos (incriminan).
    Las líneas <span style="color: red;">rojas</span> son pesos negativos (defienden).
    El grosor indica la importancia del peso.
    </div>
    """, unsafe_allow_html=True)

    fig = go.Figure()

    n = len(factores)
    angulos = np.linspace(0, 2 * np.pi, n, endpoint=False)

    for i, (factor, peso) in enumerate(pesos.items()):
        x = 3 * np.cos(angulos[i])
        y = 3 * np.sin(angulos[i])

        color_linea = "green" if peso >= 0 else "red"
        grosor = max(abs(peso) * 0.5, 1)

        valor = entradas[factor]
        color_nodo = f"rgba(59, 130, 246, {0.3 + valor / 14})"
        tamano_nodo = 12 + valor * 2

        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=tamano_nodo, color=color_nodo, line=dict(width=1, color='white')),
            text=[f"<b>{factor.split()[0]}</b><br>{valor}×{peso:+.0f}"],
            textposition='top center',
            textfont=dict(size=10),
            hoverinfo='text',
            hovertext=f"{factor}<br>Valor: {valor}<br>Peso: {peso:+.0f}<br>Contribución: {contribuciones[factor]:+.0f}",
            showlegend=False
        ))

        fig.add_trace(go.Scatter(
            x=[x, 0], y=[y, 0],
            mode='lines',
            line=dict(width=grosor, color=color_linea),
            hoverinfo='skip',
            showlegend=False
        ))

    color_centro = "#dc2626" if culpable else "#059669"
    texto_centro = "1<br>CULPABLE" if culpable else "0<br>INOCENTE"

    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers+text',
        marker=dict(size=40, color=color_centro, line=dict(width=2, color='white')),
        text=[f"<b>Σ</b><br>{suma_total:+.0f}<br>{texto_centro}"],
        textposition='middle center',
        textfont=dict(size=11, color='white'),
        hoverinfo='text',
        hovertext=f"Suma total: {suma_total:+.0f}<br>Umbral: {umbral}<br>Veredicto: {'CULPABLE' if culpable else 'INOCENTE'}",
        showlegend=False
    ))

    fig.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-5, 5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-5, 5]),
        plot_bgcolor='white',
        height=550,
        margin=dict(l=20, r=20, t=40, b=20),
        title=dict(text="Diagrama de la Neurona Perceptrón", font=dict(size=16))
    )

    st.plotly_chart(fig, use_container_width=True)

    # --- RESUMEN DE CONTRIBUCIONES ---
    st.subheader("📊 ¿Qué faktor influyó más?")

    contrib_ordenadas = sorted(contribuciones.items(), key=lambda x: abs(x[1]), reverse=True)

    factores_nombres = [c[0] for c in contrib_ordenadas]
    factores_valores = [c[1] for c in contrib_ordenadas]
    factores_colores = ["green" if v >= 0 else "red" for v in factores_valores]

    fig_bar = go.Figure(go.Bar(
        x=factores_valores,
        y=factores_nombres,
        orientation='h',
        marker_color=factores_colores,
        text=[f"{v:+.0f}" for v in factores_valores],
        textposition='outside'
    ))

    fig_bar.update_layout(
        xaxis_title="Contribución",
        yaxis=dict(autorange="reversed"),
        height=400,
        margin=dict(l=200, r=20, t=20, b=40),
        xaxis=dict(zeroline=True, zerolinecolor='gray', zerolinewidth=2)
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    # --- EXPLICACIÓN AUTOMÁTICA ---
    st.markdown("---")
    st.header("📝 Explicación del Jurado IA")

    top_positivo = max(contribuciones.items(), key=lambda x: x[1] if x[1] > 0 else -999)
    top_negativo = min(contribuciones.items(), key=lambda x: x[1] if x[1] < 0 else 999)

    if culpable:
        st.markdown(f"""
        <div class="explicacion">
        <strong>¿Por qué es culpable?</strong><br><br>
        La evidencia con mayor peso a favor de la culpabilidad fue <strong>{top_positivo[0]}</strong>
        con una contribución de <strong>{top_positivo[1]:+.0f}</strong> puntos.<br><br>
        La suma total de <strong>{suma_total:+.0f}</strong> superó el umbral de <strong>{umbral}</strong>,
        por lo tanto el jurado dictamina <strong>CULPABLE</strong>.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="explicacion">
        <strong>¿Por qué es inocente?</strong><br><br>
        {'La coartada fue clave: ' + top_negativo[0] + ' restó ' + str(abs(top_negativo[1])) + ' puntos.' if top_negativo[1] < 0 else 'No hay evidencia suficiente para superar el umbral.'}<br><br>
        La suma total de <strong>{suma_total:+.0f}</strong> no superó el umbral de <strong>{umbral}</strong>,
        por lo tanto el jurado dictamina <strong>INOCENTE</strong>.
        </div>
        """, unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #94a3b8; font-size: 0.9rem; padding: 1rem;">
    <strong>El Perceptrón</strong> — Herramienta educativa para entender neurona artificial<br>
    Concepto explicado: multiplicación ponderada + función de activación<br>
    Inspirado en el modelo de Rosenblatt (1957)
    </div>
    """, unsafe_allow_html=True)
