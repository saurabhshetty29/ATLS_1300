"""
Animates a bobbing circle (that wraps around the screen)
"""

import turtle, math
# turtle.tracer(0)

# creat a window
win = turtle.Screen()
w = 600
h = 600
win.setup(width=w, height=h)

# variable definition
circle = turtle.Turtle(shape="circle")
running = True # control animation loop

# start coordinates & conditions
step = 5 # step size for bobbing animation, in pixels
angle = 0 # start value for sine angle
edge = -win.window_width()/2
x = edge/2 # start value for x

# setup
win.bgcolor((0,0,0)) # black background
circle.color("white")
circle.up()
circle.goto(x,0) # start on left side of screen

# animation loop
while running:
    # move turtle forward incrementally
    circle.forward(step)

    # update values and screen
    turtle.update()
    
    # stop conditiono
    if (circle.xcor()>edge):
        # crosses right window, stop animation
        running = False
        
print("animation complete!")
turtle.done()