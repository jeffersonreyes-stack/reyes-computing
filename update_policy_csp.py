#!/usr/bin/env python3
import json
import subprocess

POLICY_ID = "96f0f546-d11f-4cfb-880f-b8c940896d93"
DIST_ID = "E320TPW0QW0WP6"

print("1. Leyendo política actual...")
out = subprocess.check_output(["aws.exe", "cloudfront", "get-response-headers-policy", "--id", POLICY_ID])
data = json.loads(out.decode("utf-8"))

etag = data["ETag"]
config = data["ResponseHeadersPolicy"]["ResponseHeadersPolicyConfig"]

# Update CSP to support Cloudflare Turnstile
config["SecurityHeadersConfig"]["ContentSecurityPolicy"]["ContentSecurityPolicy"] = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https://challenges.cloudflare.com https://www.googletagmanager.com https://cdnjs.cloudflare.com https://fonts.googleapis.com; "
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
    "img-src 'self' data: https:; "
    "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
    "connect-src 'self' https://www.google-analytics.com https://stats.g.doubleclick.net https://formsubmit.co https://formspree.io; "
    "frame-src 'self' https://challenges.cloudflare.com; "
    "frame-ancestors 'none'; "
    "upgrade-insecure-requests;"
)

with open("policy_update.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print("2. Actualizando política de cabeceras en CloudFront...")
subprocess.check_output([
    "aws.exe", "cloudfront", "update-response-headers-policy",
    "--id", POLICY_ID,
    "--response-headers-policy-config", "file://policy_update.json",
    "--if-match", etag
])

print("3. Invalidando caché de CloudFront...")
subprocess.check_output([
    "aws.exe", "cloudfront", "create-invalidation",
    "--distribution-id", DIST_ID,
    "--paths", "/*"
])

print("🎉 Política CSP actualizada con éxito para soporte de Cloudflare Turnstile!")
