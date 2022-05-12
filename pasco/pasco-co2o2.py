# pasco-co2o2.py
# Skrevet av Vegard Rekaa 11.11.2021
# kontakt@pythonskole.no

from pylab import *
import time
from pasco.pasco_ble_device import PASCOBLEDevice

#o2sensor = PASCOBLEDevice()
#o2sensor.connect_by_id('574-083')  #Endre ID til din O2-sensor
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('429-980')  #Endre ID til din CO2-sensor

tid_start = time.time()
tid = []
co2 = []
o2  = []
for i in range(0,100):
    t = time.time()-tid_start
    #o2verdi = o2sensor.read_data('OxygenGasConcentration')
    co2verdi = co2sensor.read_data('CO2Concentration')
    tid.append(t)
    co2.append(co2verdi)
    #o2.append(o2verdi)
    print(" O2="+str(o2verdi)+"%   CO2="+str(co2verdi)+"ppm")
    time.sleep(1)

#o2sensor.disconnect()
co2sensor.disconnect()


plot(tid,co2)

