import pygame
import random, time
pygame.init()

# globals
w = 600
h = 600
win = pygame.display.set_mode((w,h))
pygame.display.set_caption("Click Game")

# set colors
start_bg = (249, 233, 236) # lavendar blush
end_bg = (29, 47, 111) # st patricks blue
press_btn = (248, 141, 173) # darker pink
start_btn = (250, 199, 72)

win.fill(start_bg) # set background color as light

class Timer:
    def __init__(self,limit=60):
        self.limit = limit
        self.clock = pygame.time.Clock()
        self.start=pygame.time.get_ticks() #starter tick
        
        self.timeLeft = self.countDown()
        
    def countDown(self):
        currTime=(self.start + pygame.time.get_ticks())/1000 #calculate how many seconds
        return int(self.limit - currTime) # rturns whole second numbers

class Bubble:
    def __init__(self, startPos=(0,0),size=30, color=(0,255,255)):
        self.x,self.y=startPos
        self.size=size
        self.fillColor=color 
        self.lineColor = (27, 64, 121)
        self.area=[] #STORE CIRCLE LOC
        
    def forward(self,step):
        self.x += step
        self.y += step
        
    def rw(self,step=5):
        self.x+=random.randint(-step,step)
        self.y+=random.randint(-step,step)
        
        # make outlined circle by drawing 2 circles on top of each other
        pygame.draw.circle(win,self.lineColor,(self.x,self.y),self.size+2)
        self.area=pygame.draw.circle(win,self.fillColor,(self.x,self.y),self.size)
    
    def checkClick(self):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                # check for left mouse button
                if self.area.collidepoint(x, y):
                    # check if click is inside & hide circle
                    self.size = -2 # stop drawing circle
                    
    def checkMouse(self):
        # BROKEN
        if event.type == pygame.KEYDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.area.collidepoint(x, y):
                    self.size = -2 # stop drawing circle (for both outline & fill circles)                 

def checkWin(bubList):
    """Checks to see if all the bubbles are invisible.
    Arguments:
        bubList - a list of Bubble objects
    Returns a boolean to use to control the loop."""
    global text
    for bub in bubList:
        if bub.size > 0:
            # check if any circle has a radius (drawing is on)
            # stop checking sizes by returning a value (exits function)
            return True
    else:
        text = "You Win!"
        return False #set win variable to the output
            
bubList = []
timer = Timer()
timeLeft = 30 # amount of time in seconds to play the game
text = "Game Over!"
running = True

# make a list of bubbles
for i in range(5):
     bubList.append(Bubble([random.randint(0,w-20),random.randint(0,h-20)])) # place at a random location

while timeLeft > 0 and running:
    running = checkWin(bubList)
    win.fill(start_bg)
    timeLeft = timer.countDown()

    # animate bubble movement
    for bub in bubList:
        bub.rw()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # stops animation

        for bub in bubList:
            bub.checkClick()

        # Haven't worrked out key interaction yet
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         bub.checkClick()
       
    pygame.display.update()
    timer.clock.tick(30)
         
print(text) 