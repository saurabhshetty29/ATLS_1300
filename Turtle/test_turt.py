import turtle # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win =turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

'''
Description

A randomized, overwhelming, abstract piece utilizing tens of circles and squares and a central sine wave.
Square colors either RGB or CMY depending on whether they begin on the left or right side of the screen,
and circle colors are chosen from three color palettes depending on whether they begin on the bottom or top side of the screen.
The period, amplitude, and stroke size of the sine wave is also randomized to make the central, grounding element of the piece be slightly unexpected in itself.
The piece is chaotic and very colorful, but the constant black/white and position of the central sine wave cut through the chaos and evoke a calming wave.
Even in all the chaos and overwhelm, a slow flowing river calms the viewer. 

'''
#====================================================== Your code ======================================================

import random
import math

#colors and palettes
#from coolors.co
black=(0,0,0)
purple=(61,38,69)
violet=(131,33,97)
pink=(218,65,103)
white=(240,239,244)

yellish=(241,255,231)
lightgreen=(169,253,172)
green=(68,207,108)
turq=(50,162,135)
brown=(108,70,78)

blue=(102,153,204)
yellow=(255,242,117)
orange=(255,140,66)
red=(255,60,56)
maroon=(162,62,72)

bottom=(black,purple,violet,pink,white)
top=(yellish,lightgreen,green,turq,brown)
mid=(blue,yellow,orange,red,maroon)

all=(black,purple,violet,pink,white,yellish,lightgreen,green,turq,brown,blue,yellow,orange,red,maroon)

bgr=random.choice(all)
turtle.bgcolor(bgr)

#circles
cir=turtle.Turtle()
range: 100
cir.pensize(0)
cir.speed(50)

for i in range(100):
    coorx=random.randint(-350,350)
    coory=random.randint(-350,350)

    #color palettes change based on whether they're in the top, middle, or bottom of the image
    if -350<=coory<=-100:
        cir.up()
        cir.goto(coorx,coory)
        circol=random.choice(bottom)
        #circles sharing the background color will be small and unfilled, circles not sharing the background color will be filled
        if circol==bgr:
            cir.pencolor(circol)
            cir.pensize(5)
            cir.down()
            cir.circle(random.randint(5,15))
            cir.up()
        else:
            cir.begin_fill()
            cir.fillcolor(circol)
            cir.circle(random.randint(1,100))
            cir.end_fill()
    elif 100<=coory<=350:
        cir.up()
        cir.goto(coorx,coory)
        circol=random.choice(top)
        if circol==bgr:
            cir.pencolor(circol)
            cir.pensize(5)
            cir.down()
            cir.circle(random.randint(5,15))
            cir.up()
        else:
            cir.begin_fill()
            cir.fillcolor(circol)
            cir.circle(random.randint(1,100))
            cir.end_fill()
    else:
        cir.up()
        cir.goto(coorx,coory)
        circol=random.choice(mid)
        if circol==bgr:
            cir.pencolor(circol)
            cir.pensize(5)
            cir.down()
            cir.circle(random.randint(5,15))
            cir.up()
        else:
            cir.begin_fill()
            cir.fillcolor(circol)
            cir.circle(random.randint(1,100))
            cir.end_fill()

#cursor begone
cir.goto(1000,1000)


sin=turtle.Turtle()
sin.speed(10000)
sin.pensize(random.randint(5,50))
sin.pencolor((255,255,255))

period=random.randint(1,5)
amp=random.randint(50,350)

#modified from https://www.geeksforgeeks.org/draw-a-sine-wave-using-turtle-in-python/
for x in range (350):
    y = math.sin(math.radians(period*x))
    sin.goto(-x,amp*-y)
sin.up()
sin.goto(0,0)
sin.down()
for x in range (350):
    y = math.sin(math.radians(period*x))
    sin.goto(x,amp*y)

#squares
r=(255,0,0)
g=(0,255,0)
b=(0,0,255)
rgb=(r,g,b)

c=(0,255,255)
m=(255,0,255)
y=(255,255,0)
cmy=(c,m,y)

sqr=turtle.Turtle()



for i in range(50):
    xcoor=random.randint(-350,350)
    ycoor=random.randint(-350,350)
    sqr.up()
    sqr.goto(xcoor,ycoor)
    sqr.pensize(random.randint(4,10))
    sqr.speed(50)
    #squares on the left side of the screen will be red, green, or blue and smaller
    #squares on the right side will be cyan, magenta, or yellow and larger
    if -350<xcoor<0:
        sqr.down()
        sqr.pencolor(random.choice(rgb))
        l=random.randint(15,79)
        sqr.forward(l)
        sqr.right(90)
        sqr.forward(l)
        sqr.right(90)
        sqr.forward(l)
        sqr.right(90)
        sqr.forward(l)
    else:
        sqr.down()
        sqr.pencolor(random.choice(cmy))
        l=random.randint(80,150)
        sqr.forward(l)
        sqr.right(90)
        sqr.forward(l)
        sqr.right(90)
        sqr.forward(l)
        sqr.right(90)
        sqr.forward(l)

#cursor begone
sqr.up()
sqr.goto(1000,1000)

sin.pensize(3)
sin.pencolor(0,0,0)
sin.up()
sin.goto(0,0)

#modified from https://www.geeksforgeeks.org/draw-a-sine-wave-using-turtle-in-python/
sin.down()
for x in range (350):
    y = math.sin(math.radians(period*x))
    sin.pencolor(0,0,0)
    sin.goto(-x,amp*-y)
sin.up()
sin.goto(0,0)
sin.down()
for x in range (350):
    y = math.sin(math.radians(period*x))
    sin.goto(x,amp*y)


#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!