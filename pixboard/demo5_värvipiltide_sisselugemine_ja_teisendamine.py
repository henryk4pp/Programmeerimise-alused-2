"""
Kui soovid pilti sisse lugeda värvilisena, siis tuleb
load_gray asemel kasutada funktsiooni load_color
"""
from pixboard import *

pilt = load_color("varvipilt.gif")

kõrgus = len(pilt) # ridade arv
laius = len(pilt[0]) # pildi laiuse saame esimese rea pikkuse järgi


# tõmbame punase värvikomponendi nulli
for y in range(kõrgus):
    for x in range(laius):
        piksel = pilt[y][x]
        uus_piksel = (0, piksel[1], piksel[2])
        pilt[y][x] = uus_piksel

show(pilt)
