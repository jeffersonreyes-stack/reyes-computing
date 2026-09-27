#!/usr/bin/env python3
import json
import sys
import urllib.request
import subprocess

branch = sys.argv[1] if len(sys.argv) > 1 else "feature/workflow-rules-mandatory"
title = sys.argv[2] if len(sys.argv) > 2 else f"feat: {branch}"
body = sys.argv[3] if len(sys.argv) > 3 else "Pull Request generado automáticamente en cumplimiento de las reglas mandatorias del proyecto."

# Obtain token from git credential
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

url = "https://api.github.com/repos/jeffersonreyes-stack/reyes-computing/pulls"
payload = {
    "title": title,
    "head": branch,
    "base": "main",
    "body": body
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
        print(f"🎉 PULL REQUEST CREADO Y ABIERTO EN GITHUB: PR #{res_data['number']}")
        print(f"   URL: {res_data['html_url']}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8')
    print(f"❌ HTTP Error {e.code}: {err_body}")
