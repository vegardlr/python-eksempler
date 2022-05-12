#Pythonskole - Skrått kast
#Dato: 3.mai 2022 - kontakt@pythonskole.no
from pylab import *

dt = 0.001
rho= 1.293               # Lufts tetthet
CD = 0.45                # Luftmotstandkoeffisient
m  = 0.050               # Kulas masse
r  = 0.05                # Kulas radius
K  = rho*pi*r*r*CD/(2*m) # Brukes i likning a = F/m = K*v*v

g  = array([ 0.0, -9.81])
p1 = array([ 0.0,   0.0])
v1 = array([10.0,  10.0])
p2 = array([ 0.0,   0.0])
v2 = array([10.0,  10.0])

luftmotstand = empty((0,2), float)
klassisk = empty((0,2), float)

while p1[1] >= 0.0 or p2[1] >= 0.0:
    a = -K*v1*v1 + g 
    v1 += a*dt
    p1 += v1*dt 
    if p1[1] >= 0.0:
        luftmotstand = vstack([luftmotstand,p1])

    v2 += g*dt
    p2 += v2*dt 
    if p2[1] >= 0.0:
        klassisk = vstack([klassisk,p2])

plot(luftmotstand[:,0],luftmotstand[:,1],label="Med luftmotstand")
plot(klassisk[:,0],klassisk[:,1],label="Klassisk")
legend()
grid()
show()