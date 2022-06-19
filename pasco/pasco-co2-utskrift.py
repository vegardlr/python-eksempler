# pasco-co2.py
# Skrevet av Vegard Rekaa 16.06.2022
# kontakt@pythonskole.no
import time
from datetime import datetime
import matplotlib.pyplot as plt
from pasco.pasco_ble_device import PASCOBLEDevice
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('429-980')  #Endre ID til din CO2-sensor
start = datetime.now()
prev  = start
forrige_verdi = co2sensor.read_data('CO2Concentration')

plt.ion()
x = []
y = []
for i in range(300):
    verdi = co2sensor.read_data('CO2Concentration')
    now   = datetime.now()
    sek   = (now-prev).total_seconds()
    tid   = (now-start).total_seconds()
    deriv = (verdi - forrige_verdi)/sek
    print("CO2 nivå: %d ppm. Derivert: %f ppm/s " %(verdi,round(deriv,2)))
    prev = now
    forrige_verdi = verdi

    x.append(tid)
    y.append(verdi)
    plt.plot(x,y)
    plt.draw()
    plt.pause(1)

co2sensor.disconnect()

