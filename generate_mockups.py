import os
import json

# Define the lead data extracted from the text files
leads = [
    {
        "id": "arepas-deeluxe",
        "company": "Arepas rellenas Deeluxe",
        "niche": "Restaurante / Venta de Alimentos",
        "hero_title": "Las mejores arepas rellenas, ahora a un clic de distancia.",
        "hero_subtitle": "Haz tu pedido al instante o encuéntranos en tu distribuidor más cercano. Sabor inigualable directo a tu mesa.",
        "pilar1_title": "Menú Interactivo Digital",
        "pilar1_desc": "Tus clientes podrán armar su arepa con los ingredientes que deseen y enviarte el pedido directamente a tu WhatsApp, listo para preparar.",
        "pilar2_title": "Ventas al por Mayor",
        "pilar2_desc": "Catálogo optimizado para tiendas y minimarkets que quieran distribuir tus arepas congeladas y empacadas.",
        "pilar3_title": "Atrae clientes locales",
        "pilar3_desc": "Sistema preparado para recibir visitas de personas en tu zona que buscan comida rápida deliciosa."
    },
    {
        "id": "vad-fitness",
        "company": "Vad Fitness",
        "niche": "Fitness / Entrenamiento",
        "hero_title": "Transforma tu cuerpo y alcanza tu mejor versión.",
        "hero_subtitle": "Únete a nuestros programas de entrenamiento y da el primer paso hacia una vida más fuerte y saludable.",
        "pilar1_title": "Captación de Prospectos",
        "pilar1_desc": "Página optimizada con llamados a la acción claros para que los interesados se registren a tus asesorías o planes de entrenamiento.",
        "pilar2_title": "Autoridad de Marca",
        "pilar2_desc": "Diseño profesional que transmite confianza y muestra tus casos de éxito para posicionar a Vad Fitness.",
        "pilar3_title": "Inscripciones Fáciles",
        "pilar3_desc": "Formularios ágiles y botones de WhatsApp para que adquirir una membresía sea un proceso sin fricciones."
    },
    {
        "id": "gato-con-botas",
        "company": "Gato con botas",
        "niche": "Restauración de Tenis",
        "hero_title": "Devuélvele la vida a tus tenis favoritos.",
        "hero_subtitle": "Expertos en restauración y limpieza profunda. Déjalos como nuevos otra vez.",
        "pilar1_title": "Galería Antes y Después",
        "pilar1_desc": "Mostramos visualmente la calidad de tu trabajo, generando confianza inmediata en tus clientes potenciales.",
        "pilar2_title": "Cotizaciones al Instante",
        "pilar2_desc": "Tus clientes podrán subir una foto de sus tenis y pedirte una cotización rápida directamente por WhatsApp.",
        "pilar3_title": "Fidelización de Clientes",
        "pilar3_desc": "Sistema estructurado para captar amantes de los sneakers que confíen sus pares de marca repetidamente."
    },
    {
        "id": "distribuidora-amaro",
        "company": "Distribuidora de belleza Amaro",
        "niche": "Distribuidora de Belleza",
        "hero_title": "Productos de belleza profesionales al mejor precio.",
        "hero_subtitle": "Abastece tu salón o negocio con nuestro catálogo de las mejores marcas del mercado.",
        "pilar1_title": "Atrae Compradores Listos",
        "pilar1_desc": "Posicionamiento para aparecer primero cuando estilistas y salones buscan comprar productos al por mayor.",
        "pilar2_title": "Catálogo Digital",
        "pilar2_desc": "Muestra todos tus productos de forma clara y organizada para facilitar pedidos grandes.",
        "pilar3_title": "Cierre por WhatsApp",
        "pilar3_desc": "Tus clientes revisan el catálogo y envían su lista de pedidos directo a tu WhatsApp para finalizar la venta."
    },
    {
        "id": "muebles-chichi",
        "company": "Muebles colchones chichi 2",
        "niche": "Muebles y Colchones",
        "hero_title": "El confort que tu hogar merece, con ofertas exclusivas.",
        "hero_subtitle": "Renueva tus espacios con nuestra selección de muebles y colchones de alta calidad.",
        "pilar1_title": "Ofertas de Temporada",
        "pilar1_desc": "Destacamos tus camas y colchones más vendidos con fotos grandes y llamadas a la acción irresistibles.",
        "pilar2_title": "Tráfico Local",
        "pilar2_desc": "Optimización para atraer a personas de tu ciudad que están buscando activamente amueblar su hogar.",
        "pilar3_title": "Cotización Rápida",
        "pilar3_desc": "Botones flotantes para que los interesados pregunten precios e inventario en un solo clic."
    },
    {
        "id": "dyb-viajes",
        "company": "DyB Viajes",
        "niche": "Agencia de Viajes",
        "hero_title": "Planifica tus vacaciones soñadas sin estrés.",
        "hero_subtitle": "Descubre los mejores destinos, vuelos y paquetes turísticos al mejor precio del mercado.",
        "pilar1_title": "Landing Pages por Destino",
        "pilar1_desc": "Páginas específicas (Ej: Cancún) con fotos espectaculares e itinerarios para captar a quienes buscan ese viaje.",
        "pilar2_title": "Intención de Búsqueda",
        "pilar2_desc": "Atraemos a viajeros que buscan activamente 'paquetes baratos' en tu ciudad para convertirlos en clientes.",
        "pilar3_title": "Remarketing de Viajes",
        "pilar3_desc": "Mostramos tus destinos a personas que ya visitaron tu web para recordarles que soliciten su cotización."
    },
    {
        "id": "max-tom",
        "company": "Max & Tom",
        "niche": "Adopción de Mascotas",
        "hero_title": "Dales una segunda oportunidad. Encuentra a tu mejor amigo.",
        "hero_subtitle": "Conoce a nuestros peluditos rescatados que están esperando llenar tu hogar de amor.",
        "pilar1_title": "Historias Emotivas",
        "pilar1_desc": "Presentamos a los animales con fotos y relatos que conecten rápidamente con los futuros adoptantes.",
        "pilar2_title": "Postulación Ágil",
        "pilar2_desc": "Formularios de adopción sencillos y persuasivos para captar los datos de las familias interesadas sin fricciones.",
        "pilar3_title": "Gestión de Adoptantes",
        "pilar3_desc": "Un sistema ordenado para hacer seguimiento desde la solicitud hasta la visita y la adopción exitosa."
    }
]

