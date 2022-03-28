# I added some helper functions here when I saw the same code logic repeated

class Piece():
    """
    Put description of the Piece class here
    """
    def __init__(self, color):
        self.color = color

    def is_valid_move(self):
        return False

    def is_white(self):
        return self.color

    def __str__(self):
        return ''
        


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"

    def is_valid_move(self, board, start, to):
        pass

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)



class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"


    def is_valid_move(self):
        pass

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)



class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"

    def is_valid_move(self):
        pass

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)



class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"

    def is_valid_move(self):
        pass

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)



class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "K"

    def is_valid_move(self):
        pass
    
    # I added an extra method for the King class
    def can_castle(self):
        pass

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)



class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"
        self.is_first_move = True

    def is_valid_move(self, start, to, board):
        #Horizontal Step or Two steps 
        if start[1] == to[1] and board[to[0]][to[1]] == None:
            if start[0] == to[0] + 1 or (start[0] == to[0] + 2 and self.is_first_move):
                self.is_first_move = False
                return True
        #Diagonal right or left one step kill
        if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
            if board[to[0]][to[1]] != None and board[to[0]][to[1]].color != self.color:
                self.is_first_move = False
                return True
        return False

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)