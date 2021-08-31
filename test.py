# -*- coding: utf-8 -*-
"""
"""

"""from model import Recommendation
recommend = Recommendation()
u='speedlift'
r=recommend.getTopProducts(u)
print(r)"""

import pickle
import json
import pandas as pd
import numpy as np
a = pickle.load(open('user_final_rating.pkl','rb'))

#b =pd.read_csv('sample30.csv')
#a=np.array(a.index)
#r=a.to_json(orient='index')
s= np.array(a.index).tolist()
#print(s)
print(''.join(e+'|||' for e in s))

#from model import Recommendation
#recommend = Recommendation()
#print(recommend.analyiseSentiment("This is a bad product"))



#from model import Recommendation
#recommend = Recommendation()
#u='speedlift'
#r=recommend.getUsers()
#print(r)