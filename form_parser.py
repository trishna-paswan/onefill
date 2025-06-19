
from playwright.sync_api import sync_playwright
import re

def extract_fields_from_form(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()
        print(f"🌐 Navigating to {url}")
        page.goto(url, timeout=10000)
        page.wait_for_timeout(2000)  # Wait for full form load

        labels = set()

        # Target all form question blocks
        blocks = page.locator('div[role="listitem"]')

        for i in range(blocks.count()):
            try:
                label_el = blocks.nth(i).locator('div[role="heading"], .M7eMe').first
                raw_label = label_el.inner_text().strip()
                clean_label = re.sub(r"[*:\n]+", "", raw_label).strip().lower()

                if clean_label:
                    labels.add(clean_label)
            except Exception as e:
                print(f"⚠️ Skipped block {i}: {e}")
                continue


        browser.close()

        print(f"✅ Extracted labels: {labels}")
        return labels
