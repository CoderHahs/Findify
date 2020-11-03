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
    if (b):
        for col in row.columns:
            if (col not in score.keys()):
                    score[col] = [float(row.iloc[0][col]), 1]
            else:
                avg = score[col][0]
                num = score[col][1]
                new_avg = (float(row.iloc[0][col]) + avg * num) / (num+1)
                score[col] = [new_avg, num+1]

def find_best_match():
    pass