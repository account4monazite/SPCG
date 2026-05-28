import requests
import os,uuid
from dotenv import load_dotenv
from prompt import build_prompt
from PIL import Image, ImageDraw, ImageFont
load_dotenv()
api_key=os.getenv("stability")


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
    prompt= build_prompt(mood,genre,purpose)
    title=f"{mood} {genre} {purpose} \n Playlist"
    fn=f"{uuid.uuid4()}.png"
    url=f"https://image.pollinations.ai/prompt/{prompt}"
    response=requests.get(url)

    if response.status_code == 200:
        with open(fn, 'wb') as file:
            file.write(response.content)
        fn=add_text(fn,title)
    
        return fn
    else:
        raise Exception(str(response.json()))