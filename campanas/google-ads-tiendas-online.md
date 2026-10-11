# Google Ads — Nuevo servicio Tiendas Online, Colombia (3 anuncios en total)

Instrucciones paso a paso para montar la campaña de Búsqueda del nuevo servicio **Tiendas Online**: app de tienda, tienda web, automatizaciones de inventarios, precios y pedidos, e inteligencia artificial (IA). Estructura: **una campaña, 3 grupos de anuncios y exactamente 3 anuncios RSA en total (uno por grupo)**. Los campos marcados **[DEFINIR POR EL DUEÑO]** no deben llenarse con datos inventados.

| Anuncio | Enfoque | Grupo de anuncios | Landing |
|---|---|---|---|
| 1 | Tienda web + app de tienda | Grupo 3A | https://www.reyescomputing.com/tiendas-online.html |
| 2 | Automatización de inventarios, precios y pedidos; seguimiento y entrega | Grupo 3B | https://www.reyescomputing.com/tiendas-online.html |
| 3 | IA para la tienda + llamada a la acción | Grupo 3C | https://www.reyescomputing.com/tiendas-online.html |

Tiendas online **para México** (`mexico-tiendas-online.html`) se gestiona en `google-ads-mexico.md` (anuncio 3 y grupo C); no se duplica aquí.

> **Prerrequisito:** la landing debe estar publicada y responder con HTTP 200 antes de activar la campaña:
> - https://www.reyescomputing.com/tiendas-online.html
>
> Las páginas https://www.reyescomputing.com/ofertas.html y https://www.reyescomputing.com/contacto.html (sitelinks) también deben existir. Verifica que la landing describa lo mismo que dicen los anuncios (tienda web, app, automatizaciones, IA) y que no tenga precios no aprobados.

Cuenta de Google Ads: cliente 552-938-8450. ID de conversión de la etiqueta del sitio: `AW-18025178697` (ver `assets/js/reyes-conversion.js`).

## Reglas de copy aplicadas

- Sin garantías, sin superlativos no verificables, sin «#1» ni «el mejor», sin promesas de resultados (no se promete más ventas, ahorro ni tiempos), sin precios ni descuentos (ver `tests/conversion.test.js`).
- Español de Colombia: «tienda virtual», «celular», «cotización».
- La IA se describe como apoyo («podemos sumar»), no como resultado garantizado.
- No se mencionan marcas de terceros (Shopify, Mercado Libre, etc.) en el texto de los anuncios.
- No fijes titulares (pin); deja que Google rote.
- El alcance y los costos del proyecto se definen en la cotización; la pauta se paga directamente a Google Ads.

## Configuración de la campaña

| Ajuste | Valor |
|---|---|
| Nombre sugerido | «CO - Búsqueda - Tiendas online» |
| Tipo de campaña | **Búsqueda** |
| Objetivo | **Clientes potenciales** (contactos por WhatsApp y formulario) |
| Redes | Solo Red de Búsqueda de Google. **Desmarca** «Red de Display» y, al inicio, «Socios de búsqueda» |
| Ubicaciones | Colombia: **Cali**, **Bogotá**, **Medellín**. **A confirmar por el dueño** (puede añadirse o quitarse alguna ciudad) |
| Opción de ubicación | «Presencia: personas que están en tus ubicaciones objetivo» |
| Idioma | Español |
| Dispositivos | Todos al inicio; revisar a los 14 días |
| Horario de anuncios | **[DEFINIR POR EL DUEÑO]**: días y horas en que se puede responder por WhatsApp (se usa la zona horaria de la cuenta; confirmar cuál es) |
| Presupuesto diario | **[DEFINIR POR EL DUEÑO]** |
| Estrategia de puja inicial | **Maximizar clics** con **CPC máximo [DEFINIR POR EL DUEÑO]**. Pasar a **Maximizar conversiones** cuando haya **N = [DEFINIR] conversiones** registradas de forma confiable. No fijar CPA objetivo hasta tener datos reales |
| `utm_campaign` | `tiendas-online` |

