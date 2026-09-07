# AgriAI — Crop Disease Detection & Farmer Advisory

This package contains both halves of the project, already configured to talk to each other:

```
Sih-backend/   FastAPI backend (AI model, database, weather, tickets)
frontend/      index.html — the AgriAI web app
```

## Quick start

**1. Start the backend** (leave this terminal running)

Mac/Linux:
```
cd Sih-backend
chmod +x start.sh
./start.sh
```

Windows:
```
cd Sih-backend
start.bat
```

First run installs dependencies (PyTorch + the Hugging Face model), so it can take a few minutes.
Wait for the console to print that the AI model loaded, then leave it running.
It serves at **http://127.0.0.1:8000**.

**2. Start the frontend** (in a second terminal)

Mac/Linux:
```
cd frontend
chmod +x start.sh
./start.sh
```

Windows:
```
cd frontend
start.bat
```

This serves `index.html` at **http://localhost:3000** using Node's `serve` package (installed
automatically via `npx`). If you don't have Node.js installed, use `python -m http.server 3000`
from inside the `frontend` folder instead.

**3. Open the app**

Go to **http://localhost:3000** in your browser. The status dot in the navbar should turn green,
confirming the frontend can reach the backend. From there:
- **Disease Diagnosis** — upload a crop leaf photo for an AI diagnosis
- **Weather & Risk** — live weather + pest/disease risk for a crop and location
- **Support Tickets** — submit a ticket with a photo and problem description
- **Expert View** — review and update submitted tickets

## Configuration notes

- The backend's CORS-allowed origins live in `Sih-backend/.env` (`ALLOWED_CORS_ORIGINS`). It's
  already set to allow `localhost:3000` and `:5173`. If you serve the frontend from a different
  port or domain, add it to that list and restart the backend.
- The frontend's backend address lives in `frontend/index.html`, near the top of the `<script>`
  tag: `const API_BASE = "http://127.0.0.1:8000";`. Change this if the backend runs somewhere
  other than your own machine on the default port.

## Troubleshooting

Open your browser's DevTools (F12) → Console/Network tab:
- **CORS error** → the frontend's origin isn't in `ALLOWED_CORS_ORIGINS` — add it and restart the backend.
- **Failed to fetch / connection refused** → the backend isn't running, or `API_BASE` points to the wrong address.
- **A response with a 400/422 status** → the connection is working; the request itself was rejected
  (e.g. a missing field or an unsupported image format) — the error message returned describes why.
