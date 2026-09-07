# Módulo 1: Introducción a Spec-Driven Development (SDD)

Bienvenido al primer módulo del curso. En esta lección aprenderás los conceptos fundamentales de **Spec-Driven Development (SDD)** (Desarrollo Guiado por Especificaciones) y por qué transforma radicalmente la forma de construir software con asistencia de Inteligencia Artificial.

---

## 📖 1. ¿Qué es Spec-Driven Development (SDD)?

Durante décadas, en la industria del software el **código fuente** ha sido el producto principal. Las especificaciones, requisitos y documentos de diseño solían tratarse como andamios temporales que se descartaban una vez iniciada la programación.

Con la llegada de las herramientas de IA generativa, surgió la práctica popular conocida como *"vibe coding"*: escribir prompts informales y dejar que la IA genere código directamente. Sin embargo, en proyectos medianos o grandes, este enfoque suele fracasar debido a:
- Falta de coherencia arquitectónica.
- Olvido de casos borde e inconsistencias en la interfaz.
- Acumulación de código espagueti difícil de mantener.

**Spec-Driven Development invierte la balanza**:
En SDD, **las especificaciones se vuelven ejecutables**. La especificación escrita deja de ser un documento pasivo para convertirse en la fuente única de verdad (*Single Source of Truth*) a partir de la cual los agentes de IA generan planes técnicos, listas de tareas estructuradas e código ejecutable.

---

## 🏛️ 2. ¿Qué es Spec Kit?

**Spec Kit** es un conjunto de herramientas de código abierto (*toolkit*) creado por GitHub que automatiza el flujo de trabajo SDD. Proporciona:
1. Una interfaz de línea de comandos CLI (`specify-cli`) para inicializar proyectos y gestionar plantillas.
2. Un conjunto de comandos barra (slash commands) como `/speckit.specify`, `/speckit.plan`, `/speckit.tasks` e `/speckit.implement`.
3. Compatibilidad con más de 30 agentes de codificación por IA (GitHub Copilot, Claude Code, Gemini CLI, Cursor, etc.).

---

## 🏢 3. Caso de Uso del Mundo Real: "Taskify"

A lo largo de este curso, utilizaremos un proyecto del mundo real llamado **Taskify**: una aplicación de gestión de tareas colaborativa estilo Kanban para equipos de producto y desarrollo.

Sin SDD, pedirle a una IA *"Créame un Trello sencillo"* suele generar una app incompleta, sin persistencia de datos adecuada o sin control de permisos. Con SDD y Spec Kit, aprenderemos a definir rigurosamente qué debe hacer Taskify antes de escribir una sola línea de código.

---

## 🛠️ 4. Ejercicio Práctico Paso a Paso

### Objetivo
Explorar la estructura mental de una especificación ejecutable comparando un prompt informal frente a una especificación estructurada.

### Paso 1: Analizar el enfoque informal ("Vibe Coding")
Imagina enviar el siguiente mensaje a un asistente de IA:
> *"Hazme una app de tareas en React con columnas To Do y Done."*

**Problema**: La IA asumirá respuestas a preguntas críticas sin preguntarte:
- ¿Cómo se guardan las tareas? ¿En memoria o en base de datos?
- ¿Se pueden editar las tareas creadas?
- ¿Hay usuarios o roles?

### Paso 2: Analizar la estructura de una Especificación SDD
En SDD, definimos la especificación respondiendo al **QUÉ** y al **POR QUÉ**, postergando el **CÓMO** técnico para la fase de planificación.

Observa cómo Spec Kit organiza los requisitos en tres pilares:
1. **Historias de Usuario** (*User Stories*): Define quién realiza la acción y qué beneficio obtiene.
2. **Requisitos Funcionales**: Reglas de negocio claras e inequívocas.
3. **Criterios de Aceptación**: Condiciones verificables para considerar la característica terminada.

---

## 📌 Resumen de Puntos Clave

- **SDD (Spec-Driven Development)** convierte las especificaciones en artefactos ejecutables que guían a la IA.
- **Spec Kit** es la herramienta que proporciona los comandos y la estructura para implementar SDD en cualquier proyecto.
- **Separación de responsabilidades**: La especificación define el *QUÉ* (funcionalidad), mientras que el plan define el *CÓMO* (tecnología y arquitectura).
- Evitamos el *"vibe coding"* para obtener resultados predecibles, testeables y de alta calidad.

---

➡️ **Siguiente lección**: [Módulo 2: Instalación y Configuración](./02-instalacion-y-configuracion.md)
