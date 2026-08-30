# VSCode — Guia de uso

> Ya instalaste VSCode en la Clase 1. Esta guia es para que aprendas a **usarlo de verdad**, no solo a abrirlo.
> Si necesitas reinstalarlo, el instalador esta en el pendrive: carpeta `VSCode/`.

---

## Atajos de teclado esenciales

Aprende estos 10 atajos. Te van a ahorrar horas.

| Atajo (Windows/Linux) | Atajo (Mac) | Que hace |
|-----------------------|-------------|---------|
| `Ctrl+Shift+P` | `Cmd+Shift+P` | Paleta de comandos — el "buscador universal" de VSCode |
| `Ctrl+P` | `Cmd+P` | Abrir archivo rapidamente (escribi el nombre) |
| `Ctrl+` ` | `Cmd+` ` | Abrir/Cerrar terminal integrada |
| `Ctrl+B` | `Cmd+B` | Mostrar/Ocultar barra lateral |
| `Ctrl+S` | `Cmd+S` | Guardar archivo |
| `Ctrl+Z` | `Cmd+Z` | Deshacer |
| `Ctrl+Shift+V` | `Cmd+Shift+V` | Previsualizar Markdown (abri el archivo `.md` primero) |
| `Ctrl+K V` | `Cmd+K V` | Previsualizar Markdown en otra pestaña (mejor) |
| `Ctrl+Shift+E` | `Cmd+Shift+E` | Ir al explorador de archivos |
| `Ctrl+F` | `Cmd+F` | Buscar texto en el archivo actual |
| `Ctrl+Shift+F` | `Cmd+Shift+F` | Buscar texto en todos los archivos del proyecto |

> **Tip:** La paleta de comandos (`Ctrl+Shift+P`) es lo mas importante. No necesitas recordar menus ni botones. Abris la paleta, escribis lo que queres hacer, y VSCode te muestra las opciones. Proba escribir "format", "theme", "terminal", "markdown".

---

## Las 3 zonas de VSCode

```
┌─────────────┬──────────────────────────┬─────────────┐
│             │                          │             │
│  BARRA      │                          │  MINIMAPA   │
│  LATERAL    │     AREA DE EDICION      │  (vista     │
│  (Ctrl+B)   │     (donde escribis)     │   reducida  │
│             │                          │   del       │
│  • Explorer │                          │   archivo)  │
│  • Search   │                          │             │
│  • Git      │                          │             │
│  • Extens.  │                          │             │
│             │                          │             │
│             ├──────────────────────────┤             │
│             │     TERMINAL (Ctrl+`)     │             │
└─────────────┴──────────────────────────┴─────────────┘
```

---

## La terminal integrada

La terminal integrada es lo mejor de VSCode. En vez de andar saltando entre ventanas, escribis comandos ahi mismo donde esta tu codigo.

Para abrirla: `Ctrl + ` ` (la tecla a la izquierda del numero 1).

**Ventajas de la terminal integrada:**
- Ya se abre en la carpeta de tu proyecto (no tenes que navegar con `cd`)
- Podes tener varias terminales abiertas (clic en el +)
- Podes elegir PowerShell, CMD, Git Bash, o la que prefieras
- Esta al lado del codigo: ves el error y lo corregis sin cambiar de ventana

---

## Extensiones utiles

Ya deberias tener instaladas (de la Clase 1):
- **Python** (Microsoft) — para que entienda Python
- **Jupyter** (Microsoft) — para ejecutar notebooks

Para esta clase, instala (opcional):

| Extension | Para que sirve |
|-----------|---------------|
| **Markdown All in One** | Atajos para escribir Markdown mas rapido |
| **Markdown Preview GitHub Styling** | La preview de Markdown se ve como en GitHub |
| **Spanish Language Pack** | VSCode en español |

Para instalar: barra lateral izquierda → icono de cuadrados → buscar → Install.

---

## Split editor (editar dos archivos a la vez)

Util cuando queres ver el README.md de ejemplo y escribir el tuyo al mismo tiempo.

1. Abri el primer archivo
2. `Ctrl+\` (o clic derecho en la pestaña → Split Right)
3. Abri el segundo archivo en el panel nuevo

---

## Buscar y reemplazar

### En un archivo
1. `Ctrl+F` para buscar
2. `Ctrl+H` para buscar y reemplazar

### En todo el proyecto
1. `Ctrl+Shift+F` para buscar
2. Clic en la flechita para expandir el panel de reemplazo

---

## Configuracion rapida

Abrí la paleta de comandos (`Ctrl+Shift+P`) y escribi:

- `theme` → para cambiar el tema de colores
- `font size` → para agrandar o achicar la letra
- `auto save` → para que guarde solo (recomendado: `afterDelay`)
- `word wrap` → para que el texto no se salga de la pantalla

---

## Problemas comunes

### "No me aparece la terminal"
`Ctrl+` ` o menu `View → Terminal`

### "No veo los archivos del proyecto"
`Ctrl+Shift+E` (explorador) o `File → Open Folder` y elegi la carpeta de tu proyecto.

### "La preview de Markdown no se ve"
Asegurate de tener el archivo `.md` abierto y activo al hacer `Ctrl+Shift+V`.

### "El notebook no corre"
Asegurate de tener activado el entorno virtual (venv). Si no, repasa el [setup de la Clase 1](../Clase-01-Evolucion-de-la-IA-y-Setup-de-Entorno/setup-entorno.md).
