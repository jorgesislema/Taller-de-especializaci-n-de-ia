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

### Primero: ¿Qué es la "inteligencia"?

Antes de hablar de IA, necesitamos entender qué significa "inteligencia". No es una palabra mágica. En términos simples:

> **Inteligencia es la capacidad de resolver problemas, aprender de la experiencia y adaptarse a situaciones nuevas.**

Cuando un bebé aprende a caminar, está siendo inteligente: prueba, se cae, ajusta, vuelve a intentar. Cuando resolvés un rompecabezas, usás inteligencia. Cuando adaptás tu ruta al trabajo porque hay tráfico, también.

La inteligencia tiene varias capacidades asociadas:

- **Aprender** de experiencias pasadas.
- **Razonar** para llegar a conclusiones.
- **Reconocer patrones** (ej: "esta cara me suena").
- **Resolver problemas** nuevos que no viste antes.
- **Entender lenguaje** (hablado o escrito).

Ahora, la pregunta clave: *¿Puede una máquina hacer algo parecido a esto?*

La respuesta corta es: **puede imitar algunas de estas capacidades, pero de forma muy distinta a como lo hace un cerebro humano.** No "piensa" como vos. Calcula. Pero los resultados pueden parecerse tanto que es difícil distinguirlos.

### Entonces, ¿qué es la IA?

> **La Inteligencia Artificial es un programa de computadora que aprende patrones a partir de datos para tomar decisiones o generar cosas.**

Desarmemos esa frase:

- **Programa de computadora:** código. Nada más. Como una calculadora, pero más compleja.
- **Aprende patrones:** no le damos reglas fijas. Le damos ejemplos y ella "nota" qué se repite.
- **A partir de datos:** los datos son su combustible. Sin datos, no hay IA.
- **Tomar decisiones o generar cosas:** clasificar un mail como spam, o escribir un texto nuevo.

### La diferencia clave: inteligencia humana vs. inteligencia artificial

| Inteligencia Humana | Inteligencia Artificial |
|---------------------|------------------------|
| Entiende el **significado** de las cosas | Calcula **probabilidades** sobre patrones |
| Aprende de **pocas** experiencias | Necesita **miles o millones** de ejemplos |
| Tiene **sentido común** (sabe que el fuego quema) | No tiene sentido común (solo ve números) |
| Puede **razonar** sobre cosas que nunca vio | Solo funciona con lo que vio en entrenamiento |
| Usa **intuición** y emociones | No tiene intuición ni emociones |

> **Analogía:** la IA es como un estudiante que estudió para un examen con miles de preguntas de práctica. Si la pregunta es parecida a las que estudió, responde bien. Si es algo completamente nuevo, puede fallar estrepitosamente. Un humano, en cambio, puede razonar sobre lo nuevo.

### Analogía del aprendiz de panadería

Imaginá que le enseñás a alguien a hacer pan. No le das una receta exacta. Le mostrás 1000 panes buenos y 1000 panes malos. Después de ver tantos, el aprendiz **nota** qué tienen en común los buenos y qué falla en los malos. Cuando le pedís que haga uno nuevo, lo hace parecido a los buenos.

Eso es la IA. No "entiende" el pan. **Nota patrones.**

> ⚠️ **Idea clave de todo el taller:** la IA no piensa, no siente, no quiere. **Calcula.** Vamos a volver a esta idea en cada clase.

---

## 3. La IA NO es magia: es estadística (con componentes probabilísticos)

Esta es la idea más importante del taller. Si te llevás una sola cosa hoy, que sea esta.

### La IA es estadística

Cuando ChatGPT te responde, no está "pensando qué decir". Está calculando: **"dado lo que me escribiste, ¿cuál es la palabra más probable que debería ir después?"** Y luego la siguiente. Y la siguiente.

Es como el autocorrector del celular, pero en esteroides. El autocorrector no "sabe" lo que querés escribir: **calcula** qué letra es más probable.

La palabra clave es **probabilidad**. La IA no dice "esta es LA respuesta correcta". Dice "esta es la respuesta **más probable** dado todo lo que aprendí". Hay una diferencia enorme:

- **Determinista puro:** `2 + 2 = 4`. Siempre. Sin excepciones. Es matemática exacta.
- **Estadístico con componentes probabilísticos:** "Dado que el usuario escribió 'buenos días', la palabra más probable que sigue es '¿cómo estás?' con 73% de probabilidad, pero también podría ser '¿qué tal?' con 15%, o '¿todo bien?' con 8%".

