class INode:
    def __int__(self, board, depth, parent=None):
        self.board = board
        self.parent = parent
        self.depth = depth
        self.score = 0
        self.turn = 0


    #def expand(self):
        
        
        