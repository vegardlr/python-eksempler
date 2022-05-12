# pasco-co2.py
# Skrevet av Vegard Rekaa 17.11.2021
# kontakt@pythonskole.no

from pasco.pasco_ble_device import PASCOBLEDevice
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('181-000')  #Endre ID til din CO2-sensor
for i in range(0,10):
    verdi = co2sensor.read_data('CO2Concentration')
    if verdi > 700:
        melding = "Det er for høyt. Kan du åpne et vindu?"
    elif verdi < 400: 
        melding = "Oi, det var lavt. Er du på vei ut i verdensrommet?"
    else:
        melding = "Alt OK!"
    print("CO2 i rommet er "+str(verdi)+"ppm. "+melding)
co2sensor.disconnect()
