#!/usr/bin/env python3
import sys
import numpy as np
from astropy.time import Time
import matplotlib.pyplot as plt

#Åpne mappe og finn datafil, les til minnet. 
if len(sys.argv) < 2:
    print("Usage: viewdata.py datafolder")
    sys.exit(1)
datafolder = sys.argv[1]
datafile = datafolder+"/data.txt"
f = open(datafile,'r')
data = np.genfromtxt(f,delimiter='\t')

#Lagre relevante kolonner fra datafilen som tid og mag
tid = Time(data[:,0],format='jd').to_value('datetime64')
mag = data[:,1]

#Vis data - Resten av jobben gjøres i plottevinduet eller "på ark"
plt.plot(tid,mag,'-.')
plt.grid(True)
plt.xlabel("Tid")
plt.ylabel("Mag")
plt.title(datafolder)
ax = plt.gca()
ax.invert_yaxis()
plt.show()
