class GameObject:

    def __init__(self, x, y, image, gameObjects, plants):
        self.x = x
        self.y = y
        self.image = image
        self.gameObjects = gameObjects
        self.plants = plants

    def update(self):
        raise NotImplementedError("Please Implement this method")

    def getImage(self):
        return self.image

    def getX(self):
        return self.x

    def getY(self):
        return self.y