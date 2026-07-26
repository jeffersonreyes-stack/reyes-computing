import os

leads = [
    {
        "filename": "propuesta-gato-con-botas.html",
        "name": "Alexander",
        "company": "Gato con botas",
        "intro": "Entendemos que en \"Gato con botas\" buscas incrementar el servicio de restauración de tenis, generar más visitas a tu página y fidelizar a tus clientes potenciales. Es un modelo de negocio excelente y de alta demanda, donde el factor visual y la confianza son todo.",
        "pilar1_title": "Galería del 'Antes y Después'",
        "pilar1_desc": "Estructuramos una página web ultra rápida donde los usuarios puedan ver claramente la calidad de tus restauraciones de tenis con fotos dinámicas de antes y después, lo cual es la mejor prueba de confianza.",
        "pilar2_title": "Cotizaciones al instante",
        "pilar2_desc": "Colocamos botones estratégicos y un formulario muy sencillo para que el usuario pueda subir fotos de sus tenis directamente y solicitar una cotización por WhatsApp en un solo clic.",
        "pilar3_title": "Fidelización y Campañas de Visitas",
        "pilar3_desc": "Te ayudamos a estructurar la página para que, junto con campañas digitales en redes sociales (Instagram/Facebook) y Google, captes clientes repetitivos que confíen sus tenis de marca en tus manos."
    },
    {
        "filename": "propuesta-vad-fitness.html",
        "name": "Bhray",
        "company": "Vad Fitness",
        "intro": "Felicitaciones por tu proyecto; el sector de fitness tiene un potencial gigantesco en canales digitales, siempre y cuando se capte la atención del usuario de inmediato. En Reyes Computing no diseñamos páginas web informativas comunes. Creamos herramientas de venta.",
        "pilar1_title": "Captar prospectos calificados",
        "pilar1_desc": "Diseñamos páginas rápidas, optimizadas para móviles, con llamados a la acción claros para que los interesados se registren por asesorías, planes de entrenamiento, o membresías.",
        "pilar2_title": "Posicionar tu marca",
        "pilar2_desc": "Estructuramos el sitio para transmitir autoridad, profesionalismo y confianza, mostrando tus servicios o productos de forma atractiva.",
        "pilar3_title": "Facilitar la venta",
        "pilar3_desc": "Integramos botones de contacto directo (como WhatsApp) o formularios ágiles para que el proceso de inscripción o compra sea lo más sencillo posible para tus clientes."
    },
    {
        "filename": "propuesta-dyb-viajes.html",
        "name": "Damian",
        "company": "DyB Viajes",
        "intro": "Entendemos que en \"DyB Viajes\" buscan generar oportunidades comerciales para dar a conocer más destinos turísticos y captar viajeros interesados. El sector turístico es altamente dinámico y Google Ads es la herramienta perfecta para capturar a las personas en el momento exacto en que están planificando sus próximas vacaciones.",
        "pilar1_title": "Captar Intención de Búsqueda Activa",
        "pilar1_desc": "Mostramos tus anuncios en Google a personas que buscan términos de alta intención como \"paquetes turísticos baratos\", \"agencias de viajes en [Tu Ciudad]\" o destinos específicos.",
        "pilar2_title": "Landing Pages por Destinos",
        "pilar2_desc": "Para optimizar tu presupuesto, en lugar de enviar a todos al home de tu web, los dirigimos a páginas específicas del destino que buscaron con formularios de cotización rápidos.",
        "pilar3_title": "Campañas de Remarketing",
        "pilar3_desc": "Mostramos anuncios con tus mejores destinos en redes sociales y la red de Google a aquellas personas que ya visitaron tu web pero aún no han solicitado una cotización, recordándoles contactarse."
    },
    {
        "filename": "propuesta-max-tom.html",
        "name": "Gabriel",
        "company": "Max & Tom",
        "intro": "Recibimos tu solicitud para estructurar una estrategia comercial digital enfocada en promover la adopción de animales en situación de calle. Es un proyecto con un propósito excelente, y podemos impulsarlo aplicando el mismo sistema que usamos para acelerar las ventas de nuestros clientes.",
        "pilar1_title": "Sitio Web de Alta Conversión",
        "pilar1_desc": "En lugar de una web informativa básica, creamos una página optimizada y rápida donde se presenten las historias de los animales de forma emotiva, con un formulario de postulación ágil y persuasivo que capte los datos de los interesados.",
        "pilar2_title": "Publicidad en Google Ads y Redes Sociales",
        "pilar2_desc": "Configuramos campañas dirigidas a personas en tu zona geográfica que ya están buscando activamente adoptar mascotas, asegurando que tu presupuesto se dirija solo a adoptantes potenciales reales.",
        "pilar3_title": "Sistema de Gestión y Seguimiento",
        "pilar3_desc": "Automatizamos la recepción de datos. Cada persona interesada entrará a un sistema estructurado (CRM) para hacer seguimiento: Postulados -> Entrevistados -> Visitas -> Adopción exitosa."
    },
    {
        "filename": "propuesta-arepas-deeluxe.html",
        "name": "Jesika",
        "company": "Arepas rellenas Deeluxe",
        "intro": "Entendemos que buscan crear un sitio web de alta conversión para vender más y lograr que sus productos sean reconocidos por más personas. El sector de alimentos tiene un potencial increíble en internet si se presenta de la manera adecuada para generar antojo e interés de inmediato.",
        "pilar1_title": "Presentación Visual Impecable",
        "pilar1_desc": "Diseñamos una página web rápida y moderna donde tus arepas se muestren con fotografías de alta calidad que resalten su sabor y presentación, ideal tanto para consumidores finales como para distribuidores.",
        "pilar2_title": "Adaptabilidad a tu canal de ventas",
        "pilar2_desc": "Menú interactivo para delivery directo a WhatsApp, o catálogo digital optimizado para recibir pedidos al por mayor de tiendas, minimarkets y distribuidores.",
        "pilar3_title": "Conexión con campañas locales",
        "pilar3_desc": "Optimizamos la web para recibir visitas de anuncios en redes sociales dirigidos exactamente a la zona geográfica de tu público objetivo."
    },
    {
        "filename": "propuesta-distribuidora-amaro.html",
        "name": "Paola",
        "company": "Distribuidora de belleza Amaro",
        "intro": "Entendemos que buscas conseguir más visitas para tu negocio, incrementar tus ventas, ganar mayor reconocimiento de marca y atraer nuevos clientes de forma constante. La distribución de productos de belleza tiene una gran demanda en internet, y el canal ideal es Google Ads.",
        "pilar1_title": "Atraer Clientes Listos para Comprar",
        "pilar1_desc": "Configuramos anuncios de búsqueda para que cuando salones de belleza, estilistas o clientes finales busquen productos específicos en Google, tu negocio aparezca de primero.",
        "pilar2_title": "Anuncios de Ficha de Producto (Google Shopping)",
        "pilar2_desc": "Si cuentas con catálogo o tienda online, podemos mostrar directamente tus productos con foto y precio a quienes buscan comprar de inmediato.",
        "pilar3_title": "Medición y Retorno de Inversión (ROI)",
        "pilar3_desc": "Te ayudamos a configurar la medición de conversiones para que sepas exactamente cuántas personas te llaman, te escriben a WhatsApp o te compran en la web gracias a los anuncios."
    },
    {
        "filename": "propuesta-muebles-chichi.html",
        "name": "Walberto",
        "company": "Muebles colchones chichi 2",
        "intro": "Entendemos que buscan implementar una estrategia comercial digital integral con el objetivo de vender más y llegar a muchos nuevos clientes. La venta de muebles y colchones es un negocio competitivo pero altamente rentable en digital si se segmenta localmente.",
        "pilar1_title": "Landing Page de Ofertas de Temporada",
        "pilar1_desc": "Diseñamos una página web rápida y enfocada únicamente en tus productos más vendidos (colchones, camas, muebles) con fotos grandes, precios de oferta y botones flotantes para cotizar directamente por WhatsApp.",
        "pilar2_title": "Campañas de Publicidad Local",
        "pilar2_desc": "Creamos anuncios dirigidos únicamente a personas en tu ciudad o zona de influencia que estén buscando activamente cambiar de colchón o amueblar su hogar, asegurando que tu inversión atraiga visitas reales.",
        "pilar3_title": "Embudo de Ventas por WhatsApp / CRM",
        "pilar3_desc": "Configuramos un sistema simple para organizar los datos de todas las personas que preguntan precios, permitiéndote darles seguimiento rápido y cerrar más ventas diarias."
    }
]

