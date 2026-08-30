# Glosario — Clase 1

> Términos de esta clase, en lenguaje sencillo, con analogía. Si una palabra te traba, vení acá.

---

## A

### Algoritmo
Una **receta** paso a paso para resolver algo. "Para hacer un huevo frito: 1) calentá la sartén, 2) poné aceite, 3) rompé el huevo". Un algoritmo es eso, pero para una computadora.

### Alucinación
Cuando una IA **inventa** algo que parece verdad pero no lo es. Como un vendedor que responde con seguridad algo que no sabe: suena convincente, pero está equivocado. Le pasa a ChatGPT cuando no tiene datos pero igual responde.

### Antropomorfismo
Significa **atribuirle características humanas a algo que no es humano**. Cuando decís "la IA se dio cuenta" o "la IA quiere ayudarte", estás antropomorfizando. La IA no se da cuenta ni quiere nada. Calcula. (Tema central de la Clase 2.)

### ANI (Inteligencia Artificial Estrecha)
IA que hace **una sola tarea** muy bien. Ej: el filtro de spam, FaceID, el ajedrez, ChatGPT. Todo lo que usamos hoy es ANI.

### AGI (Inteligencia Artificial General)
IA que podría hacer **cualquier tarea** humana. **No existe todavía.** Es un objetivo de investigación, no una realidad.

### ASI (Superinteligencia Artificial)
IA que **supera al humano** en todo. Ciencia ficción por ahora.

---

## B

### Bias / Sesgo
Una **inclinación previa**. En la neurona artificial, es un número que se suma al final y empuja la decisión hacia un lado. Como el favoritismo de un jurado: antes de escuchar a los testigos, ya tiene una inclinación.

---

## C

### Commit
Un **"punto guardado"** de tu trabajo en Git. Como guardar partida en un videojuego: si metés la pata después, podés volver a ese punto.

### Clonar (un repo)
**Bajar** una copia del repositorio de GitHub a tu computadora. Como descargar una carpeta, pero con conexión a GitHub para sincronizar cambios.

### Contexto
El **texto previo** que la IA ya procesó y que usa para calcular las probabilidades de la siguiente palabra. Sin contexto, "Necesito un..." puede ser cualquier cosa. Con contexto ("tengo frío"), la probabilidad de "café" se dispara. Como en una conversación: lo que dijiste antes cambia cómo interpretás lo que viene.

---

## D

### Data Scientist
Persona que **extrae conocimiento de los datos**. Su pregunta es "¿qué nos dicen estos datos?". Hace reportes, dashboards, análisis estadístico. No necesariamente arma productos.

### Dataset
El **conjunto de datos** que usamos para entrenar a la IA. Como el librero de ejemplos del aprendiz de panadería: cuantos más y mejores ejemplos, mejor aprende.

### Deep Learning
**Machine Learning con redes neuronales de muchas capas** ("profundas"). "Deep" = profundo. Es lo que hizo despegar a la IA en 2012 (AlexNet).

### Determinístico
Que **siempre da el mismo resultado** con el mismo input. Como una calculadora: `2 + 2` siempre da `4`. No hay sorpresas. La IA, en el fondo, es determinística.
---

## E

### Embedding
Una forma de representar cosas (palabras, imágenes) como **vectores** (listas de números) donde cosas parecidas quedan cerca. Como un mapa donde ciudades cercanas son parecidas. (Lo veremos en la Clase 12.)

### Epoch
**Una pasada completa** por todos los ejemplos de entrenamiento. Si el dataset tiene 100 ejemplos, un epoch = procesar los 100 una vez. Suele hacerse many epochs para que la neurona aprenda bien.

---

## F

### Fine-tuning
**Ajuste fino.** Después del entrenamiento principal, se le muestran al modelo ejemplos específicos para que aprenda a hacer algo mejor (ej: responder como un asistente útil). Como un pianista que ya sabe tocar y ahora perfecciona una pieza específica.

### Función de activación
La **regla** que decide si una neurona "se dispara" o no. En el perceptrón, es una función escalón: "si la suma pasa el umbral, da 1; si no, da 0". Como el botón de encendido: o está prendido o está apagado.

---

## G

### Generativa (IA)
IA que **crea cosas nuevas**: texto, imágenes, código. Pregunta: "dado esto, ¿qué sigue?". Ej: ChatGPT, Midjourney. Opuesto de discriminativa.

### Git
Un sistema para **controlar versiones** de tu código. Como un "guardar partida" profesional: guarda cada cambio, te deja volver atrás, trabajar en equipo sin pisarse.

---

## I

### Ingeniero de IA
Persona que **construye sistemas que usan IA para resolver problemas reales**. No necesariamente programa desde cero. Sabe qué herramienta usar, cómo conectarlas, cómo controlar que funcione. Es el rol que construye este taller.

---

## L

