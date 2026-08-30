# Clase 3 — La Economía de la IA: Tokens, Parámetros y Costos

**Modulo 1: Infraestructura y Limitaciónes de la IA**

---

## Resumen

Tercera clase del taller. Hoy no solo aprendes a usar IA: aprendes a **calcular cuanto cuesta**. Vas a entender que es un token realmente (la "moneda" con que pagas), por qué "gato" es 1 token pero "hipopótamo" puede ser 3, que significa que un modelo tenga 8k o 128k de contexto, y como la ventana de contexto llena se traduce en dólares. Vas a comparar las tres formas de conectarte a la IA (Chat, API, Local) y vas a leer una tabla de precios como un profesional. Al terminar, vas a saber elegir el modelo y la modalidad correcta para qué tu proyecto no quiebre en una semana.

## Objetivos

Al terminar esta clase vas a poder:

1. Explicar que es un **token**, como se tokeniza el texto, y calcular cuantos tokens tiene un texto aproximado.
2. Diferenciar **tokens de entrada** (input) de **tokens de salida** (output) y por qué pagás distinto por cada uno.
3. Entender que es la **ventana de contexto** (8k, 32k, 128k) y como llenarla impacta directamente el costo.
4. Explicar que son los **parametros** de un modelo y la relación entre parametros, inteligencia y costo.
5. Elegir entre **modelos grandes** (GPT-4o, Claude Sonnet) y **modelos pequenios** (Haiku, Llama 8B) según la tarea.
6. Comparar las **tres modalidades** de conexión: Chat (minorista), API (mayorista/ingeniería) y Local (soberanía).
7. Leer e interpretar una **tabla de precios** de APIs de IA (Input/1M tokens, Output/1M tokens).
8. Calcular el **costo mensual** de un proyecto real con IA usando distintas APIs.
9. Identificar **costos ocultos**: rate limits, latencia, VRAM.

## Material de la clase

- 📖 [`apuntes.md`](apuntes.md) — Teoria completa. Material de apoyo para leer y estudiar.
- 📕 [`glosario.md`](glosario.md) — Terminos clave en lenguaje sencillo, con analogía.
- 🧮 [`práctica.md`](práctica.md) — Laboratorio practico: calculadora de tokens, presupuesto de proyecto, comparativa de APIs.
- 🎬 [`recursos.md`](recursos.md) — Herramientas, videos, articulos.

## Agenda (70 + 20 min)

| Minuto | Bloque | Tema |
|--------|--------|------|
| 0–10 | 1 | **Introduccion:** La economía de la IA y por qué un ingeniero cuenta tokens |
| 10–25 | 2 | **Tokens y Tokenización:** Que es un token, el proceso de tokenización, regla de oro (1 token aprox 4 caracteres en inglés / 0.75 palabra en español), tokens input vs output, la ventana de contexto (8k/32k/128k) |
| 25–35 | 3 | **Parametros:** Que es un parametro, relación parametros-inteligencia-costo, modelos grandes vs pequenios |
| 35–45 | 4 | **Las 3 Modalidades:** Chat (minorista/el casino), API (mayorista/ingeniería pura), Local (soberanía/off-the-grid) |
| 45–60 | 5 | **Matematica de Costos:** Anatomia de una tabla de precios, comparativa real (GPT-4o, GPT-4o-mini, Claude Sonnet, Claude Haiku, DeepSeek, Qwen), ejercicio en vivo "libro de 200 páginas", el costo del contexto |
| 60–70 | 6 | **Costos Ocultos y Limites:** Rate limits (RPM/TPM), latencia, VRAM |
| 70–90 | 7 | **Laboratorio y consultas:** Ejercicio practico (chatbot de 500 consultas diarias), cálculo de costos entre APIs, tarea para casa |

## Temas que cubre esta clase

| Bloque | Tema |
|--------|------|
| 1 | Tokens y Tokenización: La Moneda de la IA |
| 2 | Parametros: El "Peso" del Cerebro |
| 3 | Las 3 Modalidades: Chat vs API vs Local |
| 4 | La Matematica de los Costos |
| 5 | Costos Ocultos y Limites de Ingenieria |
| 6 | Laboratorio de Costos y Tarea |
| 7 | El Ingeniero de IA en esta clase |

## Proxima clase

**Clase 4: Vibe Coding — Programacion Dirigida por Lenguaje Natural.** Programar con IA, primeros programas sin saber programar.
