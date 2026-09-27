#!/usr/bin/env python3
import glob
import re
import os

TURNSTILE_SCRIPT = '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>'
TURNSTILE_WIDGET = '<div class="cf-turnstile my-4" data-sitekey="0x4AAAAAAFE4OGm_xxNsWqtq" data-theme="dark"></div>'

files_modified = 0

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "<form" not in content or "cf-turnstile" in content:
        continue

    # Inject Turnstile Script in <head> if missing
    if "challenges.cloudflare.com/turnstile" not in content:
        content = content.replace("</head>", f"    {TURNSTILE_SCRIPT}\n</head>")

    # Inject Turnstile Widget before submit button in form
    content = re.sub(
        r'(<button[^>]*type=["\']submit["\'][^>]*>)',
        f'    {TURNSTILE_WIDGET}\n                    \\1',
        content,
        flags=re.IGNORECASE
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Protegido con Cloudflare Turnstile: [{filepath}]")
    files_modified += 1

print(f"\n🎉 Total de páginas protegidas con Captcha transparente: {files_modified}")
