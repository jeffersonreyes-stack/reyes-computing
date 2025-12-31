# Guía: Activar Correos de Formularios

Para que los mensajes que envían tus clientes lleguen directamente a tu correo (`control@reyescomputing.com`), debes activar una pequeña configuración en Netlify.

### Pasos a seguir:

1.  **Entra a Netlify:**
    *   Ve a [https://app.netlify.com/](https://app.netlify.com/) e inicia sesión.

2.  **Selecciona tu sitio:**
    *   Haz clic en tu sitio (que ahora debería llamarse `reyes-computing` o similar).

3.  **Ve a la sección de Formularios:**
    *   En el menú de la izquierda (o arriba), busca donde dice **"Forms"**.
    *   Aquí verás una lista de todos los mensajes que han llegado (si ya has probado el formulario).

4.  **Activar Notificaciones:**
    *   Ve a **"Site configuration"** (Configuración del sitio) en el menú lateral.
    *   En la lista de opciones de la izquierda, busca **"Notifications"** (Notificaciones).
    *   Haz clic en el botón que dice **"Add notification"**.
    *   Selecciona **"Email notification"**.

5.  **Configurar el Correo:**
    *   **Event:** Déjalo en "New form submission".
    *   **Email to notify:** Escribe `control@reyescomputing.com`
    *   **Form:** Déjalo en "Any form" (o selecciona "contact" si te deja).
    *   Haz clic en **Save**.

¡Listo! Ahora cada vez que alguien llene el formulario en tu web, te llegará una alerta inmediata a tu correo corporativo.

---

### Nota sobre el Anti-Spam
He actualizado el código de tu sitio web para incluir un "campo trampa" (Honeypot). Los robots de spam llenarán este campo invisible y Netlify los bloqueará automáticamente, manteniendo tu bandeja de entrada limpia.
