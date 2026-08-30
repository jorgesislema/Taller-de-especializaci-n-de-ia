# Practica — Clase 3: Laboratorio de Costos y Calculadora de Tokens

> Guia práctica. Agarra lapiz, papel y calculadora (o abri una hoja de cálculo). Esto no es teorico: es lo que hace un Ingeniero de IA antes de escribir una línea de código.

---

## Ejercicio 1: La Regla de Oro en accion

**Objetivo:** Acostumbrarte a estimar tokens sin herramientas, usando la regla de oro.

### Instrucciones

Para cada uno de los siguientes textos, estima la cantidad de tokens usando la regla de oro:

> **Tokens ≈ cantidad de caracteres (con espacios) / 3.2** (para español)

Luego, si tenés acceso, verifica con el tokenizador de OpenAI (`platform.openai.com/tokenizer`) o Anthropic y anota la diferencia.

| # | Texto | Caracteres (contalos) | Tokens estimados (÷ 3.2) | Tokens reales (tokenizador) | Diferencia |
|---|-------|-----------------------|---------------------------|-----------------------------|------------|
| 1 | "Hola, ¿como estas?" | | | | |
| 2 | "Necesito consultar el saldo de mi cuenta corriente por favor." | | | | |
| 3 | "El rapidisimo murcielago hipopótamo electrostatico volo sobre el ferrocarril transiberiano." | | | | |
| 4 | (Busca un mail real que hayas escrito, copialo aca) | | | | |
| 5 | (Copia la letra del estribillo de tu cancion favorita) | | | | |

### Preguntas de reflexión

1. ¿En que textos la regla de oro fue mas precisa? ¿En cuales menos? ¿Por qué?
2. ¿Qué tipo de palabras hacen que la regla falle mas? (Ej: palabras técnicas, códigos, emojis, números largos).
3. Si tuvieras que estimar tokens para un texto en inglés vs español, ¿usarías el mismo divisor? ¿Cual usarías para cada idioma?

---

## Ejercicio 2: El Libro de 200 Paginas (replica el cálculo)

**Objetivo:** Practicar el cálculo de costo para un escenario real de procesamiento de documentos.

### Escenario

Un abogado te pide que la IA lea un libro de **350 páginas** y escriba un resumen ejecutivo de **10 páginas**. El libro y el resumen estan en español.

### Paso 1: Estima los tokens

- 350 páginas × _____ palabras/página (usa 500 como promedio) = _____ palabras totales.
- Tokens de input: _____ palabras / 0.75 = _____ tokens.

- 10 páginas × _____ palabras/página = _____ palabras de resumen.
- Tokens de output: _____ palabras / 0.75 = _____ tokens.

### Paso 2: Calcula el costo con cada modelo

| Modelo | Formula Input | Costo Input | Formula Output | Costo Output | **COSTO TOTAL** |
|--------|---------------|-------------|----------------|--------------|-----------------|
| GPT-4o | × $2.50/1M | | × $10.00/1M | | |
| GPT-4o-mini | × $0.15/1M | | × $0.60/1M | | |
| Claude 3.5 Sonnet | × $3.00/1M | | × $15.00/1M | | |
| Claude 3 Haiku | × $0.25/1M | | × $1.25/1M | | |
| DeepSeek-V3 | × $0.27/1M | | × $1.10/1M | | |

> **Tip:** Para convertir tokens a costo: `(tus_tokens / 1,000,000) × precio_por_1M`. Ej: 150,000 tokens con GPT-4o input: `(150,000 / 1,000,000) × $2.50 = 0.15 × $2.50 = $0.375`.

### Paso 3: Responde

1. ¿Cuál es el modelo más barato para esta tarea?
2. ¿En que situación elegirías el más caro en lugar del más barato?
3. Si el abogado te pidiera hacer esto con **50 libros por mes**, ¿qué modelo elegirías y cual sería el costo mensual?

---

## Ejercicio 3: El Chatbot de Atencion al Cliente (el presupuesto)

**Objetivo:** Hacer un presupuesto completo para un proyecto real. Este es **el ejercicio principal** de la clase.

