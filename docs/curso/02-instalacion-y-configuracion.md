# Módulo 2: Instalación y Configuración del Entorno

En este módulo aprenderás a instalar las herramientas necesarias para trabajar con **Spec Kit**, preparar tu entorno local y configurar la integración con tu agente de codificación por Inteligencia Artificial favorito.

---

## 📖 1. Requisitos Previos del Sistema

Para utilizar Spec Kit y ejecutar el CLI `specify` necesitas contar con los siguientes elementos en tu equipo:

1. **Sistema Operativo**: Linux, macOS o Windows (WSL2 recomendado en Windows).
2. **Python 3.11 o superior**: Lenguaje base sobre el cual opera el CLI.
3. **uv**: Administrador de paquetes de Python ultrarrápido escrito en Rust (Recomendado).
4. **Git**: Para el control de versiones y manejo automático de ramas de características.
5. **Agente de IA compatible**: Un agente instalado y autenticado (ej. GitHub Copilot, Claude Code, Gemini CLI, Cursor CLI, etc.).

---

## 🛠️ 2. Ejercicio Práctico Paso a Paso: Instalación y Primer Proyecto

### Paso 1: Instalar `uv` (Gestor de Paquetes)

`uv` es la forma oficial y recomendada de instalar y ejecutar `specify-cli`.

**En macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**En Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verifica la instalación ejecutando:
```bash
uv --version
```

---

### Paso 2: Instalar Specify CLI

Instala la versión global de `specify-cli` mediante `uv tool`:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Verifica que el comando `specify` esté disponible en la terminal:
```bash
specify --version
```

---

### Paso 3: Inicializar un nuevo proyecto

Crearemos nuestro proyecto del curso llamado `taskify-app`:

```bash
specify init taskify-app --integration copilot
```

> 💡 **Nota sobre integraciones**: Puedes reemplazar `copilot` por tu agente preferido, por ejemplo: `--integration claude`, `--integration gemini`, `--integration cursor`, `--integration codex`, etc. Para ver la lista completa de agentes soportados ejecuta `specify integration list`.

Entra en la carpeta creada:
```bash
cd taskify-app
```

Examina la estructura generada con `ls -la`:
```text
.
├── .specify/
│   ├── memory/
│   │   └── constitution.md
│   ├── scripts/
│   └── templates/
└── README.md
```

---

## 🏢 3. Caso de Uso del Mundo Real: Verificación de Integración

Cuando inicializas un proyecto con `specify init`, Spec Kit instala los comandos personalizados (Slash Commands) en la configuración de tu agente de IA.

Por ejemplo, si estás utilizando **Claude Code** o **GitHub Copilot CLI**, se habrán instalado los comandos:
- `/speckit.constitution`
- `/speckit.specify`
- `/speckit.clarify`
- `/speckit.plan`
- `/speckit.tasks`
- `/speckit.implement`

Para comprobar que la integración está lista, inicia tu agente en la carpeta del proyecto y escribe `/speckit.` para verificar que autocompleta los comandos disponibles.

---

## 📌 Resumen de Puntos Clave

- **`uv`** es el método preferido para instalar `specify-cli` de manera rápida e aislada.
- **`specify init <nombre_proyecto>`** descarga las plantillas, scripts y comandos barra necesarios.
- El parámetro `--integration` especifica para qué agente de IA se deben registrar las habilidades o comandos personalizados.
- Todo proyecto administrado por Spec Kit guarda sus reglas y plantillas en el directorio oculto `.specify/`.

---

➡️ **Siguiente lección**: [Módulo 3: Constitución y Especificación](./03-constitucion-y-especificacion.md)
