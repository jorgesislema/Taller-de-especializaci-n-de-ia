# Guía de Markdown — Qué es y cómo se usa

> Markdown es el idioma que usa este taller. Aprendelo una vez y lo usás siempre.

---

## ¿Qué es Markdown?

**Markdown** es una forma de escribir texto con formato usando solo el teclado, sin menús, sin botones, sin Mouse.

Cuando escribís `**negrita**` en un archivo `.md`, el navegador o GitHub lo muestra como **negrita**. Cuando escribís `# Título`, se muestra como un título grande.

**Analogía:** Es como escribir con señales de tráfico en el texto. El símbolo `#` significa "esto es un título". El símbolo `**` significa "ponelo en negrita". Cualquier programa que entienda Markdown convierte esas señales en formato visual automáticamente.

**Por qué lo usamos en este taller:**
- Funciona en GitHub, en VS Code, en Jupyter, en ChatGPT y en casi toda herramienta de IA
- No necesitás instalar Word ni ningún procesador de texto
- El archivo es texto plano: liviano, portable, nunca se corrompe
- La IA genera respuestas en Markdown de forma natural

---

## Títulos

Los títulos se hacen con el símbolo `#`. Cuantos más `#`, más chico el título.

**Cómo se escribe:**
```
# Taller de Especialización en IA
## Módulo 2 — Riesgos y Seguridad
### Clase 2 — El Costo Real de la IA
#### 2.1 El Enganche Psicológico
```

**Cómo se ve:**
# Taller de Especialización en IA
## Módulo 2 — Riesgos y Seguridad
### Clase 2 — El Costo Real de la IA
#### 2.1 El Enganche Psicológico

> **Regla:** Dejá siempre un espacio entre el `#` y el texto. `#Título` no funciona. `# Título` sí.

**Otro ejemplo real — estructura de un apunte de clase:**
```
# Clase 5 — Fundamentos de Machine Learning

## Objetivos
## Teoría
### Qué es un modelo
### Cómo aprende
## Práctica
## Glosario
```

---

## Texto en negrita, cursiva y tachado

| Lo que escribís | Lo que se ve | Para qué sirve |
|-----------------|-------------|----------------|
| `**texto**` | **texto** | Énfasis fuerte, palabras clave |
| `*texto*` | *texto* | Énfasis suave, términos en otro idioma |
| `~~texto~~` | ~~texto~~ | Algo que ya no aplica o está cancelado |
| `**_texto_**` | **_texto_** | Negrita + cursiva al mismo tiempo |

**Ejemplo:**
```
La IA **no siente** ni *entiende*. Solo ~~piensa~~ calcula.
```
Se ve: La IA **no siente** ni *entiende*. Solo ~~piensa~~ calcula.

---

## Listas

### Lista con viñetas (sin orden)

Usá `-` o `*` al comienzo de cada línea. Dejá una línea en blanco antes de la lista.

**Cómo se escribe:**
```
- Herramientas de IA gratuitas
- Herramientas de IA de pago
- Herramientas de IA locales
  - LM Studio
  - Ollama
  - GPT4All
```

**Cómo se ve:**
- Herramientas de IA gratuitas
- Herramientas de IA de pago
- Herramientas de IA locales
  - LM Studio
  - Ollama
  - GPT4All

**Otro ejemplo — riesgos de subir datos a un LLM:**
```
- Contraseñas y credenciales
- Bases de datos de clientes
  - Nombres y apellidos
  - Correos electrónicos
  - Números de documento
- Código fuente privado de la empresa
- Información financiera confidencial
```

- Contraseñas y credenciales
- Bases de datos de clientes
  - Nombres y apellidos
  - Correos electrónicos
  - Números de documento
- Código fuente privado de la empresa
- Información financiera confidencial

---

### Lista numerada (con orden)

Usá números seguidos de punto. No importa si los números están en orden o no, Markdown los acomoda solo.

**Cómo se escribe:**
```
1. Abrí ChatGPT en el navegador
2. Escribí tu prompt usando la plantilla Smarkdown
3. Revisá la respuesta completa antes de usarla
4. Verificá los datos importantes (fechas, números, citas)
5. Editá y personalizá el output
```

**Cómo se ve:**
1. Abrí ChatGPT en el navegador
2. Escribí tu prompt usando la plantilla Smarkdown
3. Revisá la respuesta completa antes de usarla
4. Verificá los datos importantes (fechas, números, citas)
5. Editá y personalizá el output

