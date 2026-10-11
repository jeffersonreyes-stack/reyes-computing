# Definición del servicio "Tiendas Online" (documento interno)

> Documento interno. No se publica en el sitio: el workflow `deploy.yml` excluye `*.md` del `aws s3 sync` (ver sección 8).
> Fecha de la revisión: 2026-10-11. Base: lectura de solo lectura de los repos locales `ferretero`, `juanshop`, `listoshop` y `powerbud`, más `operacion/evidencia_produccion.csv`, `operacion/verificacion_evidencia.csv` y `operacion/costos_productos.csv`.
> No contiene precios. Página pública asociada: `tiendas-online.html`.

## 1. Propuesta de nombre y posicionamiento

- **Nombre del servicio:** *Tiendas Online* (nombre exacto de la página; ya hay una fila "Tienda online" en `operacion/costos_productos.csv` con estado `EN_BACKLOG`, y un plan "Tienda Online (E-Commerce)" en `desarrollo-web.html`).
- **Nombre interno de la arquitectura:** "Tienda modular" (catálogo + inventario + precios + pedidos + notificaciones + panel + IA).
- **Posicionamiento:** tienda a medida construida por módulos sobre bases propias ya probadas, para negocios que hoy venden por chat/Excel. Se vende por alcance, sin precios publicados.
- **Tres niveles, cada uno incluye al anterior:**
  - **Básico / Tienda web:** web de tienda (catálogo, búsqueda y filtros, ficha, carrito, pedido con coordinación por WhatsApp), panel de productos/stock/pedidos, estados de pedido con historial.
  - **Intermedio / + App:** app móvil Android/iOS (vista comprador y vendedor) sobre la misma base de datos, más configuración de compilación y envío a tiendas de apps.
  - **Completo / + Automatizaciones + IA:** automatizaciones a medida de inventario, precios y pedidos; avisos automáticos; módulo de asistente con IA en Docker, con revisión humana.
- **Reglas de comunicación (vigiladas por `tests/conversion.test.js`):** sin precios ni descuentos, sin garantía de ventas/ROI, sin "24/7", sin certificaciones de terceros; el cliente aporta fotos, videos y textos; producción visual y volumen de imágenes adicional se cotizan aparte; comisiones de pasarelas, hosting/dominio, cuentas de Apple/Google, API oficial de WhatsApp y consumo de API de IA los paga el cliente aparte.

## 2. Arquitectura por módulos

| # | Módulo | Qué hace | Estado real en los repos | Origen reutilizable |
|---|--------|----------|--------------------------|---------------------|
| 1 | Catálogo | Productos, categorías, búsqueda, filtros (marca/talla/color), imágenes | Existe en las 3 apps. Filtros marca/talla/color: `listoshop` (`add_product_filters.sql`, `search.tsx`) | listoshop / juanshop |
| 2 | Inventario | Stock por producto, validación y descuento en el pedido, devolución al cancelar, alerta de stock bajo | Descuento atómico con bloqueo de fila y devolución al cancelar: `juanshop` y `listoshop` (`checkout_atomic`, `advance_order_status`). Alerta de stock bajo (< 10): `ferretero/my-products.tsx`. **`ferretero_checkout` NO valida ni descuenta stock** | juanshop |
| 3 | Precios | Precio vigente desde el catálogo, precio histórico en cada ítem | Recalculo de totales en servidor y `unit_price` por ítem: las tres apps. **No existe** lista de precios por cliente/categoría ni carga/actualización masiva en el código | juanshop (base); resto es a medida |
| 4 | Pedidos | Carrito, checkout, estados con bitácora, chat por pedido, comprobantes, evidencia de entrega | Máquina de estados + `order_events`: `juanshop`/`listoshop`. Chat con Realtime, `payment_receipts` (nequi/transferencia/efectivo): solo `juanshop`. `delivery_evidence`: `juanshop`/`listoshop` | juanshop |
| 5 | Pagos | Pasarela en línea | `ferretero`: simulación + webhook de ejemplo. `juanshop`/`listoshop`: modo sandbox simulado y rama Wompi escrita en el cliente. **Ninguna validada con un comercio real en el código** | A rehacer del lado servidor |
| 6 | Notificaciones / WhatsApp | Avisos al cliente y al vendedor | Solo enlaces `wa.me` con mensaje prellenado (`juanshop`: "Hacer pedido por WhatsApp" y "Gestionar pago en WhatsApp"). No hay WhatsApp Business API. `powerbud`: notificaciones in-app y correo (Resend) | juanshop (wa.me) / powerbud (correo, notificaciones) |
| 7 | Panel admin | Productos, stock, pedidos, métricas básicas | Vista de vendedor en las 3 apps (dashboard con ventas/pedidos, mis productos, agregar producto, pedidos). `powerbud` tiene rutas de admin | ferretero / juanshop |
| 8 | IA | Asistente que genera borradores y los somete a revisión | `powerbud/src/ai.js`: Gemini (`gemini-2.5-flash-lite`) con reintentos, plan de respaldo si falla, segundo prompt de revisión, salida JSON. Dominio actual: fitness/nutrición, **no** tienda | powerbud (patrón); adaptación a tienda es nueva |
| 9 | Despliegue | Contenedor del backend y compilación de apps | `powerbud`: `Dockerfile` + `docker-compose.yml`. Apps: `eas.json` con perfiles development/preview/production | powerbud / apps |

