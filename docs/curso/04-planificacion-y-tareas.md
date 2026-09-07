# Módulo 4: Planificación Técnica y Desglose de Tareas

Una vez definida y aclarada la especificación funcional, es momento de traducir las necesidades del usuario en decisiones técnicas concretas. En este módulo aprenderás a utilizar `/speckit.plan` para definir la arquitectura y `/speckit.tasks` para descomponer la solución en tareas pequeñas y ordenadas.

---

## 📖 1. Creación del Plan Técnico (`/speckit.plan`)

Mientras que la especificación respondía al **QUÉ**, el plan técnico responde al **CÓMO**. Aquí indicaremos las decisiones tecnológicas de nuestro proyecto:
- Lenguaje y marco de trabajo (*framework*).
- Base de datos y modelo de datos.
- Contratos de API (REST, GraphQL, WebSocket).
- Estrategia de pruebas unitarias e integración.

Al ejecutar `/speckit.plan`, Spec Kit analiza la especificación funcional y la constitución para generar una serie de documentos en la carpeta del feature (ej. `specs/001-desarrollar-taskify/`):
- `plan.md`: El plan maestro de arquitectura.
- `data-model.md`: Entidades, relaciones y esquemas de base de datos.
- `contracts/`: Especificaciones OpenAPI/JSON Schema de las APIs.
- `research.md`: Investigaciones técnicas y decisiones de librerías.

---

## 📖 2. Desglose en Lista de Tareas (`/speckit.tasks`)

Pedirle a un agente de IA que construya toda una aplicación en un solo paso suele provocar errores por exceso de contexto o falta de orden.

El comando `/speckit.tasks` transforma el plan técnico en un archivo `tasks.md` altamente estructurado que organiza las tareas considerando:
1. **Orden de Dependencias**: Crear modelos antes que controladores, y controladores antes de la interfaz visual.
2. **Marcadores de Paralelismo `[P]`**: Identifica tareas independientes que se pueden desarrollar en paralelo.
3. **Rutas Exactas de Archivos**: Cada tarea especifica qué archivos crear o modificar.
4. **Puntos de Control (Checkpoints)**: Verificaciones intermedias para validar que cada historia de usuario funciona antes de pasar a la siguiente.

---

## 🛠️ 3. Ejercicio Práctico Paso a Paso

### Paso 1: Generar el Plan Técnico de Taskify

Ejecuta `/speckit.plan` indicando el stack tecnológico elegido para Taskify:

```text
/speckit.plan Construiremos Taskify usando Node.js con Express para el servidor backend y SQLite como base de datos ligera. El frontend usará HTML, CSS y JavaScript Vanilla (sin frameworks pesados), aprovechando la API nativa de Drag and Drop del navegador para el tablero Kanban. Incluye pruebas unitarias con Jest.
```

Revisa los archivos generados dentro de `specs/001-desarrollar-taskify/`:
- Abre `data-model.md` para inspeccionar la estructura de las tablas `Users`, `Projects`, `Tasks` y `Comments`.
- Abre `plan.md` para verificar las fases de desarrollo propuestas.

---

### Paso 2: Generar la Lista de Tareas

Con el plan validado, ejecuta el comando de descomposición de tareas:

```text
/speckit.tasks
```

Spec Kit generará el archivo `specs/001-desarrollar-taskify/tasks.md`.

---

### Paso 3: Inspeccionar la estructura de `tasks.md`

Abre el archivo `tasks.md` y observa cómo las tareas están clasificadas:

```markdown
## Fase 1: Configuración Inicial del Proyecto
- [ ] Tarea 1.1: Inicializar estructura de archivos en `src/` e instalar dependencias (express, sqlite3, jest)
- [ ] Tarea 1.2: Configurar esquema SQLite en `src/db/schema.sql`

## Fase 2: Historias de Usuario - Gestión de Usuarios y Proyectos
- [ ] Tarea 2.1: [P] Crear modelo de datos `User` en `src/models/user.js`
- [ ] Tarea 2.2: [P] Crear modelo de datos `Project` en `src/models/project.js`
- [ ] Tarea 2.3: Implementar endpoints `/api/users` y `/api/projects` en `src/routes/`
- [ ] CHECKPOINT: Verificar que la API responde con los 5 usuarios y 3 proyectos iniciales

## Fase 3: Tablero Kanban e Interacción
...
```

---

## 📌 Resumen de Puntos Clave

- **`/speckit.plan`** define el **CÓMO** técnico (stack, base de datos, arquitectura y contratos).
- Genera documentación de arquitectura (`plan.md`, `data-model.md`, `contracts/`).
- **`/speckit.tasks`** convierte el plan en una secuencia de tareas accionables en `tasks.md`.
- Respetar el orden de dependencias en las tareas evita errores en cadena durante la compilación e implementación.

---

➡️ **Siguiente lección**: [Módulo 5: Implementación y Verificación](./05-implementacion-y-verificacion.md)
