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
lowrange=[]
highrange=[]
avgrange=[]
for category in categories:
    markgroup=tneet[tneet.COMMUNITY==category]
    low=min(markgroup.MARK)
    high=max(markgroup.MARK)
    avg=(low+high)/2
    lowrange.append(low)
    highrange.append(high)
    avgrange.append(avg)

plt.plot(categories,lowrange)
plt.plot(categories,highrange)
plt.plot(categories,avgrange)
plt.title('Mark Range - Low & High');
plt.xlabel('Community')
plt.ylabel('Mark')
plt.legend(['Low Mark Range','High Mark Range'])
plt.show()    

    
