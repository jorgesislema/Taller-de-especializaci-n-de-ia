# Glosario — Clase 3

> Terminos de esta clase, en lenguaje sencillo, con analogía. Si una palabra te traba, veni aca.

---

## A

### API (Application Programming Interface)
Una **ventanilla de pedidos** entre programas. Como cuando vas al banco: no entras a la boveda, le pedís al cajero (la API) lo que necesitas, y el te lo trae. En IA, la API te deja usar un modelo (GPT-4o, Claude) desde tu propio programa sin usar la página web. Pagas por cada pedido, no una suscripción fija.

### API Key (Clave API)
Un **código secreto** que te identifica ante la API. Como la clave de tu home banking. Si alguien la obtiene, puede usar la IA a tu nombre y **vos pagás la cuenta**. Nunca se sube a GitHub.

---

## B

### Batch Processing (Procesamiento por lotes)
Procesar muchos pedidos **en bloque**, en lugar de uno por uno en tiempo real. Como lavar ropa: no lavas una medía a la vez, juntas todo y lo lavas junto. En IA, mandás 1000 consultas juntas de noche (más barato) en lugar de 1 cada vez que un usuario hace clic.

---

## C

### Contexto (Context)
Todo el texto que la IA ya "leyo" en la conversación actual. Es lo que ocupa la **ventana de contexto**. Como los mensajes anteriores en un chat: la IA los usa para entender de que estás hablando. Pero cada palabra de contexto que enviás **cuesta tokens**, incluso si ya la enviaste antes.

### Context Window (Ventana de Contexto)
El **tamano máximo del pizarron** donde la IA escribe y lee la conversación. Medido en tokens: 8k, 32k, 128k. Cuando el pizarron se llena, lo que se escribio primero **se borra** (la IA lo olvida). Como la memoria RAM de una computadora: finita y cara de llenar.

---

## E

### Input (Tokens de Entrada)
Los tokens que **vos le envias** a la IA. Tu pregunta, tu prompt, el contexto historico que le mandas. Es la "materia prima" que entra a la fábrica. **Es más barato que el output.**

---

## I

### Inferencia (Inference)
El momento en qué un modelo ya entrenado **genera una respuesta** a partir de tu input. Como un cocinero que ya aprendio la receta y ahora cocina pedidos. Cada vez que hablás con ChatGPT, estás haciendo inferencia. **La inferencia cuesta dinero y gasta electricidad.**

---

## L

### Latencia
El **tiempo que tarda** la IA en responder desde que enviaste el prompt. Medido en segundos. Como el tiempo que pasa entre que pedís la comida y te la traen. En chatbots en tiempo real, latencia > 3 segundos = cliente impaciente. En procesamiento nocturno, la latencia no importa.

---

## M

### Memoria de Video (VRAM / Video RAM)
La **memoria de la tarjeta grafica (GPU)**. Ahi se carga el modelo de IA para correr en local. Como el tamano de tu mesa de trabajo: si es chica, no entra el plano (modelo) y no podés trabajar. Si es grande, todo fluye. Medida en GB.

### Modelo Grande (Large Model)
Un modelo con **cientos de miles de millónes de parametros** (GPT-4o, Claude Sonnet). Excelente para tareas complejas (analisis legal, escritura creativa), pero **caro y lento**. Como un auto de carrera: potente, pero gasta mucha nafta.

### Modelo Pequenio (Small Model)
Un modelo con **pocos miles de millónes de parametros** (Haiku, GPT-4o-mini, Llama 8B). Rapido, barato, y suficiente para el 80% de las tareas (clasificar texto, responder preguntas simples). Como una moto: no lleva carga pesada, pero es agil y gasta poca nafta.

### Modalidad Chat
Usar la IA a traves de la **página web**, con suscripción fija (ej: ChatGPT Plus ~$20/mes). Comodo, pero **no sirve para construir aplicaciónes profesionales**. Es para uso personal, no para producción.

### Modalidad API
Usar la IA a traves de una **conexión programática**. Pagas por cada token consumido (pay-as-you-go). Es la **única forma profesional** de construir productos con IA. Escala, automatiza, integra.

### Modalidad Local
Correr el modelo de IA en **tu propia computadora** (con Ollama, LM Studio). Sin internet, sin APIs, privacidad total. Pero necesitas **hardware (GPU con VRAM)** y pagás con electricidad. No hay costo por token, pero si costo de equipo.

---

## N

### Notacion de modelos (8B, 70B, etc.)
La **B** significa **billion** (miles de millónes, billones en inglés). "Llama 3 8B" significa 8 mil millónes de parametros. Como decir "motor 2.0" en autos: te da una idea de la potencia, pero no es el único factor.

