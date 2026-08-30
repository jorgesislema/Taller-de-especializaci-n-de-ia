# Recopilatorio de Recursos para tu Portfolio — Clase 4

> **Enfoque Ingeniero de IA:** Tu portfolio de GitHub es tu primera API publica. Tratalo como tal: versiona, automatiza, testea. Cada badge, cada grafico, cada accion automatica es un endpoint de tu presencia digital. No decores: diseña.

---

## Indice

1. [GitHub Actions: tu portfolio vivo](#1-github-actions-tu-portfolio-vivo)
2. [Badges e insignias profesionales](#2-badges-e-insignias-profesionales)
3. [Estadisticas y graficos dinamicos](#3-estadisticas-y-graficos-dinamicos)
4. [Emojis tematicos por perfil](#4-emojis-tematicos-por-perfil)
5. [Iconos, divisores y decoracion ASCII](#5-iconos-divisores-y-decoracion-ascii)
6. [Generadores de imagenes y headers](#6-generadores-de-imagenes-y-headers)
7. [Plantilla completa: README de ingeniero IA](#7-plantilla-completa-readme-de-ingeniero-ia)
8. [Como probar tu README antes de publicar](#8-como-probar-tu-readme-antes-de-publicar)

---

## 1. GitHub Actions: tu portfolio vivo

> **Mentalidad de ingeniero:** Un README estatico es codigo muerto. Un README con GitHub Actions es un sistema que se actualiza solo. Vos escribis las reglas, GitHub las ejecuta.

### 1.1 Snake Animation — La viborita que come contribuciones

Crea el archivo `.github/workflows/snake.yml` en tu repo:

```yaml
name: Generate Snake Animation

on:
  schedule:
    - cron: "0 0 * * *"   # Corre todos los dias a medianoche UTC
  workflow_dispatch:        # Te permite ejecutarlo manualmente

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Generate snake 🐍
        uses: Platane/snk@v3
        with:
          github_user_name: TU-USUARIO        # ← Cambia esto
          outputs: |
            dist/github-snake.svg
            dist/github-snake-dark.svg?palette=github-dark
            dist/ocean.gif?color_snake=orange&color_dots=#bfd6f6,#8dbdff,#64a1f4,#4b91f1,#3c7dd9&color_background=#aaaaaa

      - name: Push to output branch
        uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Para mostrarlo en tu README**, agrega esto donde quieras que aparezca la viborita:

```markdown
![Snake animation](https://github.com/TU-USUARIO/TU-REPO/blob/output/github-snake.svg)
```

**Variantes de paleta y colores:**

| Comando | Resultado |
|---------|-----------|
| `dist/snake.svg` | Paleta github clasica (clara) |
| `dist/snake-dark.svg?palette=github-dark` | Paleta oscura |
| `dist/snake-light.svg?palette=github-light` | Paleta clara suave |
| `dist/ocean.gif?color_snake=orange&color_dots=#bfd6f6,#8dbdff,#64a1f4,#4b91f1,#3c7dd9` | GIF animado con snake naranja y dots azules |

> **Tip del ingeniero:** El snake es tu "health check". Si no se actualiza hace 3 dias, tu action fallo. Revisa la pestaña Actions de tu repo. Debuggear pipelines es mas importante que saber CSS.

### 1.2 Actualizador automatico de blog / actividad reciente

```yaml
name: Latest Blog Posts

on:
  schedule:
    - cron: "0 6 * * *"
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: gautamkrishnar/blog-post-workflow@v1
        with:
          feed_list: "https://TU-BLOG.com/feed.xml"
          max_post_count: 5
          template: "- 📝 [$title]($url) — *$date*"
```

### 1.3 WakaTime — Cuanto programas en cada lenguaje

> Requisito: cuenta gratuita en [wakatime.com](https://wakatime.com) + plugin en VSCode.

```yaml
name: WakaTime Stats

on:
  schedule:
    - cron: "0 0 * * 0"   # Cada domingo
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: anmol098/waka-readme-stats@v4
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          SHOW_LINES_OF_CODE: "True"
          SHOW_PROFILE_VIEWS: "False"
          SHOW_TOTAL_CODE_TIME: "True"
```

---

## 2. Badges e insignias profesionales

> **Mentalidad de ingeniero:** Los badges son tu `requirements.txt` visual. Cualquier reclutador tecnico ve un badge de "Python 3.12" y sabe que no mentis. Usa badges que linkeen a documentacion real.

### 2.1 Generador rapido: Shields.io con parametros por URL

Formato base:

```
https://img.shields.io/badge/<ETIQUETA>-<MENSAJE>-<COLOR>?style=<ESTILO>&logo=<LOGO>
```

**Ejemplos copy-paste:**

```markdown
<!-- Lenguajes -->
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown)

<!-- Herramientas -->
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
![ChatGPT](https://img.shields.io/badge/IA-ChatGPT-75ac9d?style=flat&logo=openai&logoColor=white)
![Claude](https://img.shields.io/badge/IA-Claude-d97757?style=flat&logo=anthropic&logoColor=white)

<!-- Estado del repo -->
![Status](https://img.shields.io/badge/status-aprendiendo-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Made with](https://img.shields.io/badge/hecho_con-IA_+_❤️-ff69b4)

<!-- Redes sociales (badges que linkean) -->
[![GitHub](https://img.shields.io/badge/GitHub-TU_USUARIO-181717?style=flat&logo=github)](https://github.com/TU-USUARIO)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-TU_NOMBRE-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/TU-PERFIL)
[![Email](https://img.shields.io/badge/Email-contacto-FF6B6B?style=flat&logo=gmail)](mailto:tu@email.com)
```

### 2.2 Tabla de colores de badges por tecnologia

| Tecnologia | Color | Codigo Hex | Badge |
|------------|-------|------------|-------|
| Python | Azul | `#3776AB` | `![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)` |
| Arduino | Verde | `#00979D` | `![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat&logo=arduino&logoColor=white)` |
| Discord | Morado | `#5865F2` | `![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white)` |
| Twitch | Purpura | `#9146FF` | `![Twitch](https://img.shields.io/badge/Twitch-9146FF?style=flat&logo=twitch&logoColor=white)` |
| YouTube | Rojo | `#FF0000` | `![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white)` |
| TikTok | Negro | `#000000` | `![TikTok](https://img.shields.io/badge/TikTok-000000?style=flat&logo=tiktok)`) |
| Spotify | Verde | `#1DB954` | `![Spotify](https://img.shields.io/badge/Spotify-1DB954?style=flat&logo=spotify&logoColor=white)` |
| FL Studio | Naranja | `#F97C00` | `![FL Studio](https://img.shields.io/badge/FL_Studio-F97C00?style=flat&logo=flstudio&logoColor=white)` |
| Photoshop | Azul | `#31A8FF` | `![Photoshop](https://img.shields.io/badge/Photoshop-31A8FF?style=flat&logo=adobephotoshop&logoColor=white)` |

### 2.3 Estilos de badges

```
?style=flat          → Minimalista (recomendado para GitHub)
?style=flat-square   → Cuadrado compacto
?style=plastic       → 3D clasico
?style=for-the-badge → Grande, bold, llamativo
?style=social        → Solo texto, estilo boton social
```

---

## 3. Estadisticas y graficos dinamicos

> **Mentalidad de ingeniero:** Las estadisticas son tu "dashboard de monitoreo". No las pongas por decoracion: cada grafico debe responder una pregunta real sobre tu perfil.

### 3.1 GitHub Stats Cards (anuraghazra)

```markdown
<!-- Estadisticas principales -->
![Tus stats](https://github-readme-stats.vercel.app/api?username=TU-USUARIO&show_icons=true&theme=default&hide_border=true&count_private=true)

<!-- Lenguajes mas usados -->
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=TU-USUARIO&layout=compact&theme=default&hide_border=true)

<!-- Racha de contribuciones -->
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=TU-USUARIO&theme=default&hide_border=true)
```

**Temas disponibles (cambia `theme=`):**

| Tema | Apariencia |
|------|------------|
| `default` | Gris claro, minimalista |
| `dark` | Fondo oscuro |
| `radical` | Purpura/rosa neon |
| `merko` | Verde oscuro |
| `gruvbox` | Retro, calido |
| `tokyonight` | Azul nocturno |
| `onedark` | Atom One Dark |
| `cobalt` | Azul electrico |
| `synthwave` | Rosa/azul ochentoso |
| `highcontrast` | Accesibilidad total |
| `transparent` | Fondo transparente (combina con `bg_color=00000000`) |

### 3.2 GitHub Profile Trophy (logros)

```markdown
![Trophies](https://github-profile-trophy.vercel.app/?username=TU-USUARIO&theme=flat&no-frame=true&column=4&margin-w=15)
```

### 3.3 Profile Views Counter

```markdown
![Profile views](https://komarev.com/ghpvc/?username=TU-USUARIO&color=blue&style=flat)
```

### 3.4 Spotify Now Playing (para musicos/beatmakers)

```markdown
![Spotify](https://spotify-github-profile.kittinanx.com/api/view?uid=TU-SPOTIFY-ID&cover_image=true&theme=default)
```

---

## 4. Emojis tematicos por perfil

> **Regla de ingeniero IA:** 1 emoji por seccion. Maximo 2. Si tu README parece un arbol de navidad, perdiste.

### Paleta Gamer / Streamer

```
🎮 👾 🕹 ⚡ 🎯 🤖 🎬 🧠 📦 📡 🏆 🎒 💻 🔥
```

### Paleta Creador de Contenido

```
🎬 📱 🎨 🚀 🧪 📲 ✂️ 🎞 📊 🔥 💡 🎭 🎤
```

### Paleta Artista Digital

```
🎨 🖌 🖼 🧰 📬 ✨ 🎭 🌈 🖍 💫 🎯 🌸 🖊
```

### Paleta Musico / Beatmaker

```
🎧 🎹 🔊 🎼 🎛 📡 🎵 🎸 🥁 🎚 🎤 🎶 💿
```

### Paleta Tech / Maker

```
🔧 ⚡ 🛠 🤖 📚 📡 🔬 🧪 💻 🖥 ⚙️ 🔌 🧲
```

### Paleta Profesional / Reinvencion

```
💼 📖 🎯 🔄 🚀 🧰 📞 📈 💡 🏗 🔑 🌱 🎓
```

### Emojis para secciones comunes

| Seccion | Emojis sugeridos |
|---------|-----------------|
| Sobre mi | 👋 🧑‍💻 🚀 ✨ |
| Skills | 🛠 💻 🧰 ⚡ |
| Proyectos | 🚀 📂 🏗 🔨 |
| Contacto | 📫 📬 🤝 💬 |
| Estadisticas | 📊 📈 🔥 ⭐ |
| Setup/Herramientas | 💻 ⌨️ 🖥 🎒 |
| Aprendizaje | 📚 🌱 🎓 🧠 |

---

## 5. Iconos, divisores y decoracion ASCII

### 5.1 Divisores horizontales elegantes

```markdown
<!-- Linea simple -->
---

<!-- Linea con emoji -->
--- ⚡ ---

<!-- Linea doble (requiere HTML) -->
<br>

<!-- Divisor grueso -->
***
```

### 5.2 Headers con ASCII art

```markdown
<!-- Banner de presentacion -->
```
╔══════════════════════════════════════╗
║   🧑‍💻  Hola, soy [Tu Nombre]          ║
║   Ingeniero de IA en formacion       ║
║   Construyo con prompts, no con codigo ║
╚══════════════════════════════════════╝
```

```markdown
<!-- Separador minimalista -->
┌──────────────────────────────────────┐
│           MIS PROYECTOS              │
└──────────────────────────────────────┘
```

### 5.3 Barras de progreso estilo "skill bars"

```markdown
<!-- Barras de progreso con bloques Unicode -->
Python:     ██████████ 100%
Git:        ████████░░  80%
Markdown:   █████████░  90%
IA Prompt:  ███████░░░  70%
VSCode:     █████████░  85%

<!-- Con emojis como indicadores -->
🐍 Python     ⭐⭐⭐⭐  (Avanzado)
📦 Git        ⭐⭐⭐    (Intermedio)
📝 Markdown   ⭐⭐⭐⭐⭐ (Experto)
🤖 ChatGPT    ⭐⭐⭐⭐  (Avanzado)
```

### 5.4 "Quote blocks" estilizados

```markdown
> 💡 *"No necesitas saber programar para construir. Necesitas saber describir."*

> 🔥 *"Cada prompt es un commit. Cada iteracion es un deploy."*

> 🧠 *"La IA no reemplaza tu criterio: lo amplifica. Pero el dueño de las decisiones seguis siendo vos."*
```

---

## 6. Generadores de imagenes y headers

### 6.1 Header / Banner generators

| Herramienta | URL | Que genera |
|-------------|-----|------------|
| **Capsule Render** | `https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&text=TU-NOMBRE&fontSize=40` | Banner con olas animadas |
| **Readme Typing SVG** | `https://readme-typing-svg.herokuapp.com/?lines=Primera+linea;Segunda+linea;Tercera+linea&font=Fira+Code&center=true` | Texto que se "escribe solo" |
| **GPRM** | [gprm.itsvg.in](https://gprm.itsvg.in/) | Generador visual de README completo |
| **ProfileMe.dev** | [profileme.dev](https://www.profileme.dev/) | Constructor drag-and-drop |

### 6.2 Ejemplo: Capsule Render con codigo

```markdown
<!-- Banner de olas -->
![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,24,30&height=200&section=header&text=TU%20NOMBRE&fontSize=50&fontAlignY=35&desc=Ingeniero%20de%20IA%20en%20formacion&descSize=20&descAlignY=55)
```

### 6.3 Ejemplo: Readme Typing SVG

```markdown
![Typing](https://readme-typing-svg.herokuapp.com/?lines=Construyo+con+prompts;Aprendo+con+IA;Itero+sin+miedo&font=Fira+Code&center=true&width=380&height=45&duration=4000&pause=1000)
```

### 6.4 GitHub Profile README Generator (arrastrar y soltar)

1. Anda a [gprm.itsvg.in](https://gprm.itsvg.in/)
2. Llena tu info en el formulario visual
3. El sitio genera el Markdown completo
4. Copia y pega en tu `README.md`
5. **Despues editalo a mano** — el template generado es un punto de partida, no el destino.

---

## 7. Plantilla completa: README de ingeniero IA

> Copia, pega, reemplaza `TU-*` con tus datos. Ejecuta `git push`. Listo.

```markdown
<!-- Header animado -->
![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,24,30&height=180&section=header&text=TU%20NOMBRE&fontSize=45&fontAlignY=35&desc=Ingeniero%20de%20IA%20en%20formación&descSize=18&descAlignY=55)

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown)
![ChatGPT](https://img.shields.io/badge/IA-ChatGPT-75ac9d?style=flat&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/status-aprendiendo-brightgreen)
![Profile views](https://komarev.com/ghpvc/?username=TU-USUARIO&color=blue&style=flat)

---

## 👋 Sobre mi

Soy **TU-NOMBRE**, estudiante del Taller de Especialización en IA.  
Construyo software sin saber programar: mi IDE es el prompt, mi debugger es la iteración.

> 🧠 *"La IA no es magia: es estadística. Pero bien dirigida, construye castillos."*

---

## 🛠 Stack actual

| Categoria | Herramientas |
|-----------|-------------|
| **IA / LLMs** | ChatGPT, Claude, Gemini, Opencode |
| **Prompt Engineering** | Smarkdown, Zero-shot, Few-shot, Chain of Thought |
| **Lenguajes** | Python (aprendiendo con IA), Markdown |
| **Herramientas** | VSCode, Git, GitHub, Terminal |
| **Conceptos** | Tokens, temperature, chunking, token budget |

---

## 🚀 Proyectos

### 🤖 Agente de [TEMA]
[Descripción breve de 2 líneas.]
**Tools:** ChatGPT GPTs · Markdown · mi conocimiento de [area]

### 📊 [NOMBRE PROYECTO 2]
[Descripción breve de 2 líneas.]
**Tools:** Python · Opencode · VSCode

### 🎨 Mi Portfolio GitHub
Este mismo repo. Mi carta de presentación como ingeniero de IA en formación.
**Tools:** Markdown · GitHub Actions · IA · Git

---

## 📊 Estadisticas

![Stats](https://github-readme-stats.vercel.app/api?username=TU-USUARIO&show_icons=true&theme=default&hide_border=true&count_private=true)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=TU-USUARIO&layout=compact&theme=default&hide_border=true)

<!-- Snake animation (requiere GitHub Action configurado) -->
![Snake](https://github.com/TU-USUARIO/TU-REPO/blob/output/github-snake.svg)

---

## 📚 Lo que estoy aprendiendo

| Modulo | Tema | Estado |
|--------|------|--------|
| 1 | Infraestructura y Limitaciones de la IA | ✅ |
| 2 | Fundamentos de Datos y Prompting | 🔧 En progreso |
| 3 | Control de Outputs y Vectores | ⏳ Proximo |
| 4 | RAG y Seguridad | ⏳ Proximo |
| 5 | Sistemas Autonomos y Debugging | ⏳ Proximo |
| 6 | Multiagentes y Despliegue | ⏳ Proximo |

---

## 📫 Contacto

[![GitHub](https://img.shields.io/badge/GitHub-TU_USUARIO-181717?style=flat&logo=github)](https://github.com/TU-USUARIO)
[![Email](https://img.shields.io/badge/Email-contacto-FF6B6B?style=flat&logo=gmail)](mailto:tu@email.com)

---

> 💡 *"Prompt engineering no es 'escribir lindo'. Es diseñar APIs con lenguaje natural."*

<!-- Footer -->
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,24,30&height=100&section=footer)
```

---

## 8. Como probar tu README antes de publicar

> **Mentalidad de ingeniero:** No deployes a ciegas. Testea en local.

### Opcion A: VSCode (recomendado)

```bash
# Abri tu README.md en VSCode
code README.md

# Previsualiza (Ctrl+Shift+V o Cmd+Shift+V)
# La preview de VSCode es ~90% fiel a GitHub
```

### Opcion B: GitHub en el navegador

1. Anda a tu repo en `github.com/TU-USUARIO/TU-REPO`
2. Edita el README.md directamente en GitHub (lapicito ✏️)
3. Pestaña **Preview** para ver como queda
4. No hagas commit hasta que estes conforme

### Opcion C: Script de validacion (ingeniero level)

```bash
# Verifica que los links de badges funcionen
# (requiere curl)
curl -s -o /dev/null -w "%{http_code}" "https://img.shields.io/badge/Python-3776AB?style=flat&logo=python"
# Si devuelve 200, el badge existe

# Verifica que tu README no tenga links rotos
# (instala: npm install -g markdown-link-check)
markdown-link-check README.md
```

---

## 🚀 Checkout final: ¿esta listo tu portfolio?

Antes de compartir la URL, repasa:

- [ ] Tiene titulo con tu nombre real (o apodo profesional)
- [ ] Tiene al menos 1 badge funcional
- [ ] Las secciones estan separadas con `---` o headers `##`
- [ ] Los links a redes sociales funcionan (abrilo en una pestaña incognito)
- [ ] Las imagenes cargan (las de shields.io, stats, snake)
- [ ] No hay datos personales sensibles (direccion, telefono real, DNI)
- [ ] El tono es profesional pero humano
- [ ] La frase final refleja tu filosofia como ingeniero de IA
- [ ] Hiciste `git push` y la URL publica funciona

---

> **Ultimo consejo del ingeniero:** Tu portfolio no se termina nunca. Es un sistema vivo. Cada clase del taller, cada proyecto nuevo, cada herramienta que aprendas... actualiza el README. Un repo abandonado habla mas fuerte que un repo vacio.
