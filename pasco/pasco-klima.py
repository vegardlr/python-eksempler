#PASCO & Python - Klimapakken
import time
from pylab import *
from pasco.pasco_ble_device import PASCOBLEDevice
from pasco.code_node_device import CodeNodeDevice

codenode = CodeNodeDevice()
codenode.connect_by_id('354-873')
tempsensor = PASCOBLEDevice()
tempsensor.connect_by_id('574-083')
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('429-980')

tid = [time.time()]
co2 = [co2sensor.read_data('CO2Concentration')]
temp = [tempsensor.read_data('Temperature')]

smilemunn = [[0,0],[4,0],[2,1],[0,2],[1,3],[2,3],[3,3],[4,2]]
rettmunn = [[0,0],[4,0],[2,1],[0,3],[1,3],[2,3],[3,3],[4,3]]
surmunn = [[0,0],[4,0],[2,1],[0,4],[1,3],[2,3],[3,3],[4,4]]

while tid[-1] < 100.0 or co2[-1] < 700.0: 
    
    # Les data og lagre i lister
    tid.append(time.time() - tid[0])
    co2.append(co2sensor.read_data('OxygenGasConcentration'))
    temp.append(tempsensor.read_data('Temperature'))

    # Varsle via //code.Node
    if co2[-1] < 700:
        codenode.set_rgb_led(0, 255, 0)   #GREEN
        codenode.set_leds_in_array(smilemunn)
        print("Akseptabelt nivå")
    elif co2[-1] < 1200:
        codenode.set_rgb_led(255, 255, 0) #YELLOW 
        codenode.set_leds_in_array(rettmunn)
        print("Tilfør frisk luft")
    else: 
        codenode.set_rgb_led(255, 0, 0)   #RED
        codenode.set_leds_in_array(surmunn)
        print("Over akseptabelt nivå")

with open("klima-data.csv","w") as f:
    for t,c,T in zip(tid,co2,temp):
        f.write(t,c,T,"\n")
