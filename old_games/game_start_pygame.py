import pygame, random
pygame.init()

w = 400
h = 400
win = pygame.display.set_mode((w, h))

class Button():
  def __init__(self):
    
    # make a rectangle Surface & add to window
    self.w = 100
    self.h = 50
    self.x = w/2
    self.y = h/2-self.h/2
    self.box = pygame.Rect(self.x,self.y,self.w,self.h)  # store loc for pygame

    # drawing button face
    self.face = pygame.Surface((self.w,self.h)) 
    self.face.fill(pygame.Color("white")) # white becomes color

    # button text
    self.text = "Click"
    self.fontSize = 20

    self.writeText(self.text) # write text upon instantiation
#   adding text
  def writeText(self,text):
    '''writes text to a surface. text should be string.'''
    font = pygame.font.SysFont("Arial", self.fontSize, bold=True) # arguments: (fontName, size, bold=False, italic=False)
    text = font.render(self.text, 1, pygame.Color("Black")) #overwrite text input to turn it into blit-able content
    self.face.blit(text, (0, 0)) # add text to button Face
  
  def click(self,event):
      '''Controls click interaction for a surface. To be called in event for loop.
      event - pygame event (from for loop)
      surface - pygame surface to draw on (win, buttonFace, etc.)'''
      if event.type == pygame.MOUSEBUTTONDOWN :
          x, y = pygame.mouse.get_pos() # so it doesn't get multiple points (faster code)
          if pygame.mouse.get_pressed()[0]:
              if self.box.collidepoint(x, y):
                  print('Click in box')
                  self.face.fill((255,0,0))
                  self.writeText("clicked")
    
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
  button1 = Button()
  button2 = Button()
  
  while running:
      win.fill((0,0,0))
      # uncomment for animation
      # button.x += random.randint(-2,2)
      for event in pygame.event.get():
          if (event.type == pygame.QUIT):
              pygame.quit()
          button1.click(event)
          button1.key(event)
          button2.click(event)
          button2.key(event)
      button1.show()
      button2.show()
      pygame.display.update()


# call func to run game
main()