**Otro ejemplo — pasos para crear un AlterEgo:**
```
1. Elegí un problema real de tu trabajo o estudio
2. Escribí tu ficha de AlterEgo (sin datos reales)
3. Hacé el checklist pre-prompt
4. Construí el prompt con Smarkdown
5. Aplicá HITL al output que recibas
6. Traé tu experiencia a la próxima clase
```

1. Elegí un problema real de tu trabajo o estudio
2. Escribí tu ficha de AlterEgo (sin datos reales)
3. Hacé el checklist pre-prompt
4. Construí el prompt con Smarkdown
5. Aplicá HITL al output que recibas
6. Traé tu experiencia a la próxima clase

---

### Lista de tareas (checkboxes)

Muy útil para checklists y tareas pendientes.

**Cómo se escribe:**
```
- [x] Tarea completada
- [ ] Tarea pendiente
- [ ] Otra tarea pendiente
```

**Cómo se ve:**
- [x] Tarea completada
- [ ] Tarea pendiente
- [ ] Otra tarea pendiente

**Ejemplo real — checklist pre-prompt del taller:**
```
- [x] ¿El prompt tiene al menos Tarea + Restricciones?
- [x] ¿Usé mi AlterEgo para anonimizar datos sensibles?
- [ ] ¿Si esto se publica en un periódico, estaría bien enviarlo?
- [ ] ¿Estoy usando el plan adecuado para este tipo de dato?
```

- [x] ¿El prompt tiene al menos Tarea + Restricciones?
- [x] ¿Usé mi AlterEgo para anonimizar datos sensibles?
- [ ] ¿Si esto se publica en un periódico, estaría bien enviarlo?
- [ ] ¿Estoy usando el plan adecuado para este tipo de dato?

---

## Links (enlaces)

**Formato:** `[texto que se ve](URL)`

**Ejemplos:**
```
[Ir a Google](https://www.google.com)
[Ver apuntes de Clase 1](Clase-01-Evolucion-de-la-IA-y-Setup-de-Entorno/apuntes.md)
```

