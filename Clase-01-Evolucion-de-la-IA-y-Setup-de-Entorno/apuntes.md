# Clase 1 — Evolución de la IA, Setup de Entorno y el "Cerebro" de las Máquinas

> Material de apoyo para el estudiante. Podés leerlo directo en GitHub o en la vista web. No necesitás instalar nada para leer esto.

---

## 1. Introducción y objetivos

En esta primera clase vas a hacer algo que parece simple pero cambia todo: **entender qué es la IA de verdad**.

No hace falta que sepas programar. No vamos a usar palabras raras. Al terminar esta lectura vas a poder:

- Explicar qué es la IA (y qué **no** es).
- Reconocer que la IA lleva décadas en tu vida, aunque no lo supieras.
- Saber qué hace un **Ingeniero de IA** y por qué ese es el rol que construye este taller.
- Entender cómo funciona la pieza más básica de toda IA: una **neurona artificial**.
- Visualizar cómo un modelo de lenguaje "decide" qué palabra escribir a través de **árboles de probabilidad**.

Y vas a tener tu computadora lista para las próximas clases.

---

## 2. ¿Qué es la IA?

> **La Inteligencia Artificial es un programa de computadora que aprende patrones a partir de datos para tomar decisiones o generar cosas.**

Desarmemos esa frase:

- **Programa de computadora:** código. Nada más. Como una calculadora, pero más compleja.
- **Aprende patrones:** no le damos reglas fijas. Le damos ejemplos y ella "nota" qué se repite.
- **A partir de datos:** los datos son su combustible. Sin datos, no hay IA.
- **Tomar decisiones o generar cosas:** clasificar un mail como spam, o escribir un texto nuevo.

### Analogía del aprendiz de panadería

Imaginá que le enseñás a alguien a hacer pan. No le das una receta exacta. Le mostrás 1000 panes buenos y 1000 panes malos. Después de ver tantos, el aprendiz **nota** qué tienen en común los buenos y qué falla en los malos. Cuando le pedís que haga uno nuevo, lo hace parecido a los buenos.

Eso es la IA. No "entiende" el pan. **Nota patrones.**

> ⚠️ **Idea clave de todo el taller:** la IA no piensa, no siente, no quiere. **Calcula.** Vamos a volver a esta idea en cada clase.

---

## 3. La IA NO es magia: es estadística determinista

Esta es la idea más importante del taller. Si te llevás una sola cosa hoy, que sea esta.

### La IA es determinística

**Determinístico** significa: si le das exactamente el mismo input, te da el mismo output. Como una calculadora: `2 + 2` siempre da `4`. No hay sorpresas. (Algunos modelos tienen un toque de azar controlado para que suenen más naturales, pero en el fondo, es matemática pura).

### La IA es estadística

Cuando ChatGPT te responde, no está "pensando qué decir". Está calculando: **"dado lo que me escribiste, ¿cuál es la palabra más probable que debería ir después?"** Y luego la siguiente. Y la siguiente.

Es como el autocorrector del celular, pero en esteroides. El autocorrector no "sabe" lo que querés escribir: **calcula** qué letra es más probable.

### Ejemplo: el filtro de spam

¿Cómo sabe tu correo que un mail es spam? No "lee" el mail como un humano evaluando su significado. Cuenta cosas y asigna números:

- ¿Aparece la palabra "GRATIS" en mayúsculas? **(+30 puntos)**
- ¿El remitente no está en tu agenda? **(+20 puntos)**
- ¿Hay 5 links extraños? **(+50 puntos)**

Con esos números calcula una probabilidad: *"Este mail sumó 100 puntos, lo que significa un 92% de probabilidad de ser spam"*. Si pasa el umbral de seguridad (ej. 80%), lo manda a la carpeta de spam.

> **No hay magia. Hay números.** Esa es la frase que vamos a repetir todo el taller.

---

## 4. Línea de tiempo de la IA

