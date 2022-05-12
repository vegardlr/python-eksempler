#Exoplanet (read rawdata, print simplified)
#Pythonskole 11.4.2022

import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
import astropy.time as at

def datestring(bjd_tdb):
    # BJD : baryonic julian date
    # https://en.wikipedia.org/wiki/Barycentric_Julian_Date
    astropyTimeObject = at.Time(str(bjd_tdb), format='jd',scale='tdb')
    return at.Time.strftime(astropyTimeObject ,'%Y-%m-%d %H:%M:%S')

#Initialize storage
time  = []
stars = [[] for i in range(9)]

#Read data file
f = open('Measurements_Quatar1b_HD.txt', 'r')
header = f.readline() #Skip header line

for line in f:
    data = line.strip().split("\t")
    time.append(float(data[8])) #Julian day
    #Relative flux of stars t1,c2,c3,c4,c5,c,c7,c8 and c9
    for i in range(9): stars[i].append(float(data[21+i]))
f.close()

obsdate_start = datestring(time[0])
obsdate_stop  = datestring(time[-1])
print("Observation start: ", obsdate_start)
print("Observation stop: " , obsdate_stop)
print("Number of measurments:",len(stars[0]))

#Find and subtract linear trend in target data
a,b = np.polyfit(time,stars[0],1)
stars[0] = [s/(a*t+b) for t,s in zip(time,stars[0])]

#Normalize all data-sets to 1
for i in range(9):
    m = np.mean(stars[i])
    # Normalize against first and last 30 elements of data
    m = np.mean([stars[i][0:30],stars[i][-31:-1]])
    stars[i] = [s/m for s in stars[i]]


columns = ['Datetime','BJD_TDB','Duration (seconds)','Relative flux T1','Relative flux C2','Relative flux C3','Relative flux C4','Relative flux C5','Relative flux C6','Relative flux C7','Relative flux C8','Relative flux C9']
f = open('Exoplanet_Quatar1b_HD.csv','w')
writer = csv.writer(f)
writer.writerow(["Object:","Quatar 1B HD (exoplanet)"])
writer.writerow(["Observation start: ", obsdate_start])
writer.writerow(["Observation stop: " , obsdate_stop])
writer.writerow(["Data columns:"])
writer.writerow(["0:","Datetime (yyyy-mm-dd HH:MM:SS)"])
writer.writerow(["1:","Julian date (BJD_TDB)"])
writer.writerow(["2:","Duration (seconds)"])
writer.writerow(["3:","Relative flux of target star (T1)"])
writer.writerow(["4-8:","Relative flux of comparison stars (C2-C9)"])
writer.writerow(columns)
for it in range(len(time)):
    dt = datestring(time[it])
    bjd_tdb = time[it]
    duration_seconds = round((time[it]-time[0])*24*60*60)
    row = [dt,bjd_tdb,duration_seconds]
    for i in range(9):
        row.append(stars[i][it])
    writer.writerow(row)
f.close()


