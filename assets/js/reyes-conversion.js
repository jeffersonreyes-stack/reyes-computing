/* ============================================================
   REYES COMPUTING - Capa de conversion (WhatsApp + medicion)
   ============================================================ */

const REYES = {
  // WhatsApp comercial: +57 333 070 0828 (formato internacional, sin + ni espacios).
  WHATSAPP_NUMERO: '573330700828',

  // ID de conversion de Google Ads. OJO: no es el numero de cliente (552-938-8450),
  // es el "ID de conversion" que aparece junto a la etiqueta en Objetivos > Conversiones.
  ADS_ID: 'AW-18025178697',

  // Etiqueta de la accion "Clic WhatsApp" (categoria Contacto).
  ADS_ETIQUETA_CONVERSION: 'J5ZoCID2qPIcEMnMiZND',

  MENSAJE_POR_DEFECTO: 'Hola Reyes Computing, quiero mi Diagnostico Digital gratis de 24 horas.'
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

  if (REYES.ADS_ETIQUETA_CONVERSION) {
    gtag('event', 'conversion', { send_to: `${REYES.ADS_ID}/${REYES.ADS_ETIQUETA_CONVERSION}` });
  }
}

function activarEnlacesWhatsApp() {
  document.querySelectorAll('[data-wa]').forEach((enlace) => {
    enlace.href = construirEnlaceWhatsApp(enlace.dataset.waMsg);
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
    form.addEventListener('submit', () => registrarConversion('formulario', form.id || 'form'));
  });
}

function inyectarBotonFlotante() {
  if (document.querySelector('.reyes-wa-flotante')) return;

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

  inyectarBotonFlotante();
  activarEnlacesWhatsApp();
  activarEnlacesTelefono();
  activarFormularios();
});