## Medición de conversiones (antes de lanzar)

Con `assets/js/reyes-conversion.js` el sitio ya registra:

- **Clic WhatsApp:** acción existente con etiqueta ya cargada. Mide **clics** en botones de WhatsApp, **no** conversaciones ni ventas.
- **`formulario_intento`:** el visitante envió el formulario válido; no confirma recepción.
- **`contacto_iniciado`** (`metodo`: `whatsapp` o `llamada`): evento de análisis. Las llamadas son un evento separado; hoy el sitio no publica enlaces `tel:`.
- **`success.html`:** página de agradecimiento tras FormSubmit; ya incluye la etiqueta global y un comentario con el marcador `ETIQUETA_FORMULARIO`.

**Recomendación (no inventes la etiqueta):**

1. En Google Ads: **Objetivos → Conversiones → Resumen → Nueva acción de conversión → Sitio web** y crea una acción **propia para formularios** («Formulario enviado»). Usa la etiqueta que Google te entregue; no reutilices la de WhatsApp. Si ya la creaste para la campaña de México, usa la misma.
2. Quien mantenga el sitio pega esa etiqueta en `success.html` (PR aparte) y confirma que el formulario de `tiendas-online.html` redirige a `success.html`.
3. Verifica con **Tag Assistant** y con una prueba real que el correo llega a `control@reyescomputing.com` (FormSubmit activado por el dueño).
4. Decide con el dueño cuáles acciones son **Principales**. «Clic WhatsApp» sigue siendo clic, no lead confirmado.

> Pendiente legal: el aviso de datos está en `contacto.html#privacidad` y no configura consentimiento de cookies. Confirma con el dueño antes de escalar el gasto.

## Pasos en Google Ads

1. **Campañas → + Nueva campaña** → objetivo **Clientes potenciales** → tipo **Búsqueda**.
2. Objetivos de conversión: WhatsApp y formulario.
3. Nombre, puja y presupuesto según la tabla (valores [DEFINIR]).
4. Redes, ubicaciones (Cali, Bogotá, Medellín), opción «Presencia», idioma español.
5. Crea los **3 grupos de anuncios** (3A, 3B, 3C) con sus palabras clave.
6. En **cada grupo** crea **un solo anuncio RSA** (el que corresponde). En total son **3** anuncios; no dupliques.
7. Agrega negativas y extensiones.
8. Revisa en la vista previa y envía a revisión.

## Grupos de anuncios y palabras clave

URL final de todos los anuncios: la landing de la campaña con el UTM del anuncio.

**Grupo 3A — Tienda online y app** (anuncio 1)

| Palabra clave | Concordancia |
|---|---|
| "crear tienda online" | Frase |
| [crear tienda online] | Exacta |
| "tienda virtual para negocio" | Frase |
| "desarrollo de tienda online" | Frase |
| [desarrollo de tienda online] | Exacta |
| "tienda online colombia" | Frase |
| "app para mi tienda" | Frase |
| "aplicación para tienda online" | Frase |
| "tienda online con app móvil" | Frase |
| "catálogo de productos online" | Frase |

**Grupo 3B — Automatización de inventarios, precios y pedidos** (anuncio 2)

| Palabra clave | Concordancia |
|---|---|
| "automatización de inventarios" | Frase |
| [automatización de inventarios] | Exacta |
| "sincronizar inventario tienda online" | Frase |
| "actualización automática de precios" | Frase |
| "automatizar pedidos tienda online" | Frase |
| "control de inventario para tienda online" | Frase |
| "gestión de pedidos online" | Frase |
| [software de inventario y pedidos] | Exacta |
| "seguimiento de pedidos tienda online" | Frase |
| "seguimiento de despachos" | Frase |
| "software de logística y entregas" | Frase |
| "evidencia de entrega" | Frase |
| "prueba de entrega con foto" | Frase |
| "pago en app tienda online" | Frase |

