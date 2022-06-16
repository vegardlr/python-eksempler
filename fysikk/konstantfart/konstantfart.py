from pylab import *

#Les data eksportert fra SparkVue
data = loadtxt('konstantfart.csv',\
        delimiter=';',skiprows=1, usecols=(1,2))
tid  = data[12:-1,0]
pos  = data[12:-1,1]

# Regn ut endring per tid
endring = (pos-roll(pos,1))[1:-1]/(tid[1]-tid[0])

# Vis frem resultatet grafisk
plot(tid,pos,label='Posisjon $x(t)$')
plot(tid[1:-1],endring,label='Endring $\Delta x/\Delta t$')
xlabel("t (s)")
ylabel("$x(t)$ (m) og $\Delta x/\Delta t$ (m/s)")
grid()
legend()
show()
