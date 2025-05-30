import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import TimeSeriesSplit
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("nba_games.csv", index_col=0)
df = df.sort_values("date")
df.reset_index(drop=True)
del df["mp.1"]
del df["mp_opp.1"]
del df["index_opp"]

def add_target(team):
  team["target"] = team["won"].shift(-1)
  return team

df = df.groupby("team", group_keys = False).apply(add_target)

df["target"][pd.isnull(df["target"])] = 2
df["target"] = df["target"].astype(int,errors="ignore")

valid_columns = df.columns[~df.columns.isin(nulls.index)]
df = df[valid_columns].copy()

rr = RidgeClassifier(alpha=1)
split = TimeSeriesSplit(n_splits=3)
sfs = SequentialFeatureSelector(rr, n_features_to_select=30, direction="forward", cv=split)
removed_columns = ["season","date","won","target","team","team_opp"]
selected_columns = df.columns[~df.columns.isin(removed_columns)]
scaler = MinMaxScaler()
df[selected_columns] = scaler.fit_transform(df[selected_columns])

sfs.fit(df[selected_columns],df["target"])
