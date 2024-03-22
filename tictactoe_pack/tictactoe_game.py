from values_in_board import ValuesInBoard


class Tictactoe:
    def __init__(self):
        self.board = [[ValuesInBoard.EMPTY] * 3] * 3

    def get_board(self):
        return self.board

    def show_board(self):
        the_board = [list(x) for x in self.board]
        for row in the_board:
            print(row)



