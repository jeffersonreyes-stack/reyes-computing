# Campañas de Google Ads — Índice

Documentación interna (no se publica en el sitio). Contiene las instrucciones para montar las campañas de Búsqueda de Reyes Computing.

| Archivo | Contenido |
|---|---|
| [google-ads-mexico.md](google-ads-mexico.md) | Campaña **México**: 3 grupos de anuncios y **3 anuncios en total** (1: desarrollo web y marketing digital; 2: nube y seguridad web, contexto fintech; 3: tiendas en línea México) |
| [google-ads-tiendas-online.md](google-ads-tiendas-online.md) | Campaña **Tiendas Online Colombia**: 3 grupos y **3 anuncios en total** (tienda web + app; automatización; IA) |
| [../google_ads_campaign_urls.md](../google_ads_campaign_urls.md) | URL finales recomendadas de todas las campañas |

En total son **6 anuncios** (3 México + 3 Colombia).

## Prerrequisitos (antes de lanzar cualquiera)

1. **Landings publicadas** (PR fusionados y desplegados; comprobar que cada URL responde 200):
   - https://www.reyescomputing.com/mexico-desarrollo-web-marketing-digital.html
   - https://www.reyescomputing.com/mexico-nube-seguridad-web.html
   - https://www.reyescomputing.com/mexico-tiendas-online.html
   - https://www.reyescomputing.com/tiendas-online.html
   - https://www.reyescomputing.com/ofertas.html y https://www.reyescomputing.com/contacto.html (sitelinks)
2. **Medición:** crear la acción de conversión propia del formulario en Google Ads, instalar su etiqueta en `success.html` y verificar con Tag Assistant. «Clic WhatsApp» mide clics, no conversaciones.
3. **El dueño define:** presupuesto diario, CPC máximo, N conversiones para cambiar de puja, horario y ciudades (México: CDMX, Guadalajara, Monterrey; Colombia: Cali, Bogotá, Medellín).
4. Facturación de Google Ads activa y alguien disponible para responder WhatsApp.

## Orden de lanzamiento sugerido

1. **Campaña México** (`google-ads-mexico.md`): sirve para validar la medición. Si alguna landing mexicana aún no está publicada, deja pausado su grupo de anuncios (el grupo B, nube y seguridad, requiere más cuidado de políticas).
2. **Campaña Tiendas Online Colombia** (`google-ads-tiendas-online.md`): servicio nuevo.

Lanza una a la vez, con unos días de diferencia, para aislar problemas de aprobación o medición. Cada archivo incluye su checklist y qué revisar a los 7, 14 y 30 días.

## Reglas comunes de copy

Sin garantías, superlativos, «#1» ni promesas de resultados; sin precios ni descuentos inventados; atención remota explícita en México (sin oficina en México); en fintech, sin afirmar cumplimiento ni certificaciones.
