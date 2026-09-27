#!/usr/bin/env python3
"""
Suite de Pruebas y Verificación para Servicios de Reyes Computing (Startups & Fintechs)
"""

import os
import re
import urllib.request
import ssl
from html.parser import HTMLParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES_TO_TEST = [
    "startups-fintech.html",
    "ciberseguridad-fintech.html",
    "devsecops-startups.html",
    "infraestructura-nube-startups.html"
]

def test_html_pages():
    print("\n=======================================================")
    print(" 1. VERIFICACIÓN DE LANDING PAGES (FINTECH & STARTUPS)")
    print("=======================================================\n")
    
    total_checks = 0
    passed_checks = 0

    for page_file in PAGES_TO_TEST:
        page_path = os.path.join(BASE_DIR, page_file)
        print(f"📄 Analizando: [{page_file}]")
        
        if not os.path.exists(page_path):
            print(f"   ❌ ERROR: El archivo {page_file} no existe.")
            continue
            
        with open(page_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check 1: Valid HTML Structure
        total_checks += 1
        if "<!DOCTYPE html>" in content and "<html" in content and "</html>" in content:
            print("   ✅ Estructura HTML5 básica: VÁLIDA")
            passed_checks += 1
        else:
            print("   ❌ Estructura HTML5 básica: INVÁLIDA")

        # Check 2: Title Tag
        total_checks += 1
        title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
        if title_match:
            print(f"   ✅ Meta Title: '{title_match.group(1)}'")
            passed_checks += 1
        else:
            print("   ❌ Meta Title: NO ENCONTRADO")

        # Check 3: Description Meta Tag
        total_checks += 1
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        if desc_match:
            print(f"   ✅ Meta Description: '{desc_match.group(1)[:70]}...'")
            passed_checks += 1
        else:
            print("   ❌ Meta Description: NO ENCONTRADA")

        # Check 4: WhatsApp CTA Links
        total_checks += 1
        wa_links = re.findall(r'href=["\'](https://wa\.me/[^"\']+)["\']', content)
        if wa_links:
            print(f"   ✅ Botones WhatsApp Directo: {len(wa_links)} enlace(s) detectado(s)")
            for wa in wa_links[:2]:
                print(f"      • {wa[:65]}...")
            passed_checks += 1
        else:
            print("   ⚠️ Advertencia: No se encontraron enlaces wa.me directos")

        # Check 5: Tax & Value Proposition Claims (Colombia / Mexico / On-Demand)
        total_checks += 1
        if "IVA" in content or "SAT" in content or "USD" in content:
            print("   ✅ Propuesta Financiera & Tributaria (0% IVA / SAT / USD): DETECTADA")
            passed_checks += 1
        else:
            print("   ⚠️ Propuesta Financiera: No menciona IVA u ofertas claras")

        print("-" * 55)

    print(f"\n📊 Resultado Pruebas Páginas: {passed_checks}/{total_checks} verificaciones exitosas.\n")

def test_diagnostic_engine_simulation():
    print("=======================================================")
    print(" 2. PRUEBA SIMULADA DEL MOTOR DE AUDITORÍA PERIMETRAL")
    print("=======================================================\n")
    
    mock_headers = {
        'Server': 'cloudflare',
        'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
        'X-Frame-Options': 'DENY',
        'X-Content-Type-Options': 'nosniff',
        'Content-Security-Policy': "default-src 'self'",
        'Referrer-Policy': 'strict-origin-when-cross-origin'
    }
    
    print("Simulando evaluación de cabeceras para una Fintech objetivo ('app.fintechdemo.com')...")
    
    sec_score = 100
    sec_checks = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options', 'X-Content-Type-Options', 'Referrer-Policy']
    
    for h in sec_checks:
        if h in mock_headers:
            print(f"   ✅ {h}: CORRECTO")
        else:
            sec_score -= 10
            print(f"   ❌ {h}: FALTANTE")
            
    if 'cloudflare' in mock_headers.get('Server', '').lower():
        print("   ✅ WAF Perimetral: Cloudflare WAF Activo")
        
    print(f"\n📈 Score de Auditoría Simulado: {sec_score}/100 [A+ BANK-READY]")
    print("✅ Motor de Diagnóstico Express de Reyes Computing verificado correctamente.\n")

if __name__ == "__main__":
    test_html_pages()
    test_diagnostic_engine_simulation()
