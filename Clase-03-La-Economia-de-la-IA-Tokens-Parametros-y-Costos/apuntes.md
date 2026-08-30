# Clase 3 — La Economía de la IA: Tokens, Parámetros y Costos

> Material de apoyo para el estudiante. Podés leerlo directo en GitHub o en la vista web. No necesitas instalar nada para leer esto.

---

## Filosofía de la clase

> **Un ingeniero de IA no solo sabe pedirle cosas a ChatGPT. Sabe cuánto cuesta cada letra que escribe la IA, por qué un modelo es más caro que otro, y cómo elegir la forma correcta de conectarse para que el proyecto sea viable financieramente.**

En la Clase 1 aprendimos que la IA no es magia: es estadística determinística. En la Clase 2 aprendimos los riesgos de confiar ciegamente en lo que parece inteligente. Hoy ponemos los pies sobre la tierra: **la IA no es magia, pero tampoco es gratis**. Cada palabra que genera tiene un costo real, en dólares, en electricidad, en hardware.

Si te llevás una sola cosa de esta clase, que sea esta:

> **La diferencia entre un usuario y un Ingeniero de IA es que el ingeniero sabe cuánto cuesta cada token antes de enviar el prompt.**

---

## 1. Tokens y Tokenización: La Moneda de la IA

> Si la electricidad es el combustible físico, el **token** es la moneda con la que pagás por usar la IA.

### 1.1 ¿Qué es un Token realmente?

En la Clase 1 lo dijimos de pasada: un token es un **trozo de texto** al que se le asigna un número ID. Pero eso es la definición técnica. La definición **económica** es más importante para vos como ingeniero:

> **Un token es la unidad mínima por la que te cobra una API de IA.**

Cada vez que la IA "lee" una palabra tuya, consume tokens. Cada vez que "escribe" una palabra, consume tokens. Y cada token tiene un precio.

**¿Es lo mismo una letra, una palabra y un token? No.**

| Unidad | Ejemplo | ¿Cuántos tokens? |
|--------|---------|-------------------|
| Una letra | `a` | 1 token |
| Una palabra corta | `gato` | 1 token |
| Una palabra larga | `hipopótamo` | ~3 tokens |
| Una palabra en inglés | `cat` | 1 token |
| Una palabra en inglés | `hippopotamus` | ~4 tokens |
| Un espacio | ` ` | 1 token (a veces) |
| Un signo de puntuación | `.` | 1 token |

**Analogía del restaurant:** Pedirle texto a la IA es como pedir comida por peso. No pagás por "plato" (palabra), pagás por "gramo" (token). Algunas palabras son livianas (1 token), otras son pesadas (3 o 4 tokens). Y el idioma importa: el español suele ser mas "pesado" que el inglés.

### 1.2 El proceso de Tokenización: Cómo la IA "muerde" las palabras

Cuando vos escribís `"Hola, ¿como estas?"`, la IA no ve letras. Un **tokenizador** (un programita dentro del modelo) parte el texto en pedazos. Es como un carnicero que corta la carne: no corta vaca por vaca, corta en trozos que ya conoce.

Veamos ejemplos reales de tokenización:

```
Texto: "El gato duerme en el sofa"
Tokenización: ["El", " g", "ato", " du", "erme", " en", " el", " sof", "a"]
Tokens: 9 tokens para 5 palabras en español

Texto: "The cat sleeps on the couch"
Tokenización: ["The", " cat", " sleeps", " on", " the", " couch"]
Tokens: 6 tokens para 6 palabras en inglés
```

**¿Por qué "gato" = 2 tokens pero "cat" = 1 token?** Porque los tokenizadores más usados (como el de OpenAI) fueron entrenados mayoritariamente con texto en **inglés**. Conocen palabras completas en inglés. Para el español, a veces tienen que partir en pedazos más chiquitos. Es como un diccionario: si la palabra está en el diccionario, va entera (1 token). Si no, la parte en sílabas o letras (varios tokens).

**Analogía del rompecabezas:** Imagina que el tokenizador es una fábrica de rompecabezas. Tiene un catalogo de piezas pre-fábricadas. Si tu palabra coincide con una pieza del catalogo, sale entera. Si no, la parten en pedazos que SI estan en el catalogo. El catalogo tiene mas piezas en inglés que en español, por eso el español "gasta" más tokens.

**Ejemplos reales de tokenización con GPT-4:**

| Texto | Tokens | Explicacion |
|-------|--------|-------------|
| `"Hola"` | 1 | Palabra comun, esta en el catalogo |
| `"Hola mundo"` | 3 | "Hola" (1) + espacio (1) + "mundo" (1) = 3 |
| `"Inteligencia Artificial"` | 5 | Palabras largas en español se parten mas |
| `"Artificial Intelligence"` | 3 | En inglés, ambas palabras estan en el catalogo |
| `"😊"` | 1-3 | Los emojis también son tokens (depende del emoji y del tokenizador) |
| `"1234567890"` | 3-4 | Los números largos se parten en bloques |

### 1.3 La regla de oro empirica

> **1 token ≈ 4 caracteres en inglés ≈ 0.75 de una palabra en español.**

Esta regla no es exacta, pero es suficiente para hacer cálculos rápidos **sin tokenizador**. Si necesitas precisión, usa la herramienta de tokenización de OpenAI (la vemos en el laboratorio).

**Cómo usarla:**

- Tenes un texto de 100 palabras en español → ~133 tokens (100 / 0.75)
- Tenes un texto de 100 palabras en inglés → ~75 tokens (100 / 1.33)
- Tenes un texto de 1000 caracteres en español → ~250 tokens (1000 / 4)

**Pero ojo:** esto es un promedio. Las palabras técnicas, los códigos de programacion, los números y los emojis pueden consumir más o menos tokens que el promedio. Solo la herramienta de tokenización te da el número exacto.

### 1.4 Tokens de Entrada (Input) vs. Tokens de Salida (Output)

Esta es una de las distinciones más importantes para entender los costos:

| | Tokens de Entrada (Input) | Tokens de Salida (Output) |
|---|---|---|
| **¿Qué son?** | Lo que vos le escribís a la IA (tu prompt) | Lo que la IA te responde |
| **¿Quien los genera?** | Vos | La IA |
| **¿Cuestan igual?** | **No.** El output es más caro. | **Si.** Suele costar 3x a 5x más que el input. |
| **¿Por qué?** | Leer es barato (la IA procesa tu texto de una pasada). | Escribir es caro (la IA genera una palabra a la vez, calculando probabilidades para cada una). |

**Analogía de la fábrica:** Leer tu prompt es como recibir materia prima en la fábrica: rápido, barato. Generar la respuesta es como fábricar el producto terminado: lento, caro, requiere energía y tiempo de maquina.

