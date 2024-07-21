"""
Animates a bobbing circle (that wraps around the screen)
"""

import pygame
pygame.init() # initialize pygame managers

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # create window

# start coordinates & conditions
running = True
x = -w/2 # start coordinates
y = h/2
step = 5
clock = pygame.time.Clock()

# do the task
win.fill((0,0,0)) # set background to black 

# create canvas that has a circle
while running:
    # move win.fill into loop
    # win.fill((0,0,0)) #fill background
    circ = pygame.draw.circle(win, (255,255,255),(x, y), 100)
    x += step # increment x poosition
    clock.tick(60)
    clock.tick(60)
    pygame.display.update() # update window
    if x > w:
        running = False

# clean up
# what you need to do to clear RAM in your code.
# pygame.quit() # not necessary