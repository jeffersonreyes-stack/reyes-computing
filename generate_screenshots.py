from playwright.sync_api import sync_playwright
import os
import time

proposals = [
    {"file": "propuesta-gato-con-botas.html", "folder": "gato-con-botas"},
    {"file": "propuesta-vad-fitness.html", "folder": "vad-fitness"},
    {"file": "propuesta-dyb-viajes.html", "folder": "dyb-viajes"},
    {"file": "propuesta-max-tom.html", "folder": "max-tom"},
    {"file": "propuesta-arepas-deeluxe.html", "folder": "arepas-deeluxe"},
    {"file": "propuesta-distribuidora-amaro.html", "folder": "distribuidora-amaro"},
    {"file": "propuesta-muebles-chichi.html", "folder": "muebles-chichi"}
]

base_dir = "/app/capturas_propuestas"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

def generate_screens():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for p_info in proposals:
            # Crear la carpeta de la propuesta
            folder_path = os.path.join(base_dir, p_info["folder"])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Cargar la pagina
            filepath = f"file:///app/{p_info['file']}"
            print(f"Abriendo {filepath}...")
            page.goto(filepath)

            # Dar un momento para cargar fuentes/imágenes
            time.sleep(2)

            # Tomar captura
            screenshot_path = os.path.join(folder_path, f"{p_info['folder']}.png")
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Guardado: {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    generate_screens()
    print("Todas las capturas generadas con éxito.")
