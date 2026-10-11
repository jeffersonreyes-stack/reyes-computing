/* ============================================================
   REYES COMPUTING - Capa de conversion (WhatsApp + medicion)
   ============================================================ */

const REYES = {
  // WhatsApp comercial: +57 312 808 4929 (formato internacional, sin + ni espacios).
  WHATSAPP_NUMERO: '573128084929',

  // ID de conversion de Google Ads. OJO: no es el numero de cliente (552-938-8450),
  // es el "ID de conversion" que aparece junto a la etiqueta en Objetivos > Conversiones.
  ADS_ID: 'AW-18025178697',

  // Etiqueta de la accion "Clic WhatsApp" (categoria Contacto).
  ADS_ETIQUETA_CONVERSION: 'J5ZoCID2qPIcEMnMiZND',

  MENSAJE_POR_DEFECTO: 'Hola Reyes Computing. Tengo una empresa en ____ y vendemos ____. Quiero conseguir clientes por Google. Mi presupuesto aproximado para web/anuncios es ____.'
};

// Servicios que pueden llegar a contacto.html?servicio=<slug>: opcion del selector y mensaje inicial.
const SERVICIOS_CONTACTO = {
  'diagnostico': { opcion: 'Diagnóstico digital gratuito', nombre: 'el diagnóstico digital gratuito' },
  'landing': { opcion: 'Sitio web de alta conversión', nombre: 'una Landing Page de Ventas' },
  'sitio-web': { opcion: 'Sitio web de alta conversión', nombre: 'un Sitio Web Empresarial' },
  'tienda-online': { opcion: 'Tienda online', nombre: 'una Tienda Online' },
  'google-ads': { opcion: 'Google Ads', nombre: 'una campaña de Google Ads de arranque' },
  'motor-clientes': { opcion: 'Google Ads', nombre: 'el Motor de Clientes (Google Ads y landing)' },
  'multicanal': { opcion: 'Social Ads B2B', nombre: 'una Estrategia Multicanal' },
  'google-business': { opcion: 'Google Business Profile', nombre: 'la optimización de mi perfil de Google Business' },
  'actualizacion-digital': { opcion: 'Actualización Digital Comercial', nombre: 'la Actualización Digital Comercial' },
  'presencia-digital': { opcion: 'Presencia digital completa', nombre: 'mejorar mi presencia digital' },
  'auditoria-express': { opcion: 'Ciberseguridad, DevSecOps y Cloud', nombre: 'la Auditoría Técnica Express' },
  'ciberseguridad': { opcion: 'Ciberseguridad, DevSecOps y Cloud', nombre: 'un servicio de ciberseguridad' },
  'devsecops': { opcion: 'Ciberseguridad, DevSecOps y Cloud', nombre: 'la Auditoría CI/CD y DevSecOps' },
  'cloud': { opcion: 'Ciberseguridad, DevSecOps y Cloud', nombre: 'Soporte Cloud On-Demand' }
};

function construirEnlaceWhatsApp(mensaje) {
  const texto = encodeURIComponent(mensaje || REYES.MENSAJE_POR_DEFECTO);
  return `https://wa.me/${REYES.WHATSAPP_NUMERO}?text=${texto}`;
}

function registrarConversion(tipo, destino) {
  if (typeof gtag !== 'function') return;

  gtag('event', 'contacto_iniciado', {
    metodo: tipo,
    pagina: window.location.pathname,
    destino: destino || ''
  });

  if (tipo === 'whatsapp' && REYES.ADS_ETIQUETA_CONVERSION) {
    gtag('event', 'conversion', { send_to: `${REYES.ADS_ID}/${REYES.ADS_ETIQUETA_CONVERSION}` });
  }
}

function activarEnlacesWhatsApp() {
  document.querySelectorAll('[data-wa], a[href^="https://wa.me/"]').forEach((enlace) => {
    if (enlace.hasAttribute('data-wa')) {
      enlace.href = construirEnlaceWhatsApp(enlace.dataset.waMsg);
    }
    enlace.target = '_blank';
    enlace.rel = 'noopener noreferrer';
    enlace.addEventListener('click', () => registrarConversion('whatsapp', enlace.dataset.waOrigen || 'cta'));
  });
}

