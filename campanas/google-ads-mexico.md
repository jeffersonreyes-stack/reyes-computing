# Google Ads — Servicios en México (Campañas 1 y 2)

Instrucciones paso a paso para montar dos campañas de Búsqueda dirigidas a México. Los textos están listos para pegar; los campos marcados **[DEFINIR POR EL DUEÑO]** no deben llenarse con datos inventados.

> **Prerrequisito:** las landings deben estar publicadas y responder con HTTP 200 antes de activar cualquier anuncio:
> - https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html (campaña 1)
> - https://www.reyescomputing.com/mexico-nube-seguridad-web.html (campaña 2)
>
> Revisa que el contenido de cada landing coincida con lo que dicen los anuncios (servicios, atención remota, sin precios inventados). Si la landing cambia, ajusta los textos.

Cuenta de Google Ads: cliente 552-938-8450. ID de conversión de la etiqueta del sitio: `AW-18025178697` (ver `assets/js/reyes-conversion.js`).

## Reglas de copy aplicadas (revisar antes de pegar)

- Sin garantías, sin superlativos no verificables, sin «#1» ni «el mejor», sin promesas de resultados, sin precios ni descuentos (el sitio no tiene precios aprobados; ver `tests/conversion.test.js`).
- Español de México (es-MX): «celular», «cotización», «tú».
- **Transparencia geográfica:** Reyes Computing es una empresa colombiana. No hay oficina en México; la atención es **remota** (videollamada y WhatsApp). Ningún anuncio sugiere sede física en México.
- La pauta en Google Ads se paga directamente a Google; los honorarios y el alcance se definen en la cotización.
- Fintech (campaña 2): no se afirma cumplimiento normativo, certificaciones ni auditorías formales. No uses «PCI DSS», «CNBV», «ISO 27001» ni similares como afirmación en titulares o descripciones.
- No uses marcas de terceros (AWS, Google Cloud, Azure) en el texto de los anuncios; solo como palabras clave si lo decides.
- Evita mayúsculas excesivas, signos repetidos y puntuación fuera de lo normal (política de Google Ads).
- Fijar titulares (pin): no fijes ninguno; deja que Google rote. Si el dueño quiere fijar, fija solo la marca en la posición 3.

## Configuración común (campañas 1 y 2)

| Ajuste | Valor |
|---|---|
| Tipo de campaña | **Búsqueda** |
| Objetivo de la campaña | **Clientes potenciales** (contactos por WhatsApp y formulario) |
| Redes | Solo Red de Búsqueda de Google. **Desmarca** «Red de Display» y, al inicio, también «Socios de búsqueda» |
| Ubicaciones | México: **Ciudad de México**, **Guadalajara** (Jalisco), **Monterrey** (Nuevo León). Ciudades a confirmar por el dueño |
| Opción de ubicación | «Presencia: personas que están en tus ubicaciones objetivo» (no «Presencia o interés») |
| Idioma | Español |
| Dispositivos | Todos al inicio; revisar por dispositivo a los 14 días |
| Audiencias | Solo «Observación» si se agregan; sin segmentación restringida |
| Rotación de anuncios | Optimizar (preferir los de mejor rendimiento) |
| Fechas | Inicio: el día que se active; sin fecha de fin |
| Horario de anuncios | **[DEFINIR POR EL DUEÑO]**: días y horas en que se puede responder por WhatsApp. La programación usa la **zona horaria de la cuenta** (confirmar cuál es; Colombia es UTC‑5 y el centro de México es UTC‑6 todo el año, 1 hora menos). Sugerencia: empezar con los horarios de atención reales y ampliar según datos |
| Presupuesto diario | **[DEFINIR POR EL DUEÑO]** (por campaña) |
| Estrategia de puja inicial | **Maximizar clics** con **CPC máximo [DEFINIR POR EL DUEÑO]**. Pasar a **Maximizar conversiones** cuando haya **N = [DEFINIR] conversiones** registradas de forma confiable (Google suele necesitar un volumen de conversiones recientes para que la puja automática funcione bien; revisa el estado de aprendizaje). No fijar CPA objetivo hasta tener datos reales |
| Nombres sugeridos | «MX - Búsqueda - Desarrollo web y marketing» y «MX - Búsqueda - Nube y seguridad web» |