**Ejemplo concreto con GPT-4o:**

- Input: 1000 tokens → cuesta ~$0.0025 USD
- Output: 1000 tokens → cuesta ~$0.010 USD

**Generar texto cuesta 4 veces más que leerlo.** Esto es clave cuando diseñás una aplicación: si tu chatbot recibe consultas cortas pero responde con textos largos, el costo principal esta en el output.

### 1.5 El "Context Window" (Ventana de Contexto): La memoria a corto plazo

> La **ventana de contexto** es la cantidad máxima de tokens que un modelo puede "recordar" en una sola conversación.

**Pensalo como la memoria RAM de tu computadora o como un pizarron:** cada vez que hablás con la IA, todo lo que se dijo se escribe en un pizarron. El modelo solo puede "ver" lo que está en ese pizarron. Cuando el pizarron se llena, lo que se escribio primero se borra. Lo que se borro, la IA **lo olvida para siempre** (en esa conversación).

| Ventana | Tamano en tokens | ¿Qué entra? | Ejemplo de modelo |
|---------|-----------------|-------------|-------------------|
| **4k** | 4,096 | ~3,000 palabras en español | GPT-3.5 (original) |
| **8k** | 8,192 | ~6,000 palabras | Modelos antiguos |
| **32k** | 32,768 | ~24,000 palabras (~80 páginas) | GPT-4 (versión inicial) |
| **128k** | 131,072 | ~98,000 palabras (~350 páginas) | GPT-4o, Claude 3.5 Sonnet |
| **200k** | 200,000 | ~150,000 palabras (~500 páginas) | Claude 3.5 Sonnet (algunas versiónes) |
| **1M** | 1,000,000 | ~750,000 palabras (~2,500 páginas) | Gemini 1.5 Pro |

**¿Qué significa esto en la práctica?**

- Con **128k tokens** podés meter una novela entera (~350 páginas) en el prompt y la IA la "recuerda" toda durante la conversación.
- Pero **llenar la ventana de contexto tiene un costo directo**. Si le mandás 100,000 tokens de contexto previo, **pagás por esos 100,000 tokens de input en CADA pregunta nueva**, aúnque la IA ya los "leyo" antes.

**El costo del contexto: un ejemplo que asusta**

Imagina que estás construyendo un chatbot de atención al cliente para un banco. Queres que la IA "recuerde" todo el historial del cliente. Le mandás los últimos 50 correos electronicos como "contexto" para qué la IA este informada.

- 50 correos × ~500 palabras cada uno = 25,000 palabras ≈ **33,000 tokens**.
- Costo de input con GPT-4o: 33,000 tokens × $2.50/1M tokens = **$0.0825 USD por consulta**.
- Si atendes **500 consultas por dia**, solo en input de contexto vas a gastar:
  - $0.0825 × 500 = **$41.25 USD por dia**
  - $41.25 × 30 dias = **$1,237 USD por mes**

**Solo por enviar el contexto historico.** Y eso sin contar el output de la IA.

> **Leccion de ingeniería:** No llenes la ventana de contexto porque "total, hay espacio". Cada token que enviás cuesta dinero. Aprende a resumir, filtrar, y solo enviar lo relevante. La Clase 14 (RAG Avanzado) te va a enseniar técnicas para hacer exactamente esto.

**¿Cómo se comporta la IA cuando el contexto está lleno?**

- Los primeros mensajes de la conversación **se olvidan**. Es como si nunca los hubieras escrito.
- La IA no te avisa que "olvido" algo. Simplemente deja de usarlo.
- Si tu sistema depende de que la IA "recuerde" instrucciónes que le diste al principio, y la conversación es larga... esas instrucciónes desaparecen. **Esto rompe aplicaciónes en producción.**

> Por eso existen técnicas como **memoria externa** y **RAG** (que veremos en modulos 4 y 5). Son formas de guardar información fuera de la ventana de contexto y solo cargar lo relevante cuando se necesita, ahorrando tokens y dinero.

**Analogía del pizarron rebooteado:** Es como si estuvieras en una reunion con un pizarron. Todo lo que se dice se escribe. Cuando el pizarron se llena, borras lo más viejo para hacer espacio. Si una decisión importante estaba al principio del pizarron... se perdio. La IA funcióna igual.

---

## 2. Parametros: El "Peso" del Cerebro

### 2.1 Recordatorio rápido: ¿Qué es un peso?

En la Clase 1 programamos un perceptrón. Vimos que cada input tenía un **peso** (un número que indica que tan importante es ese input) y un **sesgo**. El perceptrón aprendia **ajustando esos números** hasta que sus predicciones fueran correctas.

> Un **parametro** es simplemente uno de esos números ajustables. En el perceptrón habia 3 parametros (2 pesos + 1 sesgo). En un LLM hay **miles de millónes**.

### 2.2 Mini-Clase de Machine Learning: ¿Cómo se ajustan los parámetros?

Hasta ahora dijimos que los parámetros "se ajustan durante el entrenamiento". Pero... ¿cómo? ¿Quién los ajusta? ¿Con qué criterio?

Esto se llama **Machine Learning** (aprendizaje automático). No es magia: es un proceso de **prueba, error y ajuste**.

#### Las tres formas de aprender

Imaginá que querés enseñarle a un programa a reconocer si una imagen contiene un perro o un gato. Hay tres caminos:

| Forma de aprender | ¿Cómo funciona? | Analogía |
|-------------------|-----------------|----------|
| **Supervisado** | Le mostrás 10,000 fotos **con etiqueta**: "esto es un perro", "esto es un gato". El modelo ajusta sus parámetros hasta acertar. | Como un nene que aprende con flashcards: ve la imagen y atrás dice la respuesta. |
| **No supervisado** | Le das 10,000 fotos **sin etiquetas**. El modelo encuentra patrones solo: "hay dos grupos de animales distintos". | Como ordenar una caja de juguetes sin que nadie te diga cómo: agrupás lo que se parece. |
| **Por refuerzo** | El modelo **toma decisiones y recibe premios o castigos**. No le decís "esto es un perro". Le decís "¡bien!" cuando acierta y "¡mal!" cuando falla. | Como entrenar a un cachorro: no le explicás "sentate significa doblar las patas traseras", le das una galletita cuando lo hace bien. |

#### Foco: Aprendizaje por Refuerzo (Reinforcement Learning)

> Esta es la forma más intuitiva de entender cómo una IA "aprende" sin que un humano le dé todas las respuestas.

**El experimento mental del perrito que aprende a sentarse viendo imágenes**

