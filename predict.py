import pandas as pd

df = pd.read_csv("nba_games.csv", index_col=0)
df = df.sort_values("date")
df.reset_index(drop=True)
del df["mp.1"]
del df["mp_opp.1"]
del df["index_opp"]

def add_target(team):
  team["target"] = team["won"].shift(-1)
  return group
