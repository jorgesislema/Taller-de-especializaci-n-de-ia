# Ingenieria de Prompt — Resumen del Taller

> Resumen extraido del [repositorio completo de ingenieria de prompt](https://github.com/jorgesislema/apuntes_de_ingenieria_de_prompt).
> Si queres profundizar, ahi estan los 16 modulos completos. Esto es lo esencial para arrancar.

---

## 1. Que es un prompt (en serio)

Un **prompt** es la instruccion que le das a la IA. Todo lo que escribis antes de presionar Enter.

La IA no "entiende" tu prompt como lo haria una persona. Lo que hace es buscar, en su enorme arbol de probabilidades, cual es la secuencia de palabras mas probable para responder.

**Analogia:** Es como hablarle a alguien que habla tu idioma pero recien llego al pais. Entiende las palabras, pero no el contexto cultural, no el tono implicito, no "lo que no dijiste". Cuanto mas explicito seas, mejor resultado obtenes.

> **Regla de oro:** La calidad de la respuesta es proporcional a la calidad del prompt. Prompt vago = respuesta vaga. Prompt preciso = respuesta precisa.

---

## 2. Los 5 elementos de un buen prompt

Todo prompt efectivo puede tener hasta 5 componentes. No todos son obligatorios siempre.

| Elemento | Que es | Obligatorio | Ejemplo |
|----------|--------|-------------|---------|
| **Rol** | Que personaje o experto queres que sea la IA | Recomendado | "Eres un diseñador senior con 15 años de experiencia" |
| **Contexto** | La situacion, quien sos vos | Muy recomendado | "Soy estudiante del taller de IA, armando mi portfolio" |
| **Tarea** | Que queres que haga, con verbo concreto | **SI, siempre** | "Redacta / Genera / Explica / Analiza / Lista" |
| **Restricciones** | Limites: formato, tono, longitud | Recomendado | "Maximo 200 palabras, tono profesional, en español" |
| **Ejemplo** | Muestra del output esperado | Opcional pero muy util | "Aca hay un ejemplo de como quiero que se vea..." |

### Verbos de tarea mas utiles

| Si queres... | Usa este verbo |
|-------------|----------------|
| Un texto nuevo | **Redacta / Escribi / Crea** |
| Explicar algo complejo | **Explica como si tuviera 12 años** |
| Un listado | **Lista / Enumera / Dame 5 opciones** |
| Analizar | **Analiza / Evalua / Identifica puntos clave** |
| Resumir | **Resumi en X parrafos** |
| Mejorar algo escrito | **Mejora / Revisa / Reescribi** |
| Traducir | **Traduci al [idioma] manteniendo el tono** |
| Comparar | **Compara A vs B en una tabla** |
| Dar pasos | **Explica paso a paso como...** |

---

## 3. Los 4 tipos de prompting

| Tipo | Como funciona | Cuando usarlo |
|------|---------------|---------------|
| **Zero-shot** | Le pedis sin ejemplos previos | Tareas simples y directas |
| **One-shot** | Un ejemplo, despues tu consulta | Queres un formato especifico |
| **Few-shot** | Varios ejemplos (3+), despues tu consulta | Clasificacion, formatos fijos |
| **Chain of Thought** | Le pedis que muestre su razonamiento paso a paso | Matematicas, logica, decisiones |

### Ejemplo de Zero-shot
```
Resumi en 3 puntos el concepto de inteligencia artificial.
```

### Ejemplo de One-shot
```
Clasifica comentarios como POSITIVO, NEGATIVO o NEUTRO.

Ejemplo:
Comentario: "El producto llego roto"
Clasificacion: NEGATIVO

Ahora clasifica:
Comentario: "El servicio fue rapido pero el empaque daniado"
Clasificacion:
```

### Ejemplo de Chain of Thought
```
Resolve este problema paso a paso, mostrando cada razonamiento:
Si tengo 24 manzanas y reparto 1/3 entre 4 amigos,
cuantas manzanas le toca a cada uno?
```

**Analogia de los 4 tipos:**
- Zero-shot: "Cantame una cancion triste" (sin mostrarte ninguna)
- One-shot: Te muestro UNA foto de como doblar remeras → "todas igual"
- Few-shot: Te muestro 5 empanadas → "asi las quiero"
- Chain of Thought: "Explicame la receta mientras cocinas"

---

## 4. La plantilla Smarkdown

Smarkdown = Structured Markdown. Es escribir prompts usando sintaxis Markdown.

Copiala, edita lo que necesites, borra lo que no uses:

```markdown
## Rol
Eres [profesion/personaje] con [X años] de experiencia en [area].

## Contexto
[Situacion. Quien sos vos. Que problema estas resolviendo.]

## Tarea
[Verbo concreto + que + para que/para quien]

## Restricciones
- Formato: [parrafo / lista / tabla / codigo]
- Tono: [formal / informal / simple / tecnico]
- Longitud: [maximo X palabras / X parrafos]
- No incluir: [X, Y, Z]
- Idioma: [español]

## Ejemplo de output esperado
[Opcional: muestra del formato que queres]
```

> **Por que Markdown funciona mejor:** La IA fue entrenada con millones de documentos en Markdown (GitHub, documentacion tecnica, tutorials). Cuando estructuras tu prompt con `##`, `-`, `|`, la IA reconoce el patron y responde con mas precision.

---

## 5. Agentes: la IA con personalidad definida

Un **agente** es una IA a la que le asignas un rol fijo y una serie de instrucciones que sigue siempre. No es magia: es un system prompt que se mantiene "pegado" a cada conversacion.

### Componentes de un agente

```
┌─────────────────────────────────────────────┐
│                  AGENTE                      │
├─────────────────────────────────────────────┤
│  1. ROL FIJO — siempre el mismo personaje    │
│  2. INSTRUCCIONES — que debe hacer siempre   │
│  3. PERSONALIDAD — tono, estilo, voz         │
│  4. LIMITES — que NO debe hacer nunca         │
│  5. SKILLS — herramientas/capacidades extra  │
│  6. KNOWLEDGE — archivos o datos que "sabe"  │
└─────────────────────────────────────────────┘
```

**Analogia:** Un agente es como un empleado con un manual de procedimientos. No importa quien le hable: responde segun el manual.

### La estructura universal de un agente

```markdown
## Rol
Eres [profesion/personaje] con [X años] de experiencia en [area].

## Contexto
Tus usuarios son [descripcion]. El objetivo es [objetivo].

## Tarea principal
- [Tarea 1]
- [Tarea 2]

## Reglas y restricciones
- [Regla 1]
- [Lo que NUNCA debe hacer]

## Formato de respuesta
[Tono, estructura, longitud esperada]

## Skills / Herramientas
- [Herramienta 1]
- [Herramienta 2]
```

> **Tip del ingeniero:** El system prompt de un agente es el 80% de su utilidad. Dedicale tiempo. Un agente con malas instrucciones es peor que ningun agente.

---

## 6. Skills: las herramientas del agente

Las **skills** son capacidades extra que le das a un agente para que haga cosas que normalmente no haria:

| Skill | Que le permite hacer | Ejemplo de uso |
|-------|---------------------|----------------|
| Busqueda web | Acceder a informacion actualizada | "Busca el precio del dolar hoy" |
| Leer archivos | Analizar PDFs, Excels, imagenes | "Resumi este PDF de 50 paginas" |
| Ejecutar codigo | Correr Python, calculos complejos | "Analiza este dataset y grafica los resultados" |
| APIs | Consultar servicios externos | "Busca vuelos a Mendoza para el finde" |
| Generar imagenes | Crear ilustraciones, diagramas | "Dibuja un diagrama de flujo de este proceso" |

**Analogia:** Las skills son las herramientas del cinturon de Batman. El agente es Batman. Las skills son el batarang, la pistola de garfio, la capa. Sin skills, es solo un tipo disfrazado.

---

## 7. Loops: cuando el agente trabaja en ciclos

Un **loop** (bucle) es el ciclo de: pensar → actuar → observar → pensar otra vez... hasta completar la tarea.

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  PENSAR  │ ──→ │  ACTUAR  │ ──→ │ OBSERVAR │
│ (que     │     │ (ejecutar│     │ (leer el  │
│  hago?)  │ ←── │  accion) │ ←── │ resultado)│
└──────────┘     └──────────┘     └──────────┘
      ↑                                  │
      └────────── REPETIR ──────────────┘
```

### Ejemplo concreto

Le pedis a un agente: "busca vuelos baratos a Mendoza para el finde largo".

1. **Piensa:** "Necesito buscar en 3 aerolineas, comparar precios"
2. **Actua:** Llama a la API de Aerolineas Argentinas
3. **Observa:** $15,000, sale 18:30
4. **Piensa:** "Falta consultar FlyBondi y JetSmart"
5. **Actua:** Llama a las otras APIs
6. **Observa:** Ya tiene los 3 precios
7. **Piensa:** "La mas barata es JetSmart a $12,000"
8. **Accion final:** Te entrega el resultado con comparativa

### Por que importan los loops

| Sin loop | Con loop |
|----------|----------|
| 1 solo paso (A → B) | Varios pasos (A → B → C → D) |
| Bueno para tareas simples | Necesario para tareas complejas |
| Menos tokens, mas barato | Mas tokens, mas caro, mejor resultado |
| ChatGPT gratuito | Agentes con herramientas |

**Analogia:** Es como armar un rompecabezas. Sin loop, miras la caja una vez y tiras todas las piezas juntas. Con loop, probas una pieza, ves si encaja, ajustas, probas otra. Es mas lento pero el resultado es mejor.

> **Dato clave de la Clase 3:** Los loops consumen mas tokens. Cada vuelta del ciclo suma tokens a tu factura. Por eso los agentes con loops suelen estar en planes de pago.

---

## 8. Errores comunes al hacer prompts

### Error 1: El prompt vago
```
MAL:  "Explicame la IA"
BIEN: "Explica en 3 parrafos que es un LLM para alguien sin
       conocimientos tecnicos, usando una analogia cotidiana"
```

### Error 2: Pedir todo de una
```
MAL:  "Haceme un plan de negocio completo con FODA, finanzas,
       marketing y operaciones" → todo superficial

BIEN: Prompt 1: "Genera el FODA"
      Prompt 2: "Basado en el FODA, genera estrategia de marketing"
      Prompt 3: "Para la estrategia 2, desarrolla el plan operativo"
```

### Error 3: No dar contexto
```
MAL:  "Revisa este email y mejoralo" (sin contexto)

BIEN: "Revisa este email de solicitud de trabajo para el puesto X
       en una empresa del sector Y. Tono profesional pero no robotico.
       El destinatario es el jefe de RRHH."
```

### Error 4: No iterar
```
El 90% de la gente: Prompt → No le gusta → Abandona.

El ingeniero: Prompt → Resultado → "Mejora X" → Resultado 2 →
"Ajusta Y" → Resultado 3 → LISTO.
```

### Error 5: Creer que "mas largo = mejor"
Un prompt de 500 palabras sin estructura es peor que uno de 100 palabras con Smarkdown. La clave es **precision**, no extension.

---

## 9. Checklist antes y despues de cada prompt

### ANTES de enviar
- [ ] Tiene al menos Tarea + Restricciones?
- [ ] Use mi AlterEgo? (sin datos personales reales)
- [ ] Si esto se publica mañana en un diario, estaria bien?

### DESPUES de recibir
- [ ] Lei la respuesta completa (no solo el primer parrafo)?
- [ ] Verifique numeros, fechas y citas clave?
- [ ] Edite y personalice antes de usar?
- [ ] Podria defender este contenido si alguien me pregunta de donde salio?

---

## 10. Parametros que controlan la creatividad

Si usas la API directamente (OpenAI, Anthropic, Gemini) en vez del chat web, tenes acceso a parametros que cambian radicalmente el comportamiento del modelo. Son el equivalente a los "knobs" de un sintetizador: no son magia, son matematicas.

### Los 7 parametros esenciales

| Parametro | Rango | Que hace | Cuando ajustarlo |
|-----------|-------|----------|-----------------|
| `temperature` | 0.0 – 2.0 | Escala la aleatoriedad: 0 = deterministico, 2 = caotico | 0 para codigo/facturas/extraccion. 0.7–1.0 para creatividad. **Nunca uses temperature y top_p juntos.** |
| `top_p` | 0.0 – 1.0 | Nucleus sampling: solo considera tokens cuya probabilidad acumulada llega a X% | Alternativa a temperature. 0.1 = muy predecible, 0.9 = diverso |
| `frequency_penalty` | -2.0 – 2.0 | Penaliza tokens que ya aparecieron (reduce repeticion) | >0 cuando la IA se repite en loops largos |
| `presence_penalty` | -2.0 – 2.0 | Penaliza tokens ya usados aunque sea una sola vez | >0 para forzar diversidad tematica |
| `max_tokens` | 1 – limite modelo | Corta la respuesta a X tokens de output | Controlar costo. Recorda: output tokens tambien se facturan (Clase 3) |
| `stop` | strings | Detiene la generacion al encontrar la secuencia | Limpiar outputs: `stop=["\n", "###"]` para respuestas breves |
| `logit_bias` | -100 a 100 | Fuerza o prohibe tokens especificos por ID | Evitar palabras prohibidas, forzar formato JSON, sesgar vocabulario |

### Formula practica: el "triangulo de sampling"

```
¿Que estoy generando?
├── Codigo / Datos estructurados → temperature=0, top_p=N/A
├── Texto creativo (marketing, guiones) → temperature=0.7, frequency_penalty=0.3
├── Brainstorming / Ideacion → temperature=1.0, presence_penalty=0.5
└── Respuestas factuales (QA, soporte) → temperature=0.2, top_p=0.3
```

### Anti-Patron #1: Subir temperature para "arreglar" un mal prompt

```python
# MAL: El prompt es vago, subis temperature esperando magia
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "escribime algo lindo"}],
    temperature=1.8  # La IA va a delirar, no a "inspirarse"
)

