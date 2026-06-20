from huggingface_hub import InferenceClient
import os,httpx
from pathlib import Path
from fastapi import HTTPException
from dotenv import load_dotenv
from prompt import build_prompt
from PIL import Image, ImageDraw, ImageFont

dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)
headers = {
    "User-Agent": "Mozilla/5.0"
}

font_path=os.path.join(
    os.path.dirname(__file__),"fonts","Lato-Black.ttf"
)

def add_text(
    image_path,
    title,
    
):

    img = Image.open(image_path).convert("RGB")

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font_path,70)

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
    title = f"{mood} {genre} {purpose} \n playlist"
    fn = f"cover.png"

    try:
        client = InferenceClient(
            provider='fal-ai',
            api_key=os.getenv('HF_TOKEN')
        )
        image = client.text_to_image(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )
    except httpx.RequestError as exc:
        print("Network error when calling Hugging Face inference:", exc)
        raise HTTPException(
            status_code=503,
            detail="Unable to reach the image generation service. Please check network/DNS or try again later."
        )

    if not isinstance(image, Image.Image):
        raise HTTPException(
            status_code=503,
            detail="Unexpected response from image generation service."
        )

    image.save(fn, format="PNG")
    fn = add_text(fn, title)
    return fn
