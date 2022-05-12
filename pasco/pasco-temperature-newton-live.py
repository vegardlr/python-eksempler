#CODE: pasco-temperature-newton.py
#Version: 20.10.2021
#Author: Vegard Rekaa, Pythonskole.no
#kontakt@pythonskole.no

# Documentation: https://pypi.org/project/pasco/
from pasco.pasco_ble_device import PASCOBLEDevice
#from pasco.code_node_device import CodeNodeDevice
#from pasco.character_library import Icons

import matplotlib.pyplot as plt
import numpy as np
import time

selected_device = None
device = PASCOBLEDevice()
available_devices = device.scan()
n = len(available_devices)
print("Found ",n," devices")
for dev in available_devices: 
    if 'Temperature' in str(dev):
        selected_device = dev

if selected_device == None:
    print("No device found")
    exit(0)

device.connect(selected_device)
if not device.is_connected():
    print("Connection FAILED: "+selected_device)
    exit(0)

device.keepalive()



#Prepare measurments
tid_start = time.time()
tid = 0
tid_previous = tid
temp = float(device.read_data('Temperature'))
temp_start = temp
temp_sim = temp
temp_room = 25.0
k = 0.02

#Create storage arrays
tid_array = np.array([])
temp_array = np.array([])
temp_sim_array = np.array([])

print("Starting experiment")
print("Time(s)  Temp(data)  Temp(sim)")
print("{0:8.2f}   {1:8.2f}  {2:8.2f}".format(tid,temp,temp_sim))
while(tid < 1*60.0):
    #Measure temperature
    temp        = float(device.read_data('Temperature'))
    tid         = time.time()-tid_start

    #Simulate temperature
    dt              = tid-tid_previous
    #print(k,temp_sim,temp_room,dt)
    temp_sim        = temp_sim - k*(temp_sim-temp_room)*dt

    # Save values in arrays
    tid_array       = np.append(tid_array,[tid])
    temp_array      = np.append(temp_array,[temp])
    temp_sim_array  = np.append(temp_sim_array,[temp_sim])

    #Output / Prepare next iteration
    print("{0:8.2f}   {1:8.2f}  {2:8.2f}".format(tid,temp,temp_sim))
    tid_previous = tid
    time.sleep(1)

device.disconnect()
print("Experiment finished")

plt.plot(tid_array,temp_array,'bo-')
plt.plot(tid_array,temp_sim_array,'ro-')
plt.legend(["Data","Sim"])
plt.ylabel("Temp (C)")
plt.xlabel("Tid (s)")
plt.show()

