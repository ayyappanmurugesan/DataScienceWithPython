# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:22:03 2018

@author: Ayyappan

NEET 2018 Analysis
"""

import pandas as pd

import matplotlib.pyplot as plt
tneet=pd.read_csv("process.csv")
def cutOff(allocation):
    govtGQ=2445
    selfGQ=783
    rajGQ=127
    bdsGQ=85
    bdsSelfGQ=1020
    rajbds=68
    totalSeats=govtGQ+selfGQ+rajGQ+bdsGQ+bdsSelfGQ+rajbds
    minmarks=[]
    maxmarks=[]
    lowmarks=[]
    categories=allocation.keys()
    for category in categories:
        seat=round((totalSeats*allocation[category])/100)
        allstudents=tneet[tneet.COMMUNITY==category]
        students=allstudents[:seat]
        minmarks.append(min(students.MARK))
        maxmarks.append(max(students.MARK))
        lowmarks.append(min(allstudents.MARK))
    
    rows=['Low Mark','CutOff Mark','High Mark']
    plt.plot(categories,lowmarks)
    plt.plot(categories,minmarks)
    plt.plot(categories,maxmarks)
    plt.ylabel('Mark')
    plt.title('Cut OFF Analysis Using Category Seat Allocation')
    plt.legend(rows)
    plt.table(cellText=[lowmarks,minmarks,maxmarks],
                          rowLabels=rows,
                          colLabels=tuple(categories),
                          loc='bottom')
    plt.xticks([])
    plt.show()    

cutOff({'OC': 31,'BC': 26.5,'BCM': 3.5,
        'MBC/DNC': 20,'SC': 16,'SCA': 2,'ST': 1
})

    
    

    
    
    








    
    
        
        