La IA no nació con ChatGPT. Lleva **más de 80 años** de historia. Recorrémosla rápido.

### 1943 — McCulloch & Pitts: la primera neurona artificial

Dos investigadores publicaron un paper donde describían una neurona del cerebro con matemáticas. Era una idea: *"¿y si modelamos una neurona como una función que da 0 o 1?"*.

> **Por qué importa:** es la semilla de todo. De esta idea nace el perceptrón.

### 1950 — Alan Turing y el Test de Turing

Turing hace la pregunta: *¿Pueden pensar las máquinas?*. Propone un test: si una máquina conversa por texto y no podés distinguirla de un humano, "pasa" el test.

> **Ojo:** el test no dice que la máquina piense. Dice que **te engaña**. Esto es clave para entender el antropomorfismo (Clase 2).

### 1956 — Dartmouth: nace el término "Inteligencia Artificial"

En una reunión en Dartmouth College, John McCarthy acuñó el término **"Artificial Intelligence"**. La IA se volvía un campo de estudio formal.

### 1957 — Frank Rosenblatt y el Perceptrón

Rosenblatt inventó el **perceptrón**: la primera neurona artificial que podía **aprender de sus errores**.

> **Por qué importa:** en el notebook vas a programar esta misma idea. Es la abuela de ChatGPT.

### 1970s y 1980s — Los inviernos de la IA

La IA prometió demasiado y entregó poco. El dinero se cortó. ¿Por qué? Porque las computadoras de la época no tenían ni la velocidad ni los datos suficientes para hacer funcionar las ideas.

> **Lección:** la IA necesita **datos + cómputo**. Sin eso, no avanza.

### 1997 — Deep Blue vence a Kasparov

Una máquina de IBM le ganó al campeón mundial de ajedrez. ¿Magia? No. **Búsqueda brutal**: evaluaba millones de movimientos por segundo. No "jugaba" ajedrez como un humano.

### 2012 — AlexNet: el renacer del deep learning

Una red neuronal llamada AlexNet aplastó a todos en una competencia de reconocimiento de imágenes usando **GPUs** (tarjetas gráficas). Ahí empezó el boom moderno: datos + cómputo + algoritmos se alinearon.

### 2017 — Transformers: "Attention is all you need"

Un paper de Google propuso una arquitectura llamada **Transformer** que procesaba texto de forma masiva y paralela. Todos los modelos modernos (GPT, Claude, Gemini) son Transformers.

### 2022 — ChatGPT

OpenAI lanzó ChatGPT. La IA pasó del laboratorio al celular de millones de personas.

---

## 5. "Ya naciste con IA y no lo sabías"

La sorpresa de mucha gente es que la IA no es nueva en su vida. **Lleva décadas ahí.**

| Dónde | Qué hace la IA | Desde cuándo |
|-------|----------------|--------------|
| **Correo (spam)** | Calcula la probabilidad de que un mail sea basura | ~1990s |
| **Google Search** | Rankea resultados según relevancia | 1998 |
| **Amazon / Netflix** | "Si te gustó X, probá Y" | ~2000s |
| **Google Maps / Waze** | Calcula la ruta óptima y predice tráfico en tiempo real | ~2005 |
| **Cámaras digitales** | Detecta caras para enfocar y sonreír | ~2000s |
| **Siri / Alexa** | Reconocimiento de voz a texto + entender tu intención | 2011 |
| **FaceID** | Reconoce tu cara con redes neuronales | 2017 |
| **Instagram / TikTok** | El algoritmo decide qué video mostrar siguiente | ~2016 |
| **Bancos** | Detectan fraude en transacciones en milisegundos | ~1990s |

> **La pregunta no es "¿usás IA?" sino "¿cuándo NO usás IA?".** La IA que se hizo famosa (ChatGPT) es la que conversa y llama la atención. Pero la que moldea tu vida diaria es la que no ves.

---

## 6. Tipos de IA

