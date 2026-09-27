#!/usr/bin/env python3
import sys
import subprocess

branch = sys.argv[1] if len(sys.argv) > 1 else "feature/fix-fintech-ads-landing-url"
title = sys.argv[2] if len(sys.argv) > 2 else "fix: restaurar contenido original completo de paginas de servicios"
body = sys.argv[3] if len(sys.argv) > 3 else "Se restaura el 100% del contenido handcrafted original manteniendo unicamente la estandarizacion del estilo visual del header y logo oficial."

cmd = ["/snap/bin/gh", "pr", "create", "--title", title, "--body", body, "--base", "main", "--head", branch]
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print(res.stderr, file=sys.stderr)
sys.exit(res.returncode)
