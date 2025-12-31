# Guía Definitiva: Configuración de Dominio para Reyes Computing

Esta guía está personalizada para tu configuración actual. Sigue estos pasos exactos para conectar tu dominio `reyescomputing.com` (Squarespace) a tu sitio web.

---

## Paso 0: Renombrar tu Sitio en Netlify (Para evitar confusiones)

Para que no tengas que buscar direcciones extrañas, vamos a ponerle un nombre fácil a tu sitio.

1.  Inicia sesión en [Netlify](https://app.netlify.com/).
2.  Entra a tu sitio actual (el que tiene el nombre raro).
3.  Ve a **"Site configuration"** (Configuración del sitio).
4.  Haz clic en el botón **"Change site name"**.
5.  Escribe exactamente: `reyes-computing`
    *   *(Si te dice que ya está tomado, prueba con `reyescomputing-web` o `reyes-computing-cloud`).*
6.  Guarda los cambios.
    *   **IMPORTANTE:** Ahora tu dirección segura será: `https://reyes-computing.netlify.app` (o el nombre que hayas elegido).

---

## Paso 1: Configurar DNS en Squarespace

Viendo tu captura de pantalla, ya estás en el lugar correcto.

1.  En esa pantalla de **Squarespace Dominios**, haz clic sobre la fila que dice **`reyescomputing.com`** (donde está el logo verde de "Activo").
2.  En el menú lateral izquierdo que aparecerá, haz clic en **DNS**.
3.  Busca la sección llamada **"Registros personalizados"** (o "Custom Records").
    *   *Nota: Si ves registros antiguos que no sean de Google/Gmail, bórralos.*

### Agrega estos 2 registros exactos:

**Registro 1 (Para que funcione sin www):**
*   **Host:** `@`
*   **Tipo:** `A`
*   **Datos / Valor:** `75.2.60.5`
    *   *(Si Squarespace te muestra un error rojo de "Conflicto", haz clic en el botón **"REEMPLAZAR AJUSTE PREDETERMINADO"**).*

**Registro 2 (Para que funcione con www):**
*   **Host:** `www`
*   **Tipo:** `CNAME`
*   **Datos / Valor:** `reyes-computing.netlify.app`
    *   *(Asegúrate de poner aquí el nombre que elegiste en el Paso 0 + .netlify.app).*

---

## Paso 2: Conectar el Dominio en Netlify

Ahora volvemos a Netlify para decirle que el dominio es tuyo.

1.  Ve a tu sitio en Netlify (`reyes-computing`).
2.  Haz clic en **"Domain management"** en el menú izquierdo.
3.  Haz clic en **"Add a domain"**.
4.  Escribe: `reyescomputing.com`
5.  Haz clic en **Verify** y luego en **Add domain**.

---

## Paso 3: Esperar el Certificado de Seguridad (HTTPS)

1.  Al principio podría decir "Waiting on DNS propagation". Es normal.
2.  Espera unos minutos (o hasta 1 hora).
3.  Netlify activará automáticamente el candadito verde (SSL) para tu sitio.

---

## Resumen Final

Una vez hechos estos pasos, tu sitio será accesible en:
*   `https://reyescomputing.com`
*   `https://www.reyescomputing.com`

¡Avísame cuando hayas completado el Paso 1 para verificarlo desde aquí!
