# REGLAS MANDATORIAS DE DESARROLLO Y FLUJO GIT (REYES COMPUTING)

## ⚠️ REGLA DE ORO DE DESARROLLO (NON-NEGOTIABLE)

1. **PROHIBIDO EL PUSH DIRECTO A `main`:**
   - Queda estrictamente prohibido ejecutar `git push origin main` o modificar `main` directamente.

2. **FLUJO OBLIGATORIO DE PULL REQUEST:**
   - Todo cambio, corrección o nueva característica DEBE realizarse en una rama dedicada (`feature/<nombre-feature>`).
   - Todos los cambios deben commitearse en la rama de característica.
   - El agente DEBE ejecutar la API de GitHub (`open_pull_request.py`) para **CREAR Y ABRIR UN PULL REQUEST OFICIAL** en GitHub.
   - El agente DEBE proporcionar al usuario el número de PR abierto (#PR) y la URL para su revisión antes de cualquier fusión.

3. **VERIFICACIÓN Y CALIDAD (QUALITY GATE):**
   - Antes de abrir el PR, se debe ejecutar la suite de pruebas `python3 test_services_suite.py` y validar que el resultado sea 100% exitoso (20/20 verificaciones aprobadas).
