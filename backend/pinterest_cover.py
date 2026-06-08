'''this only works in CLI'''

import asyncio
import json
import re
import sys
from playwright.async_api import async_playwright
from PIL import Image
from io import BytesIO
import requests


def build_query(mood: str, genre: str, purpose: str) -> str:
    return f"{mood} {genre} {purpose} aesthetic playlist cover"


async def scrape_pinterest_images(query: str, count: int = 4) -> list[str]:
    image_urls = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
        })

        search_url = f"https://www.pinterest.com/search/pins/?q={query.replace(' ', '%20')}"
        print(f"Searching: {search_url}")

        await page.goto(search_url, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(3000)

        # Scroll to load images
        await page.evaluate("window.scrollBy(0, 800)")
        await page.wait_for_timeout(2000)

        # Extract image URLs from pin images
        images = await page.evaluate("""
            () => {
                const imgs = document.querySelectorAll('img[src*="pinimg.com"]');
                return Array.from(imgs)
                    .map(img => img.src)
                    .filter(src => src.includes('236x') || src.includes('474x') || src.includes('736x'))
            }
        """)

        # Prefer higher resolution
        seen = set()
        for url in images:
            # Upgrade to 736x if possible
            high_res = re.sub(r'/\d+x/', '/736x/', url)
            if high_res not in seen:
                seen.add(high_res)
                image_urls.append(high_res)
            if len(image_urls) >= count:
                break

        await browser.close()

    return image_urls[:count]


def download_images(urls: list[str]) -> list[Image.Image]:
    images = []
    headers = {"User-Agent": "Mozilla/5.0"}
    for url in urls:
        try:
            res = requests.get(url, headers=headers, timeout=10)
            img = Image.open(BytesIO(res.content)).convert("RGB")
            images.append(img)
            print(f"Downloaded: {url}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
    return images


def make_collage(images: list[Image.Image], output_path: str = "cover.png", size: int = 1200):
    collage = Image.new("RGB", (size, size))
    half = size // 2

    positions = [(0, 0), (half, 0), (0, half), (half, half)]

    for i, img in enumerate(images[:4]):
        img = img.resize((half, half),resample= Image.Resampling.LANCZOS)
        collage.paste(img, positions[i])

    collage.save(output_path)
    print(f"\nSaved cover to: {output_path}")
    return output_path


async def generate_cover(mood: str, genre: str, purpose: str, output: str = "cover.png"):
    query = build_query(mood, genre, purpose)
    print(f"Query: {query}\n")

    urls = await scrape_pinterest_images(query, count=4)

    if not urls:
        print("No images found. Pinterest may have blocked the request.")
        return

    print(f"\nFound {len(urls)} images")
    images = download_images(urls)

    if len(images) < 4:
        print(f"Only got {len(images)} images, need 4 for a full collage.")

    if images:
       return make_collage(images, output)


if __name__ == "__main__":
    mood    = input("Mood (e.g. melancholic, euphoric): ").strip()
    genre   = input("Genre (e.g. indie, hip-hop): ").strip()
    purpose = input("Purpose (e.g. late night drives, gym): ").strip()

    asyncio.run(generate_cover(mood, genre, purpose))
