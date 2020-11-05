import pandas as pd
import numpy as np
import lsh
import sys

df_master = pd.read_csv('../spotify_dataset/data.csv')
df = df_master[['id','acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness','speechiness', 'tempo', 'valence', 'year']]
score = dict()
history = set()

def getSpotifyId():
    print(score, file=sys.stderr)
    if (len(score.keys()) == 0):
        spotify_id = lsh.get_random_id(df)
        return spotify_id
    elif (score['acousticness'][1] == 1):
        print('random', file=sys.stderr)
        spotify_id = lsh.get_random_id(df)
        return spotify_id
    else:
        print('finding best match', file=sys.stderr)
        spotify_id = find_best_match(6)
        return spotify_id

def configure_score(id), b:
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
                score[col] = [new_avg, num+1]

def find_best_match(num_pred):
    data = []
    for key in score.keys():
        data.append(score[key][0])
    # print(data, file = sys.stderr)
    # spotify_id = lsh.full_lsh(data, num_pred, df)
    # return spotify_id
    print(data, file=sys.stderr)
    return lsh.get_random_id(df)
    # id = ''
    # min_score = np.Inf
    # for index, row in df.iterrows():
    #     curr_score = 0
    #     for col in range(1, len(row)-1):
    #         curr_score += abs(data[col] - row[col])
    #     if (min_score > curr_score):
    #         min_score = curr_score
    #         id = row[0]
    #         print(id, curr_score)
    # return id