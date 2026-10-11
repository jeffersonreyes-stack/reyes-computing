const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const root = path.join(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'assets/js/reyes-conversion.js'), 'utf8');
const css = fs.readFileSync(path.join(root, 'assets/css/input.css'), 'utf8');

function loadMenu() {
  const context = vm.createContext({ console, window: { location: { pathname: '/tiendas-online.html', search: '' } }, document: { addEventListener() {} } });
  vm.runInContext(source, context);
  return {
    items: vm.runInContext('MENU_LATERAL', context),
    html: vm.runInContext('construirMenuLateral()', context)
  };
}

test('side menu links point to existing pages and cover the new services', () => {
  const { items } = loadMenu();
  const hrefs = items.flatMap((group) => group.enlaces.map((link) => link[2]));
  for (const href of hrefs) assert.ok(fs.existsSync(path.join(root, href)), href);
  for (const required of ['tiendas-online.html', 'mexico-tiendas-online.html', 'mexico-desarrollo-web-marketing-digital.html', 'mexico-nube-seguridad-web.html', 'ofertas.html', 'contacto.html']) {
    assert.ok(hrefs.includes(required), required);
  }
  assert.equal(new Set(hrefs).size, hrefs.length);
});

test('side menu marks the current page, keeps both CTAs and tracks their origin', () => {
  const { html } = loadMenu();
  assert.match(html, /href="tiendas-online\.html"[^>]*aria-current="page"/);
  assert.equal((html.match(/aria-current="page"/g) || []).length, 1);
  assert.match(html, /href="contacto\.html\?servicio=diagnostico" data-origen="menu-lateral"/);
  assert.match(html, /data-wa data-wa-origen="menu-lateral"/);
  assert.match(html, /aria-label="Cerrar menu principal"/);
});

test('side menu has hidden-by-default styles and respects reduced motion', () => {
  assert.match(css, /\.menu-lateral \{[^}]*visibility: hidden;/);
  assert.match(css, /\.menu-lateral\.abierto \{[^}]*visibility: visible;/);
  assert.match(css, /prefers-reduced-motion: reduce/);
});