### Medición de conversiones (antes de lanzar)

El sitio ya mide, con `assets/js/reyes-conversion.js`:

| Señal | Qué mide realmente | Uso en Google Ads |
|---|---|---|
| Acción existente «Clic WhatsApp» (etiqueta ya cargada en `ADS_ETIQUETA_CONVERSION`) | **Clics** en botones de WhatsApp, **no** conversaciones ni ventas | Conversión secundaria (o principal solo en la fase inicial); no equivale a un lead confirmado |
| Evento `formulario_intento` | El visitante envió el formulario válido; **no confirma recepción** | No tiene acción de conversión en Google Ads todavía |
| Evento `contacto_iniciado` (`metodo`: `whatsapp` o `llamada`) | Evento de análisis; las llamadas son un evento separado | No reutilizar la etiqueta de WhatsApp para llamadas o formularios |
| `success.html` (página de agradecimiento tras FormSubmit) | Carga tras el envío del formulario; ya tiene la etiqueta global y un comentario `ETIQUETA_FORMULARIO` | Mejor señal de formulario enviado |

**Recomendación (no inventes la etiqueta):**

1. En Google Ads: **Objetivos → Conversiones → Resumen → Nueva acción de conversión → Sitio web**. Crea una acción **propia para formularios** (por ejemplo, «Formulario enviado», categoría «Enviar formulario de clientes potenciales»). Usa la etiqueta que Google te entregue; **no** copies la del WhatsApp.
2. Quien mantenga el sitio debe pegar esa etiqueta en `success.html` (hay un comentario con el marcador `ETIQUETA_FORMULARIO`) en un PR aparte, y confirmar que cada landing de campaña envía el formulario con redirección a `success.html`.
3. Verifica con **Tag Assistant** que la conversión se dispara una sola vez al cargar `success.html`, y con una prueba real que el correo llega a `control@reyescomputing.com` (el dueño debe tener activado FormSubmit para esa cuenta).
4. Marca como **Principales** solo las acciones que quieras optimizar. Mientras «Clic WhatsApp» sea clic y no conversación, decide con el dueño si queda como principal o secundaria, y contrasta los chats reales con los clics.
5. Si algún día se publica un número telefónico con enlaces `tel:`, crea una acción de llamada propia; hoy el sitio no publica enlaces `tel:`.

> Pendiente legal: el aviso de datos está en `contacto.html#privacidad`, pero no configura consentimiento de cookies. Confirma con el dueño si hace falta antes de escalar el gasto en México.

### Extensiones (activos) comunes

- **Llamada:** no activar. El sitio no publica un teléfono de atención; el único número es el WhatsApp comercial de Colombia (+57). Si el dueño habilita un número con atención remota para México, evalúalo después.
- **Fragmentos estructurados:** encabezado «Servicios».
- **Formulario de clientes potenciales / mensajes:** no activar al inicio; el flujo es WhatsApp y formulario del sitio.
- **Imágenes:** opcional; solo con imágenes propias, sin promesas ni precios.

---

# Campaña 1 — Servicios en México: Agencia de desarrollo web y marketing digital

| Campo | Valor |
|---|---|
| Landing | https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html |
| `utm_campaign` | `mx-desarrollo-web-marketing` |
| Objetivo | Contactos (WhatsApp y formulario) de empresas en México que buscan sitio web y/o publicidad digital con atención remota |
| Presupuesto diario | **[DEFINIR POR EL DUEÑO]** |
| CPC máximo inicial | **[DEFINIR POR EL DUEÑO]** |
| N conversiones para pasar a Maximizar conversiones | **[DEFINIR]** |

## Pasos en Google Ads

1. **Campañas → + Nueva campaña** → objetivo **Clientes potenciales** → tipo **Búsqueda**.
2. Objetivos de conversión de la campaña: marca WhatsApp y formulario (ver «Medición»).
3. Nombre de campaña, puja y presupuesto según la tabla de configuración común (valores [DEFINIR]).
4. Redes, ubicaciones (CDMX, Guadalajara, Monterrey), opción «Presencia», idioma español.
5. Crea los **grupos de anuncios** de la sección siguiente y pega sus palabras clave.
6. En **cada grupo de anuncios** pega los **3 anuncios** de abajo (son los mismos 3 textos; no crees variantes adicionales).
7. Agrega las **palabras clave negativas** a nivel de campaña y las **extensiones** (activos).
8. Revisa en «Vista previa de anuncios» y envía a revisión. Estado esperado: «Aprobado» o «Aprobado (limitado)»; corrige cualquier rechazo por política en lugar de apelar sin cambios.