Alcance en los anuncios y la landing (sección «Del pago a la entrega, todo trazable»): parte es base ya construida y parte se desarrolla a la medida según el alcance (panel de logística, rol de conductor, pasarela de pago real validada). Los textos usan «pago en la app», «seguimiento del pedido» y «evidencia de entrega» sin presentarlo como ya incluido ni como operando con clientes; no prometas integración con una pasarela o transportadora concretas.

**Grupo 3C — Tienda online con IA** (anuncio 3)

| Palabra clave | Concordancia |
|---|---|
| "tienda online con inteligencia artificial" | Frase |
| "inteligencia artificial para tiendas online" | Frase |
| "chatbot para tienda online" | Frase |
| "asistente de ventas con ia" | Frase |
| "automatización con ia para ecommerce" | Frase |

Empieza con frase y exacta; evita amplia hasta revisar términos de búsqueda.

## Palabras clave negativas (nivel campaña)

`gratis`, `gratuito`, `gratuita`, `curso`, `cursos`, `tutorial`, `como hacer`, `cómo hacer`, `plantilla`, `plantillas`, `template`, `descargar`, `pdf`, `código fuente`, `github`, `empleo`, `trabajo`, `vacante`, `sueldo`, `salario`, `prácticas`, `universidad`, `diplomado`, `shopify`, `mercadolibre`, `mercado libre`, `amazon`, `comprar`, `tienda cerca`, `crear tienda online gratis`

Nota: no se agrega «precio» como negativa porque puede traer consultas legítimas de cotización; revisa los términos a los 7 días.

## Anuncios (3 RSA en total)

Límites: titulares ≤ 30 caracteres, descripciones ≤ 90, rutas ≤ 15. La columna «Car.» fue calculada con un script.

### Anuncio 1 — Tienda web + app de tienda (Grupo 3A)

URL final: `https://www.reyescomputing.com/tiendas-online.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=anuncio-1`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | tiendas-online | 14 |
| R2 | web-y-app | 9 |

| # | Titular | Car. |
|---|---|---|
| H1 | Tienda Online a tu Medida | 25 |
| H2 | App para tu Tienda | 18 |
| H3 | Tienda Web y App Móvil | 22 |
| H4 | Vende en Línea con tu Marca | 27 |
| H5 | Catálogo y Carrito de Compras | 29 |
| H6 | Tienda Virtual para tu Negocio | 30 |
| H7 | Diseño de Tienda Online | 23 |
| H8 | App de Tienda para Celular | 26 |
| H9 | Nuevo: Servicio de Tiendas | 26 |
| H10 | Reyes Computing | 15 |
| H11 | Cali, Bogotá y Medellín | 23 |
| H12 | Un Solo Equipo, Todo Conectado | 30 |
| H13 | Cotiza tu Tienda Online | 23 |
| H14 | Solicita tu Cotización | 22 |
| H15 | Escríbenos por WhatsApp | 23 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Diseñamos tu tienda web y tu app de tienda para que tus clientes compren desde el celular. | 90 |
| D2 | Servicio nuevo de Reyes Computing: tienda web, app, automatizaciones e IA para tu negocio. | 90 |
| D3 | Elige solo lo que necesitas: tienda web, app o automatizaciones. Alcance en la cotización. | 90 |
| D4 | Cuéntanos qué vendes y cómo manejas tu inventario. Te enviamos una propuesta a tu medida. | 89 |

### Anuncio 2 — Automatización de inventarios, precios y pedidos; seguimiento y entrega (Grupo 3B)

URL final: `https://www.reyescomputing.com/tiendas-online.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=anuncio-2`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | automatiza | 10 |
| R2 | tu-tienda | 9 |

