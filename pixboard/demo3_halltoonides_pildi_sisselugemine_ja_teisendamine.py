"""
Pixboard oskab (ilma animatsioonita) gif faile maatriksina sisse lugeda.
Peale sisselugemist võime me aga maatriksit suvaliselt teisendada.

NB! Enne käivamist proovi ennustada, millist laadi pilditeisendusega on tegemist.

Selle pildi teisendamine ja näitamine võib võtta mõned sekundid aega.
"""

from pixboard import *

# load_gray tagastab näidatud pildi pikslid kahemõõtmelises listis,
# st. samal kujul, nagu demo1 näitemaatriks.
# Kui tegemist on värvipildiga, siis maatriksisse satub
# ainult värvide heleduse info -- värvitooni siin ignoreeritakse.
pilt = load_gray("portree.gif")


# Me võiksime pilti kohe näidata käsuga show(pilt)
# aga antud juhul on üritame seda enne natuke mudida

# Arvutame abiinfona välja pildi mõõtmed
kõrgus = len(pilt) # ridade arv
laius = len(pilt[0]) # pildi laiuse saame esimese rea pikkuse järgi

# Järgnevas tsüklis käime läbi ja muudame ära kõik pildi pikslid
for y in range(kõrgus):
    for x in range(laius):

        # kuna pildi maatriksi välimisel tasemel on read, mitte veerud,
        # siis indekseerimisel peame kõigepealt ütlema y koordinaadi
        heledus = pilt[y][x]
        uus_heledus = 255 - heledus
        pilt[y][x] = uus_heledus 

show(pilt)



