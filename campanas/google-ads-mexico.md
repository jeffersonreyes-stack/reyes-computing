# Google Ads — Servicios en México (3 anuncios en total)

Instrucciones paso a paso para montar **una campaña de Búsqueda para México** con **3 grupos de anuncios** (uno por servicio) y **exactamente 3 anuncios RSA en total** (uno por grupo, cada uno con su landing). Los textos están listos para pegar; los campos marcados **[DEFINIR POR EL DUEÑO]** no deben llenarse con datos inventados.

| Anuncio | Servicio | Grupo de anuncios | Landing |
|---|---|---|---|
| 1 | Agencia de desarrollo web y marketing digital | Grupo A | https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html |
| 2 | Computación en la nube y seguridad web (contexto fintech) | Grupo B | https://www.reyescomputing.com/mexico-nube-seguridad-web.html |
| 3 | Tiendas online para México | Grupo C | https://www.reyescomputing.com/mexico-tiendas-online.html |

La campaña de Tiendas Online para Colombia (`tiendas-online.html`) es independiente y está en `google-ads-tiendas-online.md`; no se repite aquí.

> **Prerrequisito:** las 3 landings mexicanas deben estar publicadas y responder con HTTP 200 antes de activar la campaña. Revisa que el contenido de cada una coincida con su anuncio (servicios, atención remota, sin precios inventados). Si la landing cambia, ajusta los textos. Si alguna landing no está lista, deja **pausado** su grupo de anuncios.

Cuenta de Google Ads: cliente 552-938-8450. ID de conversión de la etiqueta del sitio: `AW-18025178697` (ver `assets/js/reyes-conversion.js`).

## Reglas de copy aplicadas (revisar antes de pegar)

- Sin garantías, sin superlativos no verificables, sin «#1» ni «el mejor», sin promesas de resultados, sin precios ni descuentos (el sitio no tiene precios aprobados; ver `tests/conversion.test.js`).
- Español de México (es-MX): «celular», «cotización», «tienda en línea», «tú».
- **Transparencia geográfica:** Reyes Computing es una empresa colombiana. No hay oficina en México; la atención es **remota** (videollamada y WhatsApp). Ningún anuncio sugiere sede física en México.
- La pauta en Google Ads se paga directamente a Google; los honorarios y el alcance se definen en la cotización.
- Fintech (anuncio 2): no se afirma cumplimiento normativo, certificaciones ni auditorías formales. No uses «PCI DSS», «CNBV», «ISO 27001» ni similares como afirmación.
- La IA (anuncio 3) se describe como apoyo, no como resultado garantizado.
- No uses marcas de terceros (AWS, Google Cloud, Azure, Shopify, etc.) en el texto de los anuncios.
- Evita mayúsculas excesivas, signos repetidos y puntuación fuera de lo normal.
- No fijes titulares (pin); deja que Google rote.

## Configuración de la campaña

| Ajuste | Valor |
|---|---|
| Nombre sugerido | «MX - Búsqueda - Servicios» |
| Tipo de campaña | **Búsqueda** |
| Objetivo | **Clientes potenciales** (contactos por WhatsApp y formulario) |
| Redes | Solo Red de Búsqueda de Google. **Desmarca** «Red de Display» y, al inicio, «Socios de búsqueda» |
| Ubicaciones | México: **Ciudad de México**, **Guadalajara** (Jalisco), **Monterrey** (Nuevo León). Ciudades a confirmar por el dueño |
| Opción de ubicación | «Presencia: personas que están en tus ubicaciones objetivo» (no «Presencia o interés») |
| Idioma | Español |
| Dispositivos | Todos al inicio; revisar a los 14 días |
| Audiencias | Solo «Observación» si se agregan |
| Rotación de anuncios | Optimizar (preferir los de mejor rendimiento) |
| Horario de anuncios | **[DEFINIR POR EL DUEÑO]**: días y horas en que se puede responder por WhatsApp. La programación usa la **zona horaria de la cuenta** (confirmar cuál es; Colombia es UTC‑5 y el centro de México es UTC‑6 todo el año, 1 hora menos) |
| Presupuesto diario | **[DEFINIR POR EL DUEÑO]** (una sola campaña; los 3 grupos comparten presupuesto) |
| Estrategia de puja inicial | **Maximizar clics** con **CPC máximo [DEFINIR POR EL DUEÑO]**. Pasar a **Maximizar conversiones** cuando haya **N = [DEFINIR] conversiones** registradas de forma confiable (revisa el estado de aprendizaje). No fijar CPA objetivo hasta tener datos reales |
| `utm_campaign` | `mx-servicios` |

