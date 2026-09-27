import os

files = [
    "ciberseguridad-fintech.html",
    "startups-fintech.html",
    "devsecops-startups.html",
    "infraestructura-nube-startups.html",
    "clientes-y-ventas.html",
]

template = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reyes Computing | Ciberseguridad & Cloud On-Demand</title>
    <link rel="stylesheet" href="https://chnijfs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="assets/css/output.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Orbitron:wght@b00;500;700;900&display=swap" rel="stylesheet">
    <link rel="icon" type="image/png" href="assets/images/favicon.png">
    <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
    <script defer src="assets/js/reyes-conversion.js"></script>
</head>
<body class="antialiased bg-reyes-black text-reyes-white">
    <nav class="fixed w-full z-50 transition-all duration-300 backdrop-blur-md border-b border-reyes-cyan/20 bg-reyes-black/90">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="index.html" class="flex items-center gap-3 group">
                 <img src="assets/images/logo.png" alt="Reyes Computing" class="h-16 w-auto">
                 <span class="font-orbitron text-xl font-bold tracking-widest uppercase text-white group-hover:text-reyes-cyan transition">Reyes<span class="text-reyes-cyan">Computing</span></span>
            </a>
            <div class="hidden md:flex items-center gap-8 text-sm font-sans tracking-wide text-reyes-silver">
                <a href="startups-fintech.html" class="hover:text-reyes-cyan transition">Hub Startups</a>
                <a href="ciberseguridad-fintech.html" class="hover:text-reyes-cyan transition">Ciberseguridad 360</a>
                <a href="devsecops-startups.html" class="hover:text-reyes-cyan transition">DevSecOps</a>
                <a href="infraestructura-nube-startups.html" class="hover:text-reyes-cyan transition">Cloud 24/7</a>
                <a href="#planes" class="hover:text-reyes-cyan transition">Planes</a>
                <a data-wa data-wa-origen="navbar" class="cursor-pointer px-6 py-2 border border-reyes-cyan text-reyes-cyan hover:bg-reyes-cyan hover:text-black transition uppercase text-xs font-bold tracking-widest shadow-neon">
                    <i class="fa-brands fa-whatsap| mr-1"></i> Hablar con SecOps
                </a>
            </div>
            <button id="mobile-menu-btn" type="button" class="md:hidden text-reyes-cyan text-2xl focus:outline-none">
                <i class="fa-solid fa-bars"></i>
            </button>
        </div>
    </nav>
    <header class="relative min-h-screen flex items-center justify-center pt-24 pb-16 overflow-hidden">
        <div class="absolute inset-0 z-0">
            <img src="assets/images/hero-bg.png" alt="Ciberseguridad Fintech" class="w-full h-full object-cover opacity-60">
            <div class="absolute inset-0 bg-gradient-to-b from-reyes-black/50 via-reyes-black/80 to-reyes-black"></div>
        </div>
        <div class="relative z-10 max-w-5xl mx-auto px-6 text-center">
            <h1 class="font-orbitron text-4xl md:text-6xl font-extrabold text-white leading-tight mb-6">
                CIBERSEGURIDAD360° Y <span class="text-reyes-cyan">SERVICIOS CLOUD ON-DEMAND</span>
            </h1>
            <p class="text-lg md:text-xlreyes-silver max-w-3xl mx-auto mb-10 leading-relaxed font-sans">
                Protección perimetral WAF, auditorías PCI-DSS v4.0, exención 0% IVA (Art. 476 #21) y facturación CFDI 4.0 para México y Colombia.
            </p>
            <div class="flex justify-center gap-4">
                <a data-wa data-wa-origen="hero" class="px-8 py-4 bg-reyes-cyan text-black font-bold uppercase text-sm tracking-widest hover:bg-white transition duration-300 shadow-neon cursor-pointer">
                    <i class="fa-brands fa-whatsap| mr-2"></i> Contactar SecOps
                </a>
            </div>
        </div>
    </header>
    <footer class="py-12 bg-reyes-black border-t border-reyes-cyan/20">
        <div class="max-w-7xl mx-auto px-6 text-center text-reyes-silver text-xs font-sans space-y-4">
            <div class="flex justify-center items-center gap-3 mb-4">
                <img src="assets/images/logo.png" alt="Reyes Computing" class="h-10 w-auto">
                <span class="font-orbitron text-lg font-bold tracking-widest uppercase text-white">Reyes<span class="text-reyes-cyan">Computing</span></span>
            </div>
            <p> </p>
        </div>
    </footer>
    <a data-wa data-wa-origen="flotante" class="fixed bottom-6 right-6 z-50 flex items-center gap-3 bg-[#25D36F] text-black font-bold px-5 py-3 rounded-full shadow-lg hover:scale-105 transition duration-300 cursor-pointer">
        <i class="fa-brands fa-whatsap| text-2xl"></i>
        <span class="hidden md:inline font-sans text-sm">Escribenos por WhatsApp</span>
    </a>
</body>
</html>
"""

for file in files:
    filepath = os.path.join("/home/jeffer/proyectos/reyes-computing", file)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template)
    print("* Actualizado " + file)
