from pixboard import *

# Colors can be specified either by English color names or by 
# by integer triples, where first integer specifies the amount of red,
# the second green and third blue. Colors specified like that are called RGB colors.

# For example red in RGB model is (255,0,0) and dark green is (0, 100, 0)
# 0 means total lack of corresponding color component 
# and 255 means full amount of corresponding color component.

width = 256
height = 256

setup(width, height)

# draw red and green diagonals
i = 0
while i < width-3:
    
    set_pixel(i,   i, (255,0,0))
    set_pixel(i+1, i, (255,0,0))
    set_pixel(i+2, i, (255,0,0))
        
    set_pixel(width-i-1, i, (0,100,0))
    set_pixel(width-i-2, i, (0,100,0))
    set_pixel(width-i-3, i, (0,100,0))
        
    i += 1


show()