Si el dueño prefiere controlar el presupuesto por servicio, se puede mover cada grupo de anuncios a su propia campaña sin cambiar los textos (sigue siendo un anuncio por servicio).

## Medición de conversiones (antes de lanzar)

El sitio ya mide, con `assets/js/reyes-conversion.js`:

| Señal | Qué mide realmente | Uso en Google Ads |
|---|---|---|
| Acción existente «Clic WhatsApp» (etiqueta ya cargada en `ADS_ETIQUETA_CONVERSION`) | **Clics** en botones de WhatsApp, **no** conversaciones ni ventas | Conversión secundaria (o principal solo en la fase inicial); no equivale a un lead confirmado |
| Evento `formulario_intento` | El visitante envió el formulario válido; **no confirma recepción** | No tiene acción de conversión en Google Ads todavía |
| Evento `contacto_iniciado` (`metodo`: `whatsapp` o `llamada`) | Evento de análisis; las llamadas son un evento separado | No reutilizar la etiqueta de WhatsApp para llamadas o formularios |
| `success.html` (agradecimiento tras FormSubmit) | Carga tras el envío del formulario; ya tiene la etiqueta global y un comentario `ETIQUETA_FORMULARIO` | Mejor señal de formulario enviado |

**Recomendación (no inventes la etiqueta):**

1. En Google Ads: **Objetivos → Conversiones → Resumen → Nueva acción de conversión → Sitio web**. Crea una acción **propia para formularios** («Formulario enviado», categoría «Enviar formulario de clientes potenciales»). Usa la etiqueta que Google te entregue; **no** copies la de WhatsApp.
2. Quien mantenga el sitio pega esa etiqueta en `success.html` (comentario `ETIQUETA_FORMULARIO`) en un PR aparte, y confirma que el formulario de cada landing redirige a `success.html`.
3. Verifica con **Tag Assistant** que la conversión se dispara una sola vez, y con una prueba real que el correo llega a `control@reyescomputing.com` (el dueño debe tener activado FormSubmit para esa cuenta).
4. Marca como **Principales** solo las acciones que quieras optimizar y contrasta los chats reales con los clics de WhatsApp.
5. Si algún día se publica un número con enlaces `tel:`, crea una acción de llamada propia; hoy el sitio no publica enlaces `tel:`.

> Pendiente legal: el aviso de datos está en `contacto.html#privacidad`, pero no configura consentimiento de cookies. Confirma con el dueño antes de escalar el gasto.

## Pasos en Google Ads

1. **Campañas → + Nueva campaña** → objetivo **Clientes potenciales** → tipo **Búsqueda**.
2. Objetivos de conversión: WhatsApp y formulario (ver «Medición»).
3. Nombre, puja y presupuesto según la tabla (valores [DEFINIR]).
4. Redes, ubicaciones (CDMX, Guadalajara, Monterrey), opción «Presencia», idioma español.
5. Crea **3 grupos de anuncios** (A, B, C) con las palabras clave de la sección siguiente.
6. En **cada grupo** crea **un solo anuncio RSA** (el que corresponde). No dupliques anuncios entre grupos: en total son **3**.
7. Agrega las negativas (nivel campaña y por grupo) y las extensiones.
8. Revisa en «Vista previa de anuncios» y envía a revisión; corrige cualquier rechazo por política en lugar de apelar sin cambios.

## Grupos de anuncios y palabras clave

**Grupo A — Desarrollo web y marketing digital** (anuncio 1)

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
| "agencia de marketing digital" | Frase |
| [agencia de marketing digital] | Exacta |
| "marketing digital para pymes" | Frase |
| "publicidad en google ads" | Frase |
| [agencia de google ads] | Exacta |
| "agencia de marketing digital cdmx" | Frase |
| "agencia de marketing digital guadalajara" | Frase |
| "agencia de marketing digital monterrey" | Frase |
| "desarrollo web cdmx" | Frase |
| "desarrollo web guadalajara" | Frase |
| "desarrollo web monterrey" | Frase |

Negativas del grupo A (frase): `tienda online`, `tienda en línea`, `ecommerce`, `nube`, `seguridad web` (para que esas búsquedas vayan a los grupos C y B).

**Grupo B — Nube y seguridad web (contexto fintech)** (anuncio 2)

