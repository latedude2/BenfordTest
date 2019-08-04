from GameObject import GameObject

class Plant(GameObject):
    def __init__(self, x, y, image, nutritionalValue, gameObjects, plants):
        self.x = x
        self.y = y
        self.image = image
        self.nutritionalValue = nutritionalValue
        self.gameObjects = gameObjects
        self.plants = plants

    def update(self):
        if self.nutritionalValue <= 0:
            self.gameObjects.remove(self)

    def getNutritionalValue(self):
        return self.nutritionalValue