## Grupos de anuncios y palabras clave

URL final de todos los grupos: la landing de la campaña (con el UTM del anuncio correspondiente).

**Grupo 1A — Desarrollo web (empresas)**

| Palabra clave | Concordancia |
|---|---|
| "desarrollo web méxico" | Frase |
| "agencia de desarrollo web" | Frase |
| [agencia de desarrollo web] | Exacta |
| "desarrollo de sitios web a la medida" | Frase |
| "crear página web para empresa" | Frase |
| [página web para empresa] | Exacta |
| "diseño de páginas web para negocios" | Frase |
| [diseño de páginas web] | Exacta |
| "landing page profesional" | Frase |
| "desarrollo web cdmx" | Frase |
| "desarrollo web guadalajara" | Frase |
| "desarrollo web monterrey" | Frase |

**Grupo 1B — Marketing digital y publicidad**

| Palabra clave | Concordancia |
|---|---|
| "agencia de marketing digital" | Frase |
| [agencia de marketing digital] | Exacta |
| "marketing digital para pymes" | Frase |
| "publicidad en google ads" | Frase |
| [agencia de google ads] | Exacta |
| "campañas de google ads para empresas" | Frase |
| "publicidad en redes sociales para empresas" | Frase |
| "agencia de marketing digital cdmx" | Frase |
| "agencia de marketing digital guadalajara" | Frase |
| "agencia de marketing digital monterrey" | Frase |

Empieza con estos dos grupos. Evita concordancia amplia hasta tener datos de términos de búsqueda.

## Palabras clave negativas (nivel campaña)

Cárgalas en concordancia de frase; todas filtran búsquedas que no son clientes.

`gratis`, `gratuito`, `gratuita`, `curso`, `cursos`, `tutorial`, `como hacer`, `cómo hacer`, `plantilla`, `plantillas`, `template`, `descargar`, `pdf`, `código fuente`, `github`, `empleo`, `empleos`, `trabajo`, `vacante`, `vacantes`, `sueldo`, `salario`, `prácticas`, `pasante`, `universidad`, `carrera`, `diplomado`, `wix gratis`, `wordpress gratis`, `hazlo tu mismo`, `app gratis`, `crear página web gratis`

Revisa el informe de **términos de búsqueda** a los 7 días y agrega más (por ejemplo, términos de estudiantes o de personas que buscan trabajo en agencias).

## Anuncios (3 RSA)

Límites: titulares ≤ 30 caracteres, descripciones ≤ 90, rutas ≤ 15. Los conteos de la columna «Car.» fueron calculados con un script.

### Anuncio 1 — Beneficio (un solo equipo para web y marketing)

URL final: `https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-desarrollo-web-marketing&utm_content=anuncio-1`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | desarrollo-web | 14 |
| R2 | mexico | 6 |

| # | Titular | Car. |
|---|---|---|
| H1 | Desarrollo Web para México | 26 |
| H2 | Sitios Web a tu Medida | 22 |
| H3 | Agencia de Marketing Digital | 28 |
| H4 | Web y Marketing en un Equipo | 28 |
| H5 | Reyes Computing Colombia | 24 |
| H6 | Atención Remota en México | 25 |
| H7 | Páginas Web Profesionales | 25 |
| H8 | Publicidad en Google y Redes | 28 |
| H9 | Tu Negocio Visible en Google | 28 |
| H10 | Sitios Adaptados al Celular | 27 |
| H11 | Estrategia Digital con Plan | 27 |
| H12 | Cotiza por WhatsApp | 19 |
| H13 | Equipo Colombiano, en Remoto | 28 |
| H14 | Sitio Web y Campañas | 20 |
| H15 | Habla con Reyes Computing | 25 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Creamos tu sitio web y tu plan de marketing digital con un solo equipo de trabajo. | 82 |
| D2 | Empresa colombiana con atención remota para negocios en CDMX, Guadalajara y Monterrey. | 86 |
| D3 | Sitios adaptados al celular con botones de contacto por WhatsApp y formulario. | 78 |
| D4 | Cuéntanos de tu negocio y recibe una propuesta a tu medida. Atención 100% remota. | 81 |

