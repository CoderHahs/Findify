import pandas as pd
import numpy as np
import sys

df = pd.read_csv('../spotify_dataset/data.csv')
score = dict()

def getSpotifyId():
    spotify_id = df.sample().iloc[0]['id']
    return spotify_id

def configure_score(id, b):
    row = df[df['id'] == id]
    row = row[['acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence', 'year']]
    for col in row.columns:
        if (col not in score.keys()):
            if (b):
                score[col] = [float(row.iloc[0][col]), 1]
            else:
                score[col] = [-float(row.iloc[0][col]), 1]
        else:
            avg = score[col][0]
            num = score[col][1]
            if (b):
                new_avg = (float(row.iloc[0][col]) + avg * num) / (num+1)
            else:
                new_avg = (-float(row.iloc[0][col]) + avg * num)
            score[col] = [new_avg, num+1]
    print(score, file=sys.stderr)

