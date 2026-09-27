#!/usr/bin/env python3
"""
Auditoría Técnica Express (20 min) - Reyes Computing
Herramienta de diagnóstico de ciberseguridad perimetral y cloud para Fintechs & Startups.
"""

import sys
import os
import json
import ssl
import socket
import urllib.request
import urllib.parse
from datetime import datetime

def run_express_audit(domain_or_url):
    # Standardize URL
    if not domain_or_url.startswith("http://") and not domain_or_url.startswith("https://"):
        target_url = "https://" + domain_or_url
        domain = domain_or_url
    else:
        target_url = domain_or_url
        domain = urllib.parse.urlparse(domain_or_url).netloc

    # Remove port if present for domain string
    hostname = domain.split(":")[0]

    print("=" * 65)
    print(" 🛡️  REYES COMPUTING - AUDITORÍA TÉCNICA EXPRESS DE SEGURIDAD")
    print(f" Target: {hostname} ({target_url})")
    print(f" Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 65)

    findings = []
    score = 100

    # 1. SSL / TLS Inspection
    print("\n🔒 1. Inspección SSL / TLS:")
    ssl_info = {}
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                version = ssock.version()
                
                issuer = dict(x[0] for x in cert.get('issuer', []))
                issuer_name = issuer.get('organizationName', issuer.get('commonName', 'Desconocido'))
                not_after = cert.get('notAfter')

                print(f"   ✅ Protocolo: {version}")
                print(f"   ✅ Cifrado: {cipher[0]} ({cipher[2]} bits)")
                print(f"   ✅ Emisor Certificado: {issuer_name}")
                print(f"   ✅ Vencimiento: {not_after}")

                ssl_info = {
                    "version": version,
                    "cipher": cipher[0],
                    "issuer": issuer_name,
                    "expires": not_after
                }
    except Exception as e:
        print(f"   ❌ ERROR SSL/TLS: {e}")
        score -= 30
        findings.append({
            "severity": "ALTA",
            "title": "Fallo en configuración SSL/TLS",
            "detail": f"No se pudo establecer una conexión HTTPS segura: {e}"
        })

    # 2. HTTP Security Headers
    print("\n🌐 2. Análisis de Security Headers:")
    headers = {}
    server_header = None
    powered_by = None
    waf_detected = "No detectado explícitamente"

    try:
        req = urllib.request.Request(
            target_url,
            headers={'User-Agent': 'Mozilla/5.0 (ReyesComputing Audit/1.0)'}
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            headers = dict(resp.headers)
            server_header = headers.get('Server')
            powered_by = headers.get('X-Powered-By')

            # WAF Detection signatures
            h_str = json.dumps(headers).lower()
            if 'cloudflare' in h_str or '__cf_bm' in h_str:
                waf_detected = "Cloudflare WAF / CDN"
            elif 'cloudfront' in h_str or 'x-amz-cf-id' in h_str:
                waf_detected = "AWS CloudFront / WAF"
            elif 'akamai' in h_str:
                waf_detected = "Akamai WAF"
            elif 'fastly' in h_str:
                waf_detected = "Fastly WAF"
            elif 'sucuri' in h_str:
                waf_detected = "Sucuri WAF"

            print(f"   🛡️  WAF / Edge Protection: {waf_detected}")

            # Header evaluation
            sec_headers = {
                'Strict-Transport-Security': 'HSTS (Forzamiento HTTPS)',
                'Content-Security-Policy': 'CSP (Prevención XSS/Inyección)',
                'X-Frame-Options': 'Anti-Clickjacking',
                'X-Content-Type-Options': 'MIME Sniffing Shield',
                'Referrer-Policy': 'Política de Referrer'
            }

            for h_key, h_desc in sec_headers.items():
                if h_key in headers or h_key.lower() in [k.lower() for k in headers]:
                    print(f"   ✅ {h_key}: Presente ({h_desc})")
                else:
                    print(f"   ❌ {h_key}: FALTANTE ({h_desc})")
                    score -= 10
                    findings.append({
                        "severity": "MEDIA" if h_key != 'Strict-Transport-Security' else "ALTA",
                        "title": f"Falta cabecera {h_key}",
                        "detail": f"La ausencia de {h_key} ({h_desc}) expone la aplicación a riesgos perimetrales."
                    })

    except Exception as e:
        print(f"   ❌ Error al consultar la URL: {e}")
        score -= 20

    # 3. Server Information Leakage
    print("\n🔍 3. Fuga de Información Técnica:")
    if server_header:
        print(f"   ⚠️ Server Header Expuesto: '{server_header}'")
        score -= 5
        findings.append({
            "severity": "BAJA",
            "title": "Cabecera Server expone información",
            "detail": f"El servidor expone '{server_header}'. Se recomienda ocultar la versión del servidor web."
        })
    else:
        print("   ✅ Server Header: Oculto o Genérico")

    if powered_by:
        print(f"   ⚠️ X-Powered-By Expuesto: '{powered_by}'")
        score -= 5
        findings.append({
            "severity": "BAJA",
            "title": "Cabecera X-Powered-By expuesta",
            "detail": f"Revela tecnología interna: '{powered_by}'."
        })

    # Ensure score doesn't drop below 0
    score = max(0, score)

    # 4. Summary & Score Report
    print("\n" + "=" * 65)
    print(f" 📈 SCORE DE SEGURIDAD PERIMETRAL: {score} / 100")
    print("=" * 65)

    if score >= 85:
        nivel = "EXCELENTE (Preparado para auditorías)"
    elif score >= 65:
        nivel = "ACEPTABLE (Requiere ajustes en Security Headers)"
    else:
        nivel = "VULNERABLE (Acciones de blindaje urgentes requeridas)"

    print(f" Estado: {nivel}")
    print("\n ⚠️ HALLAZGOS Y RECOMENDACIONES CLAVE:")
    if not findings:
        print("   🎉 ¡Felicidades! No se detectaron vulnerabilidades perimetrales obvias.")
    else:
        for idx, f in enumerate(findings, 1):
            print(f"   {idx}. [{f['severity']}] {f['title']}")
            print(f"      👉 {f['detail']}")

    # Save Markdown Audit Report
    report_filename = f"reporte_audit_{hostname.replace('.', '_')}.md"
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), report_filename)

    with open(report_path, "w", encoding="utf-8") as rf:
        rf.write(f"# Reporte de Auditoría Técnica Express - Reyes Computing\n\n")
        rf.write(f"- **Cliente / Dominio:** `{hostname}`\n")
        rf.write(f"- **Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        rf.write(f"- **Puntaje Global:** `{score}/100` ({nivel})\n")
        rf.write(f"- **WAF Detectado:** `{waf_detected}`\n\n")
        
        rf.write("## 1. Diagnóstico Perimetral\n")
        rf.write("| Componente | Estado |\n|---|---|\n")
        rf.write(f"| SSL / TLS | Protocolo {ssl_info.get('version', 'N/A')} ({ssl_info.get('issuer', 'N/A')}) |\n")
        rf.write(f"| Protección WAF | {waf_detected} |\n")
        rf.write(f"| Server Exposure | {server_header or 'Protegido'} |\n\n")

        rf.write("## 2. Puntos Críticos a Corregir\n")
        for idx, f in enumerate(findings, 1):
            rf.write(f"### {idx}. [{f['severity']}] {f['title']}\n")
            rf.write(f"{f['detail']}\n\n")

        rf.write("## 3. Plan de Acción Recomendado (Reyes Computing)\n")
        rf.write("- **Fase 1 (Inmediata):** Implementación de Cloudflare WAF Sprint ($1,200 USD / 0% IVA).\n")
        rf.write("- **Fase 2 (Cumplimiento):** Dossier técnico para homologación bancaria y PCI-DSS v4.0 ($3,500 USD).\n")
        rf.write("- **Contacto Directo:** WhatsApp +57 312 808 4929 | control@reyescomputing.com\n")

    print(f"\n📄 Reporte Markdown generado en: {report_path}\n")
    return score, findings

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "www.reyescomputing.com"
    run_express_audit(target)