### Anuncio 2 — Dolor (web que no genera contactos)

URL final: `https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-desarrollo-web-marketing&utm_content=anuncio-2`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | revisa-tu-web | 13 |
| R2 | marketing | 9 |

| # | Titular | Car. |
|---|---|---|
| H1 | ¿Tu Web No Genera Contactos? | 28 |
| H2 | ¿Poca Visibilidad en Google? | 28 |
| H3 | ¿Tu Sitio Está Desactualizado? | 30 |
| H4 | Evita Perder Contactos | 22 |
| H5 | Ordena tu Presencia Digital | 27 |
| H6 | Web Clara, Contacto Directo | 27 |
| H7 | Campañas con Plan y Reporte | 27 |
| H8 | Revisamos tu Sitio Web | 22 |
| H9 | Marketing sin Adivinar | 22 |
| H10 | Revisión de tu Presencia Web | 28 |
| H11 | Atención Remota a México | 24 |
| H12 | Web y Anuncios Coordinados | 26 |
| H13 | Medición de Contactos Web | 25 |
| H14 | Mejora tu Web Paso a Paso | 25 |
| H15 | Escríbenos por WhatsApp | 23 |

| # | Descripción | Car. |
|---|---|---|
| D1 | ¿Tu sitio no te trae contactos? Revisamos tu web y tus anuncios y proponemos mejoras. | 85 |
| D2 | Medimos los contactos por WhatsApp y formulario para saber qué canal te funciona. | 81 |
| D3 | Sin oficina en México: trabajamos en remoto, con reuniones por videollamada. | 76 |
| D4 | La pauta se paga directo a Google Ads. Alcance y honorarios van en la cotización. | 81 |

### Anuncio 3 — Prueba, claridad y llamada a la acción

URL final: `https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-desarrollo-web-marketing&utm_content=anuncio-3`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | cotiza | 6 |
| R2 | agencia-digital | 15 |

| # | Titular | Car. |
|---|---|---|
| H1 | Solicita tu Cotización Web | 26 |
| H2 | Cotiza tu Proyecto Digital | 26 |
| H3 | Agenda una Videollamada | 23 |
| H4 | Escríbenos por WhatsApp | 23 |
| H5 | Cuéntanos tu Proyecto | 21 |
| H6 | Desarrollo Web y Marketing | 26 |
| H7 | Agencia Digital Colombiana | 26 |
| H8 | Atendemos México en Remoto | 26 |
| H9 | Propuesta Según tu Negocio | 26 |
| H10 | Primer Contacto por WhatsApp | 28 |
| H11 | Conoce Nuestros Servicios | 25 |
| H12 | Sitios Web para Empresas | 24 |
| H13 | Marketing Digital en Remoto | 27 |
| H14 | Equipo Remoto desde Colombia | 28 |
| H15 | Resuelve tus Dudas por Chat | 27 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Solicita tu cotización de desarrollo web o marketing digital. Te respondemos por WhatsApp. | 90 |
| D2 | Agencia colombiana con atención remota a México. No tenemos oficina en México. | 78 |
| D3 | Elige lo que necesitas: sitio web, publicidad en Google o publicidad en redes sociales. | 87 |
| D4 | Escríbenos, cuéntanos tu proyecto y te orientamos sobre los siguientes pasos. | 77 |

> Si el dueño aprueba una oferta concreta en `ofertas.html`, puede sustituir un titular o descripción del anuncio 3 por el texto exacto de la oferta, con sus condiciones reales. No inventes precios ni descuentos.

## Extensiones (activos) — Campaña 1

**Vínculos de sitio (sitelinks)** — título ≤ 25, líneas ≤ 35. Las URL de `ofertas.html` y `contacto.html` dependen de que estén publicadas.