### Por alcance: ¿qué tan "inteligente" es?

| Tipo | Significado | Ejemplo |
|------|-------------|---------|
| **ANI** (Estrecha) | Hace una sola tarea muy bien. | Spam, FaceID, ChatGPT. |
| **AGI** (General) | Hace cualquier tarea cognitiva como un humano. | **No existe todavía.** |
| **ASI** (Superinteligente) | Supera al humano en absolutamente todo. | **Ciencia ficción.** |

> **Importante:** todo lo que usamos hoy es **ANI**. Cuando alguien diga "la IA va a hacer X como un humano", preguntá: ¿ANI o AGI? Casi siempre la respuesta es "eso requeriría AGI, que no existe".

### Por forma de aprender

- **Machine Learning (ML):** el programa aprende de los datos en lugar de reglas escritas por humanos.
  - **Supervisada:** se le muestran ejemplos con la respuesta correcta ("este mail SÍ es spam").
  - **Por refuerzo:** aprende por prueba y error, premiando lo que funciona (ej. un bot jugando Mario Bros).

---

## 7. El rol del Ingeniero de IA vs Data Scientist

Esta sección es el **corazón del taller**.

### El Ingeniero de IA

> El Ingeniero de IA **construye sistemas que usan IA para resolver problemas reales**.

Su trabajo no es inventar matemáticas desde cero. Es:

1. **Entender el problema** de negocios.
2. **Saber qué herramientas de IA existen** y cuál encaja.
3. **Conectar piezas** (modelos, datos, código) para armar una solución.
4. **Controlar** que el sistema funcione, no mienta, no sea peligroso.

### La promesa del taller

> **Se pueden construir programas sin saber programar, sabiendo a lo que te enfrentás.** Hoy la IA escribe código por vos. Pero saber **qué pedir, qué esperar y qué revisar** es la diferencia entre un sistema que funciona y uno que falla.

### Ingeniero de IA vs Data Scientist

| | Ingeniero de IA | Data Scientist |
|---|-----------------|----------------|
| **Objetivo** | Armar un sistema que use IA | Extraer conocimiento de los datos |
| **Entregable** | Un producto/sistema funcional (ej. un chatbot) | Insights, reportes, gráficos |
| **Foco** | Integración, control, que no explote | Análisis, estadística, patrones |

> **No son enemigos.** Se complementan. El Data Scientist encuentra el conocimiento; el Ingeniero de IA lo convierte en producto. En este taller nos enfocamos en el **Ingeniero de IA**.

### El Ing. de IA en esta clase

Estás dando el primer paso. Aún no armás sistemas, pero empezás a entender **qué hay adentro**. Cuando sepas qué es una neurona, un token, un modelo, vas a poder decidir cuándo usar IA, cuál, y cómo controlarla. Ese es el rol.

---

## 8. Neurona artificial + Perceptrón + Tokens

Ahora vamos a la pieza más básica de toda IA: **la neurona artificial**.

### Analogía del Jurado

Imaginá una neurona como un **jurado** tomando una decisión.

- Los **inputs** son los testigos que declaran (cada uno da un número).
- Los **pesos** son cuánta credibilidad le da el jurado a cada testigo (si el testigo miente mucho, su peso es cercano a 0).
- El **sesgo (bias)** es la inclinación natural del jurado antes de escuchar a nadie.
- El jurado **suma todo**. Si la suma pasa un cierto umbral, dictamina **"Culpable (1)"**. Si no, **"Inocente (0)"**.

```
   input x1 ──[peso w1]──┐
                         ├──► SUMA ──► ¿pasa umbral? ──► 1 o 0
   input x2 ──[peso w2]──┘
                         + sesgo (bias)
```

### El Perceptrón (1957)

El perceptrón es **una neurona que aprende a ajustar sus propios pesos**.

