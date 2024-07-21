import pygame, sys
from pygame.locals import *
pygame.init()

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # define window variable
pygame.display.set_caption('Click!')

#== Variables & functions 
WHITE = (255,255,255) # some handy RGB values
BLACK = (0,0,0)


#== Animation loop 
# start values defined here
running = True
clock = pygame.time.Clock() # for framerate timing


while running:
    for event in pygame.event.get():
      # checks for all events: window, key, mouse
        if event.type == QUIT:
            #pygame.quit()
            running = False
          
        if event.type == pygame.KEYDOWN:
            # handles keys
            if event.key == K_SPACE:
                print('space bar has free drink')
              
        if event.type == pygame.MOUSEBUTTONDOWN:      
            # handles mouse
            if event.button == 1:
                print('left mouse click')
            if event.button == 2:
                print('right mouse click') # won't work with Mac trackpads!

# Useful link: https://www.geeksforgeeks.org/pygame-input-handling/