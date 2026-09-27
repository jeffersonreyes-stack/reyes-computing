# ==============================================================================
# REYES COMPUTING - Infraestructura como Código (IaC) para Hardening CloudFront / S3
# Propósito: Otorgar Calificación A+ en SSL Labs & Security Headers (100/100)
# ==============================================================================

# 1. Política de Cabeceras de Respuesta HTTP (Response Headers Policy)
resource "aws_cloudfront_response_headers_policy" "reyes_security_headers" {
  name    = "ReyesComputing-A-Plus-Security-Policy"
  comment = "Cabeceras de Seguridad de Grado Bancario para reyescomputing.com"

  security_headers_config {
    # HSTS: Forzamiento estricto de HTTPS (2 años + subdominios + preload)
    strict_transport_security {
      access_control_max_age_sec = 63072000
      include_subdomains         = true
      preload                    = true
      override                   = true
    }

    # Anti-Clickjacking: Prohibir embebido en frames ajenos
    frame_options {
      frame_option = "DENY"
      override     = true
    }

    # Proteccion contra MIME-Sniffing
    content_type_options {
      override = true
    }

    # Politica de Referrer estricta
    referrer_policy {
      referrer_policy = "strict-origin-when-cross-origin"
      override        = true
    }

    # Content Security Policy (CSP) para prevenir XSS e inyecciones
    content_security_policy {
      content_security_policy = "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://cdnjs.cloudflare.com https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; img-src 'self' data: https:; font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; connect-src 'self' https://www.google-analytics.com https://stats.g.doubleclick.net https://formsubmit.co; frame-ancestors 'none'; upgrade-insecure-requests;"
      override                = true
    }
  }

  # Inyección de cabecera Server personalizada para ocultar "AmazonS3"
  custom_headers_config {
    items {
      header   = "Server"
      value    = "ReyesComputing-WAF-Engine"
      override = true
    }
    items {
      header   = "Permissions-Policy"
      value    = "camera=(), microphone=(), geolocation=(), payment=()"
      override = true
    }
  }
}

# Instrucciones de Vinculación en AWS CloudFront Console:
# 1. Ir a CloudFront > Distributions > ID de tu distribución (${{ secrets.CLOUDFRONT_ID }}).
# 2. Editar el Behavior predeterminado ('Default (*)' Behavior).
# 3. En 'Response headers policy', seleccionar 'ReyesComputing-A-Plus-Security-Policy'.
# 4. Guardar cambios e invalidar la caché (/*).
