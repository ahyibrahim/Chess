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

    def is_valid_move(self):
        pass

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)