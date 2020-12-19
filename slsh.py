import pandas as pd
import numpy as np
import random
from datasketch import MinHash, MinHashLSH
import pickle
import sys

lsh_signatures = pickle.load(open('lsh_signatures_0.3.sav', 'rb'))
history = set()

def create_minhash(data, num_perm):
    min_hash = []
    m = MinHash(num_perm = num_perm)
    for d in data:
        m.update(str(d).encode('utf8'))
    min_hash.append(m)
    return min_hash

def query_lsh(minhash, lsh_signature):
    results = []
    for idx, h in enumerate(minhash):
        result = lsh_signature.query(h)
        results.append(result)
    return(results)

def display_nearest_neighbours(results, df):
    for idx, res in enumerate(results):
        temp_lst = []
        for i in res:
            temp_lst.append(df.iloc[i])

def get_nearest_neighbours(results, df):
    nn = []
    for idx, res in enumerate(results):
        for i in res:
            nn.append(df.iloc[i])
    return nn

def get_NN_id(results, df):
    songs = get_nearest_neighbours(results, df)
    sid = random.choice(songs)['id']
    while (sid in history):
        sid = random.choice(songs)['id']
    history.add(sid)
    return sid

def get_random_id(df):
    sid = df.sample().iloc[0]['id']
    while (sid in history):
        sid = df.sample().iloc[0]['id']
    history.add(sid)
    return sid

def get_history():
    return history

def full_lsh(data, num_perm, df):
    min_hash = create_minhash(data, num_perm)
    results = query_lsh(min_hash, lsh_signatures)
    print(results)
    if (len(results[0]) == 0):
        return get_random_id(df)
    else:
        nn = get_NN_id(results, df)
        return nn