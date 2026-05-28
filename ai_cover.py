import requests
import os,uuid
from dotenv import load_dotenv
from prompt import build_prompt
load_dotenv()
api_key=os.getenv("stability")
async def generate_cover(mood,genre,purpose):
    prompt= build_prompt(mood,genre,purpose)
    fn=f"{uuid.uuid4()}.png"
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            #"negative_prompt":"text, letters, words, logo, watermark, typography",
            "output_format": "png",
        },
    )

    if response.status_code == 200:
        with open(fn, 'wb') as file:
            file.write(response.content)
        return fn
    else:
        raise Exception(str(response.json()))