# shipment-tracker
Shipment Tracker — How I built it (step-by-step + lessons learned)
Summary

This mini project is a simple Shipment Tracker web app built with Flask (Python). It uses fake tracking data for demos (so you don’t need carrier credentials). The goal: a portfolio piece that shows API knowledge, web development, and Dev workflow.

Step-by-step (what we actually did)

Created the GitHub repo

shipment-tracker repo created on GitHub with a README.md.

Prepared local project structure

Files: app.py, requirements.txt, templates/index.html, README.md.

Wrote a simple Flask app (app.py)

Routes:

/ — show form and accept tracking ID.

POST handler — lookup tracking ID from a fake dataset and show status.

Added HTML templates in templates/ (basic UI: create + track forms).

Saved minimal dependencies to requirements.txt (e.g., flask).

Tried to run app but hit common problems (and fixed them)

Mistake: tried to run a folder path as a command.
→ Fix: use cd <folder> to change directory first.

Mistake: pip not recognized.
→ Fix: install Python or use python -m pip once Python is available.

Mistake: python --version returned not found because Python path not set.
→ Fix: install Python and enable Add Python to PATH or set PATH manually.

Mistake: nested folder structure (project folder inside another identically-named folder).
→ Fix: cd into the inner folder where app.py actually is.

Installed dependencies and ran the app locally:

python -m pip install -r requirements.txt

python app.py → open http://127.0.0.1:5000.

Tested the app using built-in fake tracking IDs like ABC123, XYZ789.

Next (optional): deploy the app (Render, Railway, Heroku) to make it publicly accessible.

Exact commands you can copy/paste (Windows)
cd C:\Users\Richard\OneDrive\Desktop\work\shipment-tracker-main\shipment-tracker-main
python --version                 # check Python
python -m pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000 in your browser


If pip is missing, run:

python -m pip install flask


If python not found, download & install from https://python.org
 and make sure Add Python to PATH is checked.

Common mistakes we encountered (short)

Trying to run a folder path as an executable (use cd instead).

pip not found — Python not in PATH or not installed.

Working from parent folder instead of the folder containing app.py.

requirements.txt empty or missing — install packages manually if needed.

Tools & skills learned

Python — basic scripting and running a web server.

Flask — lightweight web framework for building web apps and routes.

HTML Templates — simple UI using templates/index.html and Jinja in Flask.

pip / virtualenv — dependency management and creating isolated environments.

Git & GitHub — repo creation, pushing code, and version control.

EasyPost (concept) — API for fake/test shipments (we can integrate later).

Local debugging — how to read terminal/server logs and fix path & dependency errors.

Deployment options (next step) — Render, Railway, Heroku (connect repo for automatic deploy).

How this helps me (CV / interview points)

“Built a shipment-tracking demo using Flask to simulate a carrier API.”

“Solved environment & path issues while configuring Python — comfortable debugging dev setups.”

“Can integrate real carrier APIs (EasyPost/FedEx) later and deploy a full demo.”

Next steps / suggestions

Replace fake data with EasyPost test mode to create fake shipments & get test tracking IDs.

Add a small SQLite DB to persist created shipments and scan events.

Add more front-end polish (Bootstrap/Tailwind) and a few demo screenshots/GIFs.

Deploy on Render and add live demo link to README and resume.
