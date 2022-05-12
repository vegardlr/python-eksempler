#LIVE PLOTTING WITH PASCO PYTHON MODULE
#CONTACT: kontakt@pythonskole.no
#Version 26.1.2022

# Documentation: https://pypi.org/project/pasco/
from pasco.pasco_ble_device import PASCOBLEDevice

from matplotlib import animation
import matplotlib.pyplot as plt
import time
import numpy as np
import csv

##############################################################
#Edit this section: 
##############################################################
device_id = '469-021'       #Change to you sensor
data      = 'Accelerationx' #Choose from the list of available data
measure_time = 15.0         #Say how many seconds you want to measure
ymin =  8                   #What max/min y-values do you expect
ymax =  11.5
max_iterations = 200        #At how many iterations do you wish to abort?
animate = False


#################################################################
################  EDIT THIS AT YOUR OWN RISK ####################
#################################################################
# Create a code element, through which we can handle the instrument
device = PASCOBLEDevice()
device.connect_by_id(device_id)
if not device.is_connected():
    print("Connection failed")
    exit(0)

#Prevent the device to disconnect after 5 minutes
device.keepalive()

#Setup data storage and plotting parameters
fps     = 10.0
xdata   = []
ydata   = []
t_start = time.time()
t_stop  = t_start+measure_time
xdata_range = [0,measure_time]
ydata_range = [ymin,ymax]

#Set up figure, axis and plot element
fig = plt.figure()
ax  = plt.axes()
plt.title(data)
plt.ylabel(data)
plt.xlabel('Tid (s)')
ax.set_xlim(xdata_range)
ax.set_ylim(ydata_range)
line, = ax.plot([], [])

# initialization function: plot the background
def init():
    line.set_data([],[])
    return line,

# animation function.  This is called sequentially
def animate(i):
    verdi = device.read_data(data)
    tid   = time.time()-t_start
    fps = i/tid
    xdata.append(tid)
    ydata.append(verdi)
    line.set_data(xdata,ydata)
    print("Frame:{0:3d} Tid:{1:6.2f}s  fps={2:4.1f}".\
           format(i,tid,i/tid),end='\r')
    return line,

def animate_save(i):
    tid = xdata[i]
    line.set_data(xdata[0:i],ydata[0:i])
    print("Frame:{0:3d}".format(i),end='\r')
    return line,

# call the animator.
if animate == True:
    print("")
    print("Animating plot")
    anim = animation.FuncAnimation(fig, animate, init_func=init,
            frames=max_iterations, interval=1, blit=True, repeat=False)
    plt.show()
else:
    print("")
    print("Reading and saving data (NO ANIMATION)")
    for i in range(max_iterations):
        verdi = device.read_data(data)
        tid   = time.time()-t_start
        fps   = i/tid
        xdata.append(tid)
        ydata.append(verdi)
        print("Frame:{0:3d} Tid:{1:6.2f}s  fps={2:4.1f}".\
               format(i,tid,i/tid),end='\r')

#### SAVE TO VIDEO FILES (mp4 and gif) AND DATA FILE (csv)
Nframes = len(xdata)
fps_save = fps
giffile = data+'.gif'
mp4file = data+'.mp4'
csvfile = data+'.csv'
video = animation.FuncAnimation(fig, animate_save, init_func=init,
            frames=Nframes, save_count=Nframes,  
            interval=1, blit=True, repeat=False)
print("")
print("Saving video to "+giffile)
writergif = animation.PillowWriter(fps=fps_save)
video.save(giffile, writer=writergif)
print("")
print("Saving video to "+mp4file)
writervideo = animation.FFMpegWriter(fps=fps_save) 
video.save(mp4file,writer=writervideo)

device.disconnect()


#Sometimes, the first data value is None. Replace it
print("")
print("Saving data to "+csvfile)
with open(csvfile, 'w', encoding="UTF8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Tid",data])
    writer.writerows(np.array([xdata,ydata]).T.tolist())

print("Done!")
