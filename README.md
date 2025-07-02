# murgenere-web

This repository contains a minimal React front‑end and a FastAPI back‑end for
`murgenere.com`, `inventory.murgenere.com`, and `investments.murgenere.com`. The front‑end is a single HTML file that
loads React from a CDN. The back‑end exposes API endpoints that can call the
`filippobounous/fball` package when it is installed.

## Setup

1. **Install Python dependencies**

   ```bash
   python3 -m pip install fastapi uvicorn
  # Optional: install the fball package for real analysis
  python3 -m pip install git+https://github.com/filippobounous/fball.git
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

   By default the app determines what to display based on the host name. For
   local testing you can map custom sub‑domains to `127.0.0.1` in your
   `/etc/hosts` file, for example:

   ```
   127.0.0.1 murgenere.localhost inventory.localhost investments.localhost
   ```

   After that you can open:
   - `http://murgenere.localhost:8080` to view the picture shown on
     **murgenere.com**.
   - `http://inventory.localhost:8080` for the **Inventory** section.
   - `http://investments.localhost:8080` for the **Investments** section.

   On production the corresponding `*.murgenere.com` domains serve the same
   content.
  Each button triggers a request to the back‑end which can use your `fball`
  package to perform analysis.

The front‑end uses standard `fetch` calls to `/api/inventory` and
`/api/investments` and displays the JSON response in an alert.
