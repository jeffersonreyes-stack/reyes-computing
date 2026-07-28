import os
import json

# Define the lead data extracted from the text files, now with DIRECT RESPONSE COPYWRITING
leads = [
    {
        "id": "arepas-deeluxe",
        "company": "Arepas rellenas Deeluxe",
        "niche": "Comida Rápida Premium",
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
        "hero_title": "El Antojo Perfecto, Caliente y Directo a tu Puerta en Minutos.",
        "hero_subtitle": "Crujientes por fuera, absurdamente rellenas por dentro. Deja de buscar, acabas de encontrar tu nueva obsesión. ¡Pide ahora antes de que se agoten!",
        "cta_primary": "¡Quiero mi Arepa Ahora! 🤤",
        "cta_secondary": "Ver Menú Completo",
        "trust_badge": "Más de 5,000 clientes felices este mes",
        "pilar1_title": "Pide en 3 Clics por WhatsApp",
        "pilar1_desc": "Sin registros tediosos. Elige tus ingredientes, presiona un botón y tu pedido llega directo a nuestra cocina. Así de rápido.",
        "pilar2_title": "Distribuidores: Multipliquen sus Ventas",
        "pilar2_desc": "Nuestras arepas congeladas tienen una rotación altísima. Accede a precios exclusivos por volumen y garantiza un producto que tus clientes amarán.",
        "pilar3_title": "Sabor 100% Garantizado",
        "pilar3_desc": "Si nuestra arepa no es la más rellena y deliciosa que has probado en la zona, te devolvemos tu dinero. Sin preguntas."
    },
    {
        "id": "vad-fitness",
        "company": "Vad Fitness",
        "niche": "Transformación Física",
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
        "hero_title": "Deja las Excusas. Construye el Cuerpo que Siempre Has Querido.",
        "hero_subtitle": "Programas de entrenamiento diseñados para resultados reales, no promesas vacías. Únete hoy y nota la diferencia en solo 30 días.",
        "cta_primary": "¡Empezar mi Transformación! 🔥",
        "cta_secondary": "Ver Casos de Éxito",
        "trust_badge": "+500 Vidas Transformadas",
        "pilar1_title": "Planes a tu Medida",
        "pilar1_desc": "No más rutinas genéricas. Evaluamos tu nivel y creamos un mapa exacto para quemar grasa o ganar músculo de forma eficiente.",
        "pilar2_title": "Comunidad que te Impulsa",
        "pilar2_desc": "Entrena en un ambiente donde rendirse no es opción. Nuestros coaches y miembros te mantendrán motivado todos los días.",
        "pilar3_title": "Garantía de Resultados",
        "pilar3_desc": "Sigue nuestro programa al pie de la letra por 30 días. Si no ves cambios reales en el espejo, te asesoramos gratis hasta que los veas."
    },
    {
        "id": "gato-con-botas",
        "company": "Gato con botas",
        "niche": "Sneaker Restoration",
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
        "hero_title": "No Tires Tus Tenis Favoritos. Nosotros los Hacemos Lucir como Nuevos.",
        "hero_subtitle": "Servicio premium de limpieza profunda y restauración experta. Revive tus sneakers y ahorra dinero.",
        "cta_primary": "¡Cotizar mi Restauración Gratis! 👟",
        "cta_secondary": "Ver Galería Antes/Después",
        "trust_badge": "Especialistas en Marcas Premium (Nike, Jordan, Yeezy)",
        "pilar1_title": "El 'Shock' del Antes y Después",
        "pilar1_desc": "Eliminamos manchas imposibles, restauramos el color original y devolvemos la textura. Te garantizamos que no creerás que son los mismos tenis.",
        "pilar2_title": "Cotización Inmediata por Foto",
        "pilar2_desc": "No tienes que moverte. Toma una foto con tu celular, envíala a nuestro WhatsApp y recibe un presupuesto exacto en menos de 10 minutos.",
        "pilar3_title": "Protección Total de tus Pares",
        "pilar3_desc": "Sabemos cuánto valen tus sneakers. Utilizamos productos importados especializados que no dañan los materiales, cuidando tu inversión."
    },
    {
        "id": "distribuidora-amaro",
        "company": "Distribuidora de belleza Amaro",
        "niche": "Insumos de Belleza Mayorista",
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
        "hero_title": "Abastece tu Salón con las Mejores Marcas, Sin Pagar de Más.",
        "hero_subtitle": "El catálogo mayorista más completo para profesionales de la belleza. Precios inmejorables, envíos rápidos y stock garantizado.",
        "cta_primary": "¡Solicitar Lista de Precios Mayorista! 💄",
        "cta_secondary": "Explorar Catálogo de Marcas",
        "trust_badge": "Proveedor de Confianza de +300 Salones Exitosos",
        "pilar1_title": "Márgenes de Ganancia Reales",
        "pilar1_desc": "Nuestros precios exclusivos para profesionales te permiten aumentar la rentabilidad de tu negocio desde el primer pedido.",
        "pilar2_title": "Pedidos Rápidos y Sin Estrés",
        "pilar2_desc": "Olvídate de procesos lentos. Revisa nuestro catálogo digital, arma tu pedido y ciérralo directamente por WhatsApp en minutos.",
        "pilar3_title": "Asesoría para tu Negocio",
        "pilar3_desc": "No solo vendemos productos, te asesoramos sobre las tendencias y marcas que más rotación tienen para que tu inversión siempre sea segura."
    },
    {
        "id": "muebles-chichi",
        "company": "Muebles colchones chichi 2",
        "niche": "Hogar y Descanso",
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
        "hero_title": "Duerme Mejor y Renueva tu Hogar con Ofertas de Locura.",
        "hero_subtitle": "Colchones ortopédicos y muebles modernos directo de fábrica. Máxima calidad a precios que no volverás a ver. ¡Aprovecha la liquidación de temporada!",
        "cta_primary": "¡Ver Ofertas de Temporada! 🛏️",
        "cta_secondary": "Consultar Precios por WhatsApp",
        "trust_badge": "Garantía de Fábrica de hasta 10 Años",
        "pilar1_title": "Descanso que Cambia tu Vida",
        "pilar1_desc": "Pasas 8 horas al día en tu cama. Nuestros colchones de alta tecnología eliminan el dolor de espalda y garantizan un sueño profundo y reparador.",
        "pilar2_title": "Diseño Moderno, Precio Justo",
        "pilar2_desc": "Salas y comedores que hacen lucir tu casa como de revista, fabricados con materiales duraderos, sin los sobrecostos de las grandes cadenas.",
        "pilar3_title": "Cotización y Entrega Rápida",
        "pilar3_desc": "Pregunta por el modelo que te gusta con un clic y te damos precio, disponibilidad y opciones de entrega en el mismo día."
    },
    {
        "id": "dyb-viajes",
        "company": "DyB Viajes",
        "niche": "Agencia de Viajes B2C",
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
        "hero_title": "Tus Vacaciones Soñadas, Planificadas a la Perfección y Sin Estrés.",
        "hero_subtitle": "Desde las playas del Caribe hasta tours en Europa. Paquetes con todo incluido y tarifas secretas que los buscadores online no te muestran.",
        "cta_primary": "¡Cotizar mi Viaje Gratis! ✈️",
        "cta_secondary": "Ver Destinos en Promoción",
        "trust_badge": "Agencia Certificada - Pagos 100% Seguros",
        "pilar1_title": "Asesoría Experta, No un Robot",
        "pilar1_desc": "No te arriesgues a equivocarte comprando solo. Diseñamos un itinerario a tu medida, optimizando tu presupuesto para que disfrutes como VIP.",
        "pilar2_title": "Ofertas de Último Minuto (Reales)",
        "pilar2_desc": "Tenemos acceso a bloqueos de aerolíneas y hoteles con descuentos de hasta un 30% en temporadas altas. Si buscas viajar pronto, somos tu mejor opción.",
        "pilar3_title": "Respaldo Total 24/7",
        "pilar3_desc": "¿Cancelaron un vuelo? ¿Problemas en el hotel? Nosotros lo resolvemos. Viaja con la tranquilidad de que siempre tienes a alguien respaldándote."
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
        },
        "hero_title": "No Compres un Amigo, Salva una Vida. Adopta Hoy.",
        "hero_subtitle": "Decenas de peluditos rescatados están esperando un hogar lleno de amor. Conoce sus historias y encuentra al compañero perfecto para tu familia.",
        "cta_primary": "¡Quiero Adoptar un Peludito! 🐾",
        "cta_secondary": "Conocer a los Rescatados",
        "trust_badge": "Proceso de adopción seguro y responsable",
        "pilar1_title": "Amor Incondicional Garantizado",
        "pilar1_desc": "Una mascota rescatada sabe que le salvaste la vida. La lealtad y el agradecimiento que recibirás cambiarán tu vida para siempre.",
        "pilar2_title": "Proceso Ágil, Cero Burocracia",
        "pilar2_desc": "Cuidamos a nuestros animales, pero no te ponemos trabas imposibles. Completa un formulario sencillo y te guiaremos paso a paso hasta que estén juntos.",
        "pilar3_title": "Sanos y Listos para Amar",
        "pilar3_desc": "Todos nuestros peluditos se entregan desparasitados, vacunados y con evaluación veterinaria, listos para integrarse a su nueva familia."
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
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Fredoka+One&family=Inter:wght@400;600;800&family=Lato:wght@400;700;900&family=Merriweather:wght@700;900&family=Montserrat:wght@700;900&family=Nunito:wght@400;600;800&family=Open+Sans:wght@400;600;800&family=Oswald:wght@500;700&family=Playfair+Display:wght@700;900&family=Poppins:wght@400;600;800&family=Quicksand:wght@500;700&family=Raleway:wght@700;900&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">

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
            letter-spacing: -0.02em;
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
            transition: all 0.3s ease;
            box-shadow: 0 4px 14px 0 rgba(0, 0, 0, 0.39);
        }

        .btn-primary:hover {
            background-color: var(--primary-hover);
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        }

        .mockup-hero {
            background: linear-gradient(to right, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.6) 100%),
                        url('__HERO_IMG__');
            background-size: cover;
            background-position: center;
        }

        .service-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
            border-top: 4px solid var(--primary);
        }

        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 30px -10px rgba(0,0,0,0.1);
        }

        .text-muted-custom {
            color: var(--text-muted);
        }

        .text-primary-custom {
            color: var(--primary);
        }

        .trust-badge-container {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(5px);
            border-left: 3px solid var(--primary);
        }
    </style>
