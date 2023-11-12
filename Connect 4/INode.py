class INode:
    def __init__(self, board, depth, parent):
        self.board = board
        self.parent = parent
        self.depth = depth
        self.children = []
        self.score = 0


    #def expand(self):
        
        
        