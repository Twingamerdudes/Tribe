# Tribe
![TribeLogo](https://user-images.githubusercontent.com/81382687/211170831-46c7b403-f169-4f8a-b4ce-542ead953e90.png)

Tribe is a open source library made in Python for the purpose of making simulations. It can be used to simulate humans, animals, and more!
Here's how to get started!
You can clone this repo and open it up in you're favorite IDE and make a new python script.

By the end of this, this script will be you're first simulation! Inside the file we need to import some stuff.
In the script type this:
```python
import simulation
import pygame
import sys
```
Make sure you have pygame installed as this requires it. If you don't have it, you can this command to install it: `pip install pygame`

Now we can initialize everything. First we will start up pygame and set up some settings for our simulation

```python
screen = simulation.init()
```
This initializes everything. We can also add parameters to change the simulation, like height and width. We can also set more complex parameters like the age
at when a human can fight with another human in a different tribe (population must also be above 20 for that to happen), or the possible names a tribe can have.

Here is a example of a customized init function:
```python
screen = simulation.init(width=800, height=600, fightingEnabled=False)
```
Now with our simulation initialized, we can setup our Simulation Loop!

In you're script, put the following lines of code after you're initialization code:
```python
clock = pygame.time.Clock()
HUNGER_THIRST_TICK = pygame.USEREVENT + 1
LIFE_TICK = pygame.USEREVENT + 2
HOUSE_COOLDOWN = pygame.USEREVENT + 3
pygame.time.set_timer(HUNGER_THIRST_TICK, 1000)
pygame.time.set_timer(LIFE_TICK, 2000)
pygame.time.set_timer(HOUSE_COOLDOWN, 500)
```
This setups our events that will need to be called in our game loop.
Now we can create the world! 

In you're program, add the following lines of code:
```python
from human import Human
from resources import *
for i in range(10):
    simulation.humanList.append(Human())
for i in range(100):
    simulation.foodList.append(Food())
    simulation.waterList.append(Water())
    simulation.woodList.append(Wood())
```
This creates 10 humans and some food, water, and wood. Pretty simple.
Now it is time for the main simulation loop.
```python
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
```
This handles all of the events, like the HUNGER_THIRST_TICK event. First we handle quitting the application which is pretty simple. We then handle the mouse down event which handles placing food, water, and humans. Now, remember those events we made earlier. Well, this is the code that executes them. HUNGER_THIRST_TICK just makes the life form hungier, thristier, and lowers it's reproduction cooldown. LIFE_TICK makes the human older, and HOUSE_COOLDOWN handles cooldowns when it comes to taking food
out of the house.

Now after that, we can update the humans, tribes, and houses. Aswell as drawing them to the screen along with some simulation info:
```python
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
```
Now you can run you're program. Congrats, you have just made you're first simulation! Now go on and explore Tribe even more. There are more life forms then just humans. Like bears and ants, well you can simulate them too by creating you're own Life Forms!!!!