### ¿Determinista o probabilístico? Los dos

En la práctica, la IA es **ambas cosas a la vez**:

- **Determinista en su estructura:** la arquitectura del modelo, los pesos que aprendió, las operaciones matemáticas... todo eso es fijo. Si corrés el mismo modelo dos veces con la misma entrada, en principio obtendrás lo mismo.
- **Probabilística en su salida:** cuando el modelo "elige" qué palabra poner, a menudo usa un proceso llamado **sampling** (muestreo), que introduce una componente de azar controlado. Por eso, si le hacés la misma pregunta dos veces, a veces te da respuestas ligeramente diferentes.

> **¿Por qué tiene azar?** Porque si siempre eligiera la palabra más probable, sus respuestas serían aburridas y repetitivas. El azar controlado (llamado "temperatura" en los LLM) le da variedad y naturalidad, como un humano que no dice siempre exactamente lo mismo.

> **Matiz importante:** no todos los modelos usan sampling. Algunos, en modo determinista puro (temperatura = 0), siempre eligen la opción más probable. Es como una calculadora: misma entrada, mismo resultado. Pero la mayoría de los asistentes conversacionales sí usan algo de azar para sonar más naturales.

### Ejemplo: el filtro de spam

¿Cómo sabe tu correo que un mail es spam? No "lee" el mail como un humano evaluando su significado. Cuenta cosas y asigna números:

- ¿Aparece la palabra "GRATIS" en mayúsculas? **(+30 puntos)**
- ¿El remitente no está en tu agenda? **(+20 puntos)**
- ¿Hay 5 links extraños? **(+50 puntos)**

Con esos números calcula una probabilidad: *"Este mail sumó 100 puntos, lo que significa un 92% de probabilidad de ser spam"*. Si pasa el umbral de seguridad (ej. 80%), lo manda a la carpeta de spam.

> **No hay magia. Hay números.** Esa es la frase que vamos a repetir todo el taller.

---

## 4. Línea de tiempo de la IA

La IA no nació con ChatGPT. Lleva **más de 80 años** de historia. Pero no fue un camino lineal: hubo avances brillantes seguidos de décadas de estancamiento. Recorrémosla.

### 1943 — McCulloch & Pitts: la primera neurona artificial

Dos investigadores (Warren McCulloch y Walter Pitts) publicaron un paper donde describían una neurona del cerebro con matemáticas. Era una idea revolucionaria: *"¿Y si modelamos una neurona como una función lógica que recibe señales y da 0 o 1?"*.

**En qué consistía el estudio:** tomaron lo que se sabía de biología sobre cómo las neuronas del cerebro reciben señales de otras neuronas, y lo tradujeron a una fórmula matemática. Si la suma de señales superaba un umbral, la neurona "se activaba" (salía 1). Si no, se quedaba dormida (salía 0). Era un modelo simple, pero demostraba que algo parecido a una neurona biológica podía representarse con matemáticas.

> **Por qué no se profundizó más:** era una idea teórica, sin forma de entrenarla con datos reales. Faltaban computadoras potentes y métodos para ajustar esos pesos automáticamente. Se quedó como una idea en papel hasta que Rosenblatt le dio vida práctica 14 años después.

> **Por qué importa:** es la semilla de todo. De esta idea nace el perceptrón.

### 1950 — Alan Turing y el Test de Turing

Turing, considerado el padre de la computación, hace la pregunta más famosa de la historia de la IA: *¿Pueden pensar las máquinas?*. Pero en lugar de quedarse filosofando, propone un test práctico: si una máquina conversa por texto y un humano no logra distinguirla de otro humano, se dice que "pasa" el test.

**En qué consistía el test:** un evaluador conversa por texto con una máquina y con un humano, sin saber cuál es cuál. Si después de un rato el evaluador no puede adivinar cuál es la máquina, esta "pasa" el test. No se mide si la máquina "piensa", sino si puede **simular** una conversación humana de forma convincente.

> **Por qué no se profundizó como investigación formal:** el test de Turing era una propuesta filosófica, no un algoritmo. No decía *cómo* construir esa máquina, solo *cómo* medirla. Además, las computadoras de la época eran tan lentas que intentar algo así era impráctico. La idea quedó como un desafío teórico durante décadas.

> **Ojo:** el test no dice que la máquina piense. Dice que **te engaña**. Esto es clave para entender el antropomorfismo (Clase 2).

