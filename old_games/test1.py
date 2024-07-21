import pygame
pygame.init()

#create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

running = 1
white = (255,255,255)

while running:
    pygame.draw.circle(win,white,(0,h/2),60,0)
    pygame.display.update()
    clock.tick(10)
    #running = 0