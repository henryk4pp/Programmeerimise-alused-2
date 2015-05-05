from pixboard import *
from math import sin

# You can compute color components dynamically.
# In this example the red component depends on x coordinate,
# green depends on y coordinate and blue depends on sine of x.

width = 256
height = 256

setup(width, height)

x = 0
while x < width:
    
    y = 0
    while y < height:
        red = x
        green = y
        blue = int((sin(x/12) + 1) * 127)
        set_pixel(x, y, (red, green, blue))
        
        y += 1
        
    x += 1


show()