Imaginá que tenés una IA que controla un perrito robot. El perrito tiene una **cámara** (ve imágenes del mundo) y **puede hacer 4 cosas**: sentarse, pararse, caminar, ladrar.

```
   ┌──────────────────────────────────────────┐
   │                                            │
   │   CÁMARA (IMAGEN)        ACCIÓN            │
   │  ┌─────────────┐      ┌──────────┐        │
   │  │  Ve a un      │      │  Sentarse │        │
   │  │  humano con   │ ──► │  Pararse  │ ──► ¿Premio o castigo?
   │  │  una galleta  │      │  Caminar  │        │
   │  └─────────────┘      │  Ladrar   │        │
   │                        └──────────┘        │
   │                                            │
   │   Si el humano dice "siéntate" y el        │
   │   perrito se sienta → 🦴 +10 puntos        │
   │   Si el humano dice "siéntate" y ladra → ❌ -5 puntos │
   └──────────────────────────────────────────┘
```

**Día 1 (cero conocimiento):** El perrito ve una imagen (un humano borroso diciendo algo). No tiene idea de qué hacer. **Prueba las 4 acciones al azar.** La mayoría falla. Pero una vez, por casualidad, se sienta cuando el humano dijo "siéntate". ¡Premio! El perrito anota en su "memoria numérica":

> *"Cuando veo una imagen CON ESTAS FORMAS Y COLORES (humano + boca abierta) y elijo SENTARME, hay 10% de chance de premio. Antes era 5%. Subo un poquito esa probabilidad."*

**Día 100:** El perrito ya vio 10,000 imágenes distintas. Humanos altos, bajos, de día, de noche, con distintos fondos. Cada vez que acertó, **ajustó sus parámetros internos** para que "sentarse" sea más probable cuando la imagen se parece a "humano dando una orden". Cada vez que falló, ajustó para que ladrar o caminar sea menos probable en esas situaciones.

**Día 1000:** El perrito **nunca falla**. Ve una imagen de un humano con la boca abierta, y sus parámetros internos inmediatamente activan "sentarse" con 98% de probabilidad. No "entiende" español. No "sabe" lo que es un humano. Pero sus **números internos se calibraron** para que cada imagen produzca la acción correcta.

> **Eso es Machine Learning por refuerzo:** convertir imágenes (píxeles = números) en decisiones (acciones = números), ajustando millones de parámetros a fuerza de premios y castigos.

#### De las imágenes a los textos: RLHF (Refuerzo con humanos)

Cuando OpenAI entrenó ChatGPT, usó una técnica llamada **RLHF** (Reinforcement Learning from Human Feedback — Aprendizaje por Refuerzo con Retroalimentación Humana).

El proceso fue:

1. **Etapa 1:** El modelo lee internet entera (aprendizaje supervisado masivo). Aprende que después de "El cielo es..." suele venir "azul".
2. **Etapa 2:** Humanos reales **califican respuestas**. Le muestran al modelo 4 respuestas distintas para la misma pregunta y votan: "esta es útil", "esta es mala", "esta es peligrosa".
3. **Etapa 3:** El modelo usa esos votos como **premios y castigos** (igual que el perrito con las galletitas) y ajusta sus 1.8 billones de parámetros para producir respuestas que los humanos prefieren.

**Por eso ChatGPT suena "amable" y "útil":** no porque sea bueno, sino porque fue recompensado cuando sonaba amable y castigado cuando sonaba grosero o peligroso. Es el perrito, pero en vez de sentarse, escribe texto.

#### ¿Cuánto cuesta entrenar?

Acá conectamos con el tema de esta clase:

| Tipo de entrenamiento | Costo estimado | ¿Quién lo paga? |
|-----------------------|----------------|-----------------|
| Entrenar GPT-4 desde cero | ~$100 millones USD (electricidad + GPUs + salarios) | OpenAI / Microsoft |
| Entrenar Llama 3 70B | ~$10-20 millones USD | Meta |
| Hacer fine-tuning de un modelo existente | ~$50-$500 USD | Vos (un ingeniero) |
| **Inferencia** (usar el modelo ya entrenado) | Fracciones de centavo por consulta | El que usa la API |

> **Dato clave:** Entrenar un modelo grande es **carísimo**. Pero una vez entrenado, usarlo (inferencia) es **barato**. Es como construir una autopista: la construcción cuesta miles de millones, pero cada auto que pasa paga centavos de peaje.

#### Cómo se ve una imagen para una IA

Como bonus visual: cuando el perrito robot "ve" una imagen, no ve un humano lindo con una galleta. Ve esto:

```
Imagen de 100×100 píxeles (10,000 números)
┌────────────────────────────┐
│ 255  255  255  128  64 ... │  ← Cada número = intensidad de un píxel
│ 255  200  100   50  30 ... │     (0 = negro, 255 = blanco)
│ 180  120   80   40  20 ... │
│  ...                       │
└────────────────────────────┘
         ↓
  10,000 números entran a la red neuronal
         ↓
  Se multiplican por MILLONES de parámetros
         ↓
  Sale un número: "sentarse = 98%, ladrar = 1%, caminar = 0.5%, pararse = 0.5%"
```

La IA no "ve" un humano. Ve una **matriz de números**. Y sus parámetros son los engranajes que transforman esa matriz en una decisión. Sin magia, sin comprensión, sin cariño por el humano. **Solo números.**

> **En la Clase 4 vas a programar tus primeros experimentos de Machine Learning.** Vas a ver en código cómo un modelo "aprende" patrones simples. Por ahora, quedate con la idea: **entrenar = probar, medir el error, ajustar parámetros, repetir.**

### 2.3 ¿Qué significa "GPT-4 tiene 1.8 billones de parámetros"?

Cuando lees que un modelo tiene "X parametros", eso es literalmente la cantidad de **números** que se ajustaron durante el entrenamiento.

| Modelo | Parametros (aprox.) | ¿Qué significa? |
|--------|---------------------|-----------------|
| Perceptrón de la Clase 1 | 3 | Un portero que decide "abrir o no abrir" |
| Llama 3 8B | 8 mil millónes | Una biblioteca municipal |
| Llama 3 70B | 70 mil millónes | Una biblioteca universitaria |
| DeepSeek V3 | 671 mil millónes (total, 37B activos por consulta) | Una red de bibliotecas con acceso inteligente |
| GPT-4 (estimado) | ~1.8 billones | La Biblioteca del Congreso de EE.UU. |
| Claude 3.5 Sonnet | No revelado (estimado cientos de miles de millónes) | — |

