from pylab import sqrt

c = 299792458 #m/s  Lysets hastighet
v = (1-1.8e-12)*c # Buzz lightyear sin hastighet

gamma = 1/sqrt(1-v**2/c**2) # Relativitetsfaktoren

t0 = 4*60 # minutes  #Reisetid (ifølge Buzz)
m0 = 1    # vekt (astronautens)

t = t0 * gamma  # Regner ut relativistisk tid
m = m0 * gamma  # Regner ut relativistisk masse

print("(v-c)/c:",((c-v)/c)*100,"%")
print("t0= %ds " % (t0))
print("t=%ds = %d timer = %d døgn = %f år" % (t,t/3600,t/86400,t/31556926))
print("m0= %dkg" % (m0))
print("m=%dkg = %f Falcon 9 raketter = %f F35 fly" % (m,m/549054,m/13100))

