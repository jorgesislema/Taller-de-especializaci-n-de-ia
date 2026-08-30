# Opencode — Instalacion y manual

> Opencode es tu copiloto de IA en la terminal. Le escribis en español lo que necesitas y te genera codigo, explica errores, crea archivos o ejecuta comandos.
>
> Los instaladores (Node.js + Opencode) estan en el pendrive. Esta guia te muestra como instalarlos paso a paso.

---

## 1. Instalar Node.js (requisito)

Opencode necesita Node.js. Si ya lo tenes, salta al paso 2.

**Como verificar si ya lo tenes:**

Abrí una terminal (PowerShell en Windows, Terminal en Mac/Linux) y escribi:

```bash
node --version
npm --version
```

Si ves algo como `v20.x.x` y `10.x.x`, ya lo tenes. Anda al paso 2.

### Instalacion desde el pendrive (Windows)

1. Anda a la carpeta `NodeJS/` en el pendrive
2. Ejecuta `node-v20.x.x-x64.msi`
3. Instalacion estandar:
   - Next
   - Aceptar licencia (checkbox)
   - Next
   - **IMPORTANTE:** Asegurate de que "Add to PATH" este marcado
   - Install
   - Finish
4. **Cerras la terminal y la volves a abrir** (esto es clave)
5. Verifica: `node --version` y `npm --version`

### Instalacion desde el pendrive (Mac)

1. Carpeta `NodeJS/` → ejecuta `node-v20.x.x.pkg`
2. Segui el asistente de instalacion
3. Cerra y volve a abrir la terminal
4. Verifica: `node --version`

### Instalacion desde internet (alternativa)

1. Anda a [nodejs.org](https://nodejs.org/)
2. Descarga la version **LTS** (izquierda, la que dice "Recommended")
3. Instala con opciones por defecto
4. Reinicia la terminal
5. Verifica con `node --version`

---

## 2. Instalar Opencode

Con Node.js instalado, abri la terminal y ejecuta:

```bash
npm install -g opencode-ai@latest
```

> La `-g` significa "global": Opencode queda instalado en toda la computadora, no solo en una carpeta.

**Verifica que quedo instalado:**

```bash
opencode --version
```

Deberias ver un numero de version como `v1.x.x`.

### Metodos alternativos (si npm no funciona)

**Windows:**
```bash
# Con Scoop (si lo tenes instalado)
scoop install opencode

# Con Chocolatey (si lo tenes instalado)
choco install opencode
```

**Mac / Linux:**
```bash
# Con Homebrew (recomendado)
brew install opencode

# Universal (curl)
curl -fsSL https://opencode.ai/install | bash
```

### Opencode Desktop (opcional)

Opencode tambien tiene aplicacion de escritorio. Descargala desde [opencode.ai/download](https://opencode.ai/download) si preferis ventanas en vez de terminal.

---

## 3. Primeros pasos con Opencode

### Abrir Opencode

En la terminal, simplemente escribi:

```bash
opencode
```

Se abre la interfaz interactiva. Es como un chat, pero dentro de la terminal.

### Tu primer comando

Escribi tu primer pedido en la interfaz de Opencode:

```
genera un archivo hola.py que imprima "Hola mundo desde Opencode!" y explicalo
```

Opencode va a:
1. Crear el archivo `hola.py` en tu carpeta actual
2. Escribir el codigo Python adentro
3. Explicarte linea por linea que hace

Probalo. Tarda unos segundos y es magico la primera vez.

### Comandos directos (sin abrir la interfaz)

Tambien podes pedirle cosas sin entrar al chat:

```bash
opencode "crea un README.md basico para un proyecto de Python"

opencode "que hace este comando: git log --oneline --graph"

opencode "explicame este error: ModuleNotFoundError: No module named 'requests'"
```

---

## 4. Lo que Opencode puede hacer

| Tarea | Ejemplo de comando |
|-------|-------------------|
| Generar codigo | "crea una funcion que calcule el promedio de una lista de numeros" |
| Explicar codigo | "explicame que hace este archivo linea por linea" |
| Debuggear errores | "me tira este error: NameError... que significa y como lo arreglo?" |
| Mejorar codigo | "revisa mi codigo y sugiere mejoras" |
| Escribir documentacion | "genera un README.md para este proyecto" |
| Ejecutar comandos | "busca todos los archivos .py en esta carpeta" |
| Crear archivos | "crea un .gitignore para un proyecto de Python" |

---

## 5. Como usarlo eficientemente

### Regla 1: Se especifico

```
MAL:  "ayudame con mi codigo"
BIEN: "revisa el archivo calculadora.py. La funcion dividir()
       falla cuando el segundo numero es 0. Como lo arreglo?"
```

### Regla 2: Da contexto

Opencode "ve" toda tu carpeta de proyecto. Menciona archivos especificos para que sepa donde mirar.

```
BIEN: "En el archivo main.py, linea 15, hay un error de sintaxis.
       Cual es y como lo corrijo?"
```

### Regla 3: Itera

```
Primer prompt: "crea un script que lea un archivo CSV y muestre
               el promedio de la columna 'ventas'"

Segundo prompt: "ahora agregale que tambien muestre cual fue
                el mes con mas ventas"

Tercer prompt: "cambia el formato de salida a una tabla Markdown"
```

El 90% de usar Opencode es saber iterar. El primer resultado casi nunca es perfecto.

### Regla 4: Conecta con VSCode

Abrí VSCode y la terminal integrada (`Ctrl+` `) en la misma carpeta. Podes:
1. Pedirle algo a Opencode en la terminal
2. Ver el resultado en VSCode al instante
3. Editar lo que haga falta
4. Pedirle ajustes

---

## 6. Opencode vs. ChatGPT/Claude/Gemini

| Caracteristica | Opencode | ChatGPT Web | Claude Web |
|---------------|----------|-------------|------------|
| Donde funciona | Terminal | Navegador | Navegador |
| Ve tus archivos | Si, toda la carpeta | Solo lo que subis | Solo lo que subis |
| Ejecuta comandos | Si (con permiso) | No | No |
| Crea archivos | Si | No | No |
| Gratis | Si (con Copilot gratis o API propia) | Si (limitado) | Si (limitado) |
| Ideal para | Programar, debugear, archivos | Charlar, brainstorm, prompts | Charlar, textos largos, analisis |

> **No compiten: se complementan.** Usa ChatGPT/Claude para pensar y planear. Usa Opencode para ejecutar, codificar, crear archivos.

---

## 7. Solucion de problemas

### "npm: command not found"
Node.js no esta instalado o no esta en el PATH. Reinstala Node.js asegurandote de marcar "Add to PATH".

### "opencode: command not found"
Opencode no se instalo correctamente. Revisa:
1. `npm install -g opencode-ai@latest` (ejecutalo de nuevo)
2. Cerra y reabri la terminal
3. Si seguis con problemas, proba con `npx opencode-ai`

### "Permission denied" (Mac/Linux)
```bash
sudo npm install -g opencode-ai@latest
```

### Error de ejecucion de scripts (Windows PowerShell)
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
(Ejecutalo una vez como administrador, despues volve a probar)

### Opencode se instalo pero no responde
Revisa tu conexion a internet. Opencode necesita conexion para comunicarse con los modelos de IA.
