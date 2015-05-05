from pixboard import *

def pööratudpilt(pildifail):

   pilt = load_color(pildifail)

   kõrgus = len(pilt)
#150
   laius = len(pilt[0])
#200
   uus_pilt=[]
   a = 0
   
   for y in range(1,kõrgus+1):
      uue_pildi_rida = []
      uus_pilt.append(uue_pildi_rida)
      
      for x in range(laius):           
           uue_pildi_rida.append(pilt[kõrgus-y][x])

# kõrgus - y peab algama 149-st, sest viimase piksli indeks on 149
# kõrgus + 1 tähendab, et 149-st lahutatakse 149 ja indeks on 0

   show(uus_pilt)
           

               
def peegelpilt(pildifail):

   pilt = load_color(pildifail)

   kõrgus = len(pilt)
   laius = len(pilt[0])

   uus_pilt=[]

   for y in range(kõrgus):
      uue_pildi_rida = []
      uus_pilt.append(uue_pildi_rida)
      
      for x in range(1,laius+1):
           uue_pildi_rida.append(pilt[y][laius-x])
           

   
   show(uus_pilt)