### LLM (Large Language Model)
**Modelo de Lenguaje Grande.** Un programa entrenado con miles de millones de textos que aprendió a **predecir qué palabra viene después**. No "piensa", no "entiende": **calcula probabilidades** y elige la palabra más probable. ChatGPT, Claude, Gemini y Llama son LLMs. Como el autocorrector del celular, pero gigante.

---

## M

### Machine Learning (ML)
Rama de la IA donde el programa **aprende de los datos** en lugar de seguir reglas escritas a mano. Como el aprendiz de panadero: no le damos la receta, le mostramos ejemplos y él nota patrones.

### Modelo
El **resultado** de entrenar una IA con datos. Es como el "cerebro ya entrenado" que podés usar para predecir o generar. "Modelo" = "programa que ya aprendió".

---

## N

### Neurona (artificial)
Una **unidad mínima de cómputo** que recibe números, los pesa, los suma y dispara (1 o 0). Inspirada en la neurona del cerebro, pero es una simplificación matemática. Como un pequeño interruptor que decide.

### Neurona (biológica)
La célula del cerebro que recibe señales, las suma, y si llega a un umbral, **se dispara**. La artificial imita esta idea, pero con matemática simple.

---

## P

### Perceptrón
La **primera neurona artificial que aprende** (Rosenblatt, 1957). Aprende ajustando los pesos con cada error. Es la base de todas las redes neuronales modernas. Hoy lo programamos en el notebook.

### Parámetro
Un **peso ajustable** dentro de un modelo. En el perceptrón hay 3 parámetros (2 pesos + 1 sesgo). En un LLM hay **miles de millones**. Cuantos más parámetros, más patrones complejos puede aprender el modelo.

### Peso
Un **número** que indica qué tan importante es un input para una neurona. Si el peso es alto, ese input importa mucho; si es bajo, casi no importa. Como cuánto le creés a cada testigo en un jurado.

### Probabilidad
Un **número entre 0 y 1** que indica qué tan posible es algo. 0 = imposible, 1 = seguro. Un LLM calcula la probabilidad de cada palabra posible y elige la más alta. Como un pronóstico del clima: "80% de chance de lluvia" = probabilidad 0.8.

---

## R

### Repo (repositorio)
Una **carpeta de proyecto** gestionada por Git. Donde vive tu código + su historial de cambios. En GitHub, los repos son públicos o privados y se pueden clonar a tu computadora.

### RLHF (Reinforcement Learning from Human Feedback)
**Entrenamiento con feedback humano.** Después del entrenamiento principal, humanos califican las respuestas del modelo ("esta es buena, esta es mala"). El modelo aprende a generar respuestas que los humanos prefieren. Es lo que hace que ChatGPT sea útil y no solo un predictor de palabras crudo.

---

## S

### Supervisado (aprendizaje)
Cuando le enseñamos a la IA con **ejemplos que tienen la respuesta**. "Este mail SÍ es spam, este NO". La IA aprende a predecir la respuesta para casos nuevos.

---

## T

### Token
Un **trozo mínimo de texto** al que le asignamos un número. Como las letras de un abecedario gigante: en vez de 27 letras, hay miles de "piezas" de palabras. El texto se convierte en una lista de tokens (números) que la neurona puede procesar.

### Transformer
Una **arquitectura** de red neuronal (Google, 2017) que procesa texto de forma muy eficiente. Todos los modelos modernos (GPT, Claude, Gemini, Llama) son Transformers. "GPT" = "Generative Pre-trained Transformer".

---

## V

### Entorno virtual (venv)
Una **carpeta aislada** donde instalás las librerías de Python de un proyecto, sin afectar el resto de tu sistema. Como una caja de herramientas exclusiva para ese proyecto: si la rompés, no rompés las demás.

---

## Más términos que aparecieron

- **Deep Blue** — programa de IBM que le ganó a Kasparov al ajedrez en 1997. No "jugaba", calculaba millones de posiciones.
- **AlexNet** — red neuronal que ganó una competencia de imágenes en 2012 y arrancó el deep learning moderno.
- **ChatGPT** — chatbot de OpenAI lanzado en 2022. Primer contacto masivo con IA generativa.
- **Dartmouth** — reunión de 1956 donde nació el término "Inteligencia Artificial".
- **Turing** — matemático que en 1950 planteó la pregunta "¿pueden pensar las máquinas?" y propuso el Test de Turing.
- **McCulloch & Pitts** — pioneros que en 1943 modelaron la neurona con matemática.
- **Rosenblatt** — inventor del perceptrón (1957).
- **Jekyll / GitHub Pages** — herramienta que convierte los `.md` del repo en una página web navegable.

---

> ¿Falta algún término? Avísale al instructor para agregarlo.

---

## Imágenes de referencia

Las imágenes de esta clase están en la carpeta [`imagenes clase 1/`](imagenes%20clase%201/). Se referencian dentro de los apuntes en la sección "¿Qué es un LLM y cómo funciona?".
