import requests
import os,uuid
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
async def generate_cover_ai(mood,genre,purpose):
    #prompt= build_prompt(mood,genre,purpose).strip()
    prompt="dark jazz study playlist"
    prompt=quote(prompt)
    print("api called ",prompt)
    title=f"{mood} {genre} {purpose} \n Playlist"
    fn=f"cover.png"
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    response=requests.get(url,headers=headers)
    print("CONTENT TYPE:", response.headers.get("content-type"))
    print("STATUS:", response.status_code)
    print("BODY:", response.text[:500])
    if response.status_code == 200:
        with open(fn, 'wb') as file:
            file.write(response.content)
        fn=add_text(fn,title)
    
        return fn
    else:
       raise HTTPException(
        status_code=503,
        detail="Image generation service is busy. Please try again in a few moments."
    )