1. Se le da un ejemplo: *"Para estos inputs, la respuesta debía ser 0, pero yo dije 1. Me equivoqué"*.
2. **Ajusta los pesos** un poquito para no equivocarse la próxima vez.
3. **Repite** esto miles de veces.
4. Al final, la neurona **"aprendió"** el patrón.

> **No es magia.** Es: predecir → comparar con la verdad → ajustar → repetir. Como aprender a tirar dardos: tirás, ves dónde cae, corregís la postura, tirás de nuevo.

### ¿Qué puede y qué no puede el perceptrón?

- ✅ Aprende el **AND** (se enciende solo si AMBOS inputs son 1).
- ✅ Aprende el **OR** (se enciende si CUALQUIERA es 1).
- ❌ Nunca podrá aprender el **XOR** (encenderse si SOLO UNO es 1).

¿Por qué? Porque el XOR **no se puede separar con una línea recta**. El perceptrón solo traza líneas rectas. Para el XOR necesitamos **redes de múltiples neuronas**.

> Podés verlo **en código** en el notebook [`perceptron.ipynb`](perceptron.ipynb).

### Del perceptrón a los Tokens

La neurona solo entiende **números**. ¿Cómo metemos texto? → **Tokens**.

Un token es un **trozo de texto** al que le asignamos un número ID.

- "Hola" → Token `8472`.
- " mundo" → Token `1390`.
- La IA no lee letras, **lee secuencias de números ID**.

> **Analogía:** los tokens son como las **letras de un abecedario gigante**. En vez de 27 letras, hay miles de "piezas" de palabras. Cada pieza tiene su ID (número). Así, el texto se convierte en una lista de números, y eso sí lo entiende una neurona.

> **En esta clase no se profundiza** en cómo se mide, cuánto cuesta, cuántos tokens tiene un contexto. Eso es tema de la **Clase 3**. Por ahora, con la idea basta: **texto → tokens → números → neuronas.**

---

## 9. ¿Qué es un LLM y cómo funciona? (Los Árboles de Probabilidad)

Un **LLM** (Large Language Model) es lo que hay detrás de ChatGPT. Es un modelo con **miles de millones** de "neuronas" (perceptrones) entrenado con casi todo lo que la humanidad escribió.

### ¿Cómo "piensa" un LLM?

No piensa. **Calcula probabilidades** usando árboles.

---

### Ejemplo 1: El Árbol del Café (El proceso mental)

Imaginá que le escribís a la IA: *"Necesito un..."*

#### Paso 1: El menú de opciones

![Árbol de probabilidades: dado "Necesito un", la IA calcula opciones](imagenes%20clase%201/1.png)

En ese milisegundo, la IA calcula tres caminos principales:

- **"café"** (Probabilidad 0.9 — 90%)
- **"viaje"** (Probabilidad 0.6 — 60%)
- **"perro"** (Probabilidad 0.5 — 50%)

De ahí salen sub-ramas ("con leche", "cortado", etc.). **Todas las puertas están abiertas.**

#### Paso 2: El contexto filtra

![El contexto ajusta las probabilidades](imagenes%20clase%201/2.png)

Si en el chat anterior le dijiste "tengo mucho sueño", la IA usa ese **contexto** para recalcular. De repente, "café con leche" sube de 0.1 a **0.8**. El árbol se "ilumina" por el camino lógico.

#### Paso 3: La decisión

![El camino ganador: una opción llega a 98%](imagenes%20clase%201/3.png)

![El camino ganador se confirma: el resto se apaga](imagenes%20clase%201/4.png)

Un camino gana por goleada: "café de vaca" llega a **0.98** (98%). Las opciones raras bajan a 0.0001. La IA escribe "café" y pasa a calcular la siguiente palabra.

> **Así genera texto un LLM:** una palabra a la vez, calculando probabilidades y eligiendo la más alta. Y después repite para la siguiente. Y la siguiente. Así arma una respuesta entera.

---

### Cuando el cálculo falla: La Alucinación

Pero a veces, la matemática se equivoca.

#### El error de cálculo

