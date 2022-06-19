# pasco-co2-plot.py
# Skrevet av Vegard Rekaa 16.06.2022
# kontakt@pythonskole.no
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
co2sensor = PASCOBLEDevice()
co2sensor.connect_by_id('429-980')  #NB Endre ID til din CO2-sensor

#Lag tomme lister hvor det er mulig å lagre data fra koden
tid = []
co2 = []

#Finn ut tidspunktet når målingene starter
tid_start = time.time()

#Skriv ut kolonne-overskrifter for skjermutskrift
print("   Tid   O2         CO2     Fukt    Temp")

#Gjenta følgende kode (med innrykk) flere ganger
for i in range(0,600):
    
    #Les data fra Pasco-sensorene
    tid_verdi  = time.time() - tid_start
    co2_verdi  = co2sensor.read_data('CO2Concentration')
    
    # Lagre målte verdier i lister, til bruk i plotting
    tid.append(tid_verdi)
    o2.append(o2_verdi)
    co2.append(co2_verdi)
    
    
    #Skriv data til fil (ny rad for hver måling og tid)
    #writer.writerow([tid_verdi, o2_verdi, co2_verdi, fukt_verdi, temp_verdi])
 
    #Skriv ut data til skjerm
    print("{:5.1f}s {:5.1f}% {:7.0f}ppm   {:5.1f}% {:5.1f}C".format(
        tid_verdi,o2_verdi,co2_verdi,fukt_verdi,temp_verdi))
    time.sleep(5)

#Lukk filene på en ryddig måte når vi er ferdig med å skrive
f.close()
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