html_template = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex">

    <title>Landing Page Mockup - __COMPANY__</title>
    <meta name="description" content="Propuesta de diseño web de alta conversión para __COMPANY__.">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="assets/css/output.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@400;500;700;900&display=swap" rel="stylesheet">

    <style>
        /* Mockup specific styles maintaining Reyes Computing aesthetic */
        .mockup-hero {
            background: linear-gradient(to bottom, rgba(5,5,5,0.7), rgba(5,5,5,1)),
                        url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80');
            background-size: cover;
            background-position: center;
        }
        .mockup-badge {
            display: inline-block;
            background: rgba(0, 243, 255, 0.1);
            border: 1px solid #00F3FF;
            color: #00F3FF;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 0.8rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 20px;
        }
    </style>
</head>
<body class="antialiased bg-reyes-black text-reyes-white">

    <!-- Mockup Header -->
    <nav class="fixed w-full z-50 transition-all duration-300 backdrop-blur-md border-b border-reyes-cyan/20 bg-reyes-black/90">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <span class="font-orbitron text-xl font-bold tracking-widest uppercase text-white">__COMPANY__</span>
            </div>
            <div class="hidden md:flex items-center gap-8 text-sm font-sans tracking-wide">
                <a href="#servicios" class="text-reyes-silver hover:text-reyes-cyan transition">Servicios</a>
                <a href="#nosotros" class="text-reyes-silver hover:text-reyes-cyan transition">Nosotros</a>
                <a href="#contacto" class="px-6 py-2 border border-reyes-cyan bg-reyes-cyan text-black hover:bg-white transition uppercase text-xs font-bold tracking-widest shadow-neon">
                    Contactar
                </a>
            </div>
        </div>
    </nav>

    <!-- Mockup Hero Section -->
    <header class="relative min-h-[90vh] flex items-center justify-center pt-20 mockup-hero">
        <div class="relative z-10 max-w-4xl mx-auto px-6 text-center">
            <span class="mockup-badge font-orbitron">Sitio Web de Alta Conversión</span>
            <h1 class="font-orbitron text-4xl md:text-6xl font-bold text-white leading-tight mb-6">
                __HERO_TITLE__
            </h1>
            <p class="font-sans text-lg md:text-xl text-reyes-silver mb-10 max-w-2xl mx-auto font-light leading-relaxed">
                __HERO_SUBTITLE__
            </p>
            <div class="flex flex-col sm:flex-row justify-center gap-6">
                <a href="#contacto" class="bg-reyes-cyan text-black px-8 py-4 font-bold tracking-widest uppercase hover:bg-white transition shadow-neon w-full sm:w-auto text-center font-orbitron text-sm">
                    Solicitar Información
                </a>
                <a href="#servicios" class="border border-white text-white px-8 py-4 font-bold tracking-widest uppercase hover:bg-white hover:text-black transition w-full sm:w-auto text-center font-orbitron text-sm">
                    Ver Servicios
                </a>
            </div>
        </div>
    </header>

    <!-- Mockup Features Section -->
    <section id="servicios" class="py-24 relative">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="font-orbitron text-3xl md:text-4xl font-bold text-white mb-6">¿Por qué elegirnos?</h2>
                <div class="w-16 h-1 bg-reyes-cyan mx-auto shadow-neon"></div>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                <div class="bg-reyes-black border border-white/5 p-8 service-card" style="background-color: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 8px; padding: 30px;">
                    <i class="fa-solid fa-star text-3xl text-reyes-cyan mb-6"></i>
                    <h3 class="font-orbitron text-xl font-bold text-white mb-4">__PILAR1_TITLE__</h3>
                    <p class="text-reyes-silver leading-relaxed">__PILAR1_DESC__</p>
                </div>

                <div class="bg-reyes-black border border-white/5 p-8 service-card" style="background-color: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 8px; padding: 30px;">
                    <i class="fa-solid fa-bolt text-3xl text-reyes-cyan mb-6"></i>
                    <h3 class="font-orbitron text-xl font-bold text-white mb-4">__PILAR2_TITLE__</h3>
                    <p class="text-reyes-silver leading-relaxed">__PILAR2_DESC__</p>
                </div>

                <div class="bg-reyes-black border border-white/5 p-8 service-card" style="background-color: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 8px; padding: 30px;">
                    <i class="fa-solid fa-shield-halved text-3xl text-reyes-cyan mb-6"></i>
                    <h3 class="font-orbitron text-xl font-bold text-white mb-4">__PILAR3_TITLE__</h3>
                    <p class="text-reyes-silver leading-relaxed">__PILAR3_DESC__</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Notice Banner -->
    <div class="fixed bottom-0 left-0 w-full bg-reyes-cyan text-black py-3 px-4 text-center font-orbitron font-bold text-sm z-50">
        <i class="fa-solid fa-info-circle mr-2"></i> ESTO ES UNA MUESTRA DE DISEÑO CREADA POR REYES COMPUTING
    </div>

</body>
</html>"""

def main():
    print("Generating mockup landing pages...")
    for lead in leads:
        filename = f"mockup-{lead['id']}.html"
        html = html_template.replace("__COMPANY__", lead["company"])
        html = html.replace("__HERO_TITLE__", lead["hero_title"])
        html = html.replace("__HERO_SUBTITLE__", lead["hero_subtitle"])
        html = html.replace("__PILAR1_TITLE__", lead["pilar1_title"])
        html = html.replace("__PILAR1_DESC__", lead["pilar1_desc"])
        html = html.replace("__PILAR2_TITLE__", lead["pilar2_title"])
        html = html.replace("__PILAR2_DESC__", lead["pilar2_desc"])
        html = html.replace("__PILAR3_TITLE__", lead["pilar3_title"])
        html = html.replace("__PILAR3_DESC__", lead["pilar3_desc"])

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: {filename}")

if __name__ == "__main__":
    main()
