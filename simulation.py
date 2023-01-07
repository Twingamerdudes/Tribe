#make a simulation of humainty using pygame
import pygame
import random
import math
import sys

foodList = []
waterList = []
woodList = []
houseList = []
humanList = []
tribeList = []
tribeNames = []
font = None
header = None
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
FIGHTING_AGE = 0
FIGHTING_ENABLED = True

#Handles the entire simulation
class Simulation:
  def __init__(self, width=640, height=480, fullscreen=False, fightingAge=18, fightingEnabled=True, possibleTribeNames=["The Tribe of the Gold", "The Tribe of the Silver", "The Tribe of the Bronze", "The Tribe of the Copper", "The Tribe of the Iron", "The Tribe of the Steel", "The Tribe of the Titanium", "The Tribe of the Platinum", "The Tribe of the Silver", "The Tribe of the Gold", "The Tribe of the Diamond", "The Tribe of the Emerald", "The Tribe of the Ruby", "The Tribe of the Sapphire", "The Tribe of the Amethyst", "The Tribe of the Topaz", "The Tribe of the Opal", "The Tribe of the Pearl", "The Tribe of the Jade", "The Tribe of the Obsidian", "The Tribe of the Onyx", "The Tribe of the Quartz", "The Tribe of the Lapis", "The Tribe of the Amber", "The Tribe of the Jade", "The Tribe of the Turquoise", "The Tribe of the Garnet", "The Tribe of the Peridot", "The Tribe of the Agate", "The Tribe of the Jasper", "The Tribe of the Malachite", "The Tribe of the Moonstone", "The Tribe of the Sunstone", "The Tribe of the Ametrine", "The Tribe of the Carnelian", "The Tribe of the Citrine", "The Tribe of the Hematite", "The Tribe of the Hemimorphite", "The Tribe of the Labradorite", "The Tribe of the Moonstone", "The Tribe of the Obsidian", "The Tribe of the Onyx", "The Tribe of the Quartz", "The Tribe of the Lapis", "The Tribe of the Amber", "The Tribe of the Jade", "The Tribe of the Turquoise", "The Tribe of the Garnet", "The Tribe of the Peridot", "The Tribe of the Agate", "The Tribe of the Jasper", "The Tribe of the Malachite", "The Tribe of the Moonstone", "The Tribe of the holy 69"]):
    pygame.init()
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global FIGHTING_AGE
    global FIGHTING_ENABLED
    global tribeNames
    global font
    global header

    tribeNames = possibleTribeNames
    if fullscreen:
      SCREEN_WIDTH = pygame.display.Info().current_w
      SCREEN_HEIGHT = pygame.display.Info().current_h
    else:
      SCREEN_WIDTH = width
      SCREEN_HEIGHT = height
    self.SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    self.fullscreen = fullscreen
    font = pygame.font.SysFont("Arial", 16)
    header = pygame.font.SysFont("Arial", 20)
    FIGHTING_AGE = fightingAge
    FIGHTING_ENABLED = fightingEnabled
#Custom Lifeforms (not humans)
class LifeForm:
  def __init__(self, size=5, color=(255, 255, 255), hasHunger=True, hasThirst=True, name="LifeForm"):
    self.x = random.randint(0, SCREEN_WIDTH)
    self.y = random.randint(0, SCREEN_HEIGHT)
    if hasHunger:
        self.hunger = 0
    if hasThirst:
        self.thirst = 0
    self.color = color
    self.dead = False
    self.size = size
    self.name = name
    self.reproduced = False
  def move(self, foodList, waterList):
    #Find the closest food and water
    closestFood = None
    if len(foodList) > 0:
      for food in foodList:
        if closestFood == None:
          closestFood = food
        elif math.sqrt((self.x - food.x)**2 + (self.y - food.y)**2) < math.sqrt((self.x - closestFood.x)**2 + (self.y - closestFood.y)**2):
          closestFood = food
    closestWater = None
    if len(waterList) > 0:
      for water in waterList:
        if closestWater == None:
          closestWater = water
        elif math.sqrt((self.x - water.x)**2 + (self.y - water.y)**2) < math.sqrt((self.x - closestWater.x)**2 + (self.y - closestWater.y)**2):
          closestWater = water
    if self.thirst >= self.hunger:
      if closestWater != None:
        if self.x < closestWater.x:
          self.x += 1
        elif self.x > closestWater.x:
          self.x -= 1
        if self.y < closestWater.y:
          self.y += 1
        elif self.y > closestWater.y:
          self.y -= 1
    else:
      if closestFood != None:
        if self.x < closestFood.x:
          self.x += 1
        elif self.x > closestFood.x:
          self.x -= 1
        if self.y < closestFood.y:
          self.y += 1
        elif self.y > closestFood.y:
          self.y -= 1
    
    #Make sure the lifeform doesn't go off the screen
    if self.x < 0:
      self.x = 0
    if self.y < 0:
      self.y = 0
    if self.x > SCREEN_WIDTH:
      self.x = SCREEN_WIDTH
    if self.y > SCREEN_HEIGHT:
      self.y = SCREEN_HEIGHT
  def reproduce(self):
    lifeform = LifeForm(self.size, self.color, self.hasHunger, self.hasThirst, self.name)
    lifeform.x = self.x
    lifeform.y = self.y
    lifeform.size += random.randint(-1, 1)
    if lifeform.size < 1:
      lifeform.size = 1
    return lifeform
  def update(self, foodList, waterList, lifeformList):
    self.move(foodList, waterList)
    
    #If the lifeform is close enough to food or water, eat or drink.
    for food in foodList:
      if math.sqrt((self.x - food.x)**2 + (self.y - food.y)**2) < 5:
        self.hunger -= 10
        foodList.remove(food)
    for water in waterList:
      if math.sqrt((self.x - water.x)**2 + (self.y - water.y)**2) < 5:
        self.thirst -= 10
        waterList.remove(water)

    #Make sure hunger and thirst don't go below 0
    if self.hunger < 0:
      self.hunger = 0
    if self.thirst < 0:
      self.thirst = 0

    if self.hunger > 100:
      self.dead = True
    if self.thirst > 100:
      self.dead = True

    #if not hungry or thirsty, reproduce
    if self.hunger < 50 and self.thirst < 50:
      if random.randint(1, 5) == 1 and not self.reproduced:
        lifeform = self.reproduce()
        lifeformList.append(lifeform)
        self.reproduced = True
  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)