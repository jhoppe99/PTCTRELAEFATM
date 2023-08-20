import numpy as np
import numpy.linalg as la
from typing import Any

K = 5
J = 1


class DiagonalsPreparation:

    def __init__(self, K) -> None:
        self.K = K

    def looping_over_k1(self):
        big_diagonal = []
        for k1 in range(0, self.K):
            big_diagonal.append(self.looping_over_k2(k1=k1))
        return big_diagonal

    def looping_over_k2(self, k1: int) -> list:
        small_diagonal = []
        for k2 in range(0, self.K):
            if k1 == k2:
                small_diagonal.append(self.equal_ks_equation(k1, k2))
            else:
                small_diagonal.append(self.not_equal_ks_equation(k1, k2))
        return small_diagonal

    def equal_ks_equation(self, k1: int, k2: int) -> int:
        eq = (k1 * 2) + (k2 * 3)
        return eq

    def not_equal_ks_equation(self, k1: int, k2: int) -> int:
        eq = (k1 * 100) - (k2 * 50)
        return eq


class MatrixesCreation:
    def __init__(self, diagonals: list) -> None:
        self.diagonals = diagonals

    def print_separate_lists(self):
        for k in range(0, len(self.diagonals)):
            print(self.diagonals[k])


tryout = DiagonalsPreparation(K=5)
print(tryout.looping_over_k1())
separate = MatrixesCreation(diagonals=tryout.looping_over_k1())
separate.print_separate_lists()
