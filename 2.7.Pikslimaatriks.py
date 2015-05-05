from pixboard import *

def peegelpilt(pildifail):

   pilt = load_color(pildifail)

   kõrgus = len(pilt)
   laius = len(pilt[0])

   for y in range(kõrgus):
       for x in range(laius):
           piksel = pilt[y][x]
           pilt[x][y] = piksel

   show(pilt)
           
    
