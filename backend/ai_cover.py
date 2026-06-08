import requests
import os,httpx
from pathlib import Path
from fastapi import HTTPException
from dotenv import load_dotenv
from prompt import build_prompt
from PIL import Image, ImageDraw, ImageFont
from urllib.parse import quote

# Load backend-specific environment variables even when the app is started from the repo root
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)
#api_key=os.getenv("stability")
headers = {
    "User-Agent": "Mozilla/5.0"
}


def add_text(
    image_path,
    title,
    
):

    img = Image.open(image_path).convert("RGB")

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(
        "C:\\WINDOWS\\FONTS\\CANDARAL.ttf",
        70
    )

    x, y = 80, 80

    draw.text(
        (x+4, y+4),
        title,
        fill="black",
        font=font
    )

    draw.text(
        (x, y),
        title,
        fill="white",
        font=font
    )

    img.save(image_path)

    return image_path
async def generate_cover_ai(mood, genre, purpose):
    prompt = build_prompt(mood, genre, purpose).strip()
    title = f"{mood} {genre} {purpose} \n Playlist"
    fn = f"cover.png"

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell",
                headers={"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"},
                json={"inputs": prompt}
            )
    except httpx.RequestError as exc:
        print("Network error when calling Hugging Face inference:", exc)
        raise HTTPException(
            status_code=503,
            detail="Unable to reach the image generation service. Please check network/DNS or try again later."
        )

    print("CONTENT TYPE:", response.headers.get("content-type"))
    print("STATUS:", response.status_code)

    if response.status_code == 200:
        with open(fn, 'wb') as file:
            file.write(response.content)
        fn = add_text(fn, title)
        return fn
    
    elif response.status_code == 503:
        # Model is loading, tell frontend to retry
        raise HTTPException(
            status_code=503,
            detail="Model is loading, please try again in 20 seconds."
        )
    else:
        print("BODY:", response.text[:500])
        raise HTTPException(
            status_code=503,
            detail="Image generation failed. Please try again."
        )