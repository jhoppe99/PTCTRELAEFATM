import pytest

import numpy as np

from computations.matrix_operations import calculate_determinant, get_round_determinant


def test_calculate_determinant() -> None:
    assert int(calculate_determinant(np.array([[4, 7], [5, 1]]))) == -31


def test_round_determinant() -> None:
    assert get_round_determinant(np.array([[7, 5], [12, 10]])) == 10
