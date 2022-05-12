#LIVE PLOTTING WITH PASCO PYTHON MODULE
#CONTACT: kontakt@pythonskole.no
#Version 15.10.2021

# Documentation: https://pypi.org/project/pasco/
from pasco.pasco_ble_device import PASCOBLEDevice
from pasco.code_node_device import CodeNodeDevice
from pasco.character_library import Icons

from matplotlib import animation
import matplotlib.pyplot as plt
import time
import numpy as np

##############################################################
#Edit this section: 
##############################################################
# Say what data you want to plot from the code-node. 
# These are your options: 
# 'Temperature', 'Brightness', 'Loudness', 'MagneticFieldStrength', 
# 'Accelerationx', 'Accelerationy', 'TiltAngleX', 'TiltAngleY', 
# 'CartPosition', 'CartVelocity', 'Button1', 'Button2'
data    = 'Accelerationx'   #Choose from the list above
measure_time = 15.0         #Say how many seconds you want to measure
ymin =  -15                  #What max/min y-values do you expect
ymax =  15
max_iterations = 200        #At how many iterations do you wish to abort?
dump_data = True


#################################################################
################  EDIT THIS AT YOUR OWN RISK ####################
#################################################################


# Create a code element, through which we can handle the instrument
codenode = CodeNodeDevice()
# List all code.Node-devices
codenode_list = codenode.scan('//code.Node')
if codenode_list:  # Go forth if some devices are found
    # Print the list of devices
    for i, dev in enumerate(codenode_list):
        print(str(i)+":"+str(dev))
    # Get user input which device you want. 
    # If there is only one, select that device automatically
    select = input('Select a codenode: ') if len(codenode_list) > 1 else 0
    select_codenode = codenode_list[int(select)]
    print("Connecting to:"+str(select_codenode))
    codenode.connect(select_codenode)
else:
    print("No codenode found")
    exit(0)

if not codenode.is_connected():
    print("Connection failed")
    exit(0)

smilemunn = [[0,0],[4,0],[2,1],[0,2],[1,3],[2,3],[3,3],[4,2]]
codenode.set_leds_in_array(smilemunn)

#Setup data storage and plotting parameters
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
    tid = time.time()-t_start
    verdi = codenode.read_data(data)
    print("Lest data:",verdi)
    xdata.append(tid)
    ydata.append(verdi)
    line.set_data(xdata,ydata)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
            frames=max_iterations, interval=1, blit=True, repeat=False)
plt.show()



# My experience is that this is needed to avoid 
# bluetooth-issues at connection-time
codenode.disconnect()


