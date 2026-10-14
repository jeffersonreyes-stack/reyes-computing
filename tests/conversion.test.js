const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '../assets/js/reyes-conversion.js'), 'utf8');

function createContext(elements = []) {
  const events = [];
  const pending = [];
  const context = vm.createContext({
    console,
    window: { location: { pathname: '/contacto.html' } },
    document: { addEventListener() {}, querySelectorAll: () => elements },
    gtag: (...args) => events.push(args),
    queueMicrotask: (callback) => pending.push(callback)
  });
  vm.runInContext(source, context);
  return { context, events, flush: () => pending.splice(0).forEach((callback) => callback()) };
}

test('only WhatsApp clicks use the WhatsApp conversion label', () => {
  const { context, events } = createContext();
  vm.runInContext("registrarConversion('llamada'); registrarConversion('formulario'); registrarConversion('whatsapp');", context);
  assert.equal(events.filter((event) => event[1] === 'conversion').length, 1);
});

test('cancelled forms do not produce events, including later validation', () => {
  let handler;
  const { context, events, flush } = createContext([{ id: 'contactForm', addEventListener: (_, callback) => { handler = callback; } }]);
  vm.runInContext('activarFormularios()', context);
  const event = { defaultPrevented: false };
  handler(event);
  event.defaultPrevented = true;
  flush();
  assert.equal(events.length, 0);
});

test('valid submission is an attempt, not a confirmed lead or Ads conversion', () => {
  let handler;
  const { context, events, flush } = createContext([{ id: 'contactForm', addEventListener: (_, callback) => { handler = callback; } }]);
  vm.runInContext('activarFormularios()', context);
  handler({ defaultPrevented: false });
  flush();
  assert.equal(events.length, 1);
  assert.equal(events[0][1], 'formulario_intento');
});

test('direct WhatsApp links retain their message and are tracked', () => {
  let handler;
  const link = { href: 'https://wa.me/573128084929?text=Oferta', dataset: {}, hasAttribute: () => false, addEventListener: (_, callback) => { handler = callback; } };
  const { context, events } = createContext([link]);
  vm.runInContext('activarEnlacesWhatsApp()', context);
  handler();
  assert.equal(link.href, 'https://wa.me/573128084929?text=Oferta');
  assert.equal(events.filter((event) => event[1] === 'conversion').length, 1);
});

const root = path.join(__dirname, '..');
const htmlFiles = fs.readdirSync(root).filter((file) => /\.html$/i.test(file));

test('all pages have unique IDs and a mobile viewport', () => {
  for (const file of htmlFiles) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
    assert.equal(new Set(ids).size, ids.length, file);
    assert.match(html, /name="viewport"/, file);
  }
});

test('corporate pages load shared contact and menu behavior', () => {
  for (const file of htmlFiles.filter((file) => !file.startsWith('mockup-'))) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /src="assets\/js\/reyes-conversion\.js"/, file);
    assert.doesNotMatch(html, /getElementById\('mobile-menu-btn'\)/, file);
  }
});

test('Google Business audit submits named contact fields to the delivery service', () => {
  const html = fs.readFileSync(path.join(root, 'google-business-profile.html'), 'utf8');
  assert.match(html, /action="https:\/\/formsubmit\.co\/control@reyescomputing\.com" method="POST"/);
  for (const field of ['name', 'phone', 'google_business', '_next']) {
    assert.ok(html.includes(`name="${field}"`), field);
  }
});

test('all contact forms remain connected to FormSubmit', () => {
  const formPages = [
    'ciberseguridad-fintech.html',
    'ciberseguridad-ia-cali.html',
    'contacto.html',
    'devsecops-startups.html',
    'google-business-profile.html',
    'infraestructura-nube-startups.html',
    'mexico-desarrollo-web-marketing-digital.html',
    'mexico-nube-seguridad-web.html',
    'startups-fintech.html'
  ];
  for (const file of formPages) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /<form\b[^>]*action="https:\/\/formsubmit\.co\/control@reyescomputing\.com"[^>]*method="POST"/i, file);
  }
  for (const file of ['mexico-desarrollo-web-marketing-digital.html', 'mexico-nube-seguridad-web.html']) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /name="_honey"/, file);
    assert.match(html, /class="cf-turnstile/, file);
    assert.match(html, /name="_next" value="https:\/\/www\.reyescomputing\.com\/success[\w-]*\.html"/, file);
  }
});

