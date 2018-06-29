# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:22:03 2018

@author: Ayyappan

NEET 2018 Analysis
"""

import pandas as pd

import matplotlib.pyplot as plt

allocation={'OC': 31,'BC': 26.5,'BCM': 3.5,
        'MBC/DNC': 20,'SC': 16,'SCA': 2,'ST': 1
}

tneet=pd.read_csv("process.csv")
cols=[]
totalSeat=[]
seatallot=[]
rseat=[]
parti=[]

govtGQ=2445
selfGQ=783
rajGQ=127
bdsGQ=85
bdsSelfGQ=1020
rajbds=68
totalSeats=govtGQ+selfGQ+rajGQ+bdsGQ+bdsSelfGQ+rajbds
markgroup=tneet.groupby(['COMMUNITY'])
groups=markgroup.size()
for category in allocation.keys():
    seat=round((totalSeats*allocation[category])/100)
    totalSeat.append(100)
    cols.append(category)
    seatallot.append(round((seat/groups[category])*100))
    rseat.append(seat)
    parti.append(groups[category]) 
plt.plot(cols,parti)
plt.plot(cols,rseat)
plt.title("Participants Vs Available Seats (In Count)")
plt.legend(['Participants','Available Seats'])
plt.xlabel('Community')
plt.ylabel('Candidates')
plt.show()
plt.bar(cols,totalSeat)
plt.bar(cols,seatallot)
plt.ylim(1,110)
plt.title("Participants Vs Available Seats (In %) ")
plt.legend(['Participants','Available Seats'])
plt.xlabel('Community')
plt.ylabel('Candidates(%)')
plt.show()






    
    
        
        


