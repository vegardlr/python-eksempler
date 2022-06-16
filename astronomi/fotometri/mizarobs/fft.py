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

# Konverter tid-array til sekunder siden første måling
tid = (tid - tid[0]) / np.timedelta64(1,'s')

ind = tid.argsort()
tid = tid[ind]
mag = mag[ind]

N    = len(mag)
tid2 = np.linspace(tid[0],tid[-1],N)
mag2 = np.interp(tid2,tid,mag)
time_step = tid2[1]-tid2[0]

max_freq = 2*np.pi/time_step
min_freq = 2*np.pi/(tid[-1]-tid[0])
print(min_freq,max_freq)

ps = np.abs(np.fft.fft(mag2))**2
freqs = np.fft.fftfreq(N, time_step)
idx = np.argsort(freqs)
plt.plot(ps)
plt.xscale('log')
plt.yscale('log')
plt.show()

