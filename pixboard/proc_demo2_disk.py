from pixboard import *
from math import sqrt


# Task: draw a disk at the center of picture

def distance(x1,y1, x2,y2):
    return sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

width = 600
height = 400

center_x = width // 2
center_y = height // 2
radius = 100

setup(width, height)

# "visit" all pixels on the image
x = 0
while x < width:
    
    y = 0
    while y < height:
        
        # if the pixel is close enough to the center, then paint it red
        if distance(x, y, center_x, center_y) <= radius:
            set_pixel(x, y, "red")
                        
        y += 1
    x += 1


show()