import simulation
import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))
simulation.SCREEN_WIDTH = 600
simulation.SCREEN_HEIGHT = 600
simulation.font = pygame.font.SysFont("Arial", 16)
simulation.header = pygame.font.SysFont("Arial", 20)
simulation.tribeNames = ["The Tribe of the Gold", "The Tribe of the Silver", "The Tribe of the Bronze", "The Tribe of the Copper", "The Tribe of the Iron", "The Tribe of the Steel", "The Tribe of the Titanium", "The Tribe of the Platinum", "The Tribe of the Silver", "The Tribe of the Gold", "The Tribe of the Diamond", "The Tribe of the Emerald", "The Tribe of the Ruby", "The Tribe of the Sapphire", "The Tribe of the Amethyst", "The Tribe of the Topaz", "The Tribe of the Opal", "The Tribe of the Pearl", "The Tribe of the Jade", "The Tribe of the Obsidian", "The Tribe of the Onyx", "The Tribe of the Quartz", "The Tribe of the Lapis", "The Tribe of the Amber", "The Tribe of the Jade", "The Tribe of the Turquoise", "The Tribe of the Garnet", "The Tribe of the Peridot", "The Tribe of the Agate", "The Tribe of the Jasper", "The Tribe of the Malachite", "The Tribe of the Moonstone", "The Tribe of the Sunstone", "The Tribe of the Ametrine", "The Tribe of the Carnelian", "The Tribe of the Citrine", "The Tribe of the Hematite", "The Tribe of the Hemimorphite", "The Tribe of the Labradorite", "The Tribe of the Moonstone", "The Tribe of the Obsidian", "The Tribe of the Onyx", "The Tribe of the Quartz", "The Tribe of the Lapis", "The Tribe of the Amber", "The Tribe of the Jade", "The Tribe of the Turquoise", "The Tribe of the Garnet", "The Tribe of the Peridot", "The Tribe of the Agate", "The Tribe of the Jasper", "The Tribe of the Malachite", "The Tribe of the Moonstone", "The Tribe of the holy 69"]

from human import Human
from resources import *

class Owia(simulation.LifeForm):
    def __init__(self, target=None):
        super().__init__(color=(100, 0, 100, 100), hasHunger=False, hasThirst=False, size=10)
        self.target = target
        self.surface = pygame.Surface((self.size + 20, self.size + 20), pygame.SRCALPHA)
    def move(self):
        if self.target != None:
            if self.x < self.target.x:
                self.x += 1
            elif self.x > self.target.x:
                self.x -= 1
            if self.y < self.target.y:
                self.y += 1
            elif self.y > self.target.y:
                self.y -= 1
    def update(self):
        self.move()
        distanceToTarget = math.sqrt((self.x - self.target.x)**2 + (self.y - self.target.y)**2)
        if distanceToTarget < 5:
            if self.target in simulation.humanList:
                simulation.humanList.remove(self.target)
        for house in simulation.houseList:
            distanceToHouse = math.sqrt((self.x - house.x)**2 + (self.y - house.y)**2)
            if distanceToHouse < 20:
                simulation.houseList.remove(house)
        if len(simulation.humanList) > 0:
            self.target = simulation.humanList[0]
    def draw(self, screen):
        pygame.draw.circle(self.surface, self.color, (self.surface.get_width() / 2, self.surface.get_height() / 2), self.size)
        screen.blit(self.surface, (self.x, self.y))

clock = pygame.time.Clock()
HUNGER_THIRST_TICK = pygame.USEREVENT + 1
LIFE_TICK = pygame.USEREVENT + 2
HOUSE_COOLDOWN = pygame.USEREVENT + 3
pygame.time.set_timer(HUNGER_THIRST_TICK, 1000)
pygame.time.set_timer(LIFE_TICK, 2000)
pygame.time.set_timer(HOUSE_COOLDOWN, 500)
owia = None
for i in range(10):
    simulation.humanList.append(Human())
for i in range(100):
    simulation.foodList.append(Food())
    simulation.waterList.append(Water())
    simulation.woodList.append(Wood())
while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          food = Food()
          food.x = event.pos[0]
          food.y = event.pos[1]
          simulation.foodList.append(food)
        elif event.button == 2:
            human = Human()
            human.x = event.pos[0]
            human.y = event.pos[1]
            simulation.humanList.append(human)
        elif event.button == 3:
          water = Water()
          water.x = event.pos[0]
          water.y = event.pos[1]
          simulation.waterList.append(water)
      if event.type == HUNGER_THIRST_TICK:
        for human in simulation.humanList:
          human.hunger += 1
          human.thirst += 1
          if human.reproductionCooldown > 0:
            human.reproductionCooldown -= 1
      if event.type == LIFE_TICK:
        for human in simulation.humanList:
          human.age += 1
      if event.type == HOUSE_COOLDOWN:
        for human in simulation.humanList:
          if human.houseCooldown > 0:
            human.houseCooldown -= 1
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          sys.exit()
        if event.key == pygame.K_o:
            owia = Owia(target=simulation.humanList[0])
            owia.x = pygame.mouse.get_pos()[0]
            owia.y = pygame.mouse.get_pos()[1]
    for human in simulation.humanList:
      human.update()
    for tribe in simulation.tribeList:
      tribe.update()
    for house in simulation.houseList:
      house.update()
    if owia != None:
        owia.update()
    screen.fill((0, 0, 0))
    for food in simulation.foodList:
      food.draw(screen)
    for water in simulation.waterList:
      water.draw(screen)
    for wood in simulation.woodList:
      wood.draw(screen)
    for house in simulation.houseList:
      house.draw(screen)
    for human in simulation.humanList:
      human.draw(screen)
    if owia != None:
        owia.draw(screen)
    #Simulation Info
    bg = pygame.surface.Surface((simulation.SCREEN_WIDTH, 100))
    bg.fill((100, 100, 100))
    bg.set_alpha(150)
    screen.blit(bg, (0, 0))
    text = simulation.header.render("Simulation Info", True, (255, 255, 255))
    screen.blit(text, (10, 5))
    text = simulation.font.render("Humans: " + str(len(simulation.humanList)), True, (255, 255, 255))
    screen.blit(text, (10, 26))
    text = simulation.font.render("Tribes: " + str(len(simulation.tribeList)), True, (255, 255, 255))
    screen.blit(text, (10, 42))
    if len(simulation.tribeList) > 0:
        mostPowerfulTribe = simulation.tribeList[0]
        for tribe in simulation.tribeList:
            if len(tribe.members) > len(mostPowerfulTribe.members):
                mostPowerfulTribe = tribe
        text = simulation.font.render("Most Powerful Tribe: " + mostPowerfulTribe.name, True, (255, 255, 255))
        screen.blit(text, (10, 58))
        text = simulation.font.render("Most Powerful Tribe Power: " + str(mostPowerfulTribe.power), True, (255, 255, 255))
        screen.blit(text, (10, 74))
    pygame.display.flip()
