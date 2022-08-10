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

    def check_diagonal_obstruction(self, start, to, board):
        n = start[0] = to[0]
        # Path is right diagonal
        if start[0] - to[0] == to[1] - start[1]:
            # Upper Diagonal
            if n > 0:
                pass
            # Lower Diagonal
            else:
                pass

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

    def is_valid_move(self, start, to, board):
        n = start[0] - to[0]
        if n == to[1] - start[1] or n == start[1] - to[1]:
            print(
                f"Piece said it was ok to move piece at {start} to {to}\n\tPiece Awaiting path validation")
        # print(f"N = {start[0] - to[0]}")
        # if start[0] - to[0] == to[1] - start[1]:
        #     print("UR Passed")
        # else:
        #     print("UR Failed")
        # if to[0] - start[0] == to[1] - start[1]:
        #     print("LR Passed")
        # else:
        #     print("LR Failed")
        # if start[0] - to[0] == start[1] - to[1]:
        #     print("UL Passed")
        # else:
        #     print("UL Failed")
        # if to[0] - start[0] == start[1] - to[1]:
        #     print("LL Passed")
        # else:
        #     print("LL Failed")
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
        # Horizontal Step or Two steps
        if start[1] == to[1] and board[to[0]][to[1]] == None:
            if start[0] == to[0] + 1 or (start[0] == to[0] + 2 and self.is_first_move and board[to[0] + 1][to[1]] == None):
                self.is_first_move = False
                return True
        # Diagonal right or left one step kill
        if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
            if board[to[0]][to[1]] != None and board[to[0]][to[1]].color != self.color:
                self.is_first_move = False
                return True
        return False

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.name)
