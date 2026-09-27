#!/usr/bin/env python3
import json
import subprocess

DIST_ID = "E320TPW0QW0WP6"
POLICY_ID = "96f0f546-d11f-4cfb-880f-b8c940896d93"

print("1. Obteniendo configuración actual de CloudFront...")
out = subprocess.check_output(["aws.exe", "cloudfront", "get-distribution-config", "--id", DIST_ID])
data = json.loads(out.decode("utf-8"))

etag = data["ETag"]
config = data["DistributionConfig"]

print("2. Vinculando la política de cabeceras A+ (ID:", POLICY_ID, ")...")
config["DefaultCacheBehavior"]["ResponseHeadersPolicyId"] = POLICY_ID

with open("updated_dist_config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print("3. Actualizando la distribución en AWS CloudFront...")
update_out = subprocess.check_output([
    "aws.exe", "cloudfront", "update-distribution",
    "--id", DIST_ID,
    "--distribution-config", "file://updated_dist_config.json",
    "--if-match", etag
])

print("✅ Distribución de CloudFront actualizada con éxito!")

print("4. Invalidando caché de CloudFront...")
inval_out = subprocess.check_output([
    "aws.exe", "cloudfront", "create-invalidation",
    "--distribution-id", DIST_ID,
    "--paths", "/*"
])

print("🎉 Invalidación creada con éxito. Las cabeceras A+ ya están activas en vivo!")
