#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:32:51 2021

@author: sazamore

Math art

"""
import turtle, math

#equations from https://www.flerlagetwins.com/2017/11/beyond-me-part-3-parametric-equations_45.html?showComment=1562434668701&m=1
#  t : -8 to 8
# x = 6*SIN(13.58*[t])*ROUND(SQRT(COS(COS(7.4*[t]))),0)
# y = 6*POWER(COS(13.58*[t]),4)*SIN(SIN(7.4*[t]))
turtle.tracer(0)

pen = turtle.Turtle(visible=False)
s = pen.getscreen()
s.bgcolor("blue3")
pen.color("cyan4")
pen.pensize(6)
pen.up()

t=-8
x = 6 * math.sin(13.58*t) * round(math.sqrt(math.cos(math.cos(7.4*t))),0)
y = 6*math.cos(13.58*t)**4 * math.sin(math.sin(7.4*t))
pen.goto(x,y) # go to start position
pen.down()

for t in range(-4000,4000):
    t = t/500. # cheap way to get a fraction
    x = 6 * math.sin(13.58*t) * round(math.sqrt(math.cos(math.cos(7.4*t))),0)
    y = 6*math.cos(13.58*t)**4 * math.sin(math.sin(7.4*t))
    pen.goto(x*55,y*55)

pen.up()
s.update()
turtle.done()