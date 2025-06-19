#app.py
from flask import Flask, request, render_template
from form_parser import extract_fields_from_form
from autofiller import fill_google_form
from fuzzywuzzy import fuzz
import re

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    from fuzzywuzzy import fuzz

    urls = [url.strip() for url in request.form["form_urls"].splitlines() if url.strip()]
    raw_fields = set()

    for url in urls:
        try:
            fields = extract_fields_from_form(url)
            raw_fields.update(fields)
        except Exception as e:
            print(f"❌ Failed to extract from {url}: {e}")

    # Step 1: Manual normalization map
    normalization_map = {
        "full name": "name",
        "name": "name",
        "email address": "email",
        "phone number": "phone",
        "mobile number": "phone",
        "dob": "date of birth",
        "roll number": "roll number",
        "date of birth": "date of birth",
        "address": "address"
    }

    normalized_fields = set()
    for field in raw_fields:
        key = field.lower().strip()
        normalized_fields.add(normalization_map.get(key, field.strip()))

    # Step 2: Remove fuzzy duplicates (keep shortest name if similar)
    final_fields = []
    threshold = 80

    for new_field in sorted(normalized_fields):
        matched = False
        for i, existing in enumerate(final_fields):
            score = fuzz.token_sort_ratio(new_field.lower(), existing.lower())
            if score >= threshold:
                # Keep shorter version
                if len(new_field) < len(existing):
                    final_fields[i] = new_field
                matched = True
                break
        if not matched:
            final_fields.append(new_field)

    return render_template("unified_form.html", fields=sorted(final_fields), urls=urls)

@app.route("/fill", methods=["POST"])
def fill():
    user_data = {k: v for k, v in request.form.items() if k != "urls"}
    urls = request.form.getlist("urls")
    results = []

    for url in urls:
        filled = fill_google_form(url, user_data)
        results.append((url, filled))

    return render_template("success.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
