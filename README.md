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
