#!/bin/bash

# Install browser needed by Playwright
playwright install chromium

# Start your Flask app
python app.py