test('every FormSubmit form posts to the corporate address with a redirect and honeypot', () => {
  for (const file of htmlFiles) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    const forms = [...html.matchAll(/<form\b[^>]*>/gi)].map((match) => match[0]).filter((tag) => /formsubmit\.co/.test(tag));
    for (const tag of forms) {
      assert.match(tag, /action="https:\/\/formsubmit\.co\/control@reyescomputing\.com"/, file);
      assert.match(tag, /method="POST"/i, file);
    }
    if (forms.length) {
      const next = html.match(/name="_next" value="https:\/\/www\.reyescomputing\.com\/(success[\w-]*\.html)"/)?.[1];
      assert.ok(next && fs.existsSync(path.join(root, next)), `${file}: _next must point to an existing success page`);
      assert.match(html, /name="_honey"/, file);
    }
  }
});

const storePages = [
  { file: 'tiendas-online.html', lang: 'es', country: 'Colombia', canonical: 'https://www.reyescomputing.com/tiendas-online.html' },
  { file: 'mexico-tiendas-online.html', lang: 'es-MX', country: 'México', canonical: 'https://www.reyescomputing.com/mexico-tiendas-online.html' }
];

function readStorePage(file) {
  const html = fs.readFileSync(path.join(root, file), 'utf8');
  const visible = html
    .replace(/<script\b[\s\S]*?<\/script>/gi, '')
    .replace(/<meta\b[^>]*>/gi, '')
    .replace(/\bhref="[^"]*"/g, '');
  return { html, visible };
}

test('Tiendas Online pages are published, cross-linked and have a valid contact form', () => {
  const sitemap = fs.readFileSync(path.join(root, 'sitemap.xml'), 'utf8');
  for (const { file, lang, canonical } of storePages) {
    const { html } = readStorePage(file);
    assert.match(html, new RegExp(`<html lang="${lang}"`), file);
    assert.ok(html.includes(`<link rel="canonical" href="${canonical}">`), file);
    assert.match(html, /<link rel="alternate" hreflang="es-CO" href="https:\/\/www\.reyescomputing\.com\/tiendas-online\.html">/, file);
    assert.match(html, /<link rel="alternate" hreflang="es-MX" href="https:\/\/www\.reyescomputing\.com\/mexico-tiendas-online\.html">/, file);
    assert.match(html, /<link rel="alternate" hreflang="x-default"/, file);
    assert.match(html, /"@type": "Service"/, file);
    assert.match(html, /"@type": "FAQPage"/, file);
    assert.ok(sitemap.includes(`<loc>${canonical}</loc>`), file);

    const forms = [...html.matchAll(/<form\b[^>]*>/gi)].map((match) => match[0]);
    assert.equal(forms.length, 1, file);
    assert.match(forms[0], /id="tiendaForm"/, file);
    assert.match(forms[0], /action="https:\/\/formsubmit\.co\/control@reyescomputing\.com"[^>]*method="POST"/i, file);
    for (const field of ['name', 'email', 'phone', 'message', 'package', 'catalog_size', '_subject', '_next', '_honey']) {
      assert.ok(html.includes(`name="${field}"`), `${file}: ${field}`);
    }
    assert.match(html, /https:\/\/wa\.me\/573128084929\?text=/, file);
    assert.match(html, /<p id="selector-pais"/, file);
  }
  assert.match(readStorePage('tiendas-online.html').html, /href="mexico-tiendas-online\.html"/);
  assert.match(readStorePage('mexico-tiendas-online.html').html, /href="tiendas-online\.html"/);
  for (const file of ['index.html', 'sistemas-de-ventas.html', 'caso-ferretero.html']) {
    assert.match(fs.readFileSync(path.join(root, file), 'utf8'), /href="tiendas-online\.html"/, file);
  }
});