### El caso de negocio

> Una empresa de e-commerce te contrata. Vas a construir un **chatbot de atención al cliente** con los siguientes números:
>
> - **500 consultas por dia** × 30 dias = **15,000 consultas/mes**.
> - Cada consulta del cliente: **200 palabras** promedio.
> - Cada respuesta de la IA: **100 palabras** promedio.
> - Contexto historico: el sistema envia las **últimas 3 interacciones** del cliente (~100 palabras c/u = 300 palabras adicionales).
> - **Presupuesto máximo para API: $100 USD/mes.**

### Fase 1: Calculos base (sin contexto historico)

1. Tokens de input por consulta (solo la pregunta del cliente):
   - _____ palabras / 0.75 = _____ tokens.

2. Tokens de output por consulta:
   - _____ palabras / 0.75 = _____ tokens.

3. Tokens mensuales totales:
   - Input: _____ × 15,000 = _____ tokens/mes.
   - Output: _____ × 15,000 = _____ tokens/mes.

### Fase 2: Agregar el contexto historico

1. Tokens de contexto por consulta:
   - _____ palabras / 0.75 = _____ tokens.

2. Tokens de input TOTALES por consulta (pregunta + contexto):
   - _____ + _____ = _____ tokens.

3. Nuevos tokens mensuales totales:
   - Input: _____ × 15,000 = _____ tokens/mes.
   - Output (sin cambios): _____ tokens/mes.

### Fase 3: Calcular costo mensual para CADA modelo

**CON contexto historico (Fase 2):**

| Modelo | Costo Input | Costo Output | **Costo Mensual Total** | ¿Dentro de $100? |
|--------|-------------|--------------|------------------------|---------------------|
| GPT-4o | | | | |
| GPT-4o-mini | | | | |
| Claude 3.5 Sonnet | | | | |
| Claude 3 Haiku | | | | |
| DeepSeek-V3 | | | | |

### Fase 4: Escenario de crecimiento

**La empresa crece a 5,000 consultas/dia (150,000/mes).** Recalcula el costo mensual para los 3 modelos más baratos de la tabla anterior.

| Modelo | Costo Input | Costo Output | **Costo Mensual Total** | ¿Sigue siendo viable? |
|--------|-------------|--------------|------------------------|------------------------|
| | | | | |
| | | | | |
| | | | | |

### Fase 5: Tu recomendación final

Redacta un parrafo (5-8 líneas) con tu recomendación profesional. Debe incluir:

1. **Que modelo elegis** y por que.
2. **Por que descartas** los otros.
3. **Que harías con el contexto historico** (¿lo mandás siempre? ¿lo resumis? ¿lo omits para consultas simples?).
4. **Que plan de contingencia** propones para cuando la empresa crezca.

---

**Escribe tu recomendación aqui:**




---

## Ejercicio 4: Investigacion de precios actualizados

**Objetivo:** Los precios de las APIs cambian constantemente. Aprende a buscar los precios reales del dia en qué haces este ejercicio.

### Instrucciones

1. Abri las siguientes páginas (busca la seccion "Pricing" o "Precios"):
   - OpenAI: `openai.com/pricing`
   - Anthropic: `anthropic.com/pricing`
   - DeepSeek: `platform.deepseek.com/api-docs/pricing`
   - Google AI (Gemini): `ai.google.dev/pricing`

2. Completa la tabla con los precios **reales de hoy** (no los de los apuntes):

| Proveedor | Modelo | Input/1M tokens | Output/1M tokens | Fecha de consulta |
|-----------|--------|-----------------|-------------------|-------------------|
| OpenAI | GPT-4o | | | |
| OpenAI | GPT-4o-mini | | | |
| Anthropic | Claude 3.5 Sonnet | | | |
| Anthropic | Claude 3 Haiku | | | |
| DeepSeek | DeepSeek-V3 | | | |
| Google | Gemini 1.5 Flash | | | |
| Google | Gemini 1.5 Pro | | | |

3. **Compara con los precios de los apuntes.** ¿Bajaron, subieron o se mantienen igual? ¿Qué modelo se abarato mas desde que se escribieron los apuntes?

