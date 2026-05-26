import numpy as np
from lightfm.dataset import fetch_movielens
from lightfm import LightFM


data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))


model =LightFM(loss='wrap')


model.fit(data['train'],epochs=30,num_threads=2)

def s_recom(model,data,user_ids):
    n_us,n_it=data['train'].shape

    for user_id in user_ids:
        known_positive=data['item_label'][data['train'].tocsr()[user_id].indices]

        score=model.predict(user_id,np.arange(n_it)) 

        top_it=data['item_labels'][np.argsort(-score)]

        print("User %s " % user_id)
        print("Known +ve :")

        for x in known_positive[:3]:
            print("             %s" % x)
        
        print("      Recommended : " )

        for x in top_it[:3]:
            print("             %s" % x)



s_recom(model,data,[3,25,450])
