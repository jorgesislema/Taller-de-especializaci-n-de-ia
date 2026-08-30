# Apuntes — Clase 4

> Teoria central de la clase. Las guias practicas de cada herramienta estan en archivos separados para que no te pierdas:
> - [Ingenieria de Prompt (resumen)](ingenieria-de-prompt.md)
> - [Guia Avanzada (API, testing, token budget)](avanzado.md)
> - [VSCode — Guia de uso](vscode.md)
> - [Git y GitHub — Guia practica](github.md)
> - [Markdown — Guia de sintaxis](markdown.md)
> - [Opencode — Instalacion y manual](opencode.md)

---

## 1. Introduccion al Vibe Coding

### Que es el Vibe Coding

**Vibe Coding** es programar describiendo lo que queres en lenguaje natural, y dejar que la IA genere el codigo por vos.

No necesitas saber Python, JavaScript, ni HTML. Necesitas saber **describir exactamente que queres que el programa haga**. La IA traduce tu español a codigo.

**Analogia:** Es como pedirle a un arquitecto que diseñe tu casa. Vos no sabes de estructuras ni de calculo de cargas. Pero sabes que queres 3 dormitorios, cocina integrada, y un patio con parrilla. El arquitecto traduce tus deseos a planos tecnicos. Con Vibe Coding, vos sos el cliente y la IA es el arquitecto del codigo.

### Por que funciona

Recorda lo que vimos en la Clase 1: la IA no piensa, **calcula**. Los modelos de lenguaje fueron entrenados con miles de millones de lineas de codigo real. Vieron tantos ejemplos de "alguien pidio X y el codigo resultante fue Y" que pueden predecir el codigo que corresponde a tu descripcion.

No es magia. Es patrones estadisticos a escala masiva.

### La formula del Vibe Coding

```
BUEN PROMPT + ITERACION = PROGRAMA FUNCIONAL
```

1. **Buen prompt:** Describis que queres con precision. Usas los 5 elementos de ingenieria de prompt (ver el [resumen](ingenieria-de-prompt.md)).
2. **Iteracion:** El primer resultado casi nunca es perfecto. Le pedis ajustes: "cambia el color a azul", "agrega un boton de descarga", "ahora hace que funcione sin internet".

El 90% del Vibe Coding es **saber iterar**. No es "un prompt magico y listo". Es una conversacion donde vos dirigis y la IA ejecuta.

### Que podes construir sin saber programar

| Tipo de proyecto | Ejemplo | Que necesitas saber describir |
|-----------------|---------|-------------------------------|
| Pagina web personal | Tu portfolio en GitHub | Como queres que se vea, que secciones tiene |
| Script de automatizacion | Renombrar 100 archivos de una carpeta | Que archivos, que patron de nombre |
| Analisis de datos simple | "De este Excel, decime cual fue el mes con mas ventas" | Donde esta el archivo, que columna mirar |
| Chatbot basico | Un bot que responda preguntas frecuentes de tu negocio | Las preguntas y respuestas tipicas |
| Juego simple | Piedra, papel o tijera contra la computadora | Las reglas del juego |

### Lo que el Vibe Coding NO puede hacer (por ahora)

- Programas gigantes de una sola vez (como "haceme un Facebook"). Hay que dividir en partes chicas.
- Codigo 100% libre de errores siempre. Vas a tener que probar y pedir correcciones.
- Reemplazar el criterio humano. Vos decidis si lo que genero esta bien o no (recorda: HITL, Human-in-the-Loop).

---

## 2. Creando agentes en diferentes chats

Cada plataforma de IA tiene su forma de crear agentes. Aca van las recetas para las tres mas populares.

