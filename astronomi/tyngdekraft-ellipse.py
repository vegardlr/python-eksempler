# SIMULERING MED TYNGDEKRAFT I PYTHON
# Pythonskole.no 14.12.2021
#
# Versjon 2: Ellipsebaner av ett legeme i bane rundt et stort

#Installer pythonskole på ditt system med: 
#  pip install pythonskole
#Importer pythonskole.astronomi sin Tyngdekraft-funksjon
from pythonskole.astronomi import Tyngdekraft

# Lag ditt 2D-rom, og bestem: 
#  - størrelsen L (hvor stor boksen skal være, LxL)
#  - Hvilken tittel du vil ha skrevet i plottevinduet
modell = Tyngdekraft(L=10.0,tittel="Ellipse")

# Nå skal vi legge til objekter/planeter i modellen. Da 
# trenger vi funksjonen nyttObjekt som bruker følgende argumenter: 
#   modell.nyttObjekt(posisjon, fart, masse )
#     - posisjon er en vektor med to elementer (f.eks. [1,3])
#     - fart er en vektor med to elementer
#     - masse  er et vanlig desimaltall
modell.nyttObjekt([0,0],[0,0],500.)
modell.nyttObjekt([-5.0,0],[0,2.0],10.)

#Start simulering
modell.start()


