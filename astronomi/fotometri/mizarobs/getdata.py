#!/usr/bin/env python3
import os,sys
import urllib.request
import numpy as np
import matplotlib.pyplot as plt

sys.exit(1)

if len(sys.argv) < 3: 
    print("Usage getdata.py datafolder url")
    sys.exit(1)

datafolder = sys.argv[1]
url = sys.argv[2]

#url = "http://mizar.voksenlia.net/Variable/Redukvis/W-lyr/01-63-76/"
#url = "http://mizar.voksenlia.net/Variable/Redukvis/W-lyr/02-76-82/"
#url = "http://mizar.voksenlia.net/Variable/Redukvis/W-lyr/03-82-89/"
#url = "http://mizar.voksenlia.net/Variable/Redukvis/W-lyr/04-89-97/"
#url = "http://mizar.voksenlia.net/Variable/Redukvis/W-lyr/05-97-03/"
#url = "http://mizar.voksenlia.net/Variable/Redukvis/W-lyr/06-03-08/"
#datafolder = "W-lyr"

#url = "http://mizar.voksenlia.net/Variable/Redukvis/Ir-gem/"
#datafolder = "IR-gem"

if not os.path.isdir(datafolder):
    os.mkdir(datafolder)


def isdata(line):
    elements = str(line.decode('UTF8')).split(" ")
    #print(elements)
    if len(elements) < 4:
        return False
    try: 
        float(elements[1])
    except ValueError: 
        return False
    try: 
        float(elements[-1])
    except ValueError: 
        return False
    return True

def getcolumns(line):
    elements = str(line.decode('UTF8')).split(" ")
    return [float(elements[1]),float(elements[-1])]

def readmagfile(path):
    print("Reading data from: "+path)
    mf = urllib.request.urlopen(path)
    for mline in mf.readlines():
        line = mline.rstrip()
        if isdata(line):
            data.append(getcolumns(line))

print("Downloading data from: "+url)
indexfile = datafolder+"/index.html"
#if not os.path.isfile(indexfile):
os.system("wget -q -O "+indexfile+" "+url)
index = open(indexfile)
data = []
subfolders = []
for iline in index:
    if "[DIR]" in iline:
        subfolders.append(iline[80:88])

index.close()

print(subfolders)

if len(subfolders) == 0:
    for iline in index:
        if "MAG" in iline:
            readmagfile(url+iline[81:90])
else:
    for sub in subfolders:
        subindexfile = datafolder+"/"+sub+".html"
        print("Downloading: "+subindexfile)
        os.system("wget -q -O "+subindexfile+" "+url+"/"+sub)
        subindex = open(subindexfile,'r')
        print("Reading: "+url+sub)
        for sline in subindex:
            if "MAG" in sline:
                readmagfile(url+sub+"/"+sline[81:90])

        subindex.close()


data = np.array(data)
datafile = datafolder+"/data.txt"

plt.plot(data[:,0],data[:,1],'o')
plt.title("Preview of "+datafile)
plt.xlabel("JD")
plt.ylabel("Mag")
plt.show()


mode=None
print("Writing data to: "+datafile)
if os.path.isfile(datafile):
    print("Datafile exists: "+datafile)
    while mode != "a" and mode != "w" and mode != "q":
        mode = input("Overwrite (w), append (a) or quit (q)? ")
if mode == "q":
    sys.exit(0)

if mode == None: 
    mode = 'w'

with open(datafile,mode) as f:
    f.write("#Data source:"+url+"\n")
    f.write("#JD    MAG\n")
    for d in data:
        s = [str(i) for i in d]
        f.write("\t".join(s)+"\n")
