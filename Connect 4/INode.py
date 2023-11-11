class INode:
    def __init__(self, board, depth, parent):
        self.board = board
        self.parent = parent
        self.depth = depth
        self.score = 0
        self.turn = 0


    #def expand(self):
        
        
        