test('Tiendas Online pages only publish prices supported in the master file and avoid unverified claims', () => {
  const masterContent = fs.readFileSync(path.join(root, 'master_productos_tiendas_online.md'), 'utf8');

  for (const { file } of storePages) {
    const { visible } = readStorePage(file);

    if (file === 'tiendas-online.html') {
      // Precios oficiales de combos respaldados en el documento maestro
      const supportedComboPrices = ['$5.640.000', '$8.580.000', '$13.370.000'];
      for (const price of supportedComboPrices) {
        assert.ok(masterContent.includes(price), `Master file missing price: ${price}`);
        assert.ok(visible.includes(price), `${file} debe mostrar el precio soportado: ${price}`);
      }
      // Cualquier precio publicado debe pertenecer exclusivamente a la lista soportada
      const foundPrices = visible.match(/\$\s?[\d.]+/g) || [];
      for (const fp of foundPrices) {
        const cleanPrice = fp.replace(/\s/, '');
        assert.ok(supportedComboPrices.includes(cleanPrice), `${file} contiene un precio no soportado: ${cleanPrice}`);
      }
    } else {
      // Las páginas de otros mercados (ej. México) se mantienen a cotización personalizada sin precios
      assert.doesNotMatch(visible, /\$\s?\d|\b(?:COP|USD|MXN|MX\$)\s?\d|\d\s?(?:COP|USD|MXN)\b|\bpesos?\b/i, file);
      assert.match(visible, /Cotización/, file);
    }

    assert.doesNotMatch(visible, /\d\s?%|\bOFF\b|\bpromo(?:ci[oó]n)?\b|\bdescuentos? (?!de stock)(?:de|del|especial|por)\b/i, file);
    assert.doesNotMatch(visible, /24\s?\/\s?7|garantizamos|garant[ií]a de|\bROI\b|retorno de inversi[oó]n|certificad[oa] por|homologad/i, file);
    assert.match(visible, /fotos, videos/i, file);
    assert.match(visible, /aparte/i, file);
    assert.match(visible, /volumen de imágenes superior al acordado/i, file);
    assert.match(visible, /no incluye certificación ni homologación de terceros/, file);
    assert.match(visible, /Comisiones de pasarelas de pago, (?:paqueterías y envíos, )?dominio y hosting/, file);
  }
});

test('Tiendas Online pages show the payment-to-delivery flow with built vs custom scope', () => {
  for (const { file } of storePages) {
    const { html, visible } = readStorePage(file);
    const section = html.match(/<section id="flujo-entrega"[\s\S]*?<\/section>/)?.[0];
    assert.ok(section, `${file}: missing #flujo-entrega`);
    assert.match(section, /Del pago a la entrega|DEL PAGO A LA ENTREGA/i, file);
    assert.equal((section.match(/PASO [1-6]/g) || []).length, 6, file);
    assert.ok((section.match(/Base ya construida/g) || []).length >= 6, file);
    assert.ok((section.match(/A (?:la )?medida, según alcance/g) || []).length >= 6, file);
    for (const term of [/remisi[oó]n/i, /conductor/i, /log[ií]stica/i, /a[uú]n no existen|Hoy los roles|roles actuales/i]) {
      assert.match(visible, term, `${file}: ${term}`);
    }
    assert.match(visible, /no presentamos este flujo como operando con clientes/, file);
    assert.match(html, /remisión firmada como tipo de evidencia explícito/, file);
    assert.match(html, /&copy; 2026 Reyes Computing S\.A\.S\./, file);
    assert.doesNotMatch(html, /&copy; 2025/, file);
  }
});