function activarEnlacesContacto() {
  document.querySelectorAll('a[href^="contacto.html"]').forEach((enlace) => {
    enlace.addEventListener('click', () => registrarConversion('formulario', enlace.dataset.origen || 'cta'));
  });
}

function prellenarFormularioContacto() {
  const slug = new URLSearchParams((window.location && window.location.search) || '').get('servicio');
  const servicio = slug && Object.prototype.hasOwnProperty.call(SERVICIOS_CONTACTO, slug) ? SERVICIOS_CONTACTO[slug] : null;
  const form = document.getElementById('contactForm');
  const select = form && form.querySelector('select[name="service_interest"]');
  if (!servicio || !select) return;

  const opcion = Array.from(select.options).find((item) => item.value === servicio.opcion);
  if (opcion) select.value = opcion.value;

  const mensaje = form.querySelector('textarea[name="message"]');
  if (mensaje && !mensaje.value) {
    mensaje.value = `Hola, quiero una propuesta o cotización para ${servicio.nombre}. Mi empresa es ____ y vendemos ____.`;
  }

  const asunto = form.querySelector('input[name="_subject"]');
  if (asunto) asunto.value = `${asunto.value} - ${servicio.opcion}`;

  const aviso = document.getElementById('servicio-seleccionado');
  if (aviso) {
    aviso.textContent = `Solicitud seleccionada: ${servicio.nombre}. Puedes cambiarla en el formulario.`;
    aviso.classList.remove('hidden');
  }
}

function activarEnlacesTelefono() {
  document.querySelectorAll('a[href^="tel:"]').forEach((enlace) => {
    enlace.addEventListener('click', () => registrarConversion('llamada'));
  });
}

function activarFormularios() {
  document.querySelectorAll('form').forEach((form) => {
    form.addEventListener('submit', (event) => {
      queueMicrotask(() => {
        if (event.defaultPrevented || typeof gtag !== 'function') return;
        gtag('event', 'formulario_intento', {
          pagina: window.location.pathname,
          formulario: form.id || 'form'
        });
      });
    });
  });
}

const MENU_LATERAL = [
  {
    titulo: 'Servicios',
    enlaces: [
      ['fa-code', 'Desarrollo Web', 'desarrollo-web.html'],
      ['fa-store', 'Tiendas Online', 'tiendas-online.html'],
      ['fa-bullhorn', 'Google Ads', 'publicidad-web.html'],
      ['fa-location-dot', 'Google Business', 'google-business-profile.html'],
      ['fa-rocket', 'Startups & Fintech', 'startups-fintech.html'],
      ['fa-infinity', 'DevSecOps', 'devsecops-startups.html'],
      ['fa-cloud', 'Cloud On-Demand', 'infraestructura-nube-startups.html'],
      ['fa-shield-halved', 'Ciberseguridad Fintech', 'ciberseguridad-fintech.html']
    ]
  },
  {
    titulo: 'México',
    enlaces: [
      ['fa-laptop-code', 'Desarrollo web y marketing', 'mexico-desarrollo-web-marketing-digital.html'],
      ['fa-cloud-arrow-up', 'Nube y seguridad web', 'mexico-nube-seguridad-web.html'],
      ['fa-cart-shopping', 'Tiendas en línea', 'mexico-tiendas-online.html']
    ]
  },
  {
    titulo: 'Empresa',
    enlaces: [
      ['fa-tags', 'Planes & Precios', 'planes.html'],
      ['fa-fire', 'Ofertas', 'ofertas.html'],
      ['fa-trophy', 'Casos de éxito', 'casos-de-exito.html'],
      ['fa-list-check', 'Cómo funciona', 'como-funciona.html'],
      ['fa-envelope', 'Contacto', 'contacto.html']
    ]
  }
];