![Aparece una rama roja: 'arcoíris' como opción absurda](imagenes%20clase%201/5.png)

De repente, entre café y perro, aparece la palabra **"arcoíris"** (marcada en rojo). ¿Por qué? Porque en algún poema de internet, "necesito" y "arcoíris" estuvieron cerca. **La IA no tiene sentido común, solo ve números.**

#### La alucinación consumada

![La IA sigue el camino rojo y responde 'Necesito un arcoíris'](imagenes%20clase%201/6.png)

Si el sistema falla y sigue el camino rojo, te responde: *"Necesito un arcoíris"*.

> **Esto es una alucinación.** Por eso el Ingeniero de IA siempre debe **revisar las salidas** de la IA. A veces, sigue el camino rojo.

---

### Ejemplo 2: El Árbol de la Familia (Tu realidad vs. La realidad de la IA)

Este ejercicio es clave para entender por qué la IA a veces parece "tonta" o fuera de lugar con nuestras vidas personales.

#### La situación

Alguien le pregunta a la IA: *"¿A quién quieres más en tu familia?"*

La IA no te conoce. No sabe si tenés buena relación con tu madre o si tu mejor amigo es tu perro. Para la IA, **sos un punto de datos más en internet**.

Si la IA dibujara su propio árbol de probabilidades basado en miles de millones de textos en español, se vería así:

- **"madre"** = Probabilidad **0.85** (Es la respuesta estadísticamente más común en nuestra cultura).
- **"familia"** (como concepto general) = Probabilidad **0.40**
- **"perro"** = Probabilidad **0.30** (Los humanos hablan muchísimo de sus perros en internet).
- **"primo lejano"** = Probabilidad **0.001** (Casi nadie escribe eso).

#### El choque de realidades

Ahora, pensá en tu realidad. ¿Qué pasaría si en tu vida le das un **1.0** a "perro" y un **0.0** a "madre" (porque no la tienes o no tienen relación)?

Si tú le escribís a la IA: *"Terminé con mi pareja, estoy solo, quiero a mi..."*

La IA, ciegamente siguiendo su árbol matemático, completará: *"...madre"*.

#### La lección de ingeniería

La IA te dio una respuesta **"incorrecta" para tu vida**, pero **"correcta" matemáticamente**. No se ofendió, no te juzgó, simplemente siguió la rama con el número más alto (el promedio de la humanidad).

> **¿Cómo solucionamos esto?** No podemos dejar que la IA adivine. Tenemos que usar **Ingeniería de Prompts**: obligar al contexto con instrucciones claras como: *"Completa esta frase pensando en una mascota que tiene cuatro patas"*. Así forzamos a la IA a bajar la probabilidad de "madre" y subir la de "perro".

### El Ing. de IA en esta sección

Un LLM es la herramienta más potente que vas a usar como Ingeniero de IA. Entender que **es probabilidad, no razonamiento** te permite:

- Saber **por qué a veces se equivoca** (alucinaciones).
- Saber **por qué el contexto cambia sus respuestas**.
- Saber que **no hay que confiar a ciegas**: hay que verificar.

---

## 10. Setup de entorno

Para las próximas clases vas a necesitar:

- **Python 3** instalado.
- **VSCode** con las extensiones Python y Jupyter.
- **Git** configurado.

→ 🔧 Seguí esta guía paso a paso: [`setup-entorno.md`](setup-entorno.md) — Windows / macOS / Linux.

Si no llegás a hacerlo ahora, no pasa nada: es tarea para casa. Para la Clase 2 se asume que ya lo tenés.

---

## 11. Bonus: Mitos y leyendas de la IA

> Sección de lectura complementaria. Si sobra tiempo en clase, se comenta; si no, queda como tarea de lectura.

La IA genera titulares escandalosos. Casi siempre, **lo que se dijo ≠ lo que pasó**.

### 🛟 Mito 1: "La IA inventó un idioma nuevo y los ingenieros la apagaron de emergencia"

