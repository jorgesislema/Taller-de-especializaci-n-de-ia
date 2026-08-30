# ARQUITECTURA.md — Estructura del repositorio

> Cómo está organizado el repo, qué archivo va dónde y cómo replicar la plantilla para cada clase nueva.

## Estructura de carpetas

```
Taller-de-especializaci-n-de-ia/
├── README.md                # Portada del taller
├── AGENTS.md                # Instrucciones para el agente de IA (memoria)
├── ARQUITECTURA.md          # Este archivo
├── TEMARIO.md               # 24 clases oficiales con estado
├── DECISIONES.md            # Bitácora de decisiones de diseño
├── _config.yml              # Configuración de Jekyll (GitHub Pages)
├── .gitignore
├── LICENSE                  # MIT
│
├── Clase-01-.../
│   ├── README.md            # Resumen + agenda 70+20 min
│   ├── apuntes.md           # Teoría completa
│   ├── glosario.md          # Términos de la clase en sencillo
│   ├── practica.ipynb       # Notebook (código) o guia.md (setup/demo)
│   └── recursos.md          # Material complementario
│
├── Clase-02-.../
│   └── ...
└── ...
```

## Plantilla por clase

Cada carpeta `Clase-NN-Titulo-con-guiones/` contiene:

| Archivo | Propósito | Obligatorio |
|---------|-----------|-------------|
| `README.md` | Resumen, objetivos, agenda minuto a minuto (70+20) | Sí |
| `apuntes.md` | Teoría completa, con sub-sección "El Ing. de IA en esta clase" | Sí |
| `glosario.md` | Términos nuevos de la clase, con analogía | Sí |
| `*.ipynb` o `*.md` | Práctica: notebook de Jupyter o guía práctica | Sí |
| `recursos.md` | Videos, papers, documentales, lecturas | Sí |

## Convenciones de naming

- Carpetas: `Clase-NN-Titulo-con-guiones/` — NN siempre dos dígitos (`01`, `02`, ..., `24`).
- Título de la carpeta = título de la clase en el temario, con espacios reemplazados por guiones.
- Archivos en minúsculas, sin espacios ni acentos.

## Convenciones de código

- Python 3, sin librerías de ML en los primeros módulos.
- Imports permitidos desde el inicio: `random`, `math`, estándar de Python.
- matplotlib opcional, con fallback ASCII siempre.
- Cada notebook debe correr con `python` estándar y un venv mínimo.

## Convenciones de Markdown

- Idioma: español.
- Encabezados con `#` jerárquicos.
- Analogías cotidianas para cada concepto técnico.
- Diagramas en ASCII cuando ayuden (no requiere imágenes externas).

---

## Activar vista web (GitHub Pages)

El repo se puede ver como un **sitio web navegable** (en lugar de solo archivos en GitHub). Es gratis y se activa en 2 clics:

1. En GitHub, ir al repo → pestaña **Settings**.
2. Menú lateral izquierdo → **Pages**.
3. En **Source**, elegir **Deploy from a branch**.
4. Branch: `main` → carpeta: `/ (root)`.
5. Clic en **Save**.
6. Esperar 1–2 minutos. Aparecerá una URL tipo:
   `https://jorgesislema.github.io/Taller-de-especializaci-n-de-ia/`

El archivo `_config.yml` (en la raíz) ya viene preconfigurado con un tema y el título del taller, por lo que al activar Pages se verá ordenado sin trabajo extra.

> Nota: los notebooks `.ipynb` no se renderizan automáticamente en Jekyll, pero los `.md` sí. El `README.md` de cada carpeta funciona como página de inicio de esa "sección".
