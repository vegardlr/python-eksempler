# YATZY - pythonskole.no
# Kast terninger til du får Yatzy
# Velg hvilken terninger du vil kaste igjen
# 7.2.2022, kontakt@pythonskole.no

from pylab import *

# Dette er en funksjon. Når vi kaller den lenger ned, 
# sjekker den om alle terningene er like. Hvis de er det, 
# returnerer den en verdi som heter "Sann" (True), hvis ikke
# returnerer den "Usann" (False). 
def yatzy(terninger):
    return terninger[0] == terninger[1] and \
            terninger[0] == terninger[2] and \
            terninger[0] == terninger[3] and \
            terninger[0] == terninger[4] and \
            terninger[0] == terninger[5]

# Lag en array hvor vi kan lagre terningkastene
terninger = array([])

# Kast alle 6 terningene første gang
for i in range(6):
    terningkast = randint(5)+1 # tilfeldig tall mellom 1 og 6
    terninger = append(terninger,terningkast)

# Gjør klar en løkke hvor spilleren kan velge hvilke
# terninger som skal kastes på nytt
antall_kast = 0  # Denne skal vi telle antall kast med

# Så lenge de kastede terningene ikke viser yatzy,
# la brukeren velge hvilke terninger som kan kastes på nytt.
while not yatzy(terninger):
    antall_kast = antall_kast + 1
    #terninger = sort(terninger)
    print("Du fikk: ",terninger)

    print("Skriv inn hvilke terninger du vil kaste på nytt (f.eks.:1,2,3).")
    kast_igjen = input("Kast igjen: ")
    for k in kast_igjen.split(","):
        terninger[int(k)-1] = randint(5)+1

print("Gratulerer! Du fikk Yatzy etter",antall_kast,"kast.")
