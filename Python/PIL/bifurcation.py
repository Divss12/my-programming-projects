from PIL import Image, ImageDraw
import decimal

f1 = 10000
f2 = 100

decimal.getcontext().prec = 4

def bifurcation(r):
    r = decimal.Decimal(r)
    a = decimal.Decimal(0.001)
    for i in range(f1):
        a = r*a*(1-a)
    lst = []
    for j in range(f2):
        if a in lst:
            break
        else:
            lst.append(a)
            a = r*a*(1-a)
    return lst

width = 4000
height = 3000

w = width/4
h = height/3
acc = 100

im = Image.new('HSV',(width,height),(0,0,0))
draw = ImageDraw.Draw(im)

for x in range(1000,width):
    for y in bifurcation(x/w):
        draw.point([x,height-y*3000],(0,0,255))

#for i in range(3000):
#    draw.point([i,i],(0,0,255))

im.convert('RGB').save('bifurc1.png', 'PNG')