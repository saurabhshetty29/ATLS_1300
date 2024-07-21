
"""Voronoi example using turtle. 
Difficulty level: 4

Voronoi cells are made by partitioning a 2D area into regions close
to a set of points. The cell partitinos are made by finding all th epoints in the
plane that are closer to one point than any other.

This code is modified from https://www.generativehut.com/post/robots-and-generative-art-and-python-oh-my

Dr. Z 
August 1, 2022
"""
import turtle
from scipy.spatial import Voronoi
import numpy as np
import random

win = turtle.Screen() 
w = 600
h = 600
win.setup(width=w, height=h)
turtle.tracer(0)      # turn off turtle animation

PALETTE = ["#F3DAD8","#D0FCB3","#92DCE5","#F18F01","#235789","#DCEDFF"]
# misty rrose, tea green, middle blue, carrot oranged, bdazzled blue

def dot():
    """Creats "agents" to do your tasks. 
    Agents are circles that don't draw.
    Output from function can be saved to a name."""
    dot =turtle.Turtle("circle")
    dot.shapesize(.1)
    dot.up()
    return dot

# place the dots in randome places around the screen
seed = [] # empty list

for i in range(200):
    # make a random coordinate
    pts = [random.randint(-w*2/3,w*2/3),random.randint(-h*2/3,h*2/3)]

    #add it to a list
    seed.append(pts)


# turn the list into a numpy array (overwrites pts)
pts = np.array(seed)

turtle.update() #update the animation, so you can see the dots appear

# Voronoi cell biz
vor = Voronoi(pts)
verts = vor.vertices
shapes_ind = vor.regions

# remove empty shapes
shapes_ind = [s+s[0:1] for s in shapes_ind if len(s)>0 and -1 not in s]
shapes = [verts[s] for s in shapes_ind] # get vertices of filtered shapes

# A turtle to draw
VorDraw = dot()
VorDraw.pensize(3)

for shape in shapes:
    VorDraw.color("gray20",random.choice(PALETTE))
    VorDraw.begin_fill()
    for vert in shape:
        VorDraw.goto(vert)
        VorDraw.down() # draw
    VorDraw.end_fill()
    turtle.update()
    VorDraw.up()

turtle.done()