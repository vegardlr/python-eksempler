from pylab import *
print("")

lengde = 100 #cm
print("Høyde (cm)   Vinkel (grader)")
for høyde in [0.0, 1.3, 5.6, 10.4, 14.7]:
    vinkel = arcsin(høyde/lengde) * 180/pi
    print(høyde,"        ", round(vinkel,1))



print("")
    