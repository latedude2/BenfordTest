import pygame
import random
from Plant import Plant
from Rabbit import Rabbit
from pygame.locals import *
image = pygame.image.load("test.png")
plantImage = pygame.image.load("plant.png")
rabbitImage = pygame.image.load("rabbit.png")
gameObjects = []
plants = []
rabbits = []

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1600, 900

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        for i in range(0, 10):
            plants.append(Plant(random.randint(100, 1500), random.randint(100, 800), plantImage, random.randint(200, 300), self))
        for i in range (0,2):
            rabbits.append(Rabbit(random.randint(100, 1500), random.randint(100, 800), rabbitImage, 0.25, self))

        gameObjects.extend(rabbits)
        gameObjects.extend(plants)


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        gameObjects.clear()
        gameObjects.extend(plants)
        gameObjects.extend(rabbits)
        i = 0
        while i < gameObjects.__len__():
            gameObjects[i].update()
            i = i + 1


    def on_render(self):
        self._display_surf.fill([0, 200, 0])
        for i in range(0, gameObjects.__len__()):
            self._display_surf.blit(gameObjects[i].getImage(), (gameObjects[i].getX(), gameObjects[i].getY()))
        pygame.display.flip()
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()




    def getPlants(self):
        return plants

    def removePlant(self, plant):
        plants.remove(plant)

    def removeRabbit(self, rabbit):
        rabbits.remove(rabbit)

    def getGameObjects(self):
        return gameObjects


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()