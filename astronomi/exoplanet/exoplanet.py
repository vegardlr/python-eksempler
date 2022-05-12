#Exoplanet (dataanalyse)
#Pythonskole.no 11.4.2022
import csv
import matplotlib.pyplot as plt

#Data storage 
time = []
flux = [[] for i in range(9)]

# Read data from csv-file
with open('Exoplanet_Quatar1b_HD.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=',')
    for i in range(10): 
        next(reader) # Skip header (10 lines)
    for row in reader:
        time.append(float(row[2])) # Col 2: Duration (seconds)
        for i in range(9):
            flux[i].append(float(row[3+i]))

time = [t/3600 for t in time ] #Convert time (duration) to hours

for i in range(9):
    plt.plot(time,flux[i],lw=1,ls='--')

#Plot target data (again) on top
plt.plot(time,flux[0],lw=2,color='b')
plt.xlabel('Time (h)')
plt.ylabel('Relative flux')

plt.show()