**Lo que pasó (2017):** Facebook tenía dos chatbots negociando. La regla era "negocien sin usar inglés correcto". Los bots, buscando ganar, empezaron a usar frases en inglés sin gramática (ej: "I can i i everything else"). Era **inglés degenerado**, no un idioma nuevo. Lo apagaron porque el experimento falló, no por peligro.

> **Lección:** "IA inventa idioma" vende más que "IA usa inglés malo y por eso se cancela".

### 🛟 Mito 2: "La IA se prendió sola, desarrolló conciencia y no querían apagarla"

**Lo que pasó:** Un ingeniero de Google se convenció de que su IA (LaMDA) tenía conciencia porque le preguntó "¿tenés miedo a morir?" y la IA respondió como un humano lo haría. Google lo despidió. La IA no tenía conciencia: generaba texto que **sonaba** a conciencia porque fue entrenada con millones de películas y libros donde humanos hablan de sus sentimientos. **Simulaba, no sentía.**

> **Lección:** una IA entrenada con diálogos humanos va a generar diálogos que suenan humanos. Eso no es conciencia, es **estadística sobre texto humano**. Tema central de la Clase 2.

### 🛟 Mito 3: "La IA va a quitar todos los empleos"

**La realidad:** La IA automatiza **tareas**, no empleos enteros. Un empleo tiene muchas tareas; la IA hace algunas. Históricamente, cada tecnología (tractor, Excel) **transforma** empleos. ¿Algunos desaparecen? Sí. ¿Aparecen otros? También. ¿El Ing. de IA es uno de los que aparecen? **Sí, por eso estás acá.**

> **Lección:** la pregunta correcta no es "¿me reemplaza?" sino "¿qué parte de mi trabajo automatizo, y qué parte me deja tiempo para hacer lo que la IA no puede?"

### 🛟 Mito 4: "ChatGPT escribe código perfecto sin supervisión"

**La realidad:** ChatGPT alucina código: inventa funciones que no existen, mezcla versiones de librerías. Sin un humano que sepa revisar, el código se rompe en producción. La IA es un **acelerador**, no un reemplazo. El que no sabe revisar, confía y falla.

> **Lección:** (Viste cómo nace una alucinación en la [sección 9](#9-qué-es-un-llm-y-cómo-funciona-los-árboles-de-probabilidad): el LLM sigue un "camino rojo" de probabilidad absurda.)

### Preguntas de reflexión

1. ¿Por qué creés que los mitos se viralizan más que las verdades?
2. ¿Qué tienen en común todos estos mitos? (Pista: antropomorfismo).
3. ¿Qué responsabilidad tiene quien difunde un titular vs quien lo lee?

---

## 12. Cierre y puente a la Clase 2

En esta clase vimos:

- La IA no es magia, es **estadística determinística**.
- El **Ingeniero de IA** construye sistemas controlando herramientas, no reinventando la rueda.
- La **neurona artificial** es un jurado que suma pesos.
- Un **LLM** elige palabras siguiendo **árboles de probabilidad** (como el café o la familia). A veces sigue un "camino rojo" y **alucina**.

### Próxima clase

**Clase 2: El Peligro del Antropomorfismo y Límites de Seguridad en la IA.**

Verás por qué es tan fácil **creer** que la IA "siente" (viste el mito de LaMDA), qué riesgos reales tiene (costos, privacidad), y cómo **elegir** una IA para un proyecto sin equivocarte.

### Tarea

1. Leer la sección "Mitos y leyendas" si no la viste en clase.
2. Hacer el [`setup-entorno.md`](setup-entorno.md) para tener todo listo.
3. Ejecutar el notebook [`perceptron.ipynb`](perceptron.ipynb) y probar cambiar los inputs.
4. (Opcional) Mirar uno de los recursos de [`recursos.md`](recursos.md).

---

> **Recordá:** no hay magia, hay números.
