import numpy as np


class Snake:
    def __init__(self,
                 startCell,
                 len: int,
                 mat: np.matrix
                 ) -> None:
        self.startCell = startCell
        self.len = len
        self.posC = startCell[1]
        self.posR = startCell[0]
        self.maxC = mat.shape[1]
        self.maxR = mat.shape[0]
        self.mat = mat
        self.moves = []
        mat[startCell] = -10002

    def left(self):
        if self.posC == 0:
            return self.posR, self.maxC - 1
        else:
            return self.posR, self.posC - 1

    def right(self):
        if self.posC == self.maxC - 1:
            return self.posR, 0
        else:
            return self.posR, self.posC + 1

    def up(self):
        if self.posR == 0:
            return self.maxR - 1, self.posC
        else:
            return self.posR - 1, self.posC

    def down(self):
        if self.posR == self.maxR - 1:
            return 0, self.posC
        else:
            return self.posR + 1, self.posC

    def move(self, move):
        if move == "L":
            self.posR, self.posC = self.left()
        elif move == "R":
            self.posR, self.posC = self.right()
        elif move == "D":
            a = self.down()
            self.posR, self.posC = self.down()
        elif move == "U":
            self.posR, self.posC = self.up()
        else:
            raise Exception("invalid move")

        self.moves.append(move)

    def greedy_move(self, matrix):
        best_move = "L"
        new_pos = self.left()
        max = matrix[new_pos]

        if matrix[self.right()] > max:
            best_move = "R"
            new_pos = self.right()

        if matrix[self.up()] > max:
            best_move = "U"
            new_pos = self.up()

        if matrix[self.down()] > max:
            best_move = "D"
            new_pos = self.down()

        if max == -10002 or max == -10001:
            return None, None

        return best_move, new_pos
