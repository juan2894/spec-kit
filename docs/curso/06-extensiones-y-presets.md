# Módulo 6: Extensiones y Presets

¡Felicitaciones por llegar al último módulo! Ahora que dominas el flujo estándar de Spec Kit, aprenderás a **extender y personalizar** su comportamiento para adaptarlo a las necesidades de tu empresa, equipo o proyecto específico mediante **Extensiones** y **Presets**.

---

## 📖 1. Personalización de Spec Kit

Spec Kit ofrece dos mecanismos de extensión complementarios para adaptar la herramienta sin modificar su código base:

| Mecanismo | ¿Qué hace? | Ejemplo de uso | Comando CLI |
| :--- | :--- | :--- | :--- |
| **Extensiones** | Agregan **nuevas capacidades y comandos** que Spec Kit no incluye de manera nativa. | Agregar integración con Jira, revisiones de código automáticas post-implementación o diagnósticos de salud del proyecto. | `specify extension add` |
| **Presets** | Personalizan **CÓMO** funcionan los comandos y plantillas existentes de Spec Kit. | Enforzar plantillas con normas de cumplimiento regulatorio, cambiar la terminología (ej. estilo Agile, Scrum o Kanban) o adaptar prompts. | `specify preset add` |

---

## 📖 2. Jerarquía de Plantillas y Sobrescritura

Spec Kit resuelve las plantillas en tiempo de ejecución utilizando una jerarquía de prioridades estricta (de mayor a menor prioridad):

1. ⬆️ **Sobrescrituras Locales del Proyecto**: `.specify/templates/overrides/`
2. 🥈 **Presets**: `.specify/presets/templates/`
3. 🥉 **Extensiones**: `.specify/extensions/templates/`
4. ⬇️ **Núcleo de Spec Kit**: `.specify/templates/`

Si deseas personalizar cómo se genera la especificación solo en un proyecto, no necesitas crear una extensión o preset; basta con colocar tu plantilla modificada en `.specify/templates/overrides/spec-template.md`.

---

## 🛠️ 3. Ejercicio Práctico Paso a Paso

### Paso 1: Buscar e instalar un Preset de la comunidad

Abre tu terminal y explora los presets disponibles con el CLI de Specify:

```bash
specify preset search
```

Para instalar un preset (por ejemplo, un preset de auditoría de seguridad o estilo específico):

```bash
specify preset add <nombre-del-preset>
```

---

### Paso 2: Buscar e instalar una Extensión

Explora las extensiones creadas por la comunidad:

```bash
specify extension search
```

Para instalar una extensión que añada nuevos comandos a tu agente de IA:

```bash
specify extension add <nombre-de-extension>
```

---

### Paso 3: Crear una sobrescritura local personalizada (Project Overrides)

Imagina que en tu equipo es obligatorio que toda especificación incluya una sección explícita sobre **Consideraciones de Seguridad y Privacidad**.

1. Copia la plantilla base a la carpeta de sobrescritura local:
   ```bash
   mkdir -p .specify/templates/overrides
   cp .specify/templates/spec-template.md .specify/templates/overrides/spec-template.md
   ```

2. Edita `.specify/templates/overrides/spec-template.md` y añade la nueva sección requerida:
   ```markdown
   ## 🔒 Requisitos de Seguridad y Privacidad
   - [ ] ¿El componente maneja datos personales (PII)?
   - [ ] Requisitos de encriptación en tránsito y en reposo.
   ```

3. A partir de este momento, cada vez que ejecutes `/speckit.specify` en este proyecto, Spec Kit usará tu plantilla personalizada con la sección de seguridad.

---

## 📌 Resumen de Puntos Clave

- **Extensiones** añaden *nuevas funcionalidades y comandos*.
- **Presets** personalizan el *formato, vocabulario y comportamiento* de los comandos existentes.
- **Sobrescrituras locales** (`.specify/templates/overrides/`) permiten personalizar plantillas para un único proyecto de forma rápida.
- Spec Kit es completamente modular y adaptable a cualquier metodología de trabajo (Scrum, Kanban, Waterfall, TDD, etc.).

---

## 🎉 ¡Enhorabuena!

Has completado el curso completo de **Spec Kit y Spec-Driven Development**. Ahora tienes el conocimiento y las herramientas para construir software de alta calidad de forma predecible, ordenada y eficiente junto a agentes de IA.

➡️ Volver al [Índice del Curso](./index.md)
