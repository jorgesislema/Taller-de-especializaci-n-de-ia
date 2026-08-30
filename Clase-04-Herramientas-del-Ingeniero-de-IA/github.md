# Git y GitHub — Guia practica

> Git es el sistema de control de versiones. GitHub es la pagina donde se guardan los repositorios.
> Vas a aprender los dos metodos: terminal (CLI) y aplicacion (GitHub Desktop).

---

## Parte A: Git CLI — Comandos esenciales

### La analogia de la foto

Imagina que tu proyecto es un album de fotos. Cada vez que llegas a un punto importante, sacas una foto y la guardas con una etiqueta.

```
Tu proyecto → git add     (elegis que entra en la foto)
            → git commit  (sacas la foto y le pones etiqueta)
            → git push    (subis la foto al album online en GitHub)
```

### Los 7 comandos que necesitas

| Comando | Que hace | Analogia |
|---------|---------|----------|
| `git clone <url>` | Baja un repositorio de GitHub a tu compu | Fotocopiar un libro |
| `git status` | Te dice que archivos cambiaron desde el ultimo commit | Revisar el album y ver que fotos faltan |
| `git add <archivo>` | Marca un archivo para el proximo commit | Elegir una foto para poner en el album |
| `git add .` | Marca TODOS los cambios de una vez | Meter todas las fotos juntas |
| `git commit -m "mensaje"` | Guarda los cambios con descripcion | Pegar la foto en el album con una nota |
| `git push` | Sube los commits a GitHub | Mandar el album a tus amigos |
| `git pull` | Baja los cambios que otros hicieron | Recibir las fotos que sacaron otros |
| `git log --oneline` | Muestra el historial de commits resumido | Ver el indice del album |

### Configuracion inicial (si no la hiciste en Clase 1)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

Verifica que quedo:

```bash
git config --global user.name
git config --global user.email
```

### Flujo tipico de trabajo

```bash
# 1. Ver que cambiaste
git status

# 2. Agregar los cambios
git add .

# 3. Guardar con mensaje descriptivo
git commit -m "Agrego la seccion de proyectos al portfolio"

# 4. Subir
git push
```

### Flujo para crear un repo desde cero

```bash
# 1. Crear carpeta
mkdir mi-proyecto
cd mi-proyecto

# 2. Inicializar Git
git init

# 3. Crear archivos...
#    (escribis tu codigo o tu README)

# 4. Primer commit
git add .
git commit -m "Commit inicial"

# 5. Crear repo en GitHub.com...

# 6. Conectar local con remoto
git remote add origin https://github.com/TU-USUARIO/mi-proyecto.git

# 7. Renombrar rama a main
git branch -M main

# 8. Subir
git push -u origin main
```

### Como escribir buenos mensajes de commit

```
BUENO: "Agrego la seccion de habilidades al portfolio"
BUENO: "Corrijo el link roto en la seccion de contacto"
BUENO: "Actualizo los proyectos con fechas"

MALO:  "cambios"
MALO:  "fix"
MALO:  "asdfghjkl"
MALO:  "."
```

> **Regla:** El mensaje del commit debe responder a la pregunta: "Si dentro de 6 meses leo esto, voy a entender que hice?"

---

## Parte B: GitHub Desktop

GitHub Desktop es la version con botones de Git. No necesitas comandos.

### Instalacion

1. El instalador esta en el pendrive: carpeta `GitHubDesktop/`
2. Ejecuta el instalador:
   - Windows: `GitHubDesktopSetup.exe`
   - Mac: `GitHubDesktop.dmg`
3. Next, Next, aceptar licencia, Install, Finish
4. Al abrir, inicia sesion con tu cuenta de GitHub
5. Configura nombre y email (los mismos de `git config`)

### Flujo basico

```
┌─────────────────────────────────────────────┐
│  1. File → Clone Repository                 │
│     (pega la URL de tu repo de GitHub)      │
│                                             │
│  2. Haces cambios en tus archivos           │
│     (con VSCode o el editor que uses)       │
│                                             │
│  3. GitHub Desktop detecta los cambios      │
│     Panel izquierdo: archivos modificados   │
│                                             │
│  4. Escribis mensaje en "Summary"           │
│     Clic en "Commit to main"               │
│                                             │
│  5. Clic en "Push origin" para subir        │
└─────────────────────────────────────────────┘
```

### Añadir un repo local

Si ya tenes una carpeta con Git iniciado:

1. `File → Add Local Repository`
2. Elegi la carpeta
3. Listo, GitHub Desktop la reconoce

### Ver que cambiaste

El panel del medio te muestra:
- **Verde:** lineas agregadas
- **Rojo:** lineas borradas

Esto se llama "diff" (diferencia). Es lo mas util de cualquier herramienta Git.

### Cuando usar cada uno

| Situacion | Que usar |
|-----------|----------|
| Commits del dia a dia | GitHub Desktop (mas facil) |
| Ver cambios visualmente | GitHub Desktop (el diff es mejor) |
| Algo salio mal y necesitas control total | Terminal (mas comandos disponibles) |
| Estas siguiendo un tutorial que usa comandos | Terminal |
| Queres sentirte hacker | Terminal |

> Los dos usan el mismo Git por debajo. No son incompatibles. Podes hacer un commit en GitHub Desktop y despues hacer `git log` en la terminal. Es el mismo historial.

---

## Problemas comunes

### "fatal: not a git repository"
Estas en una carpeta que no tiene Git iniciado. Navega a la carpeta correcta o hace `git init`.

### "failed to push some refs"
Alguien subio cambios antes que vos. Hace `git pull` primero, despues `git push`.

### "Please tell me who you are"
No configuraste nombre y email. Corre `git config --global user.name` y `user.email`.

### Me equivoque en el mensaje del commit
```bash
git commit --amend -m "El mensaje correcto"
```
Solo funciona si todavia NO hiciste push.

### Quiero deshacer el ultimo commit (sin perder los cambios)
```bash
git reset --soft HEAD~1
```

### GitHub Desktop no me deja hacer push
Revisa que hayas iniciado sesion con tu cuenta correcta en `File → Options → Accounts`.
