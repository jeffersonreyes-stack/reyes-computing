const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const root = path.join(__dirname, '..');
const read = (file) => fs.readFileSync(path.join(root, file), 'utf8');
const htmlFiles = fs.readdirSync(root).filter((file) => /\.html$/i.test(file));
const corporateFiles = htmlFiles.filter((file) => !file.startsWith('mockup-') && !file.startsWith('success'));
const source = read('assets/js/reyes-conversion.js');

function loadServicios() {
  const context = vm.createContext({ console, window: { location: { pathname: '/', search: '' } }, document: { addEventListener() {} } });
  vm.runInContext(source, context);
  return vm.runInContext('SERVICIOS_CONTACTO', context);
}

test('every corporate page links to ofertas.html in navbar and footer', () => {
  for (const file of corporateFiles) {
    const html = read(file);
    const nav = html.match(/<nav class="hidden lg:flex[\s\S]*?<\/nav>|<div class="hidden lg:flex items-center gap-\d[\s\S]*?<\/div>/)?.[0] || '';
    assert.match(nav, /<a href="ofertas\.html"[^>]*>Ofertas<\/a>/, `${file}: navbar`);
    const footer = html.match(/<footer\b[\s\S]*?<\/footer>/)?.[0] || '';
    assert.match(footer, /<a href="ofertas\.html"[^>]*>Ofertas/, `${file}: footer`);
  }
});

test('static mobile menus include Ofertas', () => {
  for (const file of corporateFiles) {
    const menu = read(file).match(/<div id="mobile-menu"[\s\S]*?<\/div>/)?.[0];
    if (menu) assert.match(menu, /href="ofertas\.html"/, file);
  }
});

test('navbar Diagnóstico Gratis goes to the contact form, not WhatsApp', () => {
  for (const file of corporateFiles) {
    const html = read(file);
    const buttons = [...html.matchAll(/<a\b[^>]*>(?:(?!<\/a>)[\s\S])*Diagnóstico Gratis\s*<\/a>/g)].map((match) => match[0]);
    assert.ok(buttons.length > 0, file);
    for (const button of buttons) {
      assert.match(button, /href="contacto\.html\?servicio=diagnostico"/, file);
      assert.doesNotMatch(button, /wa\.me|data-wa|fa-whatsapp/, file);
    }
  }
});

test('quote and proposal CTAs use the contact form; WhatsApp is kept only where explicit', () => {
  for (const file of corporateFiles) {
    const html = read(file);
    for (const match of html.matchAll(/<a\b[^>]*(?:data-wa|wa\.me)[^>]*>((?:(?!<\/a>)[\s\S])*)<\/a>/g)) {
      const text = match[1].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      if (/^(Diagnóstico Gratis|Solicitar propuesta|Cotizar|Contratar|Pedir|Quiero|Revisar|Auditar)/i.test(text)) {
        assert.match(text, /WhatsApp/i, `${file}: ${text}`);
      }
    }
  }
});

