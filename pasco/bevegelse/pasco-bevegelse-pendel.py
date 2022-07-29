import pasco, time, csv
from pylab import *
dev = pasco.CodeNodeDevice()
dev.connect_by_id('354-873')

tid_start = time.time()
tid, aks = [], []
print("Start")
for i in range(100):
    tid.append(time.time()-tid_start)
    aks.append(dev.read_data('Accelerationy'))
    print(tid[-1],aks[-1])

plot(tid,aks,'-O')
xlabel('Tid (s)')
ylabel('Akselerasjon ($m/s^2$)')
title('Pendel med luftmotstand')
show()

savetxt('pendel.csv',array([tid,aks]),delimiter=",")
