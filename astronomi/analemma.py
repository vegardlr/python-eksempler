#Kode utviklet av Pythonskole.no 8.11.2021
#Se instrukser for hvordan installere 
#bibliotekene som brukes i denne koden på 
#pythonskole.no/starthjelp
#Kode en delt gratis for bruk til undervisning.
# - Vegard Rekaa, kontakt@pythonskole.no

import ephem
import matplotlib.pyplot as plt

#Definer foerst et sted hvor vi skal 
#observere solen fra.
#Tilpass variable sted.lat og sted.lon
#om dere oensker en utvalgt by.
#Ephem vil ha alle verdier oppgitt som 
#tekst-variable, så derfor må de omkapsles
#av anførseltegn ('xx.xx').
sted = ephem.Observer()
sted.date = '2016/01/01 12:00:00'
sted.lat = '60.0'
sted.lon = '10.0'

#Biblioteket vet hva solen er, vi maa bare
#opprette en lenke fra vaar kode til Solen
#i PyEphem
sol = ephem.Sun()

#Tomme lister hvor vi skal lagre data
#Disse skal vi plotte siden
alt = []
az = []

#Vi vil ogsaa ha merkelapper i plottet 
#som sier hvor paa analemmaet vi finner
#utvalgte datoer
merker_tekst = []
merker_alt = []
merker_az = []

#Saa en for-loekke hvor vi tar 365 steg. Verdien av
#for-variablen 'day' brukes ikke til noe
for day in range(0,365):

	#Beregner solens posisjon sett fra 'sted' 
	sol.compute(sted)

	#Legg til solens posisjon i datalistene
    #Siden solens verdier for 'alt' og 'az' oppgis i 
    #radianer [0,2pi], må vi regne om til grader før
    #verdiene lagres i våre egne lister 'alt' og 'az'
	alt.append(float(sol.alt)*180.0/ephem.pi)
	az.append(float(sol.az)*180.0/ephem.pi)

	#Lagre dato som en tuple (tuple = vektor)
	#d[2] = dag i maaneden
	#d[1] = maaned-nr
	d = sted.date.tuple()

	#Hvis det er den foerste dagen i en maaned 
	#eller datoen er 21/3, 21/6, 21/9 eller 21/12, 
	#("x%3==0" tester om x er delelig med 3)
	#lag en merkelapp i plottet med dato paa rett posisjon
	if d[2]==1 or (d[2]==21 and d[1]%3==0):

		#Legg til et tekst-element i merker_tekst-listen
		#med formatet 'dag/maaned'
		merker_tekst.append("%s.%s"%(d[2],d[1]))

		#Lagre solens posisjon denne dagen slik
		#at vi kan sette merkelappen paa samme 
		#plass som grafen i plottet
		merker_az.append(az[-1])
		merker_alt.append(alt[-1])
	
	#Oek steget med 1 dag foer neste 
	#gjennomgang av for-loekken
	sted.date = ephem.Date(sted.date+1)

#Plot dataene
plt.plot(az,alt)

#Plot merkelappene 
for i in range(0,len(merker_tekst)):
	plt.plot(merker_az[i],merker_alt[i],'+',color='blue')
	plt.text(merker_az[i],merker_alt[i]+0.5,merker_tekst[i])

#Tekst paa aksene
plt.ylabel('Altitude')
plt.xlabel('Azimuth')
plt.title('Analemma\nLat=%s Lon=%s ' % (sted.lat,sted.lon))

#Vis bildet
plt.show()