test('ofertas.html is in the sitemap and has SEO metadata', () => {
  assert.match(read('sitemap.xml'), /<loc>https:\/\/www\.reyescomputing\.com\/ofertas\.html<\/loc>/);
  const html = read('ofertas.html');
  assert.match(html, /<title>[^<]+<\/title>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/www\.reyescomputing\.com\/ofertas\.html">/);
  assert.match(html, /property="og:title"/);
  assert.match(html, /property="og:url" content="https:\/\/www\.reyescomputing\.com\/ofertas\.html"/);
  assert.match(html, /src="assets\/js\/reyes-conversion\.js"/);
});

test('ofertas.html avoids invented prices, discounts, guarantees and ROI claims', () => {
  const html = read('ofertas.html');
  assert.doesNotMatch(html, /PROMO|\d+\s?% ?(?:OFF|de descuento|dto)|descuento del|ahorra(?:s)? \d|\bOFF\b/i);
  assert.doesNotMatch(html, /\$\s?\d|\b(?:COP|USD|MXN)\b|\d+\s?(?:USD|COP|MXN)/);
  assert.doesNotMatch(html, /Precios claros|Precios Claros|Entrega en \d|Google Business verificada|garantizad[oa]s?\b|ROI|retorno de inversi/i);
  assert.match(html, /Cotización/);
  assert.match(html, /se confirman por escrito/);
  assert.match(html, /impuestos/i);
});

test('every offer in ofertas.html has a form CTA and a WhatsApp CTA', () => {
  const html = read('ofertas.html');
  const cards = html.match(/<article\b[\s\S]*?<\/article>/g) || [];
  assert.ok(cards.length >= 8);
  for (const card of cards) {
    assert.match(card, /href="contacto\.html\?servicio=[a-z-]+#contactForm"/);
    assert.match(card, /data-wa\b/);
    assert.match(card, /Solicitar por formulario/);
    assert.match(card, /Para quién:/);
  }
  assert.match(html, /id="proximas"/);
});

test('every servicio slug used in links is known and every known slug maps to a form option', () => {
  const servicios = loadServicios();
  const contacto = read('contacto.html');
  const options = [...contacto.match(/name="service_interest"[\s\S]*?<\/select>/)[0].matchAll(/<option>([^<]+)<\/option>/g)].map((match) => match[1]);
  for (const [slug, servicio] of Object.entries(servicios)) {
    assert.ok(options.includes(servicio.opcion), `${slug}: ${servicio.opcion}`);
  }
  for (const file of htmlFiles) {
    for (const match of read(file).matchAll(/contacto\.html\?servicio=([^"#&]+)/g)) {
      assert.ok(servicios[match[1]], `${file}: ${match[1]}`);
    }
  }
});

test('contact form is prefilled from ?servicio= without overwriting user text', () => {
  const select = { value: '', options: [{ value: 'Google Ads' }, { value: 'Tienda online' }] };
  const mensaje = { value: '' };
  const asunto = { value: 'Nuevo Lead Comercial - Reyes Computing' };
  const aviso = { textContent: '', classList: { removed: [], remove(name) { this.removed.push(name); } } };
  const form = {
    querySelector: (selector) => ({ 'select[name="service_interest"]': select, 'textarea[name="message"]': mensaje, 'input[name="_subject"]': asunto })[selector]
  };
  const context = vm.createContext({
    console,
    URLSearchParams,
    window: { location: { pathname: '/contacto.html', search: '?servicio=tienda-online' } },
    document: { addEventListener() {}, getElementById: (id) => (id === 'contactForm' ? form : aviso) }
  });
  vm.runInContext(source, context);
  vm.runInContext('prellenarFormularioContacto()', context);
  assert.equal(select.value, 'Tienda online');
  assert.match(mensaje.value, /Tienda Online/);
  assert.match(asunto.value, /Tienda online$/);
  assert.deepEqual(aviso.classList.removed, ['hidden']);

  mensaje.value = 'Mensaje del cliente';
  vm.runInContext('prellenarFormularioContacto()', context);
  assert.equal(mensaje.value, 'Mensaje del cliente');
});

test('unknown or missing servicio leaves the form untouched', () => {
  for (const search of ['', '?servicio=__proto__', '?servicio=inexistente']) {
    const select = { value: 'x', options: [] };
    const context = vm.createContext({
      console,
      URLSearchParams,
      window: { location: { pathname: '/contacto.html', search } },
      document: { addEventListener() {}, getElementById: () => ({ querySelector: () => select }) }
    });
    vm.runInContext(source, context);
    vm.runInContext('prellenarFormularioContacto()', context);
    assert.equal(select.value, 'x', search);
  }
});

test('contact-form link clicks are tracked without using the WhatsApp Ads label', () => {
  let handler;
  const events = [];
  const link = { dataset: { origen: 'navbar' }, addEventListener: (_, callback) => { handler = callback; } };
  const context = vm.createContext({
    console,
    URLSearchParams,
    window: { location: { pathname: '/index.html', search: '' } },
    document: { addEventListener() {}, querySelectorAll: () => [link] },
    gtag: (...args) => events.push(args)
  });
  vm.runInContext(source, context);
  vm.runInContext('activarEnlacesContacto()', context);
  handler();
  assert.equal(events.length, 1);
  assert.equal(events[0][2].metodo, 'formulario');
  assert.equal(events.filter((event) => event[1] === 'conversion').length, 0);
});

test('local links between pages point to existing files', () => {
  for (const file of htmlFiles) {
    for (const match of read(file).matchAll(/\bhref="([^"#?:]+\.html)(?:[#?][^"]*)?"/g)) {
      assert.ok(fs.existsSync(path.join(root, match[1])), `${file} -> ${match[1]}`);
    }
  }
});