| Palabra clave | Concordancia |
|---|---|
| "servicios de computación en la nube" | Frase |
| [servicios de computación en la nube] | Exacta |
| "migración a la nube" | Frase |
| [migración a la nube para empresas] | Exacta |
| "consultoría cloud" | Frase |
| "consultoría en la nube méxico" | Frase |
| "infraestructura en la nube para startups" | Frase |
| "optimización de costos en la nube" | Frase |
| "monitoreo de servidores" | Frase |
| "seguridad web para empresas" | Frase |
| [seguridad web para empresas] | Exacta |
| "protección de sitio web" | Frase |
| "firewall de aplicaciones web" | Frase |
| [waf para sitio web] | Exacta |
| "revisión de seguridad web" | Frase |
| "seguridad web para fintech" | Frase |
| [ciberseguridad para fintech] | Exacta |
| "seguridad en la nube para fintech méxico" | Frase |

Notas del grupo B:
- No agregues «pci dss» ni términos de normativa financiera como palabra clave objetivo; podrían atraer búsquedas que esperan un anuncio que prometa cumplimiento.
- No ofrecemos productos financieros (servicios de TI para empresas, incluidas fintechs). Si Google solicita **verificación del anunciante** o marca «servicios financieros», sigue las instrucciones de la cuenta y confirma con el dueño.

**Grupo C — Tiendas en línea para México** (anuncio 3)

| Palabra clave | Concordancia |
|---|---|
| "crear tienda en línea" | Frase |
| [crear tienda en línea] | Exacta |
| "tienda en línea para negocio" | Frase |
| "desarrollo de tienda online méxico" | Frase |
| [desarrollo de tienda online] | Exacta |
| "app para mi tienda" | Frase |
| "aplicación para tienda en línea" | Frase |
| "automatización de inventarios" | Frase |
| [automatización de inventarios] | Exacta |
| "sincronizar inventario tienda en línea" | Frase |
| "actualización automática de precios" | Frase |
| "automatizar pedidos tienda en línea" | Frase |
| "tienda en línea con inteligencia artificial" | Frase |
| "chatbot para tienda en línea" | Frase |
| "tienda en línea cdmx" | Frase |
| "tienda en línea guadalajara" | Frase |
| "tienda en línea monterrey" | Frase |

Empieza con frase y exacta en todos los grupos; evita concordancia amplia hasta revisar términos de búsqueda.

## Palabras clave negativas (nivel campaña)

Cárgalas en concordancia de frase.

`gratis`, `gratuito`, `gratuita`, `curso`, `cursos`, `tutorial`, `como hacer`, `cómo hacer`, `plantilla`, `plantillas`, `template`, `descargar`, `pdf`, `código fuente`, `github`, `empleo`, `empleos`, `trabajo`, `vacante`, `vacantes`, `sueldo`, `salario`, `prácticas`, `pasante`, `universidad`, `carrera`, `maestría`, `diplomado`, `wix gratis`, `wordpress gratis`, `hazlo tu mismo`, `app gratis`, `certificación`, `certificacion`, `certificado`, `examen`, `que es`, `qué es`, `definición`, `antivirus`, `vpn`, `hackear`, `hackeo`, `hacker`, `contraseña`, `recuperar cuenta`, `cuenta hackeada`, `crack`, `shopify`, `mercadolibre`, `mercado libre`, `amazon`, `comprar`, `tienda cerca`

Revisa el informe de **términos de búsqueda** a los 7 días y agrega más.

## Anuncios (3 RSA en total)

Límites: titulares ≤ 30 caracteres, descripciones ≤ 90, rutas ≤ 15. Los conteos de la columna «Car.» fueron calculados con un script.

### Anuncio 1 — Desarrollo web y marketing digital (Grupo A)

URL final: `https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=anuncio-1`

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
| H9 | Sitios Adaptados al Celular | 27 |
| H10 | ¿Tu Web No Genera Contactos? | 28 |
| H11 | Revisamos tu Sitio Web | 22 |
| H12 | Estrategia Digital con Plan | 27 |
| H13 | Cotiza por WhatsApp | 19 |
| H14 | Solicita tu Cotización Web | 26 |
| H15 | Agenda una Videollamada | 23 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Creamos tu sitio web y tu plan de marketing digital con un solo equipo de trabajo. | 82 |
| D2 | Empresa colombiana con atención remota para negocios en CDMX, Guadalajara y Monterrey. | 86 |
| D3 | ¿Tu sitio no te trae contactos? Revisamos tu web y tus anuncios y proponemos mejoras. | 85 |
| D4 | La pauta se paga directo a Google Ads. Alcance y honorarios van en la cotización. | 81 |