Flujo de datos recomendado: apps y web → Supabase (Auth, Postgres con RLS, Storage, funciones RPC para reglas de pedido) → Edge Function para webhook de pasarela → (opcional) servicio Node/Docker para IA y avisos.

## 3. Stack real encontrado por repo

### ferretero (app móvil Expo; marketplace ferretero)
- Expo ~54, React Native 0.81, Expo Router, NativeWind, Zustand, `@supabase/supabase-js`, TypeScript.
- 62 archivos versionados. Rutas: `(auth)`, `(buyer_tabs)` (inicio, búsqueda, carrito, pedidos, perfil), `(vendor_tabs)` (dashboard, productos, agregar producto, pedidos), `product/[id]`.
- Supabase: `supabase_schema.sql` (perfiles, tiendas, productos, cotizaciones, pedidos, categorías, reseñas, documentos) con RLS; función `ferretero_checkout` (recalcula precios desde BD); Edge Function `payment-webhook`.
- Commits: 25 (evidencia: 8.8 h medidas, 4.578 líneas, 0 archivos de prueba).
- **Discrepancia a tener en cuenta:** `ANALYSIS.md` e `INFORME.md` mencionan `ETLService`/OCR y descuentos por cliente y categoría, pero en el árbol de trabajo **no existe `services/etl.ts`**, no hay UI de descuentos (solo un tipo `VendorDiscount` en `types/database.ts`) y `jest.config.js` no tiene pruebas. No se declaró nada de eso en la web pública.
- `ferretero_checkout_rpc.sql` y `supabase/migrations/002_seed_test_products.sql` están sin versionar (`??` en git).

### juanshop (app móvil Expo; el sistema más completo en flujo de pedidos)
- Mismo stack que ferretero (Expo 54, NativeWind, Zustand, Supabase). `app.json`: paquete `com.reyescomputing.juanshop`.
- Esquema `juanshop_schema_v2.sql`: perfiles, tiendas, productos, pedidos, ítems, `order_events`, `messages`, `payment_receipts`, `delivery_evidence`; funciones `checkout_atomic` (valida y descuenta stock con `FOR UPDATE`), `advance_order_status` (valida transiciones, devuelve stock al cancelar) y helpers RLS.
- Servicios: `orders.ts`, `messages.ts` (Realtime), `receipts.ts`, `delivery.ts`, `payment.ts` (sandbox + Wompi en cliente).
- Pantallas: carrito con "Hacer pedido por WhatsApp", detalle de pedido, chat por pedido.
- Commits: 10 (5.6 h, 4.725 líneas, 1 archivo de prueba = snapshot de plantilla Expo). 14 cambios sin commit en el clon local al 2026-10-01.
- **El flujo "pedido por WhatsApp" (`cart.tsx`, `order/[id].tsx`) existe solo como cambios sin commit en el clon local**: en `HEAD` esos archivos no contienen `wa.me`. Hay que commitearlo antes de usarlo como base. También sin versionar: `fix_vendor_stores.sql`, `seed_juanshop.sql` y `juanshop_schema_v2.sql.save*`.
- `package.json` se llama `"listoshop"` (copia de ListoShop) y hay una entrada gitlink huérfana `juanshop` (directorio vacío, sin `.gitmodules`).

