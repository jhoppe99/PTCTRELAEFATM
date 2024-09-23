import math
import logging

import numpy as np


_logger = logging.getLogger(__name__)


def calculate_determinant(arr: np.array) -> float:
    if len(arr.shape) == 1:
        return arr[0][0]
    determinant = np.linalg.det(arr)
    return determinant


def get_round_determinant(arr: np.array, decimals=0) -> int:
    multiplier = 10 ** decimals
    determinant = calculate_determinant(arr)
    return int(math.floor(determinant*multiplier + 0.5) / multiplier)
