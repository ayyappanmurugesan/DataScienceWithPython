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


def repeatMarks(groups,start,stop):
    rgroups=groups.loc[start:stop]
    plt.bar(rgroups.index,rgroups.values)
    plt.title("Repeating Marks (Range: {0} to {1}) - Total: {2}".format(start,stop,np.sum(rgroups.values)))
    plt.xlabel('Mark (min: {0},max: {1})'.format(min(rgroups.index),max(rgroups.index)))
    plt.ylabel('Number of Candidates')
    plt.show()

markgroup=tneet.groupby(['MARK'])
groups=markgroup.size()
repeatMarks(groups,1,720)
repeatMarks(groups,1,100)
repeatMarks(groups,101,200)
repeatMarks(groups,201,300)
repeatMarks(groups,301,400)
repeatMarks(groups,401,500)
repeatMarks(groups,501,600)
repeatMarks(groups,601,720)

