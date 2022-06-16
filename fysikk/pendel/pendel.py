
# Pendel m/luftmotstand - PYTHONSKOLE.NO
# Sanntid og simultan simulering og datalogging
# av en klassisk pendel 
# 4.2.2022, kontakt@pythonskole.no
import time
import numpy as np
#from pylab import *
from pasco import PASCOBLEDevice
import matplotlib.pyplot as plt

snor_lengde = 2.43  # Pendelens lengde
vinkel_grader = 25  # Maks utslag ved start
maks_perioder = 5   # Stopp simulering ved maks_perioder
device_id='469-773' # ID på din PASCO akselerasjon sensor
ymin = 8.0          # Laveste y-verdi i ditt akselerasjonsplot
ymax = 12.0         # Høyeste y-verdi i ditt akselerasjonsplot
xmax = 16.0         # Høyeste verdi for tid som plottes

#Konstanter til bruk i utregningene
pi = np.pi
g  = 9.81            # Tyngdens akselerasjon
rho= 1.293           # Lufts tetthet
CD = 0.40            # Luftmotstand-koeffisient (en sfære har CD=0.45)
m  = 0.050           # Kulas masse
r  = 0.05            # Kulas radius
l  = snor_lengde     # Snorlengden
K  = rho*pi*r*r*CD/2 # Brukes i likning F=K*v*v

#Lister til å lagre data
omega    = []  # Vinkelhastighet
theta    = []  # Vinkelposisjon
aks_data = []  # Akselerasjon (data)
aks_sim  = []  # Akselerasjon (simulering)
tid      = []  # Tidssteg

#Setter initialverdier til løkka
tid_forrige = 0.0
periode     = 0 
omega_start = 0
theta_start = -pi*vinkel_grader/180

#Gjør klar et interaktivt plottevindu
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line_sim, = ax.plot(tid,aks_sim,lw=3,label="Simulering")
line_exp, = ax.plot(tid,aks_data,'-x',lw=3,label="PASCO data")
ax.set_xlim(0.,xmax)
ax.set_ylim(ymin,ymax)
ax.set_xlabel("Tid (s)")
ax.set_ylabel("Aks. ($m/s^2$)")
ax.legend()
fig.canvas.draw()
plt.pause(0.001)

# Gjør klar til måling av data
device = PASCOBLEDevice()
device.connect_by_id(device_id)

# Alt er klart. 
#Start pendelen først, og la brukeren velge når simuleringen starter
print("Simuleringen er klar!")
print("Vent til pendelen er på maks utslag,")
input("trykk Enter for å starte...")

#Start simulering og måling
tid_start = time.time()
tid_forrige = tid_start
while periode<maks_perioder:
    
    #Kraftberegninger
    v=np.absolute(omega_start*l)       # Fart, absoluttverdi
    am = K*v*v*np.sign(omega_start)/m  # Akselerasjon av luftmotstand
    ag = g*np.sin(theta_start)         # Akselerasjon tyngdekraft
    alpha=(ag+am)/l                    # Vinkelakselerasjon 
    
    #Les aksellerasjon målt av sensor i snorens lengderetning
    aks_data.append(device.read_data('Accelerationx'))
    
    #Beregn variabelt tidssteg dt (sanntid)
    tid_naa = time.time()
    dt = tid_naa-tid_forrige 
    print("t=",round(tid_naa-tid_start,2),"s")
    
    #Integrer vinkelposisjon og vinkelhastighet fra vinkelakselerasjon
    omega_slutt = omega_start - alpha*dt
    theta_slutt = theta_start + omega_slutt*dt
    #Beregn akselerasjon fra simulert vinkel og vinkelhastighet
    aks = g*np.cos(theta_slutt) + l*omega_slutt**2

    # Teller antall perioder pendelen har fullført
    if omega_slutt>=0 and omega_start<0:
        periode = periode + 1  
        print("Fullført periode",periode)
    
    #Lagre data i lister
    tid.append(tid_naa-tid_start)
    aks_sim.append(aks)  
    
    #Oppdater linjesegmenter i plot
    line_sim.set_xdata(tid)
    line_sim.set_ydata(aks_sim)
    line_exp.set_xdata(tid)
    line_exp.set_ydata(aks_data)
    fig.canvas.draw()
    plt.pause(0.01)

    #Forbered neste iterasjon
    theta_start = theta_slutt
    omega_start = omega_slutt
    tid_forrige = tid_naa

#Ferdig med å måle data (koble fra sensor)
device.disconnect()

#Beregn avvik mellom datapunkter i simulert og eksperimentell data
diffsum = 0.0
count = 0.0
for i in range(len(aks_data)):
    if (not aks_data[i] == None) and (not aks_sim[i] == None):
        count = count + 1
        diffsum = diffsum + np.absolute(aks_data[i]-aks_sim[i])
error_abs = round(diffsum/len(aks_data),2)
error_rel = round(diffsum/count/g,2)

print("Gjennomsnittlig absolutt feil:", error_abs)
print("Gjennomsnittlig relativ feil :", 100.0*error_rel,"%")

#Lukk interaktivt plottevindu for å få frem et statisk/endelig plot
input("Animasjon ferdig. Lukk plot-vinduet og trykk enter for å fortsette...")
plt.ioff()
plt.plot(tid,aks_sim,label="Simulering")
plt.plot(tid,aks_data,'-x',label="PASCO-data")
plt.title("Klassisk pendel - Akselerasjon")
plt.legend()
plt.xlabel("Tid (s)")
plt.ylabel("Aks. ($m/s^2$)")
plt.show()





# NOTATER IKKE TA BORT!!!
#ERFARINGER: Det ideelle oppsettet
# - Snorlengde opp til 2m OK
# - Utslag bær være større enn 20 grader
# - Lang pendel betinger lett snor (fiskensnøre) eller tungt lodd 
#   og dertil solid oppheng
# - Lodd bør skrus fast i bunn av aks.sensor