### Preguntas de reflexión

1. Si los precios bajan cada 6 meses, ¿cómo afecta eso tu decisión de qué modelo usar hoy?
2. ¿Tiene sentido "casarse" con un solo proveedor de API o conviene diseniar tu sistema para cambiar de proveedor fácilmente?
3. DeepSeek y Qwen ofrecen calidad similar a GPT-4o por 1/10 del precio. ¿Que desventajas podrían tener? (Pista: latencia, censura, ubicación de servidores, privacidad).

---

## Ejercicio 5: El costo del contexto (pesadilla de ingeniero)

**Objetivo:** Entender visceralmente por qué enviar contexto en crudo es peligroso.

### Escenario

Estas construyendo un **asistente legal para abogados**. Cada vez que un abogado hace una pregunta, tu sistema envia:

- **Opcion A (ingenua):** Los últimos 5 contratos completos como "contexto" (30 páginas c/u = 150 páginas totales ≈ 100,000 tokens). Mas la pregunta del abogado (200 tokens).
- **Opcion B (inteligente):** Buscas SOLO los 3 parrafos relevantes de los contratos (1 página ≈ 670 tokens). Mas la pregunta del abogado (200 tokens).

### Calculos

1. **Tokens de input por consulta:**
   - Opcion A: _____ tokens.
   - Opcion B: _____ tokens.

2. **Costo por consulta con GPT-4o** (input: $2.50/1M, output: ~100 tokens × $10.00/1M = $0.001):
   - Opcion A: $_____ por consulta.
   - Opcion B: $_____ por consulta.

3. **Costo mensual** (asumiendo 200 consultas por dia × 30 dias = 6,000 consultas/mes):
   - Opcion A: $_____ / mes.
   - Opcion B: $_____ / mes.

4. **Ahorro mensual** por usar la Opcion B en lugar de la A: $_____ / mes.

### Preguntas de reflexión

1. ¿Que técnica usarías para implementar la Opcion B? (No hace falta saberla ya; la veremos en las Clases 12-14. Es RAG + embeddings + busqueda vectorial.)
2. ¿Se te ocurre otra forma de reducir el contexto sin perder calidad?
3. ¿Qué pasaría si en lugar de 5 contratos, el abogado necesitara contexto de 50?

---

## Ejercicio 6 (opciónal): Explorando Ollama

Si tenés una computadora con al menos 8 GB de RAM y querés probar IA local:

1. Anda a `ollama.com` y descarga Ollama para tu sistema operativo.
2. Abri una terminal y ejecuta: `ollama run llama3.2` (modelo de ~3B, ligero).
3. Hacele 5 preguntas. Compara la velocidad de respuesta con ChatGPT web.
4. Proba otro modelo: `ollama run mistral` (7B, un poco más pesado y capaz).
5. Si tu computadora lo soporta, proba: `ollama run llama3` (8B).

### Preguntas de reflexión

1. ¿Notaste diferencia de velocidad entre los modelos?
2. ¿Como se compara la calidad de respuesta con ChatGPT?
3. ¿Cuanta RAM/VRAM esta usando? (En Windows, abri el Administrador de Tareas y mira el consumo.)
4. ¿Para qué tipo de tareas usarías un modelo local?

---

## Entrega

Al terminar los ejercicios, deberías tener:

- [ ] Ejercicio 1: Tabla de estimacion de tokens completada.
- [ ] Ejercicio 2: Costo del libro de 350 páginas calculado para 5 modelos.
- [ ] Ejercicio 3: **Presupuesto completo del chatbot** con recomendación final (el más importante).
- [ ] Ejercicio 4: Tabla de precios actualizados con fecha de consulta.
- [ ] Ejercicio 5: Calculo del costo con y sin contexto inteligente.
- [ ] Ejercicio 6 (opciónal): Prueba de Ollama local.

---

> **Recorda:** El Ingeniero de IA no programa hasta no haber hecho estás cuentas. Porque programar sin saber cuánto cuesta es como construir una casa sin saber el precio de los materiales.
