# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:22:03 2018

@author: Ayyappan

NEET 2018 Analysis
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

tneet=pd.read_csv("process.csv")

categories=['OC','BC','BCM','MBC/DNC','SC','SCA','ST']
ranges=['1-100','101-200','201-300','301-400','401-500','501-600','601-720']
cateData=[]
for category in categories:
    markgroup=tneet[tneet.COMMUNITY==category].groupby(['MARK'])
    groups=markgroup.size()
    cdata=[]
    for rang in ranges:
        start,stop=rang.split("-")
        start=int(start)
        stop=int(stop)
        cdata.append(sum(groups.loc[start:stop].values))
    cateData.append(cdata)
cateData=np.array(cateData)



fig, ax = plt.subplots()
im = ax.imshow(cateData)


# We want to show all ticks...
ax.set_xticks(np.arange(len(categories)))
ax.set_yticks(np.arange(len(ranges)))
# ... and label them with the respective list entries
ax.set_xticklabels(categories)
ax.set_yticklabels(ranges)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=49, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(categories)):
    for j in range(len(ranges)):
        text = ax.text(j, i, cateData[i, j],
                       ha="center", va="center", color="w")
ax.set_title("Category Vs Mark Range")
plt.show()
    
    
    
        
        


