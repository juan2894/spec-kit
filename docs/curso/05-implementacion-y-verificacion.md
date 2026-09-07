# Módulo 5: Implementación y Verificación

En este módulo llegamos a la etapa donde la magia de Spec Kit se materializa: la **construcción automática de código**. Aprenderás a ejecutar `/speckit.implement` para procesar la lista de tareas, aplicar Desarrollo Guiado por Pruebas (*Test-Driven Development* o TDD) y verificar la aplicación terminada.

---

## 📖 1. El Comando `/speckit.implement`

El comando `/speckit.implement` toma como insumos todos los artefactos creados en los pasos anteriores:
- La **Constitución** (`.specify/memory/constitution.md`)
- La **Especificación** (`spec.md`)
- El **Plan Técnico** (`plan.md`)
- La **Lista de Tareas** (`tasks.md`)

El agente de IA leerá `tasks.md` secuencialmente y ejecutará cada tarea de forma autónoma:
1. Escribirá o modificará los archivos indicados en la tarea.
2. Ejecutará comandos del sistema en la terminal local (compilación, pruebas unitarias, linter, etc.).
3. Marcará cada casilla en `tasks.md` de `[ ]` a `[x]` a medida que se completen exitosamente.

---

## 📖 2. Enfoque TDD (Test-Driven Development)

Si en el plan o la constitución se especificó escribir pruebas unitarias, Spec Kit aplicará el ciclo clásico de TDD:
1. **Red**: Escribe la prueba unitaria basada en el contrato/especificación y confirma que falla.
2. **Green**: Escribe el código de implementación mínimo necesario para que la prueba pase.
3. **Refactor**: Limpia el código manteniendo todas las pruebas en verde.

---

## 🛠️ 3. Ejercicio Práctico Paso a Paso

### Paso 1: Ejecutar la implementación autónoma

Inicia tu agente de IA en la terminal y ejecuta:

```text
/speckit.implement
```

Verás cómo la IA comienza a procesar tarea por tarea:
- Creará las carpetas y archivos del proyecto.
- Ejecutará comandos en tu máquina (ej. `npm install`, `node src/index.js`, etc.).
- Irá actualizando el estado de `tasks.md`.

---

### Paso 2: Monitorear el progreso y Checkpoints

Durante la ejecución, la IA se detendrá en los **Checkpoints** definidos en `tasks.md` para validar que el sistema funciona correctamente.

Si ocurre un error en la terminal o falla un test, la IA pausará la tarea actual, analizará los logs de error, corregirá el código y volverá a ejecutar el test hasta que se resuelva la falla.

---

### Paso 3: Probar la aplicación en vivo

Una vez que todas las casillas de `tasks.md` estén marcadas como completadas `[x]`, prueba la aplicación localmente:

1. Inicia el servidor de Taskify (ej. `node src/server.js` o `npm start`).
2. Abre tu navegador en `http://localhost:3000`.
3. Comprueba el funcionamiento:
   - Selecciona un usuario predefinido.
   - Revisa que las tareas asignadas a ti se destaquen con un color diferente.
   - Arrastra una tarjeta entre las columnas *To Do* e *In Progress*.
   - Agrega y edita un comentario.

---

## 📌 Resumen de Puntos Clave

- **`/speckit.implement`** ejecuta las tareas de `tasks.md` de forma metódica y autónoma.
- El agente interactúa con la terminal local para instalar dependencias y ejecutar tests.
- Se respetan los checkpoints de verificación para garantizar la calidad en cada etapa.
- Si surgen errores durante la implementación, el agente los diagnostica y corrige sin perder el contexto del proyecto.

---

➡️ **Siguiente lección**: [Módulo 6: Extensiones y Presets](./06-extensiones-y-presets.md)
