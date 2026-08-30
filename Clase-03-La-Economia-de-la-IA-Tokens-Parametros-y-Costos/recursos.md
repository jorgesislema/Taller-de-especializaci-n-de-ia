# Recursos — Clase 3

> Material complementario para profundizar. Todo opciónal. Elegi lo que te llame la atención.

---

## Herramientas (gratis, online)

- **OpenAI Tokenizer:** `platform.openai.com/tokenizer` — La herramienta oficial para contar tokens. Pegas texto, te dice cuantos tokens son y cómo se parte. Ideal para calibrar tu regla de oro mental.
- **Anthropic Console:** `console.anthropic.com` — Similar al tokenizer de OpenAI pero para modelos Claude. Util para comparar como tokenizan distinto.
- **Tiktoken (libreria Python):** `github.com/openai/tiktoken` — La libreria de OpenAI para contar tokens desde código. Si ya sabés Python basico, la instalas con `pip install tiktoken`.
- **Ollama:** `ollama.com` — Herramienta gratuita para correr modelos de IA en tu computadora. Un solo comando: `ollama run llama3`.

---

## Paginas de precios oficiales (para mantenerse actualizado)

Los precios de esta clase son de referencia. Para ver los precios de hoy (cambian con frecuencia):

- **OpenAI Pricing:** `openai.com/pricing`
- **Anthropic Pricing:** `anthropic.com/pricing`
- **DeepSeek API Pricing:** `platform.deepseek.com/api-docs/pricing`
- **Google AI (Gemini) Pricing:** `ai.google.dev/pricing`
- **Groq (inferencia rápida para open-source):** `groq.com` — Ofrecen acceso a Llama, Mistral y otros via API, muy rápido.
- **Together AI:** `together.ai/pricing` — Otro proveedor de APIs para modelos open-source (Llama, Mistral, Qwen).

---

## Videos

- **3Blue1Brown — "But what is a GPT?"** — Explica visualmente como funcióna un transformer y el concepto de tokens. En inglés, subtítulos disponibles. YouTube.
- **Dot CSV — "Tokens y contexto en ChatGPT"** — Explicacion en español de como funciónan los tokens, el contexto y por qué importa. YouTube.
- **Fireship — "DeepSeek explained"** — Video corto y dinamico sobre el "shock asiatico" de DeepSeek y como lograron calidad GPT-4 a 1/10 del precio. YouTube.

---

## Articulos y lecturas

- **"What are tokens and how to count them" (OpenAI Docs):** `platform.openai.com/docs/guides/tokens` — La documentación oficial. Corta y clara. Explica el tokenizador y da ejemplos.
- **"Language Models are Few-Shot Learners" (Brown et al., 2020):** Paper original de GPT-3. La seccion 2.2 explica tokenización con BPE (Byte Pair Encoding). Avanzado, pero interesante para los curiosos.
- **"DeepSeek-V3 Technical Report" (2024):** El paper tecnico de DeepSeek explicando su arquitectura Mixture of Experts y como logran eficiencia extrema. Para mentes técnicas.
- **"The AI Pricing War"** — Busca en Google News: "AI API pricing comparison 2025". Vas a encontrar articulos actualizados que comparan precios entre proveedores. Los precios cambian cada pocos meses.

---

## Sobre el shock asiatico: DeepSeek y Qwen

- **DeepSeek Overview:** `deepseek.com` — La empresa china que sacudio el mercado con modelos de calidad GPT-4 a precios 10x menores.
- **Qwen (Alibaba):** `tongyi.aliyun.com` — La familia de modelos de Alibaba, competencia directa de DeepSeek en precio/calidad.
- **Analisis:** Busca en YouTube "DeepSeek vs GPT-4o comparison" y mira comparativas reales. Fijate no solo en calidad sino en latencia y rate limits.

### Preguntas para pensar

1. ¿Por qué una empresa china puede ofrecer el mismo servicio que OpenAI a 1/10 del precio?
2. ¿Que implicaciones geopolíticas tiene que los modelos más baratos vengan de China?
3. ¿Donde estan alojados los servidores de DeepSeek? ¿Que implicaciones de privacidad tiene enviar datos a servidores en China?

---

## Sobre Ollama y modelos locales

- **Ollama GitHub:** `github.com/ollama/ollama` — El repositorio oficial. La documentación esta en el README.
- **Ollama Library:** `ollama.com/library` — Lista de todos los modelos disponibles para descargar. Desde Llama 3 hasta Gemma, Phi, Mistral, DeepSeek.
- **LM Studio:** `lmstudio.ai` — Alternativa a Ollama con interfaz grafica. Si preferis no usar la terminal.

---

## Glosario referenciado

Si alguna palabra te trabo, anda al [`glosario.md`](glosario.md) de esta clase. Terminos clave: token, parametro, API, VRAM, rate limit, latencia, ventana de contexto.

---

## Para los que quieren mas (opciónal, avanzado)

- **"Mixture of Experts Explained" (Hugging Face blog):** Explica la arquitectura que usan DeepSeek y Mixtral para ser eficientes (activan solo una fraccion de los parametros por consulta).
- **"Quantization for LLMs" (varios autores):** Busca en Google "LLM quantization explained". Explica como se comprimen modelos para qué quepan en hardware modesto. Clave para entender IA local.
- **Curso: "LangChain for LLM Application Development" (DeepLearning.AI):** Si ya querés empezar a construir aplicaciónes con APIs de IA, este curso corto de Andrew Ng te ensenia a conectar tu código con OpenAI.

---
### https://drive.google.com/drive/u/2/folders/1ORi48lTXyRGp8lBcvZSqarpk59JvIzaI
> Encontraste un recurso bueno que no está acá? Avisale al instructor para sumarlo.