### 1956 — Dartmouth: nace el término "Inteligencia Artificial"

En una reunión de verano en Dartmouth College (EE.UU.), John McCarthy y otros investigadores acuñaron el término **"Artificial Intelligence"**. La IA se volvía un campo de estudio formal.

**En qué consistía la conferencia:** era un grupo pequeño de matemáticos y científicos que creían que "cada aspecto del aprendizaje o cualquier otra característica de la inteligencia puede describirse con tanta precisión que se puede construir una máquina para simularlo". Era una apuesta enorme: creían que en 10 años tendrían máquinas que pensaran.

> **Por qué la promesa falló:** subestimaron enormemente la complejidad del problema. Pensaron que programar "inteligencia" era cuestión de lógica y reglas. Lo que no sabían era que el cerebro humano procesa información de formas que la lógica sola no puede capturar. Faltaban décadas para tener datos y cómputo suficientes.

### 1957 — Frank Rosenblatt y el Perceptrón

Rosenblatt inventó el **perceptrón**: la primera neurona artificial que podía **aprender de sus errores**. A diferencia de McCulloch & Pitts, Rosenblatt agregó algo crucial: un mecanismo para **ajustar automáticamente los pesos** cada vez que se equivocaba.

**En qué consistía:** el perceptrón era un programa que recibía datos (por ejemplo, imágenes de letras), hacía una predicción ("esta es una A"), comparaba con la respuesta correcta ("no, es una B"), y si se equivocaba, ajustaba sus pesos internos un poquito. Repetido miles de veces, el perceptrón "aprendía" a clasificar correctamente.

> **Por qué no se profundizó (y por qué vino el primer invierno):** en 1969, Marvin Minsky y Seymour Papert publicaron un libro demostrando que el perceptrón simple **no podía aprender XOR** (una operación lógica básica). Esto sonó como una sentencia de muerte para las redes neuronales. El gobierno y las universidades dejaron de financiar investigación en esa línea. **El problema era real, pero la solución existía:** apilar múltiples capas de perceptrones (redes multicapa). Pero esa solución tardó 20 años en ser redescubierta y aceptada.

> **Por qué importa:** en el notebook vas a programar esta misma idea. Es la abuela de ChatGPT.

### 1970s — El primer invierno de la IA

La IA prometió demasiado y entregó poco. El dinero se cortó masivamente.

**¿Por qué ocurrió?** Los investigadores habían prometido máquinas inteligentes en 10 años (la "promesa de Dartmouth"). Pero las computadoras de la época eran increíblemente limitadas:

- **Cómputo:** una computadora de los 70 era millones de veces más lenta que un celular actual.
- **Datos:** no existía internet. Los datasets eran manuales, pequeños y caros.
- **Algoritmos:** solo sabían resolver problemas con reglas lógicas escritas por humanos, lo cual no escalaba.

Los gobiernos vieron que la IA no cumplía lo prometido y cortaron el financiamiento. Este período se conoce como el **"primer invierno de la IA"**.

> **Lección histórica:** la idea era correcta, pero la infraestructura no existía. La IA necesita **datos + cómputo + algoritmos buenos**. Si falta uno de los tres, no avanza.

### 1980s — El segundo auge y segundo invierno

Volvieron los sueños con los **sistemas expertos** (programas que usaban reglas escritas por humanos para imitar decisiones de expertos). Funcionaban bien en dominios muy específicos (ej: diagnóstico médico con reglas fijas), pero eran frágiles: si el caso no estaba en las reglas, fallaban estrepitosamente.

> **¿Por qué fracasaron?** Porque dependían de que humanos escribieran todas las reglas manualmente. No aprendían de datos. Era como intentar construir un GPS escritos a mano todas las rutas posibles del mundo: no escala. Cuando llegaron las primeras computadoras personales baratas, el dinero volvió a fluir hacia la IA, pero el segundo invierno llegó cuando los sistemas expertos demostraron sus limitaciones.

### 1997 — Deep Blue vence a Kasparov

Una máquina de IBM le ganó al campeón mundial de ajedrez, Garry Kasparov. Fue un hito histórico: por primera vez, una máquina derrotaba a un humano en un juego considerado "de inteligencia".

**En qué consistía:** Deep Blue evaluaba **200 millones de posiciones por segundo** usando pura fuerza bruta. No "jugaba" ajedrez como un humano (con intuición o estrategia emocional). Simplemente calculaba más posiciones que cualquier humano podría procesar en mil vidas.

