# AGENTS.md — Instrucciones para el agente

> Este archivo es la **memoria del proyecto**. Lo lee el agente de IA en cada sesión para retomar el contexto sin volver a preguntar todo. **No borrar ni mover de la raíz.**

## Naturaleza del proyecto

Taller teórico-práctico de Inteligencia Artificial, **24 clases en 6 módulos**, una carpeta por clase. El repo lo usa el instructor (jorgesislema) para preparar y dictar las clases.

## Audiencia

**Principiantes.** Sin conocimientos previos de IA ni de programación. Tono: simple, analogías cotidianas, cero jerga innecesaria. Cuando un término técnico sea inevitable, explicarlo con una analogía y agregarlo al `glosario.md` de esa clase.

## Duración de cada clase

**70 minutos** de contenido + **20 minutos** de consulta y conversación. Calibrar el volumen de contenido a 70 min reales.

## Formato

- **Teoría:** Markdown (`.md`) — legible directamente en GitHub o en la vista web (GitHub Pages + Jekyll).
- **Práctica:** Notebooks de Jupyter (`.ipynb`) cuando hay código; guías `.md` cuando es un setup o demostración.
- **Idioma:** español.

## Práctica / código

- **Python puro** (`random`, `math`) en los primeros módulos. Sin sklearn/tensorflow/pytorch hasta que el alumno entienda qué hay dentro de la "caja negra".
- matplotlib **opcional**, siempre con fallback ASCII para que el notebook corra sin instalar nada.
- Cada notebook debe poder ejecutarse con un `python` estándar y un entorno virtual mínimo.

## Principios rectores (no negociables)

1. **La IA es una herramienta determinística basada en estadística, no magia.** Desmitificar en cada clase.
2. **Desantropomorfizar la IA.** La IA no "piensa", no "siente", no "quiere". Calcula.
3. **El Rol del Ingeniero de IA es el hilo conductor de todo el taller.** Cada clase lleva una sub-sección "El Ing. de IA en esta clase" que conecta el tema con el rol profesional. Enseñar que se pueden construir programas sin saber programar, sabiendo a lo que se enfrentan; al final, con práctica, se aprende a programar.
4. **Mitos y leyendas:** aprovechar historias virales reales para enseñar (¿qué se dijo vs. qué pasó?) y enganchar la lectura.

## Convenciones de estructura

- Carpeta por clase: `Clase-NN-Titulo-con-guiones/` (NN = 01, 02, ...).
- Dentro de cada clase:
  - `README.md` — resumen, objetivos, agenda 70+20 min.
  - `apuntes.md` — teoría completa.
  - `glosario.md` — términos de esa clase en lenguaje sencillo, con analogía.
  - práctica: `*.ipynb` (código) o `*.md` (guía/demo).
  - `recursos.md` — videos, papers, lecturas, documentales.
- Archivos raíz de contexto (no borrar):
  - `AGENTS.md` — este archivo.
  - `ARQUITECTURA.md` — estructura del repo, plantilla por clase, cómo activar Pages.
  - `TEMARIO.md` — las 24 clases oficiales con estado.
  - `DECISIONES.md` — bitácora de decisiones de diseño.
  - `_config.yml` — configuración de Jekyll para GitHub Pages.

## Temario oficial (24 clases, 6 módulos)

Ver [`TEMARIO.md`](TEMARIO.md). Resumen:

- **Módulo 1 (1–4):** Infraestructura y Limitaciones — evolución, antropomorfismo/seguridad, vibe coding, tokens.
- **Módulo 2 (5–8):** Fundamentos de Datos y Prompting — bases de datos, ML, EDA, prompting base.
- **Módulo 3 (9–12):** Control de Outputs y Vectores — prompts avanzados, JSON, local vs cloud, embeddings.
- **Módulo 4 (13–16):** RAG y Seguridad — RAG foundations, RAG avanzado, arneses, de workflows a agentes.
- **Módulo 5 (17–20):** Sistemas Autónomos y Debugging — debugging, ReAct, memoria, HITL.
- **Módulo 6 (21–24):** Multiagentes y Despliegue — LangGraph, MCP, testing, cierre.

## Estado actual

- **Clase 1:** completa (en desarrollo de contenido).
- **Clase 2:** próxima — ciberseguridad, cómo escoger IA, costos.
- **Clase 5:** completa — Arquitectura, Estructura y Mentalidad de Ingeniería para IA.
- **Clase 8:** completa — Gobernanza de Datos y Protección de Datos Personales en Ecuador.
- **Resto:** planificada en `TEMARIO.md`.

## Contexto administrativo

- Se pidieron 24 clases; se aprobaron 8 inicialmente. Capacidad del curso: 30. Inscritos: 10. Si hay acuerdo con los alumnos, se puede pedir más horas.
- Repo: `jorgesislema/Taller-de-especializaci-n-de-ia` (público).
- Licencia: MIT.

## Cómo trabajar en cada nueva clase

1. Leer este archivo, `TEMARIO.md` y `ARQUITECTURA.md`.
2. Crear la carpeta `Clase-NN-Titulo/` con los archivos de la plantilla (ver `ARQUITECTURA.md`).
3. Escribir teoría en `apuntes.md` siguiendo los principios rectores.
4. Incluir sub-sección "El Ing. de IA en esta clase".
5. Incluir `glosario.md` con los términos nuevos.
6. Crear la práctica (notebook o guía) en Python puro si es código.
7. Al terminar, validar: `python -m json.tool` sobre `.ipynb`; ejecutar el código fuera del notebook; revisar render Markdown.
8. No commitear: el instructor revisa y commitea él mismo.
