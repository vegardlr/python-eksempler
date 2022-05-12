# konstantfart.py  12.5.2022 pythonskole.no
# Les og skriv ut endringer hvert tidssteg 
# fra en måling av bevegelse med konstant fart
from pylab import *

#Les datafil (OBS Her har jeg vært inne og endret alle "," til "."
data = loadtxt('konstantfart.csv',delimiter=';',skiprows=1, usecols=(1,2))
tid  = data[12:-1,0]
pos  = data[12:-1,1]

# TRE LØSNINGSFORSLAG
# 1) Utskrift med forløkker og indeksering
endring = []
for i in range(len(pos)-1):
    endring.append(pos[i+1]-pos[i])
print(endring)

# 2) Utskrift med innebygde array-metoder (roll)
endring = pos-roll(pos,1)
print(endring[1:-1])

# 3) Grafisk løsning med innebygde array-metoder (roll)
plot(tid,pos,label='Posisjon')
plot(tid[1:-1],(pos-roll(pos,1))[1:-1],label='Endring')
grid()
legend()
show()
