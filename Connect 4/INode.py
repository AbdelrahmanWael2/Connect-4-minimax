import math


class INode:
    def __init__(self, board, depth, parent, alpha=-math.inf, beta=math.inf):
        self.board = board
        self.parent = parent
        self.depth = depth
        self.children = []
        self.score = 0
        self.alpha = alpha
        self.beta = beta

    # def expand(self):
