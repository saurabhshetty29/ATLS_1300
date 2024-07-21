"""
Animating white circle across black screen
"""
 
import pygame, math, random
pygame.init()
 
# create a window
w = 300
h = 400
win = pygame.display.set_mode((w,h)) # set window to size (w x h)
 
# set up clock for animation
clock = pygame.time.Clock() #animation control
 
def wraparound(x,w):
    if x > w:
        x = 0 # send circle to the start x position
    return x
 
# creates points on a circle path
# oslce x, y along circle, set radius
def loop():
    rad = 50
    for t in range(360):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
 
        angle = math.radians(t) # convert to radians
        X = rad * math.sin(angle)
        Y = rad * math.cos(angle)
        pygame.draw.circle(win, (255,255,255), (X+w/2,Y+h/2),rad, 0) # drawing white filled circle at (0, h/2)
        pygame.display.update() # draws everything to window
        clock.tick(30)
def rainbowCircles(win):
    #randomize colors
    c1, c2, c3 = random.randint(1,255), random.randint(1,255), random.randint(1,255)
    pygame.draw.circle(win,(c1,c2,c3),(200,200),8,0)
    pygame.draw.circle(win,(c1,c2,c3),(400,200),8,0)
def bounce():
    X = 0
    Y = 600
    for square in range(360):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        X += 1
        if X < 300:
            Y -= 1
        elif X >= 300:
            Y+= 1
        pygame.draw.rect(win, (150,200,250), 50, 10,0)
        pygame.display.update() # draws everything to window
        clock.tick(30)
# start coordinates & conditions
step = 5 # step size for bobbing animation, in pixels
angle = 0 # start value for the angle
 
cross = 0 # start value for a counter
running = True #control animation loop
x, y = 0,h/2
 
face = pygame.image.load("face6.gif")  # code from https://www.askpython.com/python-modules/pygame-looping-background#:~:text=To%20add%20the%20background%20image,fills%20up%20the%20whole%20screen.

while running:
    win.blit(face,(0,0)) # code from https://www.askpython.com/python-modules/pygame-looping-background#:~:text=To%20add%20the%20background%20image,fills%20up%20the%20whole%20screen.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
 
    # draw task
 
    pygame.draw.circle(win, (255,255,255), (x,y),50, 0) # drawing white filled circle at (0, h/2)
    # circle arguments - surface, color, center(x,y), radius, filled/line
    x += step
    # same as x = x + step
 
 
    # call the function
    x = wraparound(x,w)
    if x == 0:  
        cross += 1
    elif x == w/2:
        # move in circle when center is hit
        loop()
 
    # stop task
    if cross == 10:
        # stops animation when circle crosses 10 times
     running = False
 
    pygame.display.update() # draws everything to window
    clock.tick(30)