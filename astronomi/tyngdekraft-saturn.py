# SIMULERING MED TYNGDEKRAFT I PYTHON
# Pythonskole.no 14.12.2021
#
# Versjon: Saturn med måner og ringer

#Installer pythonskole på ditt system med: 
#  pip install pythonskole
#Importer pythonskole.astronomi sin Tyngdekraft-funksjon
from pythonskole.astronomi import Tyngdekraft

# Importer noen utvalgte funksjoner fra numpy
# som vi trenger for å lage lister med tall (arrays), 
# tilfeldige tall (random) og til å beregne vinkler
# og komponenter
from numpy import array, random, sin, cos, pi


# Lag ditt 2D-rom, og bestem: 
#  - størrelsen L (hvor stor boksen skal være, LxL)
#  - Hvilken tittel du vil ha skrevet i plottevinduet
modell = Tyngdekraft(L=20.0,tittel="Saturn")

# Nå skal vi legge til objekter/planeter i modellen. Da 
# trenger vi funksjonen nyttObjekt som bruker følgende argumenter: 
#   modell.nyttObjekt(posisjon, fart, masse)
#     - posisjon er en vektor med to elementer (f.eks. [1,3])
#     - fart er en vektor med to elementer
#     - masse er et vanlig desimaltall

# Legg til et stort objekt i modellen. 
# Sett den i midten, gi den null fart og stor masse (200)
modell.nyttObjekt([0,0],[0,0],500.)
# Legg til to middels store objekter like til 
# venstre og høyre for midten, og gi dem fart i y-retning
modell.nyttObjekt([-2.0,0],[0,5.0],50.)
modell.nyttObjekt([+9.0,0],[0,-2.2],50.)

#Legg til mange små objekter.
#Ved å gjenta de neste linjene med kode mange ganger. Til hver gang 
#et nytt objekt lages trekkes verdier for posisjon, hastighet og 
#størrelse som tilfeldige tall

for i in range(100): #Øk dette talletom du vil ha flere små-objekter

    #Hvert objekt får masse som er trukket fra et tilfeldig tall
    masse    = random.uniform(1.0,1.1) 

    #Hvert objekt blir plassert i en avstand fra midten
    avstand   = random.uniform(4.0,5.0)

    #Hvert objekt får en tilfeldig fart (i absolutt størrelse, 
    #foreløpig uten retning) som er gitt av objektets størrelse og 
    #avstand til midten
    fart      = 17.0*masse/avstand

    #Retningen farten får er bestemt av en vinkel, som også trekkes 
    #som et tilfeldig tall mellom 0 og 360 grader. Vinkelen er gitt
    #i radianer, så derfor er tallet mellom 0 og 2pi
    vinkel    = random.uniform(0.0,2.0*pi)

    #Vinkelen brukes også til å velge hvor rundt midten objektet 
    #plasseres, slik at hastigheten står 90 grader på en linje mellom 
    #objektet og midten. Her regner vi ut hvilke koordinater hvert 
    #objektet da får, gitt av avstand og vinkel
    posisjon  = array([avstand*cos(vinkel), avstand*sin(vinkel)])

    #Hastigheten beregnes som en vektor, gitt av farten og vinkelen
    hastighet = array([fart*sin(vinkel), -fart*cos(vinkel)])

    #Objektet legges til i modellen, med de verdiene vi har regnet
    #ut for posisjon, hastighet og masse
    modell.nyttObjekt(posisjon, hastighet, masse)

#Start simulering
modell.start()


