##CODE copied straight from the internet

from PIL import Image, ImageDraw
from math import log, log2

#MANDELBROT
MAX_ITER = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER
    
    return n + 1 - log(log2(abs(z)))


# Image size (pixels)
WIDTH = 6000
HEIGHT = 4000

# Plot window
RE_START = -1.27
RE_END = -1.24 
IM_START = 0.37
IM_END = 0.39

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
#im = Image.open('output.png')
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        hue = int(255 * m / MAX_ITER)
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        # Plot the point
        draw.point([x, y], (hue, saturation, value))
'''
for i in range(WIDTH):
    x1 = ((0.37 - IM_START)/(IM_END - IM_START))*HEIGHT
    x2 = ((0.39 - IM_START)/(IM_END - IM_START))*HEIGHT
    draw.point([i,x1],(0,0,255))
    draw.point([i,x2],(0,0,255))

for j in range(HEIGHT):
    x1 = ((-1.27 - RE_START)/(RE_END - RE_START))*WIDTH
    x2 = ((-1.24 - RE_START)/(RE_END - RE_START))*WIDTH
    draw.point([x1,j],(0,0,255))
    draw.point([x2,j],(0,0,255))
'''
im.convert('RGB').save('output.png', 'PNG')