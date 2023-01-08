import simulation
import pygame
import sys

screen = simulation.init(width=800, height=600, fightingEnabled=False)
clock = pygame.time.Clock()
HUNGER_THIRST_TICK = pygame.USEREVENT + 1
LIFE_TICK = pygame.USEREVENT + 2
HOUSE_COOLDOWN = pygame.USEREVENT + 3
pygame.time.set_timer(HUNGER_THIRST_TICK, 1000)
pygame.time.set_timer(LIFE_TICK, 2000)
pygame.time.set_timer(HOUSE_COOLDOWN, 500)

from human import Human
from resources import *
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
    for human in simulation.humanList:
      human.update()
    for tribe in simulation.tribeList:
      tribe.update()
    for house in simulation.houseList:
      house.update()
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
