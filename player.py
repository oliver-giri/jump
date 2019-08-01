from block import Block

class Player(Block):

    size = 20

    def __init__(self, color):
        super().__init__(390, 20, 0, 0, self.size, self.size, color)