### Anuncio 2 — Nube y seguridad web, con contexto fintech (Grupo B)

URL final: `https://www.reyescomputing.com/mexico-nube-seguridad-web.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=anuncio-2`

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
| H5 | Atención Remota en México | 25 |
| H6 | Protección de Sitios Web | 24 |
| H7 | WAF y HTTPS para tu Sitio | 25 |
| H8 | Seguridad Web para Fintech | 26 |
| H9 | ¿Sube tu Factura de Nube? | 25 |
| H10 | ¿Caídas en tu Servidor? | 23 |
| H11 | Revisión de Seguridad Web | 25 |
| H12 | Monitoreo de tu Servidor | 24 |
| H13 | Consultoría Cloud en Remoto | 27 |
| H14 | Reyes Computing Colombia | 24 |
| H15 | Cotiza por WhatsApp | 19 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Te ayudamos con tu infraestructura en la nube y con la seguridad de tu sitio web. | 81 |
| D2 | Para fintech en México: revisión de controles web y nube. No es una auditoría formal. | 85 |
| D3 | Configuración de WAF, HTTPS, respaldos y monitoreo según lo que tu proyecto necesite. | 85 |
| D4 | Sin oficina en México: atención remota. Los costos de nube se pagan al proveedor. | 81 |

### Anuncio 3 — Tiendas en línea para México (Grupo C)

URL final: `https://www.reyescomputing.com/mexico-tiendas-online.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=anuncio-3`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | tienda-en-linea | 15 |
| R2 | mexico | 6 |

| # | Titular | Car. |
|---|---|---|
| H1 | Tienda en Línea para México | 27 |
| H2 | Tienda Online a tu Medida | 25 |
| H3 | App para tu Tienda | 18 |
| H4 | Tienda Web y App de Celular | 27 |
| H5 | Automatiza Inventarios | 22 |
| H6 | Precios Sincronizados | 21 |
| H7 | Pedidos Más Ordenados | 21 |
| H8 | Tienda en Línea con IA | 22 |
| H9 | Catálogo y Carrito de Compras | 29 |
| H10 | ¿Inventario en Excel y Chats? | 29 |
| H11 | Atención Remota en México | 25 |
| H12 | Reyes Computing Colombia | 24 |
| H13 | Cotiza tu Tienda en Línea | 25 |
| H14 | Escríbenos por WhatsApp | 23 |
| H15 | Agenda una Videollamada | 23 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Diseñamos tu tienda en línea y tu app para que tus clientes compren desde el celular. | 85 |
| D2 | Conectamos inventario, precios y pedidos. Podemos sumar IA para atención y seguimiento. | 87 |
| D3 | Empresa colombiana con atención remota para negocios en CDMX, Guadalajara y Monterrey. | 86 |
| D4 | Cuéntanos qué vendes y cómo manejas tu inventario. Alcance y honorarios en la cotización. | 89 |

> Si el dueño aprueba una oferta concreta en `ofertas.html`, puede sustituir un titular o descripción de un anuncio por el texto exacto de la oferta con sus condiciones reales. No inventes precios ni descuentos.

## Extensiones (activos) — a nivel de campaña

**Vínculos de sitio (sitelinks)** — título ≤ 25, líneas ≤ 35. Las URL de `ofertas.html` y `contacto.html` dependen de que estén publicadas.

| # | Título | Línea 1 | Línea 2 | URL final | Car. T/L1/L2 |
|---|---|---|---|---|---|
| SL1 | Web y marketing | Sitios web y publicidad digital | Atención remota a México | https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=sitelink-web-marketing | 15/31/24 |
| SL2 | Nube y seguridad web | Infraestructura y protección web | Atención remota a México | https://www.reyescomputing.com/mexico-nube-seguridad-web.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=sitelink-nube-seguridad | 20/32/24 |
| SL3 | Tiendas en línea | Tienda web, app y automatización | Atención remota a México | https://www.reyescomputing.com/mexico-tiendas-online.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=sitelink-tiendas | 16/32/24 |
| SL4 | Cómo funciona | Del contacto a la propuesta | Paso a paso, en remoto | https://www.reyescomputing.com/como-funciona.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=sitelink-como-funciona | 13/27/22 |
| SL5 | Ofertas | Revisa las ofertas vigentes | Condiciones en la página | https://www.reyescomputing.com/ofertas.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=sitelink-ofertas | 7/27/24 |
| SL6 | Contacto | Escríbenos por WhatsApp | O usa el formulario | https://www.reyescomputing.com/contacto.html?utm_source=google&utm_medium=cpc&utm_campaign=mx-servicios&utm_content=sitelink-contacto | 8/23/19 |

