# pasco-light.py
# Skrevet av Vegard Rekaa 11.11.2021
# kontakt@pythonskole.no

from pylab import *
import time
from pasco.pasco_ble_device import PASCOBLEDevice
lightsensor = PASCOBLEDevice()
#PASCO Lyssensor kan måle følgende datatyper:  
#    'R', 'G', 'B', 'IR', 'UVA', 'UVB', 'UVIndex', 
#    'Illuminance', 'SolarIrradiance', 'SolarPAR', 'White'
data = 'Illuminance'
lightsensor.connect_by_id('900-209')  #Endre ID til din sensor
enhet = lightsensor.get_measurement_unit(data)

x = []
y = []
tid_start = time.time()
for i in range(0,100):
    tid = time.time() - tid_start
    verdi = lightsensor.read_data(data)
    x.append(tid)
    y.append(verdi)
    print(str(verdi)+enhet)
    time.sleep(1)
lightsensor.disconnect()

plot(x,y)
ylabel("Illuminance (lux)")
xlabel("Tid (s)")
show()