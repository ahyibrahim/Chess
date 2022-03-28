import Controller

if __name__ == "__main__":
    chess = Controller.Controller()
    chess.board.print_board()

    # White starts first. turn = True : White, turn = False : Black
    turn = True

    while True:
        start = input("From: ")
        to = input("To: ")

        # Translate user input to coordinates
        start = chess.translate(start)
        to = chess.translate(to)

        if start == None or to == None:
            continue

        chess.move(start, to)

        # check for promotion pawns
        # i = 0
        # while i < 8:
        #     if not chess.turn and chess.board.board[0][i] != None and \
        #         chess.board.board[0][i].name == 'P':
        #         chess.promotion((0, i))
        #         break
        #     elif chess.turn and chess.board.board[7][i] != None and \
        #         chess.board.board[7][i].name == 'P':
        #         chess.promotion((7, i))
        #         break
        #     i += 1
        turn = not turn
        chess.board.print_board(turn)
