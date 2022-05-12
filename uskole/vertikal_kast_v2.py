# VERTIKALT KAST - Versjon 2
# Enkel fysikk-simulering av bev.likningene
# med søk etter maksimumsverdier
# 7.2.2022, kontakt@pythonskole.no

from pylab import *

# Forbered simuleringen
dt = 0.1       # tidsteg (s)
t_start = 0.0  # start tidsmåling (s)
v_start = 10.0 # start hastighet (m/s)
h_start = 0.0  # start høyde (m)
a = -9.81      # tyngdens akselerasjon (m/s²)

# Forbered variable til å finne maks-verdier
v_maks = v_start
h_maks = h_start

while h_start >= 0.0:

    #Regn ut nye verdier for hastighet (v) og posisjon (h)
    t_slutt = t_start + dt
    v_slutt = v_start + a*dt
    h_slutt = h_start + v_slutt*dt
    
    #Skriv ut resultatet underveis
    print("Når t=",round(t_slutt,1),"s    er h=",round(h_slutt,1),"m")

    # Finn maksimale verdier for fart og høyde
    if h_slutt > h_maks:
        h_maks = h_slutt
    if v_slutt > v_maks:
        v_maks = v_slutt
    
    # Gjør klar til neste iterasjon
    h_start = h_slutt
    v_start = v_slutt
    t_start = t_slutt

#Programmet er ferdig
print("Ballen har landet!")
print("Maksimale høyde var:",round(h_maks,1),"m")
print("Maksimale hastighet var:",v_maks,"m/s")