test('Colombian Tiendas Online page only mentions Mexico in the country selector', () => {
  const { visible } = readStorePage('tiendas-online.html');
  assert.doesNotMatch(visible.replace(/<p id="selector-pais"[\s\S]*?<\/p>/, ''), /M[eé]xico|MXN|CFDI/i);
});

test('Mexico Tiendas Online page is remote, Colombian-contact and only promises CFDI validation', () => {
  const { html, visible } = readStorePage('mexico-tiendas-online.html');
  for (const city of ['Ciudad de México', 'Guadalajara', 'Monterrey']) {
    assert.ok(html.includes(`{ "@type": "City", "name": "${city}" }`), city);
  }
  assert.match(html, /"@type": "Country", "name": "Mexico"/);
  assert.match(html, /<meta property="og:locale" content="es_MX">/);
  assert.match(visible, /La facturación aplicable, incluido si procede un CFDI, se valida antes de contratar/);
  assert.match(visible, /no tenemos oficinas en México/i);
  assert.match(visible, /empresa colombiana/);
  assert.match(visible, /pasarela de pagos de terceros/);
  assert.doesNotMatch(html, /\+52|\b52\s?55\b|\(55\)|tel:/);
  assert.doesNotMatch(visible, /integrad[oa]s? con (?:Mercado ?Pago|Conekta|Stripe|OXXO|SPEI|Estafeta|DHL|FedEx|Redpack)|SAT\b.*certific/i);
});

test('technical landings do not include unrelated web promotions or conflicting cloud prices', () => {
  for (const file of ['startups-fintech.html', 'devsecops-startups.html', 'infraestructura-nube-startups.html', 'ciberseguridad-fintech.html']) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.doesNotMatch(html, /TABLA 1:|450 USD|\$599\.000/);
  }
});

test('technical landings do not promise human 24/7 coverage or third-party certification', () => {
  const technicalFiles = ['startups-fintech.html', 'devsecops-startups.html', 'infraestructura-nube-startups.html', 'ciberseguridad-fintech.html'];
  for (const file of technicalFiles) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.doesNotMatch(html, /Monitoreo (?:continuo )?24\/7|Homologación SPEI|Compliance Bancario|\$3,500|nóminas de \$6,000|Elimina caídas|reporte en 24 horas|Proyecto 2 Semanas|Entrega 5 Días|Despliegues Zero-Downtime/);
    assert.match(html, /Monitoreo automatizado continuo/);
    assert.match(html, /no incluye certificación ni homologación de terceros/);
    assert.doesNotMatch(html, /\$600|\$1,500|\$1,200/);
  }

  const allSecurityHtml = [...technicalFiles, 'ciberseguridad-ia-cali.html']
    .map(file => fs.readFileSync(path.join(root, file), 'utf8'))
    .join('\n');
  assert.doesNotMatch(allSecurityHtml, /maximizar el flujo de caja|exclusión de IVA|\+52%|garantizando la privacidad/);
  assert.doesNotMatch(allSecurityHtml, /Supera auditorías|certifica tu infraestructura|CIERRA CONTRATOS CON BANCOS|Certificado formal firmado/);
});

test('Ads offers separate media budget and avoid unverified ROI or click-fraud claims', () => {
  const adsHtml = fs.readFileSync(path.join(root, 'publicidad-web.html'), 'utf8');
  const homeHtml = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
  assert.doesNotMatch(adsHtml, /Medición Exacta de ROI|exactamente cuánto|Reporte mensual de Retorno de Inversión|Protección anti-fraude de clics/);
  assert.match(adsHtml, /La pauta se paga directamente a Google Ads/);
  assert.doesNotMatch(homeHtml, /PROMO 50% OFF|Aprovechar Promo 50%|Incluye anuncios y optimización en Google|Contratar Motor/);
  assert.match(homeHtml, /presupuesto pagado a Google Ads/);
});

