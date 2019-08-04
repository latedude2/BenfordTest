from GameObject import GameObject
from Plant import  Plant
import math
class Rabbit(GameObject):
    eatingSpeed = 2
    deathHunger = 1000
    starvationSpeed = 0.2

    def __init__(self, x, y, image, speed, gameObjects, plants):
        self.x = x
        self.y = y
        self.image = image
        self.hunger = 200
        self.speed = speed
        self.gameObjects = gameObjects
        self.plants = plants

    def increaseHunger(self):
        self.hunger = self.hunger + self.starvationSpeed

    def run(self, targetX, targetY):
        if targetX < self.x:
            self.x = self.x - self.speed
        else:
            self.x = self.x + self.speed

        if targetY < self.y:
            self.y = self.y - self.speed
        else:
            self.y = self.y + self.speed

    def eat(self):
        if self.distance(self.target) < 50:
            self.target.nutritionalValue = self.target.nutritionalValue - self.eatingSpeed
            self.hunger = self.hunger - self.eatingSpeed
            if(self.target.getNutritionalValue() <= 0):
                self.target = self.findTarget(self.plants)


    def findTarget(self, plants):
         if self.hunger > 100:
             self.target = plants[0]
             for i in range(0, plants.__len__()):
                 if self.distance(plants[i]) < self.distance(self.target):
                     if(plants[i].getNutritionalValue() >= 0):
                        self.target = plants[i]
         else:
             pass


    def update(self):
        self.increaseHunger()
        self.findTarget(self.plants)
        if self.target is None:
            pass
        else:
            self.run(self.target.getX(), self.target.getY())
            self.eat()

        if self.hunger > self.deathHunger:
            self.gameObjects.remove(self)

    def distance(self, gameObject):
        return math.sqrt((self.x - gameObject.x) ** 2 + (self.y - gameObject.y) ** 2)

    def getTarget(self):
        return self.target



