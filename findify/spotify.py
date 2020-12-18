import pandas as pd
import numpy as np
import lsh
import sys

df_master = pd.read_csv('static/data/data.csv')
df = df_master[['id','acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence', 'year']]
score = dict()

def getSpotifyId(b):
    print(score, file=sys.stderr)
    if (b == False):
        spotify_id = lsh.get_random_id(df)
        return spotify_id
    else:
        if (len(score.keys()) == 0):
            spotify_id = lsh.get_random_id(df)
            return spotify_id
        elif (score['acousticness'][1] == 1):
            print('random', file=sys.stderr)
            spotify_id = lsh.get_random_id(df)
            return spotify_id
        else:
            print('finding best match', file=sys.stderr)
            spotify_id = find_best_match()
            return spotify_id  

def configure_score(id, b):
    row = df[df['id'] == id]
    row = row[['acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence', 'year']]
    if (b):
        for col in row.columns:
            if (col not in score.keys()):
                    score[col] = [float(row.iloc[0][col]), 1]
            else:
                avg = score[col][0]
                num = score[col][1]
                new_avg = (float(row.iloc[0][col]) + avg * num) / (num+1)
                # new_avg = float(row.iloc[0][col])
                score[col] = [round(new_avg,4), num+1]

def find_best_match():
    data = []
    for key in score.keys():
        data.append(score[key][0])
    print(data, file = sys.stderr)
    spotify_id = lsh.full_lsh(data, 6, df)
    return spotify_id