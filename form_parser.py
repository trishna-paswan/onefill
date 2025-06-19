from playwright.sync_api import sync_playwright
import re

def extract_fields_from_form(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()
        print(f"🌐 Navigating to {url}")
        page.goto(url, timeout=10000)
        page.wait_for_timeout(2000)  # Ensure form loads fully

        labels = set()
        blocks = page.locator('div[role="listitem"]')

        for i in range(blocks.count()):
            try:
                block = blocks.nth(i)
                label_els = block.locator('div[role="heading"], .M7eMe')

                for j in range(label_els.count()):
                    raw_label = label_els.nth(j).inner_text().strip()
                    clean_label = re.sub(r"[*:\n]+", "", raw_label).strip().lower()

                    if clean_label:
                        labels.add(clean_label)
                        break  # Stop at the first valid label
            except Exception as e:
                print(f"⚠️ Skipped block {i}: {e}")
                continue

        browser.close()
        print(f"✅ Extracted labels: {labels}")
        return labels
