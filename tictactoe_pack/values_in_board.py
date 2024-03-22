from enum import Enum


class ValuesInBoard(Enum):
    X = "X"
    O = "O"
    EMPTY = "EMPTY"

    def __str__(self):
        return self.value
