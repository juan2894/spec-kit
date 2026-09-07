# Módulo 3: Constitución y Especificación

En este módulo aprenderás las primeras dos fases activas del flujo de trabajo de **Spec Kit**:
1. Definir los principios rectores del proyecto a través de la **Constitución**.
2. Redactar especificaciones claras e inequívocas usando `/speckit.specify` y refinarlas con `/speckit.clarify`.

---

## 📖 1. La Constitución del Proyecto (`/speckit.constitution`)

Antes de pedirle a la IA que cree características específicas, es fundamental establecer las **reglas de juego** de la aplicación. La Constitución es un archivo guardado en `.specify/memory/constitution.md` que contiene los principios arquitectónicos, estándares de código, políticas de prueba y pautas de experiencia de usuario que el agente de IA **debe respetar en cada decisión posterior**.

### ¿Por qué es vital para principiantes?
Sin una constitución, la IA podría usar una librería UI diferente en cada pantalla, ignorar los tests automáticos o mezclar patrones de código incompatibles.

---

## 📖 2. Especificación de Características (`/speckit.specify`)

El comando `/speckit.specify` inicia el diseño funcional de una nueva característica. Aquí nos enfocamos en el **QUÉ** y el **POR QUÉ**, sin mencionar librerías ni arquitecturas concretas.

Un buen prompt de especificación incluye:
- El objetivo del usuario.
- Historias de usuario claras (*Como [rol], quiero [acción] para [beneficio]*).
- Reglas de negocio y comportamientos esperados.
- Casos límite o restricciones iniciales.

Al ejecutar `/speckit.specify`, Spec Kit crea automáticamente una rama de Git (ej. `001-create-taskify`) y un archivo `.md` de especificación bajo la carpeta `specs/`.

---

## 📖 3. Clarificación de Requisitos (`/speckit.clarify`)

Ninguna primera versión de especificación es perfecta. El comando `/speckit.clarify` hace que el agente de IA analice la especificación recién creada en busca de lagunas, supuestos ambiguos o detalles no especificados, haciéndote preguntas secuenciales para llenar esos vacíos antes de pasar a la fase técnica.

---

## 🛠️ 3. Ejercicio Práctico Paso a Paso

### Paso 1: Crear la Constitución de Taskify

Inicia tu agente de IA dentro de la carpeta `taskify-app` y ejecuta:

```text
/speckit.constitution Crear principios enfocados en la calidad del código, cobertura de pruebas unitarias superior al 80%, diseño accesible y limpio con HTML/CSS semántico, y rendimiento óptimo sin dependencias innecesarias.
```

Revisa el archivo generado en `.specify/memory/constitution.md`. Observa cómo se han registrado tus normas de desarrollo.

---

### Paso 2: Generar la primera especificación

Ejecuta el comando `/speckit.specify` proporcionando la descripción funcional de la app Taskify:

```text
/speckit.specify Desarrollar Taskify, una plataforma de productividad para equipos. Debe permitir crear proyectos, asignar miembros del equipo, agregar tareas y moverlas entre columnas en un tablero Kanban.

En esta primera fase:
- Tendremos 5 usuarios predefinidos (1 Product Manager y 4 Ingenieros). No se requiere pantalla de inicio de sesión con contraseña; el usuario simplemente selecciona su perfil al iniciar.
- Existirán 3 proyectos de ejemplo preconfigurados.
- Las columnas estándar del Kanban serán "To Do", "In Progress", "In Review" y "Done".
- En cada tarjeta de tarea se podrá cambiar el estado, asignar a un usuario y agregar comentarios ilimitados.
- Un usuario solo puede editar o eliminar sus propios comentarios.
- Las tareas asignadas al usuario actualmente seleccionado deben resaltarse visualmente en el tablero.
```

Spec Kit creará la rama `001-desarrollar-taskify` y redactará el archivo `specs/001-desarrollar-taskify/spec.md`.

---

### Paso 3: Clarificar ambigüedades

Ejecuta el comando de clarificación para que la IA detecte cabos sueltos:

```text
/speckit.clarify
```

La IA te formulará preguntas puntuales como:
> *"¿Qué sucede si se intenta eliminar una tarea que tiene comentarios?"* o *"¿Las tareas deben tener una fecha límite obligatoria?"*

Responde a sus preguntas para que la especificación quede completamente definida.

---

## 📌 Resumen de Puntos Clave

- **`/speckit.constitution`** define las reglas inquebrantables del proyecto (guardadas en `.specify/memory/constitution.md`).
- **`/speckit.specify`** crea la especificación funcional enfocada únicamente en el **QUÉ** y **POR QUÉ**.
- **`/speckit.clarify`** elimina ambigüedades mediante un cuestionario interactivo antes de empezar a programar.
- Todo el trabajo queda aislado en una rama de Git dedicada dentro del directorio `specs/`.

---

➡️ **Siguiente lección**: [Módulo 4: Planificación Técnica y Tareas](./04-planificacion-y-tareas.md)
