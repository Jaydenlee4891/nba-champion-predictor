# Install playwright
#!pip install playwright

# Install browser binaries
#!playwright install

import os
import time
import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

SEASONS = list(range(2014, 2025))
DATA_DIR = "data"
STANDINGS_DIR = os.path.join(DATA_DIR, "standings")
SCORES_DIR = os.path.join(DATA_DIR, "scores")

os.makedirs(STANDINGS_DIR, exist_ok=True)
os.makedirs(SCORES_DIR, exist_ok=True)

async def get_html(url, selector, sleep=5, retries=3):
    html = None
    for i in range(1, retries + 1):
        time.sleep(sleep * i)
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                await page.goto(url, timeout=30000)
                print(f"Fetched: {await page.title()}")
                html = await page.inner_html(selector)
                await browser.close()
        except PlaywrightTimeout:
            print(f"Timeout error on {url}")
            continue
        except Exception as e:
            print(f"Error on {url}: {e}")
            continue
        else:
            break
    return html

async def scrape_season(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    html = await get_html(url, "#content .filter")
    if not html:
        print(f"Skipping season {season} — no index page")
        return

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    standings_pages = [
        f"https://www.basketball-reference.com{l['href']}"
        for l in links if l.get("href")
    ]

    for url in standings_pages:
        filename = url.split("/")[-1]
        save_path = os.path.join(STANDINGS_DIR, filename)
        if os.path.exists(save_path):
            continue

        page_html = await get_html(url, "#all_schedule")
        if page_html:
            with open(save_path, "w+", encoding="utf-8") as f:
                f.write(page_html)

async def scrape_game(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    hrefs = [l.get("href") for l in links]
    box_scores = [
        f"https://www.basketball-reference.com{l}"
        for l in hrefs if l and "boxscore" in l and ".html" in l
    ]

    for url in box_scores:
        filename = url.split("/")[-1]
        save_path = os.path.join(SCORES_DIR, filename)
        if os.path.exists(save_path):
            continue

        page_html = await get_html(url, "#content")
        if page_html:
            with open(save_path, "w+", encoding="utf-8") as f:
                f.write(page_html)

async def main():
    for season in SEASONS:
        print(f"=== Scraping season {season} ===")
        await scrape_season(season)

    standings_files = [f for f in os.listdir(STANDINGS_DIR) if f.endswith(".html")]

    for f in standings_files:
        print(f"--- Scraping box scores from: {f} ---")
        filepath = os.path.join(STANDINGS_DIR, f)
        await scrape_game(filepath)

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