</head>
<body class="antialiased">

    <!-- Promo Banner Top -->
    <div class="w-full text-center py-2 text-sm font-bold text-white tracking-wide z-50" style="background-color: var(--primary-hover);">
        🔥 ¡OFERTA LIMITADA! Consulta nuestras promociones exclusivas del mes 🔥
    </div>

    <!-- Header -->
    <nav class="w-full transition-all duration-300 bg-white/95 backdrop-blur shadow-sm sticky top-0 z-40 border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <span class="heading-font text-2xl font-black tracking-tight text-gray-900">__COMPANY__</span>
            </div>
            <div class="hidden md:flex items-center gap-8 font-semibold">
                <a href="#beneficios" class="text-gray-700 hover:text-primary-custom transition">Beneficios</a>
                <a href="#contacto" class="btn-primary px-6 py-2.5 rounded-full font-bold shadow-md text-sm uppercase tracking-wider">
                    __CTA_SECONDARY__
                </a>
            </div>
        </div>
    </nav>

    <!-- Direct Response Hero Section -->
    <header class="relative min-h-[85vh] flex items-center pt-10 mockup-hero">
        <div class="relative z-10 max-w-7xl mx-auto px-6 w-full">
            <div class="max-w-3xl">
                <div class="trust-badge-container inline-flex items-center px-4 py-2 rounded mb-8 text-white font-medium text-sm">
                    <span class="text-yellow-400 mr-2">★★★★★</span> __TRUST_BADGE__
                </div>
                <h1 class="text-5xl md:text-7xl font-black text-white leading-tight mb-6 drop-shadow-2xl">
                    __HERO_TITLE__
                </h1>
                <p class="text-xl md:text-2xl text-gray-100 mb-10 max-w-2xl leading-relaxed drop-shadow-md font-medium">
                    __HERO_SUBTITLE__
                </p>
                <div class="flex flex-col sm:flex-row gap-5 items-center">
                    <a href="#contacto" class="btn-primary w-full sm:w-auto px-10 py-5 rounded-full font-black text-center text-lg uppercase tracking-wide">
                        __CTA_PRIMARY__
                    </a>
                    <span class="text-gray-300 text-sm font-medium"><i class="fa-solid fa-lock mr-1"></i> Rápido y Seguro</span>
                </div>
            </div>
        </div>
    </header>

    <!-- Persuasive Features Section -->
    <section id="beneficios" class="py-24 relative bg-gray-50">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16 max-w-3xl mx-auto">
                <h2 class="text-4xl md:text-5xl font-black mb-6 text-gray-900">Por qué somos tu mejor decisión hoy</h2>
                <div class="w-24 h-1.5 mx-auto rounded-full mb-6" style="background-color: var(--primary);"></div>
                <p class="text-xl text-gray-600 font-medium">No somos una opción más. Somos la solución exacta que estabas buscando.</p>
            </div>

            <div class="grid md:grid-cols-3 gap-10">
                <div class="service-card p-10">
                    <div class="w-16 h-16 rounded-2xl flex items-center justify-center mb-6 shadow-lg transform -translate-y-4" style="background-color: var(--primary); color: white;">
                        <i class="fa-solid fa-fire-flame-curved text-3xl"></i>
                    </div>
                    <h3 class="text-2xl font-bold mb-4 text-gray-900">__PILAR1_TITLE__</h3>
                    <p class="text-muted-custom leading-relaxed text-lg">__PILAR1_DESC__</p>
                </div>

                <div class="service-card p-10">
                    <div class="w-16 h-16 rounded-2xl flex items-center justify-center mb-6 shadow-lg transform -translate-y-4" style="background-color: var(--primary); color: white;">
                        <i class="fa-solid fa-chart-line text-3xl"></i>
                    </div>
                    <h3 class="text-2xl font-bold mb-4 text-gray-900">__PILAR2_TITLE__</h3>
                    <p class="text-muted-custom leading-relaxed text-lg">__PILAR2_DESC__</p>
                </div>

                <div class="service-card p-10">
                    <div class="w-16 h-16 rounded-2xl flex items-center justify-center mb-6 shadow-lg transform -translate-y-4" style="background-color: var(--primary); color: white;">
                        <i class="fa-solid fa-shield-check text-3xl"></i>
                    </div>
                    <h3 class="text-2xl font-bold mb-4 text-gray-900">__PILAR3_TITLE__</h3>
                    <p class="text-muted-custom leading-relaxed text-lg">__PILAR3_DESC__</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Aggressive CTA Banner -->
    <section class="py-24 relative overflow-hidden" style="background-color: var(--primary); color: white;">
        <div class="absolute inset-0 bg-black/10"></div>
        <div class="max-w-4xl mx-auto px-6 text-center relative z-10">
            <h2 class="text-4xl md:text-6xl font-black mb-8 leading-tight">La indecisión te está costando resultados.</h2>
            <p class="text-xl mb-10 font-medium opacity-90">Únete a los clientes que ya están disfrutando de nuestra calidad y servicio superior. Toma acción ahora.</p>
            <a href="#contacto" class="inline-block bg-white text-gray-900 px-12 py-5 rounded-full font-black text-xl shadow-[0_0_40px_rgba(255,255,255,0.3)] hover:shadow-[0_0_60px_rgba(255,255,255,0.5)] transition transform hover:-translate-y-2 uppercase tracking-wide">
                __CTA_PRIMARY__
            </a>
            <p class="mt-6 text-sm opacity-80"><i class="fa-regular fa-clock"></i> Responderemos en menos de 15 minutos.</p>
        </div>
    </section>

    <!-- Notice Banner -->
    <div class="fixed bottom-0 left-0 w-full bg-gray-900 text-gray-300 py-3 px-4 text-center text-xs z-50 border-t border-gray-800">
        <i class="fa-solid fa-info-circle mr-1"></i> <strong>ALTA CONVERSIÓN:</strong> Esta es una maqueta de diseño con Copywriting Estratégico (Textos persuasivos) propuesta por <strong>Reyes Computing</strong> para disparar tus ventas.
    </div>

</body>
</html>"""

def main():
    print("Generating High-Conversion Direct Response Mockups...")
    for lead in leads:
        filename = f"mockup-{lead['id']}.html"

        html = html_template.replace("__COMPANY__", lead["company"])
        html = html.replace("__NICHE__", lead["niche"])
        html = html.replace("__HERO_TITLE__", lead["hero_title"])
        html = html.replace("__HERO_SUBTITLE__", lead["hero_subtitle"])
        html = html.replace("__CTA_PRIMARY__", lead["cta_primary"])
        html = html.replace("__CTA_SECONDARY__", lead["cta_secondary"])
        html = html.replace("__TRUST_BADGE__", lead["trust_badge"])
        html = html.replace("__PILAR1_TITLE__", lead["pilar1_title"])
        html = html.replace("__PILAR1_DESC__", lead["pilar1_desc"])
        html = html.replace("__PILAR2_TITLE__", lead["pilar2_title"])
        html = html.replace("__PILAR2_DESC__", lead["pilar2_desc"])
        html = html.replace("__PILAR3_TITLE__", lead["pilar3_title"])
        html = html.replace("__PILAR3_DESC__", lead["pilar3_desc"])

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