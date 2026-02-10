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

## 📦 Deployment

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
