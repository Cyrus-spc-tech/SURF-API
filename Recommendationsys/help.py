import numpy as np
from lightfm.dataset import fetch_movielens
from lightfm import LightFM


data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))


model =LightFM(loss='wrap')


model.fit(data['train'],epochs=30,num_threads=2)

def s_recom(model,data,user_ids):


