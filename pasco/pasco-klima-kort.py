from pasco.pasco_ble_device import PASCOBLEDevice
from pasco.code_node_device import CodeNodeDevice
smilemunn = [[0,0],[4,0],[2,1],[0,2],[1,3],[2,3],[3,3],[4,2]]
rettmunn = [[0,0],[4,0],[2,1],[0,3],[1,3],[2,3],[3,3],[4,3]]
surmunn = [[0,0],[4,0],[2,1],[0,4],[1,3],[2,3],[3,3],[4,4]]

#Mål temperatur
tempsensor = PASCOBLEDevice()
tempsensor.connect_by_id('154-703')
temperatur = tempsensor.read_data('Temperature')
print("Temperatur:",temperatur,"C")

#Mål CO2
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('181-000')
co2verdi  = co2sensor.read_data('CO2Concentration')
print("CO2:",co2verdi,"ppm")

#Gi et varsel med smil eller surmunn
codenode = CodeNodeDevice()
codenode.connect_by_id('354-873')
if co2verdi < 700:
    codenode.set_leds_in_array(smilemunn)
elif co2verdi < 1200:
    codenode.set_leds_in_array(rettmunn)
else:
    codenode.set_leds_in_array(surmunn)

tempsensor.disconnect()
co2sensor.disconnect()
codenode.disconnect()
