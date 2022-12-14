import board
import neopixel
import time
npix=16*16
# even: y=16r-c, odd: y=16r-17+c
# even: y=16x-2, odd: y=16x-15
pixels = neopixel.NeoPixel(board.GP0, npix)

def pix(r,c,col= (10,0,0)):
    if (r %2)==0:
        y=16*r-c
    else:
        y=16*r-17+c
    pixels[y] = col
    
#pix(1,1)    #bottom corner pixel
    
    
r= (100,0,0) #red 
b= (0,0,100) #blue
g= (0,100,0) #green
p= (50,0,50) #purple
y= (50,50,0) #yellow
o= (70,30,0) #orange
w= (33,33,33) #white
pi= (80,20,20) #pink
t= (0,70,30) #teal



grid= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [r,0,r,0,g,g,g,0,b,0,b,0,o,o,o,p],
       [r,0,r,0,g,0,0,0,b,0,b,0,o,0,o,p],
       [r,0,r,0,g,0,0,0,b,0,b,0,o,0,o,p],
       [r,r,r,0,g,g,g,0,b,0,b,0,o,0,o,p],
       [r,0,r,0,g,0,0,0,b,0,b,0,o,0,o,p],
       [r,0,r,0,g,0,0,0,b,0,b,0,o,0,o,0],
       [r,0,r,0,g,g,g,0,b,b,b,b,o,o,o,p],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

for i in range (1,17):
    for j in range (16,0,-1):
        if (grid[15-i][j-1])!=0:
            pix(i,j,grid[15-i][j-1])