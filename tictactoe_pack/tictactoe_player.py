from values_in_board import ValuesInBoard
from InvalidPlayerNumberError import InvalidPlayerNumberError
from tictactoe_game import Tictactoe
from InvalidMergePositionError import InvalidMergePositionError
from SpaceOccupiedError import SpaceOccupiedError


class TicTacToePlayer:
    player_id = 0
    player_sig = ValuesInBoard.EMPTY

    def __init__(self, player_id: int) -> None:
        if player_id > 2 or player_id < 0:
            raise InvalidPlayerNumberError("Invalid number of player")
        self.player_id = player_id
        self.set_player_sig(player_id)

    def get_player_sig(self):
        return self.player_sig

    def get_player_id(self):
        return self.player_id

    @staticmethod
    def valid_merge_space(my_game: Tictactoe, row: int, col: int):
        if my_game.board()[row][col] != ValuesInBoard.EMPTY:
            raise SpaceOccupiedError("merge is not empty!")

    def set_player_sig(self, player_id: int):
        if player_id == 1:
            self.player_sig = ValuesInBoard.X
        if player_id == 2:
            self.player_sig = ValuesInBoard.O

    def play_game(self, game: Tictactoe, row: int, column: int) -> None:
        game.board[row][column] = self.player_sig

    def single_play(self, game: Tictactoe, merge_number: int):
        if 0 < merge_number > 9:
            raise InvalidMergePositionError("merge number must be between 1 and 9")

        if merge_number == 1:
            self.play_game(game, 0, 0)
        if merge_number == 2:
            self.play_game(game, 0, 1)
        if merge_number == 3:
            self.play_game(game, 0, 2)
        if merge_number == 4:
            self.play_game(game, 1, 0)
        if merge_number == 5:
            self.play_game(game, 1, 1)
        if merge_number == 6:
            self.play_game(game, 1, 2)
        if merge_number == 7:
            self.play_game(game, 2, 0)
        if merge_number == 8:
            self.play_game(game, 2, 1)
        if merge_number == 9:
            self.play_game(game, 2, 2)