### listoshop (app móvil Expo con Supabase; base reutilizable)
- Mismo stack. Esquema similar a juanshop **sin** chat ni comprobantes: perfiles, tiendas, productos, pedidos, ítems, `order_events`, `delivery_evidence`, `checkout_atomic`, `advance_order_status`, `confirm_payment`.
- Filtros marca/talla/color; `eas.json` con perfiles de build/submit; `seed` de productos de muestra (calzado, perfumes, ropa).
- Commits: 15 en una sola jornada (6.9 h, 3.915 líneas, 1 archivo de prueba = plantilla).

### powerbud (aplicación web con IA y Docker; NO es una tienda)
- Plataforma de entrenamiento y nutrición: entrenador/cliente, rutinas, dieta, progreso, reseñas, notificaciones, admin.
- Backend `src/server.js` (Node 18, Express 5, `pg` PostgreSQL con Supabase, `sqlite3` legado, JWT + bcrypt, multer, Resend para correo), web estática en `public/`, `mobile-app/` (Expo 54).
- IA: `@google/genai` (Gemini) en `src/ai.js`: generación + revisión + plan de respaldo.
- Docker: `Dockerfile` (`node:18-alpine`, `npm ci --only=production`) y `docker-compose.yml` (variables por entorno).
- Commits: 57 (19.4 h, 10.276 líneas, 0 pruebas propias).

## 4. Qué se reutiliza y cómo

1. **Núcleo de tienda:** tomar el esquema + RPC de `juanshop` (stock atómico, estados, bitácora, chat, comprobantes, evidencia) como base; traer de `listoshop` los filtros marca/talla/color y los perfiles `eas.json`; traer de `ferretero` el panel de vendedor (stock bajo, dashboard).
2. **App y web:** una sola base Expo Router con exportación web estática (`app.json` ya declara `web.output: static`; **no hay evidencia de que se haya publicado una versión web** de ninguna app: validarlo antes de prometer "web" sobre la misma base; alternativa: web independiente HTML/Next consumiendo Supabase).
3. **WhatsApp:** empezar con `wa.me` prellenado (ya construido). API oficial de WhatsApp es un proyecto aparte y costo de terceros.
4. **IA:** reutilizar el patrón de `powerbud/src/ai.js` (reintentos, JSON estructurado, revisión, respaldo, revisión humana) con casos de tienda (borrador de descripciones, respuestas sugeridas). Es desarrollo nuevo; el dominio actual de PowerBud no es comercio.
5. **Contenedor:** el `Dockerfile`/`docker-compose.yml` de `powerbud` como plantilla, endurecido (ver riesgos).

## 5. Brechas y riesgos (honestos)

### Seguridad y secretos — acción recomendada antes de reutilizar código
- Este repositorio es **público**, por lo que el detalle de los hallazgos de seguridad de los repos de origen (credenciales versionadas, archivos `.env` y bases locales en git, endpoints sin autenticación o sin verificación de firma, funciones SQL que confían en identificadores enviados por el cliente) **no se documenta aquí**: se entregó al propietario por canal privado.
- Acciones genéricas antes de reutilizar cualquier código: rotar toda credencial que haya estado en git, retirarla del historial, leerla desde variables de entorno/secretos del servicio de build, verificar la firma de los webhooks de pago en servidor, derivar la identidad del comprador de la sesión autenticada (no de parámetros del cliente) y crear las transacciones de pasarela solo del lado servidor.

