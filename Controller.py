import Board
import Piece
import string


class Controller():
    """
    Put description of the Chess class here
    """

    def __init__(self):
        self.board = Board.Board()
        pass

    def promotion(self):
        # add any parameters necessary and replace the body with
        # functionality on promoting a Pawn that has reached the
        # end of the board
        print("Promoting Pawn")
        pass

    def move(self, start, to, color):
        selected_piece = self.board.board[start[0]][start[1]]
        if selected_piece == None or selected_piece.is_white() != color:
            return False
        self.board.board[start[0]][start[1]] = None
        self.board.board[to[0]][to[1]] = selected_piece
        self.board.flip_board()
        return True

    def translate(self, position):
        column_dict = dict(
            zip(list(string.ascii_lowercase)[0:8], list(range(0, 9))))
        if len(position) == 2 and position[0] in column_dict.keys() and int(position[1]) in list(range(1, 9)):
            return (int(position[1]) - 1, column_dict[position[0]])
        return None

    def locate(self, coord):
        column_dict = dict(
            zip(list(string.ascii_lowercase)[0:8], list(range(0, 9))))
        return "{}{}".format(self.get_key_from_value(coord[1], column_dict), coord[0] + 1)

    def get_key_from_value(self, val, dict):
        for key, value in dict.items():
            if val == value:
                return key

    def print_board(self):
        self.board.print_board()
