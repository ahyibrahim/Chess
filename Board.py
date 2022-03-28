from re import T
from typing import Tuple
from colorama import Fore, Back, Style
import Piece


class Board():
    """
    Put description of the Board class here
    """

    def __init__(self):
        self.board = []

        # Initialize empty board
        for count in range(8):
            self.board.append([None] * 8)

        # Initialize Black Pieces
        self.board[7][0] = Piece.Rook(True)
        self.board[7][-1] = Piece.Rook(True)
        self.board[7][1] = Piece.Knight(True)
        self.board[7][-2] = Piece.Knight(True)
        self.board[7][2] = Piece.Bishop(True)
        self.board[7][-3] = Piece.Bishop(True)
        self.board[7][3] = Piece.Queen(True)
        self.board[7][-4] = Piece.King(True)
        for i, pos in enumerate(self.board[6]):
            self.board[6][i] = Piece.Pawn(True)

         # Initialize White Pieces
        self.board[0][0] = Piece.Rook(False)
        self.board[0][-1] = Piece.Rook(False)
        self.board[0][1] = Piece.Knight(False)
        self.board[0][-2] = Piece.Knight(False)
        self.board[0][2] = Piece.Bishop(False)
        self.board[0][-3] = Piece.Bishop(False)
        self.board[0][3] = Piece.Queen(False)
        self.board[0][-4] = Piece.King(False)
        for i, pos in enumerate(self.board[1]):
            self.board[1][i] = Piece.Pawn(False)

        self.color = True

    def print_board(self):
        print("  ", "_" * 10 * 4)
        for i, row in enumerate(self.board):
            print(i+1, end="  ")
            for piece in row:
                if piece == None:
                    print(f'|    ', end="")
                elif not piece.is_white():
                    print('| ' + Fore.BLUE + f'{piece} ' + Fore.WHITE, end="")
                else:
                    print(f'| {piece} ', end="")
            print("|")
        print("  ", "-" * 10 * 4, end="\n      ")
        column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for name in column_names:
            print(name, end="    ")
        print("")

    def flip_board(self, to_color):
        if self.color != to_color:
            self.color = to_color
            self.board = self.board.reverse()
