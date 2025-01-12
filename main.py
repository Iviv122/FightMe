import time
import board
import displayio

from blinka_displayio_pygamedisplay import PyGameDisplay 

display = PyGameDisplay(width=128, height=128) 
bitmap = displayio.Bitmap(display.width, display.height, 3)

palette = displayio.Palette(3)
palette[0] = 0x000000  # Black
palette[1] = 0xffffff  # White

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

group = displayio.Group()
group.append(tile_grid)

display.root_group = group

for x in range(60, 67):  # Create a small square
    for y in range(60, 67):
        bitmap[x, y] = 1

while True:
    pass