> **¿Por qué no cambió todo inmediatamente?** Porque era un sistema ultraespecializado: solo sabía jugar ajedrez. No podía hacer otra cosa. Era como tener un robot que gana en ajedrez pero no puede hacer un café. El mundo esperaba que esto fuera el inicio de algo más grande, pero faltaban 15 años para que los algoritmos y el cómputo estuvieran listos.

### 2012 — AlexNet: el renacer del deep learning

Una red neuronal llamada **AlexNet** aplastó a todos en una competencia de reconocimiento de imágenes (ImageNet) usando **GPUs** (tarjetas gráficas) para entrenar. Ahí empezó el boom moderno.

**¿Qué cambió?** Tres cosas se alinearon por primera vez:

1. **Datos masivos:** internet generaba millones de imágenes etiquetadas.
2. **Cómputo potente:** las GPUs, diseñadas para videojuegos, resultaron perfectas para las operaciones matemáticas de las redes neuronales.
3. **Algoritmos mejores:** se redescubrieron técnicas como el **backpropagation** (el método para ajustar pesos en redes multicapa, la solución al problema del perceptrón de Minsky).

> **Lección:** la idea de las redes neuronales existía desde los 40. Pero sin datos ni cómputo, era una bicicleta sin ruedas. En 2012, por fin tenía las tres cosas que necesitaba.

### 2017 — Transformers: "Attention is all you need"

Un paper de Google propuso una arquitectura llamada **Transformer** que procesaba texto de forma masiva y paralela. Todos los modelos modernos (GPT, Claude, Gemini, Llama) son Transformers.

**En qué consistía:** el Transformer introdujo un mecanismo llamado **"atención" (attention)** que le permitía a la red neuronal "mirar" todas las palabras de una frase a la vez y decidir cuáles eran más importantes entre sí. Los modelos anteriores procesaban palabra por palabra en orden, lo cual era lento y perdía contexto. El Transformer procesa todo en paralelo, como quien lee una frase completa de un vistazo.

> **¿Por qué fue tan revolucionario?** Porque permitió entrenar modelos **masivamente grandes** con enormes cantidades de texto de internet. De este paper nacieron GPT (OpenAI), BERT (Google), y todos los LLMs que usamos hoy.

### 2022 — ChatGPT

OpenAI lanzó ChatGPT. La IA pasó del laboratorio al celular de millones de personas. Por primera vez, la gente común podía conversar con un modelo de lenguaje y ver resultados impresionantes.

> **¿Por qué fue tan impactante?** No era el modelo más potente (GPT-4 ya existía internamente). Lo revolucionario fue la **interfaz**: una caja de texto simple que cualquiera podía usar. La tecnología existía, pero nadie la había puesto al alcance de todos.

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

No toda la IA es igual. Hay varias formas de clasificarla. Vamos a ver las más importantes.

### Por alcance: ¿qué tan "inteligente" es?

| Tipo | Significado | Ejemplo |
|------|-------------|---------|
| **ANI** (Estrecha) | Hace una sola tarea muy bien. | Spam, FaceID, ChatGPT, GPS. |
| **AGI** (General) | Hace cualquier tarea cognitiva como un humano. | **No existe todavía.** |
| **ASI** (Superinteligente) | Supera al humano en absolutamente todo. | **Ciencia ficción.** |

> **Importante:** todo lo que usamos hoy es **ANI**. Cuando alguien diga "la IA va a hacer X como un humano", preguntá: ¿ANI o AGI? Casi siempre la respuesta es "eso requeriría AGI, que no existe".

**Analogía para entender ANI vs AGI:**

- **ANI** es como un cuchillo de cocina: corta muy bien, pero solo eso. No puede atornillar ni pintar.
- **AGI** sería como un ser humano que puede cocinar, atornillar, pintar, conducir y escribir poesía, todo con la misma cabeza.
- **ASI** sería como un superhéroe que hace todo eso mejor que cualquier humano en la historia.

Hoy tenemos cuchillos de cocina increíblemente afilados (ANI), pero todavía no tenemos la cabeza versátil (AGI).

### Por forma de aprender: las ramas del Machine Learning

El **Machine Learning (ML)** es la forma más común de IA. Es cuando el programa aprende de los datos en lugar de seguir reglas escritas por humanos. Dentro del ML, hay varias "escuelas":

#### 1. Aprendizaje Supervisado

