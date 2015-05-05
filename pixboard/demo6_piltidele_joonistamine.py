"""
Me võime muuta vaid mingi osa pildist
"""
from pixboard import *

pilt = load_color("varvipilt.gif")

kõrgus = len(pilt) # ridade arv
laius = len(pilt[0]) # pildi laiuse saame esimese rea pikkuse järgi


# joonistame diagonaalis üle pildi ühe punase joone

for y in range(kõrgus):
    # kui meil oleks ruudukujuline pilt, siis võiksime
    # diagonaali koordinaatide saamiseks võtta lihtsalt x = y
    # praegu peame rohkem arvutama
    x = round(laius / kõrgus * y)
    pilt[y][x] = (255, 0, 0)

show(pilt)
