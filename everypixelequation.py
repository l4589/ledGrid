
import board
import neopixel
import time
npix=16*16
# even: y=16r-c, odd: y=16r-17+c

# even: y=16x-2, odd: y=16x-15
pixels = neopixel.NeoPixel(board.GP0, npix)
pixels[1] = (10,0,0)
pixels[30] = (0,10,0)
pixels[33] = (0,0,10)
pixels[62] = (10,0,0)
pixels[65] = (0,10,0)
pixels[94] = (0,0,10)
pixels[97] = (10,0,0)
pixels[126] = (0,10,0)
# even: y=16x-3, odd: y=16x-14
pixels[2] = (0,10,0)
pixels[29] = (0,0,10)
pixels[34] = (10,0,0)
pixels[61] = (0,10,0)
pixels[66] = (0,0,10)
pixels[93] = (10,0,0)
pixels[98] = (0,10,0)
pixels[125] = (0,0,10)

pixels[5+10+11+11+10+11+11] = (10,0,0)


def pix(r,c,col= (10,0,0)):
    if (r %2)==0:
        y=16*r-c
    else:
        y=16*r-17+c
    pixels[y] = col
pix(4,7)
pix(10,3,(0,10,0))
pix(4,8)
pix(5,9)
pix(6,7)
pix(6,8)
pix(5,6)
