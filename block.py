class Block():

    def __init__(self, xLeft, yUp, xVelocity, yVelocity, width, height, color):
        self.xLeft = xLeft
        self.yUp = yUp
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.width = width
        self.height = height
        self.color = color
        self.shouldDestroy = False

    def move(self):
        self.xLeft += self.xVelocity
        self.yUp += self.yVelocity

    def checkDestroy(self):
        if self.yUp > 700:
            self.shouldDestroy = True