**Analogía del cerebro de papel:** Imagina que cada parametro es una **conexión entre dos neuronas**. Un modelo de 8 mil millónes de parametros tiene 8 mil millónes de conexiónes. El cerebro humano tiene aproximadamente 100 billones de conexiónes (sinapsis). O sea, el modelo más grande actual tiene menos conexiónes que un cerebro humano, pero más que suficiente para patrónes de lenguaje.

### 2.4 La relación entre Parámetros, Inteligencia y Costo

> **Un modelo más grande (mas parametros) no siempre es más inteligente, pero siempre es más caro.**

| Mas parametros | Menos parametros |
|----------------|------------------|
| ✅ Captura patrónes más sútiles y complejos | ✅ Corre más rápido (menos cálculos) |
| ✅ Mejor en tareas creativas y razónamiento | ✅ Cuesta mucho menos por consulta |
| ✅ Mejor comprensión de matices y contexto | ✅ Puede correr en hardware modesto (local) |
| ❌ Mas caro de usar (API) o de correr (local) | ❌ Pierde matices y puede fallar en tareas complejas |
| ❌ Mas lento (mas cálculos = mas latencia) | ❌ Menor capacidad de razónamiento profundo |
| ❌ Requiere mas VRAM si es local | ❌ Puede "olvidar" instrucciónes complejas |

**El punto clave de ingeniería:**

> **Para el 80% de las tareas, un modelo pequenio hace el mismo trabajo que uno gigante. Y cuesta 1/10 o 1/50 del precio.**

**Ejemplos concretos de qué modelo elegir según la tarea:**

| Tarea | Modelo recomendado | ¿Por qué? |
|-------|-------------------|-----------|
| Clasificar si un mail es spam o no | Haiku / GPT-4o-mini / Llama 8B | Es una tarea simple. No necesitas 1.8 billones de parametros para decidir "spam / no spam". |
| Corregir ortografía y gramática | Haiku / GPT-4o-mini / Llama 8B | Los modelos pequenios corrigen ortografía perfectamente. |
| Traducir un texto simple | GPT-4o-mini / DeepSeek | La traducción básica no requiere razónamiento profundo. |
| Escribir un poema con métrica y rima | GPT-4o / Claude Sonnet | Requiere creatividad y comprensión de patrónes complejos. |
| Analizar un contrato legal de 50 páginas | GPT-4o / Claude Sonnet | Requiere comprensión profunda, matices legales, y no alucinar. |
| Resumir 100 páginas de texto tecnico | GPT-4o / Claude Sonnet (o DeepSeek para ahorrar) | Requiere mantener coherencia en textos largos. |
| Chatbot de atención al cliente (consultas simples) | GPT-4o-mini / Haiku | El 90% de consultas son repetitivas y simples. No gastes GPT-4o en "¿cuál es mi saldo?". |

> **Regla de oro:** Empeza siempre con el modelo más barato. Si no alcanza, subi al siguiente. Es mas fácil escalar hacia arriba que pagar de mas desde el dia 1.

### 2.5 Modelos Grandes vs. Modelos Pequeños (Small/Medium)

| Caracteristica | Modelo Grande (GPT-4o, Claude Sonnet) | Modelo Pequenio (Haiku, GPT-4o-mini, Llama 8B) |
|----------------|---------------------------------------|------------------------------------------------|
| **Costo input/1M tokens** | ~$2.50–$3.00 USD | ~$0.15–$0.25 USD |
| **Costo output/1M tokens** | ~$10.00–$15.00 USD | ~$0.60–$1.25 USD |
| **Velocidad** | Mas lento | Mas rápido |
| **Razonamiento complejo** | Excelente | Bueno (limitado) |
| **Tareas simples** | Sobrado (dinero tirado) | Perfecto |
| **¿Corre en local?** | Necesitas GPU de $5,000+ USD | Corre en una laptop gamer |

**Ejemplo real de ahorro:**

Un sistema que clasifica 1 millón de tickets de soporte por mes:
- Con GPT-4o: $2.50 USD (input) + $10.00 USD (output con clasificación) ≈ **$12.50 USD**
- Con GPT-4o-mini: $0.15 USD (input) + $0.60 USD (output) ≈ **$0.75 USD**

> **Ahorro: 94%.** Y la clasificación probablemente sea igual de buena. Para clasificar texto, no necesitas un modelo que escriba poemas.

---

## 3. Las 3 Modalidades: ¿Cómo te conectás a la IA?

No es lo mismo usar la web de ChatGPT que programar una app que se conecte por debajo. Son **tres negocios distintos**.

### 3.1 La Modalidad "Chat" (Minorista / El Casino)

> **Como funcióna:** Vas a una página web (chat.openai.com, claude.ai), escribís en una caja de texto, y la IA responde. Pagas una suscripción mensual fija (~$20 USD/mes ChatGPT Plus).

**La ilusión del "todo incluido":**

- Parece que podés hablar infinitamente.
- **Realidad:** Hay límites de uso (rate limits). Si hablas mucho en poco tiempo, el sistema te frena.
- En ChatGPT Plus, el límite es aproximadamente 40-80 mensajes cada 3 horas con GPT-4o (cambia según demanda).
- Si pasas el límite, te degrada a GPT-4o-mini temporalmente.

**Para qué sirve:**

- Uso personal, exploracion, aprendizaje.
- Probar prompts antes de pasarlos a producción.
- Tareas puntuales: escribir un mail, traducir un texto, pedir una idea.

**Para que NO sirve:**

- **Produccion profesional.** No podés construir una app que dependa de una sesión de ChatGPT abierta en un navegador.
- Automatizacion: no podés conectar tu sistema de tickets a la web de ChatGPT.
- Escala: si tu app recibe 10,000 consultas por dia, la web de ChatGPT no te sirve.
- Confiabilidad: los rate limits y cortes de servicio no son aceptables para un negocio.

**¿Por qué "el casino"?** Porque esta diseñado para que te quedes. La suscripción fija te da la sensacion de "ya pague, ahora uso todo lo que pueda". Pero tiene límites que no ves hasta que los chocas. Como un casino: la casa siempre gana.

### 3.2 La Modalidad "API" (Mayorista / Ingenieria Pura)

> **API** = Application Programming Interface. **"Ventanilla de pedidos."**

**Analogía del restaurante:** La web de ChatGPT es como ir a comer al salon del restaurant. La API es como pedir por delivery: no ves el salon, pero recibis la comida en tu casa. Y pagás por cada plato que pedís (pay-as-you-go), no una membresía mensual.

**¿Cómo funcióna?**

