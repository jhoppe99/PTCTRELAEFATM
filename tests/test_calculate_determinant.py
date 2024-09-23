import numpy as np

from computations.matrix_operations import DetOfMatrixCalculation


def test_calculate_determinant() -> None:
    det = DetOfMatrixCalculation(arr=np.array([
        [4, 7],
        [5, 1]
    ]))
    assert int(det.calculate_determinant()) == -31


def test_round_determinant() -> None:
    det = DetOfMatrixCalculation(arr=np.array([
        [7, 5],
        [12, 10]
    ]))
    assert det.round_determinant() == 10
