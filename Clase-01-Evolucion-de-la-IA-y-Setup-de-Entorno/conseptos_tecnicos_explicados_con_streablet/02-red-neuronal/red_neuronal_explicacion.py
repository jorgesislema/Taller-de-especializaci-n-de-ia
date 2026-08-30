import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Red Neuronal Visual", page_icon="🕸️", layout="wide")

st.markdown("""
<style>
    .titulo { font-size: 2rem; color: #1e3a8a; text-align: center; font-weight: bold; }
    .subtitulo { font-size: 1rem; color: #64748b; text-align: center; margin-bottom: 1.5rem; }
    .caja { background: #f0f9ff; border-left: 5px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; }
    .verde { background: #d1fae5; border-left: 5px solid #059669; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; }
    .rojo { background: #fee2e2; border-left: 5px solid #dc2626; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="titulo">🕸️ Red Neuronal: Una Neurona vs Varias</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Elegí un problema y mirá por qué un solo perceptrón no alcanza</p>', unsafe_allow_html=True)

# ============================================================================
# FUNCIÓN: generar datos según el problema
# ============================================================================
def generar_datos(problema, n=30):
    np.random.seed(42)
    if problema == "XOR (el clásico)":
        # 4 grupos en las esquinas
        X = np.array([[0,0],[0,1],[1,0],[1,1]] * 7, dtype=float)
        y = np.array([0,1,1,0] * 7)
        X += np.random.randn(len(X), 2) * 0.08
    elif problema == "Círculo":
        # Grupo azul adentro, rojo afuera
        angulos = np.linspace(0, 2*np.pi, n)
        interno = np.column_stack([0.3*np.cos(angulos), 0.3*np.sin(angulos)])
        externo = np.column_stack([0.8*np.cos(angulos)+0.1, 0.8*np.sin(angulos)+0.1])
        X = np.vstack([interno, externo])
        y = np.array([0]*n + [1]*n)
    elif problema == "Línea curva":
        # Separación con curva
        x1 = np.random.uniform(-1, 1, n*2)
        x2 = np.random.uniform(-1, 1, n*2)
        X = np.column_stack([x1, x2])
        y = (x2 > x1**2 + 0.1).astype(int)
    else:  # Espirales
        n = 40
        t = np.linspace(0, 4*np.pi, n)
        x1 = np.concatenate([t*np.cos(t), t*np.cos(t+np.pi)]) / 12
        x2 = np.concatenate([t*np.sin(t), t*np.sin(t+np.pi)]) / 12
        X = np.column_stack([x1, x2]) + np.random.randn(n*2, 2)*0.05
        y = np.array([0]*n + [1]*n)
    return X, y

# ============================================================================
# FUNCIÓN: entrenar red neuronal simple (2 capas)
# ============================================================================
def entrenar_red(X, y, epocas=800, tasa=2.0):
    np.random.seed(0)
    n_ocultas = 8
    W1 = np.random.randn(2, n_ocultas) * 1.5
    b1 = np.zeros(n_ocultas)
    W2 = np.random.randn(n_ocultas) * 1.5
    b2 = 0.0

    historial = []
    for epoca in range(epocas):
        # Forward
        h_raw = X @ W1 + b1
        h = np.maximum(0, h_raw)  # ReLU
        o_raw = h @ W2 + b2
        pred = 1 / (1 + np.exp(-np.clip(o_raw, -500, 500)))  # sigmoid

        # Error
        error = float(np.mean((pred - y) ** 2))
        historial.append(error)

        # Backward
        d_o = 2 * (pred - y) / len(y)
        d_W2 = h.T @ d_o
        d_b2 = np.sum(d_o)
        d_h = d_o.reshape(-1, 1) * W2.reshape(1, -1)
        d_h[h_raw <= 0] = 0  # ReLU derivada
        d_W1 = X.T @ d_h
        d_b1 = np.sum(d_h, axis=0)

        W2 -= tasa * d_W2
        b2 -= tasa * d_b2
        W1 -= tasa * d_W1
        b1 -= tasa * d_b1

    return W1, b1, W2, b2, historial

def predecir(X, W1, b1, W2, b2):
    h = np.maximum(0, X @ W1 + b1)
    o = h @ W2 + b2
    return 1 / (1 + np.exp(-np.clip(o, -500, 500)))

# ============================================================================
# FUNCIÓN: graficar frontera
# ============================================================================
def graficar_frontera(X, y, titulos, predicciones=None, rango=(-1.5, 2.5)):
    fig = make_subplots(rows=1, cols=len(titulos),
                        subplot_titles=titulos,
                        horizontal_spacing=0.08)

    xx, yy = np.meshgrid(np.linspace(rango[0], rango[1], 200),
                         np.linspace(rango[0], rango[1], 200))
    puntos = np.c_[xx.ravel(), yy.ravel()]

    for i, titulo in enumerate(titulos):
        if predicciones is not None and i < len(predicciones):
            z = predicciones[i](puntos).reshape(xx.shape)
            fig.add_trace(go.Contour(
                x=np.linspace(rango[0], rango[1], 200),
                y=np.linspace(rango[0], rango[1], 200),
                z=z,
                colorscale=[[0, '#dbeafe'], [0.5, '#f5f5f5'], [1, '#fecaca']],
                showscale=False, opacity=0.6, showlegend=False
            ), row=1, col=i+1)

        # Puntos reales
        for clase, color, nombre in [(0, '#3b82f6', 'Clase 0'), (1, '#ef4444', 'Clase 1')]:
            mask = y == clase
            fig.add_trace(go.Scatter(
                x=X[mask, 0], y=X[mask, 1],
                mode='markers',
                marker=dict(size=8, color=color, line=dict(width=1, color='white')),
                name=nombre, showlegend=(i == 0)
            ), row=1, col=i+1)

    fig.update_layout(height=420, margin=dict(l=20, r=20, t=50, b=20))
    for i in range(1, len(titulos)+1):
        fig.update_xaxes(range=[rango[0], rango[1]], row=1, col=i, showticklabels=False)
        fig.update_yaxes(range=[rango[0], rango[1]], row=1, col=i, showticklabels=False)
    return fig

# ============================================================================
# INTERFAZ PRINCIPAL
# ============================================================================

# 1. Elegir problema
problema = st.selectbox(
    "📋 Elegí un problema:",
    ["XOR (el clásico)", "Círculo", "Línea curva", "Espirales"]
)

# Descripción del problema
desc = {
    "XOR (el clásico)": "Los puntos rojos y azules están mezclados en las esquinas. Ninguna línea recta los separa.",
    "Círculo": "Un grupo adentro, otro afuera. Necesitás una frontera circular, no recta.",
    "Línea curva": "La separación sigue una curva parabólica. Una línea recta falla.",
    "Espirales": "Dos espirales entrelazadas. El problema más difícil para un perceptrón."
}
st.info(desc[problema])

# 2. Generar datos
X, y = generar_datos(problema)

# 3. Entrenar red neuronal
if st.button("▶️ Entrenar la Red Neuronal", type="primary"):
    with st.spinner("Entrenando..."):
        W1, b1, W2, b2, historial = entrenar_red(X, y)
        pred_red = lambda pts: predecir(pts, W1, b1, W2, b2)

    # 4. Mostrar resultados lado a lado
    st.markdown("---")

    # Perceptrón simple: ajustar una línea recta con regresión logística
    from numpy.linalg import lstsq
    X_aug = np.column_stack([X, np.ones(len(X))])
    w_lin, _, _, _ = lstsq(X_aug, y, rcond=None)
    pred_perceptron = lambda pts: 1 / (1 + np.exp(-np.clip(
        np.column_stack([pts, np.ones(len(pts))]) @ w_lin, -500, 500)))

    fig = graficar_frontera(
        X, y,
        ["❌ Un Perceptrón (solo recta)", "✅ Red Neuronal (frontera curva)"],
        [pred_perceptron, pred_red]
    )
    st.plotly_chart(fig, use_container_width=True)

    # Explicación
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="rojo">
        <strong>❌ Perceptrón</strong><br>
        Solo puede trazar una <strong>línea recta</strong>.
        Mire cómo intenta separar los puntos pero siempre falla
        ensome zonas.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="verde">
        <strong>✅ Red Neuronal</strong><br>
        Tiene <strong>neuronas ocultas</strong> que crean fronteras
        <strong>curvas y complejas</strong>. Separa los puntos correctamente.
        </div>
        """, unsafe_allow_html=True)

    # Curva de aprendizaje
    st.subheader("📉 La Red Aprendió (Error vs Tiempo)")
    fig_err = go.Figure()
    fig_err.add_trace(go.Scatter(y=historial, mode='lines', line=dict(color='#1e3a8a', width=2)))
    fig_err.update_layout(
        xaxis_title="Iteraciones", yaxis_title="Error",
        height=280, margin=dict(l=40, r=20, t=20, b=40)
    )
    st.plotly_chart(fig_err, use_container_width=True)

    st.markdown("""
    <div class="caja">
    <strong>🔑 ¿Qué pasó?</strong><br>
    Al principio, la red se equivocaba mucho (error alto). Con cada iteración,
    ajustó sus pesos internos y el error bajó. La frontera pasó de ser una
    línea recta a una curva que separa correctamente los puntos.
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("---")
    st.markdown("### 👆 Dale a **Entrenar** para ver la magia")

    # Mostrar solo los datos sin entrenar
    fig = graficar_frontera(X, y, ["Datos del Problema"])
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 0.85rem;">
Red Neuronal Visual — Herramienta educativa para Clase 1<br>
Un perceptrón = línea recta · Una red neuronal = frontera curva
</div>
""", unsafe_allow_html=True)
