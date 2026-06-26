# Spotify Playlist Cover Generator (SPCG)

A full-stack playlist cover generator with:
- a React + Vite frontend
- a FastAPI backend
- collage-based cover generation using Unsplash/Pexels
- optional AI cover generation using Hugging Face inference
  
## How it works:
You open the link: https://playlist-cover-generator-nine.vercel.app/
<img width="1600" height="739" alt="image" src="https://github.com/user-attachments/assets/4eff3f68-21c1-423a-8bd8-1c6dc11631c3" />

- Enter Mood, Genre and the Purpose(work,study, coding,etc) of the playlist
  <img width="931" height="565" alt="image" src="https://github.com/user-attachments/assets/e293dfcd-628c-4afc-abb8-9f45f0d9f4bd" />

- Generate an image via AI or a Collage 
 <img width="931" height="732" alt="image" src="https://github.com/user-attachments/assets/4a704515-5be2-4ea8-a1ee-a4b55cf39c47" />

- Design is generated
  <img width="934" height="538" alt="image" src="https://github.com/user-attachments/assets/836edcb0-b9b4-4e9e-9a97-b6938f981e7a" />
<img width="907" height="423" alt="image" src="https://github.com/user-attachments/assets/bf83d386-99a0-4842-85d9-e75b8860f102" />

- Download it :)
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

## Troubleshooting

- If the frontend cannot load images, confirm the backend is running and `VITE_API_URL` points to the correct server
- If image search fails, confirm API keys and network access

## Development notes

- Backend CORS is configured to allow all origins
-fastapi endpoint cannot be created for pinterest_cover.py (pinterest blocks it)
- AI image generation uses the Hugging Face inference API
- Collage generation uses PIL and image search results from Unsplash/Pexels