**Textos destacados (callouts)** — ≤ 25 caracteres.

| # | Texto | Car. |
|---|---|---|
| C1 | Atención remota a México | 24 |
| C2 | Cotización por WhatsApp | 23 |
| C3 | Equipo colombiano | 17 |
| C4 | Contacto por videollamada | 25 |
| C5 | Sitios para celular | 19 |

**Fragmentos estructurados** — encabezado «Servicios», valores ≤ 25 caracteres.

| # | Valor | Car. |
|---|---|---|
| S1 | Desarrollo web | 14 |
| S2 | Marketing digital | 17 |
| S3 | Nube y seguridad web | 20 |
| S4 | Tiendas en línea | 16 |

**Llamada:** no activar. El sitio no publica un teléfono de atención; el único número es el WhatsApp comercial de Colombia (+57). **Formulario de clientes potenciales / mensajes:** no activar al inicio.

## Checklist de lanzamiento

- [ ] Las 3 landings (`mexico-desarrollo-web-marketing-digital.html`, `mexico-nube-seguridad-web.html`, `mexico-tiendas-online.html`) publicadas, con HTTPS, buen aspecto en celular y aclaración de atención remota (sin oficina en México).
- [ ] La landing 2 no afirma cumplimiento, certificaciones ni resultados.
- [ ] Botón de WhatsApp y formulario operativos en cada landing; el formulario llega a `control@reyescomputing.com` y redirige a `success.html`.
- [ ] Acción de conversión del formulario creada y etiqueta instalada (si no, lanzar midiendo solo WhatsApp y dejar claro que el formulario no se cuenta como conversión).
- [ ] Tag Assistant confirma «Clic WhatsApp» y `formulario_intento`.
- [ ] Presupuesto, CPC máximo, N, horario y ciudades **confirmados por el dueño**.
- [ ] Exactamente 3 anuncios cargados, 1 por grupo; ninguno excede los límites.
- [ ] Negativas (campaña y grupo A) y extensiones cargadas; las páginas de sitelink existen.
- [ ] Verificar si Google pide verificación del anunciante (grupo B).
- [ ] Facturación activa y alguien disponible para responder WhatsApp en el horario.

## Qué revisar

**A los 7 días**
- Aprobación de anuncios y estado de política (especialmente el anuncio 2).
- **Términos de búsqueda** por grupo: agregar negativas; confirmar que las búsquedas de tienda no entran al grupo A ni las de seguridad personal (antivirus, VPN, cuentas hackeadas) al B.
- Impresiones, CTR, CPC medio frente al máximo; cuota de impresiones perdida por presupuesto/ranking. Si algún grupo no tiene impresiones, revisa si hay poco volumen y amplía con frase.
- Conversiones: clics en WhatsApp vs. chats reales; formularios (`success.html`) vs. correos.
- Informe de ubicaciones: que no entren clics fuera de CDMX/Guadalajara/Monterrey.
- No cambiar la puja ni pausar anuncios antes de tener datos suficientes (salvo problemas de política).

**A los 14 días**
- Rendimiento de los 3 grupos/anuncios por conversiones y calificación de activos, no solo por CTR; comparar qué servicio atrae contactos de calidad.
- Informes por ciudad, dispositivo, día y hora; ajustar el horario real.
- Calidad de los contactos: registrar en una hoja con la fuente (`utm_content=anuncio-1|2|3`).
- Sustituir titulares de menor rendimiento por otras variantes que respeten las reglas de copy (sin añadir anuncios).

**A los 30 días**
- Decidir si hay N conversiones fiables para pasar a **Maximizar conversiones**.
- Decidir con el dueño si se amplían, recortan o separan por campaña ciudades y servicios.
- Pausar palabras clave con gasto sin contactos y ampliar las que traen contactos de calidad.
- Revisión de presupuesto con costos reales por contacto calculados por el dueño; este documento no fija CPA ni ROI.
- Ajustar las landings con las preguntas reales que llegaron por WhatsApp.

---

Estos textos no confirman el estado real de Google Ads; verifica la cuenta antes de duplicar o pausar campañas existentes. Ver también `campanas/README.md` y `google_ads_campaign_urls.md`.
