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

test('all seven contact forms remain connected to FormSubmit', () => {
  const formPages = [
    'ciberseguridad-fintech.html',
    'ciberseguridad-ia-cali.html',
    'contacto.html',
    'devsecops-startups.html',
    'google-business-profile.html',
    'infraestructura-nube-startups.html',
    'startups-fintech.html'
  ];
  for (const file of formPages) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.match(html, /<form\b[^>]*action="https:\/\/formsubmit\.co\/control@reyescomputing\.com"[^>]*method="POST"/i, file);
  }
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