1. Te creas una cuenta de desarrollador (platform.openai.com, console.anthropic.com).
2. Generas una **clave API** (API Key): un código secreto como `sk-abc123...`. Esta clave es tu "identidad" para qué la API sepa que sos vos y a quien cobrarle.
3. Tu programa (un script de Python, una app web, un backend) envia pedidos a la API usando esa clave.
4. La API procesa tu pedido y te devuelve la respuesta.
5. **Pagas por cada token** que consumiste. A fin de mes, te llega la factura.

**¿Por qué es la única forma válida para construir aplicaciónes reales?**

| Ventaja | Explicacion |
|---------|-------------|
| **Escala** | Podes hacer 1 consulta o 1 millón. La API escala con tu necesidad. |
| **Automatizacion** | Tu programa decide cuando llamar a la IA, sin intervención humana. |
| **Control** | Vos decidis qué modelo usar, que parametros (temperatura, max tokens, etc.). |
| **Sin rate limits absurdos** | Los límites son mucho más altos que en la web. Y si necesitas mas, pagás mas (aumento de cuota). |
| **Integracion** | Conectas la IA a tu base de datos, tu sistema de tickets, tu app movil. |
| **Privacidad (relativa)** | En planes empresariales, OpenAI NO entrena con tus datos de API. En la web gratuita, si. |

**La clave API y seguridad básica:**

> **Trata tu API Key como la clave de tu home banking.** Si alguien la obtiene, puede usar la IA a tu nombre y **vos pagás la cuenta**.

Reglas básicas de seguridad con API Keys:

1. **Nunca las escribas en el código** que subis a GitHub. Hacelo y en minutos hay bots que la roban.
2. Guardalas en **variables de entorno** (un archivo `.env` que NO se sube a GitHub).
3. Si una clave se filtra, **revocala inmediatamente** (la desactivas y creas una nueva).
4. Pone **límites de gasto** (hard limits) en la plataforma. Ej: "no gastar mas de $50 USD este mes."

### 3.3 La Modalidad "Local" (Soberania / Off-the-grid)

> **Significa correr el modelo de IA en tu propia computadora**, sin internet, sin APIs, sin empresas de por medio.

**¿Cómo se hace?**

- Herramientas como **Ollama** (la mas fácil) o **LM Studio** te permiten descargar y ejecutar modelos open-source (Llama, Mistral, Gemma, DeepSeek) en tu computadora.
- Un solo comando: `ollama run llama3` y tenés un chat funciónando 100% local.

**El mito de la "IA Gratis" local:**

> **Nada es gratis.** Cuando corres un modelo en local, no pagás por token. Pero pagás de otras formas:

| Costo Oculto | Explicacion |
|--------------|-------------|
| **Hardware (VRAM)** | Necesitas una GPU con suficiente memoria de video. Un modelo de 8B parametros necesita ~6 GB de VRAM. Uno de 70B necesita ~40 GB. |
| **Electricidad** | Una GPU consume entre 150W y 450W. Correr un modelo 24/7 no es gratis en la factura de luz. |
| **Rendimiento** | Un modelo local es más lento que una API en la nube (las GPUs de OpenAI/Nvidia son mucho más potentes). |
| **Calidad** | Los modelos open-source suelen ser menos capaces que GPT-4o o Claude Sonnet (aúnque se acercan cada vez mas). |
| **Mantenimiento** | Vos sos el soporte tecnico. Si algo falla, lo arreglas vos. |

**Ventajas absolutas de lo Local:**

| Ventaja | Explicacion |
|---------|-------------|
| **Privacidad total** | Tus datos nunca salen de tu computadora. Ideal para datos medicos, legales, financieros. |
| **Sin censura** | Los modelos open-source no tienen filtros de contenido (o los podés desactivar). |
| **Sin costos por token** | Hablas todo lo que quieras. El costo marginal es cero (ya pagaste el hardware). |
| **Disponibilidad** | Funciona sin internet. Si los servidores de OpenAI se caen, tu IA local sigue andando. |
| **Personalizacion** | Podes hacer fine-tuning y modificar el modelo a tu gusto. |

**¿Puedo correr un modelo grande en mi notebook?**

| Hardware | ¿Que podés correr? |
|----------|-------------------|
| **Notebook con 8 GB RAM, sin GPU dedicada** | Modelos muy chicos (1-3B parametros). Respuestas básicas, lentas. |
| **Notebook con 16 GB RAM, GPU 6 GB VRAM** | Modelos de 7-8B (Llama 3 8B, Mistral 7B). Funcional, decente. |
| **PC gamer con GPU 12-16 GB VRAM** | Modelos de 13-20B. Buena calidad. |
| **Workstation con GPU 24 GB VRAM** | Modelos de 30-40B. Muy buena calidad. |
| **Servidor con GPU 48-80 GB VRAM** | Modelos de 70B+. Calidad cercana a GPT-4. |
| **GPT-4o (nube)** | No lo corres en local. OpenAI no publica los pesos del modelo. Es privativo. |

> **Regla práctica:** Para correr un modelo de X mil millónes de parametros con calidad decente (quantizado a 4 bits), necesitas aproximadamente X * 0.7 GB de VRAM. Ej: Llama 3 8B necesita ~5.6 GB de VRAM.

---

## 4. La Matematica de los Costos: Cómo Leer una Tabla de Precios

> Abri las calculadoras. Esto es lo que separa a un usuario de un Ingeniero de IA.

### 4.1 Anatomia de una tabla de precios

Cuando entras a la página de precios de OpenAI, Anthropic o cualquier proveedor, ves algo asi:

```
Modelo: GPT-4o
├── Input:  $2.50  / 1M tokens    ← Lo que pagás por lo que vos escribis
├── Output: $10.00 / 1M tokens    ← Lo que pagás por lo que la IA escribe
└── (Precios en USD, antes de impuestos)
```

**¿Qué significa "1M tokens"?** 1M = 1 millón de tokens.

Para que te des una idea de escala:

| Cantidad de texto | Tokens aprox. | Costo input GPT-4o | Costo input GPT-4o-mini |
|-------------------|---------------|---------------------|------------------------|
| Un tuit (280 caracteres) | ~70 tokens | $0.000175 USD | $0.0000105 USD |
| Un mail de 200 palabras | ~270 tokens | $0.000675 USD | $0.0000405 USD |
| Una página A4 (500 palabras) | ~670 tokens | $0.001675 USD | $0.0001005 USD |
| Un articulo de 2000 palabras | ~2,670 tokens | $0.006675 USD | $0.0004005 USD |
| Un libro de 200 páginas | ~133,000 tokens | $0.3325 USD | $0.01995 USD |
| La Biblia entera | ~780,000 tokens | $1.95 USD | $0.117 USD |
| 1 millón de tokens | 1,000,000 tokens | $2.50 USD | $0.15 USD |