| # | Titular | Car. |
|---|---|---|
| H1 | ¿Inventario en Excel y Chats? | 29 |
| H2 | ¿Precios Desactualizados? | 25 |
| H3 | ¿Pedidos Perdidos en WhatsApp? | 30 |
| H4 | Deja el Inventario a Mano | 25 |
| H5 | Seguimiento del Pedido | 22 |
| H6 | Mantén Stock y Precios al Día | 29 |
| H7 | Pedidos en un Solo Lugar | 24 |
| H8 | Automatización para Tiendas | 27 |
| H9 | Automatiza Inventarios | 22 |
| H10 | Evidencia de Entrega | 20 |
| H11 | Del Pago a la Entrega | 21 |
| H12 | Ordena tu Tienda Online | 23 |
| H13 | Pago en la App o Web | 20 |
| H14 | Habla con Reyes Computing | 25 |
| H15 | Escríbenos por WhatsApp | 23 |

| # | Descripción | Car. |
|---|---|---|
| D1 | ¿Manejas inventario y precios en hojas de cálculo? Automatiza esas tareas con tu tienda. | 88 |
| D2 | Conectamos tu tienda con tus pedidos y tu inventario para trabajar con datos ordenados. | 87 |
| D3 | Pago en la app, seguimiento del pedido y evidencia de entrega, según el alcance acordado. | 89 |
| D4 | El alcance depende de tu operación. Te hacemos una propuesta al conocer tu negocio. | 83 |

### Anuncio 3 — IA para la tienda y llamada a la acción (Grupo 3C)

URL final: `https://www.reyescomputing.com/tiendas-online.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=anuncio-3`

| Ruta | Texto | Car. |
|---|---|---|
| R1 | tienda-con-ia | 13 |
| R2 | cotiza | 6 |

| # | Titular | Car. |
|---|---|---|
| H1 | Tienda Online con IA | 20 |
| H2 | IA para Atender Clientes | 24 |
| H3 | Asistente con IA para Ventas | 28 |
| H4 | Chatbot para tu Tienda | 22 |
| H5 | Alertas de Stock con IA | 23 |
| H6 | Clasifica Pedidos con IA | 24 |
| H7 | Automatización con IA | 21 |
| H8 | Solicita tu Cotización | 22 |
| H9 | Agenda una Videollamada | 23 |
| H10 | Escríbenos por WhatsApp | 23 |
| H11 | Cuéntanos qué Vendes | 20 |
| H12 | Propuesta Según tu Negocio | 26 |
| H13 | Equipo Colombiano | 17 |
| H14 | Ve las Ofertas del Servicio | 27 |
| H15 | Resuelve tus Dudas por Chat | 27 |

| # | Descripción | Car. |
|---|---|---|
| D1 | Podemos sumar IA a tu tienda online: respuestas a clientes y seguimiento de pedidos. | 84 |
| D2 | La IA es un apoyo para tu equipo; el alcance se define según tu operación y tus datos. | 86 |
| D3 | Solicita tu cotización de tienda online. Te respondemos por WhatsApp. | 69 |
| D4 | Escríbenos o usa el formulario y te orientamos sobre los siguientes pasos. | 74 |

> Si el dueño aprueba una oferta concreta en `ofertas.html`, puede sustituir un titular o descripción por el texto exacto de la oferta con sus condiciones reales. No inventes precios ni descuentos. Si «Ve las Ofertas del Servicio» (anuncio 3, H14) no se corresponde con una oferta publicada, elimínalo.

## Extensiones (activos)

**Vínculos de sitio (sitelinks)** — título ≤ 25, líneas ≤ 35. Las URL de `ofertas.html` y `contacto.html` dependen de que estén publicadas.

