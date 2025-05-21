# Install playwright
!pip install playwright

# Install browser binaries
!playwright install

import os
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import time

SEASONS = list(range(2014,2025))
DATA_DIR="data"
STANDINGS_DIR = os.path.join(DATA_DIR, "standings")
SCORES_DIR = os.path.join(DATA_DIR, "scores")

async def get_html(url, selector, sleep=5, retries=3):
    html = None
    for i in range(1, retries+1):
      time.sleep(sleep*i)

      try:
        async with async_playwright() as p:
          browser = await p.chromium.launch()
          page = await browser.new_page()
          await page.goto(url)
          print(await page.title())
          html = await page.inner_html(selector)
      except PlaywrightTimeout:
        print(f"Timeout error on {url}")
        continue
      else:
        break
    return html

async def scrape_season(season):
  url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
  html = await get_html(url, "#content .filter")
  
  soup=BeautifulSoup(html)
  links = soup.find_all("a")
  href = [l["href"] for l in links]
  standings_pages = [f"https://www.basketball-reference.com{l}" for l in links]

  for url in standings_pages:
    save_path = os.path.join(STANDINGS_DIR, url.split("/")[-1])
    if os.path.exists(save_path):
      continue

    html = await get_html(url, "#all_schedule")
    with open(save_path, "w+") as f:
      f.write(html)

for season in SEASONS:
  await scrape_season(season)
standings_files = os.listdir(STANDINGS_DIR)

standings_file = standings_files[0]
with open(standings_file, 'r') as f:
    html = f.read()

soup = BeautifulSoup(html)
links = soup.find_all('a')
d
