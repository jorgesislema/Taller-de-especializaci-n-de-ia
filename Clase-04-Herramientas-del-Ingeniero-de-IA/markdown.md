# Markdown — Guia de sintaxis

> Markdown es un lenguaje para formatear texto con simbolos simples.
> Lo usamos en todos los archivos `.md` del taller y es el mejor formato para escribir prompts.

---

## Por que Markdown importa

Dos razones:

1. **GitHub renderiza Markdown.** El `README.md` de tu repo se ve lindo automaticamente. Es tu carta de presentacion.
2. **Las IAs responden mejor a prompts estructurados en Markdown.** Cuando usas `##`, `-`, `|`, la IA reconoce la jerarquia de tu pedido y responde con mas precision.

**Analogia:** Darle instrucciones a la IA en Markdown es como entregarle un formulario ordenado en vez de una servilleta arrugada con garabatos.

---

## Sintaxis completa

### Encabezados

```markdown
# Titulo nivel 1 (el mas grande)
## Titulo nivel 2
### Titulo nivel 3
#### Titulo nivel 4
##### Titulo nivel 5
###### Titulo nivel 6 (el mas chico)
```

> En GitHub, el `# Titulo nivel 1` es el titulo del README. Los `##` son las secciones principales.

### Enfasis

```markdown
**Texto en negrita**
*Texto en cursiva*
***Negrita y cursiva***
~~Texto tachado~~
```

### Listas

**Lista con puntitos (unordered):**
```markdown
- Item 1
- Item 2
  - Sub-item (con 2 espacios al inicio)
  - Otro sub-item
- Item 3
```

**Lista numerada (ordered):**
```markdown
1. Primer paso
2. Segundo paso
3. Tercer paso
```

### Links

```markdown
[Texto que se ve](https://url-real.com)

Ejemplo:
[Mi GitHub](https://github.com/mi-usuario)
```

### Imagenes

```markdown
![Texto alternativo](ruta/a/la/imagen.png)

Ejemplo:
![Foto de perfil](./foto.jpg)
```

### Codigo

**En linea (inline):**
```markdown
Usa el comando `git status` para ver los cambios.
```

**Bloque de codigo:**
````markdown
```python
def saludar(nombre):
    print(f"Hola, {nombre}!")
```
````

Podes cambiar `python` por `bash`, `javascript`, `html`, `json`, etc.

### Tablas

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |
```

### Citas (blockquote)

```markdown
> Esto es una cita o bloque destacado.
> Puede tener varias lineas.
```

### Linea horizontal

```markdown
---
```

### Checkboxes (listas de tareas)

```markdown
- [x] Tarea completada
- [ ] Tarea pendiente
- [ ] Otra tarea pendiente
```

---

## Como previsualizar Markdown en VSCode

1. Abri cualquier archivo `.md`
2. `Ctrl+Shift+V` → se abre la vista previa al lado
3. `Ctrl+K V` → se abre la vista previa en otra pestaña (recomendado: escribis de un lado, ves el resultado del otro)

---

## Ejemplo: un README tipico

```markdown
# Mi Proyecto

**Descripcion corta de que hace este proyecto.**

---

## Instalacion

1. Clona el repo: `git clone https://github.com/usuario/proyecto.git`
2. Entra a la carpeta: `cd proyecto`
3. Instala dependencias: `pip install -r requirements.txt`

---

## Uso

```python
from proyecto import funcion

resultado = funcion(dato)
print(resultado)
```

---

## Tecnologias usadas

- Python 3.11
- Markdown
- Git

---

## Autor

- **Nombre:** [Tu Nombre](https://github.com/tu-usuario)
- **Email:** tu@email.com
```

---

## Por que Markdown en prompts

Cuando escribis un prompt asi:

```
Hola necesito que me ayudes con un portfolio. Soy estudiante de
IA, tengo 25 años, hice un curso de Python, me gusta la
tecnologia. Quiero algo profesional. Ponele colores lindos y que
tenga secciones. Gracias.
```

La IA responde bien. Pero cuando lo escribis asi:

```markdown
## Rol
Eres un diseñador de portfolios con 10 años de experiencia.

## Contexto
Soy estudiante del taller de IA, principiante en programacion.
Estoy armando mi portfolio en GitHub.

## Tarea
Genera un README.md para mi portfolio personal.

## Restricciones
- Formato: Markdown listo para GitHub
- Tono: profesional pero amigable
- Secciones: Sobre mi, Habilidades, Proyectos, Contacto
- Usa emojis con moderacion (1 por seccion)
- Maximo 300 palabras
```

La IA responde **mucho mejor**. Misma informacion, distinta estructura.

> **Eso es Smarkdown.** Structured Markdown. La tecnica de escribir prompts usando sintaxis Markdown para darle jerarquia clara a tus instrucciones.

---

## Chuleta rapida

| Elemento | Sintaxis |
|----------|----------|
| Titulo 1 | `# Texto` |
| Titulo 2 | `## Texto` |
| Titulo 3 | `### Texto` |
| Negrita | `**Texto**` |
| Cursiva | `*Texto*` |
| Tachado | `~~Texto~~` |
| Lista | `- Item` |
| Lista numerada | `1. Item` |
| Link | `[texto](url)` |
| Imagen | `![alt](url)` |
| Codigo en linea | `` `codigo` `` |
| Bloque de codigo | ```` ```lenguaje ``` ```` |
| Tabla | `\| A \| B \|` seguido de `\|---\|---\|` |
| Cita | `> Texto` |
| Linea horizontal | `---` |
| Checkbox | `- [ ] Tarea` |
| Escape de caracter | `\*no cursiva\*` |
