# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:22:03 2018

@author: Ayyappan

NEET 2018 Analysis
"""

import matplotlib.pyplot as plt

allocation={'OC': 31,'BC': 26.5,'BCM': 3.5,
        'MBC/DNC': 20,'SC': 16,'SCA': 2,'ST': 1
}



plt.pie(allocation.values(),labels=allocation.keys())
plt.title("TN Government Seat Allocation")
plt.legend(["{!s}={!r}%".format(key,val) for (key,val) in allocation.items()])
plt.show()


govtGQ=3350
selfGQ=1600
rajGQ=127
bdsGQ=85
bdsSelfGQ=1020
rajbds=68
totalSeats=govtGQ+selfGQ+rajGQ+bdsGQ+bdsSelfGQ+rajbds
plt.bar(['Govt(2445)','Self(783)','Rajah(127)'],[govtGQ,selfGQ,rajGQ])
plt.bar(['Govt(85)','Self(1020)','Rajah(68)'],[bdsGQ,bdsSelfGQ,rajbds])
plt.title("College Wise Available Seats")
plt.ylabel('Medical Seats')
plt.legend(['MBBS','BDS'])
plt.show()


legends=[]
for (key,val) in allocation.items():
    seat=round((totalSeats*val)/100)
    legends.append("{!s}={!r}".format(key,seat))
    plt.bar([key],[seat])
plt.title("TN Government Seat Allocation")
plt.legend(legends)
plt.show()
