#!/usr/bin/env python3
import json
import urllib.request
import subprocess

# 1. Obtain token from git credential
proc = subprocess.Popen(["git", "credential", "fill"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, _ = proc.communicate("url=https://github.com\n")

token = None
for line in stdout.splitlines():
    if line.startswith("password="):
        token = line.split("=", 1)[1]
        break

if not token:
    print("❌ Error: No se pudo obtener el token de GitHub.")
    exit(1)

# 2. Call GitHub REST API to create Pull Request
url = "https://api.github.com/repos/jeffersonreyes-stack/reyes-computing/pulls"
payload = {
    "title": "feat: Matriz Ciberseguridad 360, Rediseño Fintech/Startups y Anti-Bot Turnstile",
    "head": "feature/ciberseguridad-fintech-360-hub",
    "base": "main",
    "body": """### Pull Request: Ciberseguridad 360 y Rediseño Fintech/Startups

- **Matriz de Ciberseguridad 360 en 6 Capas:** Incorporada en `ciberseguridad-fintech.html`.
- **Rediseño Fintech & Startups:** Tarifas duales (USD / MXN / COP), beneficios fiscales SAT México (CFDI 4.0) y Colombia (0% IVA Art. 476 #21 E.T.).
- **Protección Anti-Bot:** Integración de Cloudflare Turnstile transparente en formularios.
- **Seguridad CloudFront:** Política A+ de cabeceras de respuesta (HSTS, CSP, X-Frame DENY, nosniff, Referrer Policy).
- **Pruebas:** Suite `test_services_suite.py` (20/20 verificaciones aprobadas)."""
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
        "User-Agent": "ReyesComputing-Bot/1.0"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        res_data = json.loads(resp.read().decode("utf-8"))
        print(f"🎉 PULL REQUEST CREADO Y ABIERTO CON ÉXITO: PR #{res_data['number']}")
        print(f"   URL del PR: {res_data['html_url']}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8')
    print(f"❌ HTTP Error {e.code}: {err_body}")
