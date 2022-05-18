#!/usr/bin/env python3
import sys
import numpy as np
from astropy.time import Time
import matplotlib.pyplot as plt

#Angi hvilken mappe du vil lese data fra
# (ta bort "#" fra den linjen du vil bruke, 
#  og legg til en "#" fordan de du er ferdig med) 
datafolder = "W-lyr"
#datafolder = "IR-gem"
#datafolder = "S-vul"
#datafolder = "U-gem"

#Les data fra mappenavn/data.txt
f = open(datafolder+"/data.txt",'r')
data = np.genfromtxt(f,delimiter='\t')

#Lagre relevante kolonner fra datafilen som tid og mag
tid = Time(data[:,0],format='jd').to_value('datetime64')
mag = data[:,1]

#Vis data - Resten av jobben gjøres i plottevinduet eller "på ark"
plt.plot(tid,mag,'.')
plt.grid(True)
plt.xlabel("Tid")
plt.ylabel("Mag")
plt.title(datafolder)
ax = plt.gca()
ax.invert_yaxis()
plt.show()

