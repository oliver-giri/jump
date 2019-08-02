from block import Block

class Player(Block):

    size = 20

    def __init__(self, color):
        super().__init__(390, 20, 0, 0, self.size, self.size, color)

    def applyGravity(self, gravity):
        self.yVelocity += gravity

    def jump(self, distance):
        self.yVelocity = distance*-1
        self.yUp += self.yVelocity
