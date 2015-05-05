"""
Me võime pildimaatriksi ka Pythoni abil genereerida.

Pildi ilmumine võib võtta mõne sekundi aega.
"""

from pixboard import *
from math import sin, radians, pi, cos, sqrt

laius = 500
kõrgus = 500

keskx = laius // 2
kesky = kõrgus // 2
max_kaugus_keskist = sqrt(keskx ** 2 + kesky ** 2)

pilt = []
for y in range(kõrgus):
    rida = []
    for x in range(laius):
        a = round((sin(radians(x * 1)) / 2 + 0.5) * 255)
        b = round((cos(radians(y * 3)) / 2 + 0.5) * 255)
        kaugus_keskist = sqrt(abs(x - keskx) ** 2 + abs(y - kesky)**2)
        c = 255 - int (255 * (kaugus_keskist / max_kaugus_keskist))
        rida.append((a,c,b))
    pilt.append(rida)


show(pilt)
