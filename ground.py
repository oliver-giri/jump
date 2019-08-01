from block import Block

class Ground(block):

    height = 30

    def __init__(self, xLeft, yUp, yVelocity, width, color):
        super().__init__(xLeft, yUp, 0, yVelocity, width, self.height, color)

    def checkDestroy(self):
        