#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:14:42 2021

@author: sazamore
"""
import turtle
import random, time

turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 600
h = 600
panel.setup(width=w, height=h)
panel.title("Click Game ")

# set panel color
start_bg = (249, 233, 236) # lavendar blush
end_bg = (29, 47, 111) # st patricks blue
press_btn = (248, 141, 173) # darker pink
start_btn = (250, 199, 72)
panel.bgcolor(start_bg) # set background color as light

# def checkWin(turtList):
#     previous = False
#     for turt in turtList:
#         if turt.bubble.isvisible():
#             # if there are any visible bubbles, the game isn't over
#             previous = True
#             return True
#         else:
#             print("You win!")
#             return False
            

class Bubble:
    def __init__(self, startPos=(100,100),size=3, color='cyan'):
        self.bubble = turtle.Turtle(shape='circle')
        self.bubble.up()
        self.bubble.color('navyblue',color)
        self.bubble.shapesize(size)
        self.bubble.goto(startPos)
        
        self.bubble.onclick(self.pop)
        panel.update()
        
    def rw(self,step=15):
        self.bubble.goto(self.bubble.xcor()+random.randint(-step,step),self.bubble.ycor()+random.randint(-step,step))
        self.bubble.forward(random.choice([-step,step]))
        panel.update()
    
    def pop(self,x,y):
        self.bubble.ht()
        
class Timer:
    def __init__(self ,limit=30,pos=(-280,270)):
        self.writer = turtle.Turtle(visible=False)
        self.writer.up()
        self.writer.goto(pos)
        self.font = ("arial",24,"bold")
        self.count = limit
        self.start = time.time() # get current time
        
    def countDown(self):
        timeLeft = self.count-int(time.time()-self.start)
        self.writer.clear()
        self.writer.write(str(timeLeft), font=self.font)
        panel.update()
        return timeLeft

bubList = []
timer = Timer()
for i in range(5):
     bubList.append(Bubble([random.randint(-200,200),random.randint(-200,200)]))
timeLeft = 30
running = True

while timeLeft > 0:# or running:
    # running = checkWin(bubList)
    timeLeft =timer.countDown()
    for bub in bubList:
        bub.rw()
         
print("Game over!")

turtle.mainloop()