from simulation import *
from resources import *
from tribe import Tribe
from house import House
class Human:
  #Initlaztion shit
  def __init__(self):
    self.x = random.randint(0, SCREEN_WIDTH)
    self.y = random.randint(0, SCREEN_HEIGHT)
    self.color = (255, 255, 255)
    self.hunger = 0
    self.thirst = 0
    self.speed = 1
    self.reproductionCooldown = 0
    self.age = 0
    self.wood = 0
    self.hasHouse = False
    self.house = None
    self.holdingFood = False
    self.findingFood = False
    self.houseCooldown = 0
    self.tribe = None
    self.raiding = False
    self.houseRaiding = None
    self.mate = None
    self.fightingAge = FIGHTING_AGE

  #Draw the human to the screen.
  def draw(self, screen):
    if self.tribe != None:
      self.color = (self.tribe.color[0] - 50, self.tribe.color[1] - 50, self.tribe.color[2] - 50)
      if self.color[0] < 0:
        self.color = (0, self.color[1], self.color[2])
      if self.color[1] < 0:
        self.color = (self.color[0], 0, self.color[2])
      if self.color[2] < 0:
        self.color = (self.color[0], self.color[1], 0)
    else:
        self.color = (255, 255, 255)
    pygame.draw.circle(screen, self.color, (self.x, self.y), 5)
  
  #Handles movement logic of the human.
  def move(self):
    #Find the closest food and water
    closestFood = None
    for food in foodList:
      if closestFood == None:
        closestFood = food
      else:
        if math.sqrt((food.x - self.x)**2 + (food.y - self.y)**2) < math.sqrt((closestFood.x - self.x)**2 + (closestFood.y - self.y)**2):
          closestFood = food
    closestWater = None
    for water in waterList:
      if closestWater == None:
        closestWater = water
      else:
        if math.sqrt((water.x - self.x)**2 + (water.y - self.y)**2) < math.sqrt((closestWater.x - self.x)**2 + (closestWater.y - self.y)**2):
          closestWater = water
    
    #Is it hungry or thirsty?
    if self.hunger > 20 and self.thirst > 20:
      if self.hunger > self.thirst:
        #Does it have a house? Should it go to it?
        if self.hasHouse == True and self.house.foodCount > 0 and math.sqrt((self.house.x - self.x)**2 + (self.house.y - self.y)**2) < math.sqrt((closestFood.x - self.x)**2 + (closestFood.y - self.y)**2):
          if self.x < self.house.x:
            self.x += self.speed
          elif self.x > self.house.x:
            self.x -= self.speed
          if self.y < self.house.y:
            self.y += self.speed
          elif self.y > self.house.y:
            self.y -= self.speed
        else:
          if closestFood != None:
            if self.x < closestFood.x:
              self.x += self.speed
            elif self.x > closestFood.x:
              self.x -= self.speed
            if self.y < closestFood.y:
              self.y += self.speed
            elif self.y > closestFood.y:
              self.y -= self.speed
      else:
        #If the human is thirsty, go to the closest water
        if closestWater != None:
          if self.x < closestWater.x:
            self.x += self.speed
          elif self.x > closestWater.x:
            self.x -= self.speed
          if self.y < closestWater.y:
            self.y += self.speed
          elif self.y > closestWater.y:
            self.y -= self.speed
    #If the human isn't hungry or thirsty and can't reproduce, build a house, or find food for it's house
    elif self.hunger < 20 and self.thirst < 20 and self.reproductionCooldown != 0 or self.age < 18:      
      if self.hasHouse == False:
        #Find wood to build a house
        closestWood = None
        for wood in woodList:
          if closestWood == None:
            closestWood = wood
          else:
            if math.sqrt((wood.x - self.x)**2 + (wood.y - self.y)**2) < math.sqrt((closestWood.x - self.x)**2 + (closestWood.y - self.y)**2):
              closestWood = wood
        
        if closestWood != None:
          if self.x < closestWood.x:
            self.x += self.speed
          elif self.x > closestWood.x:
            self.x -= self.speed
          if self.y < closestWood.y:
            self.y += self.speed
          elif self.y > closestWood.y:
            self.y -= self.speed
      else:
        #If it needs to find food to bring to it's house
        if self.holdingFood == False:
            closestDistance = float("inf")
            self.houseRaiding = None
            closestFood = None

            if self.tribe != None:
              #Should it raid a house?
              for food in foodList:
                if closestFood == None:
                  closestFood = food
                else:
                  if math.sqrt((food.x - self.x)**2 + (food.y - self.y)**2) < math.sqrt((closestFood.x - self.x)**2 + (closestFood.y - self.y)**2):
                    closestFood = food
              
              for house in houseList:
                  if house.tribe != self.tribe and house.foodCount > 0 and self.house != house:
                      distance = math.sqrt((house.x - self.x)**2 + (house.y - self.y)**2)
                      if distance < closestDistance:
                          closestDistance = distance
                          self.houseRaiding = house
              if self.houseRaiding != None and self.houseRaiding.foodCount > 0 and closestDistance < math.sqrt((closestFood.x - self.x)**2 + (closestFood.y - self.y)**2):
                  self.raiding = True
            else:
              for food in foodList:
                if closestFood == None:
                  closestFood = food
                else:
                  if math.sqrt((food.x - self.x)**2 + (food.y - self.y)**2) < math.sqrt((closestFood.x - self.x)**2 + (closestFood.y - self.y)**2):
                    closestFood = food
            #Go to the where the closest food is or the house it's raiding
            if self.tribe != None:
                if not self.raiding:
                  if closestFood != None:
                    if self.x < closestFood.x:
                      self.x += self.speed
                    elif self.x > closestFood.x:
                      self.x -= self.speed
                    if self.y < closestFood.y:
                      self.y += self.speed
                    elif self.y > closestFood.y:
                      self.y -= self.speed
                  self.findingFood = True
                else:
                    if self.houseRaiding != None:
                        if self.x < self.houseRaiding.x:
                            self.x += self.speed
                        elif self.x > self.houseRaiding.x:
                            self.x -= self.speed
                        if self.y < self.houseRaiding.y:
                            self.y += self.speed
                        elif self.y > self.houseRaiding.y:
                            self.y -= self.speed
            else:
                if closestFood != None:
                    if self.x < closestFood.x:
                      self.x += self.speed
                    elif self.x > closestFood.x:
                      self.x -= self.speed
                    if self.y < closestFood.y:
                      self.y += self.speed
                    elif self.y > closestFood.y:
                      self.y -= self.speed
                self.findingFood = True
        else:
          #Bring the food back to the house
          if self.x < self.house.x:
            self.x += self.speed
          elif self.x > self.house.x:
            self.x -= self.speed
          if self.y < self.house.y:
            self.y += self.speed
          elif self.y > self.house.y:
            self.y -= self.speed

          distance = math.sqrt((self.house.x - self.x)**2 + (self.house.y - self.y)**2)
          if distance < 10:
            self.holdingFood = False
            self.house.foodCount += 1
            self.findingFood = False
            self.houseCooldown = 10
    elif self.age >= 18 and self.reproductionCooldown == 0:
      #It's fucking time! (God dammit)
      for human in humanList:
        if human != self:
          if self.mate == None:
            self.mate = human
          else:
            if math.sqrt((human.x - self.x)**2 + (human.y - self.y)**2) < math.sqrt((self.mate.x - self.x)**2 + (self.mate.y - self.y)**2):
              self.mate = human
      if self.mate != None:
        if self.x < self.mate.x:
          self.x += self.speed
        elif self.x > self.mate.x:
          self.x -= self.speed
        if self.y < self.mate.y:
          self.y += self.speed
        elif self.y > self.mate.y:
          self.y -= self.speed
    else:
      #If it has nothing else to do, find food and water. This else statment is rarly triggered.
      if self.hunger > self.thirst:
        if closestFood != None:
          if self.x < closestFood.x:
            self.x += self.speed
          elif self.x > closestFood.x:
            self.x -= self.speed
          if self.y < closestFood.y:
            self.y += self.speed
          elif self.y > closestFood.y:
            self.y -= self.speed
      else:
        if closestWater != None:
          if self.x < closestWater.x:
            self.x += self.speed
          elif self.x > closestWater.x:
            self.x -= self.speed
          if self.y < closestWater.y:
            self.y += self.speed
          elif self.y > closestWater.y:
            self.y -= self.speed
    
    #Bound the human to the screen
    if self.x < 0:
      self.x = 0
    if self.y < 0:
      self.y = 0
    if self.x > SCREEN_WIDTH:
      self.x = SCREEN_WIDTH
    if self.y > SCREEN_HEIGHT:
        self.y = SCREEN_HEIGHT
  
    #If the human is near the house it's raiding, take the food
    if self.raiding and self.houseRaiding != None:
        if math.sqrt((self.houseRaiding.x - self.x)**2 + (self.houseRaiding.y - self.y)**2) < 10:
            self.raiding = False
            self.houseRaiding.foodCount -= 1
            self.holdingFood = True
            self.findingFood = False
  def eat(self):
    #Allows the human to eat food, or get food from it's house
    if self.hasHouse == True and self.houseCooldown == 0:
      if self.hunger > 20:
        #Make sure the house has enough food
        if self.house.foodCount > 0:
          if math.sqrt((self.house.x - self.x)**2 + (self.house.y - self.y)**2) < 50:
            self.hunger += 10
            self.house.foodCount -= 1
    for food in foodList:
      if math.sqrt((food.x - self.x)**2 + (food.y - self.y)**2) < 10:

        #If it is not finding food for it's house.
        if not self.findingFood:
          self.hunger -= 10
          foodList.remove(food)
          foodList.append(Food())
        else:
          self.findingFood = False
          self.holdingFood = True
          foodList.remove(food)
          foodList.append(Food())
  def drink(self):
    #If the human is close enough to some water, it drinks it.
    for water in waterList:
      if math.sqrt((water.x - self.x)**2 + (water.y - self.y)**2) < 10:
        self.thirst -= 10
        waterList.remove(water)
        waterList.append(Water())
  def collectWood(self):
    #If the human is close enough to a wood pile, it collects the wood.
    for wood in woodList:
      if math.sqrt((wood.x - self.x)**2 + (wood.y - self.y)**2) < 10:
        self.wood += 10
        woodList.remove(wood)
        woodList.append(Wood())
  def buildHouse(self):
    #Makes the human build a house if it has enough wood and does not already have a house
    if self.wood >= 50 and self.hasHouse == False:
      self.wood -= 50
      self.house = House()
      self.house.x = self.x + 20
      self.house.y = self.y + 20
      
      #Make sure the house is not outside the screen
      if self.house.x > SCREEN_WIDTH:
        self.house.x = SCREEN_WIDTH - 50
      if self.house.y > SCREEN_HEIGHT:
        self.house.y = SCREEN_HEIGHT - 50

      self.house.owner = self

      #Create the house
      houseList.append(self.house)
      self.hasHouse = True
      self.house.tribe = self.tribe
  
  def reproduce(self):
    #Makes the human reprouce if it is old enough, has enough food and water, and has not recently reprouced
    if self.hunger < 50 and self.thirst < 50 and self.reproductionCooldown == 0 and self.age >= 18:
      human = Human()
      human.x = self.x + 5
      human.y = self.y + 5
      human.tribe = self.tribe

      #Mutate the baby
      human.speed += random.uniform(-0.5,0.5)
      human.fightingAge += random.randint(-1,1)

      #Add the baby to the world
      humanList.append(human)
      self.reproductionCooldown = 10
  def update(self):
    #update loop, called every frame. Handles movement, eating, drinking, building, reproducing, and dying
    self.move()
    self.eat()
    self.drink()
    self.collectWood()
    self.buildHouse()

    #Makes the human die if it starves or dehydrates
    if self.hunger > 100:
      if self in humanList:
        humanList.remove(self)
        if self.tribe != None and self in self.tribe.members:
            self.tribe.members.remove(self)
            self.tribe = None
    if self.thirst > 100:
      if self in humanList:
        humanList.remove(self)
        if self.tribe != None:
            self.tribe.members.remove(self)
            self.tribe = None

    #Make sure the human's hunger and thirst are not negative
    if self.hunger < 0:
      self.hunger = 0
    if self.thirst < 0:
      self.thirst = 0

    #replicate if you are old enough and have a mate
    if self.mate != None:
      if math.sqrt((self.mate.x - self.x)**2 + (self.mate.y - self.y)**2) < 10:
        self.reproduce()

    #Tribe creation
    for human in humanList:
        if human != self:
            #If the human is close enough to the other human to create a tribe with
            if math.sqrt((human.x - self.x)**2 + (human.y - self.y)**2) < 20:
                if human.tribe == None and self.tribe == None:
                    #Creates the tribe
                    tribe = Tribe()
                    tribe.members.append(self)
                    tribe.members.append(human)
                    self.tribe = tribe
                    human.tribe = tribe
                    tribeList.append(tribe)
                elif self.tribe != None and human.tribe == None:
                    #Allows the human to spread the tribe's influence
                    if random.randint(0, 3) == 0:
                        #add the human to the tribe
                        self.tribe.members.append(human)
                        human.tribe = self.tribe
                elif self.tribe == None and human.tribe != None:
                    #Allows another human to spread the tribe's influence
                    if random.randint(0, 3) == 0:
                        human.tribe.members.append(self)
                        self.tribe = human.tribe
                        if self.hasHouse == True:
                            self.house.tribe = self.tribe
                elif self.tribe != None and human.tribe != None:
                    #Allows human's of oppisite tribes to fight
                    if self.tribe != human.tribe and self.age > self.fightingAge and human.age > self.fightingAge and len(humanList) > 20 and FIGHTING_ENABLED:
                        #Outcome based on a random number
                        if random.randint(0, 4) <= 2:
                          if human in humanList:
                            humanList.remove(human)
                            human.tribe.members.remove(human)
                            human.tribe = None
                        else:
                          if self in humanList:
                            humanList.remove(self)
                            self.tribe.members.remove(self)
                            self.tribe = None