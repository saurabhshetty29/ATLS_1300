import pygame
pygame.init()

#create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()
x = 0
y = h/2
shift = 5
running = 1
white = (255,255,255)

while running:
    win.fill((0,0,0))
    pygame.draw.circle(win,white,(x,y),60,0)

    x += shift

    if x > w:
        x -= shift
        running = 0

    pygame.display.update()
    clock.tick(30)
    #running = 0