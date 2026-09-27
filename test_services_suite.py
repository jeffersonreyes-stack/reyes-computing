#!/usr/bin/env python3
import os
import sys

pages = [
    'ciberseguridad-fintech.html',
    'startups-fintech.html',
    'devsecops-startups.html',
    'infraestructura-nube-startups.html',
    'clientes-y-ventas.html',
    'CLIENTES-Y-VENTAS.HTML'
]

required_tokens = [
    ('assets/images/logo.png', 'Logo emblem imagen oficial'),
    ('text-reyes-cyan', 'Tipografia y estilo ciberpunk Reyes Cyan (#00f0ff)'),
    ('output.css', 'Sistema de diseno corporativo Tailwind CSS'),
    ('Orbitron', 'Tipografia corporativa Orbitron'),
    ('challenges.cloudflare.com/turnstile', 'Protección anti-bot Cloudflare Turnstile'),
    ('fa-whatsapp', 'Botonera WhatsApp corporativa'),
    ('assets/images/hero-bg.png', 'Imagen de fondo Hero corporativo 3D (hero-bg.png)'),
    ('<header', 'Estructura HTML oficial con etiqueta <header> en Hero'),
    ('<nav', 'Barra superior de navegación fija con etiqueta <nav>')
]

passed_tests = 0
total_tests = len(pages) * len(required_tokens)

print('🔍 EJECUTANDO SUITE DE PRUEBAS EXTENDIDA DE IDENTIDAD Y MAQUETACIÓN VISUAL...')
print('=' * 80)

for page in pages:
    if not os.path.exists(page):
        print(f'❌ ERROR: El archivo {page} no existe.')
        sys.exit(1)
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f'\n📄 Verificando {page}:')
    for token, description in required_tokens:
        if token in content:
            print(f'  ✔ [PASÓ] {description} ({token})')
            passed_tests += 1
        else:
            print(f'  ❌ [FALLÓ] {description} FALTA en {page}')

print('\n' + '=' * 80)
print(f'RESULTADO DE LA SUITE: {passed_tests}/{total_tests} Verificaciones Aprobadas ({(passed_tests/total_tests)*100:.1f}%)')

if passed_tests == total_tests:
    print('🎉 ¡TODAS LAS PÁGINAS CUMPLEN 100% CON LA IDENTIDAD Y ESTRUCTURA MAQUETADA!')
    sys.exit(0)
else:
    print('⚠️ ALGUNAS PRUEBAS FALLARON.')
    sys.exit(1)
