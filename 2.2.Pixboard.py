from pixboard import *


laius = 150
kõrgus = 150
setup(laius,kõrgus)

# värvime pildi keskel olevad 4 pikslit punaseks
for x in range(laius):
    
    for y in range(x, kõrgus):
        set_pixel(x,y,"black")

# näitame oma saavutust
show()
