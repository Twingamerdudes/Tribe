from simulation import *
#Handles houses
class House:
  #Initlaztion shit
  def __init__(self):
      self.x = random.randint(0, SCREEN_WIDTH)
      self.y = random.randint(0, SCREEN_HEIGHT)
      self.color = (139, 69, 19)
      self.foodCount = 5
      self.tribe = None
      self.owner = None
  #Draws the house
  def draw(self, screen):
      if self.tribe != None:
          self.color = self.tribe.color
      else:
          self.color = (139, 69, 19)
      pygame.draw.rect(screen, self.color, (self.x, self.y, 30, 30))

      #Food count
      text = font.render(str(self.foodCount), True, (255, 255, 255))
      screen.blit(text, (self.x + 10 / len(str(self.foodCount)), self.y + 6))
  
  def update(self):
    #Destroy the house if it has no food
    self.tribe = self.owner.tribe
    if self.foodCount <= 0:
      houseList.remove(self)
      self.owner.hasHouse = False
      self.owner.house = None
      self.owner.houseCooldown = 0