---

## O

### Ollama
Una **herramienta gratuita** para correr modelos de IA en tu computadora. Un solo comando: `ollama run llama3` y tenés un chat local. Como un "Docker para modelos de IA": empaqueta, descarga, ejecuta. Ideal para experimentar con IA local sin configuraciónes complicadas.

### Open-Source (Modelo de código abierto)
Un modelo cuyos **pesos (parametros) estan publicados**. Cualquiera puede descargarlo, modificarlo, correrlo en su computadora. Ej: Llama 3, Mistral, DeepSeek. Opuesto a los modelos **propietarios** (GPT-4o, Claude) cuyos pesos no son públicos.

### Output (Tokens de Salida)
Los tokens que **la IA genera** como respuesta. Es el "producto terminado" que sale de la fábrica. **Cuesta entre 3 y 5 veces más que el input**, porque generarlo requiere mas cálculos.

---

## P

### Parametro
Un **número ajustable** dentro del modelo. En el perceptrón de la Clase 1 habia 3 parametros. En GPT-4 hay ~1.8 billones. Cada parametro es como una pequenia perilla que se ajusto durante el entrenamiento para qué el modelo funcióne mejor.

### Pay-as-you-go (Pago por consumo)
Modelo de cobro donde **pagás solo por lo que usas**, sin costo fijo. Como la electricidad de tu casa: no pagás una membresía, pagás por cada kilowatt que consumiste. Las APIs de IA funciónan asi: pagás por cada token.

### Prompt
El texto que vos le escribís a la IA. Literalmente, lo que escribís en la caja de texto. El prompt es **todo input** (tokens de entrada). Incluye tu pregunta + cualquier contexto o instrucción que agregues.

### Propietario (Modelo)
Modelo cuyos **pesos NO son públicos**. Solo podés usarlo via API (pagando) o via web. No podés descargarlo ni correrlo en tu computadora. Ej: GPT-4o, Claude. Opuesto a open-source.

---

## Q

### Quantizacion
Tecnica para **reducir el tamano** de un modelo para qué quepa en menos VRAM, sacrificando un poco de precisión. Como comprimir una imagen JPEG: ocupa menos espacio, se ve casí igual. Un modelo quantizado a 4 bits ocupa ~1/4 del espacio original.

---

## R

### Rate Limit (Limite de tasa)
La **cantidad máxima de pedidos** que podés hacer a una API por minuto (RPM) o de tokens que podés enviar por minuto (TPM). Como las cabinas de peaje en una autopista: hay un número limitado. Si mandás mas trafico del que pueden procesar, la API te rechaza (error 429).

### RPM (Requests Per Minute)
Cantidad de **pedidos individuales** que podés hacer a la API por minuto. Un pedido = una pregunta + su respuesta.

### Regla de oro (de tokens)
Formula rápida para estimar tokens: **1 token ≈ 4 caracteres en inglés ≈ 0.75 de una palabra en español**. No es exacta, pero sirve para cálculos rápidos. Para precisión, usa la herramienta de tokenización del proveedor.

---

## S

### Streaming
Recibir la respuesta de la IA **token por token**, en tiempo real, en lugar de esperar la respuesta completa. Como ver un video en YouTube: se reproduce mientras se descarga. El usuario ve el texto aparecer letra por letra y percibe mas velocidad, aúnque la latencia total sea igual.

---

## T

### Token
La **unidad mínima de texto** que la IA procesa. No es una palabra ni una letra: es un trozo de texto que el tokenizador reconoce. **Es la moneda con que pagás por usar la IA.** "Gato" = 1 token, "hipopótamo" = ~3 tokens, "Artificial Intelligence" ≈ 3 tokens (en inglés).

### Tokenizador (Tokenizer)
El **programa que parte el texto en tokens**. Como un carnicero que corta la carne en trozos que ya conoce. Cada modelo tiene su propio tokenizador, y no siempre parten igual.

### TPM (Tokens Per Minute)
Cantidad de **tokens** que podés enviar a la API por minuto. Diferente de RPM: podés hacer pocos pedidos con MUCHOS tokens cada uno, y exceder el TPM aúnque no excedas el RPM.

---

## V

### Variable de Entorno
Una **configuración secreta** guardada fuera del código. Como un papelito con la clave del WiFi pegado atras del router: no esta a la vista, pero el programa sabe donde buscarlo. Se usa para guardar API Keys sin exponerlas en el código.

### VRAM (Video RAM)
Ver **Memoria de Video**.

---

> ¿Falta algun termino? Avisale al instructor para agregarlo.
