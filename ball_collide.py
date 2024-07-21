import pygame, random
pygame.init()

#window
w = 750
h = 750
win = pygame.display.set_mode((w, h))

class Ball:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rad = 50
        self.color = (24,120,233)
        self.draw = True

        self.show()
    
    def show(self):
        if self.draw:
            self.box = pygame.draw.circle(win,self.color,(self.x,self.y),self.rad)

    def move(self):
        dx = random.randint(-5,5)
        dy = random.randint(-5,5)
        self.x += dx
        self.y += dy

        if self.x < 0 or self.x > 750:
            self.x = w/2
        if self.y < 0 or self.y > 750:
            self.y = h/2

        self.show()

    def collide(self,rect):
        if self.box.colliderect(rect):
            self.draw = False

running = 1

test = Ball(w/2,h/2)
test.color = (255,255,255)

ballList = []
for i in range(20):
    x = random.randint(0,w)
    y = random.randint(0,h)
    ballList.append(Ball(x,y))

while running:
    win.fill((0,0,0))
    test.show()

    for ball in ballList:
        ball.move()
    
    for ball in ballList:
        ball.collide(test.box)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()
