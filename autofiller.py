#autofiller.py
from playwright.sync_api import sync_playwright
from fuzzywuzzy import fuzz
import re, time

def fill_google_form(url, user_data):
    print(f"\n📝 Opening form: {url}")
    print(f"🧠 User Provided Fields: {list(user_data.keys())}")

    with sync_playwright() as p:
        # autofiller.py (update this line)
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])

        page = browser.new_page()
        page.goto(url)
        time.sleep(2)

        blocks = page.locator('div[role="listitem"]')
        inputs = page.locator('input[type="text"]')
        filled = 0

        print("🔍 Scanning form fields...")
        for i in range(inputs.count()):
            label = ""
            try:
                block = blocks.nth(i)
                label_el = block.locator('div[role="heading"]')
                raw_label = label_el.inner_text().strip()
                label = re.sub(r"[*:]", "", raw_label).strip()
            except:
                label = ""

            print(f"🧾 Cleaned Label: '{label}'")

            best_match = None
            best_score = 0
            for key in user_data:
                score = fuzz.token_sort_ratio(key.lower(), label.lower())
                print(f"  🔄 Matching user field '{key}' with form label '{label}' → score: {score}")
                if score > best_score and score >= 60:
                    best_match = key
                    best_score = score

            if best_match:
                print(f"✅ Filling: {label} with '{user_data[best_match]}'")
                inputs.nth(i).fill(user_data[best_match])
                filled += 1
            else:
                print(f"⚠️ No good match for: {label}")

        try:
            page.locator('div[role="button"]', has_text="Submit").click()
            time.sleep(1)
            print("🚀 Form submitted!")
        except:
            print("❌ Could not submit the form")

        browser.close()
        return filled