> **Ojo:** Los precios parecen minúsculos por consulta. Pero cuando tu app hace **miles o millónes de consultas por mes**, esos centavos se multiplican. Un ingeniero piensa en **costo total mensual, no en costo por consulta**.

### 4.2 Comparativa de precios de referencia (verificar en el sitio oficial al momento de usar)

> **Nota importante:** Estos precios cambian. Las empresas de IA bajan precios constantemente (en 2023 costaba 10x más que hoy). Siempre verifica en la página oficial antes de hacer un presupuesto definitivo.

| Proveedor | Modelo | Input / 1M tokens | Output / 1M tokens | ¿Para qué sirve? |
|-----------|--------|-------------------|---------------------|------------------|
| **OpenAI** | GPT-4o | $2.50 | $10.00 | Tareas complejas, razónamiento, creatividad |
| **OpenAI** | GPT-4o-mini | $0.15 | $0.60 | Tareas simples, clasificación, chatbots |
| **Anthropic** | Claude 3.5 Sonnet | $3.00 | $15.00 | Razonamiento profundo, textos largos, analisis |
| **Anthropic** | Claude 3 Haiku | $0.25 | $1.25 | Rapido, barato, tareas simples |
| **DeepSeek** | DeepSeek-V3 | $0.27 | $1.10 | **El shock asiatico:** calidad cercana a GPT-4o a ~1/10 del precio |
| **DeepSeek** | DeepSeek-R1 | $0.55 | $2.19 | Razonamiento (modelo que "piensa" antes de responder) |
| **Alibaba** | Qwen-Max | ~$0.40 | ~$1.20 | Competidor chino de alta calidad, muy barato |
| **Google** | Gemini 1.5 Pro | $1.25 | $5.00 | Ventana de contexto de 1M tokens (gigante) |
| **Google** | Gemini 1.5 Flash | $0.075 | $0.30 | Muy barato y rápido |
| **Meta** | Llama 3 70B (via API) | ~$0.90 | ~$1.50 | Open-source de alta calidad (precios via proveedores como Groq/Together) |
| **Meta** | Llama 3 8B (via API) | ~$0.06 | ~$0.10 | Ultra barato, ideal para clasificación y tareas simples |

**El shock asiatico: DeepSeek y Qwen**

Entre finales de 2024 y comienzos de 2025, empresas chinas (DeepSeek, Alibaba con Qwen) lanzaron modelos que compiten en calidad con GPT-4o y Claude, pero a **1/10 del precio** (o menos). ¿Cómo lo logran?

- **Eficiencia técnica:** Innovaciones en arquitectura (Mixture of Experts, Multi-head Latent Attention) que hacen que el modelo use menos cálculos.
- **Menos costo de entrenamiento:** Infraestructura mas barata, menos restricciónes regulatorias.
- **Estrategia de mercado:** Precios bajos para ganar participacion de mercado global.

> **Leccion para el ingeniero:** El precio de la IA se desploma cada 6 meses. Lo que hoy es caro, maniana es barato. Siempre compara precios antes de elegir proveedor. No te cases con uno solo.

### 4.3 Ejercicio practico en vivo: "¿Cuanto me cuesta que la IA lea un libro de 200 páginas y me haga un resumen de 5 páginas?"

Vamos a calcularlo paso a paso con distintos modelos.

**Paso 1: Estimar tokens de entrada (el libro)**

- 200 páginas × 500 palabras/página = 100,000 palabras.
- 100,000 palabras / 0.75 = **~133,000 tokens** (regla de oro para español).

**Paso 2: Estimar tokens de salida (el resumen)**

- 5 páginas × 500 palabras/página = 2,500 palabras.
- 2,500 palabras / 0.75 = **~3,333 tokens**.

**Paso 3: Calcular costo con cada modelo**

| Modelo | Costo Input | Costo Output | **Costo Total** |
|--------|-------------|--------------|-----------------|
| GPT-4o | 133K × $2.50/1M = $0.33 | 3,333 × $10.00/1M = $0.033 | **$0.36 USD** |
| GPT-4o-mini | 133K × $0.15/1M = $0.02 | 3,333 × $0.60/1M = $0.002 | **$0.022 USD** |
| Claude 3.5 Sonnet | 133K × $3.00/1M = $0.40 | 3,333 × $15.00/1M = $0.05 | **$0.45 USD** |
| Claude 3 Haiku | 133K × $0.25/1M = $0.033 | 3,333 × $1.25/1M = $0.004 | **$0.037 USD** |
| DeepSeek-V3 | 133K × $0.27/1M = $0.036 | 3,333 × $1.10/1M = $0.004 | **$0.04 USD** |

**Conclusion:** Resumir un libro de 200 páginas cuesta entre **2 centavos de dólar** (GPT-4o-mini) y **45 centavos** (Claude Sonnet). La diferencia es 20x. Y la calidad del resumen... ¿vale 20x más? Para muchos casos, probablemente no.

### 4.4 El costo del Contexto (revisitado con números)

> **El verdadero peligro no es el costo de una consulta. Es el costo del CONTEXTO que arrastras.**

**Escenario:** Estas construyendo un asistente legal que analiza contratos. Cada vez que un usuario hace una pregunta, tu sistema envia:

1. Los últimos 3 contratos analizados como "contexto historico": ~45,000 tokens.
2. La pregunta nueva del usuario: ~200 tokens.
3. **Total input por consulta:** 45,200 tokens.

El usuario pregunta: "¿Cuál es la clausula de confidencialidad?" La respuesta es: "La clausula 7, página 3." (~100 tokens).

**Costo de esa consulta simple con GPT-4o:**

- Input: 45,200 × $2.50/1M = **$0.113 USD**
- Output: 100 × $10.00/1M = **$0.001 USD**
- **Total: $0.114 USD** — para responder "lee la clausula 7".

**Ahora multiplica por 1000 consultas al dia:**

- 1,000 × $0.114 = **$114 USD/dia**
- $114 × 30 = **$3,420 USD/mes**

**Por responder preguntas que un indice de documentos resolveria en segundos.**

> **Solucion del ingeniero:** No mandes todo el historial en crudo. Usa un sistema de búsqueda (RAG, embeddings) para encontrar SOLO los documentos relevantes y mandar solo esos. En vez de 45,000 tokens de contexto, mandás 2,000. El costo baja 22x. Esto lo aprendes en las Clases 12, 13 y 14.

---

## 5. Costos Ocultos y Limites de Ingenieria

El precio del token es solo la punta del iceberg. Hay costos que no aparecen en la tabla de precios pero que pueden arruinar tu proyecto.

### 5.1 Rate Limits (Limites de tasa): RPM y TPM

