# murgenere-web

This repository contains a minimal React front‑end and a FastAPI back‑end for
`murgenere.com` and `my.murgenere.com`. The front‑end is a single HTML file that
loads React from a CDN. The back‑end exposes API endpoints that can call the
`filippobounous/personal` package when it is installed.

## Setup

1. **Install Python dependencies**

   ```bash
   python3 -m pip install fastapi uvicorn
   # Optional: install the personal package for real analysis
   python3 -m pip install git+https://github.com/filippobounous/personal.git
   ```

2. **Run the back‑end**

   ```bash
   python3 -m uvicorn backend.app:app --reload
   ```

   The server will listen on `http://localhost:8000`.

   During development the API is available on `http://localhost:8000`.
   When deployed, the front‑end will call the API on the same origin.

3. **Open the front‑end**

   Serve the `frontend` folder with any static web server, e.g.:

   ```bash
   cd frontend && python3 -m http.server 8080
   ```

   Then visit `http://localhost:8080` in your browser.
   - When accessed on a domain such as `murgenere.com`, the page shows a simple
     picture.
   - When accessed on `my.murgenere.com`, two sections appear: **Inventory** and
     **Investments**. Each button triggers a request to the back‑end which can
     use your personal Python package to perform analysis.

The front‑end uses standard `fetch` calls to `/api/inventory` and
`/api/investments` and displays the JSON response in an alert.