**Cómo funciona:** le das al programa **miles de ejemplos con la respuesta correcta**. Él aprende el patrón y luego puede predecir respuestas para datos nuevos.

**Analogía:** es como estudiar con un libro de ejercicios que tiene las respuestas al final. Hacés ejercicio, mirás si acertaste, y corrregís. Después podés hacer ejercicios nuevos sin mirar las respuestas.

**Ejemplos reales:**
- **Filtro de spam:** le mostrás miles de mails etiquetados como "spam" o "no spam". El programa aprende los patrones y clasifica mails nuevos.
- **Reconocimiento de caras:** le mostrás miles de fotos etiquetadas "es Juan", "es María". Aprende a reconocer caras nuevas.
- **Predicción de precios:** le das datos históricos de casas (metros cuadrados, ubicación, precio). Predice el precio de una casa nueva.

**Cuándo usarlo:** cuando tenés datos etiquetados y querés que el modelo **prediga** algo (clasificar, estimar, detectar).

#### 2. Aprendizaje No Supervisado

**Cómo funciona:** le das al programa **datos sin etiquetas**. El programa debe encontrar patrones o agrupaciones por sí mismo, sin que nadie le diga cuál es la respuesta correcta.

**Analogía:** es como entrar a un supermercado gigante sin lista de compras. Mirás los productos y empezás a agruparlos: "estos son frutas", "estos son lácteos", "estos son de limpieza". Nadie te dijo cómo agruparlos; vos lo dedujiste por similitudes.

**Ejemplos reales:**
- **Segmentación de clientes:** una tienda online agrupa compradores por comportamiento (los que compran barato, los que compran ropa de marca, los que solo compran en rebajas).
- **Detección de anomalías:** un banco detecta transacciones raras que no se parecen a ninguna agrupación conocida (posible fraude).
- **Recomendaciones:** Netflix agrupa películas por géneros o patrones similares que nadie definió manualmente.

**Cuándo usarlo:** cuando tenés datos sin etiquetar y querés **descubrir estructura oculta** (grupos, patrones, anomalías).

#### 3. Aprendizaje por Refuerzo

**Cómo funciona:** el programa aprende **por prueba y error**, como un niño que aprende a caminar. Intenta algo, recibe una **recompensa** (si lo hizo bien) o un **castigo** (si lo hizo mal), y ajusta su estrategia.

**Analogía:** es como entrenar a un perro. Si hace lo que querés, le das un premio. Si no, no le das nada. Con el tiempo, el perro aprende qué le da premio y qué no.

**Ejemplos reales:**
- **AlphaGo:** la IA de Google que venció al campeón mundial de Go (juego más complejo que el ajedrez). Jugó millones de partidas contra sí misma, ganando y perdiendo, hasta desarrollar estrategias que ningún humano había visto.
- **Robots que caminan:** un robot intenta caminar, se cae (castigo), ajusta sus movimientos, vuelve a intentar. Después de miles de intentos, camina.
- **Videojuegos:** un bot de Mario Bros que aprende a saltar obstáculos probando y equivocándose.

**Cuándo usarlo:** cuando el problema requiere una **secuencia de decisiones** donde cada acción afecta la siguiente (juegos, robótica, navegación autónoma, optimización de procesos).

#### 4. Deep Learning (Aprendizaje Profundo)

**Qué es:** no es una "cuarta forma" de aprender, sino una **técnica dentro del ML** que usa redes neuronales con **muchas capas** (por eso "profundo").

**Analogía:** imaginá una fábrica con muchos departamentos. La materia prima entra en el primer departamento, cada uno hace una transformación, y al final sale el producto terminado. Cada departamento es una "capa" de la red neuronal.

**Cuándo se usa:** cuando los datos son muy complejos:
- **Imágenes** (reconocer objetos, caras, tumores en radiografías).
- **Audio** (reconocimiento de voz, música).
- **Texto** (ChatGPT, traducción automática).
- **Video** (análisis de secuencias de imágenes).

**¿Por qué es tan popular?** Porque con suficientes datos y cómputo, las redes profundas superan a cualquier otro método en tareas complejas. AlexNet (2012) demostró esto con imágenes; los Transformers (2017) lo demostraron con texto.

### Resumen visual de los tipos

