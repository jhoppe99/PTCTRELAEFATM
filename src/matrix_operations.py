import numpy as np
import math


class DetOfMatrixCalculation:
    def __init__(self, arr: np.array) -> None:
        self.arr = arr

    def calculate_determinant(self) -> float:
        determinant = np.linalg.det(self.arr)
        return determinant

    def round_determinant(self, decimals=0) -> int:
        multiplier = 10 ** decimals
        determinant = self.calculate_determinant()
        return int(math.floor(determinant*multiplier + 0.5) / multiplier)