function construirMenuLateral() {
  const pagina = ((window.location && window.location.pathname) || '').split('/').pop() || 'index.html';
  const grupos = MENU_LATERAL.map((grupo) => {
    const enlaces = grupo.enlaces.map(([icono, texto, href]) => {
      const actual = href === pagina ? ' aria-current="page"' : '';
      return `<li><a href="${href}" class="menu-lateral-enlace"${actual}><i class="fa-solid ${icono}" aria-hidden="true"></i><span>${texto}</span></a></li>`;
    }).join('');
    return `<section class="menu-lateral-grupo"><h2>${grupo.titulo}</h2><ul>${enlaces}</ul></section>`;
  }).join('');

  return `
    <div class="menu-lateral-cabecera">
      <a href="index.html" class="menu-lateral-inicio"><i class="fa-solid fa-house" aria-hidden="true"></i><span>Inicio</span></a>
      <button type="button" class="menu-lateral-cerrar" aria-label="Cerrar menu principal"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
    </div>
    <nav class="menu-lateral-cuerpo" aria-label="Menu principal">${grupos}</nav>
    <div class="menu-lateral-pie">
      <a href="contacto.html?servicio=diagnostico" data-origen="menu-lateral" class="menu-lateral-cta"><i class="fa-solid fa-envelope" aria-hidden="true"></i> Diagnóstico Gratis</a>
      <a href="https://wa.me/${REYES.WHATSAPP_NUMERO}" data-wa data-wa-origen="menu-lateral" class="menu-lateral-wa"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> Escribir por WhatsApp</a>
    </div>`;
}

function activarMenuMovil() {
  const navegacion = document.querySelector('nav.fixed, header.fixed');
  if (!navegacion) return;

  let button = document.getElementById('mobile-menu-btn');
  if (!button) {
    button = document.createElement('button');
    button.id = 'mobile-menu-btn';
    button.className = 'text-white text-2xl';
    navegacion.firstElementChild.appendChild(button);
  }
  const anterior = document.getElementById('mobile-menu');
  if (anterior) anterior.remove();

  const fondo = document.createElement('div');
  fondo.className = 'menu-lateral-fondo';
  const panel = document.createElement('aside');
  panel.id = 'menu-lateral';
  panel.className = 'menu-lateral';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-modal', 'true');
  panel.setAttribute('aria-label', 'Menu principal');
  panel.innerHTML = construirMenuLateral();
  document.body.append(fondo, panel);

  const cerrar = panel.querySelector('.menu-lateral-cerrar');
  let abierto = false;
  const setOpen = (open) => {
    const cambio = open !== abierto;
    abierto = open;
    panel.classList.toggle('abierto', open);
    fondo.classList.toggle('abierto', open);
    panel.setAttribute('aria-hidden', String(!open));
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Cerrar menu principal' : 'Abrir menu principal');
    document.body.style.overflow = open ? 'hidden' : '';
    if (!cambio) return;
    if (open) cerrar.focus();
    else button.focus();
  };

  button.type = 'button';
  button.setAttribute('aria-controls', panel.id);
  button.innerHTML = '<i class="fa-solid fa-bars"></i>';
  setOpen(false);
  button.addEventListener('click', () => setOpen(!abierto));
  cerrar.addEventListener('click', () => setOpen(false));
  fondo.addEventListener('click', () => setOpen(false));
  panel.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setOpen(false);
  });
}

function inyectarBotonFlotante() {
  if (document.querySelector('.reyes-wa-flotante, .sticky-bar')) return;

  const boton = document.createElement('a');
  boton.className = 'reyes-wa-flotante fixed bottom-6 right-6 z-[60] flex items-center gap-3 rounded-full bg-[#25D366] px-5 py-4 font-sans text-sm font-bold text-black shadow-[0_0_25px_rgba(37,211,102,0.5)] transition hover:scale-105 hover:bg-white';
  boton.setAttribute('data-wa', '');
  boton.setAttribute('data-wa-origen', 'boton-flotante');
  boton.setAttribute('aria-label', 'Escribenos por WhatsApp');
  boton.innerHTML = '<i class="fa-brands fa-whatsapp text-2xl"></i><span class="hidden sm:inline">Escríbenos por WhatsApp</span>';

  document.body.appendChild(boton);
}

document.addEventListener('DOMContentLoaded', () => {
  if (!REYES.ADS_ETIQUETA_CONVERSION) {
    console.warn('[Reyes Computing] Falta ADS_ETIQUETA_CONVERSION en assets/js/reyes-conversion.js: los contactos no se registraran como conversion en Google Ads.');
  }

  activarMenuMovil();
  inyectarBotonFlotante();
  activarEnlacesWhatsApp();
  activarEnlacesContacto();
  activarEnlacesTelefono();
  prellenarFormularioContacto();
  activarFormularios();
});
