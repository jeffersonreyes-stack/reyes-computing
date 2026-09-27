#!/usr/bin/env python3
import glob
import re

for path in glob.glob("*.html"):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    forms = re.findall(r"<form[\s\S]*?</form>", content, re.IGNORECASE)
    if forms:
        print(f"📄 {path}: {len(forms)} formulario(s) detectado(s)")
        for i, form in enumerate(forms, 1):
            action_m = re.search(r'action=["\'](.*?)["\']', form)
            honey_m = re.search(r'name=["\']_honey["\']', form)
            captcha_m = re.search(r'turnstile|g-recaptcha|cf-turnstile', form, re.IGNORECASE)
            print(f"   Form {i}: Action={action_m.group(1) if action_m else 'N/A'} | Honeypot={bool(honey_m)} | Captcha={bool(captcha_m)}")
