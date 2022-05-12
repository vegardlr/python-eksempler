# SIMULERING MED TYNGDEKRAFT I PYTHON
# Pythonskole.no 14.12.2021
#
# Versjon 2: Stjerne, planet og komet

#Installer pythonskole på ditt system med: 
#  pip install pythonskole
#Importer pythonskole.astronomi sin Tyngdekraft-funksjon
from pythonskole.astronomi import Tyngdekraft

# Lag ditt 2D-rom, og bestem: 
#  - størrelsen L (hvor stor boksen skal være, LxL)
#  - Hvilken tittel du vil ha skrevet i plottevinduet
modell = Tyngdekraft(L=10.0,tittel="Planet og komet")

# Nå skal vi legge til objekter/planeter i modellen. Da 
# trenger vi funksjonen nyttObjekt som bruker følgende argumenter: 
#   modell.nyttObjekt(posisjon, fart, masse)
#     - posisjon er en vektor med to elementer (f.eks. [1,3])
#     - fart er en vektor med to elementer
#     - masse er et vanlig desimaltall
modell.nyttObjekt([0,0],[0,0],500.)
modell.nyttObjekt([-3.0,0],[0,4.0],10.)
modell.nyttObjekt([+8.0,0],[0,-1.0],1.)

#Start simulering
modell.start()