Se ve:
- [Ir a Google](https://www.google.com)
- [Ver apuntes de Clase 1](Clase-01-Evolucion-de-la-IA-y-Setup-de-Entorno/apuntes.md)

> **Para links a archivos del mismo repositorio:** usá rutas relativas (sin `http`). Así el link funciona tanto en GitHub como localmente.

---

## Imágenes

**Formato:** `![texto alternativo](ruta-o-URL-de-la-imagen)`

Es igual que un link, pero con un `!` adelante.

**Ejemplos:**
```
![Logo del taller](imagenes/logo.png)
![Diagrama de red neuronal](https://ejemplo.com/imagen.png)
```

El texto entre corchetes `[]` es el texto alternativo (lo que aparece si la imagen no carga, y lo que leen los lectores de pantalla).

---

## Código

### Código en línea

Para mencionar una palabra de código dentro de un párrafo, usá comillas invertidas `` ` ``.

**Cómo se escribe:**
```
El archivo se llama `apuntes.md` y el comando es `git commit`.
La función se llama `calcular_promedio()` y devuelve un `float`.
El error dice `TypeError: unsupported operand type`.
```

**Cómo se ve:**
El archivo se llama `apuntes.md` y el comando es `git commit`.
La función se llama `calcular_promedio()` y devuelve un `float`.
El error dice `TypeError: unsupported operand type`.

---

### Bloque de código (varias líneas)

Para bloques de código completos, usá tres comillas invertidas ` ``` ` al principio y al final. Podés indicar el lenguaje después de las primeras tres comillas para colorear la sintaxis.

**Cómo se escribe:**

````
```python
nombre = "Juan"
print(f"Hola, {nombre}!")
```
````

**Cómo se ve:**
```python
nombre = "Juan"
print(f"Hola, {nombre}!")
```

**Más ejemplos con diferentes lenguajes:**

Python:
````
```python
# Calcular el promedio de una lista
notas = [7, 8, 9, 6, 10]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.1f}")
```
````
```python
# Calcular el promedio de una lista
notas = [7, 8, 9, 6, 10]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.1f}")
```

SQL:
````
```sql
-- Buscar todos los alumnos con nota mayor a 7
SELECT nombre, nota
FROM alumnos
WHERE nota > 7
ORDER BY nota DESC;
```
````
```sql
-- Buscar todos los alumnos con nota mayor a 7
SELECT nombre, nota
FROM alumnos
WHERE nota > 7
ORDER BY nota DESC;
```

JSON (formato de datos muy común en APIs de IA):
````
```json
{
  "modelo": "gpt-4",
  "temperatura": 0.7,
  "mensaje": "Explicá qué es un LLM en términos simples"
}
```
````
```json
{
  "modelo": "gpt-4",
  "temperatura": 0.7,
  "mensaje": "Explicá qué es un LLM en términos simples"
}
```

**Lenguajes que podés indicar:** `python`, `javascript`, `sql`, `bash`, `markdown`, `json`, `html`, `css`. Si no sabés o es texto genérico, dejá las comillas solas sin nombre.

---

## Citas (blockquotes)

Usá `>` al principio de la línea para crear una cita o un bloque destacado.

**Cómo se escribe:**
```
> La IA no piensa, calcula.
> Esta es la premisa central del taller.
```

**Cómo se ve:**
> La IA no piensa, calcula.
> Esta es la premisa central del taller.

**Más usos reales de las citas:**

Para citas de autores:
```
> "Si la abeja desapareciera de la faz de la Tierra, al hombre
> solo le quedarían cuatro años de vida."
> — Frase atribuida a Einstein (pero que Einstein nunca dijo)
```
> "Si la abeja desapareciera de la faz de la Tierra, al hombre
> solo le quedarían cuatro años de vida."
> — Frase atribuida a Einstein (pero que Einstein nunca dijo)

Para advertencias:
```
> ⚠️ **Atención:** Nunca subas contraseñas, datos de clientes
> ni código fuente privado a un LLM gratuito.
```
> ⚠️ **Atención:** Nunca subas contraseñas, datos de clientes
> ni código fuente privado a un LLM gratuito.

Para destacar ideas clave al final de una sección:
```
> **Regla de oro:** Un ingeniero de IA no solo sabe usar la herramienta.
> Sabe cuándo NO usarla.
```
> **Regla de oro:** Un ingeniero de IA no solo sabe usar la herramienta.
> Sabe cuándo NO usarla.

Muy útil para citas de autores, advertencias importantes, o resaltar una idea clave.

---

## Tablas

**Formato básico:**
```
| Herramienta | Plan gratuito    | Guarda tus datos?       |
|-------------|------------------|-------------------------|
| ChatGPT     | Sí (GPT-4o mini) | Sí, puede entrenar con ellos |
| Claude      | Sí (Claude Haiku)| 30 días por defecto     |
| Gemini      | Sí               | Términos ambiguos       |
| Copilot     | Sí               | Depende de la versión   |
```

**Cómo se ve:**
| Herramienta | Plan gratuito    | Guarda tus datos?            |
|-------------|------------------|------------------------------|
| ChatGPT     | Sí (GPT-4o mini) | Sí, puede entrenar con ellos |
| Claude      | Sí (Claude Haiku)| 30 días por defecto          |
| Gemini      | Sí               | Términos ambiguos            |
| Copilot     | Sí               | Depende de la versión        |

**Alineación de columnas — ejemplo con notas de alumnos:**
```
| Alumno     | Concepto evaluado  | Nota |
|:-----------|:------------------:|-----:|
| Ana García | Prompting básico   |  9.5 |
| Luis Pérez | AlterEgo y HITL    |  8.0 |
| Marta López| Smarkdown          | 10.0 |
```

| Alumno      | Concepto evaluado  | Nota |
|:------------|:------------------:|-----:|
| Ana García  | Prompting básico   |  9.5 |
| Luis Pérez  | AlterEgo y HITL    |  8.0 |
| Marta López | Smarkdown          | 10.0 |

- `:---` = alinear a la izquierda
- `:---:` = centrar
- `---:` = alinear a la derecha

> **Tip:** No importa si las columnas no están perfectamente alineadas en el código fuente. El resultado visual es el mismo.

---

## Línea horizontal (separador)

Tres guiones `---` en una línea sola crean una línea divisoria horizontal.

**Cómo se escribe:**
```
Texto antes del separador

---

Texto después del separador
```

Muy útil para separar secciones dentro de un documento largo.

---

## Saltos de línea y párrafos

Este es el error más común en Markdown:

| Lo que hacés | Lo que pasa |
|-------------|-------------|
| Presionás Enter una vez | El texto sigue en la **misma línea** visualmente |
| Dejás una **línea en blanco** entre dos párrafos | Se crean **dos párrafos separados** |
| Ponés dos espacios al final de una línea y Enter | Salto de línea dentro del mismo párrafo |

**Ejemplo:**
```
Este es el primer párrafo.
Esta línea parece separada pero se pega al párrafo anterior.

Este ya es un párrafo nuevo porque hay una línea en blanco arriba.
```

---

## Caracteres especiales: cómo escaparlos

Si necesitás mostrar un símbolo que Markdown usa (como `*`, `#`, `` ` ``, `_`), ponele una barra invertida `\` adelante.

```
\*esto no es cursiva\*
\# esto no es un título
```

Se ve: \*esto no es cursiva\* y \# esto no es un título

---

## Resumen visual: tabla de referencia rápida

| Elemento | Sintaxis | Resultado |
|----------|----------|-----------|
| Título nivel 1 | `# Título` | Título grande |
| Título nivel 2 | `## Título` | Título mediano |
| Título nivel 3 | `### Título` | Título chico |
| Negrita | `**texto**` | **texto** |
| Cursiva | `*texto*` | *texto* |
| Tachado | `~~texto~~` | ~~texto~~ |
| Código en línea | `` `código` `` | `código` |
| Link | `[texto](URL)` | enlace clickeable |
| Imagen | `![alt](ruta)` | imagen |
| Viñeta | `- elemento` | • elemento |
| Numerado | `1. elemento` | 1. elemento |
| Checkbox | `- [ ] tarea` | ☐ tarea |
| Cita | `> texto` | bloque destacado |
| Tabla | `\| col \| col \|` | tabla |
| Separador | `---` | línea horizontal |
| Bloque código | ` ```lenguaje ``` ` | código con color |

---

## Dónde se usa Markdown en este taller

| Herramienta | Soporta Markdown? | Notas |
|-------------|------------------|-------|
| **GitHub** | ✅ Sí, nativo | Los `.md` se renderizan automáticamente |
| **VS Code** | ✅ Sí | Ctrl+Shift+V para vista previa |
| **Jupyter Notebooks** | ✅ Sí | En celdas de tipo "Markdown" |
| **ChatGPT / Claude / Gemini** | ✅ Sí | La IA genera en Markdown y lo muestra formateado |
| **Notion** | ✅ Sí | Compatible con la mayoría de sintaxis |
| **WhatsApp** | ⚠️ Parcial | Solo negrita (`*texto*`) y tachado (`~texto~`) |
| **Word / Google Docs** | ❌ No nativo | Necesitás un plugin o convertir el archivo |

---

## Cómo ver el resultado en VS Code

1. Abrí un archivo `.md`
2. Presioná `Ctrl + Shift + V` (Windows) o `Cmd + Shift + V` (Mac)
3. Se abre una vista previa del Markdown renderizado lado a lado

O también: clic derecho sobre el archivo `.md` → **"Open Preview"**

---

---

## Ejemplo completo: un mini-apunte real en Markdown

Así se ve un documento real del taller escrito desde cero en Markdown:

```markdown
# Clase 3 — Vibe Coding

> **Filosofía:** La IA escribe el código, el ingeniero entiende qué hace.

## Objetivos

- Entender qué es el vibe coding
- Hacer tu primer programa sin escribir código a mano
- Aprender a revisar código generado por IA

## Pasos para tu primer programa

1. Describí el programa en lenguaje natural
2. Pegá la descripción en ChatGPT con formato Smarkdown
3. Copiá el código generado en un archivo `.py`
4. Ejecutalo y revisá si funciona
5. Pedile a la IA que explique cada línea

## Señales de alerta en código generado por IA

| Señal | Qué significa | Qué hacer |
|-------|---------------|-----------|
| `import librería_desconocida` | La IA inventó una librería | Buscala en PyPI antes de ejecutar |
| Comentarios demasiado genéricos | El código es de un ejemplo, no tuyo | Pedile que lo adapte a tu caso |
| `# TODO: implement this` | La IA dejó partes sin hacer | No ejecutes hasta completarlo |

## Ejemplo de código generado

```python
# Programa que saluda al usuario por su nombre
nombre = input("¿Cómo te llamás? ")
print(f"Hola, {nombre}! Bienvenido al taller de IA.")
```

> **Recordá:** Antes de ejecutar cualquier código generado por IA,
> leelo completo. No copies-pegues a ciegas.
```

---

> **En resumen:** Markdown es texto plano con señales visuales. No necesitás aprender nada de programación. Solo necesitás recordar media docena de símbolos (`#`, `**`, `*`, `-`, `>`, `` ` ``) y ya podés escribir documentos con formato completo.