# BIEN: Mejoras el prompt primero, ajustas parametros despues
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": """Escribi un poema de 4 versos
    sobre un programador que debuggea a las 3 AM.
    Tono: melancolico pero con humor. Rima consonante."""}],
    temperature=0.8,
    frequency_penalty=0.2
)
```

### Anti-Patron #2: Usar temperature y top_p simultaneamente

La documentacion de OpenAI lo dice explicito: **generalmente no combines temperature con top_p**. Son dos formas distintas de controlar el sampling. Usar ambas es como ponerle dos termostatos al mismo ambiente: generas comportamiento impredecible.

> **Regla practica:** Elegi uno. Temperature es mas intuitivo para empezar. Top_p te da mas control fino cuando sabes exactamente que distribucion de tokens queres.

### Ejemplo: forzar formato de salida con logit_bias

```python
# Fuerza a la IA a empezar la respuesta con "{" (token ID 123... varía por modelo)
# Util para garantizar output JSON sin tener que pedirlo en el prompt 50 veces
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Clasifica este texto como POSITIVO, NEGATIVO o NEUTRO."}],
    logit_bias={12345: 100},  # +100 = casi garantiza que aparezca ese token
    max_tokens=50
)
```

---

## 11. Token Budget y Chunking: no te quedes sin contexto

El contexto de un LLM es finito. Cada modelo tiene su ventana maxima:

| Modelo | Ventana de contexto | Equivalente aproximado |
|--------|---------------------|----------------------|
| GPT-4o | 128k tokens | ~300 paginas de un libro |
| GPT-4o-mini | 128k tokens | Idem, mas barato y rapido |
| Claude 3.5 Sonnet | 200k tokens | ~500 paginas |
| Gemini 1.5 Pro | 1M tokens | ~2500 paginas (una biblioteca chica) |

### El problema del "contexto perdido"

Cuando una conversacion crece, los tokens mas viejos salen de la ventana. La IA literalmente **se olvida** de lo que dijiste al principio. Esto se llama *context window overflow*.

### Estrategia 1: Rolling summary (resumen rotativo)

```python
# Pseudocodigo: cada N turnos, resumi la conversacion y reemplaza el historial
def manage_context(messages, max_tokens=8000):
    token_count = count_tokens(messages)

    if token_count < max_tokens * 0.7:  # 70% de ocupacion
        return messages  # No hagas nada

    # Separa mensajes antiguos de los recientes
    old_messages = messages[:-6]   # Todo menos los ultimos 3 pares (6 mensajes)
    recent_messages = messages[-6:]  # Ultimos 3 intercambios

    # Pide un resumen de lo viejo
    summary = llm_summarize(old_messages)
    summary_msg = {"role": "system", "content": f"[Resumen de la conversacion anterior]: {summary}"}

    return [summary_msg] + recent_messages  # Contexto comprimido
```

### Estrategia 2: Sliding window (ventana deslizante)

Para tareas de analisis de documentos largos (PDFs, logs, codigo fuente):

```python
def sliding_window_chunk(text, chunk_size=4000, overlap=500):
    """Divide texto en chunks de chunk_size tokens con overlap entre ellos."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        chunk = " ".join(words[start:start + chunk_size])
        chunks.append(chunk)
        start += (chunk_size - overlap)  # El overlap evita cortar ideas a la mitad
    return chunks

