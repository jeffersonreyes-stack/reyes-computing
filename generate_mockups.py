import os
import json

# Define the lead data extracted from the text files, now with theme variables
leads = [
    {
        "id": "arepas-deeluxe",
        "company": "Arepas rellenas Deeluxe",
        "niche": "Restaurante / Venta de Alimentos",
        "theme": {
            "primary": "#F97316", # Orange-500
            "primary_hover": "#EA580C", # Orange-600
            "bg": "#FFF7ED", # Orange-50
            "text": "#431407", # Orange-950
            "text_muted": "#7C2D12", # Orange-900
            "font_main": "'Poppins', sans-serif",
            "font_heading": "'Playfair Display', serif",
            "hero_img": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&q=80" # Burger/Food substitute
        },
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
        "theme": {
            "primary": "#E11D48", # Rose-600 (Red/Active)
            "primary_hover": "#BE123C", # Rose-700
            "bg": "#0F172A", # Slate-900
            "text": "#F8FAFC", # Slate-50
            "text_muted": "#94A3B8", # Slate-400
            "font_main": "'Inter', sans-serif",
            "font_heading": "'Oswald', sans-serif",
            "hero_img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80" # Gym
        },
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
        "theme": {
            "primary": "#3B82F6", # Blue-500
            "primary_hover": "#2563EB", # Blue-600
            "bg": "#F3F4F6", # Gray-100
            "text": "#111827", # Gray-900
            "text_muted": "#4B5563", # Gray-600
            "font_main": "'Roboto', sans-serif",
            "font_heading": "'Montserrat', sans-serif",
            "hero_img": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&q=80" # Sneakers
        },
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
        "theme": {
            "primary": "#D946EF", # Fuchsia-500
            "primary_hover": "#C026D3", # Fuchsia-600
            "bg": "#FDF4FF", # Fuchsia-50
            "text": "#4A044E", # Fuchsia-950
            "text_muted": "#701A75", # Fuchsia-900
            "font_main": "'Lato', sans-serif",
            "font_heading": "'Cormorant Garamond', serif",
            "hero_img": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&q=80" # Beauty products
        },
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
        "theme": {
            "primary": "#D97706", # Amber-600 (Wood tone)
            "primary_hover": "#B45309", # Amber-700
            "bg": "#FAFAF9", # Stone-50
            "text": "#1C1917", # Stone-900
            "text_muted": "#57534E", # Stone-500
            "font_main": "'Open Sans', sans-serif",
            "font_heading": "'Merriweather', serif",
            "hero_img": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&q=80" # Furniture
        },
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
        "theme": {
            "primary": "#0891B2", # Cyan-600 (Ocean/Sky)
            "primary_hover": "#0E7490", # Cyan-700
            "bg": "#FFFFFF", # White
            "text": "#0F172A", # Slate-900
            "text_muted": "#475569", # Slate-600
            "font_main": "'Nunito', sans-serif",
            "font_heading": "'Raleway', sans-serif",
            "hero_img": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&q=80" # Travel/Airplane
        },
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
        "theme": {
            "primary": "#10B981", # Emerald-500
            "primary_hover": "#059669", # Emerald-600
            "bg": "#F0FDF4", # Emerald-50
            "text": "#064E3B", # Emerald-900
            "text_muted": "#047857", # Emerald-700
            "font_main": "'Quicksand', sans-serif",
            "font_heading": "'Fredoka One', cursive",
            "hero_img": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&q=80" # Dog
        }
    }
]

html_template = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex">

    <title>Landing Page - __COMPANY__</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Fredoka+One&family=Inter:wght@400;600&family=Lato:wght@400;700&family=Merriweather:wght@700&family=Montserrat:wght@700&family=Nunito:wght@400;600&family=Open+Sans:wght@400;600&family=Oswald:wght@500;700&family=Playfair+Display:wght@700&family=Poppins:wght@400;600&family=Quicksand:wght@500;700&family=Raleway:wght@700&family=Roboto:wght@400;500&display=swap" rel="stylesheet">

    <style>
        :root {
            --primary: __PRIMARY__;
            --primary-hover: __PRIMARY_HOVER__;
            --bg-color: __BG__;
            --text-color: __TEXT__;
            --text-muted: __TEXT_MUTED__;
            --font-main: __FONT_MAIN__;
            --font-heading: __FONT_HEADING__;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: var(--font-main);
        }

        h1, h2, h3, .heading-font {
            font-family: var(--font-heading);
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
            transition: all 0.3s ease;
        }

        .btn-primary:hover {
            background-color: var(--primary-hover);
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        }

        .btn-outline {
            border: 2px solid var(--primary);
            color: var(--primary);
            transition: all 0.3s ease;
        }

        .btn-outline:hover {
            background-color: var(--primary);
            color: white;
        }

        .mockup-hero {
            background: linear-gradient(to right, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 100%),
                        url('__HERO_IMG__');
            background-size: cover;
            background-position: center;
        }

        .service-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
        }

        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        }

        .text-muted-custom {
            color: var(--text-muted);
        }

        .text-primary-custom {
            color: var(--primary);
        }
    </style>
