

import requests
import os
from io import BytesIO
from dotenv import load_dotenv
from prompt import MOODS,GENRES, PURPOSES,MOOD_COLORS
from PIL import Image, ImageEnhance, ImageFilter,ImageDraw,ImageOps
import random
from PIL import ImageDraw, ImageFont

load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "")  # optional for demo
PEXELS_API_KEY      = os.getenv("PEXELS_API_KEY", "")


def build_search_query(mood, genre, purpose):

    words = []

    words += MOODS.get(mood, "").split()[:2]
    words += GENRES.get(genre, "").split()[:2]
    words += PURPOSES.get(purpose, "").split()[:2]
    random.shuffle(words)
    query = " ".join(words)

    color = MOOD_COLORS.get(
        mood.lower(),
        ""
    )

    return {
        "query": query,
        "color": color
    }


def fetch_unsplash(query: str, color: str = "", count: int = 4) -> list[str]:
    headers = {}
    params = {
        "query": query,
        "per_page": count,
        "orientation": "squarish",
        "content_filter": "high",
    }

    if color:
        params["color"] = color

    if UNSPLASH_ACCESS_KEY:
        headers["Authorization"] = f"Client-ID {UNSPLASH_ACCESS_KEY}"
        url = "https://api.unsplash.com/search/photos"
    else:
        # Demo mode — no key needed but limited
        url = "https://api.unsplash.com/search/photos"
        headers["Authorization"] = "Client-ID demo"

    try:
        res = requests.get(url, headers=headers, params=params, timeout=10)
        data = res.json()
        return [photo["urls"]["regular"] for photo in data.get("results", [])]
    except Exception as e:
        print(f"Unsplash error: {e}")
        return []


# ── Pexels ────────────────────────────────────────────────────────────────────

def fetch_pexels(query: str, count: int = 4) -> list[str]:
    if not PEXELS_API_KEY:
        print("No Pexels API key, skipping.")
        return []

    headers = {"Authorization": PEXELS_API_KEY}
    params  = {"query": query, "per_page": count, "size": "medium"}

    try:
        res  = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params, timeout=10)
        data = res.json()
        return [photo["src"]["large"] for photo in data.get("photos", [])]
    except Exception as e:
        print(f"Pexels error: {e}")
        return []


# ── Image Processing ──────────────────────────────────────────────────────────

def download_image(url: str) -> Image.Image | None:
    try:
        res = requests.get(url, timeout=10)
        return Image.open(BytesIO(res.content)).convert("RGB")
    except Exception as e:
        print(f"Download failed: {e}")
        return None

def add_vignette(img: Image.Image):

    width, height = img.size

    vignette = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(vignette)

    draw.ellipse(
        (-200, -200, width + 200, height + 200),
        fill=180
    )

    mask = vignette.filter(ImageFilter.GaussianBlur(90))

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 35))

    overlay.putalpha(vignette)

    return Image.alpha_composite(
        img.convert("RGBA"),
        overlay
    ).convert("RGB")
def apply_filter(img: Image.Image, mood: str) -> Image.Image:

    mood = mood.lower()

    dark_moods = {
        "sad",
        "melancholic",
        "dark",
        "angry",
        "lonely",
    }

    warm_moods = {
        "romantic",
        "nostalgic",
        "happy",
        "euphoric",
        "cozy",
    }

    dreamy_moods = {
        "dreamy",
        "ethereal",
        "spiritual",
    }

    energetic_moods = {
        "energetic",
        "rebellious",
        "chaotic",
    }

    # ── DARK ─────────────────────────────

    if mood in dark_moods:

        img = ImageEnhance.Color(img).enhance(0.6)
        img = ImageEnhance.Brightness(img).enhance(0.82)
        img = ImageEnhance.Contrast(img).enhance(1.15)

        # subtle blur for cinematic softness
        img = img.filter(ImageFilter.GaussianBlur(0.3))

    # ── WARM ─────────────────────────────

    elif mood in warm_moods:

        img = ImageEnhance.Color(img).enhance(1.2)
        img = ImageEnhance.Brightness(img).enhance(1.05)
        img = ImageEnhance.Contrast(img).enhance(1.05)

    # ── DREAMY ───────────────────────────

    elif mood in dreamy_moods:

        img = ImageEnhance.Color(img).enhance(0.9)
        img = ImageEnhance.Brightness(img).enhance(1.08)

        img = img.filter(ImageFilter.GaussianBlur(1.2))

    # ── ENERGETIC ────────────────────────

    elif mood in energetic_moods:

        img = ImageEnhance.Color(img).enhance(1.35)
        img = ImageEnhance.Contrast(img).enhance(1.25)
        img = ImageEnhance.Sharpness(img).enhance(1.3)
    
    
    return img


def add_title(
    img: Image.Image,
    title: str
):

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(
        "arial.ttf",
        70
    )

    x, y = 80, 80

    # shadow
    draw.text(
        (x + 4, y + 4),
        title,
        fill="black",
        font=font
    )

    # main text
    draw.text(
        (x, y),
        title,
        fill="white",
        font=font
    )

    return img
def make_collage(
    images: list[Image.Image],
    mood: str,
    genre: str,
    purpose: str,
    output_path: str = "cover.png",
    size: int = 1200
) -> str:
    collage = Image.new("RGB", (size, size), color=(10, 10, 10))
    half = size // 2
    positions = [(0, 0), (half, 0), (0, half), (half, half)]

    for i, img in enumerate(images[:4]):
        img = apply_filter(img, mood)
        img = ImageOps.fit(img,(half, half),method=Image.Resampling.LANCZOS,centering=(0.5, 0.5))
        collage.paste(img, positions[i])
    collage=add_vignette(collage)
    title = f"{mood.title()} {genre.title()}"

    collage = add_title(collage, title)
    collage.save(output_path, quality=95)
    print(f"\n✅ Cover saved to: {output_path}")
    return output_path


# ── Main ──────────────────────────────────────────────────────────────────────

def generate_cover(mood: str, genre: str, purpose: str, output: str = "cover.png"):
    q = build_search_query(mood, genre,purpose)
    print(f"Query: \"{q['query']}\" | Color filter: {q['color'] or 'none'}\n")

    # Try Unsplash first, fall back to Pexels
    urls = fetch_unsplash(q["query"], q["color"], count=4)
    print(f"Unsplash: {len(urls)} images")

    if len(urls) < 4:
        extra = fetch_pexels(q["query"], count=4 - len(urls))
        urls += extra
        print(f"Pexels fallback: {len(extra)} images")

    if not urls:
        print("No images found. Check your API keys.")
        return

    images = [img for url in urls if (img := download_image(url))]
    print(f"Downloaded: {len(images)} images")

    if not images:
        print("Failed to download images.")
        return

    return make_collage(
    images,
    mood,
    genre,
    purpose,
    output
)


if __name__ == "__main__":
    print("Playlist Cover Generator\n")
    mood    = input("Mood (e.g. melancholic, euphoric, chill): ").strip()
    genre   = input("Genre (e.g. indie, hip-hop, lo-fi): ").strip()
    purpose = input("Purpose (e.g. late night drives, gym): ").strip()

    generate_cover(mood, genre, purpose)
