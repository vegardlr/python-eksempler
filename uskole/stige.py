# HVOR LANG ER STIGEN
from pylab import *

vegg = input("Hvor høy er veggen?")
avstand = input("Hvor langt unna veggen setter du stigen?")
vegg = float(vegg)
avstand = float(avstand)

stige = sqrt(vegg**2 + avstand**2)
print("Stigen din må være minst",round(stige,1),"m lang")
