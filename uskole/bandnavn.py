# BANDNAVN - Pythonskole
# Velg tilfeldige adjektiv og substantiv, og sett dem 
# sammen til bandnavn
# 7.2.2022 - kontakt@pythonskole.no

from pylab import *

adjektiv = ["Kule","Gale","Mystisk","Hoppete","Grønne","Friske",
        "Raske","Bråkete"]
substantiv = ["Frosker","Musikere","Poeter","Arbeidsfolk","Sangere",
        "Bøller"]

adj = choice(adjektiv)
sub = choice(substantiv)

print(adj+" "+sub)