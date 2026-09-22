# Catálogo de Servicios y Fichas Técnicas Comerciales
**Reyes Computing S.A.S. — Soluciones Cloud, DevSecOps y Ciberseguridad**

---

## FICHA TÉCNICA 1: Auditoría Express de Seguridad y Repositorios
*Código de Servicio:* **SEC-AUDIT-01**  
*Modalidad:* Proyecto cerrado (Pago único) / Gancho comercial

### 1. Descripción del Servicio
Evaluación técnica perimetral y estática de código fuente, imágenes de contenedores Docker y configuraciones de nube para detectar fugas de secretos (claves API, contraseñas quemadas), paquetes desactualizados con vulnerabilidades conocidas (CVEs) y configuraciones inseguras.

### 2. Público Objetivo
* Startups de software, fintechs y agencias de desarrollo web.
* Directores de Tecnología (CTOs), Tech Leads y Founders que necesitan validar la seguridad antes de lanzar o presentar su plataforma a inversores y bancos.

### 3. Alcance Técnico
* **Escaneo de Secretos y Credenciales (Secret Scanning):**
  * Rastreo exhaustivo del historial de commits en Git mediante algoritmos de entropía para identificar tokens de AWS, Stripe, SendGrid, llaves SSH y credenciales de bases de datos expuestas.
* **Análisis de Vulnerabilidades en Dependencias (SCA):**
  * Detección de librerías de terceros (Node.js, Python, PHP, Go, etc.) afectadas por vulnerabilidades críticas o exploits públicos.
* **Escaneo de Contenedores Docker:**
  * Análisis de capas de imágenes Docker para identificar paquetes del sistema operativo base con riesgos de seguridad.
* **Auditoría de Cabeceras HTTP y SSL:**
  * Evaluación de calificaciones en SSL Labs (A/A+) y presencia de cabeceras de defensa (CSP, HSTS, X-Frame-Options).

### 4. Stack y Herramientas Utilizadas
* **Trivy (Aqua Security)** — Motor principal de escaneo de vulnerabilidades y secretos.
* **TruffleHog / GitGuardian CLI** — Análisis de historial y prevención de fugas de llaves.
* **SSL Labs & SecurityHeaders Engine** — Validación perimetral.

### 5. Entregables
1. **Informe Ejecutivo y Técnico (PDF):** Resumen de vulnerabilidades clasificadas por nivel de riesgo (Crítico, Alto, Medio, Bajo).
2. **Matriz de Remediación:** Guía técnica paso a paso para que el equipo de desarrollo del cliente aplique los parches necesarios.
3. **Llamada de Entrega (30 min):** Explicación guiada de los hallazgos con el líder técnico o fundador.

### 6. Tiempo de Entrega
* **24 a 48 horas hábiles** tras recibir el acceso de solo lectura al repositorio o imagen.

### 7. Estructura de Precios
* **Tarifa Internacional:** **\$250 USD** (Pago único).
* **Tarifa Colombia:** **\$1.000.000 COP** (Pago único).
* *Opción de Gancho Comercial:* Se ofrece con 100% de descuento (gratis) como diagnóstico preliminar a clientes calificados si contratan el servicio de implementación DevSecOps (SEC-CI-02).

---

## FICHA TÉCNICA 2: Pipeline DevSecOps & Automatización CI/CD
*Código de Servicio:* **DEV-CICD-02**  
*Modalidad:* Proyecto llave en mano (Pago único por implementación)

### 1. Descripción del Servicio
Diseño, construcción y despliegue de un flujo automatizado de integración y entrega continua (CI/CD) con pruebas de seguridad embebidas (*Shift-Left Security*), garantizando despliegues en minutos, sin caídas del servicio (*Zero-Downtime*) y sin intervención manual por SSH.

### 2. Público Objetivo
* Empresas y startups con aplicaciones en producción o en fase activa de desarrollo que sufren retrasos en lanzamientos, fallos imprevistos al desplegar o despliegues manuales propensos a error humano.

### 3. Alcance Técnico
* **Diseño del Pipeline (GitHub Actions / GitLab CI):**
  * Flujo estructurado: *Checkout -> Test -> Build Contenedor -> Escaneo de Seguridad -> Deploy Staging -> Deploy Producción*.
* **Seguridad Embebida en el Pipeline:**
  * Bloqueo automático del despliegue si se detectan credenciales quemadas o vulnerabilidades críticas (Trivy + TruffleHog).
* **Construcción y Optimización de Contenedores:**
  * Dockerfiles de múltiples etapas (*Multi-stage builds*) con imágenes mínimas y optimizadas (Alpine/Distroless).
* **Despliegue Cero-Caídas (Zero-Downtime):**
  * Estrategia de sustitución progresiva (*Rolling update* o *Blue/Green*) hacia AWS (ECS/EC2), Google Cloud o VPS con Docker/Swarm.
* **Notificaciones de Estado en Tiempo Real:**
  * Integración con Slack, Discord o Telegram para alertar al equipo de desarrollo sobre el resultado de cada despliegue.

### 4. Stack y Herramientas Utilizadas
* **GitHub Actions / GitLab CI** — Orquestador de flujos de trabajo.
* **Docker & Docker Compose** — Empaquetado y aislamiento de aplicaciones.
* **Portainer / AWS CLI / GCP Cloud SDK** — Homologación y control de despliegues.
* **Trivy** — Escáner automatizado dentro del pipeline.

### 5. Entregables
1. **Código Fuente del Pipeline:** Archivos `.github/workflows/*.yml` completamente documentados y versionados en el repositorio del cliente.
2. **Gestión de Secretos:** Configuración segura de variables de entorno y secretos en GitHub Secrets / AWS Secrets Manager.
3. **Manual de Operación y Buenas Prácticas:** Documentación técnica para desarrolladores sobre cómo operar las ramas y disparar despliegues.
4. **Sesión de Transferencia Técnica (2 horas):** Capacitación remota al equipo técnico del cliente.

