'''
Turtle starter code
ATLS 1300/5650
Author: Dr. Z

Author: YOUR NAME
DATE

This is a description of what this code does. You should edit this line to get full credit on assignments.
The code will CONTINUE TO RUN (meaning you cannot run it again) when you close the window!
'''

import turtle, math # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#====================================================== Your code ======================================================

test = turtle.Turtle()
test.speed(0)

# for i in range(100):
#     test.forward(200)
#     test.left(91)

amp = 100
# for i in range(3000):
#     i = math.radians(i)
#     y = amp * math.sin(i)
#     test.goto(i,y)

# for i in range(100):
#     test.goto(i,0)

#drawing on y-axis
# for i in range(400):
#     i = math.radians(i)
#     #x = amp * math.sin(i*10)
#     y = amp * math.cos(i*10)
#     test.goto(i*50,y)

amp = 100 #Amplitude
for i in range(300):
    i = math.radians(i)
    y = amp * math.cos(i*10)
    test.goto(i*50,y)



#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!
