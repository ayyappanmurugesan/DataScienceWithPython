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

#Count the marks, which is same mark to more than one students


def repeatMarks(category,groups,start,stop):
    
    rgroups=groups.loc[start:stop]
    if len(rgroups)>0:
        plt.bar(rgroups.index,rgroups.values)
        plt.title("{3}-Repeating Marks (Range: {0} to {1}) - Total: {2}".format(start,stop,np.sum(rgroups.values),category))
        plt.xlabel('Mark (min: {0},max: {1})'.format(min(rgroups.index),max(rgroups.index)))
        plt.ylabel('Number of Candidates')
        #plt.savefig('report/categoryRepeatMark/{0}-{1}-{2}.png'.format(category.replace("/","-"),start,stop))
        plt.show()
        
        
for category in ['OC','BC','BCM','MBC/DNC','SC','SCA','ST']:
    markgroup=tneet[tneet.COMMUNITY==category].groupby(['MARK'])
    groups=markgroup.size()
    repeatMarks(category,groups,1,720)
    repeatMarks(category,groups,601,720)
    repeatMarks(category,groups,501,600)
    repeatMarks(category,groups,401,500)
    repeatMarks(category,groups,301,400)
    repeatMarks(category,groups,201,300)
    repeatMarks(category,groups,101,200)
    repeatMarks(category,groups,1,100)
    
    
        
        


