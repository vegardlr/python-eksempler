# pasco-light.py
# Skrevet av Vegard Rekaa 11.11.2021
# kontakt@pythonskole.no

from pylab import *
import time
from pasco.pasco_ble_device import PASCOBLEDevice
from pasco.code_node_device import CodeNodeDevice
device = PASCOBLEDevice()
codenode = CodeNodeDevice()
#PASCO Værstasjon kan måle følgende datatyper:  
#['Temperature', 'RelativeHumidity', 'AbsoluteHumidity', 'BarometricPressure', 'WindSpeed', 'DewPoint', 'WindChill', 'Humidex', 'SatelliteCount', 'Latitude', 'Longitude', 'Altitude', 'Speed', 'UVIndex', 'Illuminance', 'SolarIrradiance', 'SolarPAR', 'WindDirection', 'MagneticHeading', 'TrueHeading']

device_id = '920-323'
data = 'DewPoint'
device.connect_by_id(device_id)  #Endre ID til din sensor
enhet = device.get_measurement_unit(data)


#Vi bruker en //code.Node til enkel output til bruker
#//code.Node har følgende data tilgjengelig: 
#['Temperature', 'Brightness', 'Loudness', 'MagneticFieldStrength', 'Accelerationx', 'Accelerationy', 'TiltAngleX', 'TiltAngleY', 'CartPosition', 'CartVelocity', 'Button1', 'Button2']
#codenode_id = '479-256'
#codenode.connect_by_id(codenode_id)

x = []
y = []
tid_start = time.time()
for i in range(0,100):
    tid = time.time() - tid_start
    verdi = device.read_data(data)
    x.append(tid)
    y.append(verdi)
    print(str(verdi)+enhet)
#    time.sleep(1)
#    if codenode.read_data('Button1') == 1:
#        temperatur = device.read_data('Temperature')
#        print("Temperatur=",temperatur,"*C")




device.disconnect()
#codenode.disconnect()

plot(x,y)
ylabel("Illuminance (lux)")
ylabel(data+" ("+enhet+")")
xlabel("Tid (s)")
show()


#TODO: Write to file