### 6. Tiempo de Entrega
* **7 a 14 días laborables** (según complejidad de la arquitectura).

### 7. Estructura de Precios
* **Plan Sprint (1 Aplicación / Monolito o API):**
  * **\$1,500 USD** / **\$6.000.000 COP**
* **Plan Full DevSecOps (Múltiples microservicios / Staging + Prod):**
  * **\$2,800 USD** / **\$11.000.000 COP**
* *Tratamiento Tributario en Colombia:* Servicio técnico de desarrollo y computación en la nube **excluido de IVA (0%)** bajo el Art. 476, num. 21 del Estatuto Tributario.

---

## FICHA TÉCNICA 3: Plan de Monitoreo 24/7 y Continuidad Cloud
*Código de Servicio:* **OPS-MON-03**  
*Modalidad:* Suscripción mensual recurrente (MRR) / Sin cláusula de permanencia

### 1. Descripción del Servicio
Servicio gestionado de observabilidad, vigilancia de disponibilidad, respuesta ante caídas y mantenimiento preventivo de infraestructura cloud para garantizar que las aplicaciones y sitios web del cliente operen sin interrupciones.

### 2. Público Objetivo
* Startups, plataformas e-commerce y empresas financieras que no cuentan con un equipo de operaciones o SysAdmin interno y no pueden permitirse tiempos de inactividad.

### 3. Alcance Técnico
* **Monitoreo de Disponibilidad y Latencia 24/7:**
  * Pruebas de salud (*Healthchecks*) cada 60 segundos sobre endpoints HTTP(s), APIs y puertos TCP (bases de datos, SSH).
* **Vigilancia de Certificados SSL/TLS:**
  * Alertas preventivas a los 21, 14 y 7 días previos al vencimiento del certificado para evitar bloqueos del navegador.
* **Verificación de Respaldos (Push Heartbeats):**
  * Monitoreo automatizado de la ejecución de copias de seguridad: si el script de backup diario no confirma su finalización, se dispara una alerta técnica de inmediato.
* **Página de Estado Pública o Privada (Status Page):**
  * Portal web con la marca del cliente (o de Reyes Computing) que muestra el historial de uptime (99.9%) para inspirar confianza a sus usuarios finales.
* **Mantenimiento Preventivo Mensual:**
  * Aplicación periódica de parches de seguridad en servidores Linux y actualización de dependencias críticas del sistema.

### 4. Stack y Herramientas Utilizadas
* **Uptime Kuma** — Motor de observabilidad, métricas y páginas de estado.
* **Google Workspace SMTP / Telegram Bot API** — Canal de notificaciones y alertas críticas en tiempo real.
* **Portainer** — Panel de control para inspección de logs y reinicio preventivo de servicios.

### 5. Entregables
1. **Acceso al Portal de Estado (Status Page):** URL personalizada para consulta de disponibilidad del cliente.
2. **Canal de Alertas Inmediatas:** Configuración de grupo de Telegram o lista de distribución de correo para notificaciones de caída en menos de 60 segundos.
3. **Reporte Mensual de Rendimiento:** Resumen ejecutivo en PDF con porcentaje de uptime, tiempos promedio de respuesta e incidentes mitigados.
4. **Bolsa de Horas de Soporte:** Horas técnicas mensuales incluidas para ajustes de configuración, reinicio de servicios o consultoría.

### 6. Planes y Estructura de Precios (Suscripción Mensual)

| Característica / Plan | Plan Essential | Plan Pro *(Recomendado)* | Plan Enterprise |
| :--- | :---: | :---: | :---: |
| **Monitores activos (URLs / APIs)** | Hasta 5 monitores | Hasta 15 monitores | Hasta 40 monitores |
| **Frecuencia de chequeo** | Cada 60 segundos | Cada 60 segundos | Cada 30 segundos |
| **Página de estado con logo** | Sí (estándar) | Sí (personalizada) | Sí (dominio propio) |
| **Monitoreo de Backups (Heartbeat)** | 1 base de datos | Hasta 3 tareas | Ilimitado |
| **Bolsa de horas de soporte/mes** | 2 horas | 6 horas | 15 horas |
| **SLA de respuesta ante caídas** | Menor a 4 horas | Menor a 1 hora | Menor a 30 minutos |
| **PRECIO MENSUAL (USD)** | **\$350 USD / mes** | **\$650 USD / mes** | **\$1,400 USD / mes** |
| **PRECIO MENSUAL (COP)** | **\$1.400.000 COP** | **\$2.600.000 COP** | **\$5.600.000 COP** |

---

## 4. Política Comercial y Condiciones Generales

1. **Condiciones de Pago:**
   * Servicios puntuales (Auditoría y CI/CD): 50% anticipo al inicio y 50% contra entrega a satisfacción.
   * Servicios recurrentes (Monitoreo): Facturación mes anticipado los primeros 5 días de cada mes.
2. **Exclusión de IVA (Beneficio Tributario):**
   * En virtud del **Artículo 476, numeral 21 del Estatuto Tributario**, los servicios de computación en la nube, servidores y plataformas de infraestructura tecnológica facturados por Reyes Computing S.A.S. están **excluidos del impuesto sobre las ventas (IVA 0%)**.
3. **Confidencialidad:**
   * Toda intervención técnica se realiza bajo la firma previa de un **Acuerdo de Confidencialidad (NDA)** bilateral que protege el código fuente, bases de datos y secretos comerciales del cliente.
