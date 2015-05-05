from pixboard import *

# setup takes the dimensions (width, height) of image (in pixels)
setup(600,400)

# set_pixel takes x-coordinate, y-coordinate and color
# left-upper pixel is 0,0
# right-bottom pixel (in this case) 599, 399

set_pixel(300, 200, "blue")
set_pixel(300, 201, "blue")
set_pixel(301, 200, "blue")
set_pixel(301, 201, "blue")

# show() shows the i
show()