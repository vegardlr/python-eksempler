# PYTHONSKOLE.NO
# Simulering av Jorden og James Webb i Lagrange 2. 
# 3.januar 2021, Vegard L. Rekaa
# vegard@astronomen.no
import numpy as np
import matplotlib.pyplot as plt

# Definer generelle variable
dt      = 3600.0 # 1 hour
AE      = 149.6 * 10**9 #in m
G       = 6.67  * 10**(-11) #unit

# Sett verdier for avstand (baneradius) og hastighet
# for James Webb Space Telescope og Jorden (enhet m og m/s)
Rjord   = 1.0 * AE 
Vjord   = 29.78 * 10**3 
RL2     = 151.1 * 10**9 
Rjames  = RL2*1.0000
Vjames  = Vjord * ( Rjames / Rjord )

# Sett verdier for objektenes masse (enhet kg)
Msol    = 1.989 * 10**30
Mjord   = 5.972 * 10**24
Mjames  = 6500.0 

# Deklarer posisjoner og hastighet som vektorer
# P = posisjon, V = hastighet
# NB Disse overskriver de gamle variablene Vjord og Vjames
Pjord   = np.array([Rjord,0.0])
Vjord   = np.array([0.0,Vjord])
Pjames  = np.array([Rjames,0.0])
Vjames  = np.array([0.0,Vjames])
PL2     = np.array([RL2,0.0])

# Deklarer tomme lister hvor vi kan lagre verdier for plotting
tid     = []
xjord   = []
yjord   = []
xjames  = []
yjames  = []

#Lagre initielle / startverdier for simuleringen
tid = 0.0
xjord.append(Pjord[0]/AE)
yjord.append(Pjord[1]/AE)
xjames.append(Pjames[0]/AE)
yjames.append(Pjames[1]/AE)

# Noen tekniske linjer for å kunne animere plottet
plot_interval = 10
plt.ion() 
fig, (ax1,ax2) = plt.subplots(1,2)
ax1.set_title("Normal skala")
ax1.set_xlabel("x (AE)")
ax1.set_ylabel("y (AE)")
ax1.set_aspect('equal')
ax1.set_xlim(-1.2,1.2)
ax1.set_ylim(-1.2,1.2)
ax2.set_title("Forstørret")
ax2.set_aspect('equal')
ax2.set_xlabel("x (AE)")
ax2.set_xlim(Pjord[0]/AE-0.1,Pjord[0]/AE+0.1)
ax2.set_ylim(Pjord[1]/AE-0.1,Pjord[1]/AE+0.1)
line1, = ax1.plot(0,0,'yo',label="Solen")
line2, = ax1.plot(xjord,yjord,'b-',label="Jorden")
line3, = ax1.plot(xjames,yjames,'r-',label="JWST")
line4, = ax2.plot(xjord,yjord,'b-',label="Jorden")
line5, = ax2.plot(xjames,yjames,'r-',label="JWST")
line6, = ax2.plot(PL2[0],PL2[1],'bx',label="L2")
#line7, = ax2.quiver(PL2[0],PL2[1],0.0,0.0)
ax1.legend()
ax2.legend()

# Disse bruker vi for å normere tid (utskrift til terminal)
sekunder_per_aar = 60.0*60*24*365.24
sekunder_per_dag = 60.0*60*24
# Denne variabler bruker vi til å holde orden på antall tidssteg
tidssteg = 0
#Disse bruker vi til å bestemme hvor ofte vi skal plotte
tidssteg_per_aar = int(sekunder_per_aar / dt)
plot_data_lengde = int(tidssteg_per_aar/plot_interval)-10
tidssteg_per_aar = int(sekunder_per_aar / dt)
plot_data_lengde = int(tidssteg_per_aar/plot_interval)-10
print("Tidssteg per aar",tidssteg_per_aar)
print("")

# Alt er klart.
print("SIMULERING AV JAMES WEBB OG JORDEN")
print("pythonskole.no - jameswebb-l2.py")
print("----------------------------------")
print("Steglengde (tid) = ",dt,"s = ",dt/sekunder_per_dag,"dager")
print("Tidssteg per aar = ",tidssteg_per_aar)
print("Jorden")
print("  Posisjon:  ",Pjord,"m")
print("  Hastighet: ",Vjord,"m/s")
print("James Webb Space Telescope")
print("  Posisjon:  ",Pjames,"m")
print("  Hastighet: ",Vjames,"m/s")
print("")
print("")


