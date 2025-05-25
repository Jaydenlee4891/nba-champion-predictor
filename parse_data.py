import os
import pandas as pd
from bs4 import BeautifulSoup

SCORE_DIR = "data/scores"
box_scores=os.listdir(SCORE_DIR)
box_scores = [os.path.join(SCORE_DIR, f) for f in box_scores if f.endswith(".html")]

def parse_html(box_score):
  with open(box_score) as f:
    html = f.read()

  soup = BeautifulSoup(html)
  [s.decompose() for s in soup.select("tr.over_header")]
  [s.decompose() for s in soup.select("tr.thead")]
  return soup

