# Setup de Entorno — VSCode + Python + Git

> Guía paso a paso para dejar tu computadora lista para las próximas clases.
> Elegí tu sistema operativo y seguí esa sección.

---

## Tabla de contenido

1. [Instalar Python 3](#1-instalar-python-3)
2. [Instalar VSCode + extensiones](#2-instalar-vscode--extensiones)
3. [Instalar Git](#3-instalar-git)
4. [Clonar el repo del taller](#4-clonar-el-repo-del-taller)
5. [Crear un entorno virtual](#5-crear-un-entorno-virtual)
6. [Ejecutar el notebook](#6-ejecutar-el-notebook)
7. [Checklist final](#7-checklist-final)
8. [Problemas comunes](#8-problemas-comunes)

---

## 1. Instalar Python 3

Necesitamos Python 3.8 o superior. Vamos a verificar si ya lo tenés antes de instalar.

### ¿Ya lo tenés?

Abrí una terminal:

- **Windows:** tecleá `cmd` en el menú inicio y abrí "Símbolo del sistema".
- **macOS / Linux:** abrí la app "Terminal".

Ejecutá:

```bash
python --version
```

Si te dice algo como `Python 3.11.x`, **ya lo tenés**. Saltá a la sección 2.

> **Windows:** a veces el comando es `py --version`. Si `python` no funciona, probá `py`.

Si te dice "comando no reconocido" o la versión es Python 2.x, instalá:

### Windows

1. Andá a https://www.python.org/downloads/
2. Descargá el instalador de Python 3 (botón amarillo grande).
3. Ejecutá el instalador.
4. ⚠️ **MUY IMPORTANTE:** marcá la casilla **"Add Python to PATH"** abajo del instalador, antes de clicar "Install Now".
5. Clic en "Install Now" y esperá.
6. Cerrá y volvé a abrir la terminal. Verificá con `python --version`.

### macOS

Opción A (recomendada, con Homebrew):

```bash
brew install python
```

Si no tenés Homebrew, instalalo primero desde https://brew.sh

Opción B (desde python.org): igual que Windows, descargá el instalador desde https://www.python.org/downloads/

Verificá:

```bash
python3 --version
```

> En macOS, el comando suele ser `python3` (no `python`).

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Verificá:

```bash
python3 --version
```

---

## 2. Instalar VSCode + extensiones

VSCode es el editor de código que vamos a usar. Es gratis y de Microsoft.

### Instalar VSCode

1. Andá a https://code.visualstudio.com/
2. Descargá la versión para tu sistema.
3. Instalalo con las opciones por defecto.

### Extensiones necesarias

Abrí VSCode y instalá estas extensiones (barra lateral izquierda, ícono de cuadrados → "Extensions"):

1. **Python** (de Microsoft) — para que VSCode entienda Python.
2. **Jupyter** (de Microsoft) — para ejecutar notebooks `.ipynb` dentro de VSCode.

> Para instalar una extensión: buscá su nombre → clic en "Install".

### Verificá que funciona

1. En VSCode, abrí un archivo nuevo (`File → New File`).
2. Guardalo como `prueba.py` (`File → Save As`).
3. Escribí: `print("hola")`
4. Clic derecho → "Run Python File in Terminal". Deberías ver `hola` abajo.

---

## 3. Instalar Git

Git es el sistema de control de versiones. Lo usamos para bajar el repo del taller y, más adelante, para gestionar código.

### ¿Ya lo tenés?

En la terminal:

```bash
git --version
```

Si te dice algo como `git version 2.43.x`, ya lo tenés. Saltá a configurarlo (siguiente paso).

### Windows

1. Andá a https://git-scm.com/download/win
2. Descargá el instalador.
3. Ejecutalo con las opciones por defecto (Next, Next, Next...).
4. Cerrá y volvé a abrir la terminal.

### macOS

```bash
git --version
```

Si no está, macOS te ofrecerá instalar las Command Line Tools. Aceptá. O con Homebrew:

```bash
brew install git
```

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install git
```

### Configurá tu identidad (una sola vez)

Decile a Git quién sos (necesario para los commits):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

Verificá:

```bash
git config --global user.name
git config --global user.email
```

---

## 4. Clonar el repo del taller

En la terminal, andá a la carpeta donde quieras guardar el repo:

```bash
# Windows (ejemplo, Documents)
cd Documents

# macOS / Linux (ejemplo, home)
cd ~
```

Cloná:

```bash
git clone https://github.com/jorgesislema/Taller-de-especializaci-n-de-ia.git
```

Entrá al repo:

```bash
cd Taller-de-especializaci-n-de-ia
```

Verificá que ves los archivos:

```bash
# Windows
dir

# macOS / Linux
ls
```

Deberías ver `README.md`, `TEMARIO.md`, la carpeta `Clase-01-...`, etc.

---

## 5. Crear un entorno virtual

Un **entorno virtual** (venv) es una carpeta donde instalás las librerías de Python **solo para este proyecto**, sin afectar el resto de tu sistema.

### Crear el venv

Desde la carpeta del repo:

**Windows:**

```bash
python -m venv venv
```

**macOS / Linux:**

```bash
python3 -m venv venv
```

### Activar el venv

**Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

> Si te da error de "ejecución de scripts deshabilitada", abrí PowerShell como administrador y ejecutá una vez:
> ```bash
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Después volvé a probar.

**Windows (cmd):**

```bash
venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### Sabés que está activo cuando...

Veas `(venv)` al principio del prompt de la terminal. Ej:

```
(venv) C:\Users\alumno\Taller-de-especializaci-n-de-ia>
```

> **Cada vez que abras una terminal nueva para trabajar en el taller, vas a tener que activar el venv de nuevo.** Es normal.

---

## 6. Ejecutar el notebook

1. En VSCode, abrí la carpeta del repo (`File → Open Folder` → elegí `Taller-de-especializaci-n-de-ia`).
2. Navegá a `Clase-01-Evolucion-de-la-IA-y-Setup-de-Entorno/perceptron.ipynb` y abrilo.
3. VSCode te va a preguntar qué kernel usar. Elegí el entorno `venv` que acabás de crear (o "Python Environments" → `Python 3.x.x ('venv')`).
4. Si VSCode te ofrece instalar dependencias (ipykernel), aceptá.
5. Clic en la celda de código → botón **"Run All"** arriba, o `Shift + Enter` celda por celda.

El notebook debería correr sin instalar nada extra (usa solo `random` y `math`). Si tenés matplotlib, mejor; si no, el código usa fallback ASCII.

---

## 7. Checklist final

Marcá mentalmente cada uno:

- [ ] `python --version` (o `python3`) me da 3.8 o superior.
- [ ] Tengo VSCode instalado.
- [ ] Tengo las extensiones **Python** y **Jupyter** en VSCode.
- [ ] `git --version` me da una versión.
- [ ] Configuré `user.name` y `user.email` en Git.
- [ ] Cloné el repo y veo los archivos.
- [ ] Creé y activé el venv.
- [ ] Abrí y ejecuté `perceptron.ipynb` sin errores.

Si todos están ✅, **estás listo para la Clase 2.**

---

## 8. Problemas comunes

### "python: command not found" (Windows)

Usá `py` en lugar de `python`. O reinstalá Python marcando "Add Python to PATH".

### "python3: command not found" (macOS/Linux)

Probá con `python`. Si no está, instalá con `brew install python` (mac) o `sudo apt install python3` (Linux).

### VSCode no me deja ejecutar el notebook

Asegurate de:
1. Tener la extensión **Jupyter** instalada.
2. Haber activado el venv antes de abrir VSCode, o seleccionar el kernel `venv` cuando te lo pida.

### "Permission denied" al activar el venv (Windows PowerShell)

Es la política de ejecución. Ejecutá una vez como admin:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### El notebook dice que falta matplotlib

No lo necesita. El notebook está pensado para correr **sin matplotlib** (usa fallback ASCII). Si querés gráficos bonitos, instalalo dentro del venv:

```bash
pip install matplotlib
```

### No me aparece el kernel `venv` en VSCode

1. Activá el venv en la terminal.
2. Instalá ipykernel dentro del venv:

```bash
pip install ipykernel
```

3. Cerrá y volvé a abrir VSCode.

---

> ¿Te trabaste en algún paso? Anotá dónde y lo vemos en la clase de consulta.
