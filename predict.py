import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import RidgeClassifier
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

def add_target(team):
  team["target"] = team["won"].shift(-1)
  return team

def backtest(data, model, predictors, start=2, step=1):
    all_predictions = []
    
    seasons = sorted(data["season"].unique())
    
    for i in range(start, len(seasons), step):
        season = seasons[i]
        train = data[data["season"] < season]
        test = data[data["season"] == season]
        
        model.fit(train[predictors], train["target"])
        
        preds = model.predict(test[predictors])
        preds = pd.Series(preds, index=test.index)
        combined = pd.concat([test["target"], preds], axis=1)
        combined.columns = ["actual", "prediction"]
        
        all_predictions.append(combined)
    return pd.concat(all_predictions)

def shift_col(team,col_name):
  next_col = team[col_name].shift(-1)
  return next_col

def add_col(df,col_name):
  return next_col = df.groupby("team",group_keys=False).apply(lambda x: shift_col(x,col_name))
  
df = pd.read_csv("nba_games.csv", index_col=0)
df = df.sort_values("date")
df.reset_index(drop=True)
del df["mp.1"]
del df["mp_opp.1"]
del df["index_opp"]

df = df.groupby("team", group_keys = False).apply(add_target)

df["target"][pd.isnull(df["target"])] = 2
df["target"] = df["target"].astype(int, errors="ignore")

valid_columns = df.columns[~df.columns.isin(nulls.index)]
df = df[valid_columns].copy()
