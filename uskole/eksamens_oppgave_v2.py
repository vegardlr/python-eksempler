# Løsningsforslag til eksamenseksempel - Oppgave 5
# Versjon 2 - Med "input"

#La brukeren skrive inn verdiene mens koden kjører
h  = input("Skriv inn den lengste siden i trekanten: ")
k1 = input("Skriv inn en annen side i trekanten: ")
k2 = input("Skriv inn den siste siden i trekanten: ")

#Gjør om variablene til desimaltall
h =  float(h)
k1 = float(k1)
k2 = float(k2)

if k1**2 + k2**2 == h**2:
    print("Pythagoras' teorem er oppfylt") #Output a
else:
    print("Pythagoras' teorem er ikke oppfylt") #Output b
