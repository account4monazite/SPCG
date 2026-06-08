# Spotify Playlist Cover Generator (SPCG)

A full-stack playlist cover generator with:
- a React + Vite frontend
- a FastAPI backend
- collage-based cover generation using Unsplash/Pexels
- optional AI cover generation using Hugging Face inference

## Structure

- `backend/`
  - `main.py` — has FastAPI endpoints
  - `unsplash_cover.py` — collage generator using image search and PIL (unsplash and pexels API used)
  - `ai_cover.py` — AI cover generation via Hugging Face inference
  - `prompt.py` — query/prompt creation
  - `requirements.txt` — backend Python dependencies
  - `pinterest_cover.py` — This only works on CLI but its more pretty

- `frontend/frontend/`
  - `src/` — React components and UI
  - `package.json` — frontend dependencies and scripts
  - `vite.config.js` — Vite configuration

## Features

- Generate a playlist cover collage from mood, genre, and purpose
- Create an AI-generated cover from the same inputs
- Download the generated cover image in the browser
- Use either backend-generated image collage or AI-powered image generation

## Backend setup

1. Open a terminal in `backend/`
2. Create and activate a Python virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create `backend/.env` with the following values:

```env
HF_TOKEN=your_huggingface_api_token
UNSPLASH_ACCESS_KEY=your_unsplash_access_key
PEXELS_API_KEY=your_pexels_api_key
```

- `HF_TOKEN` is required for `/ai_cover`
- `UNSPLASH_ACCESS_KEY` and `PEXELS_API_KEY` are optional but improve image search reliability

5. Run the backend server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

6. Available endpoints:

- `GET /cover?mood=<mood>&genre=<genre>&purpose=<purpose>`
- `GET /ai_cover?mood=<mood>&genre=<genre>&purpose=<purpose>`

## Frontend setup

1. Open a terminal in `frontend/frontend/`
2. Install dependencies:

```bash
npm install
```

3. Create `frontend/frontend/.env` with the backend URL:

```env
VITE_API_URL=http://localhost:8000
```

4. Start the frontend:

```bash
npm run dev
```

5. Open the local Vite URL shown in the terminal (usually `http://localhost:5173`)

## How to use

- Select a mood, genre, and purpose
- Click `Generate Collage` for a collage-style cover
- Click `Generate AI` for a Hugging Face-generated cover
- Download the result using the download button

## Notes

- The frontend sends requests to the backend using `VITE_API_URL`
- If `api-inference.huggingface.co` cannot be resolved, the AI endpoint will fail with a DNS/network error
- On Windows, verify DNS with:

```cmd
nslookup api-inference.huggingface.co 8.8.8.8
```

## Troubleshooting

- If the frontend cannot load images, confirm the backend is running and `VITE_API_URL` points to the correct server
- If the AI route fails, confirm `HF_TOKEN` is valid and `api-inference.huggingface.co` is reachable
- If image search fails, confirm API keys and network access

## Development notes

- Backend CORS is configured to allow all origins
-fastapi endpoint cannot be created for pinterest_cover.py (pinterest blocks it)
- AI image generation uses the Hugging Face inference API
- Collage generation uses PIL and image search results from Unsplash/Pexels

