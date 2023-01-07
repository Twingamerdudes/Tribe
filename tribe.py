from simulation import tribeNames, tribeList, houseList
import random
#Handles tribes
class Tribe:
  #Initlaztion shit
  def __init__(self):
    self.members = []
    self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    self.power = 0
    self.name = random.choice(tribeNames)
  def update(self):
    #Calculate teh tribe's power based on how many members it has and the amount of food is stored across all houses
    self.power = 0
    self.power += len(self.members)
    for house in houseList:
        if house.tribe == self:
            self.power += house.foodCount
    self.power = self.power / 2

    #Remove the tribe if it has no members
    if len(self.members) == 0:
        tribeList.remove(self)