### Calidad y mantenibilidad
- **`powerbud` versiona `node_modules`** (1.733 archivos; ya anotado en `operacion/evidencia_produccion.csv`) e incluye un binario `.node` compilado. Limpiar con `git rm -r --cached node_modules`.
- **Sin pruebas propias:** `ferretero` (jest configurado, 0 pruebas), `powerbud` (0), `juanshop` y `listoshop` (solo el snapshot de la plantilla Expo). No hay CI en ninguno de los repos.
- `powerbud`: imagen `node:18-alpine` (Node 18 está fuera de soporte), `.dockerignore` con comentario en la misma línea que `powerbud.db` (el patrón no aplica), `docker-compose.yml` sin base de datos propia ni healthcheck, y un `README` inexistente (solo `ARCHITECTURE.md`, que describe diseño objetivo y no solo lo implementado: p. ej. suscripciones/PSE y despliegue Blue/Green **no** están en el código).
- Los cuatro repos son 4 modelos de datos casi iguales con divergencias (`juanshop` y `listoshop` tienen su propia copia del esquema). Falta consolidar un **único repo base "tienda modular"**.
- Sincronización: según `verificacion_evidencia.csv`, `ferretero` tiene 1 commit local no subido y `juanshop` 14 cambios sin commit. No usar la copia local como fuente de verdad sin reconciliar.
- Producto sin pasarela real validada: el nivel Completo no puede prometer "pago automático" hasta integrar y probar una pasarela (Wompi/ePayco) con webhook verificado.
- El ETL de WhatsApp/OCR citado en la documentación de `ferretero` no existe en el código: no ofrecer carga por foto/WhatsApp como funcionalidad.

### Comerciales
- `operacion/costos_productos.csv` tiene "Tienda online" en backlog con **33,2 h estimadas** y precio histórico bajo el piso. Las horas medidas (ferretero 8,8 h, juanshop 5,6 h, listoshop 6,9 h) son piso de actividad por commits, no horas totales; un servicio con web + app + automatizaciones + IA probablemente excede el supuesto de 33,2 h. Reestimar por nivel antes de fijar precios (decisión del propietario).
- La web pública declara "Estado" de cada sistema de referencia (prototipo/base/etc.) y no publica métricas de ventas, usuarios ni clientes.
- Dependencias de terceros que el cliente paga aparte: Supabase, hosting/dominio, Apple/Google, pasarela, WhatsApp API, API de IA.

## 6. Qué afirma la página pública y su respaldo

| Afirmación en `tiendas-online.html` | Respaldo |
|---|---|
| Descuento de stock atómico y devolución al cancelar | `juanshop_schema_v2.sql` (`checkout_atomic`, `advance_order_status`); `listoshop/supabase_schema.sql` |
| Alerta visual de stock bajo | `ferretero/app/(vendor_tabs)/my-products.tsx` |
| Precio recalculado en servidor + precio por ítem | `ferretero_checkout_rpc.sql`, `checkout_atomic` |
| Estados con bitácora | tabla `order_events` en juanshop/listoshop |
| Chat por pedido, comprobantes, evidencia de entrega | `juanshop/services/{messages,receipts,delivery}.ts` (chat y comprobantes solo juanshop) |
| Pedido por WhatsApp prellenado | `juanshop/app/(buyer_tabs)/cart.tsx`, `app/order/[id].tsx` |
| Filtros marca/talla/color | `listoshop/app/(buyer_tabs)/search.tsx`, `add_product_filters.sql` |
| Pago en simulación (Ferretero) | `ferretero/services/payment.ts`, `cart.tsx` |
| PowerBud: IA con revisión, Docker, correo, JWT, roles | `powerbud/src/ai.js`, `Dockerfile`, `mailer.js`, `auth.js` |
| App Android/iOS, EAS | `eas.json`, `app.json` de las apps |