| # | Título | Línea 1 | Línea 2 | URL final | Car. T/L1/L2 |
|---|---|---|---|---|---|
| SL1 | Cómo funciona | Atención remota paso a paso | Del contacto a la propuesta | https://www.reyescomputing.com/como-funciona.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-desarrollo-web-marketing&utm_content=sitelink-como-funciona | 13/27/27 |
| SL2 | Casos de éxito | Conoce proyectos de Reyes | Revisa ejemplos publicados | https://www.reyescomputing.com/casos-de-exito.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-desarrollo-web-marketing&utm_content=sitelink-casos | 14/25/26 |
| SL3 | Ofertas | Revisa las ofertas vigentes | Condiciones en la página | https://www.reyescomputing.com/ofertas.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-desarrollo-web-marketing&utm_content=sitelink-ofertas | 7/27/24 |
| SL4 | Contacto | Escríbenos por WhatsApp | O usa el formulario | https://www.reyescomputing.com/contacto.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-desarrollo-web-marketing&utm_content=sitelink-contacto | 8/23/19 |

**Textos destacados (callouts)** — ≤ 25 caracteres.

| # | Texto | Car. |
|---|---|---|
| C1 | Atención remota a México | 24 |
| C2 | Cotización por WhatsApp | 23 |
| C3 | Equipo colombiano | 17 |
| C4 | Sitios para celular | 19 |
| C5 | Contacto por videollamada | 25 |

**Fragmentos estructurados** — encabezado «Servicios», valores ≤ 25 caracteres.

| # | Valor | Car. |
|---|---|---|
| S1 | Desarrollo web | 14 |
| S2 | Landing pages | 13 |
| S3 | Publicidad en Google | 20 |
| S4 | Publicidad en redes | 19 |

**Llamada:** no activar (ver configuración común).

## Checklist de lanzamiento — Campaña 1

- [ ] Landing publicada, carga bien en celular y con HTTPS.
- [ ] El botón de WhatsApp y el formulario funcionan desde la landing; el formulario llega a `control@reyescomputing.com` y redirige a `success.html`.
- [ ] Acción de conversión del formulario creada y etiqueta instalada (si no, lanzar solo midiendo WhatsApp y dejar claro que el formulario no se está contando como conversión).
- [ ] Tag Assistant confirma que se dispara «Clic WhatsApp» en la landing y `formulario_intento` al enviar.
- [ ] Presupuesto, CPC máximo, horario y ciudades **confirmados por el dueño**.
- [ ] 3 anuncios cargados en cada grupo; ninguno excede los límites.
- [ ] Negativas y extensiones cargadas.
- [ ] Facturación y método de pago de Google Ads activos.
- [ ] Alguien responde WhatsApp dentro del horario configurado.
- [ ] Revisión de políticas: sin garantías, superlativos ni precios.

## Qué revisar — Campaña 1

**A los 7 días**
- Aprobación de anuncios y estado de política.
- **Términos de búsqueda:** agregar negativas, pasar términos buenos a exacta/frase.
- Impresiones, CTR, CPC medio frente al máximo definido; cuota de impresiones perdida por presupuesto/ranking.
- Conversiones: clics en WhatsApp vs. chats reales recibidos; formularios (`success.html`) vs. correos recibidos.
- Que no entren clics de fuera de CDMX/Guadalajara/Monterrey (informe de ubicaciones).
- No cambiar la puja ni pausar anuncios antes de tener datos suficientes (salvo problemas de política).

**A los 14 días**
- Rendimiento de los 3 anuncios por «calificación de activos» y por conversiones, no solo por CTR.
- Informes por ciudad, dispositivo, día y hora; ajustar el horario real.
- Calidad de los contactos: ¿cumplen el perfil? Registrar en una hoja (fuente = UTM).
- Revisar los UTM en las herramientas de analítica o registros del sitio (`utm_content=anuncio-1|2|3`).
- Probar nuevos titulares sustituyendo los de peor rendimiento.

**A los 30 días**
- Decidir si hay N conversiones fiables para pasar a **Maximizar conversiones** o seguir con Maximizar clics con CPC máximo.
- Decidir con el dueño si se amplía a otras ciudades o se recorta alguna.
- Revisión de presupuesto con costos reales por contacto calculados por el dueño con sus datos; este documento no fija CPA ni ROI.
- Revisar la landing con las preguntas reales que llegaron por WhatsApp.

---

# Campaña 2 — Servicios en México: Computación en la nube y seguridad web (con contexto fintech)

