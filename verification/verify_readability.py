from playwright.sync_api import sync_playwright
import os

def check_visibility():
    cwd = os.getcwd()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Define files to check
        files = ["finops.html", "devops.html", "seguridad.html"]

        for filename in files:
            # Construct file URL
            file_url = f"file://{cwd}/{filename}"
            print(f"Checking {file_url}...")

            page.goto(file_url)

            # Wait for the hero section to load (it's static, but good practice)
            page.wait_for_selector('h1')

            # Take a screenshot of the viewport (which covers the hero)
            screenshot_path = f"verification/{filename.replace('.html', '_hero_readability.png')}"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    check_visibility()
