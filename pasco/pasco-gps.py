import time
import numpy as np
from pasco.pasco_ble_device import PASCOBLEDevice
import matplotlib.pyplot as plt
sensor = PASCOBLEDevice()
sensor.connect_by_id('920-323')  #Endre ID til din CO2-sensor
sensor.keepalive()

data = np.empty((0, 4), float)
start_tid = time.time()
while True:
    tid = round(time.time()-start_tid,3)
    lat = sensor.read_data('Latitude')
    lon = sensor.read_data('Longitude')
    speed = sensor.read_data('Speed')
    data = np.append(data,[np.array([tid,lat,lon,speed])],axis=0)

    print("---------------------")
    print(data)

    if tid > 60*10:
        break

sensor.disconnect()
np.savetxt("gps.txt",data)

plt.plot(data[:,1],data[:,2])
plt.show()