test('commercial pages avoid unapproved prices, fictitious discounts and currency conversions', () => {
  const commercialFiles = ['index.html', 'planes.html', 'desarrollo-web.html', 'clientes-y-ventas.html', 'google-business-profile.html', 'publicidad-web.html', 'oferta-actualizacion-digital.html'];
  for (const file of commercialFiles) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.doesNotMatch(html, /PROMO 50%|Promo 50%|50% OFF|COP \/ \$\d+ USD|~[\d,.]+ MXN/);
    assert.doesNotMatch(html, /\$599\.000|\$1\.350\.000|\$2\.200\.000|\$790\.000|\$450\.000|\$890\.000|\$1\.600\.000/);
    assert.doesNotMatch(html, /Entrega en \d|Precios claros|Precios Claros|Google Business verificada/);
  }

  for (const file of ['startups-fintech.html', 'devsecops-startups.html', 'infraestructura-nube-startups.html', 'ciberseguridad-fintech.html']) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.doesNotMatch(html, /MXN \/ ~\$[\d.]+ COP/);
  }
});

test('web offers do not guarantee performance outcomes', () => {
  const html = fs.readFileSync(path.join(root, 'desarrollo-web.html'), 'utf8');
  assert.doesNotMatch(html, /garantizar tiempos de carga|cliente se va a la competencia/);
  assert.match(html, /depende también del hosting, el dispositivo y la conexión/);
});
test('web offers state that client supplies media and visual production is billed separately', () => {
  for (const file of ['index.html', 'planes.html', 'desarrollo-web.html', 'clientes-y-ventas.html']) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /fotos, videos/i, file);
    assert.match(html, /aparte/i, file);
    assert.match(html, /volumen de imágenes superior al acordado/i, file);
  }
});

test('plans do not include corporate email and offer it only as a distinctly named product', () => {
  const planPages = ['index.html', 'planes.html', 'desarrollo-web.html', 'clientes-y-ventas.html', 'oferta-actualizacion-digital.html'];
  for (const file of planPages) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.doesNotMatch(html, /Correos? corporativos? (@|con |, dominio)/i, file);
  }
  for (const file of ['index.html', 'planes.html', 'desarrollo-web.html', 'clientes-y-ventas.html']) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /no est\u00e1 incluido en los paquetes/i, file);
    assert.match(html, /Google Workspace/, file);
  }
  for (const file of ['index.html', 'planes.html']) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /Landing con Correo Corporativo|Sitio Web con Correo Corporativo/, file);
    const correoParagraph = html.match(/<span class="text-reyes-cyan font-bold">Correo corporativo:<\/span>[^<]*(?:<[^\/][^>]*>[^<]*<\/[^>]*>)*[^<]*/i)?.[0] || '';
    assert.doesNotMatch(correoParagraph, /Combo Digital/, `${file}: el parrafo de correo no debe reutilizar el nombre del combo de servicios existente`);
  }
});

const mexicoPages = ['mexico-desarrollo-web-marketing-digital.html', 'mexico-nube-seguridad-web.html'];

test('Mexico content lives only in the dedicated mexico-* pages', () => {
  const mexicoTerms = /m[ée]xico|CDMX|\bMXN\b|\bCFDI\b|\bSPEI\b|CNBV|Guadalajara|Monterrey|Conekta|🇲🇽/i;
  const satTerm = /\bSAT\b/;
  // tiendas-online.html solo enlaza a su versión mexicana (selector de país y hreflang);
  // index.html solo la enlaza desde el banner de tiendas online
  for (const file of htmlFiles.filter((file) => !file.startsWith('mexico-') && file !== 'tiendas-online.html')) {
    let html = fs.readFileSync(path.join(root, file), 'utf8');
    if (file === 'index.html') html = html.replace(/<a href="mexico-tiendas-online\.html"[^>]*>México<\/a>/, '');
    assert.doesNotMatch(html, mexicoTerms, file);
    assert.doesNotMatch(html, satTerm, file);
  }
  const sitemap = fs.readFileSync(path.join(root, 'sitemap.xml'), 'utf8');
  for (const file of mexicoPages) {
    assert.ok(sitemap.includes(`<loc>https://www.reyescomputing.com/${file}</loc>`), file);
  }
});