> **Recorda:** Un agente es una IA con rol fijo, instrucciones permanentes y posiblemente herramientas extra. En el [resumen de ingenieria de prompt](ingenieria-de-prompt.md#5-agentes-la-ia-con-personalidad-definida) esta explicado en detalle.

### Agentes en ChatGPT (GPTs)

**Requisito:** Cuenta ChatGPT Plus o Team (USD 20/mes). La version gratuita no permite crear GPTs.

**Pasos:**

1. Anda a [chat.openai.com](https://chat.openai.com)
2. Barra lateral izquierda → **"Explorar GPTs"**
3. Arriba a la derecha → **"Crear"**
4. Te aparece un split-screen:
   - **Izquierda (Create):** Describis tu agente en lenguaje natural
   - **Derecha (Configure):** Ajustes finos manuales
5. En la pestaña **Configure**:
   - **Nombre:** El nombre de tu agente
   - **Descripcion:** Que hace, para que sirve
   - **Instrucciones:** El system prompt (el "manual de procedimientos")
   - **Conversation starters:** Frases de ejemplo para empezar
   - **Knowledge:** Archivos que queres que el agente "sepa" (PDFs, Excels)
   - **Capabilities:** Web Browsing, DALL-E, Code Interpreter
6. Clic en **"Create"**
7. Visibilidad: **Only me** / **Anyone with the link** / **Public**

**Ejemplo de instrucciones para "Asistente de Portfolio":**

```markdown
Eres un diseñador de portfolios profesional con 10 años de experiencia.
Ayudas a estudiantes a crear su pagina de presentacion en GitHub.

Reglas:
- Siempre en español, tono profesional pero amigable.
- Pregunta primero: nombre, profesion, 3 proyectos destacados.
- Genera README.md con: Titulo, Sobre mi, Habilidades, Proyectos, Contacto.
- Disenio limpio, profesional, apto para GitHub.
- No uses datos personales reales a menos que el usuario los de.
- Al final, ofrece generar version en ingles.
```

### Agentes en Claude (Projects)

**Requisito:** Cuenta Claude Pro (USD 20/mes).

**Pasos:**

1. Anda a [claude.ai](https://claude.ai)
2. Barra lateral → **"Projects"** → **"Create Project"**
3. Configura:
   - **Project name:** Nombre del agente
   - **Custom instructions:** El system prompt
   - **Project knowledge:** Archivos base
4. Cada conversacion dentro del proyecto hereda las instrucciones

**Diferencia clave:** Claude no publica agentes en una tienda. Son privados. Pero Claude tiende a seguir las instrucciones con mas precision que otros modelos.

### Agentes en Gemini (Gems)

**Requisito:** Cuenta Google One AI Premium (USD 20/mes).

**Pasos:**

1. Anda a [gemini.google.com](https://gemini.google.com)
2. Barra lateral → **"Gems"** → **"Create Gem"**
3. Configura:
   - **Name:** Nombre
   - **Instructions:** El system prompt
   - **Knowledge:** Archivos de referencia
4. **Save**

### Tabla comparativa

| Caracteristica | ChatGPT (GPTs) | Claude (Projects) | Gemini (Gems) |
|---------------|----------------|-------------------|---------------|
| Plan necesario | Plus ($20/mes) | Pro ($20/mes) | AI Premium ($20/mes) |
| Archivos de conocimiento | Si | Si | Si |
| Busqueda web | Si | Si (desde 2025) | Si |
| Imagenes | Si (DALL-E) | No | Si (Imagen) |
| Publico / compartible | Si (tienda GPT) | No (privado) | No (privado) |
| Ejecucion de codigo | Si (Code Interpreter) | No (solo analisis estatico) | Si |

> **Para el taller:** Cualquiera de los 3 funciona. Si no tenes plan de pago, podes hacer prompts normales (sin agente fijo). El resultado es similar, solo que tenes que repetir el contexto en cada conversacion nueva.

---

## 3. El Ing. de IA en esta clase

En esta clase el Ingeniero de IA hace 4 cosas que definen su rol:

### Domina las herramientas

VSCode, Git, Markdown y Opencode no son "extras". Son el banco de trabajo. Asi como un carpintero no puede trabajar sin su serrucho y su metro, el Ing. de IA no puede trabajar sin su editor y su control de versiones. Hoy sumaste 5 herramientas a tu cinturon.

### Sabe crear agentes, no solo usar chats

Cualquiera puede abrir ChatGPT y hacer una pregunta. El Ingeniero de IA **crea agentes con personalidad, reglas y herramientas definidas** para resolver problemas especificos. Un agente bien diseñado es como un empleado virtual que trabaja 24/7 siguiendo tus instrucciones exactas.

### Entiende los loops

El Ing. de IA sabe que los problemas complejos no se resuelven con un solo prompt. Se resuelven con ciclos de: pensar → actuar → observar → corregir. Entender esto es lo que separa al que "juega con IA" del que **construye con IA**.

### Produce, no solo aprende

Al final de esta clase no te vas con teoria. Te vas con un repositorio de GitHub publicado, generado con IA, versionado con Git, y escrito en Markdown. El Ing. de IA **entrega cosas**. No solo estudia.

### El hilo conductor

Recorda el principio del taller: **se puede construir sin saber programar, sabiendo a lo que te enfrentas**. Hoy diste el primer paso concreto: creaste tu primer proyecto con IA. En la Clase 8, cuando hagas Vibe Coding en serio, ya vas a tener las herramientas listas y la experiencia de haber construido algo real.