# Uso tipico: analizar un PDF de 200 paginas
chunks = sliding_window_chunk(pdf_text, chunk_size=4000, overlap=500)
results = []
for chunk in chunks:
    response = llm_analyze(chunk)  # Cada chunk entra en la ventana
    results.append(response)
final = llm_merge(results)  # Unifica los analisis parciales
```

### Estrategia 3: System Prompt + User Prompt budget

Distribui tus tokens sabiamente segun el peso de cada rol:

```python
# Modelo mental de presupuesto de tokens
# Si tu ventana es de 8000 tokens:
# - System Prompt: 500 tokens (reglas, personalidad, formato)
# - Historial reciente: 3000 tokens (ultimos mensajes)
# - User Prompt actual: 2000 tokens (tu consulta + datos)
# - Output reservado: 2000 tokens (lo que esperas que responda)
# - Margen de seguridad: 500 tokens (porque siempre hay overhead)

# Ejemplo en codigo:
SYSTEM_PROMPT_TOKENS = 500
HISTORY_TOKENS = 3000
USER_INPUT_TOKENS = 2000
OUTPUT_RESERVE = 2000
SAFETY_MARGIN = 500

MAX_CONTEXT = 8000
assert SYSTEM_PROMPT_TOKENS + HISTORY_TOKENS + USER_INPUT_TOKENS + OUTPUT_RESERVE + SAFETY_MARGIN <= MAX_CONTEXT, \
    "Token budget excedido. Ajusta los valores."
