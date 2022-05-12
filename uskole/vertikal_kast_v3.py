# VERTIKALT KAST - Versjon 3
# Enkel fysikk-simulering av bev.likningene
# med grafisk fremstilling av data
# 7.2.2022, kontakt@pythonskole.no

from pylab import *

# Forbered simuleringen
dt = 0.1       # tidsteg (s)
t_start = 0.0  # start tidsmåling (s)
v_start = 10.0 # start hastighet (m/s)
h_start = 0.0  # start høyde (m)
a = -9.81      # tyngdens akselerasjon (m/s²)

# Definer arrays hvor vi kan lagre data
t = array([])
v = array([])
h = array([])

# Lagre de første verdiene i arrays
t = append(t,t_start)
v = append(v,v_start)
h = append(h,h_start)

while h_start >= 0.0:

    #Regn ut nye verdier for hastighet (v) og posisjon (h)
    t_slutt = t_start + dt
    v_slutt = v_start + a*dt
    h_slutt = h_start + v_slutt*dt
    
    #Skriv ut resultatet underveis
    print("Når t=",round(t_slutt,1),"s    er h=",round(h_slutt,1),"m")

    #Lagre nye verdier i en array
    t = append(t,t_slutt)
    v = append(v,v_slutt)
    h = append(h,h_slutt)
    
    # Gjør klar til neste iterasjon
    h_start = h_slutt
    v_start = v_slutt
    t_start = t_slutt


#Programmet er ferdig
print("Ballen har landet!")

# Vis dataene vi har lagret grafisk
plot(t,h)
xlabel("Tid (s)")
ylabel("Høyde (m)")
show()
