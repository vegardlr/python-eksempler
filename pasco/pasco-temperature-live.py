#CODE: pasco-temperature-live.py
#Version: 26.1.2022
#Author: Vegard Rekaa, Pythonskole.no
#kontakt@pythonskole.no

# Documentation: https://pypi.org/project/pasco/
from pasco.pasco_ble_device import PASCOBLEDevice

from time import time
from matplotlib import animation
import matplotlib.pyplot as plt
from numpy import polyfit

#Connect to the PASCO device. 
device = PASCOBLEDevice()
print(device.scan())
device_id = '940-072' #Change ID to your sensor
device.connect_by_id(device_id)

#set up the experiment
tid_start = time()
tid = 0
xmin = 0
xmax = 120.0
ymin = 10.0
ymax = 50.0
interval = 2000 #ms between each message
max_iterations = int((xmax-xmin)/(interval/1000))
data_type = 'Temperature'
xdata  = []
y1data = []
y2data = []


def curvefit():
    #Second order polynomial curve fit
    if len(xdata) < 3:
        a,b,c = 0.0,0.0
    else:
        a,b,c = polyfit(xdata,y1data,1)
    return [a*x*x + b*x + c for x in xdata]

    #Fourth order polynomial curve fit
    #if len(xdata) < 5:
    #    a,b,c,d,e = 0.0,0.0,0.0,0.0,0.0
    #else:
    #    a,b,c,d,e = polyfit(xdata,y1data,4)
    #return [a*x**4 + b*x**3 + c*x**2 + d*x + e for x in xdata]


############################################
### EVERYTHING BELOW HERE IS VOODO MAGIC ###
###        READ AT YOUR OWN RISK         ###
###    (you might learn something new)   ###
############################################

#Set up figure, axis and plot element
fig = plt.figure()
ax  = plt.axes()
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin,ymax])
plt.xlabel("Tid (s)")
plt.ylabel("Temperatur (C)")
labels     = ['Data','Curve fit']
colors     = ["blue","red"]
linestyles = ['dotted','solid']
markers    = ['.','']

#Set up initial line elements
lines = []
for index in range(2):
    lobj = ax.plot([],[],linewidth=1,label=labels[index],color=colors[index],
            linestyle=linestyles[index],marker=markers[index])[0]
    lines.append(lobj)


# initialization function: plot the background
def init():
    for line in lines:
        line.set_data([],[])
    plt.legend()
    return lines

# animation function.  This is called sequentially
def animate(i):
    tid = time()-tid_start
    print("Frame:{0:3d} Tid:{1:6.2f}s  fps={2:4.1f}".\
            format(i,tid,i/tid),end='\r')
    xdata.append(tid)
    y1data.append(device.read_data(data_type))
    y2data = curvefit()
    lines[0].set_data(xdata,y1data)
    lines[1].set_data(xdata,y2data)
    return lines


# call the animator (this is voodo magic)
print("Max iterations:",max_iterations)
anim = animation.FuncAnimation(fig, animate, init_func=init,
            frames=max_iterations, interval=interval, repeat=False)

plt.show()
device.disconnect()
