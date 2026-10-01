# Reyes Computing

Consultoría Cloud, FinOps y DevOps para Fintechs en Latam.

## 🛠️ Stack Técnico

- **Frontend**: HTML5 + Tailwind CSS 3.4
- **Hosting**: AWS S3 + CloudFront
- **CI/CD**: GitHub Actions
- **Fonts**: Orbitron + Inter

## 🚀 Desarrollo Local

### Instalación
```bash
npm install
```

### Desarrollo (watch mode)
```bash
npm run dev
```

### Build para producción
```bash
npm run build
```

## Validación de Contactos

Ejecutar `npm test`, `npm run build` y `python3 test_services_suite.py` antes de publicar.

La etiqueta de Google Ads existente mide clics en WhatsApp, no conversaciones ni ventas. Las llamadas generan un evento separado y los formularios válidos generan `formulario_intento`; un intento no confirma recepción. No se reutiliza la etiqueta de WhatsApp para envíos ni llamadas.

Los formularios usan FormSubmit. El propietario debe confirmar que `control@reyescomputing.com` esté activado en ese servicio y probar la recepción de un mensaje autorizado. Una conversión de formulario confirmado requiere una acción propia en Google Ads y verificación de recepción; no se inventa una etiqueta.

El aviso de datos está en `contacto.html#privacidad`. Describe los proveedores actuales, pero no sustituye una revisión legal ni configura consentimiento de cookies. Las condiciones fiscales y de facturación deben validarse antes de ofrecerlas.

Las URL recomendadas de campañas están en `google_ads_campaign_urls.md`; su configuración real en Google Ads queda fuera del código del sitio.

## Despliegue

El sitio se despliega automáticamente a AWS S3 con CloudFront cuando se hace push a `main` vía GitHub Actions.

### Proceso de Deployment

1. **Build**: GitHub Actions ejecuta `npm run build` para generar el CSS optimizado
2. **Sync**: Los archivos se sincronizan con el bucket S3
3. **Invalidación**: Se invalida el caché de CloudFront para servir la nueva versión

## 🎨 Personalización

- Colores: Ver `tailwind.config.js`
- Estilos custom: Ver `assets/css/input.css`

## 🔐 Secrets de GitHub

Para que el CI/CD funcione, se necesitan configurar los siguientes secrets en GitHub:
- `AWS_ACCESS_KEY_ID` - Credencial de AWS con permisos para S3 y CloudFront
- `AWS_SECRET_ACCESS_KEY` - Credencial secreta de AWS
- `S3_BUCKET_NAME` - Nombre del bucket S3 (ej: `reyes-computing-website`)
- `CLOUDFRONT_ID` - ID de distribución de CloudFront

Configurar en: Repositorio → Settings → Secrets and variables → Actions