> Las APIs no te dejan enviar infinitos pedidos por segundo, aúnque tengas dinero.

| Metrica | Significado | Ejemplo |
|---------|-------------|---------|
| **RPM** | Requests Per Minute — pedidos por minuto | Maximo 500 RPM en GPT-4o (plan basico) |
| **TPM** | Tokens Per Minute — tokens por minuto | Maximo 200,000 TPM en GPT-4o (plan basico) |

**¿Qué pasa si excedes el límite?** La API te devuelve un error `429 Too Many Requests`. Tu aplicación deja de funciónar.

**Analogía del peaje:** La autopista tiene 5 cabinas de peaje. Si llegan 5 autos por minuto, todo fluye. Si llegan 100, se forma una cola. Si llegan 1000, la autopista colapsa. Los rate limits son la cantidad de cabinas de peaje que el proveedor te asigna.

**¿Cómo se solucióna?**

- **Retry con backoff exponencial:** Si la API falla, tu programa espera 1 segundo, reintenta. Si falla de nuevo, espera 2s, 4s, 8s, 16s... hasta que funcióne.
- **Batch processing:** En lugar de mandar 1000 pedidos en 1 minuto, los encolas y los procesás de a 50 por minuto.
- **Aumentar el tier:** Si pagás mas (planes empresariales), los rate limits suben. Los planes enterprise de OpenAI tienen límites mucho más altos.

### 5.2 Latencia (El tiempo de espera)

> **Un modelo más barato a veces responde más lento. Y eso arruina la experiencia de usuario.**

| Modelo | Latencia tipica (por respuesta corta) | Latencia tipica (respuesta larga) |
|--------|--------------------------------------|-----------------------------------|
| GPT-4o-mini | ~1-2 segundos | ~5-10 segundos |
| GPT-4o | ~2-4 segundos | ~10-20 segundos |
| Claude 3.5 Sonnet | ~2-5 segundos | ~10-25 segundos |
| Claude 3 Haiku | ~0.5-1 segundo | ~3-5 segundos |
| DeepSeek-V3 | ~3-7 segundos | ~15-30 segundos |

**¿Por qué importa la latencia?**

- **Chatbots de atención al cliente:** Si el cliente espera mas de 3 segundos, se impacienta. Necesitas un modelo rápido (Haiku, GPT-4o-mini).
- **Procesamiento por lotes nocturno:** Si procesás documentos a las 3 AM y nadie esta esperando, la latencia no importa. Usa el modelo más barato.
- **Aplicaciones en tiempo real (voz):** Si estás construyendo un asistente por voz, necesitas latencia < 1 segundo. Solo los modelos más rápidos o locales sirven.

**Truco de ingeniero: streaming.** Las APIs permiten recibir la respuesta por partes (token por token), en lugar de esperar la respuesta completa. El usuario ve el texto aparecer en tiempo real, como si la IA "estuviera pensando". Esto mejora la percepción de velocidad aúnque la latencia total sea la misma.

### 5.3 El costo del Hardware Local (VRAM)

> **VRAM** = Video RAM. Es la memoria de la tarjeta grafica (GPU). Ahi se carga el modelo de IA para correr en local.

**Analogía de la mesa de trabajo:** La VRAM es el tamano de tu mesa de trabajo. El modelo es un plano gigante que necesitas desplegar. Si tu mesa es muy chica, el plano no entra y no podés trabajar. Si entra justo, trabajas incomodo y lento. Si tu mesa es grande, trabajas fluido.

**¿Cuánta VRAM necesito?**

| Modelo | Parametros | VRAM necesaria (quantizado 4-bit) | VRAM necesaria (precisión completa) | ¿Corre en...? |
|--------|------------|-----------------------------------|--------------------------------------|---------------|
| Llama 3 8B | 8B | ~6 GB | ~16 GB | Notebook gamer (RTX 3060/4060) |
| Mistral 7B | 7B | ~5 GB | ~14 GB | Notebook gamer |
| Llama 3 70B | 70B | ~40 GB | ~140 GB | Servidor con GPU empresarial |
| DeepSeek-V3 | 671B (37B activos) | ~80 GB+ | Imposible en una sola GPU | Multiples GPUs o solo via API |
| GPT-4o, Claude | No públicos | No disponible | No disponible | Solo via API |

**¿Qué pasa si no tengo suficiente VRAM?**

- El modelo no carga (error de memoria).
- O carga, pero usa RAM del sistema en lugar de VRAM. **La velocidad se desploma 10x-50x.** Un modelo que generaría 50 tokens/segundo pasa a generar 2 tokens/segundo.
- La computadora se vuelve inusable mientras el modelo corre (toda la memoria esta ocupada).

> **Regla práctica:** Si querés experimentar con IA local, una GPU con 12 GB de VRAM (como una RTX 3060/4060) es el punto de entrada razónable. Cuesta ~$300 USD y corre modelos de hasta 13B parametros comodamente. Para modelos de 70B+, necesitas hardware de estacion de trabajo o servidor.

---

## 6. Laboratorio de Costos y Tarea para la Casa

### 6.1 La Calculadora de Tokens (herramienta)

Antes de mandar un prompt a producción, necesitas saber cuántos tokens vas a gastar. Las herramientas gratuitas:

- **OpenAI Tokenizer:** `platform.openai.com/tokenizer` — Pegas texto y te dice cuantos tokens son. Exacto, para modelos OpenAI.
- **Anthropic Console:** `console.anthropic.com` — Similar, para modelos Claude.

**Regla rápida (sin herramienta):**

- Toma el texto.
- Cuenta los caracteres (incluyendo espacios).
- Dividi por 4 para inglés, por ~3.2 para español.
- Redondea para arriba.

**Ejemplo:** "La inteligencia artificial es una herramienta poderosa." = 56 caracteres (con espacios) / 3.2 ≈ 17 tokens.

### 6.2 El Presupuesto del Proyecto (ejercicio principal para la Clase 4 práctica y tarea)

Este es tu primer trabajo como Ingeniero de IA: **elegir el modelo correcto para un caso de negocio real.**

#### El caso de negocio

> Una empresa de e-commerce te contrata para construir un **chatbot de atención al cliente**. El chatbot debe:
>
> - Atender **500 consultas por dia** (30 dias al mes = 15,000 consultas/mes).
> - Cada consulta del cliente tiene en promedio **200 palabras**.
> - Cada respuesta de la IA tiene en promedio **100 palabras**.
> - Además, para dar contexto, el sistema envia las **últimas 3 interacciones** del cliente con soporte (~100 palabras cada una = 300 palabras adicionales por consulta).
> - El presupuesto máximo para la API de IA es de **$100 USD por mes**.

#### ¿Que tenés que hacer?

