# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:22:03 2018

@author: Ayyappan

NEET 2018 Analysis - Practics Codes
"""

import pandas as pd

import numpy as np


#Read Data From CSV
tneet=pd.read_csv("process.csv")

#Print Full Data
print(tneet)

#Get the number of records detail
print(tneet.index)

#Get the available column in the record
print(tneet.columns)

#Print Top 5 Record
print(tneet.head())

print("\n\n")

#Print Top 10 Records
print(tneet.head(2))

print("\n\n")

#Set specific column as Index Column
tneet=tneet.set_index("RANK")
print(tneet.head())

#Accessing specific Field Data Set
name=tneet['NAME']
print(name)

print("\n\n");

subset=tneet[['NAME','MARK']]
print(subset)            

print("\n\n");

subset=tneet.loc[[1,10]]
print(subset)


print("\n\n");

subset=tneet.iloc[[0,9]]
print(subset)

print("\n\n");

subset=tneet.loc[:5]
print(subset)

print("\n\n");

subset=tneet.iloc[:5]
print(subset)

print("\n\n");

subset=tneet.loc[:2,['NAME','MARK']]
print(subset)

print("\n\n");

subset=tneet.iloc[:2,[1,3]]
print(subset)

print("\n\n");

#Remove Last Col
del tneet['EMPTY']
print(tneet)


#Change type of the MARK Field
print(type(tneet["MARK"][1]))


print("\n\n");

oc=tneet[tneet.COMMUNITY=='OC']
bc=tneet[tneet.COMMUNITY=='BC']
bcm=tneet[tneet.COMMUNITY=='BCM']
mbc=tneet[tneet.COMMUNITY=='MBC/DNC']
sc=tneet[tneet.COMMUNITY=='SC']
sca=tneet[tneet.COMMUNITY=='SCA']
st=tneet[tneet.COMMUNITY=='ST']

print('OC:\t',len(oc))
print('BC:\t',len(bc))
print('BCM:\t',len(bcm))
print('MBC:\t',len(mbc))
print('SC:\t',len(sc))
print('SCA:\t',len(sca))
print('ST:\t',len(st))


import matplotlib.pyplot as plt


x=['OC','BC','BCM','MBC','SC','SCA','ST']
y=[len(oc),len(bc),len(bcm),len(mbc),len(sc),len(sca),len(st)]

#Plot chart with data
plt.plot(x,y)



#Customize the property
plt.title('Category wise Total Candidates');
plt.xlabel('Category')
plt.ylabel('# of Candidates')
plt.show()

x=['OC','BC','BCM','MBC','SC','SCA','ST']


#Example for Bar Chart

x=['OC','BC','BCM','MBC','SC','SCA','ST']
y=[len(oc),len(bc),len(bcm),len(mbc),len(sc),len(sca),len(st)]
plt.bar(x,y)
plt.title('Category wise Total Candidates');
plt.xlabel('Category')
plt.ylabel('# of Candidates')
plt.show()

#Example for Pie Chart
x=['OC','BC','BCM','MBC','SC','SCA','ST']
y=[len(oc),len(bc),len(bcm),len(mbc),len(sc),len(sca),len(st)]
plt.pie(y,labels=x)
plt.title('Category wise Total Candidates');
plt.xlabel('Category')
plt.ylabel('# of Candidates')
plt.show()


plt.plot(oc.index.astype('int'),np.arange(1,len(oc)+1))
plt.plot(bc.index.astype('int'),bc.CRANK.astype('int'))
plt.plot(bcm.index.astype('int'),bcm.CRANK.astype('int'))
plt.plot(mbc.index.astype('int'),mbc.CRANK.astype('int'))
plt.plot(sc.index.astype('int'),sc.CRANK.astype('int'))
plt.plot(sca.index.astype('int'),sca.CRANK.astype('int'))
plt.plot(st.index.astype('int'),st.CRANK.astype('int'))
plt.title('Category wise Rank Range');
plt.xlabel('Candidate')
plt.ylabel('Rank')
plt.legend(['OC','BC','BCM','MBC','SC','SCA','ST'])
plt.show()
