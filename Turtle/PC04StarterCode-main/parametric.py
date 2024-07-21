#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle, math, random
turtle.colormode(255)

######LOOP########
swaggyPen = turtle.Turtle()
swaggyPen.speed(0)
swaggyPen.hideturtle()
swaggyPen.pensize(2)

for i in range (10):
    x = 2 * math.cos(i)
    y = 2 * math.sin(i)
    swaggyPen.goto(i * x, i * y)
    rando = random.randint(1,4)
    if rando == 1:
        swaggyPen.pencolor(166, 99, 204)
    elif rando == 2:
        swaggyPen.pencolor(178, 152, 220)
    elif rando == 3:
        swaggyPen.pencolor(184, 208, 235)
    else:
        swaggyPen.pencolor(185, 250, 248)
######LOOP########

#I repeat this exact loop 4 more times, but change the value I multiply with...

######LOOPS########
# swaggyPen2 = turtle.Turtle()
# swaggyPen2.speed(0)
# swaggyPen2.hideturtle()
# swaggyPen2.pensize(2)
# swaggyPen2.pensize(2)

# for i in range (151):
#     x = -2 * math.cos(i)
#     y = 2 * math.sin(i)
#     swaggyPen2.goto(i * x, i * y)
#     rando = random.randint(1,4)
#         if rando == 1:
#             swaggyPen2.pencolor(166, 99, 204)
#         elif rando == 2:
#             swaggyPen2.pencolor(178, 152, 220)
#         elif rando == 3:
#             swaggyPen2.pencolor(184, 208, 235)
#         else:
#             swaggyPen2.pencolor(185, 250, 248)

# swaggyPen3 = turtle.Turtle()
# swaggyPen3.speed(0)
# swaggyPen3.hideturtle()
# swaggyPen3.pensize(2)

# for i in range (151):
# x = -2 * math.cos(i)
# y = -2 * math.sin(i)
# swaggyPen3.goto(i * x, i * y)
# rando = random.randint(1,4)
# if rando == 1:
# swaggyPen3.pencolor(166, 99, 204)
# elif rando == 2:
# swaggyPen3.pencolor(178, 152, 220)
# elif rando == 3:
# swaggyPen3.pencolor(184, 208, 235)
# else:
# swaggyPen3.pencolor(185, 250, 248)

# swaggyPen4 = turtle.Turtle()
# swaggyPen4.speed(0)
# swaggyPen4.hideturtle()
# swaggyPen4.pensize(2)

# for i in range (151):
# x = 2 * math.cos(i)
# y = -2 * math.sin(i)
# swaggyPen4.goto(i * x, i * y)
# rando = random.randint(1,4)
# if rando == 1:
# swaggyPen4.pencolor(166, 99, 204)
# elif rando == 2:
# swaggyPen4.pencolor(178, 152, 220)
# elif rando == 3:
# swaggyPen4.pencolor(184, 208, 235)
# else:
# swaggyPen4.pencolor(185, 250, 248)
######LOOPS########
turtle.done()