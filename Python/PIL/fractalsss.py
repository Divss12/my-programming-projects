from PIL import Image, ImageDraw
from math import sin, cos, sqrt,pi, tan
import random

def isPrime(x):
    if x < 1:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    for i in range(2,int(x**0.5)):
        if x%i == 0:
            return False
    return True

width = 1440
height = 720

w = width/(5*pi)
h = height/4
acc = 100

im = Image.new('HSV',(width,height),(255,255,255))
draw = ImageDraw.Draw(im)

for x in range(width):
    for y in range(height):
        hue = 0
        sat = 255
        val = 255 if int((y/(-h) + 2)*acc) == int(sin(x/w*acc)) else 0
        draw.point([x,y],(hue,sat,val))

im.convert('RGB').save('test6.png', 'PNG')