# ===================== form_parser.py =====================
from playwright.sync_api import sync_playwright
import re

def extract_fields_from_form(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(1500)
        blocks = page.locator('div[role="listitem"]')

        labels = set()
        for i in range(blocks.count()):
            try:
                label_el = blocks.nth(i).locator('div[role="heading"]')
                raw_label = label_el.inner_text().strip()
                # 🧼 Clean label here itself
                clean_label = re.sub(r"[*:\n]+", "", raw_label).strip()
                labels.add(clean_label)
            except:
                continue

        browser.close()
        return labels
