import pygame, random
pygame.init()

w = 400
h = 400
win = pygame.display.set_mode((w, h))

class Button():
  def __init__(self,x,y,w=50,h=50,faceColor="white",centered=True,text="Click"):
    
    # make a rectangle Surface & add to window
    self.w = w
    self.h = h
    self.x = x 
    if centered:
      self.y = y-self.h/2 # places x and y at centerof shape
    else:
      self.y = y
    self.box = pygame.Rect(self.x,self.y,self.w,self.h)  # store loc for pygame

    # drawing button face
    self.face = pygame.Surface((self.w,self.h)) 
    self.face.fill(pygame.Color(faceColor)) # white becomes color

    # button text
    self.text = "Click"
    self.fontSize = 20

    # setup methods
    self.writeText() # write text upon instantiation
    
#   adding text
  def writeText(self):
    '''writes text to a surface. text should be string.'''
    font = pygame.font.SysFont("Arial", self.fontSize, bold=True) # arguments: (fontName, size, bold=False, italic=False)
    text = font.render(self.text, 1, pygame.Color("Black")) #overwrite text input to turn it into blit-able content
    self.face.blit(text, (0, 0)) # add text to button Face
  
  def click(self,event,color=(255,0,0)):
      '''Controls click interaction for a surface. To be called in event for loop.
      event - pygame event (from for loop)
      surface - pygame surface to draw on (win, buttonFace, etc.)'''
      if event.type == pygame.MOUSEBUTTONDOWN :
          x, y = pygame.mouse.get_pos() # so it doesn't get multiple points (faster code)
          if pygame.mouse.get_pressed()[0]:
              if self.box.collidepoint(x, y):
                  print('Click in box')
                  self.face.fill(color) # change color
                  self.text="clicked" # change text
                  self.writeText() # update text
    
  def key(self, event):
      '''Controls key interaction for a surface. To be called in event for loop.
            event - pygame event (from for loop)
            surface - pygame surface to draw on (win, buttonFace, etc.)'''
      if (event.type == pygame.KEYDOWN):
          if (event.key == pygame.K_LEFT):
            # left arrow box to left
              if (self.x > self.w): # within left edge
                self.x -= 5
              print('left key press')
          if (event.key == pygame.K_RIGHT):
              if (self.x < w-self.w): # within right edge
                self.x += 5
              print('right key press')
                
  def show(self):
    '''Draw the button onto the window.'''
    win.blit(self.face, (self.x, self.y))

def main():
    running = True
    button = Button(w/2,h/2,w=100)
    button2 = Button(w/2,50,w=100,faceColor="Blue")
    
    while running:
        win.fill((0,0,0))
        # uncomment for animation
        # button.x += random.randint(-2,2)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            button.click(event)
            button.key(event)
        button.show()
        button2.show()
    
        pygame.display.update()

if __name__ == '__main__':
  # executes when run from script, but noto imported
  # now your code can be treated like a library!
  main()