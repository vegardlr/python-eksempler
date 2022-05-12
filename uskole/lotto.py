# LOTTO - Pythonskole.no
# Simuler et lottospill, hvor du 
# fortsetter å kjøpe lodd helt til 
# du har vunnet 7 rette én gang. 
# 7.2.2022, kontakt@pythonskole.no
from pylab import *

# Regn ut sannsynligheten for å vinne 7 rette
sannsynlighet = 1.0/2500000.0  #1:2 500 000

# Lag en teller-variabel for å telle antall bonger
antall_bonger = 0

# Når vi har vunnet, setter vi denne til True. 
har_vunnet = False

# Så lenge vi ikke har vunnet...
while not har_vunnet:
    # Tell at vi kjøper én bong til
    antall_bonger = antall_bonger + 1
    # Trekk et tilfeldig desimaltall mellom 0 og 1
    tilfeldig_tall = random()
    # Sjekk om det tilfeldige tallet er lavere enn sannsynligheten
    if tilfeldig_tall < sannsynlighet:
        # Hvis ja, sett variablen har_vunnet slik at løkken stopper
        har_vunnet = True

# Når vi kommer hit, har vi vunnet! 
# Skriv ut beskjed og antall lodd vi måtte kjøpe for å vinne
print("Gratulerer! Du har vunnet 7 rette i Lotto!")
print("Du kjøpte",antall_bonger,"bonger før du vant.")
