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

test('technical landings do not include unrelated web promotions or conflicting cloud prices', () => {
  for (const file of ['startups-fintech.html', 'devsecops-startups.html', 'infraestructura-nube-startups.html', 'ciberseguridad-fintech.html']) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    assert.doesNotMatch(html, /TABLA 1:|450 USD|\$599\.000/);
  }
});