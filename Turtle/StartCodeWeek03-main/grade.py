import turtle,random

turtle.colormode(255)
turtle.tracer(0)
turtle.hideturtle()

GlossyGrape = (165, 153, 181)

win=turtle.Screen()
w=700
h=700
win.setup(width=w, height=h)
win.bgcolor(GlossyGrape)

RossoCorsa= (208, 0, 0)
PalatinatePurple = (90, 11, 77)
SapphireBlue = (0, 100, 148)
Xiketic = (19, 3, 3)

color1 = random.choice((RossoCorsa,PalatinatePurple,SapphireBlue,Xiketic))
color2 = random.choice((RossoCorsa,PalatinatePurple,SapphireBlue,Xiketic))
color3 = random.choice((RossoCorsa,PalatinatePurple,SapphireBlue,Xiketic))
color4 = random.choice((RossoCorsa,PalatinatePurple,SapphireBlue,Xiketic))
color5 = random.choice((RossoCorsa,PalatinatePurple,SapphireBlue,Xiketic))

hexagon=triangle=square=circle=turtle.Turtle()


for i in range(125):
    circle.up()
    circle.goto(random.choice((-280,-210,-140,-70,0,70,140,210,280)),random.choice((-280,-210,-140,-70,0,70,140,210,280)))
    circle.pd()
    if circle.xcor()>0 and circle.ycor()>0: #draws a triangle in quadrant 1
        triangle.pensize(3)
        triangle.color(color1)
        for x in range(3):
            triangle.forward(75)
            triangle.left(120)
    if circle.xcor()<0 and circle.ycor()>0: #draws a random sized circle in quadrant 2
        circle.pensize(5)
        circle.color(color2)
        circle.circle(random.randint(5,50))
    elif circle.xcor()<0 and circle.ycor()<0: #draws a square in quadrant 3
        square.pensize(3)
        square.color(color3)
        for z in range(4):
            square.forward(50)
            square.right(90)
        if circle.xcor()<0 and -175>=circle.ycor(): #draws a tilted square in the lower part of quadrant 3
            square.pensize(4)
            square.color(color4)
            square.left(45)
            for j in range(4):
                square.forward(50)
                square.right(90)
            square.left(135)
    elif circle.xcor()>0 and circle.ycor()<0: #draws a hexagon in quadrant 4
        hexagon.pensize(5)
        hexagon.color(color5)
        for y in range(5):
            hexagon.forward(50)
            hexagon.right(72)

turtle.done()