| Campo | Valor |
|---|---|
| Landing | https://www.reyescomputing.com/mexico-nube-seguridad-web.html |
| `utm_campaign` | `mx-nube-seguridad-web` |
| Objetivo | Contactos (WhatsApp y formulario) de empresas y fintechs en México que buscan apoyo en nube y seguridad web, con atención remota |
| Presupuesto diario | **[DEFINIR POR EL DUEÑO]** |
| CPC máximo inicial | **[DEFINIR POR EL DUEÑO]** |
| N conversiones para pasar a Maximizar conversiones | **[DEFINIR]** |

**Notas de política para esta campaña**

- No ofrecemos productos financieros: ofrecemos servicios de TI a empresas, incluidas fintechs. Aun así, si Google solicita **verificación del anunciante** o marca «servicios financieros», sigue las instrucciones de la cuenta y confirma con el dueño.
- No uses «cumplimiento», «certificado», «auditoría certificada», «protegido al 100 %» ni nombres de normas como afirmación.
- Mantén lenguaje de apoyo: «revisión», «configuración», «buenas prácticas», «orientación».
- Público: responsables de TI, CTO y fundadores. Es una campaña de menor volumen; valida primero la relevancia de los términos.

## Pasos en Google Ads

Igual que la campaña 1 (misma configuración común), cambiando nombre, landing, UTM, grupos de anuncios, palabras clave y activos.

## Grupos de anuncios y palabras clave

**Grupo 2A — Computación en la nube**

| Palabra clave | Concordancia |
|---|---|
| "servicios de computación en la nube" | Frase |
| [servicios de computación en la nube] | Exacta |
| "migración a la nube" | Frase |
| [migración a la nube para empresas] | Exacta |
| "consultoría cloud" | Frase |
| "infraestructura en la nube para startups" | Frase |
| "optimización de costos en la nube" | Frase |
| "monitoreo de servidores" | Frase |
| "devsecops" | Frase |
| "consultoría en la nube méxico" | Frase |

**Grupo 2B — Seguridad web y fintech**

| Palabra clave | Concordancia |
|---|---|
| "seguridad web para empresas" | Frase |
| [seguridad web para empresas] | Exacta |
| "protección de sitio web" | Frase |
| "firewall de aplicaciones web" | Frase |
| [waf para sitio web] | Exacta |
| "revisión de seguridad web" | Frase |
| "seguridad web para fintech" | Frase |
| [ciberseguridad para fintech] | Exacta |
| "seguridad en la nube para fintech méxico" | Frase |
| "seguridad para startups fintech" | Frase |

## Palabras clave negativas (nivel campaña)

`gratis`, `gratuito`, `curso`, `cursos`, `certificación`, `certificacion`, `certificado`, `examen`, `tutorial`, `que es`, `qué es`, `definición`, `pdf`, `descargar`, `antivirus`, `vpn`, `hackear`, `hackeo`, `hacker`, `contraseña`, `recuperar cuenta`, `cuenta hackeada`, `crack`, `empleo`, `trabajo`, `vacante`, `sueldo`, `salario`, `universidad`, `maestría`, `diplomado`, `prácticas`, `github`, `código fuente`

Nota: no agregues «pci dss» ni términos de normativa financiera como palabra clave objetivo; podrían atraer búsquedas que esperan un anuncio que prometa cumplimiento. Si el dueño quiere atenderlas, definir primero el texto permitido.

## Anuncios (3 RSA)

### Anuncio 1 — Beneficio (nube y seguridad con atención remota)

URL final: `https://www.reyescomputing.com/mexico-nube-seguridad-web.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-nube-seguridad-web&utm_content=anuncio-1`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | nube-seguridad | 14 |
| R2 | mexico | 6 |