```
INTELIGENCIA ARTIFICIAL (IA)
├── Por alcance
│   ├── ANI (Estrecha) — lo que usamos hoy
│   ├── AGI (General) — no existe
│   └── ASI (Super) — ciencia ficción
│
└── Por forma de aprender (Machine Learning)
    ├── Supervisado — aprende con ejemplos etiquetados
    ├── No supervisado — encuentra patrones solo
    ├── Por refuerzo — aprende por prueba y error
    └── Deep Learning — usa redes neuronales profundas
        (técnica que puede combinarse con los anteriores)
```

> **Dato clave:** ChatGPT combina varias de estas ideas. Es **deep learning** (redes neuronales profundas) entrenado con **aprendizaje supervisado** (textos con ejemplos de conversaciones buenas) y **por refuerzo** (ajustado según las preferencias humanas). No es "una sola cosa", sino una combinación de técnicas.

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

### El Perceptrón (1957): la neurona que aprende

El perceptrón es **una neurona que aprende a ajustar sus propios pesos**. Pero, ¿cómo aprende exactamente? Vamos paso a paso con un ejemplo real.

#### Ejemplo: decidir si salís con paraguas

Imaginá que querés crear una neurona que decida si llevar paraguas o no. Los inputs son:

- **x1:** ¿Está nublado? (1 = sí, 0 = no)
- **x2:** ¿Anoche llovió? (1 = sí, 0 = no)

La neurona tiene pesos iniciales **aleatorios** (por ejemplo, w1 = 0.3, w2 = 0.5) y un sesgo (bias) de 0.1.

#### Paso 1: La primera predicción (adivinanza)

La neurona recibe: nublado = 1, llovió = 1.

Calcula: `(1 × 0.3) + (1 × 0.5) + 0.1 = 0.9`

El resultado es 0.9. Como es mayor a 0.5, la neurona dice: **"¡Llevá paraguas!" (1)**.

#### Paso 2: Comparar con la verdad

La respuesta **real** era: NO llovería (0). La neurona se equivocó.

#### Paso 3: Ajustar los pesos

Aquí es donde ocurre la magia (que no es magia). La neurona hace una cuenta simple:

- Se equivocó → los pesos que la llevaron a esa respuesta deben **bajar un poquito**.
- El ajuste es proporcional al error: si se equivocó mucho, ajusta más; si se equivocó poco, ajusta menos.

Después del ajuste, los pesos quedan en, por ejemplo: w1 = 0.2, w2 = 0.4.

#### Paso 4: Repetir miles de veces

Con cada ejemplo nuevo, la neurona repite el ciclo:

```
predecir → comparar con la verdad → ajustar pesos → repetir
```

Después de 1000 ejemplos, los pesos se estabilizan en valores que hacen que la neurona acierte la mayoría de las veces.

> **Analogía del dardo:** es como aprender a tirar dardos. Tirás (predecís), ves dónde cayó (comparás), corregís la postura (ajustás), tirás de nuevo. Con práctica, cada vez acertás más.

### El perceptrón como una receta con pasos

Pensalo como una receta de cocina:

1. **Juntá los ingredientes** (inputs): los datos que le llegan a la neurona.
2. **Pésalos** (pesos): cuánto importa cada ingrediente. Si el ingrediente principal es la harina, su peso es alto. La sal, su peso es bajo.
3. **Sumá todo** (producto ponderado + sesgo): mezclá todo en una碗.
4. **¿Pasa el umbral?** (función de activación): si la mezcla tiene buen sabor (supera el umbral), el plato está listo (salida 1). Si no, hay que seguir cocinando (salida 0).

### ¿Qué puede y qué no puede el perceptrón?

- ✅ Aprende el **AND** (se enciende solo si AMBOS inputs son 1).
- ✅ Aprende el **OR** (se enciende si CUALQUIERA es 1).
- ❌ Nunca podrá aprender el **XOR** (encenderse si SOLO UNO es 1).

¿Por qué el XOR es imposible? Porque el perceptrón solo puede trazar **líneas rectas** para separar los datos. El XOR requiere una frontera curva o una combinación de líneas.

> **Visualizalo así:** imaginá una mesa con botellas de colores. El perceptrón puede trazar una línea recta para separar las rojas de las azules. Pero si las rojas están en las esquinas opuestas y las azules en las otras dos esquinas (como el XOR), ninguna línea recta las separa. Necesitarías **dos líneas** (es decir, **dos neuronas** conectadas).

> **La solución existed pero tardó 20 años:** apilar múltiples capas de perceptrones (redes multicapa). Esto se redescubrió en los 80 con el algoritmo de **backpropagation** (retropropagación). Es la base de todas las redes neuronales modernas.

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
