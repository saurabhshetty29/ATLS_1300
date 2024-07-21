'''
Turtle starter code
ATLS 1300/5650
Author: Dr. Z

Author: YOUR NAME
DATE

This is a description of what this code does. You should edit this line to get full credit on assignments.
The code will CONTINUE TO RUN (meaning you cannot run it again) when you close the window!
'''

import turtle, random # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!
win.bgcolor("paleturquoise3")
#====================================================== Your code ======================================================
circ = turtle.Turtle()
circ.stamp()
circ.goto(350,350)
circ.home()
circ.color("dodgerblue3")
circ.up()
circ.goto(250, 200)
circ.down()
circ.begin_fill()
circ.circle(40)
circ.end_fill()
circ.ht()
print(circ.xcor())

turt = turtle.Turtle(shape="turtle")
turt.color("green4","lightgreen")
turt.up()
turt.shapesize(4)
turt.shapesize(outline=4)
turt.goto(200, 200)
#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!