| # | Titular | Car. |
|---|---|---|
| H1 | Computación en la Nube | 22 |
| H2 | Seguridad Web para Empresas | 27 |
| H3 | Migración a la Nube | 19 |
| H4 | Nube y Seguridad Web | 20 |
| H5 | Reyes Computing Colombia | 24 |
| H6 | Atención Remota en México | 25 |
| H7 | Protección de Sitios Web | 24 |
| H8 | WAF y HTTPS para tu Sitio | 25 |
| H9 | Costos de Nube Más Claros | 25 |
| H10 | Monitoreo de tu Servidor | 24 |
| H11 | Equipo Cloud desde Colombia | 27 |
| H12 | Seguridad Web para Fintech | 26 |
| H13 | Buenas Prácticas en la Nube | 27 |
| H14 | Cotiza por WhatsApp | 19 |
| H15 | Consultoría Cloud en Remoto | 27 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Te ayudamos con tu infraestructura en la nube y con la seguridad de tu sitio web. | 81 |
| D2 | Empresa colombiana con atención remota para equipos en CDMX, Guadalajara y Monterrey. | 85 |
| D3 | Configuración de WAF, HTTPS, respaldos y monitoreo según lo que tu proyecto necesite. | 85 |
| D4 | Cuéntanos tu caso por WhatsApp y recibe una propuesta. Atención 100% remota. | 76 |

### Anuncio 2 — Dolor (costos, caídas, riesgos) y contexto fintech

URL final: `https://www.reyescomputing.com/mexico-nube-seguridad-web.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-nube-seguridad-web&utm_content=anuncio-2`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | seguridad-web | 13 |
| R2 | fintech | 7 |

| # | Titular | Car. |
|---|---|---|
| H1 | ¿Sube tu Factura de Nube? | 25 |
| H2 | ¿Caídas en tu Servidor? | 23 |
| H3 | ¿Tu Sitio Sin Protección? | 25 |
| H4 | Revisión de Seguridad Web | 25 |
| H5 | Revisa los Riesgos de tu Web | 28 |
| H6 | Orden en tu Nube y Costos | 25 |
| H7 | Seguridad Web para Fintech | 26 |
| H8 | Nube para Startups Fintech | 26 |
| H9 | Configura WAF y HTTPS | 21 |
| H10 | Respaldos y Continuidad | 23 |
| H11 | Atención Remota a México | 24 |
| H12 | Apoyo en Buenas Prácticas | 25 |
| H13 | Menos Improvisación en TI | 25 |
| H14 | Escríbenos por WhatsApp | 23 |
| H15 | Habla con un Especialista | 25 |

| # | Descripción | Car. |
|---|---|---|
| D1 | ¿Tu factura de nube crece o tu servidor se cae? Revisamos tu caso y proponemos mejoras. | 87 |
| D2 | Para fintech en México: revisión de controles web y nube. No es una auditoría formal. | 85 |
| D3 | Sin oficina en México: trabajamos en remoto, con reuniones por videollamada. | 76 |
| D4 | Los costos de nube se pagan al proveedor. Nuestros honorarios van en la cotización. | 83 |

### Anuncio 3 — Prueba, claridad y llamada a la acción

URL final: `https://www.reyescomputing.com/mexico-nube-seguridad-web.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-nube-seguridad-web&utm_content=anuncio-3`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | cotiza | 6 |
| R2 | cloud | 5 |

| # | Titular | Car. |
|---|---|---|
| H1 | Solicita una Revisión Cloud | 27 |
| H2 | Cotiza Nube y Seguridad | 23 |
| H3 | Agenda una Videollamada | 23 |
| H4 | Escríbenos por WhatsApp | 23 |
| H5 | Cuéntanos tu Infraestructura | 28 |
| H6 | Plan de Nube a tu Medida | 24 |
| H7 | Consultoría Cloud Colombiana | 28 |
| H8 | Atendemos México en Remoto | 26 |
| H9 | Propuesta Según tu Proyecto | 27 |
| H10 | Conoce Nuestros Servicios | 25 |
| H11 | Seguridad Web con Orientación | 29 |
| H12 | Soporte para Equipos de TI | 26 |
| H13 | Primer Contacto por WhatsApp | 28 |
| H14 | Equipo Remoto desde Colombia | 28 |
| H15 | Resuelve tus Dudas por Chat | 27 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Solicita una revisión de tu nube y seguridad web. Te respondemos por WhatsApp. | 78 |
| D2 | Consultoría colombiana con atención remota a México. No tenemos oficina en México. | 82 |
| D3 | Cuéntanos qué infraestructura usas y qué te preocupa; te proponemos un plan de trabajo. | 87 |
| D4 | Servicios para empresas y fintechs: nube, monitoreo, WAF y seguridad web. | 73 |

## Extensiones (activos) — Campaña 2