</head>
<body class="antialiased">

    <!-- Header -->
    <nav class="fixed w-full z-50 transition-all duration-300 bg-white/90 backdrop-blur shadow-sm">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <span class="heading-font text-2xl font-bold tracking-tight text-gray-900">__COMPANY__</span>
            </div>
            <div class="hidden md:flex items-center gap-8 font-medium">
                <a href="#servicios" class="text-gray-600 hover:text-primary-custom transition">Servicios</a>
                <a href="#nosotros" class="text-gray-600 hover:text-primary-custom transition">Nosotros</a>
                <a href="#contacto" class="btn-primary px-6 py-2 rounded-full font-bold shadow-md">
                    Contactar
                </a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="relative min-h-[85vh] flex items-center pt-20 mockup-hero">
        <div class="relative z-10 max-w-7xl mx-auto px-6 w-full">
            <div class="max-w-2xl">
                <span class="inline-block px-4 py-1 rounded-full text-sm font-bold bg-white/20 text-white backdrop-blur mb-6 uppercase tracking-wider">
                    __NICHE__
                </span>
                <h1 class="text-5xl md:text-7xl font-bold text-white leading-tight mb-6 drop-shadow-lg">
                    __HERO_TITLE__
                </h1>
                <p class="text-xl text-gray-100 mb-10 max-w-xl leading-relaxed drop-shadow-md">
                    __HERO_SUBTITLE__
                </p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <a href="#contacto" class="btn-primary px-8 py-4 rounded-full font-bold text-center text-lg shadow-lg">
                        Agendar Cita
                    </a>
                    <a href="#servicios" class="px-8 py-4 rounded-full font-bold text-center text-lg border-2 border-white text-white hover:bg-white hover:text-black transition">
                        Ver Servicios
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Features Section -->
    <section id="servicios" class="py-24 relative">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold mb-6">Nuestros Servicios</h2>
                <div class="w-24 h-1 mx-auto" style="background-color: var(--primary);"></div>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                <div class="service-card p-8">
                    <div class="w-14 h-14 rounded-full flex items-center justify-center mb-6" style="background-color: var(--primary); color: white;">
                        <i class="fa-solid fa-star text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-4">__PILAR1_TITLE__</h3>
                    <p class="text-muted-custom leading-relaxed">__PILAR1_DESC__</p>
                </div>

                <div class="service-card p-8">
                    <div class="w-14 h-14 rounded-full flex items-center justify-center mb-6" style="background-color: var(--primary); color: white;">
                        <i class="fa-solid fa-bolt text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-4">__PILAR2_TITLE__</h3>
                    <p class="text-muted-custom leading-relaxed">__PILAR2_DESC__</p>
                </div>

                <div class="service-card p-8">
                    <div class="w-14 h-14 rounded-full flex items-center justify-center mb-6" style="background-color: var(--primary); color: white;">
                        <i class="fa-solid fa-check text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-4">__PILAR3_TITLE__</h3>
                    <p class="text-muted-custom leading-relaxed">__PILAR3_DESC__</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Banner -->
    <section class="py-20" style="background-color: var(--primary); color: white;">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <h2 class="text-4xl font-bold mb-8">¿Listo para dar el siguiente paso?</h2>
            <a href="#contacto" class="inline-block bg-white text-gray-900 px-10 py-4 rounded-full font-bold text-lg hover:shadow-xl transition transform hover:-translate-y-1">
                Contáctanos Hoy Mismo
            </a>
        </div>
    </section>

    <!-- Notice Banner -->
    <div class="fixed bottom-0 left-0 w-full bg-gray-900 text-white py-3 px-4 text-center text-xs z-50">
        <i class="fa-solid fa-info-circle mr-2"></i> Esta es una maqueta de diseño generada a medida para ilustrar cómo podría verse tu página web. Propuesta por Reyes Computing.
    </div>

</body>
</html>"""

def main():
    print("Generating custom-themed mockup landing pages...")
    for lead in leads:
        filename = f"mockup-{lead['id']}.html"

        # In case max-tom is missing fields, we provide fallbacks so it doesn't break
        hero_title = lead.get("hero_title", "Descubre nuestro increíble servicio hoy mismo.")
        hero_subtitle = lead.get("hero_subtitle", "La mejor solución adaptada a tus necesidades y las de tu negocio.")

        pilar1_title = lead.get("pilar1_title", "Servicio Profesional")
        pilar1_desc = lead.get("pilar1_desc", "Brindamos atención personalizada para garantizar tu éxito.")
        pilar2_title = lead.get("pilar2_title", "Calidad Garantizada")
        pilar2_desc = lead.get("pilar2_desc", "Trabajamos con los más altos estándares para ofrecerte lo mejor.")
        pilar3_title = lead.get("pilar3_title", "Atención Rápida")
        pilar3_desc = lead.get("pilar3_desc", "Respondemos a todas tus inquietudes en tiempo récord.")


        html = html_template.replace("__COMPANY__", lead["company"])
        html = html.replace("__NICHE__", lead["niche"])
        html = html.replace("__HERO_TITLE__", hero_title)
        html = html.replace("__HERO_SUBTITLE__", hero_subtitle)
        html = html.replace("__PILAR1_TITLE__", pilar1_title)
        html = html.replace("__PILAR1_DESC__", pilar1_desc)
        html = html.replace("__PILAR2_TITLE__", pilar2_title)
        html = html.replace("__PILAR2_DESC__", pilar2_desc)
        html = html.replace("__PILAR3_TITLE__", pilar3_title)
        html = html.replace("__PILAR3_DESC__", pilar3_desc)

        # Theme variables
        theme = lead["theme"]
        html = html.replace("__PRIMARY__", theme["primary"])
        html = html.replace("__PRIMARY_HOVER__", theme["primary_hover"])
        html = html.replace("__BG__", theme["bg"])
        html = html.replace("__TEXT__", theme["text"])
        html = html.replace("__TEXT_MUTED__", theme["text_muted"])
        html = html.replace("__FONT_MAIN__", theme["font_main"])
        html = html.replace("__FONT_HEADING__", theme["font_heading"])
        html = html.replace("__HERO_IMG__", theme["hero_img"])

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: {filename}")

if __name__ == "__main__":
    main()
