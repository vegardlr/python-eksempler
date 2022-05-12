# pasco-co2o2-plot.py
# Skrevet av Vegard Rekaa 17.11.2021
# kontakt@pythonskole.no

# For å gjennomføre denne øvelsen trenger du: 
#   - En PASCO //code.Node
#   - En PASCO CO2 sensor (trådløs, hvit)
#   - En PASCO O2 sensor (trådløs, hvit)
# husk å gjøre endringer i koden der vi kaller funksjonen
# connect_by_id() og endre ID til dine sensorer.

#Importer bibliotekene vi skal bruke i denne koden
import csv
import time
from pylab import *
from pasco.pasco_ble_device import PASCOBLEDevice
from pasco.code_node_device import CodeNodeDevice

# Åpne en fil hvor vi kan skrive data. 
# Denne vil kunne importeres i excel eller Python siden
f = open('co2o2-data.csv', 'w', newline='')
writer = csv.writer(f)

#Koble til PASCO-sensorene
codenode = CodeNodeDevice()
codenode.connect_by_id('354-873')  #NB Endre til ID på din //code.Node
codenode.keepalive()
 = PASCOBLEDevice()
o2sensor.connect_by_id('574-083')  #NB Endre ID til din O2-sensor
o2sensor.keepalive()
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('429-980')  #NB Endre ID til din CO2-sensor
co2sensor.keepalive()

#Lag tomme lister hvor det er mulig å lagre data fra koden
tid = []
co2 = []
o2  = []
fukt= []
temp= []

#Finn ut tidspunktet når målingene starter
tid_start = time.time()

#Skriv ut kolonne-overskrifter for skjermutskrift
print("   Tid   O2         CO2     Fukt    Temp")

#Gjenta følgende kode (med innrykk) flere ganger
for i in range(0,600):
    
    #Les data fra Pasco-sensorene
    tid_verdi  = time.time() - tid_start
    o2_verdi   = o2sensor.read_data('OxygenGasConcentration') 
    co2_verdi  = co2sensor.read_data('CO2Concentration')
    fukt_verdi = o2sensor.read_data('RelativeHumidity')
    temp_verdi = o2sensor.read_data('Temperature')
    
    # Lagre målte verdier i lister, til bruk i plotting
    tid.append(tid_verdi)
    o2.append(o2_verdi)
    co2.append(co2_verdi)
    fukt.append(fukt_verdi)
    temp.append(temp_verdi)
    
    #Bruk //code.Node til å vasle med farget lys avhengig av CO2-nivå
    if co2_verdi < 700:
        codenode.set_rgb_led(0, 255, 0)  #GREEN
        codenode.set_sound_frequency(0)
    elif co2_verdi > 700 and co2_verdi < 1200:
        codenode.set_rgb_led(255, 255, 0) #YELLOW 
        codenode.set_sound_frequency(0)
    else: 
        codenode.set_rgb_led(255, 0, 0) #RED
        codenode.set_sound_frequency(440)
    
    #Skriv data til fil (ny rad for hver måling og tid)
    writer.writerow([tid_verdi, o2_verdi, co2_verdi, fukt_verdi, temp_verdi])
 
    #Skriv ut data til skjerm
    print("{:5.1f}s {:5.1f}% {:7.0f}ppm   {:5.1f}% {:5.1f}C".format(
        tid_verdi,o2_verdi,co2_verdi,fukt_verdi,temp_verdi))
    time.sleep(5)

#Lukk filene på en ryddig måte når vi er ferdig med å skrive
f.close()
codenode.disconnect()
o2sensor.disconnect()
co2sensor.disconnect()

#Plott dataene i et vindu med flere grafer (subplots)
fig,ax = subplots(4)
ax[0].plot(tid,co2)
ax[0].set_ylabel('CO2 (ppm)')
ax[1].plot(tid,o2)
ax[1].set_ylabel('O2 (%)')
ax[2].plot(tid,fukt)
ax[2].set_ylabel('Fukt (%)')
ax[3].plot(tid,temp)
ax[3].set_xlabel('Tid (s)')
ax[3].set_ylabel('Temp (C)')

#Lagre plot-filen i en PNG-fil og vis på skjerm
savefig('co2o2-graf.png')
show()