**Vínculos de sitio (sitelinks)**

| # | Título | Línea 1 | Línea 2 | URL final | Car. T/L1/L2 |
|---|---|---|---|---|---|
| SL1 | Cómo funciona | Atención remota paso a paso | Del contacto a la propuesta | https://www.reyescomputing.com/como-funciona.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-nube-seguridad-web&utm_content=sitelink-como-funciona | 13/27/27 |
| SL2 | Seguridad fintech | Revisión de controles web | Sin promesas de certificación | https://www.reyescomputing.com/ciberseguridad-fintech.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-nube-seguridad-web&utm_content=sitelink-fintech | 17/25/29 |
| SL3 | Ofertas | Revisa las ofertas vigentes | Condiciones en la página | https://www.reyescomputing.com/ofertas.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-nube-seguridad-web&utm_content=sitelink-ofertas | 7/27/24 |
| SL4 | Contacto | Escríbenos por WhatsApp | O usa el formulario | https://www.reyescomputing.com/contacto.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-nube-seguridad-web&utm_content=sitelink-contacto | 8/23/19 |

> `ciberseguridad-fintech.html` es una página existente del sitio. Revísala antes de usarla como sitelink en México: si su contenido menciona normas o resultados que no quieres vincular a este anuncio, reemplázala por `mexico-desarrollo-web-marketing-digital.html`.

**Textos destacados (callouts)**

| # | Texto | Car. |
|---|---|---|
| C1 | Atención remota a México | 24 |
| C2 | Cotización por WhatsApp | 23 |
| C3 | Equipo colombiano | 17 |
| C4 | Nube, WAF y monitoreo | 21 |
| C5 | Contacto por videollamada | 25 |

**Fragmentos estructurados** — encabezado «Servicios».

| # | Valor | Car. |
|---|---|---|
| S1 | Computación en la nube | 22 |
| S2 | Seguridad web | 13 |
| S3 | Monitoreo de servidores | 23 |
| S4 | Optimización de costos | 22 |

## Checklist de lanzamiento — Campaña 2

- [ ] Landing `mexico-nube-seguridad-web.html` publicada, con aclaración de atención remota y sin afirmaciones de cumplimiento o certificación.
- [ ] Mismos puntos de medición que la campaña 1 (WhatsApp, formulario → `success.html`, correo recibido).
- [ ] Ciudades, presupuesto, CPC máximo y horario **confirmados por el dueño**.
- [ ] 3 anuncios en cada grupo, dentro de los límites.
- [ ] Negativas de empleo, cursos, certificaciones y seguridad personal cargadas.
- [ ] Verificar si Google pide verificación del anunciante o aplica política de servicios financieros.
- [ ] Las páginas de sitelink existen y no contradicen los anuncios.
- [ ] Alguien puede atender consultas técnicas en español dentro del horario.

## Qué revisar — Campaña 2

**A los 7 días**
- Estado de aprobación (política de servicios financieros y de afirmaciones).
- Términos de búsqueda: muchas búsquedas de seguridad son de usuarios finales (antivirus, VPN, cuentas hackeadas); agrega negativas.
- Volumen: si hay pocas impresiones, revisa si algún estado indica poco volumen de búsqueda y amplía con frase antes de usar amplia.
- Clics y contactos vs. mensajes reales.

**A los 14 días**
- Rendimiento por grupo (2A vs. 2B) y por los 3 anuncios.
- Calidad de los contactos (¿decisores? ¿pymes o fintechs?).
- Ubicaciones, horario y dispositivos; en B2B suele concentrarse en días y horas hábiles.
- Reemplazar titulares de menor rendimiento.

**A los 30 días**
- Decidir si hay N conversiones fiables para pasar a **Maximizar conversiones**.
- Decidir si se agrupan o se pausan palabras clave con gasto sin contactos.
- Evaluar con el dueño si la campaña justifica su presupuesto con costos reales; este documento no establece CPA ni ROI.
- Revisar la landing con las dudas reales de los contactos.

---

## Notas finales

- Estos textos y reglas no confirman lo que hay activo en Google Ads. Verifica el estado real en la cuenta antes de duplicar o pausar campañas existentes.
- Ver también `campanas/README.md` y `google_ads_campaign_urls.md`.