Presentado como "a medida, según alcance" (no existe en el código): carga masiva Excel/CSV, sincronización con POS/contabilidad, listas de precios por cliente/categoría, pago confirmado automáticamente con pasarela, avisos automáticos por correo/WhatsApp, y la adaptación de la IA a tienda.

## 6b. Flujo pago → logística → entrega (sección `#flujo-entrega` de las páginas)

Cinco pasos publicados en ambas páginas, cada uno con "Base ya construida" vs "A medida, según alcance". Verificado en el código local (solo lectura); **ningún flujo completo está operando con clientes** y la web lo dice.

| Paso | Base ya construida (evidencia) | A medida (no existe en el código) |
|---|---|---|
| 1. Cliente paga | `juanshop/services/payment.ts`: modo sandbox simulado y rama Wompi en el cliente; `payment.ts` cita ePayco en comentarios pero solo implementa Wompi. Pedido con total recalculado (`checkout_atomic`). Pedido por WhatsApp con comprobante (`payment_receipts`). `listoshop` tiene `confirm_payment` en SQL | Pasarela real (Wompi/ePayco en Colombia; terceros en México) con transacción creada en servidor y webhook con firma verificada. Ningún pago real está validado de punta a punta |
| 2. Pagado → listo para despacho → logística | `advance_order_status` valida `pending_payment → paid → ready_for_dispatch → shipped → delivered` y registra `order_events`. Hoy el **vendedor** pulsa "listo para despacho" en `app/order/[id].tsx` | Paso automático a `paid` al aprobarse el pago; rol y panel de logística; cola de despachos; notificación automática a logística. Los roles son solo comprador y vendedor |
| 3. Cliente sigue su despacho | `app/order/[id].tsx`: estado + línea de tiempo desde `order_events`; el comprador confirma recepción cuando el estado es `shipped` | Avisos automáticos por correo/WhatsApp (API oficial de Meta, costo aparte) |
| 4. Conductor entrega con foto de remisión | `ferretero/app/(vendor_tabs)/order/[id].tsx`: foto con cámara (`expo-image-picker`), subida a storage y `delivered`, **desde la vista del vendedor**. `juanshop`/`listoshop`: tabla `delivery_evidence` (`photo`/`signature`/`note`, lat/lon) y `services/delivery.ts` con subida a storage, **pero ninguna pantalla importa `delivery.ts`** | Rol y app de conductor; asignación de despacho a un conductor; "remisión firmada" como `evidence_type` explícito con plantilla (hoy el CHECK solo admite photo/signature/note); captura de firma y ubicación en pantalla |
| 5. Evidencia ligada al pedido, visible a comprador y vendedor | Políticas RLS `de_select_buyer` / `de_select_vendor` sobre `delivery_evidence` (juanshop v2) | La política de inserción hoy es solo del **vendedor** (`de_insert_vendor`); el conductor requeriría nueva política/rol; mostrar la evidencia en las pantallas y en el panel de logística |

Brechas adicionales de este flujo:
- Ferretero salta la máquina de estados: actualiza `orders.status` a `delivered` directamente con `update`, sin pasar por una función con validación ni bitácora; juanshop/listoshop sí usan `advance_order_status`.
- `juanshop_schema_v2.sql` hace `DROP` de `confirm_payment` y no la recrea (solo existe en `supabase_schema.sql` antiguo y en `listoshop`): decidir una única versión.
- Las tablas y servicios de evidencia (juanshop/listoshop) no tienen UI; el bucket de evidencias está referenciado por nombre en `delivery.ts` y devuelve URL pública (revisar privacidad: remisiones con datos del cliente deberían usar URLs firmadas).
- Propuesta de modelo para lo "a medida": nuevo rol `logistics` y `driver` en `profiles.role`; tabla `dispatches` (pedido, conductor, estado) con RLS; trigger o Edge Function que, al pasar a `paid`, avance a `ready_for_dispatch` y encole el despacho; ampliar `evidence_type` con `signed_delivery_note`.
- Sin plazos publicados ni promesas de resultado; estimar horas por separado (ver sección 5, Comerciales).

