import pandas as pd
from sklearn import linear_model, preprocessing
import numpy as np
from collections import defaultdict

#load the csv
df = pd.read_csv('data/teamdata.csv', parse_dates=['game_date'])

#generate our encoder
d = defaultdict(preprocessing.LabelEncoder)
# Encoding the variable
fit = df.apply(lambda x: d[x.name].fit_transform(x))
# Inverse the encoded
fit.apply(lambda x: d[x.name].inverse_transform(x))
# Using the dictionary to label future data
df = df.apply(lambda x: d[x.name].transform(x))

print df

#generate model data
logreg = linear_model.LogisticRegression(C=1e5)
columns = ['reg_season', 'home_team', 'away_team', 'game_date', 'away_player_one', 'away_player_two',
                             'away_player_three', 'away_player_four', 'away_player_five', 'home_player_one', 'home_player_two',
                             'home_player_three', 'home_player_four', 'home_player_five', 'head_ref', 'away_rest_days',
                             'home_rest_days', 'spread']

labels = df['result'].values
features = df[list(columns)].values


logreg.fit(features, labels)

#predict games
p = pd.read_csv('data/predicts.csv', parse_dates=['game_date'])
p = p.apply(lambda x: d[x.name].transform(x))

pfeatures = p[list(columns)].values
print logreg.predict(pfeatures)