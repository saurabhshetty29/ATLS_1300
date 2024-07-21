
'''
Turtle starter code
ATLS 1300/5650
Author: Dr. Z

Author: YOUR NAME
DATE

This is a description of what this code does. You should edit this line to get full credit on assignments.
The code will CONTINUE TO RUN (meaning you cannot run it again) when you close the window!
'''

import turtle, random
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win =turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

win.bgcolor(0,0,255)#107, 96, 84)
#====================================================== Your code ======================================================
palette = [(146, 148, 135), (161, 176, 171),(195, 218, 195),(213, 236, 212)]
boxes = turtle.Turtle(shape="square")
boxes.up()
boxes.shapesize(2.5)

x = -250
for k in range(7):
    y = 260
    limit = 10
    size = boxes.shapesize()
    for i in range(9):
        boxes.goto(x,y)
        if boxes.ycor()<limit:
            boxes.setheading(random.randint(-30,30)) #rotate in lower half of image
        elif boxes.ycor()<-100:
            boxes.setheading(random.randint(-70,70)) #rotate in lower half of image
        else:
            boxes.setheading(0) # keep it straight
        boxes.color(random.choice(palette))
        boxes.stamp()
        y -= 65
        limit -=10
    x += 80
    boxes.shapesize(size[0]-0.25)



#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!