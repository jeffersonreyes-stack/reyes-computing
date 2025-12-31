# Guía de Publicación en Netlify para Reyes Computing

Esta guía te explicará paso a paso cómo publicar tu sitio web en Netlify. Hemos configurado el proyecto para que sea compatible con Netlify Forms, por lo que recibirás los mensajes de contacto directamente en tu panel de administración.

---

## Opción 1: Despliegue Automático (Recomendado)

Esta es la forma profesional de hacerlo. Cada vez que guardes cambios en tu código (en GitHub/GitLab), Netlify actualizará tu sitio automáticamente.

### Pasos:

1.  **Sube tu código a GitHub/GitLab/Bitbucket** (si aún no lo has hecho).
2.  Inicia sesión en [Netlify](https://app.netlify.com/).
3.  En tu panel (Team Overview), haz clic en el botón **"Add new site"** > **"Import an existing project"**.
4.  Selecciona tu proveedor de Git (ej. **GitHub**).
5.  Busca y selecciona el repositorio de `reyes-computing`.
6.  Netlify detectará automáticamente la configuración gracias al archivo `netlify.toml` que hemos creado.
    *   **Build command:** (Déjalo vacío)
    *   **Publish directory:** `.` (Punto)
7.  Haz clic en **"Deploy site"**.

¡Listo! En unos segundos tu sitio estará en vivo. Netlify te dará una URL (ej. `reyes-computing.netlify.app`) que podrás cambiar después por tu dominio propio.

---

## Opción 2: Despliegue Manual (Drag & Drop)

Esta opción es útil si no quieres usar Git o solo quieres hacer una prueba rápida.

### Pasos:

1.  Asegúrate de tener todos los archivos del proyecto en una carpeta en tu computadora (`index.html`, `success.html`, `netlify.toml`, carpetas `css` y `js`).
2.  Inicia sesión en [Netlify](https://app.netlify.com/).
3.  Ve a la sección **"Sites"**.
4.  Al final de la lista de sitios, verás un recuadro con líneas discontinuas que dice **"Drag and drop your site output folder here"**.
5.  Arrastra tu carpeta del proyecto y suéltala ahí.

Netlify subirá los archivos y publicará el sitio instantáneamente.

---

## Gestión de Formularios (Netlify Forms)

Tu sitio está configurado para usar **Netlify Forms**. No necesitas servicios externos.

1.  Cuando alguien llene el formulario de contacto, Netlify capturará los datos.
2.  Para ver los mensajes:
    *   Ve a tu sitio en el panel de Netlify.
    *   Haz clic en la pestaña **"Forms"** en el menú superior o lateral.
    *   Verás una lista de "Active forms" (debería aparecer uno llamado `contact`).
    *   Haz clic en él para ver todos los mensajes recibidos.

**Tip:** En la configuración del sitio (*Site configuration > Forms*), puedes activar notificaciones por correo electrónico para que te avisen cada vez que recibas un nuevo mensaje.

---

## Dominio Personalizado

Si compraste un dominio (ej. `reyescomputing.com`), puedes conectarlo fácilmente:

1.  Ve a **"Domain management"** en el panel de tu sitio.
2.  Haz clic en **"Add a domain"**.
3.  Escribe tu dominio y sigue las instrucciones para configurar los DNS.
