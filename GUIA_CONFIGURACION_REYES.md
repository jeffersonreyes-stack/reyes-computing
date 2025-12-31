# Guía Definitiva: Configuración de Dominio para Reyes Computing

Esta guía te explicará exactamente cómo conectar tu sitio web, Netlify, GitHub y tu dominio `reyescomputing.com` (comprado en Squarespace).

---

## Paso 1: Confirmar Conexión con GitHub

Actualmente tu código ya está en GitHub y tienes el archivo `netlify.toml` listo. Esto significa que Netlify puede "escuchar" tus cambios.

1.  Asegúrate de que los últimos cambios (incluyendo este archivo y el archivo `CNAME` que acabo de crear) estén subidos a GitHub (yo me encargo de esto al finalizar).
2.  En **Netlify**, asegúrate de que el sitio está conectado a tu repositorio `reyes-computing`. Si ya lo hiciste, salta al paso 2.

---

## Paso 2: Configurar Dominio en Netlify

1.  Inicia sesión en [Netlify](https://app.netlify.com/).
2.  Ve a tu sitio (`reyes-computing`).
3.  Haz clic en **"Domain management"** (o "Site configuration" > "Domain management").
4.  Haz clic en el botón **"Add a domain"**.
5.  Escribe: `reyescomputing.com`
6.  Haz clic en **Verify**.
7.  Haz clic en **Add domain** (Netlify te preguntará si eres el dueño, di que sí).
8.  Netlify te mostrará unas alertas de "Check DNS configuration". Esto es normal.

---

## Paso 3: Configurar DNS en Squarespace (CRUCIAL)

**IMPORTANTE:** En tu captura de pantalla vi que tienes activado "Se renueva automáticamente en Google Workspace". Esto significa que probablemente usas Gmail para correos corporativos (ej. `control@reyescomputing.com`).

Para **NO romper tu correo**, usaremos el método de "Registros A" y no el cambio de Nameservers.

### Instrucciones para Squarespace:

1.  Ve a tu [Panel de Dominios de Squarespace](https://account.squarespace.com/domains).
2.  Haz clic en tu dominio `reyescomputing.com`.
3.  En el menú lateral izquierdo (como en tu foto), haz clic en **DNS**.
4.  Busca la sección **"Registros personalizados"** (o "Custom Records").
5.  Si ves registros antiguos que apunten a otro hosting (que NO sean los de Google/GMail), bórralos. **NO borres nada que diga "MX" o "Google" o "Mail"**.

### Agrega estos 2 registros exactos:

**Registro 1 (Para el dominio raíz):**
*   **Host:** `@` (Si no te deja poner `@`, déjalo vacío).
*   **Tipo:** `A`
*   **Datos / Valor:** `75.2.60.5`
    *(Esta es la dirección IP del balanceador de carga de Netlify)*.

    > **⚠️ SOLUCIÓN AL ERROR DE CONFLICTO:**
    > Si al agregar este registro te aparece un recuadro rojo que dice:
    > *"Un registro en este ajuste predeterminado está con conflicto..."*
    >
    > **SOLUCIÓN:** Haz clic sin miedo en el botón blanco que dice **"REEMPLAZAR AJUSTE PREDETERMINADO"** (a la derecha).
    > *   Esto borrará automáticamente las IPs viejas de Squarespace (198.185...) y pondrá la nuestra de Netlify (75.2.60.5).
    > *   Esto es exactamente lo que queremos para que el sitio se vea.

**Registro 2 (Para www):**
*   **Host:** `www`
*   **Tipo:** `CNAME`
*   **Datos / Valor:** `reyes-computing.netlify.app`

    > **❓ ¿DÓNDE ENCUENTRO ESTA DIRECCIÓN?**
    > 1. Ve a tu panel principal en [Netlify](https://app.netlify.com/).
    > 2. Haz clic en tu sitio.
    > 3. Mira en la **esquina superior izquierda** de la pantalla, justo debajo del nombre de tu equipo. Verás un enlace verde que dice algo como `nombre-de-tu-sitio.netlify.app`.
    > 4. **Esa es la dirección que debes copiar y pegar aquí.**
    > 5. (Nota: Si tu sitio se llama `reyes-computing` en Netlify, entonces la dirección es `reyes-computing.netlify.app`).

---

## Paso 4: Esperar y Verificar

1.  Los cambios de DNS pueden tardar desde 10 minutos hasta 24 horas en propagarse.
2.  Netlify detectará automáticamente el cambio y emitirá un certificado SSL (HTTPS) gratuito para que tu sitio sea seguro (candadito verde).
3.  Prueba entrar a `https://reyescomputing.com`.

---

## Resumen de Archivos Agregados

*   **CNAME:** He agregado un archivo llamado `CNAME` en tu código con el valor `reyescomputing.com`. Esto ayuda a Netlify (y otros servicios) a reconocer tu dominio oficial desde el código fuente.
*   **Canonical Link:** He agregado una etiqueta en tu `index.html` para mejorar tu SEO y decirle a Google que `reyescomputing.com` es la fuente original.

¡Listo! Con esto tu imperio digital estará en línea.