test('Mexico pages have es-MX SEO, structured data and honest remote-service positioning', () => {
  for (const file of mexicoPages) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /<html lang="es-MX"/, file);
    assert.ok(html.includes(`<link rel="canonical" href="https://www.reyescomputing.com/${file}">`), file);
    assert.ok(html.includes(`hreflang="es-MX" href="https://www.reyescomputing.com/${file}"`), file);
    assert.match(html, /property="og:title"/, file);
    assert.match(html, /src="assets\/js\/reyes-conversion\.js"/, file);
    assert.match(html, /https:\/\/wa\.me\/573128084929/, file);
    assert.doesNotMatch(html, /wa\.me\/52|\+52/, file);

    const jsonLd = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)].map((match) => JSON.parse(match[1]));
    assert.ok(jsonLd.length >= 1, file);
    const serialized = JSON.stringify(jsonLd);
    for (const place of ['Mexico', 'Ciudad de México', 'Guadalajara', 'Monterrey']) {
      assert.ok(serialized.includes(place), `${file}: ${place}`);
    }
    assert.ok(serialized.includes('FAQPage'), file);

    assert.match(html, /atención remota a empresas en México/i, file);
    assert.match(html, /no (?:somos una entidad mexicana|tenemos oficinas en México)/i, file);
    assert.match(html, /CFDI[^<]*(?:valida|confirma)/i, file);
    assert.doesNotMatch(html, /PostalAddress|streetAddress|Calle |Av\. /, file);
  }
});

test('Mexico pages avoid invented prices, discounts, currency conversions and unverifiable promises', () => {
  for (const file of mexicoPages) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.doesNotMatch(html, /[$€]\s?\d|\d+(?:[.,]\d+)?\s?(?:USD|COP|MXN|pesos)\b|\b(?:USD|COP|MXN)\s?\d/i, `${file}: precios o monedas`);
    assert.doesNotMatch(html, /descuento|\bpromo(?:ci[oó]n)?\b|\d+\s?% ?OFF|~\s?[\d,.]+/i, `${file}: descuentos`);
    assert.doesNotMatch(html, /24\/7|24 horas|ROI garantizado|retorno garantizado|resultados garantizados|primer lugar en Google|#1 en Google/i, `${file}: promesas`);
    assert.doesNotMatch(html, /Homologación SPEI|Compliance Bancario|Supera auditorías|certifica tu infraestructura|Certificado formal firmado|te certificamos|cumplimiento garantizado|Elimina caídas/i, `${file}: certificaciones`);
    assert.doesNotMatch(html, /sucursal en México|oficinas? en (?:CDMX|Ciudad de México|Guadalajara|Monterrey)|S\.A\. de C\.V\.|RFC/i, `${file}: entidad mexicana`);
  }
});

test('Mexico cloud page keeps the technical disclaimers of the other technical landings', () => {
  const html = fs.readFileSync(path.join(root, 'mexico-nube-seguridad-web.html'), 'utf8');
  assert.match(html, /Monitoreo automatizado continuo/);
  assert.match(html, /no incluye certificación ni homologación de terceros/);
  for (const topic of ['Cloud on-demand', 'DevSecOps', 'CI/CD', 'Cloudflare', 'backups', 'FinOps', 'Hardening', 'Ley Fintech', 'CNBV', 'SPEI', 'STP', 'CFDI 4.0']) {
    assert.ok(html.includes(topic), topic);
  }
});

test('Mexico web and marketing page covers its service scope and media-budget disclaimer', () => {
  const html = fs.readFileSync(path.join(root, 'mexico-desarrollo-web-marketing-digital.html'), 'utf8');
  for (const topic of ['Landing pages', 'Tiendas online básicas', 'Google Ads', 'Meta Ads', 'Google Business Profile', 'Medición']) {
    assert.ok(html.includes(topic), topic);
  }
  assert.match(html, /se paga directamente a Google o Meta/);
  assert.match(html, /aparte/);
});
