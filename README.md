# Reyes Computing

Consultoría Cloud, FinOps y DevOps para Fintechs en Latam.

## 🛠️ Stack Técnico

- **Frontend**: HTML5 + Tailwind CSS 3.4
- **Hosting**: Netlify
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

El sitio se despliega automáticamente a Netlify cuando se hace push a `main` vía GitHub Actions.

## 🎨 Personalización

- Colores: Ver `tailwind.config.js`
- Estilos custom: Ver `assets/css/input.css`

## 🔐 Secrets de GitHub

Para que el CI/CD funcione, se necesitan configurar los siguientes secrets en GitHub:
- `NETLIFY_AUTH_TOKEN` (obtener de Netlify)
- `NETLIFY_SITE_ID` (obtener de Netlify)

Configurar en: Repositorio → Settings → Secrets and variables → Actions