#Denne skal vi bruke til å etterligne en motor på JWST
Fmotor = np.array([0.0,0.0])

# La programmet kjøre til det blir avsluttet med Ctrl+C
while True:
    # Oppdater tidssteg
    tidssteg += 1
    tid += dt

    #Regn ut avstand (R) og enhetsvektor (E) mellom...
    #James Webb og Solen:
    Rjames      = np.linalg.norm(Pjames) 
    Ejames      = Pjames / Rjames
    #Jorden og Solen:
    Rjord       = np.linalg.norm(Pjord)
    Ejord       = Pjord / Rjord
    #James Webb og Jorden:
    Rjames_jord = np.linalg.norm(Pjames-Pjord)
    Ejames_jord = (Pjames-Pjord)/Rjames_jord
    
    #Regn ut kraften som virker på Jorden fra Solen
    Fjord = -Ejord * G*Msol*Mjord/Rjord**2
    #Regn ut kraften som virker på James Webb fra Jorden og Solen
    Fjames = -Ejames*G*Msol*Mjames/Rjames**2 \
                - Ejames_jord*G*Mjord*Mjames/Rjames_jord**2

    #Regn ut aksellerasjonen
    Ajord = Fjord/Mjord
    Ajames = (Fjames + Fmotor)/Mjames

    #Regn ut hastigheten fra akselerasjonen og forrige tidssteg
    Vjord += Ajord*dt
    Vjames += Ajames*dt
    #Regn ut posisjonen fra hastigheten og forrige tidsteg
    Pjord += Vjord*dt
    Pjames += Vjames*dt
    #Finn den nye posisjonen til L2 (utifra Pjord)
    PL2 = RL2 * Pjord / np.linalg.norm(Pjord)
    #Finn hvor hvor James Webb er ift. L2
    Rjames_L2 = np.linalg.norm(Pjames-PL2) 
    Ejames_L2 = (Pjames-PL2) / Rjames
    if(Rjames_L2 > 100000.0):
        Fmotor = -Ejames_L2 * G * Mjord * Mjames / Rjames_L2**2
    else:
        Fmotor = np.array([0.0,0.0])
    

    # Skriv ut antall dager som er simulert til terminal/konsoll
    print("Dager="+str(round(tid/sekunder_per_dag))+
            "  Tidssteg="+str(tidssteg)+
            "  Avstand til L2="+str(round(Rjames_L2,0))+
            "  Fmotor="+str(Fmotor)+
            "        ",end="\r")

    # Plott data, men ikke hvert eneste tidssteg. Det tar så langt tid..
    if tidssteg % 10 == 0: #Gjør dette hvert 10'ende tidsteg

        #Lagre de nye posisjonene i en array (normer størrelsene til AE)
        xjord.append(Pjord[0]/AE)
        yjord.append(Pjord[1]/AE)
        xjames.append(Pjames[0]/AE)
        yjames.append(Pjames[1]/AE)

        #Kort ned lengden av det som plottes til ett år
        xjord = xjord[-plot_data_lengde:] 
        yjord = yjord[-plot_data_lengde:] 
        xjames = xjames[-plot_data_lengde:] 
        yjames = yjames[-plot_data_lengde:] 

        #Oppdater linjene som plottes
        line2.set_xdata(xjord)
        line2.set_ydata(yjord)
        line4.set_xdata(xjord)
        line4.set_ydata(yjord)
        line3.set_xdata(xjames)
        line3.set_ydata(yjames)
        line5.set_xdata(xjames)
        line5.set_ydata(yjames)
        line6.set_xdata(PL2[0]/AE)
        line6.set_ydata(PL2[1]/AE)
#        line7.set_offsets([Pjames[0],Pjames[1]])
#        line7.set_UVC(Fmotor)

        #Juster vinduet som følger James Webb og Jorden
        ax2.set_xlim(PL2[0]/AE-0.010,PL2[0]/AE+0.010)
        ax2.set_ylim(PL2[1]/AE-0.010,PL2[1]/AE+0.010)

        #Tegn det nye plottet
        fig.canvas.draw()
        plt.pause(0.0001)
    
    
