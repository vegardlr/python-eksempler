import numpy as np
#En selvstendig funskjon som beregner luftmotstanden som virker på pendelen.
def luftmotstand(omega):
    # ---------KONSTANTER--------------
    rho=1.293
    l=1.385
    pi=3.14
    # KULE
    m_kule=4.97e-2             # Kulas masse
    d_kule=2.3e-2              # Kulas diameter
    r_kule=d_kule/2                 # Kulas radius
    CD_kule=0.45               # Drag Coefficient Sfære
    A_kule=pi*r_kule*r_kule              # Tverrsnitt til kula
    # K_kule*v² = kraften utført på kula fra luftmotstanden
    K_kule=rho*A_kule*CD_kule/2# Faktor til utregning

    # SNOR
    # Antar at massen til snora er neglisjerbar, dvs. m_snor=0 (ingen treghet)
    t_snor=0.00023                   # Snorens tykkelse = 0.23mm
    CD_snor=1.17                   # Drag Coefficient Sylinder
    dl_snor= 0.005                 # Stykker opp snora i 5mm lange biter
    A_snor= dl_snor*t_snor         # Snorens tverrsnitt
    # K_snor*v² = kraften utført på snorstykket fra luftmotstanden
    K_snor=rho*A_snor*CD_snor/2 # Faktor til utregning
    # Beregner så treghetsmoment for å finne den angulære akselerajonen
    I=m_kule*(l*l+2*r_kule*r_kule/5)

    #---------SNORENS BIDRAG TIL LUFTMOTSTAND----------
    # Beregner luftmotstanden som virker på snora, gitt i kraftmoment. Verdiene
    # blir lagret i en vektor T
    # r - for løkkas tellerverdi, som løper fra 5 mm til 1385 mm (snorens
    # lengde).
    T_snor=0.0
    r = 0.0
    while r<l:
        r += dl_snor                    
        # Luftmotstanden gitt i kraftmoment på pendelen
        T_snor += K_snor*omega*omega*(r - dl_snor/2)*np.sign(omega)

    #--------KULAS BIDRAG TIL LUFTMOTSTAND----------------
    T_kule = K_kule*omega*omega*l*np.sign(omega)

    T=T_snor+T_kule # Totale kraftmoment som virker på pendelen
    # Returnerer pendelens (luft)kraftmoment / treghetsmoment 
    return T/I