html_template = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex">

    <!-- Google tag (gtag.js) - Google Ads -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-5529388450"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'AW-5529388450');
    </script>
    <title>Propuesta Comercial - __COMPANY__ | Reyes Computing</title>
    <meta name="description" content="Propuesta comercial personalizada para __COMPANY__.">
    <link rel="canonical" href="https://www.reyescomputing.com/__FILENAME__">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="assets/css/output.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link rel="icon" type="image/png" href="assets/images/favicon.png">

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18025178697"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'AW-18025178697');
    </script>
</head>
<body class="antialiased bg-reyes-black text-reyes-white">

    <nav class="fixed w-full z-50 transition-all duration-300 backdrop-blur-md border-b border-reyes-cyan/20 bg-reyes-black/90">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="index.html" class="flex items-center gap-3 group">
                <img src="assets/images/logo.png" alt="Reyes Computing" class="h-16 w-auto">
                <span class="font-orbitron text-xl font-bold tracking-widest uppercase text-white group-hover:text-reyes-cyan transition">Reyes<span class="text-reyes-cyan">Computing</span></span>
            </a>
            <div class="hidden md:flex items-center gap-8 text-sm font-sans tracking-wide text-reyes-silver">
                <a href="como-funciona.html" class="hover:text-reyes-cyan transition">Como Funciona</a>
                <a href="desarrollo-web.html" class="hover:text-reyes-cyan transition">Desarrollo Web</a>
                <a href="google-ads.html" class="hover:text-reyes-cyan transition">Google Ads</a>
                <a href="social-ads.html" class="hover:text-reyes-cyan transition">Social Ads B2B</a>
                <a href="contacto.html" class="px-6 py-2 border border-reyes-cyan text-reyes-cyan hover:bg-reyes-cyan hover:text-black transition uppercase text-xs font-bold tracking-widest shadow-neon">
                    Diagnóstico Inicial
                </a>
            </div>
            <button id="mobile-menu-btn" type="button" aria-label="Abrir menu principal" aria-expanded="false" aria-controls="mobile-menu" class="md:hidden text-reyes-cyan text-2xl focus:outline-none z-50">
                <i class="fa-solid fa-bars"></i>
            </button>
        </div>
    </nav>

    <div id="mobile-menu" class="fixed inset-0 bg-black/95 z-40 hidden flex flex-col justify-center items-center space-y-8 backdrop-blur-xl">
        <a href="como-funciona.html" class="text-2xl font-orbitron text-white hover:text-reyes-cyan transition mobile-link">Como Funciona</a>
        <a href="desarrollo-web.html" class="text-2xl font-orbitron text-white hover:text-reyes-cyan transition mobile-link">Desarrollo Web</a>
        <a href="google-ads.html" class="text-2xl font-orbitron text-white hover:text-reyes-cyan transition mobile-link">Google Ads</a>
        <a href="social-ads.html" class="text-2xl font-orbitron text-white hover:text-reyes-cyan transition mobile-link">Social Ads B2B</a>
        <a href="contacto.html" class="px-6 py-3 border border-reyes-cyan text-reyes-cyan hover:bg-reyes-cyan hover:text-black transition uppercase text-sm font-bold tracking-widest shadow-neon mobile-link">
            Diagnóstico Inicial
        </a>
    </div>

    <header class="relative min-h-screen flex items-center justify-center pt-20 overflow-hidden">
        <div class="absolute inset-0 z-0 bg-gradient-to-b from-reyes-black/50 via-reyes-black/80 to-reyes-black bg-grid opacity-20"></div>
        <div class="relative z-10 max-w-5xl mx-auto px-6 text-center">
            <p class="font-orbitron text-xs md:text-sm text-reyes-cyan uppercase tracking-[0.4em] mb-6">Propuesta Comercial Digital</p>
            <h1 class="font-orbitron text-4xl md:text-6xl font-bold text-white leading-tight mb-6">
                Hola __NAME__, hemos preparado esta propuesta para <span class="text-reyes-cyan">__COMPANY__</span>.
            </h1>
            <p class="font-sans text-lg md:text-xl text-reyes-silver mb-10 max-w-3xl mx-auto font-light leading-relaxed">
                __INTRO__
            </p>
            <div class="flex flex-col sm:flex-row justify-center gap-6">
                <a href="#propuesta" class="bg-reyes-cyan text-black px-8 py-4 font-bold tracking-widest uppercase hover:bg-white transition shadow-neon w-full sm:w-auto text-center font-orbitron">
                    Ver Propuesta
                </a>
                <a href="contacto.html" class="border border-white text-white px-8 py-4 font-bold tracking-widest uppercase hover:bg-white hover:text-black transition w-full sm:w-auto text-center font-orbitron">
                    Agendar Llamada
                </a>
            </div>
        </div>
    </header>

    <section id="propuesta" class="py-24 relative border-t border-white/5">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-20">
                <h2 class="font-orbitron text-3xl md:text-5xl font-bold text-white mb-6">Estrategia Propuesta</h2>
                <div class="w-24 h-1 bg-reyes-cyan mx-auto shadow-neon"></div>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                <!-- Pilar 1 -->
                <div class="bg-reyes-black border border-white/5 p-8 service-card" style="background-color: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 8px; padding: 30px;">
                    <i class="fa-solid fa-chart-line text-4xl text-reyes-cyan mb-6"></i>
                    <h3 class="font-orbitron text-xl font-bold text-white mb-4">__PILAR1_TITLE__</h3>
                    <p class="text-reyes-silver leading-relaxed text-lg">__PILAR1_DESC__</p>
                </div>

                <!-- Pilar 2 -->
                <div class="bg-reyes-black border border-white/5 p-8 service-card" style="background-color: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 8px; padding: 30px;">
                    <i class="fa-solid fa-bullseye text-4xl text-reyes-cyan mb-6"></i>
                    <h3 class="font-orbitron text-xl font-bold text-white mb-4">__PILAR2_TITLE__</h3>
                    <p class="text-reyes-silver leading-relaxed text-lg">__PILAR2_DESC__</p>
                </div>

                <!-- Pilar 3 -->
                <div class="bg-reyes-black border border-white/5 p-8 service-card" style="background-color: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 8px; padding: 30px;">
                    <i class="fa-solid fa-users text-4xl text-reyes-cyan mb-6"></i>
                    <h3 class="font-orbitron text-xl font-bold text-white mb-4">__PILAR3_TITLE__</h3>
                    <p class="text-reyes-silver leading-relaxed text-lg">__PILAR3_DESC__</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Cierre y Garantia Block -->
    <section class="py-24 relative bg-black border-t border-white/10">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <h2 class="font-orbitron text-3xl md:text-5xl font-bold text-white mb-8">El siguiente paso.</h2>
            <p class="text-reyes-silver text-lg leading-relaxed mb-10 text-lg">
                Nos gustaría conversar brevemente en una llamada de 10 a 15 minutos para mostrarte ejemplos y estimar un plan de trabajo. Agendemos una corta llamada por Google Meet o WhatsApp.
            </p>
            <a href="contacto.html" class="inline-block bg-reyes-cyan text-black px-10 py-4 font-bold tracking-widest uppercase hover:bg-white transition shadow-neon font-orbitron">
                Agendar Llamada Ahora
            </a>
        </div>
    </section>

    <footer class="border-t border-white/10 bg-reyes-black py-12 relative z-10">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid md:grid-cols-4 gap-12 mb-12">
                <div class="md:col-span-2">
                    <a href="index.html" class="flex items-center gap-3 mb-6">
                        <img src="assets/images/logo.png" alt="Reyes Computing" class="h-12 w-auto">
                        <span class="font-orbitron text-lg font-bold tracking-widest uppercase text-white">Reyes<span class="text-reyes-cyan">Computing</span></span>
                    </a>
                    <p class="text-reyes-silver mb-6 font-sans">Agencia de mercadeo especializada en desarrollo web de alta conversión y campañas B2B para LATAM.</p>
                </div>
                <div>
                    <h4 class="font-orbitron text-white mb-6 uppercase tracking-widest text-sm font-bold">Servicios</h4>
                    <ul class="space-y-3 font-sans text-sm text-reyes-silver">
                        <li><a href="desarrollo-web.html" class="hover:text-reyes-cyan transition">Desarrollo Web</a></li>
                        <li><a href="google-ads.html" class="hover:text-reyes-cyan transition">Google Ads</a></li>
                        <li><a href="social-ads.html" class="hover:text-reyes-cyan transition">Social Ads B2B</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-orbitron text-white mb-6 uppercase tracking-widest text-sm font-bold">Empresa</h4>
                    <ul class="space-y-3 font-sans text-sm text-reyes-silver">
                        <li><a href="contacto.html" class="hover:text-reyes-cyan transition">Contacto</a></li>
                        <li><a href="como-funciona.html" class="hover:text-reyes-cyan transition">Como Funciona</a></li>
                        <li><a href="#" class="hover:text-reyes-cyan transition">Aviso Legal</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 font-sans">
                <p class="text-reyes-silver text-sm">&copy; 2024 Reyes Computing. Todos los derechos reservados.</p>
                <div class="flex gap-4">
                    <a href="https://www.linkedin.com/company/110759974/" target="_blank" class="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center text-reyes-silver hover:border-reyes-cyan hover:text-reyes-cyan transition group">
                        <i class="fa-brands fa-linkedin-in group-hover:scale-110 transition"></i>
                    </a>
                    <a href="mailto:control@reyescomputing.com" class="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center text-reyes-silver hover:border-reyes-cyan hover:text-reyes-cyan transition group">
                        <i class="fa-regular fa-envelope group-hover:scale-110 transition"></i>
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        const links = document.querySelectorAll('.mobile-link');
        let isOpen = false;

        function toggleMenu() {
            isOpen = !isOpen;
            if(isOpen){
                menu.classList.remove('hidden');
                btn.innerHTML = '<i class="fa-solid fa-xmark"></i>';
                document.body.style.overflow = 'hidden';
            } else {
                menu.classList.add('hidden');
                btn.innerHTML = '<i class="fa-solid fa-bars"></i>';
                document.body.style.overflow = 'auto';
            }
        }
        btn.addEventListener('click', toggleMenu);
        links.forEach(link => {
            link.addEventListener('click', () => {
                if(isOpen) toggleMenu();
            });
        });
    </script>
</body>
</html>"""

for lead in leads:
    rendered_html = html_template.replace("__COMPANY__", lead["company"])
    rendered_html = rendered_html.replace("__FILENAME__", lead["filename"])
    rendered_html = rendered_html.replace("__NAME__", lead["name"])
    rendered_html = rendered_html.replace("__INTRO__", lead["intro"])
    rendered_html = rendered_html.replace("__PILAR1_TITLE__", lead["pilar1_title"])
    rendered_html = rendered_html.replace("__PILAR1_DESC__", lead["pilar1_desc"])
    rendered_html = rendered_html.replace("__PILAR2_TITLE__", lead["pilar2_title"])
    rendered_html = rendered_html.replace("__PILAR2_DESC__", lead["pilar2_desc"])
    rendered_html = rendered_html.replace("__PILAR3_TITLE__", lead["pilar3_title"])
    rendered_html = rendered_html.replace("__PILAR3_DESC__", lead["pilar3_desc"])

    with open(lead["filename"], "w", encoding="utf-8") as f:
        f.write(rendered_html)
    print(f"Generated {lead['filename']}")

print("Done generating proposal HTML pages.")
