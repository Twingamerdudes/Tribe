from simulation import *
#Resource classes, used to store the location of food, water, and wood. Also used to draw the resources.
class Food:
  def __init__(self):
    self.x = random.randint(0, SCREEN_WIDTH)
    self.y = random.randint(0, SCREEN_HEIGHT)
    self.color = (255, 0, 0)
  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), 5)
class Water:
  def __init__(self):
    self.x = random.randint(0, SCREEN_WIDTH)
    self.y = random.randint(0, SCREEN_HEIGHT)
    self.color = (0, 0, 255)
  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), 5)
class Wood:
  def __init__(self):
    self.x = random.randint(0, SCREEN_WIDTH)
    self.y = random.randint(0, SCREEN_HEIGHT)
    self.color = (129, 59, 9)
  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), 5)