| # | Título | Línea 1 | Línea 2 | URL final | Car. T/L1/L2 |
|---|---|---|---|---|---|
| SL1 | Ofertas | Revisa las ofertas vigentes | Condiciones en la página | https://www.reyescomputing.com/ofertas.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=sitelink-ofertas | 7/27/24 |
| SL2 | Contacto | Escríbenos por WhatsApp | O usa el formulario | https://www.reyescomputing.com/contacto.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=sitelink-contacto | 8/23/19 |
| SL3 | Cómo funciona | Del contacto a la propuesta | Paso a paso | https://www.reyescomputing.com/como-funciona.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=sitelink-como-funciona | 13/27/11 |
| SL4 | Casos de éxito | Conoce proyectos de Reyes | Revisa ejemplos publicados | https://www.reyescomputing.com/casos-de-exito.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=sitelink-casos | 14/25/26 |
| SL5 | Del pago a la entrega | Seguimiento y evidencia | Alcance según tu proyecto | https://www.reyescomputing.com/tiendas-online.html?utm_source=google&utm_medium=cpc&utm_campaign=tiendas-online&utm_content=sitelink-pago-entrega#flujo-entrega | 21/23/25 |

**Textos destacados (callouts)** — ≤ 25 caracteres.

| # | Texto | Car. |
|---|---|---|
| C1 | Tienda web y app móvil | 22 |
| C2 | Automatiza inventarios | 22 |
| C3 | Cotización por WhatsApp | 23 |
| C4 | Equipo colombiano | 17 |
| C5 | IA aplicada a tu tienda | 23 |

**Fragmentos estructurados** — encabezado «Servicios», valores ≤ 25 caracteres.

| # | Valor | Car. |
|---|---|---|
| S1 | Tienda web | 10 |
| S2 | App de tienda | 13 |
| S3 | Automatización de pedidos | 25 |
| S4 | Inteligencia artificial | 23 |

**Llamada:** no activar; el sitio no publica un teléfono de atención (solo el WhatsApp comercial).

## Checklist de lanzamiento

- [ ] `tiendas-online.html`, `ofertas.html` y `contacto.html` publicadas y funcionando en celular.
- [ ] Botón de WhatsApp y formulario operativos; el formulario llega a `control@reyescomputing.com` y redirige a `success.html`.
- [ ] Acción de conversión del formulario creada y etiqueta instalada (o dejar documentado que solo se mide WhatsApp).
- [ ] Tag Assistant confirma «Clic WhatsApp» y `formulario_intento`.
- [ ] Ciudades (Cali, Bogotá, Medellín), presupuesto, CPC máximo, N y horario **confirmados por el dueño**.
- [ ] Exactamente 3 anuncios (1 por grupo) dentro de los límites; sin promesas ni precios.
- [ ] Negativas y extensiones cargadas.
- [ ] Facturación de Google Ads activa.
- [ ] Alguien responde WhatsApp en el horario configurado.

## Qué revisar

**A los 7 días**
- Aprobación y políticas.
- Términos de búsqueda por grupo: agrega negativas (en especial marcas de plataformas, «gratis», cursos y empleo).
- Impresiones, CTR, CPC medio frente al máximo; cuota de impresiones perdida. El grupo 3C puede tener poco volumen.
- Clics en WhatsApp vs. chats reales; formularios (`success.html`) vs. correos.
- No cambiar puja ni pausar sin datos suficientes (salvo problemas de política).

**A los 14 días**
- Rendimiento por grupo/anuncio (web+app, automatización, IA); calificación de activos.
- Informes por ciudad, dispositivo y hora; ajustar el horario.
- Calidad de los contactos: ¿tienen tienda o inventario real?; registrar en una hoja por UTM.
- Sustituir titulares de menor rendimiento (sin añadir anuncios).

**A los 30 días**
- Decidir si hay N conversiones fiables para pasar a **Maximizar conversiones**.
- Decidir con el dueño si se mantienen, amplían o recortan ciudades.
- Pausar palabras clave con gasto y sin contactos; ampliar las que traen contactos de calidad.
- Revisar con costos reales el presupuesto (este documento no fija CPA ni ROI).
- Ajustar la landing con las dudas reales de los contactos.

---

Estos textos no confirman el estado real de Google Ads. Ver también `campanas/README.md` y `google_ads_campaign_urls.md`.
