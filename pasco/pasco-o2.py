# pasco-o2.py
# Skrevet av Vegard Rekaa 11.11.2021
# kontakt@pythonskole.no

from pasco.pasco_ble_device import PASCOBLEDevice

o2sensor = PASCOBLEDevice()
o2sensor.connect_by_id('574-083')  #Endre ID til din O2-sensor

for i in range(0,100):
    o2verdi = o2sensor.read_data('OxygenGasConcentration')
    print(" O2="+str(o2verdi)+"%")

o2sensor.disconnect()