1. **Calcular tokens por consulta:**
   - Input: (200 palabras del cliente + 300 palabras de contexto historico) = 500 palabras → ~667 tokens.
   - Output: 100 palabras → ~133 tokens.

2. **Calcular tokens mensuales:**
   - Input: 667 × 15,000 consultas = 10,005,000 tokens (~10M).
   - Output: 133 × 15,000 consultas = 1,995,000 tokens (~2M).

3. **Calcular costo mensual con cada API:**

| Modelo | Costo Input (10M tokens) | Costo Output (2M tokens) | **Costo Mensual Total** | ¿Dentro de los $100? |
|--------|--------------------------|--------------------------|------------------------|---------------------|
| GPT-4o | 10 × $2.50 = $25.00 | 2 × $10.00 = $20.00 | **$45.00 USD** | ✅ Si |
| GPT-4o-mini | 10 × $0.15 = $1.50 | 2 × $0.60 = $1.20 | **$2.70 USD** | ✅ Sobrado |
| Claude 3.5 Sonnet | 10 × $3.00 = $30.00 | 2 × $15.00 = $30.00 | **$60.00 USD** | ✅ Si |
| Claude 3 Haiku | 10 × $0.25 = $2.50 | 2 × $1.25 = $2.50 | **$5.00 USD** | ✅ Sobrado |
| DeepSeek-V3 | 10 × $0.27 = $2.70 | 2 × $1.10 = $2.20 | **$4.90 USD** | ✅ Sobrado |

4. **¿Cuál elegís y por que?** Redacta una justificación.

#### Preguntas de reflexión

1. Si GPT-4o cuesta $45/mes y DeepSeek-V3 cuesta $4.90/mes, ¿que justificaría elegir GPT-4o?
2. ¿Qué pasaría con el costo si el 10% de las consultas requieren respuestas de 500 palabras en lugar de 100? (Ej: casos complejos que escala a un humano).
3. ¿Qué pasaría si la empresa crece a 5,000 consultas por dia en 6 meses? Recalcula los costos.
4. ¿Conviene mandar siempre las últimas 3 interacciones como contexto o solo cuando la consulta lo requiere?
5. ¿En que situación usarías un modelo local (Ollama) para este proyecto?

### 6.3 Tarea para la Clase 4

1. **Investiga los precios actualizados** de al menos 3 APIs de IA (OpenAI, Anthropic, DeepSeek, Google, etc.). Anota los precios reales de hoy (porque este documento puede desactualizarse).
2. **Usa la herramienta de tokenización de OpenAI** (`platform.openai.com/tokenizer`) para tokenizar 3 textos distintos: un mail corto (100 palabras), un articulo de noticias (1000 palabras), y la letra de tu cancion favorita. Compara el resultado con la regla de oro (caracteres / 3.2) y anota la diferencia.
3. **Completa el presupuesto del proyecto** (seccion 6.2) con tus cálculos detallados y tu justificación de elección de modelo.
4. **Lee sobre Ollama:** Que es, como se instala, qué modelos soporta. No hace falta instalarlo, solo leer la documentación. `ollama.com`

---

## 7. El Ingeniero de IA en esta clase

> El Ingeniero de IA es la persona que responde **"¿cuanto cuesta?"** antes de responder **"¿como se hace?"**.

En esta clase aprendiste las habilidades económicas fundamentales del rol:

### Sabe contar tokens
Antes de mandar un prompt, estima si le conviene enviar todo el texto o resumirlo primero. Sabe que 1 token ≈ 4 caracteres en inglés ≈ 0.75 de una palabra en español. Y sabe que generar texto (output) cuesta 3-5 veces más que leerlo (input).

### Elige la modalidad correcta
Nunca programa una app comercial dependiendo de una sesión de ChatGPT abierta en un navegador. Sabe que la única forma profesional de construir productos con IA es via API. Y sabe que para datos ultra-sensibles, existe la opción local (Ollama + modelo open-source).

### Optimiza costos
Sabe que para clasificar un texto corto (spam, categoria, sentimiento), un modelo pequenio y barato (Haiku, GPT-4o-mini, Llama 8B) hace el mismo trabajo que un modelo gigante y caro (GPT-4o). Sabe que la pregunta no es "¿cuál es el mejor modelo?" sino "¿cuál es el modelo suficiente para esta tarea?".

### Lee la letra chica
Entiende los Rate Limits y sabe diseñar sistemas que no se rompan cuando hay picos de trafico. Sabe que mandar 50 correos de contexto en cada consulta puede hacer que su aplicación quiebre en una semana, no por falta de usuarios, sino por exceso de tokens.

### Piensa en el costo total
No mira el costo por consulta ($0.0001). Mira el costo mensual del sistema completo (15,000 consultas/mes × $0.0001 = $1.50... o $1,500 si eligio mal el modelo y mando contexto de mas). Hace las cuentas antes de escribir una línea de código.

---

## 8. Cierre y puente a la Clase 4

En esta clase vimos:

- El **token** es la moneda con que pagás por usar IA. No es una palabra, no es una letra: es un trozo de texto que la IA "muerde" con su tokenizador.
- La **ventana de contexto** (8k, 32k, 128k) es la memoria a corto plazo. Llenarla cuesta dinero, y cuando se llena, la IA olvida lo más viejo sin avisar.
- Los **parametros** son los números ajustables del modelo. Mas parametros = más capacidad = mas costo. Pero para el 80% de las tareas, un modelo pequenio alcanza.
- Existen **3 modalidades**: Chat (minorista, no profesional), API (mayorista, la única forma de construir productos) y Local (soberanía, privacidad, sin costos por token).
- Leer una **tabla de precios** es simple: input/1M tokens + output/1M tokens. Y el output siempre es más caro.
- Los **costos ocultos** (rate limits, latencia, VRAM) pueden arruinar un proyecto aúnque el precio por token sea bajo.

### Proxima clase

**Clase 4: Vibe Coding — Programacion Dirigida por Lenguaje Natural.** Vas a escribir tus primeros programas usando IA, sin saber programar. Vas a ver cómo pedirle a una IA que escriba código por vos, cómo verificar que funcióne, y cómo iterar hasta que haga exactamente lo que necesitas.

### Tarea

1. Completa el laboratorio de la seccion 6 (presupuesto del proyecto).
2. Investiga precios actualizados de APIs.
3. Usa la herramienta de tokenización de OpenAI con 3 textos reales.
4. Lee sobre Ollama en `ollama.com`.

---

> **Recorda:** la diferencia entre un usuario y un Ingeniero de IA es que el ingeniero sabe cuánto cuesta cada token **antes** de enviar el prompt.
