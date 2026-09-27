# -*- coding: utf-8 -*
-*
import json, sys, urllib.request, subprocess

branch = "feature/unify-brand-identity-header-logo"
title = "feat: Unificar logo oficial e imagen corporativa en paginas de servicios"
body = "Pull Request que restablece y unifica el logo emblem oficial (logo.png), tipografia Orbitron, colores ciberpunk cyan (#00f0ff), proteccion Cloudflare Turnstile y suite de pruebas al 100% (30/30 aprobados)."

proc = subprocess.Popen("git credential fill".split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, _ = proc.communicate("url=https://github.com\n")

token = None
for line in stdout.splitlines():
    if line.startswith("password="):
        token = line.split("=", 1)[1]
        break

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
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        res_data = jM½¸¹±½…‘Ì¡É•ÍÀ¹É•… ¤¹‘•½‘” ‰ÕÑ˜´àˆ¤¤(€€€€€€€ÁÉ¥¹Ğ¡˜‰AU10IEUMPI<d	%IQ<8%Q!UèAH€íÉ•Í}‘…Ñ…l¹Õµ‰•Èuôˆ¤(€€€€€€€ÁÉ¥¹Ğ¡˜‰UI0èíÉ•Í}‘…Ñ…l¡Ñµ±}ÕÉ°uôˆ¤)•á•ÁĞÕÉ±±¥ˆ¹•ÉÉ½È¹!QQAÉÉ½È…Ì”è(€€€ÁÉ¥¹Ğ¡˜‰ÉÉ½Èèí”¹É•… ¤¹‘•½‘” ÕÑ˜´àœ¥ôˆ¤(