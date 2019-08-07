from GameObject import GameObject

class Plant(GameObject):
    def __init__(self, x, y, image, nutritionalValue, game):
        self.x = x
        self.y = y
        self.image = image
        self.nutritionalValue = nutritionalValue
        self.game = game

    def update(self):
        if self.nutritionalValue <= 0:
            self.game.removePlant(self)

    def getNutritionalValue(self):
        return self.nutritionalValue

