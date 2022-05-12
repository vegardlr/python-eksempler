# gener.py Versjon 1
# Forfatter: Birgitte Overå Hovland (mattelærer, Bergen)
# Kilde: Facebookgruppen "Programmering i skolen og programmeringsdidaktikk"
import random

genom = ["Aa","Bb","Cc","Dd","Ee","Ff"]

mor  = []
far  = []
barn = []

# Fars og mors gener velges tilfeldig
for gen in genom:
    far_gen = random.choice(gen) + random.choice(gen)
    far.append(far_gen)
    mor_gen = random.choice(gen) + random.choice(gen)
    mor.append(mor_gen)
    
#Barns gener kombineres av mor og far
for mor_gen,far_gen in zip(mor,far):
    barn_gen = random.choice(mor_gen)+random.choice(far_gen)
    barn.append(barn_gen)

#Enkel utskrift
print("far  ",far)
print("mor  ",mor)
print("barn ",barn)
