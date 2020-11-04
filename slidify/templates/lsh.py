import pandas as pd
import numpy as np
from datasketch import MinHash, MinHashLSH
import pickle

lsh_signatures = pickle.load(open('lsh_signatures.sav', 'rb'))

def create_minhash(data, lsh_threshold, num_perm):
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
        print(temp_lst)

def get_nearest_neighbours(results, df):
    for idx, res in enumerate(results):
        nn = []
        for i in res:
            nn.append(df.iloc[i])
    return nn

def get_NN_id(results, df):
    return get_nearest_neighbours(results, df)[0]['id']

def full_lsh(data, lsh_threshold, num_perm, df):
    min_hash = create_minhash(data, lsh_threshold, num_perm)
    results = query_lsh(min_hash, lsh_signatures)
    nn = get_NN_id(results, df)
    return nn