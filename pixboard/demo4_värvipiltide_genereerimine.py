"""
Värve esitatakse arvutis tavaliselt kolme värvi (punane, roheline, sinine)
kombinatsioonina. Justnagu halltoonide puhul, kasutame värvide intensiivsuse
märkimiseks täisarve vahemikus 0..255.

Pythonis esitatakse värve tavaliselt kolmeelemendilise listi või ennikuga.
Nt. (255, 0, 0) tähendab erepunast, (0, 255, 0) rohelist aga (24, 192, 184)
heledat rohekassinist. Erinevaid kombinatsioone saad katsedada näiteks siin:
http://www.maxi-pedia.com/rgb+color+picker

Ka pixboard oskab näidata värvipilte. Selleks tuleb lihtsalt pikslitena
kasutada täisarvude asemel kolmeelemendilisi ennikuid.

Järgnev näide genereerib pildi, kus pikslite värvis varieeritakse
sinise ja rohelise hulka vastavalt piksli koordinaatidele
"""
from pixboard import *


pilt = []
red = 255

for green in range(255):
    rida = []
    for blue in range(255):
        piksel = (red, green, blue)
        rida.append(piksel)
    pilt.append(rida)

show(pilt)