```

### Anti-Patron #3: Tirarle todo el PDF de una sin chunking

```python
# MAL: El PDF tiene 60000 tokens, tu ventana es 8000
# La IA solo "lee" el principio y el final. El medio se pierde.
response = llm.chat("Resumi este PDF: " + pdf_completo)  # ❌

# BIEN: Chunking + analisis por partes + merge
chunks = sliding_window_chunk(pdf_completo)
resumenes = [llm.chat(f"Resumi esta seccion: {chunk}") for chunk in chunks]
resumen_final = llm.chat("Unifica estos resumenes parciales:\n" + "\n---\n".join(resumenes))
```

---

## 12. Queres profundizar?

Este archivo es un resumen. El [repositorio completo](https://github.com/jorgesislema/apuntes_de_ingenieria_de_prompt) tiene 16 modulos:

- 01 — Conceptos Fundamentales (anatomia del prompt)
- 02 — Tecnicas de Prompting (zero-shot, few-shot, CoT, ReAct)
- 03 — Secretos del Maestro (tecnicas avanzadas)
- 04 — Prompting a Escala Empresarial (Salesforce, Spotify, Morgan Stanley)
- 05 — Adaptacion por Modelo (GPT, Claude, Gemini, DeepSeek, Llama)
- 06 — Preparacion para Entrevistas (+300 preguntas reales)
- 07 — Laboratorio y Ejemplos (casos practicos)
- 08 — Errores Comunes y Soluciones
- 12 — Seguridad y Defensa de Prompts
- 16 — Agentes, Skills y Loops (arquitectura de IA autonoma)

Y muchos mas. Recomendado para despues del taller.
