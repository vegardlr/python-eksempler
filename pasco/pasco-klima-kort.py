from pasco.pasco_ble_device import PASCOBLEDevice
from pasco.code_node_device import CodeNodeDevice

#Mål temperatur
tempsensor = PASCOBLEDevice()
tempsensor.connect_by_id('154-703')
temp = tempsensor.read_data('Temperature')
tempsensor.disconnect()
print("Temperatur:",temp,"C")

#Mål CO2
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('181-000')
co2 = co2sensor.read_data('CO2Concentration')
co2sensor.disconnect()
print("CO2:",co2,"ppm")

#Gi et varsel med smil eller surmunn
codenode = CodeNodeDevice()
codenode.connect_by_id('354-873')
smilemunn = [[0,0],[4,0],[2,1],[0,2],[1,3],[2,3],[3,3],[4,2]]
rettmunn = [[0,0],[4,0],[2,1],[0,3],[1,3],[2,3],[3,3],[4,3]]
surmunn = [[0,0],[4,0],[2,1],[0,4],[1,3],[2,3],[3,3],[4,4]]

if co2 < 700:
    codenode.set_leds_in_array(smilemunn)
elif co2 < 1200:
    codenode.set_leds_in_array(rettmunn)
else:
    codenode.set_leds_in_array(surmunn)

codenode.disconnect()