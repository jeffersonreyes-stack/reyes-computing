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

function activarMenuMovil() {
  let button = document.getElementById('mobile-menu-btn');
  if (!button) {
    const navigation = document.querySelector('nav.fixed, header.fixed');
    if (!navigation) return;
    button = document.createElement('button');
    button.id = 'mobile-menu-btn';
    button.className = 'xl:hidden text-white text-2xl';
    navigation.firstElementChild.appendChild(button);
  }
  let menu = document.getElementById('mobile-menu');
  if (!menu) {
    menu = document.createElement('div');
    menu.id = 'mobile-menu';
    menu.className = 'fixed inset-0 bg-black/95 z-40 hidden flex flex-col justify-center items-center gap-6 px-6 pt-24 pb-6 overflow-y-auto';
    button.closest('nav, header').querySelectorAll('a').forEach((link) => {
      if (link.querySelector('img')) return;
      const item = link.cloneNode(true);
      item.className = 'mobile-link text-lg text-white text-center';
      menu.appendChild(item);
    });
    document.body.appendChild(menu);
  }
  const setOpen = (open) => {
    menu.classList.toggle('hidden', !open);
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Cerrar menu principal' : 'Abrir menu principal');
    document.body.style.overflow = open ? 'hidden' : '';
    button.innerHTML = open ? '<i class="fa-solid fa-times"></i>' : '<i class="fa-solid fa-bars"></i>';
  };
  button.type = 'button';
  button.setAttribute('aria-controls', menu.id);
  setOpen(false);
  button.addEventListener('click', () => setOpen(menu.classList.contains('hidden')));
  menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setOpen(false);
  });
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1280) setOpen(false);
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
  activarEnlacesTelefono();
  activarFormularios();
});
