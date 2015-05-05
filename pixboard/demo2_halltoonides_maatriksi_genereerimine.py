"""
Me võime pildimaatriksi ka Pythoni abil genereerida.

Pildi ilmumine võib võtta mõne sekundi aega.
"""

from pixboard import *
from math import sin, radians, pi

laius = 900
kõrgus = 100

rida = []
for x in range(laius):
    # paneme piksli heleduse sõltuma x koordinaadi siinusest
    piksel = round((sin(radians(x)) / 2 + 0.5) * 255)
    rida.append(piksel) 

# dubleerime rida niimitu korda, nagu me soovime pildi kõrgust
pilt = [rida] * kõrgus
    

show(pilt)