## 7. Siguientes pasos propuestos

1. Atender los hallazgos de seguridad entregados por canal privado (rotación de credenciales, limpieza de historial, webhook verificado) y limpiar `node_modules` y archivos locales versionados de `powerbud`.
2. Crear un repo base "tienda modular" desde `juanshop` + filtros de `listoshop` + panel de `ferretero`, con un único esquema versionado en migraciones.
3. Añadir pruebas mínimas: SQL/RPC de checkout y transiciones de estado, y un smoke test de pantallas críticas; CI en GitHub Actions.
4. Integrar una pasarela (Wompi o ePayco) con Edge Function y verificación de firma; probar en sandbox del proveedor.
5. Validar la exportación web estática de la app (o decidir una web separada) y publicar una demo propia con datos de muestra.
6. Prototipo del módulo de IA para tienda (borrador de descripciones con revisión humana) sobre el patrón de `powerbud`, en contenedor con `node:20`/LTS.
7. Reestimar horas por nivel (incluyendo el flujo pago → logística → entrega a medida) y que el propietario apruebe precios y condiciones (propiedad del código/datos, soporte, revisiones) antes de publicar cifras. Registrar la decisión en `operacion/`.
8. Cuando haya un caso real autorizado por un cliente, sustituir "sistemas propios" por un caso con permiso y métricas verificables.

## 8. Publicación: qué sube el workflow y qué no

`.github/workflows/deploy.yml` hace `aws s3 sync . s3://… --delete` con `--exclude` de `.git/*`, `.github/*`, `*.md`, `*.py`, `*.tf`, `*.tfvars`, JSON de políticas, `node_modules/*`, `package*.json`, `tailwind.config.js`, `assets/css/input.css`, etc.

- `docs/definicion-servicio-tiendas-online.md` termina en `.md`, por lo que **no se publica**. No fue necesario cambiar el workflow.
- Lo que **sí** se publica y conviene recordar: `operacion/*.csv` (los CSV no están excluidos), `capturas_propuestas/`, `*.txt` (`image-prompts-paquetes.txt`) y `CLIENTES-Y-VENTAS.HTML`. Revisar si `operacion/` (costos, precios piso, matriz de competencia) debería excluirse con `--exclude "operacion/*"`; es un hallazgo ajeno a este cambio y no se modificó.
- `tiendas-online.html` se publica porque es `.html` y está en `sitemap.xml`.

## 9. Versión México (`mexico-tiendas-online.html`)

- Mismo contenido y diseño que `tiendas-online.html`, en español de México (`lang="es-MX"`, `og:locale es_MX`), con canonical propio y `hreflang` cruzado `es-CO` / `es-MX` / `x-default` (apunta a la versión Colombia). Selector de país discreto en el hero y en el pie.
- JSON-LD `Service` con `areaServed`: Mexico, Ciudad de México, Guadalajara y Monterrey; el contacto sigue siendo `control@reyescomputing.com` y WhatsApp +57 312 808 4929 (sin número mexicano).
- Pagos y envíos: solo "pasarela de pagos de terceros según alcance" y "paqueterías de terceros si su API permite integrarlas". No se nombran proveedores porque ninguno de los repos tiene una integración mexicana (ni mexicana alguna validada). Los sistemas de referencia se describen como desarrollados en Colombia y se aclara que sus medios de pago se adaptan para México según alcance.
- Facturación: solo "la facturación aplicable, incluido si procede un CFDI, se valida antes de contratar"; se indica que Reyes Computing S.A.S. es colombiana, sin oficinas ni entidad en México. Pendiente de validación contable/fiscal antes de ofrecer CFDI.
- Coordinación con las páginas México de la rama `feat/servicios-mexico`: se usan los mismos criterios (`es-MX`, ciudades, "atención remota"). Si se publica un selector de país global, enlazar `mexico-tiendas-online.html` desde allí.
