# 🌍 OneFill – Multi-Google Form AutoFiller with AI Matching
<p align="center"> <img src="https://socialify.git.ci/trishna-paswan/onefill/image?font=Bitter&language=1&name=1&owner=1&pattern=Solid&stargazers=1&theme=Dark" alt="OneFill Banner" /> </p>
OneFill is an intelligent, web-based autofiller that allows users to submit multiple Google Forms at once using a single unified form. It extracts required fields from each form, smartly merges them, and uses AI-based fuzzy matching to auto-fill each form accurately.


<p align="center"> <img src="https://img.shields.io/badge/Built%20With-Flask-blue.svg" /> <img src="https://img.shields.io/badge/Web%20Automation-Playwright-green.svg" /> <img src="https://img.shields.io/badge/AI%20Matching-FuzzyWuzzy-yellow.svg" /> <img src="https://img.shields.io/badge/Deployed%20On-Render-purple.svg" /> </p>
---
### 📌 Features
✅ Multiple Form Support

✅ Smart Field Extraction via Playwright

✅ Unified Input Form for all fields

✅ Fuzzy Matching between input & form labels

✅ Auto Submission to all Google Forms

✅ Live Deployment using Render
---

### 🖥️ Demo
🌐 Try it live here:
🔗 https://onefill.onrender.com
---

### 🛠️ Tech Stack

| Layer        | Technology                |
|--------------|---------------------------|
| Backend      | Python, Flask             |
| Automation   | Playwright                |
| AI Matching  | FuzzyWuzzy + Levenshtein  |
| Frontend     | HTML, Tailwind CSS|
| Deployment   | Render                    |
---
### 🚀 How It Works
Paste Google Form URLs

We extract field labels using Playwright

You fill a unified form on our site

We auto-match fields using AI (FuzzyWuzzy)

Forms are filled and submitted automatically!
---
### 🧪 Local Setup
1. Clone the Repository
git clone https://github.com/trishna-paswan/onefill.git
cd onefill
2. Create a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install Requirements
pip install -r requirements.txt
playwright install chromium
4. Run the App
python app.py
Visit: http://localhost:10000
---
### ✨ Author
Made with ❤️ by Trishna Kumari Paswan
📧 Connect on GitHub
